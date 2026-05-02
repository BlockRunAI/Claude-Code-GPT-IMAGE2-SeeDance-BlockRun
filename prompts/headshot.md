# `/headshot` prompt templates

> Used by `skills/headshot/SKILL.md`. The skill reads this file, picks the
> matching style template, and substitutes `{variable}` slots before calling
> `mcp__blockrun__blockrun_image` with `action="edit"` (image2image).
>
> **Model:** `openai/gpt-image-2` — best at face-consistency under edit.
> **Size:** `1024x1024` square (LinkedIn / Twitter avatar friendly).
> **Quality:** `hd`.

---

## Master template (used when the user provides only a photo)

Default `{style}` is `corporate` if the user doesn't say. Default `{wardrobe}` is derived from style.

```
Transform the person in this image into a professional headshot.

Maintain facial features, skin tone, hair color, and identity exactly as in
the source image — only restyle environment, lighting, and wardrobe.

Background: {background}
Lighting: {lighting}
Wardrobe: {wardrobe}
Composition: head-and-shoulders crop, eyes at upper third, slight three-quarter
turn, looking just past camera, gentle natural smile.

Render at high resolution with sharp focus on the eyes, soft skin retouching
that preserves pores and natural texture (do NOT smooth into plastic),
neutral white balance, suitable for LinkedIn or a corporate website.

Do not add text, watermarks, logos, or borders. Do not change the person's
ethnicity, age, gender, or facial structure.
```

---

## Style variants

The skill picks one of these by `--style` (or asks the user if unset).

### `corporate` (default — investment-bank / consulting / law-firm vibe)

```
{background}: smooth charcoal-to-graphite gradient, soft vignette
{lighting}: butterfly key with subtle fill, hint of rim light from camera-left
{wardrobe}: tailored navy suit jacket, crisp white shirt, no tie OR a single
            understated dark tie; minimalist accessories only
```

### `creative` (designer / writer / agency creative director)

```
{background}: warm neutral wall (oat / clay / sage), shallow depth of field
{lighting}: soft window light from camera-left, golden-hour warmth
{wardrobe}: well-fitted casual blazer over a fine-knit crewneck OR a
            high-quality oversized denim shirt; one tasteful watch or ring
```

### `startup` (founder / engineer / PM — modern tech aesthetic)

```
{background}: out-of-focus modern workspace (concrete + warm wood tones) OR
              clean off-white seamless paper
{lighting}: bright diffused daylight, slight cool tone, no harsh shadows
{wardrobe}: high-quality plain crew tee in navy / charcoal / cream, OR a
            zip-up technical sweater; no logos
```

### `actor` (headshot for casting / talent agencies)

```
{background}: solid neutral grey or muted teal seamless paper
{lighting}: clamshell lighting (large soft key + reflector fill), eyes catch
            two clear specular highlights
{wardrobe}: solid-color simple top in a hue that complements skin tone, no
            patterns, no jewelry, no collar that distracts from face
```

### `linkedin-2025` (the "I just got promoted" vibe — slightly aspirational)

```
{background}: slightly out-of-focus modern office or warm-tone neutral wall
{lighting}: warm Rembrandt-style key with soft fill, faint rim from behind
{wardrobe}: structured blazer over a knit tee OR a polished button-down with
            top button open; sleeves clean, posture confident-but-relaxed
```

---

## Multi-variant batch (used when the user passes `--all`)

The skill calls `blockrun_image` 4 times in series, swapping `{style}`, and
saves each as `headshot-<style>.png`. Total cost ≈ $0.48.

---

## Common pitfalls + auto-retry templates

If the first response shows any of these, the skill should retry with the
matching addendum appended to the prompt.

### "Looks like a different person"

Append:
```
CRITICAL: this is an image-to-image edit, NOT a re-imagining. Preserve the
exact facial geometry of the source: eye spacing, nose bridge, jawline,
hairline, and skin tone must match the source 1:1. Treat this as a
"clothing + lighting + background" swap only.
```

### "Too plastic / over-retouched"

Append:
```
Skin must show natural texture: pores, faint stubble or peach fuzz where
applicable, soft tonal variation. Avoid the "AI plastic" smoothness — aim
for the polish of a Hasselblad medium-format portrait, not a beauty filter.
```

### "Wrong wardrobe / colors clashing"

Append:
```
Wardrobe color must complement the source's skin undertone. If the source
appears to be {warm/cool/neutral}-toned, choose {complementary palette}.
Avoid pure black and pure white if they fight the skin tone.
```

---

## Usage examples (passed by the skill to the user as cheat-sheet)

```bash
/headshot ./me.jpg
/headshot ./me.jpg --style startup
/headshot ./me.jpg --style actor
/headshot ./me.jpg --all   # 4 styles in one go
```
