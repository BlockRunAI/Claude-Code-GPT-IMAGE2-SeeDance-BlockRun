---
title: "Durum 2-3-2-2 · Köşe Takibi + Çok Sahne İzleme"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/tr/02-camera-movement.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ad-series]
inputs: {"text": true}
---

## Original prompt

@image1'den adamın görüntüsünü referans alın. @image2'deki koridordedir. @video1'den tüm kamera hareketi efektlerini ve ana karakterin yüz ifadelerini tamamen referans alın. Kamera @image2'deki köşeyi dönerken koşan ana karakteri takip eder, ardından @image3'ün uzun koridorunda kamera arka izleme perspektifinden ana karakterin ön yörüngesine geçer. Kamera daha sonra sağa 90 derece kaydırarak @image4'ten yolun çatalını çeker, aniden durur ve ardından sağa 180 derece kaydırarak ana karakterin ön yüzünün yakın çekimi. Ana karakter ağır ağır nefes alıyor. Kamera ana karakterin perspektifini takip ederek çevreyi gözlemlemek için yörünge çizer, @video1'den hızlı sol-sağ yörünge kamera hareketini referans alarak sahneyi gösterir. Ardından @image5'e geri dönün, ana karakterin yan profil koşusunu izlemeye devam edin.

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
