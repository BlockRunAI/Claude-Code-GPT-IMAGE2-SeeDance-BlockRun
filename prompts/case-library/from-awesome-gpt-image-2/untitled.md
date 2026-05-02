---
title: "🧩 工业级提示词模板与防坑指南"
source_repo: awesome-gpt-image-2
source_url: https://github.com/freestylefly/awesome-gpt-image-2/blob/main/docs/templates.md
credit: freestylefly
workflow: image2image
model: openai/gpt-image-2
tags: [ui-system, minimalist]
inputs: {"image": "user-supplied"}
---

## Original prompt

为[产品类型]生成一张[平台，如 iOS/Android/Web]界面图。
核心功能：[功能点A]、[功能点B]、[功能点C]。
视觉风格：[极简/科技/拟物]，主色[颜色]，强调色[颜色]。
布局：[顶部导航/双栏/卡片流]，信息层级清晰，留白充足。
输出：高保真UI截图，文字清晰可读，比例[9:16/16:9]。

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/ui-system (v1.1)`.

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
