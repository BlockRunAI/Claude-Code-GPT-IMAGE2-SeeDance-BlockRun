# cc-gpt-image2-seedance-blockrun

> **Run any awesome-gpt-image-2 or Seedance prompt as a one-line Claude Code command. Pay per image with x402 USDC on Base.**

Other awesome lists tell you what prompt to copy-paste.
This one **runs them for you** — directly from Claude Code, with output
that drops into your project folder, billed by the call (no subscription).

```bash
# One-line install (registers MCP + clones bundle + symlinks /headshot, /dance, /poster)
curl -fsSL https://raw.githubusercontent.com/BlockRunAI/cc-gpt-image2-seedance-blockrun/main/install.sh | bash
```

> Prefer not to pipe to bash? Manual two-step lives in [INSTALL.md](INSTALL.md).

Restart Claude Code, fund your BlockRun wallet on first run
(`> top up my blockrun wallet` — takes ~60 seconds), and:

```
> /headshot ./me.jpg
> /dance ./me.jpg --style hiphop
> /poster "Last Light" --genre thriller
```

That's it.

---

## Demo

> The thumbnails below are **real outputs** the underlying models produce —
> served directly from the source `awesome-*` repos (raw URLs, no copies
> stored here). Click through to open the full case file with the prompt,
> attribution, and the X/Twitter post it came from.

<table>
  <tr>
    <td align="center" width="33%"><b>/headshot</b><br/><i>~$0.12 · ~10s</i></td>
    <td align="center" width="33%"><b>/dance</b><br/><i>~$0.75 · 60–180s</i></td>
    <td align="center" width="33%"><b>/poster</b><br/><i>~$0.12 · ~15s</i></td>
  </tr>
  <tr>
    <td align="center"><a href="prompts/case-library/from-awesome-gpt-image-2-prompts/case-16-soft-black-mist-idol-portrait-https-x-com-bubblebrain-status-2046518189509734903-by-bubblebrain-https.md"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-prompts/main/images/portrait_case16/output.jpg" alt="/headshot demo — Soft Black Mist Idol Portrait" width="280"/></a></td>
    <td align="center"><a href="https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-1/1/result.mp4"><img src="https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-1/1/result.jpg" alt="/dance demo — Seedance Character Scene Consistency (▶ click to play)" width="280"/></a></td>
    <td align="center"><a href="prompts/case-library/from-awesome-gpt-image-2-prompts/case-1-boston-spring-2026-city-poster-https-x-com-bubblebrain-status-2045358053831172358-by-bubblebrain-https.md"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-prompts/main/images/poster_case1/output.jpg" alt="/poster demo — Boston Spring City Poster" width="280"/></a></td>
  </tr>
  <tr>
    <td align="center"><sub>Selfie → studio portrait. 5 styles built-in (corporate, creative, startup, actor, linkedin-2025).</sub></td>
    <td align="center"><sub>Photo → 5-second video. 7 choreography presets including <code>terracotta-disco</code> 兵马俑迪斯科.</sub></td>
    <td align="center"><sub>Title → cinema-grade key art. 8 genres, multilingual title typography.</sub></td>
  </tr>
</table>

---

## What is this

