---
title: "Caso 2-3-5-3 · Final de Marca de Café (Extender 15s)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/05-video-extension.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ad-series]
inputs: {"text": true}
---

## Original prompt

15s
Extiende @video1 15 segundos. 1-5 segundos: Luz y sombra pasan lentamente a través de persianas venecianas sobre la mesa de madera y taza. Las ramas de árbol se mecen suavemente con movimiento de respiración sutil. 6-10 segundos: Un grano de café se desliza suavemente desde la parte superior del fotograma. La cámara se empuja hacia el grano de café hasta que el fotograma se vuelve negro. 11-15 segundos: El texto en inglés aparece gradualmente. Primera línea "Lucky Coffee," segunda línea "Breakfast," tercera línea "AM 7:00-10:00."

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
