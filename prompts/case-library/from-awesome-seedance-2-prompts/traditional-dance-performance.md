---
title: "Traditional Dance Performance"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: image2image
model: bytedance/seedance-2.0-fast
tags: [dance, ui-system, ad-series]
inputs: {"image": "user-supplied"}
assets:
  - kind: image
    url: "https://pbs.twimg.com/media/HHAdco5aQAAtTCa.jpg"
    alt: ""
---

![demo](https://pbs.twimg.com/media/HHAdco5aQAAtTCa.jpg)

## Original prompt

Use the first reference image as the exact choreography and motion-process guide. Use the second reference image as the identity reference for the adult woman dancer.

Create a graceful traditional dance performance that follows all 16 illustrated steps in order, from the confident opening pose to the respectful closing pose. The dancer performs with poised posture, soft knee bends, precise cross steps, elegant wrist waves, curved fingers, shoulder accents, hip sways, flowing turns, and expressive selendang sweeps.

Keep the camera in a clean full-body cinematic frame, mostly front-facing, with slow controlled movement that supports the dance instead of distracting from it. During the left and right turns, allow a subtle circular camera drift, then return to a centered frontal composition. The dancer’s hands, feet, facial expression, and selendang fabric must remain visible throughout.

Use soft studio lighting, refined contrast, and a calm traditional performance atmosphere. The motion should feel smooth, rhythmic, respectful, and feminine, with the selendang floating naturally as the dancer glides forward and backward. End on a still closing pose with hands at the heart, peaceful smile, and elegant silence.

## Run via Claude Code

After installing `Claude Code-GPT-IMAGE2-SeeDance-BlockRun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/dance`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=edit.
```

## Credit & license

Sourced from [awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md) by YouMind-OpenLab.
This case file is part of the curated `prompts/case-library/` in the
[Claude Code-GPT-IMAGE2-SeeDance-BlockRun](https://github.com/BlockRunAI/Claude-Code-GPT-IMAGE2-SeeDance-BlockRun)
bundle. Reproduced with attribution; original license applies.
