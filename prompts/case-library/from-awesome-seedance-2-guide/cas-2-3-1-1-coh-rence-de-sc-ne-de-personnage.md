---
title: "Cas 2-3-1-1 · Cohérence de Scène de Personnage"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/fr/01-consistency.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [ui-system]
inputs: {"image": "user-supplied"}
---

## Original prompt

L'homme @image1 marche fatigué dans le couloir après le travail, son pas ralentit, s'arrête finalement à la porte de l'appartement. Gros plan de son visage. L'homme respire profondément, ajuste son humeur, abandonne les émotions négatives et se détend. Puis gros plan de lui cherchant ses clés, les insérant dans la serrure, entrant dans l'appartement. Sa petite fille et son chien de compagnie courent joyeusement pour le saluer et l'étreindre. L'intérieur est très chaud et confortable. Dialogue naturel tout au long.

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
