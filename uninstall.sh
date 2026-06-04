#!/usr/bin/env bash
# uninstall.sh — reverse install.sh
#
# Removes the symlinks in ~/.claude/skills/, deletes the bundle clone,
# and (optionally) removes the BlockRun MCP server registration.

set -euo pipefail

BUNDLE_DIR="${HOME}/.claude/blockrun-art-bundle"
SKILLS_DIR="${HOME}/.claude/skills"
SKILLS=(headshot dance poster launch-film)

if [ -t 1 ]; then
    BOLD=$'\033[1m'; GREEN=$'\033[32m'; YELLOW=$'\033[33m'; RESET=$'\033[0m'
else
    BOLD=""; GREEN=""; YELLOW=""; RESET=""
fi

say() { printf "%s%s%s\n" "$BOLD" "$1" "$RESET"; }
ok()  { printf "%s✓%s %s\n" "$GREEN" "$RESET" "$1"; }
warn() { printf "%s!%s %s\n" "$YELLOW" "$RESET" "$1"; }

say "==> Claude Code-GPT-IMAGE2-SeeDance-BlockRun uninstaller"

# Remove only symlinks pointing into our bundle — never delete user data.
for skill in "${SKILLS[@]}"; do
    link="$SKILLS_DIR/$skill"
    if [ -L "$link" ]; then
        target="$(readlink "$link")"
        case "$target" in
            "$BUNDLE_DIR"/*)
                rm "$link"; ok "removed symlink $link"
                ;;
            *)
                warn "skipping $link — not pointing into our bundle ($target)"
                ;;
        esac
    fi
done

# Remove the bundle dir.
if [ -d "$BUNDLE_DIR/.git" ]; then
    rm -rf "$BUNDLE_DIR"; ok "removed $BUNDLE_DIR"
elif [ -e "$BUNDLE_DIR" ]; then
    warn "leaving $BUNDLE_DIR in place — it isn't a git checkout."
fi

# MCP server: ask before removing — user may want to keep it for other tools.
if command -v claude >/dev/null && claude mcp list 2>/dev/null | grep -qiE '(^|[[:space:]])blockrun([: ]|$)'; then
    say ""
    say "Found BlockRun MCP server registered with Claude Code."
    read -r -p "Remove the 'blockrun' MCP server registration too? [y/N] " ans || ans=""
    if [[ "$ans" =~ ^[Yy]$ ]]; then
        if claude mcp remove blockrun >/dev/null 2>&1; then
            ok "removed: blockrun MCP server"
        else
            warn "claude mcp remove failed; do it manually if needed: claude mcp remove blockrun"
        fi
    else
        ok "kept the blockrun MCP server (you can still use it for other tools)"
    fi
fi

say ""
say "Done. Restart Claude Code to drop the slash commands from completion."
