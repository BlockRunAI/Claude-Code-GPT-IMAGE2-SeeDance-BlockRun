---
title: "海报与排版"
source_repo: awesome-gpt-image-2
source_url: https://github.com/freestylefly/awesome-gpt-image-2/blob/main/docs/templates.md
credit: freestylefly
workflow: image2image
model: openai/gpt-image-2
tags: [poster, minimalist]
inputs: {"image": "user-supplied"}
---

## Original prompt

设计一张[活动/产品/电影]海报，主题为[主题词]。
主视觉：[主体元素]，标题文案：[标题]，副标题：[副标题]。
版式：[居中/左对齐/对角构图]，风格：[复古/未来/极简]。
色彩：[主色 + 辅色]，氛围：[情绪关键词]。
输出：可用于社媒传播的高分辨率海报。

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/poster`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=openai/gpt-image-2,
  action=edit.
```

## Credit & license

Sourced from [awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2/blob/main/docs/templates.md) by freestylefly.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