The two big GPT Image 2 awesome lists ([EvoLinkAI](https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts),
[freestylefly](https://github.com/freestylefly/awesome-gpt-image-2)) and the
[awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide)
are gold mines of viral image / video prompts. But they're **static** —
you copy a prompt, paste it into someone's chat UI, fight with the
upload, and pay through some subscription you never wanted.

This bundle turns them into **executable Claude Code commands**:

- **What you install:** the [BlockRun MCP server](https://github.com/BlockRunAI/blockrun-mcp)
  (one `claude mcp add` command — it runs as `npx @blockrun/mcp@latest`)
  plus this plugin (a `git clone` into `~/.claude/plugins/`). Two
  steps, ~90 seconds.
- **What it does:** thin, polished slash commands that pick the right
  model, build a vetted prompt template, call the right MCP tool, and
  drop a file in your project directory. Three commands at v1, more coming.
- **Underneath:** the [BlockRun gateway](https://blockrun.ai) routes to
  OpenAI, ByteDance, xAI, Google, and Z.ai — pay per call in Base USDC
  via x402. No API keys, no subscriptions, no minimums.

```
You type   /headshot ./me.jpg --style startup
            ↓
[this plugin]   picks template + variables, calls
            ↓
mcp__blockrun__blockrun_image    ← from `@blockrun/mcp` (registered via claude mcp add)
            ↓
BlockRun gateway · x402 USDC settle · OpenAI gpt-image-2
            ↓
You get   ./blockrun-out/2026-05-01T143200Z-headshot/headshot.png
```

> Already have BlockRun MCP registered? Skip Step 1 — `claude mcp add`
> is idempotent at the same name and a re-add is harmless.

---

## Commands

### `/headshot` — studio-quality professional photo in 10 seconds

```
/headshot ./me.jpg
/headshot ./me.jpg --style startup
/headshot ./me.jpg --style actor
/headshot ./me.jpg --all          # 4 styles in one go
```

Five built-in styles: `corporate` (default), `creative`, `startup`,
`actor`, `linkedin-2025`. Source identity is preserved 1:1 — only
wardrobe, lighting, and background are restyled.

| Param | Default | Notes |
|---|---|---|
| `image` | required | JPG / PNG / HEIC / WebP, local path or URL |
| `--style` | `corporate` | or `creative`, `startup`, `actor`, `linkedin-2025`, `all` |
| Cost | ~$0.12 | per style; `--all` = ~$0.48 |

Full prompt templates: [`prompts/headshot.md`](prompts/headshot.md) ·
Skill: [`skills/headshot/SKILL.md`](skills/headshot/SKILL.md)

---

### `/dance` — turn any photo into a 5-second dance video

```
/dance ./me.jpg
/dance ./me.jpg --style hiphop
/dance ./me.jpg --style terracotta-disco             # 兵马俑迪斯科
/dance ./me.jpg --style freestyle-from-music \
                --music "lo-fi jazz 75 bpm"
/dance ./me.jpg --duration_seconds 8 --style kpop
```

Six choreography presets: `hiphop`, `ballet`, `contemporary`, `kpop`,
`terracotta-disco`, `tiktok-trend`, plus `freestyle-from-music` for
custom soundtracks. Powered by **ByteDance Seedance 2.0 Fast** (the
price/quality knee — see [`docs/COSTS.md`](docs/COSTS.md)).

Outputs both `dance.mp4` and a shareable looping `dance.gif` (if `ffmpeg`
is installed locally).

| Param | Default | Notes |
|---|---|---|
| `image` | required | full-body or 3/4-body works best |
| `--style` | `tiktok-trend` | one of 7 presets |
| `--duration_seconds` | `5` | range 1–10 |
| `--music` | — | only for `freestyle-from-music` |
| Cost | ~$0.75 | for default 5s; $0.15/sec |

Full prompt templates: [`prompts/dance.md`](prompts/dance.md) ·
Skill: [`skills/dance/SKILL.md`](skills/dance/SKILL.md)

---

### `/poster` — cinema-grade movie / event poster in 15 seconds

```
/poster "Last Light" --genre thriller
/poster "Founders" --genre documentary --tagline "they bet everything"
/poster "BlockRun Live" --genre event --accent_color "#0066ff" --portrait
/poster "兵马俑：复活" --genre sci-fi
/poster "Coffee with the CEO" --genre documentary --square    # podcast cover
```

Eight genre presets: `thriller`, `sci-fi`, `romcom`, `documentary`,
`concert`, `horror`, `kids-animation`, `event`. **gpt-image-2's killer
feature** — multilingual title typography that actually reads correctly,
including CJK / Arabic / Cyrillic.

| Param | Default | Notes |
|---|---|---|
| `title` | required | rendered exactly as typed, multilingual safe |
| `--genre` | `documentary` | one of 8 presets |
| `--tagline`, `--subject`, `--credits` | — | optional polish |
| `--landscape` / `--portrait` / `--square` | landscape | aspect (1792×1024 / 1024×1792 / 1024×1024) |
| Cost | ~$0.12 | per call |

Full prompt templates: [`prompts/poster.md`](prompts/poster.md) ·
Skill: [`skills/poster/SKILL.md`](skills/poster/SKILL.md)

---

## Cost transparency

| Command | Cost | Wall time |
|---|---|---|
| `/headshot` (1 style) | ~$0.12 | ~10 s |
| `/headshot --all` (4 styles) | ~$0.48 | ~40 s |
| `/dance` (5 s, default) | ~$0.75 | 60–180 s |
| `/dance` (10 s, max) | ~$1.50 | 100–240 s |
| `/poster` (any aspect) | ~$0.12 | ~15 s |

**No subscription. No charge if a call times out or fails.** Settled on
Base mainnet USDC via x402. The wallet's private key never leaves
`~/.blockrun/.session` — only signed payment authorizations travel.

A typical creator session ($5 USDC top-up) covers ~40 headshots, or 6 dance
videos, or 40 posters, or any mix. See [`docs/COSTS.md`](docs/COSTS.md)
for the full breakdown of all underlying gateway prices.

---

## Demo gallery — real outputs from the source awesome lists

Below are 12 cases hand-picked from the bundled case library, rendered
with the **original demo image from the source repo**. Click any
thumbnail to open the full case file (prompt, model, attribution).

<table>
  <tr>
    <td align="center" width="25%"><a href="prompts/case-library/GALLERY.md"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-prompts/main/images/poster_case1/output.jpg" alt="Boston Spring 2026 City Poster" width="220"/><br/><sub>City Poster · poster</sub></a></td>
    <td align="center" width="25%"><a href="prompts/case-library/GALLERY.md"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-prompts/main/images/poster_case144/output.jpg" alt="Luxury Watch Ad" width="220"/><br/><sub>Luxury Product Ad · ad-series</sub></a></td>
    <td align="center" width="25%"><a href="prompts/case-library/GALLERY.md"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-prompts/main/images/poster_case123/output.jpg" alt="Water Signs Zodiac" width="220"/><br/><sub>Zodiac Character Series · card-deck</sub></a></td>
    <td align="center" width="25%"><a href="prompts/case-library/GALLERY.md"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-prompts/main/images/poster_case128/output.jpg" alt="Vintage PRS Guitar Lineage" width="220"/><br/><sub>Vintage Product Lineage · poster</sub></a></td>
  </tr>
  <tr>
    <td align="center"><a href="prompts/case-library/GALLERY.md"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-prompts/main/images/portrait_case16/output.jpg" alt="Soft Black Mist Idol Portrait" width="220"/><br/><sub>Editorial Portrait · headshot</sub></a></td>
    <td align="center"><a href="prompts/case-library/GALLERY.md"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-prompts/main/images/portrait_case99/output.jpg" alt="Portrait variant" width="220"/><br/><sub>Editorial Portrait · headshot</sub></a></td>
    <td align="center"><a href="prompts/case-library/GALLERY.md"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-prompts/main/images/portrait_case100/output.jpg" alt="Portrait variant" width="220"/><br/><sub>Glitch Portrait · headshot</sub></a></td>
    <td align="center"><a href="prompts/case-library/GALLERY.md"><img src="https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-prompts/main/images/ui_case101/output.jpg" alt="Anime Fantasy Travel Movie Poster" width="220"/><br/><sub>Anime Movie Poster · poster</sub></a></td>
  </tr>
  <tr>
    <td align="center"><a href="prompts/case-library/GALLERY.md"><img src="https://raw.githubusercontent.com/freestylefly/awesome-gpt-image-2/main/data/images/case1.jpg" alt="Urban Metabolism Atlas" width="220"/><br/><sub>Isometric Infographic · ui-system</sub></a></td>
    <td align="center"><a href="prompts/case-library/GALLERY.md"><img src="https://raw.githubusercontent.com/freestylefly/awesome-gpt-image-2/main/data/images/case166.jpg" alt="十二黄金圣斗士卡牌合集" width="220"/><br/><sub>12-Card Trading Set · card-deck</sub></a></td>
    <td align="center"><a href="prompts/case-library/GALLERY.md"><img src="https://raw.githubusercontent.com/freestylefly/awesome-gpt-image-2/main/data/images/case235.jpg" alt="治愈系助眠指南九宫格" width="220"/><br/><sub>9-Grid Information · character-sheet</sub></a></td>
    <td align="center"><a href="https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-1/4/result.mp4"><img src="https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-1/4/result.jpg" alt="Seedance Magnetic Bow Advertisement" width="220"/><br/><sub>Seedance Product Ad ▶ · dance/video</sub></a></td>
  </tr>
</table>

**See the full curated gallery: [`prompts/case-library/GALLERY.md`](prompts/case-library/GALLERY.md)** — 60 hand-picked cases.

### Full case library

| Workflow | Cases |
|---|---|
| Text → image | 268 |
| Text → video | 106 |
| Image → image (edit) | 322 |
| Image → video | 27 |
| **Total** | **723** unique cases (96% with hero image attached) |

Every case is a single markdown file with normalized frontmatter (title,
source, credit, workflow, model, tags) plus the original demo image
embedded. See [`prompts/case-library/INDEX.md`](prompts/case-library/INDEX.md)
for the full browseable catalog grouped by tag and source.

> v1 ships with 3 polished slash commands (`/headshot`, `/dance`,
> `/poster`). The 700+ cases above are the runway for v1.1+ — each tag in
> the index is a candidate slash command in waiting.

| Vibe | Source | One-line command |
|---|---|---|
| Studio Ghibli portrait | awesome-gpt-image-2 | `/headshot ./me.jpg --style ghibli` (v1.1) |
| 9-grid character sheet | awesome-gpt-image-2-prompts | `/character-sheet "Hua, terracotta scout"` (v1.1) |
| Glassmorphism UI mock | awesome-gpt-image-2 | `/ui-system social --style glass` (v1.1) |
| Movie poster (thriller) | this bundle | `/poster "Last Light" --genre thriller` |
| 5-second dance loop | awesome-seedance-2-guide | `/dance ./me.jpg --style tiktok-trend` |
| K-pop stage clip | awesome-seedance-2-guide | `/dance ./me.jpg --style kpop` |
| LinkedIn "promoted" headshot | awesome-gpt-image-2-prompts | `/headshot ./me.jpg --style linkedin-2025` |
| Podcast cover (square) | this bundle | `/poster "Coffee with the CEO" --square` |
| ... | ... | ... |

---

## Why Claude Code + BlockRun

- **Native CC integration.** No browser, no copy-paste, no separate
  tools. Slash commands inside the editor you already use.
- **Pay per call.** $0.12 here, $0.75 there. Stop when you're done. Top
  up when you want. No "10 free generations a month, then $20/mo".
- **Multi-model under one roof.** GPT Image 2 for typography. Seedance
  for video. DALL-E 3 / Nano Banana / Grok / CogView available too —
  switch with one parameter.
- **Crypto-native, but invisible.** Base USDC is the rails, but you only
  see USD prices. Your wallet auto-creates on first use. Top up with
  any wallet that speaks Base.
- **Deterministic outputs.** Files land in your project directory. Easy
  to commit (don't), share, post, or feed into the next stage of your
  pipeline.

---

## Roadmap

| Version | Commands |
|---|---|
| **v1.0** (this release) | `/headshot`, `/dance`, `/poster` |
| v1.1 | `/character-sheet`, `/ui-system`, `/ghibli` |
| v1.2 | `/lookbook`, `/ad-series`, `/card-deck`, `/unbox` |
| v2.0 | `/blockrun-art generate "<free description>"` smart router; full case-library executable as discoverable subcommands |

Want to influence what comes next? Open an issue or vote in the
discussions: [github.com/blockrunai/cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun).

---

## Credits

The viral prompt patterns in `prompts/case-library/` were curated from:

- **[EvoLinkAI/awesome-gpt-image-2-prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts)** — text-to-image and image-to-image template gold mine
- **[freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)** — image-to-image edits, style transfers, character consistency
- **[EvoLinkAI/awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide)** — Seedance text-to-video and image-to-video case studies

Each case file under `prompts/case-library/from-*/` includes
`source_url` and `credit` in its frontmatter — go give those repos a star.

The underlying gateway is **[BlockRun.ai](https://blockrun.ai)** — x402
micropayments on Base, no subscriptions, no API keys.

---

## License

MIT — see [`LICENSE`](LICENSE). Cases under `prompts/case-library/from-*/`
retain the licenses of their original repositories (all three are
MIT-compatible at the time of this release).

---

<details>
<summary>SEO keywords (for indexing)</summary>

claude code, claude code skill, claude code plugin, claude code marketplace,
gpt-image-2, gpt image 2, openai gpt image, dall-e 3, nano banana,
seedance, seedance 2.0, seedance 1.5, bytedance video, bytedance ai video,
blockrun, blockrun.ai, blockrun mcp, x402, x402 micropayments,
USDC base, base mainnet, base usdc payments,
ai image generation, ai image generator, ai video generation, ai video generator,
image to video, img2vid, image-to-image edit, photo to video,
headshot generator, ai headshot, professional headshot ai, linkedin photo ai,
movie poster generator, ai movie poster, film poster ai, key art ai,
dance video generator, ai dance video, tiktok dance ai, viral dance video,
viral ai prompts, awesome gpt image 2, awesome seedance,
mcp server, model context protocol, claude mcp,
character sheet ai, ui mockup ai, ghibli style ai, kpop video ai

</details>
