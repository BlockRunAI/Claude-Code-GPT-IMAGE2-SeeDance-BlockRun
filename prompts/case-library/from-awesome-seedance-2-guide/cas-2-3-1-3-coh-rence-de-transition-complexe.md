---
title: "Cas 2-3-1-3 · Cohérence de Transition Complexe"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/fr/01-consistency.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"text": true}
---

## Original prompt

Référencez toutes les transitions et mouvements de caméra de @video1, un plan continu. La scène commence par un échiquier, la caméra se déplace vers la gauche pour révéler du sable jaune sur le sol, la caméra se déplace vers le haut vers une plage avec des empreintes. Une fille en vêtements blancs simples s'éloigne progressivement sur la plage. La caméra coupe à une vue aérienne de haut en bas de la mer qui lave (aucune personne visible). Transition de dégradé transparente alors que les vagues de lavage se transforment en rideaux ondulants. La caméra se retire pour révéler un gros plan du visage de la fille. Un plan continu tout au long.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/fr/01-consistency.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
