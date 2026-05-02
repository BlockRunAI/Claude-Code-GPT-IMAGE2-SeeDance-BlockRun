---
title: "例 371：Scrapbook 真人图与迷你分身"
source_repo: awesome-gpt-image-2
source_url: https://github.com/freestylefly/awesome-gpt-image-2/blob/main/docs/gallery-part-2.md
credit: freestylefly
workflow: image2image
model: openai/gpt-image-2
tags: [lookbook, ad-series]
inputs: {"image": "user-supplied"}
assets:
  - kind: image
    url: "https://raw.githubusercontent.com/freestylefly/awesome-gpt-image-2/main/data/images/case371.jpg"
    alt: "Scrapbook 真人图与迷你分身"
---

![Scrapbook 真人图与迷你分身](https://raw.githubusercontent.com/freestylefly/awesome-gpt-image-2/main/data/images/case371.jpg)

## Original prompt

Transform the provided reference image into a cozy aesthetic scrapbook-style composition while strictly preserving the original subject, identity, pose, lighting, and background.

Add multiple small “mini version” characters of the same person (chibi / doll-like style), placed naturally around the scene (on objects, table, shoulder, etc.). These mini figures must match the subject’s face, hairstyle, outfit, and vibe consistently, styled as cute 3D collectible figurines. Show them doing different activities (reading, posing, taking photos, relaxing).

Overlay handwritten-style doodles and annotations across the image: arrows, hearts, stars, sparkles, icons, and playful captions connected to elements in the scene.

Use a soft pastel color palette (white base with pink, peach, blue accents).

Keep the frame visually rich and filled but balanced and clean.

Style: warm, cozy lighting, dreamy Instagram scrapbook aesthetic, soft depth of field, highly detailed, polished but playful.

The final result must look like the SAME original image enhanced with mini alter-egos and aesthetic annotations — not a recreated or different scene.

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/lookbook (v1.2)`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=openai/gpt-image-2,
  action=edit.
```

## Credit & license

Sourced from [awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2/blob/main/docs/gallery-part-2.md) by freestylefly.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/BlockRunAI/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
