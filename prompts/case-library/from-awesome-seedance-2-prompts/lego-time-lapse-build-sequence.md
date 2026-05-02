---
title: "LEGO Time-Lapse Build Sequence"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, lookbook, ad-series, unbox]
inputs: {"image": "user-supplied"}
assets:
  - kind: image
    url: "https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/b90f1ce87fc61e43b76d81c3d520419d/thumbnails/thumbnail.jpg"
    alt: ""
---

![demo](https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/b90f1ce87fc61e43b76d81c3d520419d/thumbnails/thumbnail.jpg)

## Original prompt

FORMAT: 15s / MULTI-SHOT / TIME-LAPSE BUILD SEQUENCE
STYLE: Bright, playful 3D animation, soft global illumination, vibrant colors, smooth cinematic motion, childlike warmth

⸻

CHARACTER SETUP:
•@img1 = main character (MUST remain EXACTLY as reference: no mouth, no nose, same mask, same proportions, same outfit, no alterations)
•@img2 = LEGO-style figurine model inspiration (final build result)

⸻

SCENE 1 (0s–3s) – ESTABLISHING

Full room view, warm sunlight pouring through a window onto a clean desk.
@img1 sits at the desk, posture slightly leaned forward, focused and calm.
LEGO pieces scattered across the table.
Camera: slow cinematic push-in.
Mood: peaceful, creative, bright daytime energy.

⸻

SCENE 2 (3s–6s) – TIME-LAPSE START

Time-lapse begins.
@img1 rapidly assembles LEGO bricks with precise, smooth hand movements.
Blocks snap together quickly, forming the base structure.
Camera: quick angle cuts (front → side → over-the-shoulder).
Lighting remains soft and sunlit.

⸻

SCENE 3 (6s–9s) – HAND DETAIL

Close-up on hands.
Fingers nimbly snapping LEGO pieces together with satisfying motion.
Bricks begin to resemble @img2’s form.
Camera tracks hand movement smoothly, shallow depth of field.

⸻

SCENE 4 (9s–12s) – BUILD PROGRESSION

Time-lapse intensifies.
The LEGO creation rapidly evolves into a clear version of @img2.
@img1’s body language shows focus shifting into excitement (head tilt, subtle posture lift — NO facial change since no mouth).
Camera: orbiting slow motion mixed with time-lapse.

⸻

SCENE 5 (12s–15s) – FINAL REVEAL

Time-lapse ends.
@img1 pauses, looks down at the finished LEGO figure (matching @img2).
Subtle head lift to acknowledge completion (no smile, expression conveyed through posture only).
Camera pulls back to wide shot, sunlight glowing over the desk.
Final frame: completed LEGO figure centered in view.

⸻

⚠️ STRICT CHARACTER RULES
•DO NOT add a mouth or nose to @img1
•DO NOT change head shape, mask, or textures
•DO NOT stylize @img1 into LEGO form
•Keep @img1 fully consistent with reference image at all times

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
