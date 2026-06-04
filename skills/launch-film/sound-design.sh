#!/usr/bin/env bash
# sound-design.sh — the "last 10%" you hear but can't see.
#
# Synthesizes launch-film sound-design hits with pure ffmpeg (no asset files)
# and mixes them onto the video at your cut/beat timestamps. Deterministic.
#
# Usage:
#   ./sound-design.sh INPUT.mp4 OUTPUT.mp4 "T:TYPE" ["T:TYPE" ...]
#     T    = seconds (e.g. 6.3)
#     TYPE = whoosh | tick | sub | riser
#
# Types:
#   whoosh — transition swell (scene crossfade)
#   tick   — crisp UI/reveal click (a word lands, a tag appears)
#   sub    — low impact thud (a number / logo lands)
#   riser  — rising tension sweep into a CTA (place ~1.5s before the CTA)
#
# Example (matches the bundled starter's beats):
#   ./sound-design.sh film.mp4 film-sfx.mp4 6.3:whoosh 12.3:whoosh 12.9:tick 17.8:riser 19.0:sub
#
# Env:  SFX_GAIN=0.8  (master SFX level, 0–1.5; default 0.8)
# Requires: ffmpeg, ffprobe.

set -euo pipefail

SRC="${1:-}"; OUT="${2:-}"
{ [ -n "$SRC" ] && [ -n "$OUT" ] && [ "$#" -ge 3 ]; } || {
  echo 'usage: sound-design.sh INPUT.mp4 OUTPUT.mp4 "T:TYPE" ["T:TYPE" ...]' >&2; exit 2; }
[ -f "$SRC" ] || { echo "sound-design.sh: input not found: $SRC" >&2; exit 2; }
[ "$SRC" -ef "$OUT" ] 2>/dev/null && { echo "sound-design.sh: refusing in-place overwrite" >&2; exit 2; }
command -v ffmpeg >/dev/null && command -v ffprobe >/dev/null || { echo "sound-design.sh: needs ffmpeg+ffprobe (brew install ffmpeg)" >&2; exit 2; }
shift 2

SFX_GAIN="${SFX_GAIN:-0.8}"
TMP="$(dirname "$OUT")/.sfx-tmp"; mkdir -p "$TMP"
trap 'rm -rf "$TMP"' EXIT
SR=48000

# Synthesize one SFX (mono→stereo, 48k) into $2 for TYPE $1.
synth() {
  case "$1" in
    whoosh) ffmpeg -y -f lavfi -i "anoisesrc=d=0.5:c=pink:a=0.6:r=$SR" \
              -af "highpass=f=250,lowpass=f=4500,afade=t=in:d=0.20:curve=ipar,afade=t=out:st=0.22:d=0.28,volume=0.55,aformat=channel_layouts=stereo" "$2" -loglevel error ;;
    tick)   ffmpeg -y -f lavfi -i "sine=frequency=2300:duration=0.05:sample_rate=$SR" \
              -af "afade=t=out:d=0.048:curve=exp,volume=0.45,aformat=channel_layouts=stereo" "$2" -loglevel error ;;
    sub)    ffmpeg -y -f lavfi -i "sine=frequency=55:duration=0.38:sample_rate=$SR" \
              -af "afade=t=out:d=0.35:curve=exp,volume=0.9,aformat=channel_layouts=stereo" "$2" -loglevel error ;;
    riser)  ffmpeg -y -f lavfi -i "aevalsrc='0.4*sin(2*PI*(180*t+120*t*t))':d=1.6:s=$SR" \
              -af "afade=t=in:d=1.2:curve=ipar,afade=t=out:st=1.45:d=0.15,volume=0.6,aformat=channel_layouts=stereo" "$2" -loglevel error ;;
    *) echo "sound-design.sh: unknown TYPE '$1' (use whoosh|tick|sub|riser)" >&2; exit 2 ;;
  esac
}

HAS_AUDIO=$(ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "$SRC" | head -1)
DUR=$(ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 "$SRC")

# Build inputs. Input 0 = video. Base audio = original track, or synthesized silence.
INPUTS=(-i "$SRC")
if [ -n "$HAS_AUDIO" ]; then BASE="[0:a]"; idx=1
else INPUTS+=(-f lavfi -t "$DUR" -i "anullsrc=r=$SR:cl=stereo"); BASE="[1:a]"; idx=2; fi

FILTERS=(); MIX="$BASE"; n=0
for m in "$@"; do
  t="${m%%:*}"; type="${m##*:}"
  case "$t" in ''|*[!0-9.]*) echo "sound-design.sh: bad timestamp in '$m'" >&2; exit 2;; esac
  f="$TMP/s$idx.wav"; synth "$type" "$f"
  INPUTS+=(-i "$f")
  ms=$(awk -v t="$t" 'BEGIN{printf "%d", t*1000}')
  FILTERS+=("[$idx]adelay=${ms}|${ms}[d$idx]")
  MIX+="[d$idx]"; idx=$((idx+1)); n=$((n+1))
done

FC="$(IFS=';'; echo "${FILTERS[*]}");${MIX}amix=inputs=$((n+1)):normalize=0:dropout_transition=0[mx];[mx]volume=${SFX_GAIN},alimiter=limit=0.95[aout]"

echo "==> sound-design: $n hit(s) onto ${HAS_AUDIO:+existing }${HAS_AUDIO:-silent }track, gain=$SFX_GAIN"
ffmpeg -y "${INPUTS[@]}" -filter_complex "$FC" -map 0:v -map "[aout]" \
  -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart "$OUT" -loglevel error
echo "==> done: $OUT  —  $(( $(wc -c < "$OUT") / 1000000 ))MB, ${DUR%.*}s"
