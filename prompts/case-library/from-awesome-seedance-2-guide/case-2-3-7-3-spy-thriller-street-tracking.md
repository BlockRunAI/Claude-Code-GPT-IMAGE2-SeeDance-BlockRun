---
title: "Case 2-3-7-3 · Spy Thriller Street Tracking"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/07-continuity.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [ui-system]
inputs: {"image": "user-supplied"}
assets:
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-7/3/result.jpg"
    alt: "▶ Click to Play"
  - kind: video
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-7/3/result.mp4"
    alt: "▶ Click to Play"
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-7/3/ref1.png"
    alt: ""
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-7/3/ref2.png"
    alt: ""
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-7/3/ref3.png"
    alt: ""
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-7/3/ref4.png"
    alt: ""
---

![▶ Click to Play](https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-7/3/result.jpg)

[▶️ Watch source video](https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/2-3-7/3/result.mp4)

## Original prompt

Spy thriller style. @image1 as the first frame. Camera frontal tracking shot of a woman in a red windbreaker walking forward. Full-frame camera follows, with pedestrians constantly blocking the red-clothed woman. She reaches a corner, references the corner building from @image2. Fixed camera, the red-clothed woman leaves the frame and disappears around the corner. A masked girl hiding at the corner stares fiercely at her. The masked girl's image references @image3, only the image, the girl stands at the corner. Camera pans forward toward the red-clothed special agent. She walks into a mansion and disappears. The mansion references @image4. No cuts throughout, one continuous shot.

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/ui-system (v1.1)`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/07-continuity.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/BlockRunAI/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
