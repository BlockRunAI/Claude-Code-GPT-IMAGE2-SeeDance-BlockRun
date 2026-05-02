---
title: "Case 71: [Anime Crowd POV Comparison](https://x.com/chesnyfcb/status/2047714457774637213) (by [@chesnyfcb](https://x.com"
source_repo: awesome-gpt-image-2-prompts
source_url: https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts/blob/main/cases/comparison.md
credit: EvoLinkAI
workflow: image2image
model: openai/gpt-image-2
tags: [poster, ad-series, anime]
inputs: {"image": "user-supplied"}
---

## Original prompt

{"type":"comparison graphic","style":"anime cinematic demonstration image on a black presentation background","canvas":{"aspect_ratio":"4:3","background":"solid black"},"text_elements":[{"text":"{argument name=\"headline text\" default=\"Move the camera POV to be at ground level in the crowd.\"}","position":"top center","style":"large white sans-serif"},{"text":"Source","position":"left of upper image","style":"large white sans-serif"},{"text":"Output","position":"left of lower image","style":"large white sans-serif"}],"layout":{"sections":[{"title":"Source","position":"upper center","count":1,"labels":["overhead crowd scene"]},{"title":"Output","position":"lower center","count":1,"labels":["ground-level crowd POV scene"]}],"image_frames":2},"images":[{"role":"source image","composition":"busy top-down view of a densely packed historical street crowd, seen from above","scene":"a chaotic crowd gathered around a wagon and a horse-drawn carriage, people pressed shoulder to shoulder, many wearing caps and muted early-20th-century or old-European clothing, bundles and sacks visible, one brown horse at the right edge, wooden wagon wheel and cart structure partially visible","camera":"high overhead bird's-eye angle looking down into the crowd","lighting":"soft daylight","color_palette":"muted earthy browns, dusty blues, beige, olive, warm gray","rendering":"hand-painted anime film still, detailed crowd illustration, slightly soft shading"},{"role":"output image","composition":"the same crowded historical street reimagined from inside the mass of people at near-ground height","scene":"view from within the crowd beside a carriage wheel, bodies filling the foreground and midground, a person in dark maroon clothing bent forward at left, a crouched figure in green near the bottom center, a woman in a light blue dress at right-center turning back, tightly packed figures, horse and cart implied nearby, dramatic sense of compression and closeness","camera":"very low ground-level POV from inside the crowd, upward and forward through people, emphasizing complex occlusion and depth","lighting":"soft daylight with warm cinematic shadows","color_palette":"muted earthy browns, dusty blues, beige, olive, warm gray","rendering":"hand-painted anime film still, cinematic perspective shift, detailed character crowding, soft painterly shading"}],"overall_goal":"show a before-and-after camera angle transformation of the same anime crowd scene, with the output moving from an overhead view to a low immersive POV inside the crowd"}

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/poster`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=openai/gpt-image-2,
  action=edit.
```

## Credit & license

Sourced from [awesome-gpt-image-2-prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts/blob/main/cases/comparison.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
