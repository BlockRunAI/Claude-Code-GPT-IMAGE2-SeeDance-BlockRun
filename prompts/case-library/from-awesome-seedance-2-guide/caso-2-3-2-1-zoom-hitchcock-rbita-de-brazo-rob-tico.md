---
title: "Caso 2-3-2-1 · Zoom Hitchcock + Órbita de Brazo Robótico"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/02-camera-movement.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"text": true}
---

## Original prompt

Referencia la imagen del hombre de @image1. Está en el ascensor de @image2. Referencia completamente todos los efectos de movimiento de cámara y las expresiones faciales del protagonista de @video1. Cuando el protagonista está asustado, aplica el efecto de zoom Hitchcock. Luego varios planos de órbita mostrando la perspectiva interior del ascensor. Las puertas del ascensor se abren, sigue la cámara saliendo del ascensor. La escena fuera del ascensor referencia @image3. El hombre mira alrededor. Referencia @video1 usando brazo robótico multi-ángulo siguiendo la línea de visión del personaje.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/02-camera-movement.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
