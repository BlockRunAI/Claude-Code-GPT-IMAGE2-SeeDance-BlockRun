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
    assets: list[dict] = field(default_factory=list)
    # assets[i] = {"kind": "image"|"video", "url": "<absolute raw URL>", "alt": "..."}

    def slug(self) -> str:
        return slugify(self.title)

    def hero_image_url(self) -> str | None:
        """Return the first image asset URL if any, else None."""
        for a in self.assets:
            if a.get("kind") == "image" and a.get("url"):
                return a["url"]
        return None


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


# --- asset extraction --------------------------------------------------------

# Match standard markdown image: ![alt](url)
MD_IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
# Match HTML <img src="...">
HTML_IMG_RE = re.compile(r"<img[^>]*\s+src=[\"']([^\"']+)[\"'][^>]*>", re.IGNORECASE)
# Match the seedance pattern: [![alt](poster.jpg)](video.mp4) — the inner is image, outer is video URL
LINKED_IMG_RE = re.compile(r"\[!\[([^\]]*)\]\(([^)\s]+)\)\]\(([^)\s]+)\)")
# Match <video src="..."> or <a href="...mp4">
VIDEO_HREF_RE = re.compile(r"<a[^>]*\s+href=[\"']([^\"']+\.(?:mp4|webm|mov))[\"']", re.IGNORECASE)


IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg")
VIDEO_EXTS = (".mp4", ".webm", ".mov", ".m4v")


def _is_image(url: str) -> bool:
    u = url.lower().split("?")[0].split("#")[0]
    return u.endswith(IMAGE_EXTS)


def _is_video(url: str) -> bool:
    u = url.lower().split("?")[0].split("#")[0]
    return u.endswith(VIDEO_EXTS)


def _resolve_url(raw: str, repo: dict, source_md_rel: str) -> str | None:
    """Convert a markdown asset reference into an absolute URL.

    - Absolute http(s) URLs pass through.
    - Relative paths get resolved as raw.githubusercontent.com URLs, anchored
      on the directory containing the source markdown file.
    - data: URIs and anchor-only links are dropped.
    """
    raw = raw.strip()
    if not raw or raw.startswith(("#", "data:", "mailto:", "javascript:")):
        return None
    if raw.startswith(("http://", "https://", "//")):
        return raw if not raw.startswith("//") else "https:" + raw

    # repo URL like https://github.com/<owner>/<repo>.git
    owner_repo = repo["url"].split("github.com/")[-1].removesuffix(".git")

    # source_md_rel is the markdown file's path relative to repo root, like "docs/gallery-part-1.md"
    md_dir = os.path.dirname(source_md_rel)

    # join + normalize
    joined = os.path.normpath(os.path.join(md_dir, raw))
    if joined.startswith(".."):
        return None  # escapes the repo
    joined = joined.lstrip("./")
    return f"https://raw.githubusercontent.com/{owner_repo}/main/{joined}"


def extract_assets(body: str, repo: dict, source_md_rel: str) -> list[dict]:
    """Extract image/video asset references from a case body section."""
    assets: list[dict] = []
    seen: set[str] = set()

    def _add(kind: str, url: str | None, alt: str = ""):
        if not url:
            return
        if url in seen:
            return
        seen.add(url)
        assets.append({"kind": kind, "url": url, "alt": alt[:120]})

    # Linked images first (the seedance [![](thumb)](video.mp4) pattern) so we
    # capture both the poster image AND the video URL it points to.
    for m in LINKED_IMG_RE.finditer(body):
        alt, thumb, link = m.group(1), m.group(2), m.group(3)
        thumb_url = _resolve_url(thumb, repo, source_md_rel)
        link_url = _resolve_url(link, repo, source_md_rel)
        if thumb_url and _is_image(thumb_url):
            _add("image", thumb_url, alt)
        if link_url:
            if _is_video(link_url):
                _add("video", link_url, alt)
            elif _is_image(link_url):
                _add("image", link_url, alt)

    # Standard markdown images
    for m in MD_IMG_RE.finditer(body):
        alt, url = m.group(1), m.group(2)
        u = _resolve_url(url, repo, source_md_rel)
        if u and _is_image(u):
            _add("image", u, alt)

    # HTML <img>
    for m in HTML_IMG_RE.finditer(body):
        u = _resolve_url(m.group(1), repo, source_md_rel)
        if u and _is_image(u):
            _add("image", u, "")

    # Direct <a href="*.mp4"> links
    for m in VIDEO_HREF_RE.finditer(body):
        u = _resolve_url(m.group(1), repo, source_md_rel)
        if u and _is_video(u):
            _add("video", u, "")

    # Filter out shields.io / badges / status badges
    bad_substrings = ("shields.io", "img.shields", "badge", "/badges/", "githubassets.com", "user-attachments")
    assets = [a for a in assets if not any(s in a["url"].lower() for s in bad_substrings)]

    return assets


def extract_cases_from_markdown(text: str, repo: dict, source_url: str, source_md_rel: str) -> Iterable[Case]:
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
        assets = extract_assets(body, repo, source_md_rel)

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
            assets=assets,
        )


LANG_README_RE = re.compile(r"^readme\.[a-z][a-z0-9\-]+\.md$", re.IGNORECASE)
SKIP_NAMES = {"license.md", "contributing.md", "changelog.md", "code_of_conduct.md", "code-of-conduct.md"}


LANG_PATH_RE = re.compile(r"/(de|es|fr|ja|ko|tr|pt|ru|zh-CN|zh-TW|zh)/", re.IGNORECASE)


