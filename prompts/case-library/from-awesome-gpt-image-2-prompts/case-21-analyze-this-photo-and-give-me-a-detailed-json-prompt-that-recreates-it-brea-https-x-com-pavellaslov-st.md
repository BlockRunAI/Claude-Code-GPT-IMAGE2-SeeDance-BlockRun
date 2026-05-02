---
title: "Case 21: [analyze this photo and give me a detailed JSON prompt that recreates it. brea...](https://x.com/pavellaslov/st"
source_repo: awesome-gpt-image-2-prompts
source_url: https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts/blob/main/cases/portrait.md
credit: EvoLinkAI
workflow: image2image
model: openai/gpt-image-2
tags: [ad-series, unbox]
inputs: {"image": "user-supplied"}
assets:
  - kind: image
    url: "https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-prompts/main/images/portrait_case77/output.jpg"
    alt: ""
---

![demo](https://raw.githubusercontent.com/EvoLinkAI/awesome-gpt-image-2-prompts/main/images/portrait_case77/output.jpg)

## Original prompt

analyze this photo and give me a detailed JSON prompt that recreates it. break down the color grading and every exact color in the photo

(use Opus, not Sonnet. Opus has stronger visual analysis and writes more detailed JSON)

paste that JSON into ChatGPT
upload your product image and prompt:
using this JSON as reference, generate a person holding my product
save that generated photo as your character reference

attach it to every future generation for facial consistency

you now have a consistent UGC model that works across any product

the JSON controls the lighting and color grading. GPT image-2 handles the character. you control the product placement.

the #1 tell on AI photos is flat colors and a grainy look. this method removes both.
5 minutes to set up. unlimited variations after.

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/ad-series (v1.2)`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=openai/gpt-image-2,
  action=edit.
```

## Credit & license

Sourced from [awesome-gpt-image-2-prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts/blob/main/cases/portrait.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/BlockRunAI/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
