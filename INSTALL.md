# Install Guide

Two paths. Pick whichever you trust more.

---

## Path A — One-line install (recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/BlockRunAI/cc-gpt-image2-seedance-blockrun/main/install.sh | bash
```

What `install.sh` does (you can read it [here](install.sh) before running):

1. **Registers the BlockRun MCP server** with Claude Code:
   `claude mcp add blockrun -s user -- npx -y @blockrun/mcp@latest`
2. **Clones the bundle** to `~/.claude/blockrun-art-bundle/`
3. **Symlinks** the three skills into `~/.claude/skills/`:
   - `~/.claude/skills/headshot` → `…/blockrun-art-bundle/skills/headshot`
   - `~/.claude/skills/dance`    → `…/blockrun-art-bundle/skills/dance`
   - `~/.claude/skills/poster`   → `…/blockrun-art-bundle/skills/poster`

This last step is what makes `/headshot`, `/dance`, and `/poster` show up
as **bare slash commands** in Claude Code (not `/<plugin>:<skill>` —
just the short names).

Prereqs the script checks for: `git`, `claude` (Claude Code CLI), `npx`
(comes with Node.js).

---

## Path B — Manual two-step

If you'd rather do it by hand:

```bash
# 1. Register the BlockRun MCP server (one time, user-scoped — works in every CC session)
claude mcp add blockrun -s user -- npx -y @blockrun/mcp@latest

# 2. Clone the bundle and symlink the skills
git clone https://github.com/BlockRunAI/cc-gpt-image2-seedance-blockrun \
  ~/.claude/blockrun-art-bundle

mkdir -p ~/.claude/skills
ln -sf ~/.claude/blockrun-art-bundle/skills/headshot ~/.claude/skills/headshot
ln -sf ~/.claude/blockrun-art-bundle/skills/dance    ~/.claude/skills/dance
ln -sf ~/.claude/blockrun-art-bundle/skills/poster   ~/.claude/skills/poster
```

---

## After install (either path)

### 1. Restart Claude Code

Slash commands are picked up at session start. Quit and reopen `claude`.

### 2. Verify

```bash
claude mcp list
# expect: blockrun ✓ Connected
```

In Claude Code:

```
> /help
```

You should see `headshot`, `dance`, and `poster` listed under
user-invocable skills.

### 3. Fund your BlockRun wallet (Base USDC)

The MCP auto-creates a wallet at `~/.blockrun/.session` on first use
(owner-readable only — the private key never leaves your machine). Top
it up:

```
> top up my blockrun wallet
```

Claude calls `mcp__blockrun__blockrun_wallet` with `action: setup`
which returns a QR code and a Base mainnet address. Send **at least
$1 USDC on Base** (recommended $5–$20 for casual use). USDC contract
on Base: `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`.

Common sources:

- MetaMask / Rabby with Base added as a network
- Coinbase Wallet (Base is native)
- Bridges: Base Bridge, Hop, Across

Verify your balance:

```
> what's my blockrun balance?
```

### 4. Smoke test

```
> /headshot ./me.jpg
```

After ~10 seconds you should see:

```
✅ Headshot ready

  File:   blockrun-out/2026-05-01T143200Z-headshot/headshot.png
  Style:  corporate
  Model:  openai/gpt-image-2 (HD)
  Cost:   ~$0.12 (settled on Base via x402)
```

---

## Why these symlinks?

Claude Code discovers slash commands two ways:

- **Plugin path** (`~/.claude/plugins/<plugin>/`): only works if the
  plugin is registered through a marketplace; slash names get a
  `<plugin>:` prefix.
- **Skill path** (`~/.claude/skills/<skill>/SKILL.md`, single layer):
  bare slash name (e.g., `/headshot`); auto-discovered on session
  start.

The skill path gives the cleanest UX — `/headshot` instead of
`/cc-gpt-image2-seedance-blockrun:headshot`. The bundle directory
(`~/.claude/blockrun-art-bundle/`) holds the shared resources
(`prompts/`, `scripts/`, `docs/`, the case library); the symlinks
expose only the three skills to CC.

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

By default, output lands in `./blockrun-out/{ts}-{cmd}/` in your
current working directory. To override:

```bash
export BLOCKRUN_OUT_DIR=~/Downloads/blockrun-output
```

Add to `~/.zshrc` or `~/.bashrc` to persist.

---

## Updating

Re-run the installer — it pulls and relinks idempotently:

```bash
curl -fsSL https://raw.githubusercontent.com/BlockRunAI/cc-gpt-image2-seedance-blockrun/main/install.sh | bash
```

Or manually:

```bash
git -C ~/.claude/blockrun-art-bundle pull --ff-only
```

---

## Uninstalling

```bash
~/.claude/blockrun-art-bundle/uninstall.sh
```

That removes the symlinks and the bundle clone, and asks before
removing the BlockRun MCP server registration (you might still want it
for other tools).

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `Unknown command: /headshot` after install | CC wasn't restarted, or skills aren't in `~/.claude/skills/` | `ls -la ~/.claude/skills/headshot` should show a symlink. If not, re-run `install.sh`. Restart CC. |
| `mcp__blockrun__*` tool not available | MCP server not registered or failed to start | `claude mcp list` — if `blockrun` is missing, run `claude mcp add blockrun -s user -- npx -y @blockrun/mcp@latest`. Manually test: `npx -y @blockrun/mcp@latest --help`. |
| `claude mcp add` says "command not found: claude" | Claude Code CLI not on PATH | Find it: `find / -name claude -type f 2>/dev/null \| head`. Typically `~/.claude/local/claude` or a Homebrew bin. |
| `npx ENOTFOUND` first run | Offline at first package fetch | Run `npx -y @blockrun/mcp@latest --help` once with internet to prime the cache. |
| `No wallet found` | First-run race | Run `> blockrun_wallet action: status` once to bootstrap. |
| `Payment failed: balance too low` | Wallet under required amount | Top up via `> blockrun_wallet action: setup`. |
| `Image input unreachable` (in `/dance`) | Local file vs URL mismatch | The skill auto-falls-back via `blockrun_image` upload — make sure your wallet has an extra ~$0.06. |
| Generated GIF missing | `ffmpeg` not installed | See ffmpeg step above. |

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
