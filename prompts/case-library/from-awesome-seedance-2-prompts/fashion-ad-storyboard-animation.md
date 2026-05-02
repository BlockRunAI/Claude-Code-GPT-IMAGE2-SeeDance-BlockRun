---
title: "Fashion Ad Storyboard Animation"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [poster, ui-system, lookbook, ad-series, unbox, logo-3d, minimalist]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://cms-assets.youmind.com/media/1777618752490_x37ny3_HHJ4uasbQAEpFOv.jpg"
    alt: ""
---

![demo](https://cms-assets.youmind.com/media/1777618752490_x37ny3_HHJ4uasbQAEpFOv.jpg)

## Original prompt

Video prompt:- Create a 14-second ultra-cinematic fashion advertisement video using a 20-frame storyboard collage as the source. The video should animate across each frame in sequence (left to right, top to bottom), transforming static images into a smooth, continuous motion experience. Style & Motion: •Slow cinematic Ken Burns movement (zoom + pan) on each frame •Subtle parallax depth effect (foreground vs background separation) •Natural motion blur transitions between frames •Smooth crossfade or swipe transitions (0.2–0.4s) •Maintain visual continuity as if it’s one single video shoot ⸻ ⏱️ Timing & Flow (14 sec total) •Frames 1–5 → 0.8s each (intro, slower pacing) •Frames 6–15 → 0.5–0.6s each (faster mid segment energy) •Frames 16–20 → 0.8s each (slow down for impact) Final shot (Frame 20): •Hold longer (~1.5 sec) •Add slight push-in zoom •Emphasize “Lyntilla” logo Ensure smooth temporal consistency, preserve the same facial identity, maintain outfit and lighting continuity, and simulate realistic motion between frames as if captured from a single continuous fashion film Image prompt:- A high-resolution cinematic storyboard collage composed of 20 sequential frames (4x5 grid), designed as continuous screenshots from a premium fashion advertisement video. The same young male model appears consistently in all frames, wearing a clean, modern t-shirt with the brand name “Lyntilla” clearly visible on the chest in minimal, stylish typography. The frames follow a natural motion progression like a real video sequence: Row 1 (Intro – Establishing): 1.Wide shot – model walking into frame on an urban street 2.Mid-wide – approaching camera 3.Medium shot – slow confident walk 4.Slight turn – natural motion blur 5.Close-up – face + upper torso, calm expression Row 2 (Engagement – Movement): 6. Adjusting collar (hands in motion) 7. Looking sideways, candid moment 8. Wind blowing t-shirt slightly 9. Hands in pocket, relaxed stance 10. Walking past camera (motion blur edge frame) Row 3 (Detail – Product Focus): 11. Close-up of “Lyntilla” logo on chest 12. Fabric texture macro shot 13. Slight stretch of fabric showing quality 14. Over-the-shoulder glance 15. Side profile with soft light Row 4 (Lifestyle – Emotion): 16. Sitting casually on urban steps 17. Laughing candid moment 18. Leaning against wall, streetwear vibe 19. Low-angle power pose (hero energy) 20. Final hero shot – direct eye contact, strong confident stance ⸻ 🎥 Visual Style & Consistency •Ultra-cinematic fashion ad style •Golden hour + soft diffused lighting mix •Shallow depth of field, creamy bokeh •Subtle motion blur in transitional frames •Warm, filmic color grading (slightly desaturated luxury tones) •Clean urban + minimal studio hybrid backgrounds •Consistent outfit, lighting continuity, and character identity Generate image using uploaded image as reference for facial features

## Run via Claude Code

After installing `Claude Code-GPT-IMAGE2-SeeDance-BlockRun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/poster`.

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
