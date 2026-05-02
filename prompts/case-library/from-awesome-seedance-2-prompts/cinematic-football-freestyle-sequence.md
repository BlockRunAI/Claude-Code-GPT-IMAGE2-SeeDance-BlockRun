---
title: "Cinematic Football Freestyle Sequence"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series, anime, minimalist]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://cms-assets.youmind.com/media/1777618706644_u90j36_HHH3ZskaUAA7811.jpg"
    alt: ""
---

![demo](https://cms-assets.youmind.com/media/1777618706644_u90j36_HHH3ZskaUAA7811.jpg)

## Original prompt

Create a 15-second ultra-realistic cinematic football freestyle video using image_1 as the main character, strictly following the 16-step sequence from image_2.

CHARACTER (VERY IMPORTANT):
A young adult man, athletic build, Southeast Asian appearance, short black hair, light stubble, wearing a black hoodie, black pants, and white sneakers.
Face must match image_1 exactly (100% facial consistency, realistic skin texture, natural lighting, no stylization).

STYLE:
Ultra-realistic cinematic, IMAX look, 4K–8K HDR, natural lighting, high detail, grounded physics, subtle motion blur, shallow depth of field. No anime, no cartoon, no over-glow effects.

LOCATION:
Clean minimal studio with plain white background (same as image_1), soft studio lighting, no distractions.

SEQUENCE (STRICT ORDER – FOLLOW image_2 EXACTLY):

0–1s: Player prepares with the ball in hands.
1–2s: Basic juggle (Step 01).
2–3s: Alternating foot juggle (Step 02).
3–4s: Around The World (Step 03).
4–5s: Reverse ATW (Step 04).
5–6s: Crossover (Step 05).
6–7s: Leg-over (Step 06).
7–8s: Neck stall (Step 07).
8–9s: Foot stall (Step 08).
9–10s: Knee stall (Step 09).
10–11s: Shoulder stall (Step 10).
11–12s: Hop the World (Step 11).
12–13s: Sit-down trick (Step 12).
13–14s: Ground combo → air transition (Step 13–14).
14–15s: Spin trick → final freestyle pose (Step 15–16).

CAMERA & MOTION:
Dynamic tracking shots, smooth follow camera, slight handheld feel.
Close-ups during tricks, medium shots for combos, slow motion on key moments (ATW, spin, final pose).
Natural motion blur, realistic ball physics.

IMPORTANT RULES:

Must follow all 16 steps in exact order from image_2
No skipping steps
Smooth continuous flow (no cuts)
Ball control must look realistic
Character face must remain identical to image_1

## Run via Claude Code

After installing `Claude Code-GPT-IMAGE2-SeeDance-BlockRun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/ui-system (v1.1)`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md) by YouMind-OpenLab.
This case file is part of the curated `prompts/case-library/` in the
[Claude Code-GPT-IMAGE2-SeeDance-BlockRun](https://github.com/BlockRunAI/Claude-Code-GPT-IMAGE2-SeeDance-BlockRun)
bundle. Reproduced with attribution; original license applies.
