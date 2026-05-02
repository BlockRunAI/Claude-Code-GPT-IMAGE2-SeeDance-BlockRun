---
title: "Cas 2-3-3-1 · Lunettes de Science-Fiction Voyageant à Travers Plusieurs Mondes"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/fr/03-creative-effects.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system]
inputs: {"text": true}
---

## Original prompt

Remplacez le personnage dans @video1 par @image1. @image1 est la première image. Le personnage met des lunettes virtuelles de science-fiction. Référencez le mouvement de caméra et les plans d'orbite rapprochée de @video1. Transition de la perspective à la troisième personne à la vue subjective du personnage. Naviguez à travers les lunettes virtuelles d'IA pour arriver à l'univers bleu profond de @image2. Plusieurs vaisseaux spatiaux apparaissent et naviguent vers la distance. La caméra suit les vaisseaux spatiaux naviguant vers le monde de pixels de @image3. La caméra vole bas au-dessus du monde de montagne et de forêt de pixels. Les arbres à l'intérieur poussent et apparaissent. Ensuite, la perspective s'incline vers le haut et navigue rapidement vers la planète texturée vert clair de @image4. La caméra navigue et effleure la surface de la planète.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/fr/03-creative-effects.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
