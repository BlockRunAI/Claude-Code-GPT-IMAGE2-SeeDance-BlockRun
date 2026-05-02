---
title: "Seedance 2.0 Storyboard-to-Animation Prompt"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [dance]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://cms-assets.youmind.com/media/1777618782285_gcrv30_HHK2AbuasAAVtYn.jpg"
    alt: ""
---

![demo](https://cms-assets.youmind.com/media/1777618782285_gcrv30_HHK2AbuasAAVtYn.jpg)

## Original prompt

Use the provided storyboard image @image1 as the primary visual reference for composition, framing, and scene progression. Generate a 15-second stylized 3D animated cinematic video that follows the exact sequence and visual storytelling of the storyboard.

## Run via Claude Code

After installing `Claude Code-GPT-IMAGE2-SeeDance-BlockRun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/dance`.

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
