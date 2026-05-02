---
title: "Case 2-3-8-3 · Lead Singer Replacement (Band Performance)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/08-video-editing.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ad-series]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-8/3/ref1.jpg"
    alt: "▶ ref1"
  - kind: video
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-8/3/ref1.mp4"
    alt: "▶ ref1"
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-8/3/result.jpg"
    alt: "▶ Click to Play"
  - kind: video
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-8/3/result.mp4"
    alt: "▶ Click to Play"
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-8/3/ref1.png"
    alt: ""
---

![▶ ref1](https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-8/3/ref1.jpg)

[▶️ Watch source video](https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-8/3/ref1.mp4)

## Original prompt

Replace the female lead singer in @video1 with the male lead singer from @image1. Movements completely mimic the original video. No cuts. Band singing music.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/08-video-editing.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[Claude Code-GPT-IMAGE2-SeeDance-BlockRun](https://github.com/BlockRunAI/Claude-Code-GPT-IMAGE2-SeeDance-BlockRun)
bundle. Reproduced with attribution; original license applies.
