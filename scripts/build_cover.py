#!/usr/bin/env python3
"""
build_cover.py — produce a high-density mosaic banner for the README hero.

Walks `prompts/case-library/from-*/*.md`, extracts each case's hero image
URL from the YAML frontmatter, downloads it (cached in `.tmp/cover-cache/`),
square-crops + resizes to a small thumbnail, then tiles them all into a
single banner image at `examples/cover.jpg`.

Usage:
    python3 scripts/build_cover.py [--cols 30] [--rows 12] [--cell 80]
                                   [--out examples/cover.jpg]
                                   [--cache .tmp/cover-cache]
                                   [--max N]
                                   [--shuffle]

Defaults give a 2400 × 960 banner (30 cols × 12 rows × 80px) holding 360
thumbnails — README-friendly, screenshots cleanly, ~2-3 MB JPEG.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import io
import random
import re
import sys
import urllib.request
from pathlib import Path

try:
    from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageFilter  # noqa: F401
except ImportError:
    print("ERROR: Pillow not installed. Run: pip install Pillow", file=sys.stderr)
    sys.exit(2)


# -----------------------------------------------------------------------------
# Frontmatter parsing — light-touch, just enough to grab the first image url
# -----------------------------------------------------------------------------

ASSET_KIND_URL_RE = re.compile(
    r"-\s*kind:\s*(image|video)\s*\n\s*url:\s*\"([^\"]+)\"",
    re.MULTILINE,
)


def first_image_url(case_md: Path) -> str | None:
    text = case_md.read_text(encoding="utf-8", errors="replace")
    # only look at the frontmatter (between the first two `---` lines)
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    fm = parts[1]
    for kind, url in ASSET_KIND_URL_RE.findall(fm):
        if kind == "image":
            return url
    return None


# -----------------------------------------------------------------------------
# Download with on-disk cache
# -----------------------------------------------------------------------------


def cache_path(cache_dir: Path, url: str) -> Path:
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]
    ext = url.split("?")[0].split("#")[0].rsplit(".", 1)[-1].lower()
    if ext not in {"jpg", "jpeg", "png", "gif", "webp"}:
        ext = "img"
    return cache_dir / f"{h}.{ext}"


REQ_HEADERS = {
    # Use the hyphenated repo slug here (no space) — User-Agent values are
    # robust to spaces but some upstreams treat them as token boundaries.
    "User-Agent": "Claude-Code-GPT-IMAGE2-SeeDance-BlockRun/build_cover.py (https://github.com/BlockRunAI/Claude-Code-GPT-IMAGE2-SeeDance-BlockRun)",
}


def fetch(url: str, dest: Path, timeout: float = 20.0) -> bool:
    if dest.exists() and dest.stat().st_size > 0:
        return True
    try:
        req = urllib.request.Request(url, headers=REQ_HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
        if not data:
            return False
        dest.write_bytes(data)
        return True
    except Exception as e:  # noqa: BLE001
        print(f"  ! fetch failed: {url} ({e})", file=sys.stderr)
        return False


# -----------------------------------------------------------------------------
# Tile preparation — square crop then resize, robust to varied formats
# -----------------------------------------------------------------------------


def make_tile(img_bytes: bytes, cell: int) -> Image.Image | None:
    try:
        im = Image.open(io.BytesIO(img_bytes))
        im.load()
    except Exception:  # noqa: BLE001
        return None
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGB")
    elif im.mode == "RGBA":
        # paste onto white to flatten
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg

    # ImageOps.fit does center-crop to the requested aspect, then resize.
    try:
        return ImageOps.fit(im, (cell, cell), method=Image.Resampling.LANCZOS)
    except Exception:  # noqa: BLE001
        try:
            return im.resize((cell, cell), Image.Resampling.LANCZOS)
        except Exception:  # noqa: BLE001
            return None


# -----------------------------------------------------------------------------
# Main pipeline
# -----------------------------------------------------------------------------


def collect_urls(case_root: Path) -> list[str]:
    urls: list[str] = []
    seen: set[str] = set()
    for case_md in sorted(case_root.rglob("*.md")):
        if case_md.name == "INDEX.md" or case_md.name == "GALLERY.md":
            continue
        url = first_image_url(case_md)
        if not url or url in seen:
            continue
        # filter clearly non-decorative (logos, banners) by a simple deny list
        lower = url.lower()
        if any(s in lower for s in ("logo.png", "/banner.", "shields.io", "/badge", "icon.")):
            continue
        seen.add(url)
        urls.append(url)
    return urls


def download_all(urls: list[str], cache_dir: Path, workers: int = 16) -> dict[str, Path]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    results: dict[str, Path] = {}

    def task(u: str) -> tuple[str, Path | None]:
        p = cache_path(cache_dir, u)
        ok = fetch(u, p)
        return u, (p if ok and p.stat().st_size > 0 else None)

    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        for i, (u, p) in enumerate(ex.map(task, urls), 1):
            if p is not None:
                results[u] = p
            if i % 25 == 0 or i == len(urls):
                print(f"  downloaded {len(results)}/{i} (queued {len(urls)})")
    return results


def _find_font(candidates: list[str], size: int) -> ImageFont.FreeTypeFont:
    """Try the candidate font paths in order; fall back to PIL default."""
    for path in candidates:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size)
            except Exception:  # noqa: BLE001
                continue
    return ImageFont.load_default()


BOLD_FONTS = [
    # macOS
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/HelveticaNeue.ttc",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    # Linux (common Ubuntu/Debian)
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
]
REG_FONTS = [
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/HelveticaNeue.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
]


def _measure(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    bb = draw.textbbox((0, 0), text, font=font)
    return bb[2] - bb[0], bb[3] - bb[1]


def _fit_font(
    draw: ImageDraw.ImageDraw,
    text: str,
    font_paths: list[str],
    sizes: list[int],
    max_width: int,
) -> tuple[ImageFont.FreeTypeFont, int, int]:
    """Pick the largest size from `sizes` whose rendered width fits max_width.
    Falls back to the smallest if none fit."""
    last = None
    for s in sizes:
        font = _find_font(font_paths, s)
        w, h = _measure(draw, text, font)
        last = (font, w, h)
        if w <= max_width:
            return font, w, h
    return last  # type: ignore[return-value]


def add_brand_overlay(
    canvas: Image.Image,
    brand: str,
    tagline: str,
) -> Image.Image:
    """Composite a centered dark rounded panel with brand title + tagline
    over the mosaic. Designed so a screenshot of any region of the cover
    still includes the brand name."""
    W, H = canvas.size

    # Apply a subtle global darken so text contrast holds even on light tiles.
    darken = Image.new("RGBA", (W, H), (0, 0, 0, 35))
    base = Image.alpha_composite(canvas.convert("RGBA"), darken)

    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Pick font sizes that scale with canvas height
    title_sizes = [int(H * f) for f in (0.16, 0.13, 0.11, 0.09, 0.075, 0.06)]
    sub_sizes = [int(H * f) for f in (0.06, 0.05, 0.04, 0.035, 0.03)]

    title_font, tw, th = _fit_font(draw, brand, BOLD_FONTS, title_sizes, int(W * 0.78))
    sub_font, sw, sh = _fit_font(draw, tagline, REG_FONTS, sub_sizes, int(W * 0.85))

    gap = int(H * 0.02)
    pad_x = int(W * 0.04)
    pad_y = int(H * 0.05)

    block_w = max(tw, sw) + 2 * pad_x
    block_h = th + sh + gap + 2 * pad_y

    cx = W // 2
    cy = H // 2
    rect_left = cx - block_w // 2
    rect_top = cy - block_h // 2
    rect_right = cx + block_w // 2
    rect_bottom = cy + block_h // 2

    # Soft drop shadow for the panel
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rounded_rectangle(
        (rect_left + 6, rect_top + 8, rect_right + 6, rect_bottom + 8),
        radius=int(min(W, H) * 0.025),
        fill=(0, 0, 0, 180),
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=12))

    # Foreground panel — semi-opaque dark, lets some mosaic show through
    panel = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pdraw = ImageDraw.Draw(panel)
    pdraw.rounded_rectangle(
        (rect_left, rect_top, rect_right, rect_bottom),
        radius=int(min(W, H) * 0.025),
        fill=(15, 15, 18, 215),
    )

    # Draw title + tagline
    title_x = cx - tw // 2
    title_y = rect_top + pad_y
    sub_x = cx - sw // 2
    sub_y = title_y + th + gap
    pdraw.text((title_x, title_y), brand, font=title_font, fill=(255, 255, 255, 255))
    pdraw.text((sub_x, sub_y), tagline, font=sub_font, fill=(220, 220, 220, 255))

    composed = Image.alpha_composite(base, shadow)
    composed = Image.alpha_composite(composed, panel)
    return composed.convert("RGB")


def build_mosaic(
    urls: list[str],
    cache: dict[str, Path],
    cols: int,
    rows: int,
    cell: int,
    shuffle: bool,
    seed: int,
) -> Image.Image:
    needed = cols * rows
    pool = [u for u in urls if u in cache]
    if shuffle:
        rng = random.Random(seed)
        rng.shuffle(pool)
    if len(pool) < needed:
        print(
            f"  ! only {len(pool)} usable images (needed {needed}); will repeat to fill.",
            file=sys.stderr,
        )

    canvas = Image.new("RGB", (cols * cell, rows * cell), (24, 24, 28))

    placed = 0
    pool_idx = 0
    for r in range(rows):
        for c in range(cols):
            if not pool:
                break
            url = pool[pool_idx % len(pool)]
            pool_idx += 1
            try:
                with cache[url].open("rb") as f:
                    tile = make_tile(f.read(), cell)
            except Exception:  # noqa: BLE001
                tile = None
            if tile is None:
                # try next item, don't waste the slot
                # (give up after a few misses for this slot)
                fallback_attempts = 0
                while tile is None and fallback_attempts < 20 and pool_idx < len(pool) * 2:
                    url = pool[pool_idx % len(pool)]
                    pool_idx += 1
                    fallback_attempts += 1
                    try:
                        with cache[url].open("rb") as f:
                            tile = make_tile(f.read(), cell)
                    except Exception:  # noqa: BLE001
                        tile = None
                if tile is None:
                    continue
            canvas.paste(tile, (c * cell, r * cell))
            placed += 1
    print(f"  placed {placed}/{cols * rows} tiles")
    return canvas


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--cols", type=int, default=30)
    p.add_argument("--rows", type=int, default=12)
    p.add_argument("--cell", type=int, default=80, help="thumbnail edge in px")
    p.add_argument("--out", default="examples/cover.jpg")
    p.add_argument("--cache", default=".tmp/cover-cache")
    p.add_argument("--case-root", default="prompts/case-library")
    p.add_argument("--max", type=int, default=0, help="cap pool size (0 = all)")
    p.add_argument("--shuffle", action="store_true", default=True)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--quality", type=int, default=82)
    p.add_argument("--workers", type=int, default=16)
    p.add_argument(
        "--brand",
        default="Claude Code-GPT-IMAGE2-SeeDance-BlockRun",
        help="Title overlaid on the cover. Pass empty string to skip overlay.",
    )
    p.add_argument(
        "--tagline",
        default="848 cases  ·  /headshot  /dance  /poster  ·  pay per image · USDC on Base",
        help="Subtitle overlaid below the brand.",
    )
    args = p.parse_args()

    case_root = Path(args.case_root).resolve()
    cache_dir = Path(args.cache).resolve()
    out_path = Path(args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"=> case-root: {case_root}")
    print(f"=> grid:      {args.cols}×{args.rows} = {args.cols * args.rows} cells")
    print(f"=> cell size: {args.cell}px → output {args.cols * args.cell}×{args.rows * args.cell}px")
    print(f"=> cache:     {cache_dir}")
    print(f"=> out:       {out_path}")
    print()

    print("==> collecting case hero URLs")
    urls = collect_urls(case_root)
    print(f"  {len(urls)} unique image urls")

    if args.max > 0 and len(urls) > args.max:
        rng = random.Random(args.seed)
        rng.shuffle(urls)
        urls = urls[: args.max]
        print(f"  capped to {args.max}")

    needed = args.cols * args.rows
    # download a bit more than the grid in case some fail
    wanted = min(len(urls), max(needed * 2, needed + 50))
    rng = random.Random(args.seed)
    rng.shuffle(urls)
    download_pool = urls[:wanted]
    print()

    print("==> downloading (cached)")
    cache = download_all(download_pool, cache_dir, workers=args.workers)
    print(f"  {len(cache)} usable in cache")

    print()
    print("==> tiling")
    mosaic = build_mosaic(
        download_pool, cache, args.cols, args.rows, args.cell, args.shuffle, args.seed
    )

    if args.brand:
        print()
        print(f"==> overlaying brand: {args.brand!r}")
        mosaic = add_brand_overlay(mosaic, args.brand, args.tagline)

    print()
    print("==> saving")
    mosaic.save(out_path, "JPEG", quality=args.quality, optimize=True, progressive=True)
    size_kb = out_path.stat().st_size / 1024
    print(f"  wrote {out_path} ({size_kb:.0f} KB)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
