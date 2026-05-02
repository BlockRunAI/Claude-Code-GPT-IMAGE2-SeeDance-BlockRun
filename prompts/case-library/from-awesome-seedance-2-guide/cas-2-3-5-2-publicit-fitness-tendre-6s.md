---
title: "Cas 2-3-5-2 · Publicité Fitness (Étendre 6s)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/fr/05-video-extension.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, logo-3d]
inputs: {"image": "user-supplied"}
---

## Original prompt

6s
Étendez la vidéo de 6 secondes. La musique de guitare électrique énergique apparaît. Le texte publicitaire "JUST DO IT" apparaît au milieu de la vidéo puis s'estompe progressivement. La caméra se déplace vers le plafond. Un homme musclé tire sur les anneaux. Le haut du corps porte des vêtements de fitness serrés @image1 avec le logo "Fitness" @image2 imprimé sur le dos. L'homme utilise son haut du corps musclé pour tirer sur les anneaux. Ensuite, le texte de fin publicitaire "DO SOME SPORT" apparaît au milieu de la vidéo.

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
