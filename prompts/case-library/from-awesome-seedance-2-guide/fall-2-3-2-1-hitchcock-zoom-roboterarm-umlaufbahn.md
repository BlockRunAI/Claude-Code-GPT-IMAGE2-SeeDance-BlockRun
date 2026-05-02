---
title: "Fall 2-3-2-1 · Hitchcock-Zoom + Roboterarm-Umlaufbahn"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/de/02-camera-movement.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: []
inputs: {"text": true}
---

## Original prompt

Referenzieren Sie das Bild des Mannes von @image1. Er ist im Aufzug von @image2. Beziehen Sie sich vollständig auf alle Kamerabewegungseffekte und die Gesichtsausdrücke des Protagonisten von @video1. Wenn der Protagonist verängstigt ist, wenden Sie den Hitchcock-Zoom-Effekt an. Dann mehrere Umlaufaufnahmen, die die Aufzugsinnenperspektive zeigen. Die Aufzugtüren öffnen sich, folgen Sie der Kamera, die aus dem Aufzug geht. Die Szene außerhalb des Aufzugs bezieht sich auf @image3. Der Mann schaut sich um. Referenzieren Sie @video1 mit Roboterarm-Mehrwinkel-Verfolgung der Blicklinie des Charakters.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/de/02-camera-movement.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
