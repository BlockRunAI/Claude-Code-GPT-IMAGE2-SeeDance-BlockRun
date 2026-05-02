---
title: "Case 2-3-7-2 · Airplane Window to Cabin Interior (Dreamlike)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/07-continuity.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [poster]
inputs: {"image": "user-supplied"}
---

## Original prompt

Using @image1 as the first frame. The frame zooms in to the airplane window. Clouds drift slowly into the frame. One cloud is decorated with colorful candy dots, always centered in the frame, then slowly transforms into @image2 ice cream. Camera pulls back to the cabin interior. @image3 sitting by the window reaches out to grab the ice cream from outside the window, takes a bite, mouth covered in cream, face glowing with a sweet smile.

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/poster`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/07-continuity.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
