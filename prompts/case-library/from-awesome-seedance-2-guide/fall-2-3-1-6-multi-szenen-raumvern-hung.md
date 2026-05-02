---
title: "Fall 2-3-1-6 · Multi-Szenen-Raumvernähung"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/de/01-consistency.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: []
inputs: {"text": true}
---

## Original prompt

Verwenden Sie @image1 als erstes Bild der Aufnahme, Ich-Perspektive. Beziehen Sie sich auf die Kamerabewegungseffekte von @video1. Obere Szene bezieht sich auf @image2, linke Szene bezieht sich auf @image3, rechte Szene bezieht sich auf @image4.

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
