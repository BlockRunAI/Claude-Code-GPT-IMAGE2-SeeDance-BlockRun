---
title: "Caso 2-3-5-4 · Girasoles Callejeros (Extender Adelante 10s)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/05-video-extension.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"image": "user-supplied"}
---

## Original prompt

10s
Extiende adelante 10 segundos. En luz de tarde cálida, la cámara comienza desde la esquina de la calle con una fila de toldos mecedores, se desplaza lentamente hacia abajo a algunas pequeñas margaritas asomándose en la base de la pared. Luego aparecen las zapatillas rojas del protagonista en el fotograma. Está agachado en un puesto de flores callejero, sonriendo mientras reúne un gran ramo de girasoles en sus brazos. Los pétalos de flores rozan su camiseta blanca. Mientras se gira para subirse a su patineta, el dueño del puesto de flores sonríe y grita "¡Cuidado con los pétalos voladores!" Él saluda al dueño, luego comienza a andar. Varios pétalos dorados ya han escapado del ramo, cayendo sobre la superficie del patineta.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/05-video-extension.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
