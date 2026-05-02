#!/usr/bin/env python3
"""
normalize_case.py — Build-time tool that clones the three source awesome
repos, walks their markdown trees, and writes one normalized case file per
prompt to `prompts/case-library/from-{repo-slug}/{slug}.md`.

This is NOT a runtime dependency. Run it once per release to refresh the
case library.

Usage:
    python3 scripts/normalize_case.py [--source-dir /tmp/awesome-source]
                                      [--output-dir prompts/case-library]
                                      [--no-clone]   # skip git clone, reuse existing source-dir

Output:
    - prompts/case-library/from-awesome-gpt-image-2-prompts/*.md
    - prompts/case-library/from-awesome-gpt-image-2/*.md
    - prompts/case-library/from-awesome-seedance-2-guide/*.md
    - prompts/case-library/INDEX.md
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable

# ---------------------------------------------------------------- repos


REPOS = [
    {
        "slug": "awesome-gpt-image-2-prompts",
        "url": "https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts.git",
        "credit": "EvoLinkAI",
        "default_workflow": "text2image",
        "default_model": "openai/gpt-image-2",
    },
    {
        "slug": "awesome-gpt-image-2",
        "url": "https://github.com/freestylefly/awesome-gpt-image-2.git",
        "credit": "freestylefly",
        "default_workflow": "image2image",
        "default_model": "openai/gpt-image-2",
    },
    {
        "slug": "awesome-seedance-2-guide",
        "url": "https://github.com/EvoLinkAI/awesome-seedance-2-guide.git",
        "credit": "EvoLinkAI",
        "default_workflow": "image2video",
        "default_model": "bytedance/seedance-2.0-fast",
    },
]


# ---------------------------------------------------------------- helpers


SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = SLUG_RE.sub("-", s)
    return s.strip("-") or "untitled"


def yaml_escape(s: str) -> str:
    return s.replace('"', '\\"').replace("\n", " ").strip()


# ---------------------------------------------------------------- model


@dataclass
class Case:
    title: str
    source_repo: str
    source_url: str
    credit: str
    workflow: str  # text2image | image2image | text2video | image2video
    model: str
    prompt: str
    tags: list[str] = field(default_factory=list)
    inputs: dict = field(default_factory=dict)
    notes: str = ""

    def slug(self) -> str:
        return slugify(self.title)


# ---------------------------------------------------------------- parsing


# A "case" is loosely any markdown section that contains a quoted prompt
# block. Different repos format these differently — these regexes cover
# the common patterns we observed.
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
FENCED_PROMPT_RE = re.compile(r"```(?:prompt|text|md|markdown)?\s*\n(.*?)\n```", re.DOTALL)
QUOTED_PROMPT_RE = re.compile(r"^>\s+(.+?)(?=\n[^>]|\Z)", re.DOTALL | re.MULTILINE)


# Tag heuristics — keywords that route a case under one of our v1 / v1.1
# command tags so SKILL.md can grep the case-library for inspiration.
TAG_KEYWORDS = {
    "headshot": ["headshot", "portrait", "id photo", "linkedin", "证件照", "肖像", "头像"],
    "dance": ["dance", "dancing", "choreography", "舞蹈", "跳舞"],
    "poster": ["poster", "key art", "movie", "film", "cover", "海报", "片单"],
    "ghibli": ["ghibli", "miyazaki", "吉卜力", "宫崎"],
    "character-sheet": ["character sheet", "three-view", "9-grid", "9宫格", "三视图", "角色设定"],
    "ui-system": ["ui", "app", "dashboard", "interface", "screen", "界面", "ui设计"],
    "lookbook": ["lookbook", "fashion", "outfit", "搭配", "穿搭"],
    "ad-series": ["ad", "advertising", "campaign", "creative", "广告"],
    "card-deck": ["card", "tarot", "trading card", "deck", "卡牌", "塔罗"],
    "unbox": ["unbox", "reveal", "product", "开箱"],
    "logo-3d": ["logo", "3d render", "brand mark"],
    "infographic": ["infographic", "diagram", "数据可视化"],
    "isometric": ["isometric", "axonometric", "等距"],
    "food": ["food", "cuisine", "美食", "餐桌"],
    "anime": ["anime", "manga", "二次元", "动漫"],
    "kpop": ["kpop", "k-pop", "idol"],
    "sci-fi": ["sci-fi", "cyberpunk", "futuristic", "科幻", "赛博"],
    "fantasy": ["fantasy", "wizard", "dragon", "魔法"],
    "minimalist": ["minimalist", "minimal", "极简"],
}


def detect_tags(prompt: str, title: str) -> list[str]:
    blob = (title + " " + prompt).lower()
    hit = []
    for tag, kws in TAG_KEYWORDS.items():
        if any(kw in blob for kw in kws):
            hit.append(tag)
    return hit


def detect_workflow(prompt: str, fallback: str) -> str:
    p = prompt.lower()
    has_image_input = any(
        kw in p
        for kw in [
            "image of",
            "this image",
            "the photo",
            "input image",
            "reference image",
            "source image",
            "based on the image",
            "图片中",
            "参考图",
            "原图",
        ]
    )
    is_video = any(
        kw in p
        for kw in [
            "video",
            "animation",
            "seconds",
            "5 sec",
            "8 sec",
            "动画",
            "视频",
            "镜头",
            "运动",
        ]
    )

    if is_video and has_image_input:
        return "image2video"
    if is_video:
        return "text2video"
    if has_image_input:
        return "image2image"
    return fallback


def detect_model(workflow: str, fallback: str) -> str:
    if workflow in ("text2video", "image2video"):
        return "bytedance/seedance-2.0-fast"
    return fallback or "openai/gpt-image-2"


def extract_cases_from_markdown(text: str, repo: dict, source_url: str) -> Iterable[Case]:
    """
    Walk the markdown headings; for each heading, capture the body until the
    next heading of equal-or-shallower depth, then look for the first prompt
    block in that body.
    """
    headings = list(HEADING_RE.finditer(text))
    if not headings:
        return

    for idx, m in enumerate(headings):
        depth = len(m.group(1))
        title = m.group(2).strip()
        if depth == 1:
            # repo top-level title — skip
            continue
        body_start = m.end()
        # find next heading of depth <= this depth
        body_end = len(text)
        for nxt in headings[idx + 1 :]:
            if len(nxt.group(1)) <= depth:
                body_end = nxt.start()
                break
        body = text[body_start:body_end]

        prompt_match = FENCED_PROMPT_RE.search(body)
        if prompt_match:
            prompt = prompt_match.group(1).strip()
        else:
            quoted = QUOTED_PROMPT_RE.search(body)
            if quoted:
                prompt = re.sub(r"^>\s?", "", quoted.group(0), flags=re.MULTILINE).strip()
            else:
                continue  # no prompt found in this section

        # require a meaningful prompt (>= 30 chars)
        if len(prompt) < 30:
            continue

        workflow = detect_workflow(prompt, repo["default_workflow"])
        model = detect_model(workflow, repo["default_model"])
        tags = detect_tags(prompt, title)

        yield Case(
            title=title[:120],
            source_repo=repo["slug"],
            source_url=source_url,
            credit=repo["credit"],
            workflow=workflow,
            model=model,
            prompt=prompt,
            tags=tags,
            inputs={"text": True} if workflow.startswith("text") else {"image": "user-supplied"},
        )


LANG_README_RE = re.compile(r"^readme\.[a-z][a-z0-9\-]+\.md$", re.IGNORECASE)
SKIP_NAMES = {"license.md", "contributing.md", "changelog.md", "code_of_conduct.md", "code-of-conduct.md"}


def walk_repo(repo_dir: Path, repo: dict) -> Iterable[Case]:
    """Walk *.md files in the repo and yield cases. Skip language-variant
    READMEs (README.zh-CN.md, README.ja.md, etc.) to avoid translation
    duplicates of the same case content."""
    for md_path in sorted(repo_dir.rglob("*.md")):
        name = md_path.name.lower()
        if name in SKIP_NAMES:
            continue
        # Drop language-variant READMEs — they duplicate the canonical English/zh case.
        if LANG_README_RE.match(name):
            continue
        rel = md_path.relative_to(repo_dir).as_posix()
        source_url = f"https://github.com/{repo['url'].split('github.com/')[-1].removesuffix('.git')}/blob/main/{rel}"
        try:
            text = md_path.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"  ! could not read {md_path}: {e}", file=sys.stderr)
            continue
        yield from extract_cases_from_markdown(text, repo, source_url)


# ---------------------------------------------------------------- writing


CASE_TEMPLATE = """\
---
title: "{title}"
source_repo: {source_repo}
source_url: {source_url}
credit: {credit}
workflow: {workflow}
model: {model}
tags: [{tags}]
inputs: {inputs}
---

