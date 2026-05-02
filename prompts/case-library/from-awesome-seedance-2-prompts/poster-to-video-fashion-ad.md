---
title: "Poster-to-Video Fashion Ad"
source_repo: awesome-seedance-2-prompts
source_url: https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md
credit: YouMind-OpenLab
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [poster, lookbook, ad-series]
inputs: {"image": "user-supplied"}
assets:
  - kind: image
    url: "https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/87a299b04382f022a6cf1fea497c5089/thumbnails/thumbnail.jpg"
    alt: ""
---

![demo](https://customer-qs6wnyfuv0gcybzj.cloudflarestream.com/87a299b04382f022a6cf1fea497c5089/thumbnails/thumbnail.jpg)

## Original prompt

Make a slight animation of this image, like it was a track shot of a stylish fashion ad. Don't touch the text, just a slight camera animation and slight movement of models. And this is it. Make it less than 5 seconds.

## Run via Claude Code

After installing `Claude Code-GPT-IMAGE2-SeeDance-BlockRun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/poster`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/main/README.md) by YouMind-OpenLab.
This case file is part of the curated `prompts/case-library/` in the
[Claude Code-GPT-IMAGE2-SeeDance-BlockRun](https://github.com/BlockRunAI/Claude-Code-GPT-IMAGE2-SeeDance-BlockRun)
bundle. Reproduced with attribution; original license applies.
