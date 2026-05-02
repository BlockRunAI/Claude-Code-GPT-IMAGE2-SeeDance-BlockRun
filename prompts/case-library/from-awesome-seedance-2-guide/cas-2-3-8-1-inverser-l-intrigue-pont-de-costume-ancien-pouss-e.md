---
title: "Cas 2-3-8-1 · Inverser l'Intrigue (Pont de Costume Ancien Poussée)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/fr/08-video-editing.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system]
inputs: {"text": true}
---

## Original prompt

Inversez l'intrigue dans @video1. Les yeux de l'homme changent instantanément de tendre à froid et impitoyable. Dans un moment d'inattention, il pousse soudainement l'héroïne du pont dans l'eau. L'action est rapide et décisive, avec une résolution préméditée, sans une trace d'hésitation, inversant complètement le paramètre de caractère tendre original. Alors que l'héroïne tombe dans l'eau, il n'y a pas de cri, seulement de l'incrédulité dans ses yeux. Elle regarde vers le haut et crie à l'homme: "Tu m'as menti depuis le début!" L'homme se tient sur le pont, un sourire froid sur son visage, et dit doucement à l'eau: "C'est ce que ta famille me doit."

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/fr/08-video-editing.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
