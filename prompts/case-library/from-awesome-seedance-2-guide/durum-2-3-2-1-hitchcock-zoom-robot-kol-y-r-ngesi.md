---
title: "Durum 2-3-2-1 · Hitchcock Zoom + Robot Kol Yörüngesi"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/tr/02-camera-movement.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ad-series]
inputs: {"text": true}
---

## Original prompt

@image1'den adamın görüntüsünü referans alın. @image2'deki asansördedir. @video1'den tüm kamera hareketi efektlerini ve ana karakterin yüz ifadelerini tamamen referans alın. Ana karakter korktuğunda Hitchcock zoom efektini uygulayın. Ardından asansör iç perspektifini gösteren birkaç yörünge çekimi. Asansör kapıları açılır, kamerayı asansörden çıkarken takip edin. Asansör dışındaki sahne @image3'ü referans alır. Adam etrafına bakınır. @video1'ü referans alarak robot kol çok açılı karakterin bakış açısını takip edin.

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
