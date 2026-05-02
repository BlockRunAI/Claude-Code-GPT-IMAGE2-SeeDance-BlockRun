---
title: "Cas 2-3-2-1 · Zoom Hitchcock + Orbite de Bras Robotique"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/fr/02-camera-movement.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system]
inputs: {"text": true}
---

## Original prompt

Référencez l'image de l'homme de @image1. Il est dans l'ascenseur de @image2. Référencez complètement tous les effets de mouvement de caméra et les expressions faciales du protagoniste de @video1. Lorsque le protagoniste a peur, appliquez l'effet de zoom Hitchcock. Ensuite, plusieurs prises d'orbite montrant la perspective intérieure de l'ascenseur. Les portes de l'ascenseur s'ouvrent, suivez la caméra sortant de l'ascenseur. La scène en dehors de l'ascenseur référence @image3. L'homme regarde autour de lui. Référencez @video1 en utilisant le bras robotique multi-angle suivant la ligne de mire du personnage.

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/ui-system (v1.1)`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/fr/02-camera-movement.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
