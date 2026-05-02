---
title: "Caso 2-3-1-4 · Detalles de Producto + Consistencia de Texto (Anuncio de Lazo Magnético)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/01-consistency.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [ad-series, unbox]
inputs: {"image": "user-supplied"}
---

## Original prompt

0-2 segundos: Cortes rápidos de cuatro fotogramas de lazos rojo, rosa, púrpura y estampado de leopardo, mostrando letras de marca "chéri". Voz en off: "¡Crea belleza infinita con el lazo magnético chéri!"
3-6 segundos: Primer plano del cierre magnético de plata "haciendo clic" juntos, luego separándose suavemente, mostrando textura sedosa y conveniencia. Voz en off: "¡Cierra en solo 1 segundo y completa tu mejor estilo!"
7-12 segundos: Cortes rápidos de escenarios de uso: lazo burdeos en cuello de abrigo; lazo rosa atado a cola de caballo; lazo púrpura atado a correa de bolsa; lazo estampado de leopardo colgando en solapa de traje. Voz en off: "¡Desde abrigos, bolsas hasta accesorios para el cabello, completa un estilo versátil y lleno de personalidad!"
13-15 segundos: Cuatro lazos mostrados lado a lado, nombre de marca "chéri, ¡te brinda belleza instantánea!"

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
