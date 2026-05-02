# Install Guide

Two steps. Total time: ~3 minutes (excluding USDC funding).

---

## Step 1 — Install this plugin (auto-installs the BlockRun MCP server)

```bash
git clone https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun \
  ~/.claude/plugins/cc-gpt-image2-seedance-blockrun
```

Restart Claude Code. The plugin's `.mcp.json` declares one MCP server:

```json
{
  "blockrun": {
    "command": "npx",
    "args": ["-y", "@blockrun/mcp@latest"]
  }
}
```

Claude Code reads this on plugin load, runs `npx -y @blockrun/mcp@latest`,
and registers `mcp__blockrun__blockrun_image`, `_video`, and `_wallet`
automatically.

> **Already have the standalone BlockRun MCP plugin installed?** Then the
> `blockrun` MCP server is already registered. CC will use the existing
> one and ignore the duplicate registration — there's no conflict.

Verify in Claude Code:

```
> what blockrun tools do I have?
```

You should see `blockrun_image`, `blockrun_video`, `blockrun_wallet`
(plus any other tools the BlockRun MCP exposes — chat, search, wallet,
markets, etc.).

---

## Step 2 — Fund your BlockRun wallet (Base USDC)

The MCP plugin auto-creates a wallet at `~/.blockrun/.session` on first
use (owner-readable only — the private key never leaves your machine).
To top it up:

```
> top up my blockrun wallet
```

Claude calls `mcp__blockrun__blockrun_wallet` with `action: setup`, which
returns a QR code and a Base mainnet address.

Send **at least $1 USDC on Base** to that address (recommended $5–$20 for
casual use). The USDC contract on Base is
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

(Replace `./me.jpg` with the path to a real photo of yourself.)

After ~10 seconds you should get back:

```
✅ Headshot ready

  File:   blockrun-out/2026-05-01T143200Z-headshot/headshot.png
  Style:  corporate
  Model:  openai/gpt-image-2 (HD)
  Cost:   ~$0.12 (settled on Base via x402)
```

---

## Optional — `ffmpeg` for `/dance` GIF rendering

`/dance` produces an mp4 by default. If you want a shareable looping GIF
preview, install ffmpeg:

```bash
# macOS
brew install ffmpeg

# Linux (Debian / Ubuntu)
sudo apt-get install ffmpeg
```

The skill auto-detects ffmpeg's presence and skips the GIF if it's missing.

---

## Optional — pin output to a different directory

By default, command output lands in `./blockrun-out/{ts}-{cmd}/` in the
current working directory. To override globally:

```bash
export BLOCKRUN_OUT_DIR=~/Downloads/blockrun-output
```

Add to `~/.zshrc` or `~/.bashrc` to persist.

---

## Alternative install paths

### A) Skill-only install (if you already have BlockRun MCP and don't want this plugin to manage it)

```bash
git clone https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun \
  ~/.claude/skills/cc-gpt-image2-seedance-blockrun
```

`~/.claude/skills/` does **not** read `.mcp.json`, so no auto-install.
You'll need to have the BlockRun MCP plugin from `blockrunai/blockrun`
installed separately. Use this path if you want minimal coupling.

### B) Marketplace one-click (planned for v1.1)

Once published to the BlockRun marketplace:

```
> /plugin marketplace install blockrunai/cc-gpt-image2-seedance-blockrun
```

That's the cleanest path for non-technical users. We'll update this README
when it lands.

### C) Manual MCP-add (if `.mcp.json` doesn't auto-register on your CC version)

```bash
claude mcp add blockrun -s user -- npx -y @blockrun/mcp@latest
```

Then `git clone` this repo into `~/.claude/skills/` (Path A).

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| "BlockRun MCP not found" | CC didn't read `.mcp.json` | Confirm the repo is in `~/.claude/plugins/` (not `skills/`) and restart CC |
| "Skill not recognized: /headshot" | Plugin not loaded | Check `~/.claude/plugins/cc-gpt-image2-seedance-blockrun/skills/headshot/SKILL.md` exists, restart CC |
| "No wallet found" | First-run race | Run `blockrun_wallet action: status` once to bootstrap |
| "Payment failed: balance too low" | Wallet has < required amount | Top up via `blockrun_wallet action: setup` |
| "Image input unreachable" (in `/dance`) | Local file vs URL mismatch | The skill auto-falls-back via `blockrun_image` upload — make sure your wallet has an extra ~$0.06 |
| Generated GIF missing | `ffmpeg` not installed | Optional ffmpeg step above |
| Two `blockrun` MCP servers complain | You installed both this plugin and the standalone BlockRun MCP plugin | Keep only one — easiest is uninstalling the standalone one and letting this plugin manage it |

---

## Privacy and security

- The wallet private key at `~/.blockrun/.session` **never leaves your
  machine**. The MCP signs payloads locally with `viem` and only the
  signature is sent to BlockRun's gateway.
- Photos you pass to `/headshot` and `/dance` are uploaded to BlockRun's
  CDN as part of the request. Output URLs are permanent BlockRun-hosted
  links — keep your own copies via the local files in `blockrun-out/`.
- BlockRun does not store your prompts beyond what's needed to fulfill the
  request. See [blockrun.ai/privacy](https://blockrun.ai/privacy).
