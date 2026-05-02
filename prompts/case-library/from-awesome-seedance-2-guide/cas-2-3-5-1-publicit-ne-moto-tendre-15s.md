---
title: "Cas 2-3-5-1 · Publicité Âne à Moto (Étendre 15s)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/fr/05-video-extension.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"text": true}
---

## Original prompt

Étendez la vidéo de 15 secondes. Référencez @image1 et @image2 pour l'image d'un âne montant une moto. Ajoutez un segment de publicité de trou cérébral.
Scène 1: Plan de caméra fixe latéral. L'âne monte la moto en éclatant la clôture. Les poules à proximité sont effrayées.
Scène 2: L'âne monte la moto en tournant dans le sable. D'abord gros plan du pneu de moto, puis coupé à vue aérienne de l'âne montant la moto faisant des cascades de rotation, levant la poussière.
Scène 3: L'arrière-plan est un plan de montagne enneigée. L'âne monte la moto en volant sur la pente de la montagne. Le texte publicitaire apparaît derrière le sujet, apparaissant par masquage au milieu: "Inspirer la Créativité, Enrichir la Vie." Enfin, alors que la moto s'envole, la poussière est levée.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/fr/05-video-extension.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
