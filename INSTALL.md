# Install Guide

Two steps. ~90 seconds, plus a one-time wallet top-up.

---

## Step 1 — Register the BlockRun MCP server

The slash commands in this bundle call `mcp__blockrun__blockrun_image`,
`_video`, and `_wallet`. Those tools come from the [BlockRun MCP server](https://github.com/BlockRunAI/blockrun-mcp),
not from this plugin. Register it once with Claude Code:

```bash
claude mcp add blockrun -s user -- npx -y @blockrun/mcp@latest
```

What this does:

- Writes `blockrun` into your user-level `~/.claude/mcp.json` (so it's
  available in every CC session, every project).
- On first launch CC runs `npx -y @blockrun/mcp@latest`, which fetches
  the latest BlockRun MCP server and starts it on stdio.

Verify it's wired up:

```bash
claude mcp list
# expect: blockrun ✓ Connected
```

> **Already registered?** `claude mcp add` is idempotent — re-running
> it does no harm. If you have an older BlockRun setup using a
> different command, run `claude mcp remove blockrun` first, then the
> command above.

> **Why not auto-install via `.mcp.json` in this repo?** The plugin
> ships a `.mcp.json` for environments that read it from a plugin
> directory (some marketplace install paths do). For the canonical
> `git clone` install path it's not guaranteed to be picked up — so
> the explicit `claude mcp add` above is the reliable, one-line method.

---

## Step 2 — Install this skill bundle

```bash
git clone https://github.com/BlockRunAI/cc-gpt-image2-seedance-blockrun \
  ~/.claude/plugins/cc-gpt-image2-seedance-blockrun
```

Restart Claude Code. The bundle adds `/headshot`, `/dance`, and
`/poster` as user-invocable skills.

Verify:

```
> /help
```

You should see `headshot`, `dance`, and `poster` listed.

---

## Step 3 — Fund your BlockRun wallet (Base USDC)

The BlockRun MCP auto-creates a wallet at `~/.blockrun/.session` on
first use (owner-readable only — the private key never leaves your
machine). To top it up, in Claude Code:

```
> top up my blockrun wallet
```

Claude calls `mcp__blockrun__blockrun_wallet` with `action: setup`,
which returns a QR code and a Base mainnet address.

Send **at least $1 USDC on Base** to that address (recommended $5–$20
for casual use). USDC contract on Base:
`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`.

Common sources:

- MetaMask / Rabby with Base added as a network
- Coinbase Wallet (Base is native)
- Bridges: Base Bridge, Hop, Across

Verify your balance:

```
> what's my blockrun balance?
```

---

## Quick smoke test

In any project directory:

```
> /headshot ./me.jpg
```

(Replace `./me.jpg` with a real photo path.)

After ~10 seconds you should see:

```
✅ Headshot ready

  File:   blockrun-out/2026-05-01T143200Z-headshot/headshot.png
  Style:  corporate
  Model:  openai/gpt-image-2 (HD)
  Cost:   ~$0.12 (settled on Base via x402)
```

---

## Optional — `ffmpeg` for `/dance` GIF rendering

`/dance` produces an mp4 by default. For a shareable looping GIF:

```bash
# macOS
brew install ffmpeg

# Linux (Debian / Ubuntu)
sudo apt-get install ffmpeg
```

The skill auto-detects ffmpeg and skips the GIF if it's missing.

---

## Optional — pin output to a different directory

By default, output lands in `./blockrun-out/{ts}-{cmd}/` in CWD. To
override:

```bash
export BLOCKRUN_OUT_DIR=~/Downloads/blockrun-output
```

Add to `~/.zshrc` or `~/.bashrc` to persist.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `Skill not recognized: /headshot` | Plugin not loaded — repo is in the wrong directory or CC wasn't restarted | Confirm `~/.claude/plugins/cc-gpt-image2-seedance-blockrun/skills/headshot/SKILL.md` exists, then restart CC |
| `mcp__blockrun__blockrun_wallet not available` (or any `mcp__blockrun__*` tool missing) | Step 1 wasn't run, or the MCP server failed to start | Run `claude mcp list` — if `blockrun` is missing or shows ✗, re-run Step 1's `claude mcp add` command. Check `npx -y @blockrun/mcp@latest` works manually. |
| `claude mcp add blockrun` errors with "command not found: claude" | Claude Code CLI not in PATH | Open a CC session and ask "where is the claude CLI installed?" — typically `~/.claude/local/claude` or a Homebrew path |
| `npx ENOTFOUND` on first run | First-time package fetch is offline-blocked | Run `npx -y @blockrun/mcp@latest --help` once with internet to prime the cache |
| `No wallet found` | First-run race | Run `blockrun_wallet action: status` once to bootstrap |
| `Payment failed: balance too low` | Wallet has < required amount | Top up via `blockrun_wallet action: setup` |
| `Image input unreachable` (in `/dance`) | Local file vs URL mismatch | The skill auto-falls-back via `blockrun_image` upload — make sure your wallet has an extra ~$0.06 |
| Generated GIF missing | `ffmpeg` not installed | Optional ffmpeg step above |

---

## Privacy and security

- The wallet private key at `~/.blockrun/.session` **never leaves your
  machine**. The MCP signs payloads locally with `viem` and only the
  signature is sent to BlockRun's gateway.
- Photos you pass to `/headshot` and `/dance` are uploaded to BlockRun's
  CDN as part of the request. Output URLs are permanent BlockRun-hosted
  links — keep your own copies via the local files in `blockrun-out/`.
- BlockRun does not store your prompts beyond what's needed to fulfill
  the request. See [blockrun.ai/privacy](https://blockrun.ai/privacy).
