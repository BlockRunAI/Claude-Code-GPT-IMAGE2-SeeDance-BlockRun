---
name: launch-film
description: |
  Direct and finish a product launch film — a 30–60s cinematic hero video
  for a Product Hunt / X / landing-page launch. Authors a HyperFrames HTML
  composition, paces every scene so nothing sits dead, renders to 1080p, then
  applies a one-pass cinematic finish (warm grade + fine film grain + vignette)
  sized for upload. The exact pipeline behind the Franklin Agent launch film.
triggers:
  - "launch video"
  - "launch film"
  - "product hunt video"
  - "hero video"
  - "promo video"
  - "make a launch trailer"
  - "cinematic finish"
  - "film grain"
  - "grade this video"
  - "色调电影感"
  - "产品发布视频"
user-invocable: true
allowed-tools: Bash(npm:*), Bash(npx:*), Bash(hyperframes:*), Bash(ffmpeg:*), Bash(ffprobe:*), Bash(mkdir:*), Bash(ls:*), Bash(cp:*), Bash(open:*), Bash(chmod:*), Read, Write, Edit
---

# `/launch-film` — direct + finish a cinematic product launch film

Takes a product brief and produces an upload-ready launch film with the same
craft as a professionally graded reference (Plasma / Reflect-tier): an
editorial, documentary look; **continuous motion in every scene** (no dead
holds); and a filmic finish pass that lifts a clean web render into something
that reads like film. Validated on the Franklin Agent Product Hunt launch
(`franklin-ph-v20.mp4`, 1080p/30, 54.6s, 28 MB).

This skill is **authoring + finishing**, not a single API call. It composes in
HyperFrames HTML (deterministic, seek-accurate) and finishes with `ffmpeg`. The
finish pass (`finish.sh`) is standalone — point it at **any** render, including
a Seedance clip from `/dance`, to give it the same grade.

## What "professional" actually is (the two gaps it closes)

Almost every self-made launch video fails the same two ways. This skill targets
exactly those:

1. **Dead scenes.** A card holds still for 6–8 seconds while the VO talks. The
   eye disengages. Fix: every scene carries a slow, continuous camera move for
   its *entire* duration, plus a beat in any lull.
2. **Flat finish.** A clean HTML/screen render looks like a render. Reference
   launch films are graded and grained. Fix: a single warm grade + fine grain +
   vignette pass — the single biggest perceived-quality jump available.

## Inputs

| Input | Required | Default | Notes |
|---|---|---|---|
| brief | yes | — | What you're launching + the beats (hook → problem → reveal → demo → proof → pricing → CTA). |
| `aspect` | no | `16:9` | `16:9` for Product Hunt / landing; `9:16` for Shorts/Reels/TikTok. |
| `duration` | no | `~50s` | 30–60s is the launch-film sweet spot. |
| `intensity` | no | `normal` | Finish strength: `subtle`, `normal`, `strong`. |
| `target_mb` | no | `50` | Upload ceiling; the finish auto-steps quality down once to fit. |

## Prerequisites

A HyperFrames project (`npm run render` available). If there isn't one:
`npx hyperframes init`. The **REQUIRED companion skills** for the authoring
mechanics — `data-*` timing attributes, `class="clip"`, `window.__timelines`
registration, shader-safe CSS — are the project's `hyperframes` and `gsap`
skills. This skill is the *director's layer* on top of them: pacing and finish.

## Workflow (Claude executes in order)

### Step 1 — Block the scenes

Turn the brief into 5–8 scenes on one root GSAP timeline. A proven launch arc:

> **hook** (a line that stops the scroll) → **problem** → **reveal** (the
> product name/wordmark) → **demo** (a terminal / UI / the thing working) →
> **proof** (model picker, logos, a number) → **pricing** → **CTA**.

Each scene is a `class="clip"` section with `data-start` / `data-duration` /
`data-track-index`, transitioning via blur-fade helpers:

```js
const tl = window.__timelines["root"];
const XB = 14, XD = 0.7;                 // transition blur px, duration
function trIn (sel, t, d){ tl.fromTo(sel,{opacity:0,filter:`blur(${XB}px)`},{opacity:1,filter:"blur(0px)",duration:d||XD,ease:"sine.inOut"},t); }
function trOut(sel, t, d){ tl.to    (sel,{opacity:0,filter:`blur(${XB}px)`,duration:d||XD,ease:"sine.inOut"},t); }
```

### Step 2 — The pacing rule: NObody holds still

**This is the core craft.** For every scene, add a *continuous* move that runs
the scene's whole length — not just the in/out transition. Pick per scene:

| Move | When to use | GSAP pattern (real, from the Franklin film) |
|---|---|---|
| **Push-in** | Hero portrait / product shot | `tl.fromTo("#s1-wm",{scale:1.0,opacity:0},{scale:1.14,opacity:.92,duration:8.2,ease:"sine.inOut",transformOrigin:"62% 42%"},0)` |
| **Drift** | Text-heavy / pricing cards | `tl.fromTo("#s6 .scene-pad",{y:10},{y:-14,duration:7.4,ease:"sine.inOut"},41.0)` |
| **Lean-in on a result** | Terminal / UI demo (`examples/03-terminal-camera.jpg`) | `tl.fromTo("#s3-term",{scale:0.96},{scale:1.13,duration:5.4,ease:"power1.inOut",transformOrigin:"50% 64%"},13.9)` |
| **Slow breathe** | Anything still otherwise | `tl.fromTo("#card",{scale:1.0},{scale:1.035,duration:5.2,ease:"sine.inOut"},t)` |

