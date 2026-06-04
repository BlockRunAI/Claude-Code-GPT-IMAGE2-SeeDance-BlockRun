# `/dance` prompt templates

> Used by `skills/dance/SKILL.md`. The skill reads this file, picks the matching
> dance-style block, substitutes variables, and calls
> `mcp__blockrun__blockrun_video` with `image_url` (image-to-video) +
> `model="bytedance/seedance-2.0-fast"` + `duration_seconds=5`.
>
> The MCP tool blocks while polling for ~60–180s, then returns a permanent
> mp4 URL. The skill downloads it to `./blockrun-out/{ts}-dance/dance.mp4`
> and runs `ffmpeg` to also produce a shareable `dance.gif`.

---

## Master template (Seedance 2.0-fast, image-to-video)

```
The person from the input image performs {style} dance choreography.
Full body remains visible throughout. Smooth, fluid motion synchronized to
an implied {bpm} BPM beat. Camera: {camera_motion}. Setting:
{environment}. Lighting: {lighting}. The person's facial identity, body
proportions, hairstyle, and clothing remain consistent across every frame.

Avoid: extra limbs, identity drift, hands distorting, motion blur on face,
wardrobe morphing mid-shot.
```

---

## Dance style variants

The skill picks one by `--style` (or asks). Each block fills the master
template's variables.

### `hiphop` (urban + crisp pops)

```
{style}: crisp street hip-hop — chest pops, body rolls, shoulder isolations,
         a confident two-step groove with clean weight transfers
{bpm}: 95
{camera_motion}: slow circular dolly around subject, ending with a gentle
                 push-in on the final pose
{environment}: neon-lit urban underpass with subtle rain reflections OR
               graffiti-tagged warehouse interior
{lighting}: cyan + magenta neon spill, hard rim light from behind
```

### `ballet` (graceful, classical)

```
{style}: classical ballet — a single grand jeté leading into a piqué turn
         and finishing in fourth position arabesque
{bpm}: 60
{camera_motion}: smooth slow-mo tracking shot, low angle that sweeps to eye
                 level on the final pose
{environment}: bright minimalist dance studio with floor-to-ceiling windows
               OR a gilded baroque theater stage with red velvet drapes
{lighting}: soft natural daylight from camera-left OR warm theatrical key
            with a faint backlight
```

### `contemporary` (emotional, expressive)

```
{style}: contemporary modern — flowing arm extensions, a controlled fall to
         the floor, then a slow rebound rise; focus on emotional fluidity
{bpm}: 70
{camera_motion}: handheld-but-stable, drifts in and out subtly
{environment}: empty industrial loft with shafts of dust-lit light OR a
               minimalist concrete plaza at golden hour
{lighting}: single hard key from a high window, deep falloff to shadow
```

### `kpop` (synchronized, idol-stage energy)

```
{style}: K-pop idol-style point choreography — sharp arm hits, hair flips,
         crisp footwork, a charismatic finishing pose facing camera
{bpm}: 120
{camera_motion}: dynamic — quick zoom on the final beat, slight whip-pan
                 mid-routine
{environment}: glossy black-mirror stage with LED panel walls flashing
               brand colors
{lighting}: stage spots, strobing accent lights, lens flares on hits
```

### `terracotta-disco` (兵马俑迪斯科 — viral meme combo)

```
{style}: Tang Dynasty terracotta warrior comes alive and dances disco —
         stiff-then-loose shoulder shimmies, retro point-and-pose moves, a
         signature hip drop
{bpm}: 110
{camera_motion}: slow orbit revealing the underground tomb opening up into
                 a 1970s disco
{environment}: terracotta army pit with disco ball descending from above,
               other warriors frozen mid-pose in the background
{lighting}: warm tungsten torches transitioning into rotating disco-ball
            sparkles + colored gels
```

### `tiktok-trend` (current viral choreography wedge)

```
{style}: a clean tight 5-second TikTok-style routine — two distinct
         8-counts of upper-body choreography with one signature move on
         the final beat that begs to be looped
{bpm}: 105
{camera_motion}: locked tripod, vertical 9:16-friendly framing
{environment}: a bright bedroom OR minimalist white wall (let the camera
               feel native to the platform)
{lighting}: soft front ring-light look, natural skin tones, slight peach
            warmth
```

### `freestyle-from-music` (when the user provides a music description)

```
{style}: choreography that responds to the following music: {user_music_description}
{bpm}: {inferred_or_user_supplied}
{camera_motion}: matched to musical phrasing — calm during verses, dynamic
                 on hits
{environment}: chosen to match the music's mood (let the model interpret)
{lighting}: matched to mood
```

---

## Common Seedance pitfalls + retry addenda

### Identity drift (face changes mid-clip)

Append:
```
The person's face is locked to the source image. Do not interpret or
restyle the face. Lip movement, eye direction, and head orientation may
change naturally, but underlying facial structure and skin tone must be
identical to the source frame.
```

### Hands warping into 6+ fingers

Append:
```
Render hands clearly with five fingers each at all times. If a hand passes
behind the body, it should reappear with anatomically correct fingers.
```

### Wardrobe morphing

Append:
```
Clothing remains identical to the source frame for the entire 5 seconds:
same garment type, same color, same fit. Do not introduce accessories or
patterns not present in the source.
```

### "Static feeling" (low motion energy)

Append:
```
Increase motion energy. Limbs should travel through clear arcs, the upper
body should rotate, weight should shift visibly between feet at least
twice in 5 seconds.
```

---

## Usage examples

```bash
/dance ./me.jpg
/dance ./me.jpg --style hiphop
/dance ./me.jpg --style terracotta-disco
/dance ./me.jpg --style freestyle-from-music --music "ambient lo-fi 75 bpm"
```
