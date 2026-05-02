---
title: "Case 2-3-1-3 · Complex Transition Consistency"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/01-consistency.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ad-series, unbox]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-1/3/ref1.jpg"
    alt: "▶ ref1"
  - kind: video
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-1/3/ref1.mp4"
    alt: "▶ ref1"
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-1/3/result.jpg"
    alt: "▶ Click to Play"
  - kind: video
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-1/3/result.mp4"
    alt: "▶ Click to Play"
---

![▶ ref1](https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-1/3/ref1.jpg)

[▶️ Watch source video](https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-1/3/ref1.mp4)

## Original prompt

Reference all transitions and camera movements from @video1, one continuous shot. The scene starts with a chessboard, camera pans left to reveal yellow sand on the floor, camera moves up to a beach with footprints. A girl in white simple clothing gradually walks away on the beach. Camera cuts to an aerial overhead view of the sea washing (no people visible). Seamless gradient transition as the washing waves transform into fluttering curtains. Camera pulls back to reveal a close-up of the girl's face. One continuous shot throughout.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/01-consistency.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/BlockRunAI/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
