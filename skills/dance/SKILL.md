---
name: dance
description: |
  Turn any photo into a 5-second dance video. Image-to-video via Seedance 2.0
  Fast through the BlockRun MCP plugin (x402 USDC on Base). One command,
  60–180 seconds wall time, ~$0.75 per clip. Six built-in choreography
  styles: hiphop, ballet, contemporary, kpop, terracotta-disco (兵马俑迪斯科),
  tiktok-trend, plus freestyle-from-music.
triggers:
  - "dance video"
  - "make me dance"
  - "image to video"
  - "animate this photo"
  - "seedance"
  - "img2vid"
  - "动起来"
  - "make a dance clip"
  - "tiktok dance"
  - "dance challenge"
user-invocable: true
allowed-tools: mcp__blockrun__blockrun_video, mcp__blockrun__blockrun_wallet, Bash(curl:*), Bash(ffmpeg:*), Bash(mkdir:*), Bash(date:*), Bash(ls:*), Read, Write
---

# `/dance` — Image-to-dance-video in one command

Drop a photo of a person, pick a dance style, get back a clean 5-second
mp4 (plus a shareable looping gif). Powered by ByteDance Seedance 2.0
through the BlockRun x402 gateway.

## What this skill does

Calls `mcp__blockrun__blockrun_video` with `image_url` set to the user's
photo, `model="bytedance/seedance-2.0-fast"`, and a choreography prompt
from `prompts/dance.md`. The MCP tool blocks while polling internally for
60–180 seconds, then returns a permanent mp4 URL. The skill downloads the
mp4 to `./blockrun-out/{ts}-dance/dance.mp4` and renders a GIF preview.

## Inputs

| Input | Required | Default | Notes |
|---|---|---|---|
| `image` (path or URL) | yes | — | Photo of the person. Full body or 3/4 body works best. |
| `style` | no | `tiktok-trend` | `hiphop`, `ballet`, `contemporary`, `kpop`, `terracotta-disco`, `tiktok-trend`, `freestyle-from-music`. |
| `music` | no | — | Free text. Only used when `style=freestyle-from-music`. |
| `duration_seconds` | no | `5` | Range 1–10. Seedance 2.0-fast charges $0.15/sec. |
| `output_dir` | no | `./blockrun-out/{ts}-dance/` | Override with `BLOCKRUN_OUT_DIR`. |

If the user says "make a dance video" without a photo, ask for the photo path.

## Workflow (Claude executes strictly in order)

### Step 0 — Verify the BlockRun MCP server is registered

Before any tool call, confirm `mcp__blockrun__blockrun_video` and
`mcp__blockrun__blockrun_wallet` are available. If not, surface this
exact message and stop:

> "The BlockRun MCP server isn't registered with Claude Code yet, so
> `/dance` can't run. Please run **once**:
>
> ```
> claude mcp add blockrun -s user -- npx -y @blockrun/mcp@latest
> ```
>
> Then restart Claude Code and try `/dance` again. (Full install
> guide: `INSTALL.md` in the cc-gpt-image2-seedance-blockrun bundle.)"

Do not proceed to the wallet preflight or video call if the MCP tools
are missing.

### Step 1 — Wallet preflight

Call `mcp__blockrun__blockrun_wallet` with `{"action": "status"}`.

- Required balance: `0.15 × duration_seconds` USDC plus a small buffer.
  For default 5s, require **≥ $1.00 USDC**.
- If too low, pause and tell the user:
  > "Your BlockRun wallet balance is too low. /dance with 5s Seedance 2.0-fast
  > costs ~$0.75. Run `blockrun_wallet action: setup` to top up Base USDC."
  Do not proceed.

### Step 2 — Image accessibility

The Seedance image-to-video flow needs a publicly fetchable URL or the MCP
tool will accept a hosted image. The current MCP `blockrun_video` tool's
`image_url` parameter expects a URL.

