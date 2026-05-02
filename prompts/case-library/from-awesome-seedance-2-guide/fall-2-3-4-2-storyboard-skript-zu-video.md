---
title: "Fall 2-3-4-2 · Storyboard-Skript zu Video"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/de/04-story-completion.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [poster]
inputs: {"image": "user-supplied"}
---

## Original prompt

Referenzieren Sie das Storyboard-Skript von @image1 für einen Dokumentarfilm. Referenzieren Sie die Schusskomposition, Kamerawinkel, Kamerabewegungen, Visuals und Text von @image1. Erstellen Sie eine 15-sekündige Eröffnung im Heilungsstil über "Vier Jahreszeiten der Kindheit".

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/poster`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/de/04-story-completion.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
