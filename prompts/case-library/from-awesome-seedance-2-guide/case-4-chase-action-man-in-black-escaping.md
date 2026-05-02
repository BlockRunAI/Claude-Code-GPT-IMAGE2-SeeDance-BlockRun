---
title: "Case 4 · Chase Action — Man in Black Escaping"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/README.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [ui-system]
inputs: {"image": "user-supplied"}
assets:
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/1/1-4/ref1.png"
    alt: ""
  - kind: image
    url: "https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/1/1-4/result.jpg"
    alt: ""
---

![demo](https://pub-babc88c25d274cfeb8b2ae0cd0816872.r2.dev/assets/1/1-4/ref1.png)

## Original prompt

Camera follows the man in black as he flees rapidly, with a group of people chasing behind. Camera switches to side tracking shot. The character panics and knocks over a fruit stand, gets up and continues fleeing. Chaotic crowd sounds.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/README.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/BlockRunAI/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