- If the user gave a URL: pass through.
- If the user gave a local file path:
  1. Verify the file exists with `Read`.
  2. Confirm size < 10 MB and dimensions are reasonable (Seedance prefers
     ≥ 720px on the short side).
  3. **Local-file fallback:** Use `mcp__blockrun__blockrun_image` with
     `action="edit"` and a no-op-style prompt
     (e.g. `"return the image unchanged, no edits"`) to upload-and-host the
     photo — the response URL is a permanent BlockRun CDN URL we can pass
     to `blockrun_video.image_url`. Cost ≈ $0.06 extra.
  4. Alternatively, instruct the user to upload to a host they control and
     supply the URL.

### Step 3 — Prepare prompt

Read `prompts/dance.md`. Pick the block matching `{style}` and substitute its
slots into the master template. For `freestyle-from-music`, splice the
user's `--music` argument into `{user_music_description}`.

### Step 4 — Call BlockRun MCP (the slow one)

```
Tool: mcp__blockrun__blockrun_video
Arguments:
{
  "prompt": "<filled template from Step 3>",
  "image_url": "<URL from Step 2>",
  "duration_seconds": <int, default 5>,
  "model": "bytedance/seedance-2.0-fast"
}
```

Tell the user before calling:
> "Submitting to Seedance 2.0-fast. This blocks for 60–180s while polling.
> Sit tight."

The MCP tool handles all polling internally with a 300s hard cap. When
the call returns, expect either:
- Success: `response.structuredContent.url` is a permanent mp4 URL.
- Timeout (`did not complete within 300s`): no charge — offer a retry.

### Step 5 — Download mp4 and render GIF

1. Timestamp: `date -u +"%Y-%m-%dT%H%M%SZ"`.
2. Output dir: `${BLOCKRUN_OUT_DIR:-./blockrun-out}/{ts}-dance/`.
3. `mkdir -p` the dir.
4. `curl -sSL "<url>" -o <out_dir>/dance.mp4`.
5. Render shareable looping GIF (best-effort — skip if `ffmpeg` is missing):
   ```
   ffmpeg -i <out_dir>/dance.mp4 \
     -vf "fps=15,scale=540:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
     -loop 0 <out_dir>/dance.gif
   ```
   If `ffmpeg` is not installed, omit the GIF and tell the user
   `brew install ffmpeg` would unlock it.
6. Confirm files are non-empty (`ls -la`).

### Step 6 — Report to user

```
✅ Dance video ready

  Video:    {relative path to .mp4}
  GIF:      {relative path to .gif}   (if rendered)
  Style:    {style}
  Duration: {duration} s
  Model:    bytedance/seedance-2.0-fast
  Cost:     ~${0.15 × duration} (settled on Base via x402)

Play it: open {relative path to .mp4}
```

If a GIF was generated, suggest the user attach it to a social post.

## Failure handling

| Error pattern | Action |
|---|---|
| `payment` / `balance` keywords | Show top-up message, do NOT retry. |
| `did not complete within 300s` | Tell the user the upstream was slow but no charge was taken; offer to retry. |
| `content filter` / `safety` / `invalid` | Apply the relevant retry addendum from `prompts/dance.md` (identity drift, hand warping, etc.) and retry once. |
| `image_url unreachable` / `unable to fetch source image` | Use the upload-via-blockrun_image fallback in Step 2 to host the local file, then retry. |
| `No wallet found` | Run `blockrun_wallet action: setup`, then retry. |

## Cost

| Duration | Cost |
|---|---|
| 5s (default) | ~$0.75 |
| 8s | ~$1.20 |
| 10s (max) | ~$1.50 |

Plus a one-time ~$0.06 if we used the upload-via-blockrun_image fallback.
Settled on Base USDC via x402. No charge if Seedance times out or fails.

## Examples

```
/dance ./me.jpg
/dance ./me.jpg --style hiphop
/dance ./me.jpg --style terracotta-disco
/dance ./me.jpg --style freestyle-from-music --music "lo-fi jazz 75 bpm"
/dance ./me.jpg --duration_seconds 8 --style kpop
```
