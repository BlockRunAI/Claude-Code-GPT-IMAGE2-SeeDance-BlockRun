---
title: "目录结构"
source_repo: awesome-seedance-2-guide
source_url: https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/GITHUB_SETUP.md
credit: EvoLinkAI
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [dance, ui-system, ad-series, unbox]
inputs: {"text": true}
---

## Original prompt

jimeng-seedance-2.0-guide/
├── README.md                          # 主文档（已创建）
├── LICENSE                            # 许可证
├── CONTRIBUTING.md                    # 贡献指南
├── CHANGELOG.md                       # 更新日志
│
├── docs/                              # 文档目录
│   ├── 01-overview.md                 # 概述
│   ├── 02-parameters.md               # 参数预览
│   ├── 03-interaction.md              # 交互形式
│   └── 04-capabilities/               # 能力详解
│       ├── 01-basic-enhancement.md
│       ├── 02-multimodal.md
│       ├── 03-consistency.md
│       ├── 04-camera-movement.md
│       ├── 05-creative-templates.md
│       ├── 06-story-completion.md
│       ├── 07-video-extension.md
│       ├── 08-audio-quality.md
│       ├── 09-continuity.md
│       ├── 10-video-editing.md
│       ├── 11-music-sync.md
│       └── 12-emotion.md
│
├── examples/                          # 使用案例
│   ├── case-01-character-consistency.md
│   ├── case-02-character-replacement.md
│   ├── case-03-complex-camera.md
│   ├── case-04-product-showcase.md
│   └── case-05-multi-scene.md
│
├── prompts/                           # 提示词模板
│   ├── template-01-storytelling.md
│   ├── template-02-product-showcase.md
│   ├── template-03-character-scene.md
│   └── template-04-music-sync.md
│
├── assets/                            # 图片资源（可选）
│   └── images/
│
└── .github/                           # GitHub 配置
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── feature_request.md
    └── workflows/
        └── stale.yml                  # 自动清理旧 Issue

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/dance`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-seedance-2-guide](https://github.com/EvoLinkAI/awesome-seedance-2-guide/blob/main/GITHUB_SETUP.md) by EvoLinkAI.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
