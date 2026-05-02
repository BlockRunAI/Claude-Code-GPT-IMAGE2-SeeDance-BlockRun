---
title: "Apocalyptic Jakarta Transformation"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/22324bc0a7c6e20b0829cfa7316889bf/thumbnails/thumbnail.jpg"
    alt: ""
---

![demo](https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/22324bc0a7c6e20b0829cfa7316889bf/thumbnails/thumbnail.jpg)

## Original prompt

Single continuous shot, no cuts. Opening with a medium static shot at approximately a 30° side angle.

Environment: a smoke-filled apocalyptic battlefield set in Jakarta. In the distance, ruined skyscrapers and abandoned high-rise buildings dominate the skyline. Strong winds carry light rain. The ground is cracked concrete scattered with metal debris, with puddles reflecting dim, cold light.

The camera slowly pushes forward.
A vehicle (@Image2 reference) rushes in from the distance at high speed, then performs a sudden hard brake, splashing water mist into the air. Motion blur emphasizes the speed and weight.
The protagonist (@Image1 reference) steps out of the car. His expression is serious and heavy. He looks toward the devastated city, exhales deeply, then lightly pats the car hood.
At that moment, the vehicle levitates and begins transforming—metal panels shifting and unfolding—into a blue humanoid mech (autobot-like). The transformation is powerful and mechanical, with sharp, precise movements.

The mech lands beside the protagonist. They stand side by side, facing forward, ready for battle.

Visual Style: highly realistic cinematic rendering, strong impact, dynamic motion blur on fast movements, sharp focus on key subjects. Atmospheric, epic scale, grounded realism.
Character Style: professional, authoritative digital human appearance.

Audio Style: authoritative, grounded tone design with intense, angry emotional atmosphere.
No dialogue. No background music. Only environmental sound, mechanical transformation, wind, rain, and distant destruction.

## Run via Claude Code

After installing `Claude Code-GPT-IMAGE2-SeeDance-BlockRun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/ui-system (v1.1)`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md) by YouMind-OpenLab.
This case file is part of the curated `prompts/case-library/` in the
[Claude Code-GPT-IMAGE2-SeeDance-BlockRun](https://github.com/BlockRunAI/Claude-Code-GPT-IMAGE2-SeeDance-BlockRun)
bundle. Reproduced with attribution; original license applies.
