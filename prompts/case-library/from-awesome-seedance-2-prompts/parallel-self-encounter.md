---
title: "Parallel Self Encounter"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/cdce3299d97aa8a36b243990b4f555c3/thumbnails/thumbnail.jpg"
    alt: ""
---

![demo](https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/cdce3299d97aa8a36b243990b4f555c3/thumbnails/thumbnail.jpg)

## Original prompt

Scene 1 (0-4s): Evening urban street, soft dusk lighting, shallow depth of field. Girl walking alone, suddenly stops. Across the street stands an identical version of her, staring directly. Subtle glitch effect, cinematic camera push-in.

Scene 2 (4-8s): Cross-cut visuals. Real version: neutral tones, slightly tired expression, slow movement. Parallel version: confident posture, smooth movement, warm golden lighting (or alternate darker cold tone for negative version). High contrast cinematic grading.

Scene 3 (8-12s): The girl steps forward slowly. The parallel version mirrors her movements perfectly but not as a reflection. Slight delay/glitch in synchronization. Camera handheld slight motion, building tension.

Scene 4 (12-16s): Both stand face to face. Close-up shot. Parallel version leans slightly forward. Cut to black.

On-screen text at end: “That’s not another version of you… it’s who you’re becoming.”

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