Then drop a **beat into any lull** — a moment of motion where the eye would
otherwise drift. The Franklin film's hook had a dead ~3–7s zone; a gold ink
underline drawing in fixed it and tied to the "wallet/money" theme:

```js
// a beat in the old dead zone
tl.fromTo("#s1-ink",{scaleX:0},{scaleX:1,duration:0.8,ease:"power2.inOut"},3.3);
// typewriter reveal works as a beat too
tl.fromTo("#s3-type",{clipPath:"inset(0 100% 0 0)"},{clipPath:"inset(0 0% 0 0)",duration:1.1,ease:"steps(46)"},14.5);
```

**Diagnostic — run it before rendering:** scrub the first 8 seconds. If *any*
element holds still for more than ~1.5s, the scene reads dead. Add a move.

The example frames `examples/01-front-pushin-early.jpg` (t≈1.8s) and
`examples/02-front-pushin-late.jpg` (t≈6.4s) show the same hook scene mid-move:
the portrait has scaled up, the ink underline has drawn in, the third line has
revealed — the card is never static.

### Step 3 — Validate, then render

```bash
npm run check        # lint + validate + inspect — fix all errors first
npm run render       # → renders/<project>_<timestamp>.mp4  (1080p/30)
```

Keep the VO/music/timeline intact across iterations — pacing and finish should
never desync narration.

### Step 4 — Cinematic finish pass (the biggest quality jump)

Run the bundled finish tool on the fresh render. It grades, grains, and encodes
in **one pass from the source**:

```bash
SRC=$(ls -t renders/*_*.mp4 | head -1)
INTENSITY=normal TARGET_MB=50 ./finish.sh "$SRC" renders/<name>-final.mp4
```

What it applies (warm filmic grade → fine grain → gentle vignette):

```
-vf "eq=contrast=1.05:saturation=1.06:gamma=0.98,\
     colorbalance=rs=0.02:rm=0.02:bs=-0.02:bm=-0.02,\
     noise=alls=8:allf=t+u,\
     vignette=PI/5"
-c:v libx264 -preset slow -crf 21 -pix_fmt yuv420p -c:a copy -movflags +faststart
```

`examples/04-cinematic-finish.jpg` is a graded frame: warm parchment, fine
grain, subtle corner vignette — still elegant, not muddied.

> **⚠️ The one mistake that costs you 400 MB.** Do **not** grain a clip and then
> re-encode the *grained* file — grain is high-frequency noise that defeats
> inter-frame compression and balloons the file (the Franklin grade did this:
> 443 MB). Always grade + grain + encode in **one pass from the clean source**.
> Same look, ~28 MB. `finish.sh` does this correctly; the danger is only if you
> hand-roll it.

### Step 5 — Verify motion survived, then ship

```bash
OUT=renders/<name>-final.mp4
ffprobe -v error -show_entries format=duration,size -of default=nk=1 "$OUT"
for t in 2 6 16; do ffmpeg -y -ss $t -i "$OUT" -frames:v 1 /tmp/v_$t.png -loglevel error; done
open "$OUT"
```

Confirm: front frames differ (push-in is moving), size is under `target_mb`,
audio plays. Report path + size + duration.

## Failure handling

| Symptom | Fix |
|---|---|
| Output is 300 MB+ | You re-encoded a grained file. Re-run `finish.sh` **from the clean source render**, not the graded one. |
| Front 8s feels dead | A scene is holding still. Add a continuous push-in/drift for the scene's whole duration (Step 2), plus a beat in the lull. |
| Grade looks muddy / crushed | Drop to `INTENSITY=subtle`, or `GRAIN=0` / `VIGNETTE=0` to isolate which layer is too strong. |
| Audio dropped after finish | `finish.sh` uses `-c:a copy`; if you hand-rolled ffmpeg you omitted it. Copy the audio stream through. |
| `npm run check` errors | Every timed element needs `data-start`/`data-duration`/`data-track-index` **and** `class="clip"`; timelines must be `paused` and on `window.__timelines`. See the `hyperframes` skill. |
| Motion gone after finish | Grain/CRF too aggressive hid subtle moves — lower `NOISE`, or raise scene move amplitude (scale delta ≥ 0.10). |

## Examples

```bash
/launch-film "Franklin Agent — agents that can pay. Product Hunt launch, ~50s."
/launch-film "DevTool X launch" --aspect 9:16 --intensity strong
# Finish-only: grade an existing render or a Seedance clip from /dance
./finish.sh ./blockrun-out/<ts>-dance/dance.mp4 dance-graded.mp4
INTENSITY=subtle GRAIN=0 ./finish.sh raw-screen-capture.mp4
```

## The look that ships (style notes from the Franklin film)

- **Editorial/documentary**, not "SaaS gradient": a parchment field, a serif
  display face for headlines, a mono micro-label above each (`PAY-AS-YOU-GO ·
  NO CREDIT CARD`), one restrained accent (gold).
- **One idea per scene.** The screen says less than the VO.
- **Transitions are blur-fades**, ~0.7s — soft, filmic, never hard cuts.
- **Sound design is the last 10%** the eye can't see but the ear feels:
  transition whooshes, a tick on reveals, a sub-thud on a number landing, a
  riser into the CTA. Add it after the picture locks.

## Cost

Free — local authoring + `ffmpeg`. No API calls. (If you generate B-roll for a
scene via `/dance` or Seedance, that clip is billed by that skill; pipe it
through `finish.sh` to match the film's grade for free.)
