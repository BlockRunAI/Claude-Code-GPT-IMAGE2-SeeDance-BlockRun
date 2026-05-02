---
title: "Cinematic Emotional Face Close-up"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [headshot, poster, ui-system, ad-series]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/4a47ba646e7cedd79363c861864b8714/thumbnails/thumbnail.jpg"
    alt: ""
---

![demo](https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/4a47ba646e7cedd79363c861864b8714/thumbnails/thumbnail.jpg)

## Original prompt

A realistic human face with highly detailed skin texture, pores, and micro-musculature. Scene: Tight portrait close-up against a dark, void-like background. Style: Cinematic realism, 35mm film aesthetic, shallow depth of field with soft bokeh, moody and introspective. Lighting: Dynamic emotional lighting that shifts in color temperature and direction to match the internal state. Audio: Ambient atmospheric drone, soft rhythmic breathing, subtle emotional orchestral swells. Avoid: Identity drift, jitter, distorted limbs, unnatural morphing artifacts. [0-3s] Camera: Slow, imperceptible push-in. Action: The face breaks into a genuine, soft smile; eyes crinkle at the corners and the cheeks lift. Lighting: Warm golden-hour glow, soft and frontal. Vfx: Subtle lens flare. [3-6s] Camera: Static extreme close-up. Action: The smile dissolves into a heavy, downward curve; eyes well up with glistening tears that catch the light, and the lower lip trembles. Lighting: Transition to a cool, melancholy blue wash from above. [6-9s] Camera: Controlled lateral pan. Action: The brow furrows deeply into a sharp V-shape; the jaw clenches visibly, and nostrils flare with rhythmic, heavy breathing. Lighting: Harsh, high-contrast red and orange side-lighting creating deep shadows. [9-12s] Camera: Subtle handheld micro-shake for tension. Action: The eyes snap wide, pupils dilating; the face pales as the muscles go taut, and the mouth hangs slightly open in a shallow gasp. Lighting: Dim, desaturated, flickering low-key light. [12-15s] Camera: Gentle pull-out to a medium close-up. Action: All tension drains from the face; the eyes slowly close, and the features settle into a mask of perfect, serene stillness. Lighting: Soft, diffused white light enveloping the subject like a halo.

## Run via Claude Code

After installing `Claude Code-GPT-IMAGE2-SeeDance-BlockRun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/headshot`.

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
