---
title: "Storyboard Animation Sequence"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [lookbook, ad-series]
inputs: {"image": "user-supplied"}
assets:
  - kind: image
    url: "https://cms-assets.youmind.com/media/1777618746090_rf98al_HHKKnchawAAutFt.jpg"
    alt: ""
---

![demo](https://cms-assets.youmind.com/media/1777618746090_rf98al_HHKKnchawAAutFt.jpg)

## Original prompt

Using the provided storyboard reference image, animate the character exactly as shown across all 16 panels in sequence. Follow each panel step by step — from panel 1 to panel 16 — capturing her arrival, setup, crowd forming, toprock, footwork, windmill, headspin, air freeze, power combo, cooldown, final pose, and bow. Match her face, outfit, sweat progression, and environment exactly as illustrated in the storyboard. Japanese street setting with kanji signage and summer lighting throughout. Smooth continuous motion, full color, cinematic quality, 15 seconds.

## Run via Claude Code

After installing `Claude Code-GPT-IMAGE2-SeeDance-BlockRun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/lookbook (v1.2)`.

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
