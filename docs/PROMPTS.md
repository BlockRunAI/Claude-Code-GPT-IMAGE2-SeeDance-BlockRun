# Prompt Engineering Notes

This is the working knowledge distilled from the three source repos
(`awesome-gpt-image-2-prompts`, `awesome-gpt-image-2`,
`awesome-seedance-2-guide`) plus our own runs. Read it before editing the
templates in `prompts/` or before writing your own command in v1.1+.

---

## Universal principles

### 1. State the *medium* before the content

GPT Image 2 and Seedance both interpret style cues from words like
*"cinematic key art"*, *"editorial portrait"*, *"hand-drawn animation cell"*,
*"Hasselblad medium-format"*. Lead with the medium so the model picks the
right rendering mode.

### 2. Identity preservation needs explicit guarding

For image-to-image edits (`/headshot`) and image-to-video (`/dance`), the
model will drift facial structure unless you say:

> Maintain facial features, skin tone, hair color, and identity exactly as
> in the source image — only restyle environment, lighting, and wardrobe.

Treat this as a contract clause, not flavor text.

### 3. Negative prompts via "Avoid"

Both models honor an explicit `Avoid:` section better than a NOT-X
instruction. Use it for the well-known failure modes:

```
Avoid: extra limbs, identity drift, hands distorting, motion blur on face,
wardrobe morphing mid-shot.
```

### 4. Hierarchy of attention

Composition phrases that work:
- *"head-and-shoulders crop, eyes at upper third"*
- *"subject occupies lower-third; upper two-thirds is sky"*
- *"strong silhouette readability, hierarchy flows from title → image → tagline → credits"*

Vague prompts ("nice composition") are wasted tokens.

### 5. Lighting verbs

These pay off:
- *butterfly key*, *Rembrandt key*, *clamshell*, *rim from camera-left*
- *golden-hour bounce*, *sodium-vapor accent*, *volumetric haze*
- *practical lights only*, *single hard key*, *soft window light*

---

## GPT Image 2 specific

### Strengths

- **Multilingual typography.** Renders CJK, Arabic, Cyrillic, Hebrew with
  high accuracy. Other models hallucinate glyphs.
- **Character consistency under edit.** With `action="edit"`, it preserves
  faces 1:1 if the prompt instructs it to.
- **Reasoning-driven layout.** It respects compositional instructions
  ("title at upper-third, faux credits at the bottom in tiny condensed
  caps") more reliably than DALL-E 3.

### Weaknesses

- Slow path: ~10–20 s for HD outputs (still synchronous, no polling).
- Premium price tier — use `gpt-image-1` or `nano-banana` for
  thumbnails / scratch work.
- Will sometimes over-retouch skin into "AI plastic" — counter with
  the "natural texture" addendum in `prompts/headshot.md`.

### Sizing strategy

- Avatars / square covers: `1024x1024`
- Cinematic key art: `1792x1024`
- Movie one-sheets / phone wallpapers: `1024x1792`

---

## Seedance specific

### Why `bytedance/seedance-2.0-fast` is the default for `/dance`

| Model | $/sec | Quality | Wall time |
|---|---|---|---|
| `seedance-1.5-pro` | 0.03 | OK 720p | fast |
| `seedance-2.0-fast` | 0.15 | Excellent 720p | 60–180s ← sweet spot |
| `seedance-2.0` | 0.30 | Reference-class | slower |
| `xai/grok-imagine-video` | 0.05 | Variable | fast |

For a 5-second clip:
- 1.5-pro = $0.15
- 2.0-fast = $0.75
- 2.0 = $1.50
- xAI = $0.40

`2.0-fast` is the price/quality knee. Override with
`/dance --model bytedance/seedance-2.0` when you want reference-class
output and you're OK paying 2x.

### Motion description

Seedance responds best when motion is described in terms of:
- **Body parts** — "chest pops", "shoulder isolations", "weight shift to right hip"
- **Phrasing** — "two distinct 8-counts", "a controlled fall and a slow rebound rise"
- **Camera** — "slow circular dolly", "handheld-but-stable", "locked tripod"

Vague motion verbs ("dance well", "move energetically") underperform.

### Identity drift addenda are mandatory

Always include the "face is locked to the source image" clause. Seedance
will reinterpret the face otherwise — especially on stylized choreography
like K-pop or terracotta-disco.

---

## Common retry recipes (used by the skills)

When a result fails the user-eye test, the skill auto-retries with one
of these append clauses. Each is phrased as a *contract amendment*.

| Failure | Append clause |
|---|---|
| Different person | "CRITICAL: image-to-image edit, NOT re-imagining. Preserve eye spacing, nose bridge, jawline, hairline, skin tone 1:1." |
| Plastic skin | "Show pores, faint stubble, soft tonal variation. Aim for Hasselblad portrait, not a beauty filter." |
| Title gibberish | "Title MUST read exactly: \"{title}\". Verify each glyph. CJK / Arabic / Cyrillic accuracy is mandatory." |
| Static motion | "Increase motion energy: clear limb arcs, rotating upper body, two visible weight shifts in 5 seconds." |
| Hands warping | "Hands have five fingers each, anatomically correct, every frame." |
| Wardrobe morph | "Clothing identical to source frame for entire duration: same garment, color, fit." |

---

## Building a new template

To add a new command (`/character-sheet`, `/ui-system`, etc. for v1.1):

1. Decide which MCP tool: image vs video.
2. Decide which model from the price table.
3. Write a master template with `{slot}` variables.
4. Write 3–6 style/genre variants.
5. Add 2–4 retry addenda for known failure modes.
6. Save to `prompts/<command>.md` following the headshot/dance/poster shape.
7. Mirror the SKILL.md pattern: wallet preflight → prepare prompt → MCP call → download → report → fail handling.

The **shape stays constant** so the user's mental model transfers across
commands.
