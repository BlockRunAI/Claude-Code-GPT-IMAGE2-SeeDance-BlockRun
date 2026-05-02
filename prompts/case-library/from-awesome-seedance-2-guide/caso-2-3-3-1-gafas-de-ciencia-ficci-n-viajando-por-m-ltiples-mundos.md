---
title: "Caso 2-3-3-1 · Gafas de Ciencia Ficción Viajando por Múltiples Mundos"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/03-creative-effects.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ad-series]
inputs: {"text": true}
---

## Original prompt

Reemplaza el personaje en @video1 con @image1. @image1 es el primer fotograma. El personaje se pone gafas virtuales de ciencia ficción. Referencia el movimiento de cámara y los planos de órbita cercana de @video1. Transición de perspectiva en tercera persona a la vista subjetiva del personaje. Viaja a través de las gafas virtuales de IA para llegar al universo azul profundo de @image2. Aparecen varias naves espaciales y viajan hacia la distancia. La cámara sigue las naves espaciales viajando al mundo de píxeles de @image3. La cámara vuela bajo sobre el mundo de montaña y bosque de píxeles. Los árboles dentro crecen y aparecen. Luego la perspectiva se inclina hacia arriba y viaja rápidamente al planeta texturizado verde claro de @image4. La cámara viaja y roza la superficie del planeta.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/03-creative-effects.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
