---
title: "Case 2-3-8-2 · Subvert Plot (Bar Snack Ad)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/08-video-editing.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"text": true}
---

## Original prompt

Subvert the entire plot in @video1.
0–3 seconds: A suited man sits in a bar, calm expression, gently swirling a drink glass. Ambient sound is low. The man says softly: "This deal is very big."
3–6 seconds: A woman behind him looks tense and asks: "How big?" The suited man looks up, lowers his voice: "Very big."
6–9 seconds: Suddenly the suited man pulls out from under the table — a huge package of snacks, "thud" heavily placed on the table.
9–12 seconds: The woman's muscles relax from tension, her entire expression loosens.
13–15 seconds: The suited man pulls out a snack package for the woman. Subtitle appears: "No matter how busy, remember to eat some snacks~"

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/08-video-editing.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
