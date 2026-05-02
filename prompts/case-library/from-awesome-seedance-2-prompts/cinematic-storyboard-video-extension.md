---
title: "Cinematic Storyboard Video Extension"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series, minimalist]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/97580446173eaa7bc1d491fe17804328/thumbnails/thumbnail.jpg"
    alt: ""
---

![demo](https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/97580446173eaa7bc1d491fe17804328/thumbnails/thumbnail.jpg)

## Original prompt

Scene 1 prompt: 
Use the attached storyboard sheet as the primary source of truth. 

@ Image1 Create a 15-second cinematic scene exactly following the timing, shots, and dialogue from the sheet. 

Characters: Indian man and Indian woman Location: modern apartment at night (living room + kitchen continuity) 

Style: cinematic realism, natural acting, subtle emotions 

Lighting: warm practical lighting with city lights 

outside Rules: 
Follow the exact shot timing and dialogue cadence from the sheet When a character speaks, keep them isolated in frame (close-up) Maintain realistic pacing, pauses, and micro-expressions 

Do not exaggerate acting or add extra dialogue Audio: soft ambient room tone + subtle background music, natural dialogue delivery.

Scene 2 prompt: 
Use @ video1 as the base continuity reference (same characters, positions, lighting, camera style, and emotional tone). 

Use @ image1 as the storyboard guide for the next 15 seconds (follow its timing, shot sequence, and dialogue exactly). 

Extend the scene naturally from where @ video1 ends. 

Rules: 
Maintain perfect visual continuity (same apartment layout, wardrobe, lighting, framing) 

Match character appearance and expressions exactly from @ video1 Follow @ image1 strictly for shot timing and dialogue cadence 

When a character speaks, keep them isolated in frame (close-up) Keep movements subtle, realistic, and emotionally grounded 

Preserve pauses and natural pacing Style: cinematic realism, warm indoor lighting, soft shadows, shallow depth of field 

Audio: natural dialogue delivery, soft ambient room tone, very subtle background score Do not add extra dialogue, actions, or cuts beyond @ image1.

Scene 3 prompt: 
Use @ video1 as the base continuity reference (same characters, positions, lighting, camera style, and emotional tone). 

Use @ image1 as the storyboard guide for the next 15 seconds (follow its timing, shot sequence, and dialogue exactly). 

Extend the scene naturally from where @ video1 ends. Rules: Maintain perfect visual continuity (same apartment layout, kitchen + living room positioning, wardrobe, lighting) Match facial features, expressions, and camera framing exactly from @ video1 Follow @ image1 strictly for shot timing and dialogue cadence 

When a character speaks, isolate them in frame (close-up) Keep movements minimal, realistic, and emotionally grounded 

Preserve pauses, eye contact beats, and subtle performance shifts 

Style: cinematic realism, warm indoor lighting, soft shadows, shallow depth of field Audio: natural dialogue delivery, soft ambient room tone, very subtle emotional background score 

Do not add extra dialogue, actions, or cuts beyond @ image1. 

Ensure smooth continuation with no visible jump cut—this should feel like a single continuous scene.

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
