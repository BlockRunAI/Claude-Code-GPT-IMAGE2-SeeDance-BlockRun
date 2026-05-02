---
title: "Traditional Chinese Ink Wash Video Generation"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ad-series]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/c578c92dc2b1331ad88f0c5cec1fdc78/thumbnails/thumbnail.jpg"
    alt: ""
---

![demo](https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/c578c92dc2b1331ad88f0c5cec1fdc78/thumbnails/thumbnail.jpg)

## Original prompt

Strictly maintain the traditional Chinese ink wash style, character image, scene, and composition of the original image. Light rain continues to fall, with ripples on the water surface constantly spreading; a black-awning boat slowly rows under a bridge, the oars stirring the water. Weeping willow branches sway gently in the wind; the scholar slightly raises his head, looking toward the distant green mountains. The camera has a slight breathing sensation, slowly panning left a bit. The movement is natural and smooth, without flickering or dropped frames, and the ink wash texture remains consistent. 10 seconds, 1080p, 60fps.

## Run via Claude Code

After installing `Claude Code-GPT-IMAGE2-SeeDance-BlockRun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/ad-series (v1.2)`.

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
