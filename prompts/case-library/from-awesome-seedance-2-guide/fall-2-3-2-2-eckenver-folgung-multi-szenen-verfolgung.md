---
title: "Fall 2-3-2-2 · Eckenver folgung + Multi-Szenen-Verfolgung"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/de/02-camera-movement.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ad-series]
inputs: {"text": true}
---

## Original prompt

Referenzieren Sie das Bild des Mannes von @image1. Er ist im Korridor von @image2. Beziehen Sie sich vollständig auf alle Kamerabewegungseffekte und die Gesichtsausdrücke des Protagonisten von @video1. Die Kamera folgt dem Protagonisten, der um die Ecke in @image2 läuft, dann im langen Korridor von @image3 wechselt die Kamera von einer hinteren Verfolgungsperspektive zu einer Umlaufbahn um die Vorderseite des Protagonisten. Die Kamera schwenkt dann 90 Grad nach rechts, um die Gabelung der Straße von @image4 zu schießen, stoppt abrupt und schwenkt dann 180 Grad nach rechts, Nahaufnahme des Gesichts des Protagonisten von vorne. Der Protagonist atmet schwer. Die Kamera folgt der Perspektive des Protagonisten und umkreist, um die Umgebung zu beobachten, bezieht sich auf die schnelle Links-Rechts-Umlaufkamerabewegung von @video1, um die Szene zu zeigen. Dann zurück zu @image5, weiterhin die Seitenprofilausführung des Protagonisten verfolgen.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/de/02-camera-movement.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
