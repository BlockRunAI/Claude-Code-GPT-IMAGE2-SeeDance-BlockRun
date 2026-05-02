---
title: "Case 130: [Dance Movement Reference Sheet](https://x.com/Ciri_ai/status/2048074587955658848) (by [@Ciri_ai](https://x.co"
source_repo: awesome-gpt-image-2-prompts
source_url: https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts/blob/main/cases/poster.md
credit: EvoLinkAI
workflow: text2image
model: openai/gpt-image-2
tags: [dance, ui-system, ad-series, logo-3d, infographic]
inputs: {"text": true}
assets:
  - kind: image
    url: "https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-prompts/main/images/poster_case130/output.jpg"
    alt: ""
---

![demo](https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-prompts/main/images/poster_case130/output.jpg)

## Original prompt

[STYLE]
monochromatic grayscale illustration, 3D rendered character, clean instructional reference sheet, 
white background, comic-style cell grid layout, technical diagram aesthetic

[LAYOUT]
4x4 grid layout, 16 panels total, each panel separated by thin black border lines, 
numbered cells from 1 to 16, consistent panel size

[CHARACTER]
{argument name="character" default="young female dancer, athletic build, ponytail hairstyle, crop top and baggy pants, sneakers"}, same character in all panels

[PANEL STRUCTURE - per cell]
top-left: bold number badge + {argument name="title" default="Korean title text"}
center: full-body character pose illustration
bottom-left: {argument name="description" default="Korean description text (3-4 lines)"}
overlay: directional arrows indicating movement direction

[ARROWS / MOTION INDICATORS]
curved arrows, straight arrows, circular rotation indicators, 
placed around the character to show movement flow and direction

[RENDERING STYLE]
high detail 3D sculpt style, soft studio lighting, subtle shadows, 
no color, grayscale shading, clean linework, game concept art quality

[NEGATIVE]
no background scenery, no color tones, no extra characters, 
no cluttered backgrounds

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/dance`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=openai/gpt-image-2,
  action=generate.
```

## Credit & license

Sourced from [awesome-gpt-image-2-prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts/blob/main/cases/poster.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/BlockRunAI/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
