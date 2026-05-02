---
title: "Caso 2-3-1-3 · Consistencia de Transición Compleja"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/01-consistency.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"text": true}
---

## Original prompt

Referencia todas las transiciones y movimientos de cámara de @video1, una toma continua. La escena comienza con un tablero de ajedrez, la cámara se desplaza hacia la izquierda para revelar arena amarilla en el piso, la cámara se mueve hacia arriba a una playa con huellas. Una chica con ropa blanca simple camina gradualmente en la playa. La cámara corta a una vista aérea de arriba hacia abajo del mar lavando (sin personas visibles). Transición de gradiente sin costuras mientras las olas de lavado se transforman en cortinas ondeantes. La cámara retrocede para revelar un primer plano del rostro de la chica. Una toma continua en todo momento.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/01-consistency.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
