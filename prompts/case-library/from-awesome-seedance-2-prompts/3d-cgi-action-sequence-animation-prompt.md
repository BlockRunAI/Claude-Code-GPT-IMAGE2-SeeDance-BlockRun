---
title: "3D CGI Action Sequence Animation Prompt"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/bd0e7ad5572619cf38f14807e52b4d56/thumbnails/thumbnail.jpg"
    alt: ""
---

![demo](https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/bd0e7ad5572619cf38f14807e52b4d56/thumbnails/thumbnail.jpg)

## Original prompt

Fast-paced editing cuts. 3D CGI animation with a real-time game engine feel, dynamic lighting, and post-processing bloom. Smooth 60fps visuals. The protagonist is a beautiful female warrior. The animation unfolds to the rhythm of music as follows: A lithe warrior in flowing attire sprints forward at a blurred speed, unsheathing a blade mid-run with a crisp metallic ring. The camera zooms in to focus on the cold glint of the blade as she strikes an oncoming mechanical enemy. The warrior precisely side-steps to dodge a heavy projectile that grazes past her; time briefly slows down before she accelerates, spinning like a whirlwind to release a series of rapid slashes that leave glowing trails in the dim ruins. Elegantly leaping into the air, the warrior fires a barrage of energy projectiles from dual weapons, the barrage raining down like comets on a gathered group of enemies below, each impact explosion shaking the screen violently. A close-up shows the warrior's determined eyes locking onto a charging opponent, followed by a fluid roll-dodge that seamlessly transitions into a counter-thrust, the blade piercing through armor and erupting in sparks and debris. The camera shifts to a wide angle, showing the warrior weaving through a dense barrage of laser fire, her body twisting in acrobatic flips, each move blurring into the next as she closes in for a devastating overhead strike. In a burst of explosive acceleration, the warrior summons illusory projectiles circling her before charging forward like a comet; the resulting shockwave spreads outward, shattering barriers and enemies alike. Rapid-fire sequence: The warrior parries a claw attack with crossed blades, sparks flying, and immediately counters with ultra-high-speed thrusts, precisely piercing vital points as the enemy's frame collapses in slow-motion chaos. The warrior grapples a larger mechanical beast, quickly climbing while dodging its swings, reaching the top to deliver a diving attack that sends cracks spreading like webs across its surface, finally triggering a massive explosion. Amidst collapsing buildings, the warrior performs wall-run dodges transitioning into an aerial backflip, concluding with a ground shockwave that repels surrounding enemies in a ring of dust and energy. Final Burst: The warrior channels her inner power, her whole body glowing, releasing a flood of slashes and shots in every direction. The camera rotates around her, capturing the dizzying speed and overwhelming offensive power. The 15-second sequence is well-paced, with a cut rhythm designed to make scene transitions and emotional flow easy to follow.

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
