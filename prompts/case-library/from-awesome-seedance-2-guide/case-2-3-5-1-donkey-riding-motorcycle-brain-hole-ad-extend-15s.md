---
title: "Case 2-3-5-1 · Donkey Riding Motorcycle Brain-Hole Ad (Extend 15s)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/05-video-extension.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"image": "user-supplied"}
---

## Original prompt

Extend the video by 15 seconds. Reference @image1 and @image2 for the image of a donkey riding a motorcycle. Add a brain-hole advertisement segment.
Scene 1: Side fixed camera shot. Donkey rides motorcycle bursting out of the fence. Nearby chickens are startled.
Scene 2: Donkey rides motorcycle spinning in sand. First close-up of motorcycle tires, then cut to aerial overhead shot of donkey riding motorcycle doing spinning stunts, kicking up dust.
Scene 3: Background is snowy mountain shot. Donkey rides motorcycle flying over the mountain slope. Advertisement text appears behind the subject, appearing through masking in the middle: "Inspire Creativity, Enrich Life." Finally, as the motorcycle flies past, dust is kicked up.

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
