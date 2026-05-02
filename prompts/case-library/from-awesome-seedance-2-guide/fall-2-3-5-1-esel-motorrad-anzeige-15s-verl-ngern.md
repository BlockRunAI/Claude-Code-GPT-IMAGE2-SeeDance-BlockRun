---
title: "Fall 2-3-5-1 · Esel-Motorrad-Anzeige (15s verlängern)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/de/05-video-extension.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ad-series, card-deck]
inputs: {"text": true}
---

## Original prompt

Verlängern Sie das Video um 15 Sekunden. Referenzieren Sie @image1 und @image2 für das Bild eines Esels auf einem Motorrad. Fügen Sie ein Gehirn-Loch-Anzeigensegment hinzu.
Szene 1: Seitliche feste Kameraaufnahme. Der Esel fährt auf dem Motorrad durch den Zaun. Nahegelegene Hühner sind erschrocken.
Szene 2: Der Esel fährt auf dem Motorrad im Sand herum. Zuerst Nahaufnahme des Motorradreifen, dann Schnitt zu Luftaufnahme des Esels auf dem Motorrad, der Drehstunts macht und Staub aufwirbelt.
Szene 3: Der Hintergrund ist eine schneebedeckte Bergaufnahme. Der Esel fährt auf dem Motorrad über die Berghang. Der Anzeigentext erscheint hinter dem Motiv, erscheint durch Maskierung in der Mitte: "Kreativität inspirieren, Leben bereichern." Schließlich wird beim Wegfliegen des Motorrads Staub aufgewirbelt.

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/ad-series (v1.2)`.

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
