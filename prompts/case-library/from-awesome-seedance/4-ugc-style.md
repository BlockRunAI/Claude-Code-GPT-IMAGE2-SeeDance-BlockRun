---
title: "4. UGC Style"
source_repo: awesome-seedance
source_url: https://github.com/ZeroLu/awesome-seedance/blob/main/README.md
credit: ZeroLu
workflow: text2video
model: bytedance/seedance-2.0-fast
tags: [ui-system, ad-series]
inputs: {"text": true}
assets:
  []
---

_No source-repo demo asset attached for this case._

## Original prompt

【Style】Mockumentary (Vlog Style), hyperrealism, fixed-camera real-shot feel, natural lighting, with a slight suspenseful comedy tone.
【Duration】15 seconds
【Main Character】An ordinary young beautiful woman, in front of the bathroom sink at home.
[00:00-00:06] Shot 1: Daily setup (Normalcy).
Scene: In front of a regular bathroom mirror.
Action: The protagonist is brushing her teeth, mouth full of foam. She makes various funny faces (squinting, eyebrow-wiggling) at the mirror while brushing her teeth.
Key detail: At this point, the reflection in the mirror is completely normal, movements synchronized.
[00:06-00:11] Shot 2: BUG appears (The Glitch).
Action: After brushing teeth, the protagonist lowers her head to spit out foam, then turns around to leave the bathroom.
High-impact moment (core climax): Just as the protagonist's real body has turned and left the mirror frame, the "reflection" in the mirror **doesn't move**! That "reflection" still maintains the tooth-brushing pose, even mischievously raising eyebrows at the camera with a bad smile, staying for a full 2 seconds, before suddenly panicking and "fast-forwarding" to catch up with the original body's movements before disappearing.
Director's note: Must create an extremely realistic "network delay" feel, as if the reflection has independent consciousness.
[00:11-00:15] Shot 3: Comedic callback (The Punchline).
Action: The protagonist, who has already walked to the door, seems to sense something is wrong, suddenly turning back to look at the mirror.
Result: The mirror has now completely returned to normal, completely empty, only reflecting the opposite wall. The protagonist scratches her head in confusion, showing a life-questioning expression toward the camera. The frame freezes on the protagonist's confused face (comedy effect).

## Run via Claude Code

After installing `Claude Code-GPT-IMAGE2-SeeDance-BlockRun`, you can adapt this case
into one of the bundle's commands. Closest match for this case based on
detected tags: `/ui-system (v1.1)`.

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
