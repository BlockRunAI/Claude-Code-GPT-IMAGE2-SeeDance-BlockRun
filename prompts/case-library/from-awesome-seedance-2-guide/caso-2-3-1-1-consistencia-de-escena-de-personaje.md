---
title: "Caso 2-3-1-1 · Consistencia de Escena de Personaje"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/01-consistency.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [ad-series, logo-3d]
inputs: {"image": "user-supplied"}
---

## Original prompt

El hombre @image1 camina cansadamente por el pasillo después del trabajo, su paso se ralentiza, finalmente se detiene en la puerta del apartamento. Primer plano de su rostro. El hombre respira profundamente, ajusta su estado de ánimo, deja ir las emociones negativas y se relaja. Luego primer plano de él buscando sus llaves, insertándolas en la cerradura, entrando al apartamento. Su pequeña hija y su perro mascota corren felices para saludarlo y abrazarlo. El interior es muy cálido y acogedor. Diálogo natural en todo momento.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/01-consistency.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
