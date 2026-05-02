---
title: "Case 2-3-7-1 · Street to Rooftop Tracking Run"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/07-continuity.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: []
inputs: {"image": "user-supplied"}
---

## Original prompt

@image1 @image2 @image3 @image4 @image5, one continuous shot tracking camera. Follow the runner from the street up stairs, through corridors, onto the rooftop, finally overlooking the city.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/07-continuity.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
