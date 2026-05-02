---
title: "Case 76: [Miyazaki-style short film pipeline](https://x.com/happycapyai/status/2049468986828697940) (by [@happycapyai](h"
source_repo: awesome-gpt-image-2-prompts
source_url: https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts/blob/main/cases/comparison.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [dance, poster, ghibli, ui-system]
inputs: {"text": true}
---

## Original prompt

Given a story concept, generate a complete Miyazaki-style animated short film: write a 30-shot script → generate watercolor storyboard images (gpt-image-1) → plan SOFT/HARD transitions → produce video clips with Seedance 2.0 using first/last-frame binding → synthesize the original ambient piano score → stitch everything into a final MP4 with music.

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/dance`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-gpt-image-2-prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts/blob/main/cases/comparison.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
