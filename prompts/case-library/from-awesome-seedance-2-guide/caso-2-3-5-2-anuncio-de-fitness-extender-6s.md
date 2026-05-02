---
title: "Caso 2-3-5-2 · Anuncio de Fitness (Extender 6s)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/es/05-video-extension.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series, logo-3d]
inputs: {"text": true}
---

## Original prompt

6s
Extiende el video 6 segundos. Aparece música de guitarra eléctrica energética. Texto de anuncio "JUST DO IT" aparece en el medio del video luego se desvanece gradualmente. La cámara se desplaza hacia el techo. Un hombre musculoso tira de anillos. La parte superior del cuerpo viste ropa de fitness ajustada @image1 con logo "Fitness" @image2 impreso en la espalda. El hombre usa su cuerpo superior musculoso para tirar de los anillos. Luego aparece el texto de anuncio final "DO SOME SPORT" en el medio del video.

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
