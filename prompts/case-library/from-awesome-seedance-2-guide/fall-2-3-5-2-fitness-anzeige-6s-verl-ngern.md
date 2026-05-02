---
title: "Fall 2-3-5-2 · Fitness-Anzeige (6s verlängern)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/de/05-video-extension.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [card-deck, logo-3d]
inputs: {"text": true}
---

## Original prompt

6s
Verlängern Sie das Video um 6 Sekunden. Energische E-Gitarrenmusik erscheint. Der Anzeigentext "JUST DO IT" erscheint in der Mitte des Videos und verblasst dann allmählich. Die Kamera schwenkt zur Decke. Ein muskulöser Mann zieht an Ringen. Der Oberkörper trägt enge Fitnessbekleidung @image1 mit dem auf dem Rücken gedruckten Logo "Fitness" @image2. Der Mann nutzt seinen muskulösen Oberkörper, um an den Ringen zu ziehen. Dann erscheint der Anzeigen-Endtext "DO SOME SPORT" in der Mitte des Videos.

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/card-deck (v1.2)`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/de/05-video-extension.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
