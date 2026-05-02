---
title: "Case 2-3-3-2 · Fisheye Outfit Flash Cut"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/03-creative-effects.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, lookbook]
inputs: {"image": "user-supplied"}
---

## Original prompt

Reference the model's facial features from the first image. The model wears outfits from reference images 2-6, approaching the camera with mischievous, cold, cute, surprised, and cool poses. Each pose wears different clothing. Each change is accompanied by a scene cut. Reference the fisheye lens effect and double-image flashing dazzle effect from @video1.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/03-creative-effects.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
