---
title: "Durum 2-3-5-1 · Eşek Motosiklet Reklamı (15s Uzat)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/tr/05-video-extension.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ad-series]
inputs: {"text": true}
---

## Original prompt

Videoyu 15 saniye uzatın. Eşeğin motosiklet bindiği görüntü için @image1 ve @image2'yi referans alın. Beyin deliği reklam segmenti ekleyin.
Sahne 1: Yan sabit kamera çekimi. Eşek motosiklete binerek çitin dışına fırlar. Yakındaki tavuklar korkuyor.
Sahne 2: Eşek motosiklete binerek kumda dönüyor. Önce motosiklet lastiğinin yakın çekimi, sonra eşeğin motosiklete binerek dönerken havadan çekimi, toz kaldırıyor.
Sahne 3: Arka plan karlı dağ çekimi. Eşek motosiklete binerek dağ yamaçından uçuyor. Reklam metni konunun arkasında görünüyor, ortada maskeleme yoluyla görünüyor: "Yaratıcılığı İlham Ver, Hayatı Zenginleştir." Son olarak, motosiklet uçarken toz kaldırılıyor.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/tr/05-video-extension.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
