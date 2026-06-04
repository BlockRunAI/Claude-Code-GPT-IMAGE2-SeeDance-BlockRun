#!/usr/bin/env bash
# install.sh — one-command installer for Claude Code-GPT-IMAGE2-SeeDance-BlockRun
#
# Run from the repo root after `git clone`, OR via the curl one-liner:
#   curl -fsSL https://raw.githubusercontent.com/BlockRunAI/Claude-Code-GPT-IMAGE2-SeeDance-BlockRun/main/install.sh | bash
#
# What it does:
#   1. Registers the BlockRun MCP server with Claude Code (idempotent).
#   2. Clones (or updates) the bundle to ~/.claude/blockrun-art-bundle/.
#   3. Symlinks the three skills (headshot, dance, poster) into
#      ~/.claude/skills/ so CC discovers them as bare /<command> slash
#      commands.

set -euo pipefail

REPO_URL="https://github.com/BlockRunAI/Claude-Code-GPT-IMAGE2-SeeDance-BlockRun"
BUNDLE_DIR="${HOME}/.claude/blockrun-art-bundle"
SKILLS_DIR="${HOME}/.claude/skills"
SKILLS=(headshot dance poster launch-film)

# Color helpers — fall back to plain when not a TTY.
if [ -t 1 ]; then
    BOLD=$'\033[1m'; DIM=$'\033[2m'; GREEN=$'\033[32m'; YELLOW=$'\033[33m'; RED=$'\033[31m'; RESET=$'\033[0m'
else
    BOLD=""; DIM=""; GREEN=""; YELLOW=""; RED=""; RESET=""
fi

say() { printf "%s%s%s\n" "$BOLD" "$1" "$RESET"; }
ok()  { printf "%s✓%s %s\n" "$GREEN" "$RESET" "$1"; }
warn() { printf "%s!%s %s\n" "$YELLOW" "$RESET" "$1"; }
die() { printf "%sx%s %s\n" "$RED" "$RESET" "$1" >&2; exit 1; }

# --- preflight ----------------------------------------------------------------

say "==> Claude Code-GPT-IMAGE2-SeeDance-BlockRun installer"

command -v git  >/dev/null || die "git is required but not installed."
command -v claude >/dev/null || die "Claude Code CLI ('claude') is required. Install it from https://claude.com/claude-code"

if ! command -v npx >/dev/null; then
    warn "npx not found — the BlockRun MCP server is launched via 'npx -y @blockrun/mcp@latest'."
    warn "Install Node.js (which includes npx) from https://nodejs.org first, then re-run this script."
    die  "missing dependency: npx"
fi

mkdir -p "$SKILLS_DIR"
mkdir -p "$(dirname "$BUNDLE_DIR")"

# --- step 1: register MCP server ---------------------------------------------

say "==> Step 1/3: registering BlockRun MCP server with Claude Code"

if claude mcp list 2>/dev/null | grep -qiE '(^|[[:space:]])blockrun([: ]|$)'; then
    ok "BlockRun MCP already registered (skipping claude mcp add)"
else
    if claude mcp add blockrun -s user -- npx -y "@blockrun/mcp@latest" >/dev/null 2>&1; then
        ok "registered: blockrun → npx -y @blockrun/mcp@latest"
    else
        warn "claude mcp add returned a non-zero exit. If you see 'already exists', that's fine."
        warn "If something else, run manually: claude mcp add blockrun -s user -- npx -y @blockrun/mcp@latest"
    fi
fi

# --- step 2: clone or update the bundle --------------------------------------

say "==> Step 2/3: installing bundle into $BUNDLE_DIR"

if [ -d "$BUNDLE_DIR/.git" ]; then
    ok "bundle exists, pulling latest"
    git -C "$BUNDLE_DIR" pull --ff-only --quiet || warn "pull failed (dirty or diverged checkout) — using the existing bundle as-is"
elif [ -e "$BUNDLE_DIR" ]; then
    die "$BUNDLE_DIR exists but is not a git checkout — please move or remove it and re-run."
else
    git clone --quiet --depth=1 "$REPO_URL" "$BUNDLE_DIR"
    ok "cloned to $BUNDLE_DIR"
fi

# --- step 3: symlink skills into ~/.claude/skills/ ---------------------------

say "==> Step 3/3: linking skills into $SKILLS_DIR"

for skill in "${SKILLS[@]}"; do
    target="$BUNDLE_DIR/skills/$skill"
    link="$SKILLS_DIR/$skill"

    if [ ! -d "$target" ]; then
        warn "skill source missing: $target — bundle layout has changed?"
        continue
    fi

    if [ -L "$link" ]; then
        # existing symlink — repoint it (idempotent)
        ln -sfn "$target" "$link"
        ok "relinked $link → $target"
    elif [ -e "$link" ]; then
        warn "$link exists and is NOT a symlink — leaving it alone."
        warn "   if you want this installer to manage it, move/remove $link and re-run."
    else
        ln -s "$target" "$link"
        ok "linked $link → $target"
    fi
done

# --- done --------------------------------------------------------------------

cat <<EOF

${BOLD}Done.${RESET}

Next steps:
  ${DIM}# 1. Restart Claude Code so the new skills are picked up.${RESET}
  ${DIM}# 2. Fund your BlockRun wallet (one-time):${RESET}
       ${BOLD}> top up my blockrun wallet${RESET}
  ${DIM}# 3. Try a command:${RESET}
       ${BOLD}> /headshot ./me.jpg${RESET}
       ${BOLD}> /dance    ./me.jpg --style hiphop${RESET}
       ${BOLD}> /poster   "Last Light" --genre thriller${RESET}

Bundle:    $BUNDLE_DIR
Skills:    $SKILLS_DIR/{headshot,dance,poster}
MCP:       blockrun (registered at user scope)

Cost guide: $BUNDLE_DIR/docs/COSTS.md
Uninstall:  $BUNDLE_DIR/uninstall.sh
EOF
