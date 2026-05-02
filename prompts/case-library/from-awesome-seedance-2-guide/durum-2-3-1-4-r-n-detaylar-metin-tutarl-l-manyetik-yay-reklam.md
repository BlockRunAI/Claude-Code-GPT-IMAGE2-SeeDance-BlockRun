---
title: "Durum 2-3-1-4 · Ürün Detayları + Metin Tutarlılığı (Manyetik Yay Reklamı)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/tr/01-consistency.md
credit: EvoLinkAI
workflow: image2video
model: bytedance/seedance-2.0-fast
tags: [ad-series]
inputs: {"image": "user-supplied"}
---

## Original prompt

0-2 saniye: Kırmızı, pembe, mor, leopar desenli yayların hızlı dört kare flaş kesintileri, "chéri" marka yazısını gösteriyor. Seslendirme: "chéri manyetik yayı ile sonsuz güzellik yaratın!"
3-6 saniye: Gümüş manyetik kilit "tıklama" bir araya gelip, sonra nazikçe ayrılıyor, ipeksi doku ve kolaylığı gösteriyor. Seslendirme: "Sadece 1 saniyede kilitleyin ve en iyi stilinizi tamamlayın!"
7-12 saniye: Giyim senaryolarının hızlı kesintileri: ceket yakaında bordo yay; at kuyruğuna bağlı pembe yay; çanta kayışına bağlı mor yay; takım elbise yakaasında asılı leopar desenli yay. Seslendirme: "Ceketten, çantadan saç aksesuarlarına kadar, çok yönlü ve kişilikli bir stil tamamlayın!"
13-15 saniye: Dört yay yan yana gösteriliyor, marka adı "chéri, size anlık güzellik sunuyor!"

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