## Original prompt

{prompt}

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `{primary_command}`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model={model},
  action={action}.
```

## Credit & license

Sourced from [{source_repo}]({source_url}) by {credit}.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
"""


COMMAND_BY_TAG_PRIORITY = [
    ("dance", "/dance"),
    ("headshot", "/headshot"),
    ("poster", "/poster"),
    ("ghibli", "/ghibli (v1.1)"),
    ("character-sheet", "/character-sheet (v1.1)"),
    ("ui-system", "/ui-system (v1.1)"),
    ("lookbook", "/lookbook (v1.2)"),
    ("ad-series", "/ad-series (v1.2)"),
    ("card-deck", "/card-deck (v1.2)"),
    ("unbox", "/unbox (v1.2)"),
]


def primary_command(tags: list[str]) -> str:
    for tag, cmd in COMMAND_BY_TAG_PRIORITY:
        if tag in tags:
            return cmd
    return "(case-library only — no v1 command match)"


def write_case(case: Case, out_dir: Path) -> Path:
    target = out_dir / f"from-{case.source_repo}" / f"{case.slug()}.md"
    target.parent.mkdir(parents=True, exist_ok=True)

    action = "edit" if case.workflow == "image2image" else "generate"
    body = CASE_TEMPLATE.format(
        title=yaml_escape(case.title),
        source_repo=case.source_repo,
        source_url=case.source_url,
        credit=case.credit,
        workflow=case.workflow,
        model=case.model,
        tags=", ".join(case.tags),
        inputs=json.dumps(case.inputs),
        prompt=case.prompt,
        primary_command=primary_command(case.tags),
        action=action,
    )

    # avoid clobbering — append a digit suffix if the slug collides
    if target.exists():
        existing = target.read_text(encoding="utf-8", errors="replace")
        if existing == body:
            return target  # idempotent
        i = 2
        while True:
            candidate = target.with_name(f"{target.stem}-{i}{target.suffix}")
            if not candidate.exists():
                target = candidate
                break
            i += 1

    target.write_text(body, encoding="utf-8")
    return target


def write_index(cases: list[Case], out_dir: Path) -> Path:
    by_workflow: dict[str, list[Case]] = defaultdict(list)
    by_tag: dict[str, list[Case]] = defaultdict(list)
    by_repo: dict[str, list[Case]] = defaultdict(list)
    for c in cases:
        by_workflow[c.workflow].append(c)
        for t in c.tags:
            by_tag[t].append(c)
        by_repo[c.source_repo].append(c)

    lines: list[str] = []
    lines.append("# Case Library Index\n")
    lines.append(
        "Curated from the three source repos. Each case is one markdown "
        "file with a normalized frontmatter (title, source, credit, "
        "workflow, model, tags). Use this index to find prompt templates "
        "to adapt for v1.1+ commands.\n"
    )
    lines.append(f"**Total cases:** {len(cases)}\n")

    lines.append("\n## By workflow\n")
    for wf in sorted(by_workflow):
        lines.append(f"- **{wf}** — {len(by_workflow[wf])} cases")

    lines.append("\n## By tag (likely command match)\n")
    for tag in sorted(by_tag, key=lambda t: -len(by_tag[t])):
        lines.append(f"- **{tag}** — {len(by_tag[tag])} cases")

    lines.append("\n## By source repo\n")
    for repo in sorted(by_repo):
        lines.append(f"\n### `{repo}` ({len(by_repo[repo])} cases)\n")
        for c in sorted(by_repo[repo], key=lambda c: c.title.lower()):
            slug = c.slug()
            tags = f"[{', '.join(c.tags)}]" if c.tags else ""
            lines.append(f"- [{c.title}](from-{repo}/{slug}.md) — {c.workflow} · {c.model} {tags}")

    target = out_dir / "INDEX.md"
    target.write_text("\n".join(lines), encoding="utf-8")
    return target


# ---------------------------------------------------------------- main


def clone_or_pull(source_dir: Path, repo: dict, no_clone: bool) -> Path:
    target = source_dir / repo["slug"]
    if no_clone and target.exists():
        return target
    if target.exists():
        try:
            subprocess.run(
                ["git", "-C", str(target), "fetch", "--depth=1", "origin"],
                check=True,
                capture_output=True,
            )
            subprocess.run(
                ["git", "-C", str(target), "reset", "--hard", "origin/HEAD"],
                check=True,
                capture_output=True,
            )
        except subprocess.CalledProcessError as e:
            print(f"  ! fetch failed for {repo['slug']}: {e}", file=sys.stderr)
        return target

    target.parent.mkdir(parents=True, exist_ok=True)
    print(f"  cloning {repo['url']} → {target}")
    subprocess.run(
        ["git", "clone", "--depth=1", repo["url"], str(target)],
        check=True,
    )
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-dir",
        default="/tmp/awesome-source",
        help="Where to clone the three source repos (default: /tmp/awesome-source).",
    )
    parser.add_argument(
        "--output-dir",
        default="prompts/case-library",
        help="Where to write the normalized case files (default: prompts/case-library).",
    )
    parser.add_argument(
        "--no-clone",
        action="store_true",
        help="Skip git clone — reuse whatever is in --source-dir.",
    )
    args = parser.parse_args()

    source_dir = Path(args.source_dir).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"=> source-dir: {source_dir}")
    print(f"=> output-dir: {output_dir}")
    print()

    all_cases: list[Case] = []

    # Optional content-hash dedup so the exact same prompt body doesn't get
    # written twice from two different markdown locations within a repo.
    import hashlib

    seen_hashes: set[str] = set()

    for repo in REPOS:
        print(f"--- {repo['slug']} ({repo['credit']}) ---")
        repo_dir = clone_or_pull(source_dir, repo, args.no_clone)
        raw_cases = list(walk_repo(repo_dir, repo))
        unique: list[Case] = []
        for c in raw_cases:
            h = hashlib.sha1(c.prompt.encode("utf-8", errors="replace")).hexdigest()
            if h in seen_hashes:
                continue
            seen_hashes.add(h)
            unique.append(c)
        print(f"  parsed: {len(raw_cases)} cases ({len(unique)} unique after content-hash dedup)")
        for c in unique:
            write_case(c, output_dir)
        all_cases.extend(unique)
        print()

    print(f"=> writing INDEX.md ({len(all_cases)} total cases)")
    index_path = write_index(all_cases, output_dir)
    print(f"   {index_path}")

    print()
    print("Done. Spot-check:")
    print(f"  ls {output_dir}/from-*/ | head -20")
    print(f"  cat {index_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
