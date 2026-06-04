# Changelog

All notable changes to this project are documented here. Versions track
`plugin.json`. Dates are release dates.

## [0.3.0]

### Added
- `/launch-film` is now self-contained and far more capable:
  - **9:16 vertical starter** (`skills/launch-film/starter-vertical/`) alongside
    the 16:9 starter — both lint-clean and render-tested.
  - **`finish.sh` pro upgrades:** named grades `LOOK=warm-doc|cool-tech|noir`,
    `PRECISE=1` 2-pass to hit `TARGET_MB` exactly, `NORMALIZE_AUDIO=1`
    (loudnorm −14 LUFS), in-place-overwrite guard, and a motion self-check.
  - **`sound-design.sh`** — synthesizes whoosh/tick/sub/riser hits with pure
    ffmpeg and mixes them onto the film at your cut timestamps.

### Fixed
- Removed private-context leakage ("Your Majesty") from `prompts/poster.md` and
  `prompts/dance.md`.
- Manual install path (INSTALL.md) and README now symlink/list all **four**
  skills — `/launch-film` was previously dropped from the manual path.
- Version/roadmap consistency: README + `docs/COSTS.md` now reflect v0.2's four
  commands (was mislabeled "v1.0 / three commands").
- `docs/PROMPTS.md`: the `/dance --model` override is marked roadmap (not yet
  wired into the skill) instead of implying it works today.
- `.gitignore`: ignore `examples/_inputs/` and launch-film starter render output.

### Changed
- Added CI (`.github/workflows/ci.yml`), `CONTRIBUTING.md`, and this changelog.

## [0.2.0]

### Added
- **`/launch-film`** — direct + finish a cinematic product launch film
  (HyperFrames composition + no-dead-scene pacing + ffmpeg finish), with a
  render-tested 16:9 starter and the `finish.sh` tool.

### Fixed
- `.mcp.json` wrapped in the required `mcpServers` key (was top-level).
- `install.sh`/`uninstall.sh`: looser `claude mcp list` grep; guarded
  `git pull --ff-only` so a dirty bundle no longer aborts install.
- Doc count inconsistencies (headshot styles, dance presets, poster flag,
  `normalize_case.py` source-repo count).

## [0.1.0]

### Added
- Initial release: `/headshot`, `/dance`, `/poster` via the BlockRun MCP
  (x402 USDC on Base), plus the 848-case prompt library and one-line installer.
