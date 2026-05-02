---
title: "Durum 2-3-2-6 · Dövüş + Yörünge Kamera Hareketi (Çift Video Referansı)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/tr/02-camera-movement.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: []
inputs: {"text": true}
---

## Original prompt

video1'den karakter hareketlerini referans alın. video2'den yörünge kamera lens dilini referans alın. Karakter 1 ve Karakter 2 arasında bir dövüş sahnesi oluşturun. Dövüş yıldızlı bir gece altında gerçekleşir. Dövüş sırasında beyaz toz yükselir. Dövüş sahnesi çok ayrıntılı ve gergin bir atmosferle doludur.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/tr/02-camera-movement.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
