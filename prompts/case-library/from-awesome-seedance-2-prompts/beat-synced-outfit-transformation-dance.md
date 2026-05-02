---
title: "Beat-Synced Outfit Transformation Dance"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [dance, lookbook]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://pbs.twimg.com/media/HG_FqHJboAA5vAe.jpg"
    alt: ""
---

![demo](https://pbs.twimg.com/media/HG_FqHJboAA5vAe.jpg)

## Original prompt

Have the character from Image 1 perform the dance based on the breakdown in Image 3. During the performance, include a beat-synced transformation into the character from Image 2. After the transformation, the character from Image 2 continues and completes the remaining dance steps from Image 3. Emphasize precise beat matching with the music

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
