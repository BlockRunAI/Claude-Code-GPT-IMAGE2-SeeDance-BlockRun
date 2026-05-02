---
title: "Case 2-3-2-1 · Hitchcock Zoom + Robotic Arm Orbit"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/02-camera-movement.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system]
inputs: {"text": true}
---

## Original prompt

Reference the man's image from @image1. He is in the elevator from @image2. Completely reference all camera movement effects and the protagonist's facial expressions from @video1. When the protagonist is frightened, apply Hitchcock zoom effect. Then several orbiting shots showing the elevator interior perspective. The elevator doors open, follow the camera walking out of the elevator. The scene outside the elevator references @image3. The man looks around. Reference @video1 using robotic arm multi-angle following the character's line of sight.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/02-camera-movement.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
