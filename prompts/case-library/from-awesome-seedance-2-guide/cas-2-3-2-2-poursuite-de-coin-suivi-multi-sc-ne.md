---
title: "Cas 2-3-2-2 · Poursuite de Coin + Suivi Multi-Scène"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/fr/02-camera-movement.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [poster, ui-system]
inputs: {"text": true}
---

## Original prompt

Référencez l'image de l'homme de @image1. Il est dans le couloir de @image2. Référencez complètement tous les effets de mouvement de caméra et les expressions faciales du protagoniste de @video1. La caméra suit le protagoniste courant autour du coin dans @image2, puis dans le long couloir de @image3, la caméra passe d'une perspective de suivi arrière à une orbite autour de l'avant du protagoniste. La caméra fait ensuite un panoramique à droite de 90 degrés pour filmer la fourche de la route de @image4, s'arrête brusquement puis fait un panoramique à droite de 180 degrés, gros plan du visage avant du protagoniste. Le protagoniste respire lourdement. La caméra suit la perspective du protagoniste en orbite pour observer les environs, référençant le mouvement de caméra d'orbite rapide gauche-droite de @video1 pour montrer la scène. Puis revenez à @image5, continuez à suivre le profil latéral du protagoniste en courant.

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/poster`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/fr/02-camera-movement.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
