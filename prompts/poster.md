# `/poster` prompt templates

> Used by `skills/poster/SKILL.md`. The skill reads this file, picks the
> matching genre block, substitutes variables, and calls
> `mcp__blockrun__blockrun_image` with `model="openai/gpt-image-2"`.
>
> **Why gpt-image-2:** it renders multilingual typography accurately —
> critical for poster work where the title is part of the composition.
>
> **Default size:** `1792x1024` (landscape — best for film stills + festival
> banners). Use `1024x1792` (portrait) for traditional movie one-sheets via
> `--portrait`.

---

## Master template

```
A cinematic {format} poster for "{title}".

Genre: {genre}
Mood: {mood}
Lead subject(s): {subject_description}
Composition: {composition}
Lighting: {lighting}
Color palette: {palette}
Typography: render the title "{title}" prominently in {font_style} at
{title_position}. Below the title, a tagline line reading
"{tagline}" in a smaller complementary face. Include a faux credit block
at the bottom: "{credit_block}".

Aspect: {aspect_hint}
Texture: subtle film grain, deep blacks, professional color grade.

This is a marketing key art image — strong silhouette readability, hierarchy
flows from title → image → tagline → credits, no clutter, frame edges are
intentional negative space.
```

---

## Genre variants

### `thriller` (gritty, suspense, neo-noir)

```
{mood}: tense, paranoid, mysterious; viewer feels watched
{composition}: lone protagonist mid-frame, shoulders forward, half-shadowed
              face; vast empty negative space above their head
{lighting}: chiaroscuro, single hard key from off-frame, deep shadows
            swallowing background details
{palette}: charcoal, oxidized green, blood-rust accents; ~70% black
{font_style}: heavy sans-serif (think Helvetica Inserat) compressed;
              all caps; slight chromatic aberration on the title
{title_position}: lower-third, centered
```

### `sci-fi` (epic, cosmic, future-forward)

```
{mood}: vast, awe-inspiring, technologically sublime
{composition}: subject as small silhouette against an enormous structure
              (megastructure / planetary horizon / orbital ring)
{lighting}: rim light from a distant cosmic source (sun / portal / engine
            glow); subtle volumetric haze
{palette}: deep navy + cyan + warm signal-orange contrast accents
{font_style}: futuristic geometric sans (think Eurostile / Neue Haas Unica
              Condensed Bold); subtle monospace tracking
{title_position}: upper-third or lower-third — never center
```

### `romcom` (warm, playful, character-forward)

```
{mood}: hopeful, bright, romantically optimistic
{composition}: two protagonists in playful interaction (back-to-back / one
              looking away while the other smiles), shot at golden hour
{lighting}: warm golden-hour bounce, soft and forgiving
{palette}: cream + dusty pink + sunset gold
{font_style}: handwritten-meets-display script for the title; clean serif
              for the tagline (think Caslon italic)
{title_position}: top, slightly diagonal
```

### `documentary` (founder-story / true-events vibe — Your Majesty's "创业纪录片")

```
{mood}: earnest, observational, fly-on-the-wall yet aspirational
{composition}: tight portrait of the protagonist at work — laptop / lab /
              workshop — slight motion blur from candid moment
{lighting}: practical naturalistic — desk lamps, monitor glow, window light
{palette}: muted denim, paper-white, warm tungsten accents; high realism
{font_style}: clean modern serif for title (Mercury Display / GT Sectra);
              compact grotesque for subtitle
{title_position}: bottom-third, left-justified, treated like a book cover
```

### `concert` (k-pop / festival / live event poster)

```
{mood}: high-energy, in-your-face, FOMO-inducing
{composition}: lead artist mid-pose taking up 60% of frame; secondary
              graphic motifs (lightning / bursts / typographic shapes)
              filling negative space
{lighting}: stage spotlight key + rim, lens flare on hits
{palette}: high-saturation duotone (e.g., hot pink + electric blue) OR
           single accent color over deep black
{font_style}: oversized display sans (think Druk Wide); title can break
              the bounding box
{title_position}: dominates upper half, can overlap subject
```

### `horror` (psychological, atmospheric)

```
{mood}: dread, unease, what-you-don't-see-is-worse
{composition}: extreme negative space; subject is a small silhouette OR a
              single uncanny detail (door ajar, eye in shadow); rule-of-thirds
              gives the viewer somewhere to escape to but keeps them stuck
{lighting}: minimal — one cold practical light, hint of sodium-vapor orange
            from a distant streetlamp
{palette}: ~85% black, sodium-orange accents, pale skin tones
{font_style}: distressed slab serif OR a fragile thin sans that "trembles"
{title_position}: bottom, small, almost a whisper
```

### `kids-animation` (family-friendly animated film vibe)

```
{mood}: warm, adventurous, hopeful, slight whimsy
{composition}: hero character + sidekick at lower-third, expansive sky /
              landscape filling the upper two-thirds, dynamic depth
{lighting}: full daylight, soft cloud shadows, characters slightly
            front-lit for clarity
{palette}: saturated primary triad (sky blue + grass green + warm yellow)
           with one accent character color
{font_style}: rounded display (think custom Disney / Pixar lockup);
              slight 3D bevel on the title
{title_position}: bottom, large, becomes part of the landscape
```

### `event` (conference / podcast / launch-day banner)

```
{mood}: clean, premium, "you should buy a ticket"
{composition}: bold typographic-led layout; subject (speaker portrait or
              product render) anchored to one third
{lighting}: studio flat-lit subject, contrasting graphic background
{palette}: brand-driven — derive from `--accent_color` or default to
           deep indigo + electric mint
{font_style}: contemporary geometric sans (Inter / Söhne) with a tight
              display headline; consistent grid
{title_position}: large headline + date + location stack on left; subject
                  on right
```

---

## Defaults the skill auto-fills if user doesn't specify

```
{format}        = "feature film one-sheet"
{aspect_hint}   = "landscape 1.85:1 cinematic crop"
{tagline}       = "" (omit the tagline line entirely if blank)
{credit_block}  = a fake but plausible "directed by / starring / studio"
                  line in tiny condensed caps. The skill's caller may pass
                  a real credit block via --credits.
```

---

## Common pitfalls + retry addenda

### "Title text is gibberish / wrong language"

Append:
```
The title MUST read exactly the characters: "{title}" — verify each glyph.
If rendering Chinese / Japanese / Korean, ensure correct CJK characters
and traditional vs simplified consistency. Do not invent letters.
```

### "Composition is too busy / no negative space"

Append:
```
Strip background detail by 60%. The hero subject + title + 30% empty
space is the goal. A movie poster is read in 0.5 seconds — hierarchy first,
detail second.
```

### "Looks like AI / overly painterly"

Append:
```
Render in a photorealistic key-art style with very subtle film grain. Avoid
illustrated brush strokes unless the genre is animation. Reference: think
"theatrical one-sheet shot on 70mm", not "Midjourney v3 fantasy splash".
```

---

## Usage examples

```bash
/poster "Last Light" --genre thriller
/poster "Founders" --genre documentary --tagline "they bet everything"
/poster "BlockRun Live" --genre event --accent_color "#0066ff" --portrait
/poster "兵马俑：复活" --genre sci-fi  # CJK title — gpt-image-2 handles it
```
