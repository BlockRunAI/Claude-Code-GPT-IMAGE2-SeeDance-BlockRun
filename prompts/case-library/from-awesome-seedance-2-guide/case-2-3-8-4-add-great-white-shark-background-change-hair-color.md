---
title: "Case 2-3-8-4 · Add Great White Shark Background + Change Hair Color"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/08-video-editing.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ad-series]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-8/4/ref1.jpg"
    alt: "▶ ref1"
  - kind: video
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-8/4/ref1.mp4"
    alt: "▶ ref1"
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-8/4/result.jpg"
    alt: "▶ Click to Play"
  - kind: video
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-8/4/result.mp4"
    alt: "▶ Click to Play"
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-8/4/ref1.png"
    alt: ""
---

![▶ ref1](https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-8/4/ref1.jpg)

[▶️ Watch source video](https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-8/4/ref1.mp4)

## Original prompt

Change the woman's hair in @video1 to red long hair. The great white shark from @image1 slowly surfaces, showing half its head, behind her.

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
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
[cc-gpt-image2-seedance-blockrun](https://github.com/BlockRunAI/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
