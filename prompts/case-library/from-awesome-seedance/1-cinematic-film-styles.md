---
title: "1. Cinematic Film Styles"
source_repo: awesome-seedance
source_url: https://github.com/ZeroLu/awesome-seedance/blob/main/README.md
credit: ZeroLu
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [poster, ui-system, ad-series]
inputs: {"text": true}
assets:
  []
---

_No source-repo demo asset attached for this case._

## Original prompt

Style: Hollywood Professional Racing Movie (Le Mans Style), Cinematic Night, Rain, High Stakes Sport.
Duration: 15s.

[00-05s] Shot 1: The Veteran (Interior/Close-up).
Rain lashes the windshield of a high-tech race car on a track. The Veteran driver (in helmet) looks over, calm and focused. Dashboard lights reflect on his visor.
Dialogue Cue: He gives a subtle nod and mouths "Let's go."

[05-10s] Shot 2: The Challenger (Interior/Close-up).
Cut to the rival car next to him. The younger driver grips the wheel tight, breathing heavily. Eyes wide with adrenaline.
Dialogue Cue: He whispers "Focus" to himself.

[10-15s] Shot 3: The Green Light (Wide Action).
The starting lights turn Green. Both cars accelerate in perfect sync on the wet asphalt. Water sprays massively into the camera lens. Motion blur turns the stadium lights into long streaks of color.

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
