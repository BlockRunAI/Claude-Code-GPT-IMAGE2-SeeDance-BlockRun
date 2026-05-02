---
name: poster
description: |
  Generate a cinema-grade movie, event, podcast, or concert poster with
  proper typography in any language. One command, ~15 seconds, ~$0.12.
  Uses GPT Image 2 (multilingual text rendering!) via the BlockRun MCP
  plugin (x402 USDC on Base). Eight built-in genres: thriller, sci-fi,
  romcom, documentary, concert, horror, kids-animation, event.
triggers:
  - "movie poster"
  - "film poster"
  - "event poster"
  - "concert poster"
  - "podcast cover"
  - "key art"
  - "make a poster"
  - "电影海报"
  - "活动海报"
  - "founder documentary poster"
  - "launch poster"
user-invocable: true
allowed-tools: mcp__blockrun__blockrun_image, mcp__blockrun__blockrun_wallet, Bash(curl:*), Bash(mkdir:*), Bash(date:*), Read, Write
---

# `/poster` — Cinema-grade poster in one command

Generates a polished poster with **legible, accurate title typography in
any language** (gpt-image-2's killer feature). Use it for film festival
submissions, event banners, podcast cover art, concert posters, or pitch
deck mockups.

## What this skill does

Picks a genre block from `prompts/poster.md`, fills the master template
with the user's title + tagline + subject, and calls
`mcp__blockrun__blockrun_image` with `model="openai/gpt-image-2"`.

Default size is `1792x1024` (cinematic landscape). Add `--portrait` for
the traditional one-sheet `1024x1792`. Add `--square` for `1024x1024`
(podcast cover / Spotify Canvas friendly).

## Inputs

| Input | Required | Default | Notes |
|---|---|---|---|
| `title` | yes | — | The string that will be rendered as the title. CJK works. |
| `genre` | no | `documentary` | `thriller`, `sci-fi`, `romcom`, `documentary`, `concert`, `horror`, `kids-animation`, `event`. |
| `tagline` | no | `""` | A subtitle line. Empty omits the line. |
| `subject` | no | inferred from title | e.g., "a lone astronaut on a red planet". |
| `credits` | no | auto fake | A faux credit block, or pass real credits. |
| `accent_color` | no | per-genre default | Hex or color name. Useful for `event` genre. |
| Aspect flags | no | `--landscape` | One of `--landscape` (1792×1024, default), `--portrait` (1024×1792), `--square` (1024×1024). |
| `image` | no | — | Optional reference image for the lead subject (image-to-image edit). |

## Workflow (Claude executes strictly in order)

### Step 0 — Verify the BlockRun MCP server is registered

Before any tool call, confirm `mcp__blockrun__blockrun_image` and
`mcp__blockrun__blockrun_wallet` are available. If not, surface this
exact message and stop:

> "The BlockRun MCP server isn't registered with Claude Code yet, so
> `/poster` can't run. Please run **once**:
>
> ```
> claude mcp add blockrun -s user -- npx -y @blockrun/mcp@latest
> ```
>
> Then restart Claude Code and try `/poster` again. (Full install
> guide: `INSTALL.md` in the cc-gpt-image2-seedance-blockrun bundle.)"

Do not proceed to the wallet preflight or image call if the MCP tools
are missing.

### Step 1 — Wallet preflight

Call `mcp__blockrun__blockrun_wallet` with `{"action": "status"}`.

- Required: **≥ $0.20 USDC**.
- Too low? Show:
  > "Your BlockRun wallet balance is too low. /poster costs ~$0.12.
  > Run `blockrun_wallet action: setup` to top up Base USDC."
  Do not proceed.

### Step 2 — Resolve aspect

```
--landscape  → size = "1792x1024"
--portrait   → size = "1024x1792"
--square     → size = "1024x1024"
default      → "1792x1024"
```

### Step 3 — Prepare prompt

Read `prompts/poster.md`. Pick the genre block. Fill the master template
with the user's `title`, `tagline`, `subject`, `credits`, `accent_color`.

If `subject` is missing, infer it from the title and genre. For example,
`"Founders" + documentary` → `"a focused entrepreneur at a laptop, late
night, single desk lamp"`.

### Step 4 — Call BlockRun MCP

```
Tool: mcp__blockrun__blockrun_image
Arguments:
{
  "prompt": "<filled template from Step 3>",
  "action": "<generate or edit>",   // edit if user provided --image
  "model": "openai/gpt-image-2",
  "image": "<base64 data URI or URL>",  // only if --image was given
  "size": "<from Step 2>",
  "quality": "hd"
}
```

The tool returns synchronously in ~10–20 seconds.

### Step 5 — Download and save

1. Timestamp: `date -u +"%Y-%m-%dT%H%M%SZ"`.
2. Output dir: `${BLOCKRUN_OUT_DIR:-./blockrun-out}/{ts}-poster/`.
3. `mkdir -p` the dir.
4. Filename includes aspect: `poster-{aspect}.png`
   (e.g., `poster-1792x1024.png`).
5. `curl -sSL "<url>" -o <out_dir>/<filename>`.
6. Confirm file is non-empty.

### Step 6 — Verify title rendering (cheap quality gate)

Quickly check the response for content quality flags. If the user's title
contains CJK, Arabic, Cyrillic, or Hebrew characters, gently remind them
to verify the glyphs are correct in the output — gpt-image-2 is good but
not infallible with non-Latin scripts.

### Step 7 — Report to user

```
✅ Poster ready

  File:    {relative path}
  Title:   "{title}"
  Genre:   {genre}
  Aspect:  {size}
  Model:   openai/gpt-image-2 (HD)
  Cost:    ~$0.12 (settled on Base via x402)

Open it: open {relative path}
```

## Failure handling

| Error pattern | Action |
|---|---|
| `payment` / `balance` keywords | Show top-up message, do NOT retry. |
| Title text comes back as gibberish or wrong language | Apply the "Title text is gibberish" retry addendum from `prompts/poster.md` and retry once. |
| `content filter` / `safety` / `invalid` | Suggest rephrasing — common triggers are real-celebrity names or brand-protected IP. |
| Composition feels overstuffed | Apply the "no negative space" retry addendum and retry once. |
| `No wallet found` | Walk through `blockrun_wallet action: setup`, then retry. |

## Cost

- Landscape / portrait / square: ~$0.12 each (gpt-image-2 HD)
- A retry counts as a second call (~$0.24 total for that command run)
- Settled on Base USDC via x402.

## Examples

```
/poster "Last Light" --genre thriller
/poster "Founders" --genre documentary --tagline "they bet everything"
/poster "BlockRun Live" --genre event --accent_color "#0066ff" --portrait
/poster "兵马俑：复活" --genre sci-fi
/poster "Coffee with the CEO" --genre documentary --square  # podcast cover
```
