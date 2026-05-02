---
title: "Celebrity Airport Entry Scene"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://cms-assets.youmind.com/media/1777618757327_efkhjv_HHJ9JDYbYAAoQNx.jpg"
    alt: ""
---

![demo](https://cms-assets.youmind.com/media/1777618757327_efkhjv_HHJ9JDYbYAAoQNx.jpg)

## Original prompt

Style:

Ultra realistic mass celebrity entry scene. Single continuous shot. Handheld camera from crowd perspective. Natural micro-shake. No cuts. Documentary realism.

Audio:

Only natural environment sound loud crowd cheering, people shouting, rapid camera shutter clicks, phones recording audio, airport announcements echoing, footsteps, fabric movement, distant engine idle and rev.

Lighting:

Natural daylight through airport glass panels. Mixed reflections. Realistic shadows. Slight haze for depth.

Main Character:

A female celebrity in [@/image1] with, Calm, confident presence with a subtle controlled smile. Face must remain consistent.

SCENE

0-3s:

Handheld camera starts from inside the crowd behind barricades. Slight natural shake. People in front partially block the view. Phones raised high, some screens visible recording. Crowd is loud and restless and shouting "Sarah". Camera tries to find a clear view toward the arrival gate.

3-6s:

Camera lifts slightly above shoulder level, shaky but controlled. Focus shifts between heads, waving hands, and glimpses of the arrival gate. Media cameras flash. Anticipation builds as people lean forward.

6-10s:

Security suddenly steps in, pushing the crowd slightly back. Camera reacts naturally with a small shake. Through the gaps, the celebrity becomes visible in the distance, slightly blurred at first, then gradually clearer as she walks forward with bodyguards.

10-13s:

Camera zooms slightly (natural handheld push-in feel). Celebrity now clearly visible, walking confidently in center. Security clears the path. She raises his hand and gives a calm wave with a slight smile. Camera struggles slightly to keep her in frame as people move.

13-15s:

Camera tilts and shifts trying to follow her as she reaches her convoy. Partial view of Mercedes Benz, with Mercedes G63 and Innova behind. A bodyguard opens the door of the car. The celebrity enters quickly. Engine revs. Vehicles begin moving forward. Camera lifts slightly as people jump to see.

Fade to black.

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
