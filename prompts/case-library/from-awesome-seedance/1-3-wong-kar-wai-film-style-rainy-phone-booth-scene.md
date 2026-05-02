---
title: "1.3. Wong Kar-wai Film Style (Rainy Phone Booth Scene)"
source_repo: awesome-seedance
source_url: https://github.com/ZeroLu/awesome-seedance/blob/main/README.md
credit: ZeroLu
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [poster, ui-system, ad-series, food]
inputs: {"text": true}
assets:
  []
---

_No source-repo demo asset attached for this case._

## Original prompt

[Film Style]: 90s Hong Kong Art Cinema style, retro film feel, high ISO grain, ambiguous yellow-green tint, frame stepping effect, melancholic atmosphere.

[Core Dialogue (for emotion control)]: "If memories were canned food, I hope they never expire."

[Video Duration]: 10 seconds
[Script]:

[00:00-00:04] Shot 1: Through the Glass Peeping.
Scene: A rain-covered red public telephone booth.
Character: A man (or woman) in a khaki trench coat holding the receiver tightly, not speaking, just listening.
Emotional Performance: Through the glass refraction, see his/her eyes hollow yet deeply emotional. Rain flows down the glass, distorting his face like an oil painting.
Subtitle/Narrative sense: The picture seems frozen, only the sound of rain.

[00:04-00:07] Shot 2: Extreme Close-up & Micro-expression.
Scene: Focus on the character's lips and half face.
Action: He/She whispers softly into the receiver. Lips tremble slightly, seeming to want to say something but swallow it back.
Lighting: Street neon bokeh flows across his face, bright and dim alternately.
Dialogue Emotion Mapping: Shows the ultimate restraint and loneliness of "wanting to touch but drawing back".

[00:07-00:10] Shot 3: Signature Slow-shutter Drag Shadow.
Scene: Character hangs up phone, turns around and walks into the rainy crowd.
Visual Effect: Using frame stepping effect (stop-motion feel), the character's back becomes blurred with trailing shadows (motion blur), as if the soul stayed in place while only the body walks away.
Environment: Background is flowing city car lights forming elongated light trails.

[Technical Parameters]: Simulated handheld camera, shallow depth of field, color shift, emotionally intense.

## Run via Claude Code

After installing `Claude Code-GPT-IMAGE2-SeeDance-BlockRun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/poster`.

```text
# Suggested invocation (manual prompt — wire into a command in v1.1+)
> Use the prompt above with mcp__blockrun__blockrun_image, model=bytedance/seedance-2.0-fast,
  action=generate.
```

## Credit & license

Sourced from [awesome-seedance](https://github.com/ZeroLu/awesome-seedance/blob/main/README.md) by ZeroLu.
This case file is part of the curated `prompts/case-library/` in the
[Claude Code-GPT-IMAGE2-SeeDance-BlockRun](https://github.com/BlockRunAI/Claude-Code-GPT-IMAGE2-SeeDance-BlockRun)
bundle. Reproduced with attribution; original license applies.
