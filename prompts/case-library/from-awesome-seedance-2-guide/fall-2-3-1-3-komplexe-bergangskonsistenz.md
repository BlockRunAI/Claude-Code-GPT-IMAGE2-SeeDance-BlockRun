---
title: "Fall 2-3-1-3 · Komplexe Übergangskonsistenz"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/de/01-consistency.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: []
inputs: {"text": true}
---

## Original prompt

Beziehen Sie sich auf alle Übergänge und Kamerabewegungen von @video1, eine durchgehende Aufnahme. Die Szene beginnt mit einem Schachbrett, die Kamera schwenkt nach links, um gelben Sand auf dem Boden zu enthüllen, die Kamera bewegt sich nach oben zu einem Strand mit Fußabdrücken. Ein Mädchen in einfacher weißer Kleidung geht allmählich am Strand weg. Die Kamera schneidet zu einer Luftaufnahme von oben auf das Meer, das wäscht (keine Personen sichtbar). Nahtloser Farbverlauf-Übergang, während sich die waschenden Wellen in flatternde Vorhänge verwandeln. Die Kamera zieht sich zurück, um eine Nahaufnahme des Gesichts des Mädchens zu enthüllen. Durchgehend eine durchgehende Aufnahme.

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `(case-library only — no v1 command match)`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/de/01-consistency.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
