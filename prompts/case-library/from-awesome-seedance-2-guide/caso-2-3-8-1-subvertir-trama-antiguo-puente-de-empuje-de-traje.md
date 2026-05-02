---
title: "Caso 2-3-8-1 · Subvertir Trama (Antiguo Puente de Empuje de Traje)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/08-video-editing.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ad-series]
inputs: {"text": true}
---

## Original prompt

Subvierte la trama en @video1. Los ojos del hombre cambian instantáneamente de tierno a frío e implacable. En un momento desprevenido, de repente empuja a la protagonista del puente al agua. La acción es rápida y decisiva, con resolución premeditada, sin un atisbo de vacilación, subvirtiendo completamente la configuración de carácter tierno original. Mientras la protagonista cae al agua, no hay grito, solo incredulidad en sus ojos. Ella mira hacia arriba y grita al hombre: "¡Me has estado mintiendo desde el principio!" El hombre está de pie en el puente, una sonrisa fría en su cara, y dice suavemente al agua: "Esto es lo que tu familia me debe."

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/08-video-editing.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
