#!/usr/bin/env bash
# finish.sh — the cinematic finish pass for launch films.
#
# Applies a warm filmic grade + fine film grain + gentle vignette in a SINGLE
# pass, encoded straight from the SOURCE render. This is the whole trick: grain
# is high-frequency noise that defeats inter-frame compression, so if you grain
# a clip and THEN re-encode the grained file you get a 400 MB+ monster. Grading,
# graining, and encoding in one pass from the clean source keeps a 1080p/30
# minute-long film around ~25–30 MB — small enough to upload to Product Hunt,
# X, or a landing page without a second thought.
#
# Usage:
#   ./finish.sh INPUT.mp4 [OUTPUT.mp4]
#
# Environment overrides:
#   INTENSITY=subtle|normal|strong   grade + grain strength      (default normal)
#   CRF=21                           x264 quality, lower = bigger (default 21)
#   TARGET_MB=50                     auto-bump CRF once to fit    (default 50)
#   GRAIN=1                          set 0 to disable film grain  (default 1)
#   VIGNETTE=1                       set 0 to disable vignette    (default 1)
#
# Requires: ffmpeg, ffprobe (brew install ffmpeg).

set -euo pipefail

SRC="${1:-}"
[ -n "$SRC" ] || { echo "usage: finish.sh INPUT.mp4 [OUTPUT.mp4]" >&2; exit 2; }
[ -f "$SRC" ] || { echo "finish.sh: input not found: $SRC" >&2; exit 2; }
command -v ffmpeg  >/dev/null || { echo "finish.sh: ffmpeg not installed (brew install ffmpeg)"  >&2; exit 2; }
command -v ffprobe >/dev/null || { echo "finish.sh: ffprobe not installed (brew install ffmpeg)" >&2; exit 2; }

OUT="${2:-${SRC%.*}-finished.mp4}"
INTENSITY="${INTENSITY:-normal}"
CRF="${CRF:-21}"
TARGET_MB="${TARGET_MB:-50}"
GRAIN="${GRAIN:-1}"
VIGNETTE="${VIGNETTE:-1}"

# Grade strength per intensity. Warm = lift reds, drop blues (colorbalance);
# a touch of contrast + saturation + a slight gamma lift reads as "film".
case "$INTENSITY" in
  subtle) CONTRAST=1.03; SAT=1.04; GAMMA=0.99; WARM=0.015; NOISE=6  ;;
  normal) CONTRAST=1.05; SAT=1.06; GAMMA=0.98; WARM=0.020; NOISE=8  ;;
  strong) CONTRAST=1.08; SAT=1.10; GAMMA=0.97; WARM=0.030; NOISE=12 ;;
  *) echo "finish.sh: INTENSITY must be subtle|normal|strong" >&2; exit 2 ;;
esac

build_vf() {
  local vf="eq=contrast=${CONTRAST}:saturation=${SAT}:gamma=${GAMMA}"
  vf+=",colorbalance=rs=${WARM}:rm=${WARM}:bs=-${WARM}:bm=-${WARM}"
  [ "$GRAIN" = "1" ]    && vf+=",noise=alls=${NOISE}:allf=t+u"
  [ "$VIGNETTE" = "1" ] && vf+=",vignette=PI/5"
  printf '%s' "$vf"
}

encode() { # $1 = crf
  ffmpeg -y -i "$SRC" -vf "$(build_vf)" \
    -c:v libx264 -preset slow -crf "$1" -pix_fmt yuv420p \
    -c:a copy -movflags +faststart "$OUT" -loglevel error
}

size_mb() { echo $(( $(wc -c < "$1") / 1000000 )); }

echo "==> finish: $INTENSITY grade, grain=$GRAIN vignette=$VIGNETTE, crf $CRF, from $SRC"
encode "$CRF"
MB=$(size_mb "$OUT")

# One automatic quality step-down if we blew past the platform target.
if [ "$MB" -gt "$TARGET_MB" ]; then
  NEWCRF=$(( CRF + 3 ))
  echo "==> ${MB}MB > ${TARGET_MB}MB target — re-encoding at crf ${NEWCRF}"
  encode "$NEWCRF"
  MB=$(size_mb "$OUT")
fi

DUR=$(ffprobe -v error -select_streams v:0 -show_entries format=duration -of default=nk=1:nw=1 "$OUT" 2>/dev/null | cut -d. -f1)
echo "==> done: $OUT  (${MB}MB, ${DUR}s)  — audio copied through untouched"
echo "    verify motion survived:  ffmpeg -ss 2 -i \"$OUT\" -frames:v 1 /tmp/check.png"
