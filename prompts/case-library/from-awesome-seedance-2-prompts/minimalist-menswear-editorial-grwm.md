---
title: "Minimalist Menswear Editorial GRWM"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, lookbook, ad-series, minimalist]
inputs: {"image": "user-supplied"}
assets:
  - kind: image
    url: "https://cms-assets.youmind.com/media/1777618769342_267a8h_HHI_fSibcAAbS4N.jpg"
    alt: ""
---

![demo](https://cms-assets.youmind.com/media/1777618769342_267a8h_HHI_fSibcAAbS4N.jpg)

## Original prompt

REFERENCE IMAGE: Use the provided 4×4 male storyboard collage as visual guide for framing, pacing, outfit flow, and transitions.

CONCEPT: Get Ready With Me — Modern Minimal Menswear (Clean, Sharp Look)

TIMELINE:
0:00–0:04
Dark fitted tee (espresso / charcoal tone)
Ivory tailored trousers
Clean tuck-in adjustment
Mirror check, subtle posture shift

0:04–0:08
Light blue shirt layering (open, relaxed fit)
Beige blazer on shoulders
Sleeve adjustment (watch visible)
Body turn, confident stance

0:08–0:12
Leather strap watch close-up
Minimal pendant necklace placement
Brown belt fastening (crisp motion)
Sunglasses on, sharp expression

0:12–0:15
White sneakers step-in
Walking shot (slow, editorial stride)
Leather tote bag grab
Final full look pose, composed and confident

STYLE: Neutral menswear palette (espresso, ivory, beige, soft blue), Soft natural indoor lighting, Warm tones, clean aesthetic interior, Luxury editorial, minimal and sharp.

MODEL: Single male subject, Modern hairstyle, slightly textured, Calm, confident, effortless expressions, Editorial posture, no exaggeration.

CAMERA: Close-ups + mid shots, Shallow depth of field, Steady framing, subtle handheld realism, Focus on fabric, tailoring, and textures.

TRANSITIONS: Match cuts (tuck → belt → blazer), Fabric motion transitions, Clean jump cuts synced with movement, Smooth pacing, visually satisfying flow.

OUTPUT: 4:5 vertical video, Loopable ending (final pose blends into start), Pinterest-style luxury aesthetic, Clean, smooth, premium GRWM

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
