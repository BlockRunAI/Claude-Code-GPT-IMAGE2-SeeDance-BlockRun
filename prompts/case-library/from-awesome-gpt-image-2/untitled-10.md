---
title: "场景与叙事"
source_repo: awesome-gpt-image-2
source_url: https://github.com/freestylefly/awesome-gpt-image-2/blob/main/docs/templates.md
credit: freestylefly
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: []
inputs: {"text": true}
---

## Original prompt

生成[故事主题]场景图，发生在[时间+地点]。
主事件：[事件描述]，主角：[角色]，冲突点：[冲突]。
镜头语言：[广角建立镜头/中景叙事/特写]。
氛围：[紧张/温暖/悬疑]，色调：[冷/暖/高反差]。
输出：具备叙事张力的场景概念图。

## Run via Claude Code

After installing `cc-gpt-image2-seedance-blockrun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `(case-library only — no v1 command match)`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2/blob/main/docs/templates.md) by freestylefly.
This case file is part of the curated `prompts/case-library/` in the
[cc-gpt-image2-seedance-blockrun](https://github.com/blockrunai/cc-gpt-image2-seedance-blockrun)
bundle. Reproduced with attribution; original license applies.
