---
title: "📁 Repository Structure"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/README.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"text": true}
assets:
  []
---

_No source-repo demo asset attached for this case._

## Original prompt

.
├── README.md              # This file (usage guide + featured cases + 10 capability library navigation)
└── use-cases/             # 10 major capability cases (complete prompts + videos)
    ├── en/
    │   ├── 01-consistency.md
    │   ├── 02-camera-movement.md
    │   ├── 03-creative-effects.md
    │   ├── 04-story-completion.md
    │   ├── 05-video-extension.md
    │   ├── 06-audio-voice.md
    │   ├── 07-continuity.md
    │   ├── 08-video-editing.md
    │   ├── 09-music-sync.md
    │   └── 10-emotion.md

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
