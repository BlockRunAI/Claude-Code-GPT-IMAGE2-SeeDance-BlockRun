---
title: "Case 2-3-5-4 · Street Sunflowers (Extend Forward 10s)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/05-video-extension.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"text": true}
---

## Original prompt

10s
Extend forward by 10 seconds. In warm afternoon light, the camera starts from the street corner with a row of swaying awnings, slowly pans down to a few small daisies poking out at the base of the wall. Then the protagonist's red sneakers appear in the frame. He is crouching at a street flower stall, smiling as he gathers a large bouquet of sunflowers into his arms. Flower petals brush against his white T-shirt. As he turns to step on his skateboard, the flower stall owner smiles and shouts "Watch out for the petals flying!" He waves to the owner, then starts riding. Several golden petals have already escaped from the bouquet, falling onto the skateboard surface.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/05-video-extension.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
