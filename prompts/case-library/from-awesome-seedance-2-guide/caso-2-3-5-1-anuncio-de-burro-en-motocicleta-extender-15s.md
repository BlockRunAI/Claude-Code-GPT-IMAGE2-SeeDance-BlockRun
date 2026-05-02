---
title: "Caso 2-3-5-1 · Anuncio de Burro en Motocicleta (Extender 15s)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/05-video-extension.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ad-series]
inputs: {"text": true}
---

## Original prompt

Extiende el video 15 segundos. Referencia @image1 y @image2 para la imagen de un burro montando una motocicleta. Añade un segmento de anuncio de agujero cerebral.
Escena 1: Plano fijo de cámara lateral. Burro monta motocicleta irrumpiendo por la cerca. Gallinas cercanas se asustan.
Escena 2: Burro monta motocicleta girando en arena. Primero primer plano de llantas de motocicleta, luego corte a plano aéreo superior de burro montando motocicleta haciendo acrobacias giratorias, levantando polvo.
Escena 3: El fondo es plano de montaña nevada. Burro monta motocicleta volando sobre la pendiente de montaña. Texto de anuncio aparece detrás del sujeto, apareciendo a través de enmascaramiento en el medio: "Inspira Creatividad, Enriquece la Vida." Finalmente, mientras la motocicleta vuela, se levanta polvo.

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/ad-series (v1.2)`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/05-video-extension.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
