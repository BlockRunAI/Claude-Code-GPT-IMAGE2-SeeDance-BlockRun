---
title: "Urban Freestyle Dance Script"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [dance, ui-system, lookbook, ad-series]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://cms-assets.youmind.com/media/1777618764643_x5vg3h_HHJ49UpbcAAV0ZI.jpg"
    alt: ""
---

![demo](https://cms-assets.youmind.com/media/1777618764643_x5vg3h_HHJ49UpbcAAV0ZI.jpg)

## Original prompt

Urban Freestyle Sequence (16 Steps, Night Alley)
[PROJECT TYPE]
Cinematic urban dance video (freestyle precision with structured sequence)
[CORE REQUIREMENT — STRICT]
The video must follow the exact 16-step movement sequence below in the same order.
No steps added, removed, or rearranged.
Each movement flows naturally into the next with clean transitions.
🧍‍♀️ [CHARACTER]
Female street dancer (urban / performance aesthetic)
Lean, athletic build
Same consistent face and proportions throughout
Confident, grounded presence
Movement style: controlled, expressive, rhythm-driven
👕 [WARDROBE — URBAN STYLE]
Oversized hoodie
Cargo pants
Chunky sneakers
Subtle accessories (chain or wristband)
Fabric behavior:
Heavy cotton folds, natural motion drag, realistic cloth physics
📍 [LOCATION / ENVIRONMENT]
Empty neon-lit alley (Asian urban aesthetic, not limited to Korea)
Environment details:
Wet pavement reflections
Soft neon signage glow
Concrete textures, depth perspective
No people, no traffic
Lighting:
Night setting
Neon accents (blue, pink, purple tones)
Soft reflections on ground
🔢 [16-STEP MOVEMENT SEQUENCE — LOCKED]
Idle Bounce Start
Right Groove Step
Left Groove Step
Shoulder Roll Combo
Slow Body Wave Down
Back Glide Step
Half Turn Slide
Head Whip Accent
Side Lean Drag
Cross Step Pivot
Body Wave Up
Hip Bounce Loop
Step Tap Combo
Arm Swing Hit
Chest Hit Accent
Freeze End Pose (hold)
🎥 [CAMERA DIRECTION]
Full-body framing maintained throughout
Start: centered wide shot
Smooth tracking (slight lateral + forward motion)
Subtle handheld realism (very controlled)
Gentle angle shifts during turns (front → slight side)
⚠️ No hard cuts — continuous cinematic flow
💃 [MOVEMENT STYLE — IMPORTANT]
Urban freestyle with musical groove
Deep bounce and rhythm control
Smooth transitions between steps
Strong accents on hits (Step 8, 14, 15)
Clean isolations (shoulders, chest, hips)
Balanced footwork, grounded stance
No robotic motion, no unnatural speed
⏱️ [TIMING]
Each step: ~2–3 seconds
Total duration: ~35–50 seconds
Smooth timing continuity
🎵 [MUSIC DIRECTION — VERY IMPORTANT]
Genre: Lo-fi hip-hop / chill trap
Tempo: 85–100 BPM
Style:
Deep bass
Soft hi-hats
Ambient synth layers
Sync Notes:
Groove steps match beat bounce
Step 8 (Head Whip) hits a sharp snare/accent
Step 15 (Chest Hit) aligns with bass drop
Final freeze lands on beat fade
🎨 [VISUAL STYLE]
Photorealistic with stylized neon mood
High contrast highlights + soft shadows
Cinematic color grading (cool tones)
Moody, atmospheric look
⚙️ [OUTPUT SETTINGS]
4K resolution
24 FPS
High motion clarity
Clean rendering, no artifacts
🚫 [RESTRICTIONS]
No extra dancers
No crowd or vehicles
No outfit changes
No choreography deviation
No jump cuts or broken continuity

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
