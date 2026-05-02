---
title: "Durum 2-3-1-1 · Karakter Sahne Tutarlılığı"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/tr/01-consistency.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [ad-series]
inputs: {"image": "user-supplied"}
---

## Original prompt

Adam @image1 işten sonra yorgun bir şekilde koridorda yürüyor, adımı yavaşlıyor, sonunda daire kapısında duruyor. Yüzünün yakın çekimi. Adam derin bir nefes alıyor, ruh halini ayarlıyor, olumsuz duygulardan kurtulup rahatlamış hale geliyor. Sonra anahtarlarını arayan, kilide sokan, daireye giren yakın çekimi. Küçük kızı ve evcil köpeği mutlu bir şekilde koşarak gelip onu karşılıyor ve sarılıyor. İç mekan çok sıcak ve rahat. Başından sonuna kadar doğal diyalog.

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/tr/01-consistency.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
