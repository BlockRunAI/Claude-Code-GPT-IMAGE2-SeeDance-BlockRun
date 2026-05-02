---
title: "Caso 2-3-2-2 · Persecución de Esquina + Seguimiento Multi-Escena"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/02-camera-movement.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"text": true}
---

## Original prompt

Referencia la imagen del hombre de @image1. Está en el pasillo de @image2. Referencia completamente todos los efectos de movimiento de cámara y las expresiones faciales del protagonista de @video1. La cámara sigue al protagonista corriendo alrededor de la esquina en @image2, luego en el pasillo largo de @image3, la cámara transiciona de una perspectiva de seguimiento trasero a una órbita alrededor del frente del protagonista. La cámara luego hace un paneo a la derecha de 90 grados para disparar la bifurcación del camino de @image4, se detiene abruptamente y luego hace un paneo a la derecha de 180 grados, primer plano del rostro frontal del protagonista. El protagonista está jadeando pesadamente. La cámara sigue la perspectiva del protagonista orbitando para observar los alrededores, referenciando el rápido movimiento de cámara de órbita izquierda-derecha de @video1 para mostrar la escena. Luego retrocede a @image5, continúa siguiendo el perfil lateral del protagonista corriendo.

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