def walk_repo(repo_dir: Path, repo: dict) -> Iterable[Case]:
    """Walk *.md files in the repo and yield cases. Skip language-variant
    READMEs (README.zh-CN.md, README.ja.md, etc.) and language directories
    (use-cases/ja/...) to avoid translation duplicates of the same case
    content."""
    for md_path in sorted(repo_dir.rglob("*.md")):
        name = md_path.name.lower()
        if name in SKIP_NAMES:
            continue
        # Drop language-variant README files
        if LANG_README_RE.match(name):
            continue
        rel = md_path.relative_to(repo_dir).as_posix()
        # Drop files inside language-specific directories like use-cases/ja/...
        if LANG_PATH_RE.search("/" + rel):
            # but keep the canonical English path use-cases/en/...
            if "/en/" not in "/" + rel:
                continue
        source_url = f"https://github.com/{repo['url'].split('github.com/')[-1].removesuffix('.git')}/blob/main/{rel}"
        try:
            text = md_path.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"  ! could not read {md_path}: {e}", file=sys.stderr)
            continue
        yield from extract_cases_from_markdown(text, repo, source_url, rel)


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
assets:
{assets_yaml}
---

{assets_md}

## Original prompt

{prompt}

## Run via Claude Code

After installing `Claude Code-GPT-IMAGE2-SeeDance-BlockRun`, you can adapt this case
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
[Claude Code-GPT-IMAGE2-SeeDance-BlockRun](https://github.com/BlockRunAI/Claude-Code-GPT-IMAGE2-SeeDance-BlockRun)
bundle. Reproduced with attribution; original license applies.
"""


def _render_assets_yaml(assets: list[dict]) -> str:
    if not assets:
        return "  []"
    lines = []
    for a in assets:
        alt = yaml_escape(a.get("alt") or "")
        url = a.get("url") or ""
        kind = a.get("kind") or "image"
        lines.append(f'  - kind: {kind}\n    url: "{url}"\n    alt: "{alt}"')
    return "\n".join(lines)


def _render_assets_md(assets: list[dict]) -> str:
    """Render the first image (and any video) inline at the top of the case."""
    if not assets:
        return "_No source-repo demo asset attached for this case._"
    parts = []
    img = next((a for a in assets if a.get("kind") == "image" and a.get("url")), None)
    vid = next((a for a in assets if a.get("kind") == "video" and a.get("url")), None)
    if img:
        alt = (img.get("alt") or "demo").replace("[", "(").replace("]", ")")
        parts.append(f"![{alt}]({img['url']})")
    if vid:
        parts.append(f"[▶️ Watch source video]({vid['url']})")
    return "\n\n".join(parts)


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
        assets_yaml=_render_assets_yaml(case.assets),
        assets_md=_render_assets_md(case.assets),
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


def write_gallery(cases: list[Case], out_dir: Path, top_n: int = 60) -> Path | None:
    """Write a 4-column markdown gallery of the strongest cases that have hero images.
    Used by README.md to show real demo outputs without bloating the repo with binaries."""
    # Score: cases with assets and at least one tag rank higher; prefer
    # poster/headshot/character-sheet/dance buckets first, then everything else.
    PREFERRED = ["poster", "headshot", "character-sheet", "ui-system", "ghibli", "dance", "ad-series", "card-deck", "lookbook", "anime", "kpop", "sci-fi"]

    def score(c: Case) -> tuple[int, int, int]:
        if not c.hero_image_url():
            return (-1, 0, 0)
        pref_hit = next((i for i, t in enumerate(PREFERRED) if t in c.tags), 999)
        tag_count = len(c.tags)
        prompt_len = len(c.prompt)
        return (-pref_hit, tag_count, prompt_len)

    scored = sorted([c for c in cases if c.hero_image_url()], key=score, reverse=True)
    if not scored:
        return None

    pick = scored[:top_n]

    lines: list[str] = []
    lines.append("# Featured Demo Gallery\n")
    lines.append(
        f"{len(pick)} hand-picked cases out of {len(cases)} in the library, "
        "rendered with the **original demo image from the source repo** so "
        "you can see what each prompt actually produces. Click any thumbnail "
        "to open the full case file (prompt, model, attribution).\n"
    )
    lines.append(
        "> Demo images are served via `raw.githubusercontent.com` from the "
        "source awesome-* repos. They are not stored in this bundle, so the "
        "repo stays small.\n"
    )

    cols = 4
    lines.append("\n<table>")
    for row_start in range(0, len(pick), cols):
        row = pick[row_start : row_start + cols]
        lines.append("  <tr>")
        for c in row:
            url = c.hero_image_url()
            href = f"from-{c.source_repo}/{c.slug()}.md"
            title_short = c.title[:60].replace("|", "·").replace("\"", "")
            lines.append(
                f'    <td align="center" width="25%"><a href="{href}"><img src="{url}" width="220" alt="{title_short}"/><br/><sub>{title_short}</sub></a></td>'
            )
        lines.append("  </tr>")
    lines.append("</table>\n")

    target = out_dir / "GALLERY.md"
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

    cases_with_assets = sum(1 for c in all_cases if c.assets)
    cases_with_image = sum(1 for c in all_cases if c.hero_image_url())
    print(f"=> {cases_with_assets} cases have assets ({cases_with_image} with a hero image)")
    gallery_path = write_gallery(all_cases, output_dir, top_n=60)
    if gallery_path:
        print(f"   wrote {gallery_path}")

    print()
    print("Done. Spot-check:")
    print(f"  ls {output_dir}/from-*/ | head -20")
    print(f"  cat {index_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
