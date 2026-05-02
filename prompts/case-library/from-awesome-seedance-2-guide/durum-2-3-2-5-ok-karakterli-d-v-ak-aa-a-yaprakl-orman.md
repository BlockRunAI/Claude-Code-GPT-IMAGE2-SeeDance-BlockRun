---
title: "Durum 2-3-2-5 · Çok Karakterli Dövüş (Akçaağaç Yapraklı Orman)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/tr/02-camera-movement.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ad-series]
inputs: {"text": true}
---

## Original prompt

@image1 ve @image2'den 2 karakter. Sahne @image3'ün akçaağaç yapraklı ormanındadır. @video1'den dövüş hareketleri ve kamera hareketini referans alın. 2 karakter akçaağaç yaprakları uçuşan ormanda şiddetli bir şekilde dövüşür. Kamera birden fazla açıdan dövüş sahnesini yakalar ve @image4 ile @image5'in çevre ayrıntılarını referans alır. Dövüş sahnesi dinamik ve görsel etki ile doludur.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/tr/02-camera-movement.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
