#!/usr/bin/env bash
# finish.sh — the cinematic finish pass for launch films.
#
# Grade + film grain + vignette in a SINGLE pass, encoded straight from the
# SOURCE render. Graining and re-encoding a grained file balloons it to 400 MB+
# (grain is high-frequency noise that defeats inter-frame compression). One pass
# from the clean source keeps a 1080p/30 minute-long film around ~25–30 MB.
#
# Usage:
#   ./finish.sh INPUT.mp4 [OUTPUT.mp4]
#
# Environment overrides:
#   LOOK=warm-doc|cool-tech|noir     named color grade        (default warm-doc)
#   INTENSITY=subtle|normal|strong   grade + grain strength   (default normal)
#   CRF=21                           x264 quality, lower=bigger(default 21)
#   TARGET_MB=50                     size ceiling             (default 50)
#   PRECISE=1                        2-pass to hit TARGET_MB exactly (default 0)
#   NORMALIZE_AUDIO=1                loudnorm to -14 LUFS     (default 0)
#   GRAIN=0                          disable film grain       (default 1)
#   VIGNETTE=0                       disable vignette         (default 1)
#   VERIFY=0                         skip the motion self-check (default 1)
#
# Requires: ffmpeg, ffprobe (brew install ffmpeg).

set -euo pipefail

SRC="${1:-}"
[ -n "$SRC" ] || { echo "usage: finish.sh INPUT.mp4 [OUTPUT.mp4]" >&2; exit 2; }
[ -f "$SRC" ] || { echo "finish.sh: input not found: $SRC" >&2; exit 2; }
command -v ffmpeg  >/dev/null || { echo "finish.sh: ffmpeg not installed (brew install ffmpeg)"  >&2; exit 2; }
command -v ffprobe >/dev/null || { echo "finish.sh: ffprobe not installed (brew install ffmpeg)" >&2; exit 2; }

OUT="${2:-${SRC%.*}-finished.mp4}"
# Safety: never overwrite the source in place (-ef = same file; false if OUT absent).
if [ "$SRC" -ef "$OUT" ] 2>/dev/null; then
  echo "finish.sh: refusing to overwrite the source in place — choose a different OUTPUT" >&2; exit 2
fi

LOOK="${LOOK:-warm-doc}"
INTENSITY="${INTENSITY:-normal}"
CRF="${CRF:-21}"
TARGET_MB="${TARGET_MB:-50}"
PRECISE="${PRECISE:-0}"
NORMALIZE_AUDIO="${NORMALIZE_AUDIO:-0}"
GRAIN="${GRAIN:-1}"
VIGNETTE="${VIGNETTE:-1}"
VERIFY="${VERIFY:-1}"

# Resolve grade parameters: LOOK sets the color character, INTENSITY scales it.
read -r CONTRAST SAT GAMMA WARM NWARM VIG NOISE < <(awk -v look="$LOOK" -v inten="$INTENSITY" 'BEGIN{
  if(look=="warm-doc")      { c=0.05; s=0.06;  g=-0.02; w=0.020; v=5 }
  else if(look=="cool-tech"){ c=0.07; s=0.02;  g=0.00;  w=-0.020; v=6 }
  else if(look=="noir")     { c=0.12; s=-0.45; g=-0.04; w=0.000; v=4 }
  else { print "ERR_LOOK"; exit 1 }
  if(inten=="subtle")      { m=0.6; n=6 }
  else if(inten=="normal") { m=1.0; n=8 }
  else if(inten=="strong") { m=1.5; n=12 }
  else { print "ERR_INTENSITY"; exit 1 }
  printf "%.4f %.4f %.4f %.4f %.4f %d %d\n", 1+c*m, 1+s*m, 1+g*m, w*m, -(w*m), v, n
}')
case "$CONTRAST" in ERR_LOOK) echo "finish.sh: LOOK must be warm-doc|cool-tech|noir" >&2; exit 2;;
                    ERR_INTENSITY) echo "finish.sh: INTENSITY must be subtle|normal|strong" >&2; exit 2;; esac

build_vf() {
  local vf="eq=contrast=${CONTRAST}:saturation=${SAT}:gamma=${GAMMA}"
  vf+=",colorbalance=rs=${WARM}:rm=${WARM}:bs=${NWARM}:bm=${NWARM}"
  [ "$GRAIN" = "1" ]    && vf+=",noise=alls=${NOISE}:allf=t+u"
  [ "$VIGNETTE" = "1" ] && vf+=",vignette=PI/${VIG}"
  printf '%s' "$vf"
}

