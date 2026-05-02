---
title: "Motion Graphics Intro: Chaos Unit"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: image2image
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"image": "user-supplied"}
assets:
  - kind: image
    url: "https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/8b566fe91de8991fac09061e304eb6ba/thumbnails/thumbnail.jpg"
    alt: ""
---

![demo](https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/8b566fe91de8991fac09061e304eb6ba/thumbnails/thumbnail.jpg)

## Original prompt

Based on the three characters in the reference images. High definition, Unreal Engine rendering, cinematic quality, candy-colored palette, Japanese-style aesthetics, artistic, with strong sense of rhythm.

0–2s: Empty scene, a small dot at the center, thin-line UI frame, subtle particles. Text: “STATUS: STANDBY” “SYSTEM: INIT”.

2–4s: The fox on the left from image2 appears, riding a hovering skateboard, waves toward the camera. Curved motion trails behind. Text: “ID: 01” “CODENAME: RED” “ROLE: TACTICIAN”.

4–6s: The rabbit on the right from image1 appears, swings a carrot weapon and takes a combat stance. Circular motion trails. Text: “ID: 02” “CODENAME: KANA” "ROLE: EXECUTIONER” “WEAPON: CARROT”.

6–8s: The corgi from image3 appears, looks left and right, showing a simple, friendly smile. Concentric circle UI under its feet. Text: “ID: 03” “CODENAME: Arthur” “ROLE: COMMANDER”.

8–15s: The three characters align horizontally, from left to right: FIREBIRD, SAGE, MAD RABBIT. Snap alignment, unified circular platform beneath. Text: “SYSTEM SYNC COMPLETE” “UNIT READY”. Add UI overlay to each character: tracking frames, data bars, simplified charts. Text: “TRACKING” “ANALYSIS” “LOCKED”.

Large title “CHAOS UNIT” appears, breaking into geometric fragments that expand outward. Text: “SYSTEM ERROR” “DATA BREAK”. The fragments then reassemble into “CHAOS UNIT”, centered layout with subtle circular guide lines. Text: “REBUILD COMPLETE” “SYSTEM ONLINE” “KANAWORKS_AI”.

Final frame: “CHAOS UNIT” at the top, the three characters standing side by side below, with a clean circular platform at the bottom. Text: “STATUS: LOCKED” “UNIT: ACTIVE”.

## Run via Claude Code

After installing `Claude Code-GPT-IMAGE2-SeeDance-BlockRun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/ui-system (v1.1)`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=edit.
```

## Credit & license

Sourced from [awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md) by YouMind-OpenLab.
This case file is part of the curated `prompts/case-library/` in the
[Claude Code-GPT-IMAGE2-SeeDance-BlockRun](https://github.com/BlockRunAI/Claude-Code-GPT-IMAGE2-SeeDance-BlockRun)
bundle. Reproduced with attribution; original license applies.
