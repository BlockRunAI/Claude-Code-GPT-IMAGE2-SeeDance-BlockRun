---
title: "Teenage Girl Basketball Freestyle"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [dance, ui-system, lookbook, ad-series, unbox, minimalist]
inputs: {"image": "user-supplied"}
assets:
  - kind: image
    url: "https://cms-assets.youmind.com/media/1777618712926_wshwnt_HHJ8j-4bUAAwJB0.jpg"
    alt: ""
---

![demo](https://cms-assets.youmind.com/media/1777618712926_wshwnt_HHJ8j-4bUAAwJB0.jpg)

## Original prompt

A high-quality cinematic video of a teenage girl performing a basketball freestyle routine, strictly following a structured 16-step choreography sequence (4x4 grid timing) over 10 seconds total duration.

Character:
A slim, athletic teenage girl with the same face and identity as the provided reference image (must remain consistent throughout the video). She has a slightly nerdy, awkward-cool charm, soft pale skin with light freckles, expressive eyes, and slightly messy light-toned hair tied loosely. She wears thin-frame glasses and a modern street basketball outfit: oversized jersey, loose shorts, crew socks, and high-top sneakers with subtle pastel accents (soft purple and light blue). Her personality feels shy-but-confident, revealing high-level freestyle skills.

Environment:
Minimal indoor basketball court studio. Clean wooden court floor with subtle markings, soft diffused lighting, light neutral walls, no distractions. Slight depth-of-field for a polished editorial sports look.

Style & Motion:
Smooth, controlled freestyle basketball flow. Natural body mechanics, realistic dribbling physics, fluid transitions between moves. Slight stylized cinematic feel but grounded in realism.

Camera:
Mostly medium full-body framing, slight dynamic tracking and subtle handheld feel. Occasional micro-zooms and angle shifts to enhance motion. Keep subject centered and clearly visible at all times.

⸻

⏱️ STRICT SEQUENCE (must follow exactly in order and timing)

Each move flows continuously into the next with no cuts:

Right-hand low dribble (controlled stance)
Behind-the-back transfer (right → left)
Quick crossover (left → right)
Between-the-legs dribble
Hesitation dribble (pause + fake shift)
Behind-the-back (reverse side)
Smooth 360° spin move (left direction)
Ball spin on finger (brief controlled balance)
Behind-the-back into crossover combo
Step-back motion with dribble
Fake pass (upper body feint)
Around-the-world ball motion
Behind-the-back + step-through footwork
Behind + crossover combo (tight control)
Quick low rapid dribble sequence
Stylish finish pose (confident stance, slight smile, holding ball)

⸻

🎯 Key Constraints:

The routine must strictly follow the exact step order (1–16)
Total duration: ~10 seconds (fast but readable transitions)
Ball must remain physically accurate and consistent in motion
No skipped or merged steps
No extra tricks beyond listed sequence
Character face must remain identical to reference throughout (no drift)
Maintain consistent outfit, proportions, and style

⸻

🎨 Visual Details:

Soft pastel accents in outfit subtly visible
Natural shadows and lighting consistency
Clean, minimal aesthetic (no clutter)
Slight motion trails or subtle emphasis can be added to highlight movement flow

## Run via Claude Code

After installing `Claude Code-GPT-IMAGE2-SeeDance-BlockRun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/dance`.

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
