---
title: "Caso 2-3-4-2 · Guión Gráfico a Video"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/04-story-completion.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"image": "user-supplied"}
---

## Original prompt

Referencia el guión gráfico de @image1 para un documental. Referencia la composición del plano, los ángulos de cámara, los movimientos de cámara, los elementos visuales y el texto de @image1. Crea una apertura de 15 segundos de estilo sanador sobre "Cuatro Estaciones de la Infancia".

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/04-story-completion.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