# Audio: normalize, copy, or drop depending on what's present + requested.
HAS_AUDIO=$(ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "$SRC" | head -1)
audio_args() {
  if [ -z "$HAS_AUDIO" ]; then echo "-an"
  elif [ "$NORMALIZE_AUDIO" = "1" ]; then echo "-af loudnorm=I=-14:TP=-1.5:LRA=11 -c:a aac -b:a 192k"
  else echo "-c:a copy"; fi
}

DUR=$(ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 "$SRC")
size_mb() { echo $(( $(wc -c < "$1") / 1000000 )); }

if [ -z "$HAS_AUDIO" ]; then AUDIO_DESC="none"
elif [ "$NORMALIZE_AUDIO" = "1" ]; then AUDIO_DESC="loudnorm -14LUFS"
else AUDIO_DESC="passthrough"; fi

echo "==> finish: look=$LOOK intensity=$INTENSITY grain=$GRAIN vignette=$VIGNETTE audio=$AUDIO_DESC"

if [ "$PRECISE" = "1" ]; then
  # 2-pass to hit TARGET_MB precisely. Reserve audio + 6% mux headroom.
  AUDIO_KBPS=$([ -n "$HAS_AUDIO" ] && { [ "$NORMALIZE_AUDIO" = "1" ] && echo 192 || echo 160; } || echo 0)
  VBIT=$(awk -v mb="$TARGET_MB" -v d="$DUR" -v a="$AUDIO_KBPS" 'BEGIN{ printf "%d", (mb*8192*0.94)/d - a }')
  [ "$VBIT" -ge 200 ] || { echo "finish.sh: TARGET_MB too small for ${DUR}s — computed ${VBIT}kbps" >&2; exit 2; }
  echo "    precise: 2-pass @ ${VBIT}kbps video to fit ${TARGET_MB}MB"
  PLOG="$(dirname "$OUT")/.finish-pass"
  ffmpeg -y -i "$SRC" -vf "$(build_vf)" -c:v libx264 -preset slow -b:v "${VBIT}k" -pass 1 -passlogfile "$PLOG" -an -f mp4 /dev/null -loglevel error
  ffmpeg -y -i "$SRC" -vf "$(build_vf)" -c:v libx264 -preset slow -b:v "${VBIT}k" -pass 2 -passlogfile "$PLOG" -pix_fmt yuv420p $(audio_args) -movflags +faststart "$OUT" -loglevel error
  rm -f "${PLOG}"-*.log "${PLOG}"-*.log.mbtree 2>/dev/null || true
else
  encode() { ffmpeg -y -i "$SRC" -vf "$(build_vf)" -c:v libx264 -preset slow -crf "$1" -pix_fmt yuv420p $(audio_args) -movflags +faststart "$OUT" -loglevel error; }
  echo "    crf $CRF from $SRC"
  encode "$CRF"
  if [ "$(size_mb "$OUT")" -gt "$TARGET_MB" ]; then
    NEWCRF=$(( CRF + 3 )); echo "==> $(size_mb "$OUT")MB > ${TARGET_MB}MB — re-encoding at crf ${NEWCRF}"; encode "$NEWCRF"
  fi
fi

MB=$(size_mb "$OUT")
echo "==> done: $OUT  —  ${MB}MB, ${DUR%.*}s, audio=$AUDIO_DESC"

# Motion self-check: sample 3 frames across the first third; near-identical sizes
# usually means a dead/static opening. Heuristic aid, not a guarantee.
if [ "$VERIFY" = "1" ]; then
  TMP=$(dirname "$OUT"); a=0; mn=999999999; mx=0
  for t in 1.5 $(awk -v d="$DUR" 'BEGIN{printf "%.2f", d*0.18}') $(awk -v d="$DUR" 'BEGIN{printf "%.2f", d*0.30}'); do
    f="$TMP/.fcheck_$a.png"; ffmpeg -y -ss "$t" -i "$OUT" -frames:v 1 -update 1 "$f" -loglevel error 2>/dev/null || true
    [ -f "$f" ] && { sz=$(wc -c < "$f"); [ "$sz" -lt "$mn" ] && mn=$sz; [ "$sz" -gt "$mx" ] && mx=$sz; }
    a=$((a+1))
  done
  rm -f "$TMP"/.fcheck_*.png
  DELTA=$(( mx - mn ))
  THRESH=$(( mx / 50 ))
  if [ "$mx" -gt 0 ] && [ "$DELTA" -lt "$THRESH" ]; then
    echo "    [!] motion check: opening frames near-identical — front may be holding still. Add a push-in/drift."
  else
    echo "    [ok] motion check: opening frames differ by ${DELTA}B — front is moving."
  fi
fi
