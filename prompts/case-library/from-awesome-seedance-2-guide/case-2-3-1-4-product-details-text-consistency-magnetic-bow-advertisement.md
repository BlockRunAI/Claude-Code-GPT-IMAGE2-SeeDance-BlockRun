---
title: "Case 2-3-1-4 · Product Details + Text Consistency (Magnetic Bow Advertisement)"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/01-consistency.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series, unbox]
inputs: {"text": true}
---

## Original prompt

0-2 seconds: Quick four-frame flash cuts of red, pink, purple, and leopard print bows in sequence, each freezing with close-ups of satin luster and "chéri" brand lettering. Voiceover: "Chéri 자석 리본으로 무궁무진한 아름다움을 연출해 보세요!"
3-6 seconds: Close-up of silver magnetic clasp "clicking" together, then gently pulling apart, showcasing silky texture and convenience. Voiceover: "단 1초 만에 잠그고, 최고의 스타일을 완성하세요!"
7-12 seconds: Quick cuts of wearing scenarios: burgundy bow on coat collar; pink bow tied to ponytail; purple bow tied to bag strap; leopard print bow hanging on suit lapel. Voiceover: "코트, 가방, 헤어 액세서리까지, 다재다능하고 개성 넘치는 스타일을 완성하세요!"
13-15 seconds: Four bows displayed side by side, brand name "chéri, 당신에게 즉각적인 아름다움을 선사합니다!"

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

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/use-cases/en/01-consistency.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
