---
name: mesokla-brand
description: The @mesokla visual identity (X/Twitter) — palette, fonts, leaf-vein motif, Mesy the witch mascot, and render-ready templates for the profile banner, post visuals, thread covers, memes and animated intros. Use whenever the user asks for a banner, header, post visual, thread cover, meme, announcement card, avatar treatment, mascot pose, animated video/intro, or says "in my style", "brand it", "зроби візуал", "банер", "обкладинка треду", "Мессі", "відьмочка". Always apply these rules before designing anything for mesokla.
---

# mesokla brand

Brand idea comes from the bio: **smtm sense, smtm mess**. Leaf (calm, sense) vs crimson (chaos, mess), violet = the magic between. Visual world: a night garden / grimoire on X dark mode. Owner: web3 marketer at @solus_group, Ukraine.

Open `brandbook.html` for the visual reference. Everything is reproducible from this folder.

## 1. Tokens (source of truth: `brand.css`)

| token | hex | role |
|---|---|---|
| Leaf Skin | `#A6B8A0` | "sense", useful content backgrounds |
| Muted Violet | `#8B729C` | "magic", collabs/announcements, Mesy's hat |
| Electric Crimson | `#E20942` | accent, one highlighted word, CTA, "mess" |
| Night Ink | `#0E0B10` | base background |
| Deep Plum | `#2B1F33` | surfaces on dark, Mesy's cloak |
| Bone | `#F3EDE4` | text on dark |

Proportion ≈ ink 55 / leaf 20 / violet 15 / crimson 10. Crimson is an accent, not a fill, except on `crimson` theme pieces.
Safe pairs: bone+crimson on ink · ink+crimson on leaf · bone+ink on violet · bone+ink on crimson. Never crimson text on violet, never white text on leaf.

Type: **Cormorant Garamond** 600/italic (display, wordmark, quotes) · **Inter** 400–600 (body, min 32px on 1600×900) · **JetBrains Mono** uppercase, tracked .18em (kickers, handle, numbers, dates). Fonts are bundled in `fonts/` (OFL).

Wordmark: `mesokla` in Cormorant italic 600, lowercase, followed by a crimson four-point star ✦ top-right.

Motifs: crimson leaf veins (`assets/veins-*.svg`, opacity 20–40%, never under text strokes) · four-point star ✦ (max 4 per visual) · subtle film grain.

## 2. Content pillars → theme

| pillar | theme | for |
|---|---|---|
| Sense | `leaf` | frameworks, tools, checklists (saves) |
| Mess | `crimson` | fails, POV memes, behind the scenes (shares) |
| Magic | `violet` | collabs, spaces, launches (status) |
| Night notes | `night` (default) | hot takes, quotes (replies) |

Pick the theme from the pillar. If unclear, ask once or default to `night`.

## 3. Templates (`templates/*.html`)

Render: `NODE_PATH=$(npm root -g) node scripts/render.mjs <template> <out.png> key=value ...`
Value syntax: `|` = new line / new list item, `*word*` = crimson italic emphasis. Common keys: `theme`, `handle`, `kicker`, `tag`, `mascot=../mascot/mesy-<pose>.svg`.

| template | size | keys |
|---|---|---|
| `banner` | 1500×500 X header | `theme` night/leaf/crimson, `mascot`, `l`, `r` (tagline halves). Avatar covers bottom-left ~330×170px — keep empty |
| `quote` | 1600×900 | `text`, `kicker`, `tag`, optional `mascot` |
| `thread` | 1600×900 | `title`, `eyebrow`, `sub`, `count` ("1 / 9"), `mascot` |
| `sense-mess` | 1600×900 | `sense`, `mess` (items with `|`, 2–4 each, ≤6 words) — signature format |
| `list` | 1600×900 | `title`, `items` (3–6, `|`-separated), `tag` |
| `collab` | 1600×900 (violet default) | `partner`, `what`, `date`, `tag` |
| `meme` | 1080×1350 (leaf default) | `text`, `bubble`, `mascot`, `kicker` |
| `intro` | 1600×900 animated, 4s | `tag`. Render with `scripts/video.mjs` |

Video: `node scripts/video.mjs templates/intro.html out/intro.mp4 4 1600 900 30` — scrubs CSS keyframes frame by frame into H.264 MP4. New animated templates must use only CSS animations (no JS timers) so they scrub.

Ready renders of every template live in `out/`.

## 4. Mesy (the mascot)

Name = mesokla + mess. Tiny witch-marketer: violet hat with crimson band, star and a leaf-vein leaf on the tip; wheat hair `#E9D6B0` (only off-palette colour, Mesy only); plum cloak with crimson lining; crimson star wand with glow. Flat vector sticker, 4px ink outline, no shadows/3D.

Poses in `mascot/`: `mesy.svg` (default, confident) · `mesy-happy.svg` (it worked!) · `mesy-wow.svg` (shocked) · `mesy-content.svg` (pleased). New poses: copy `mesy.svg` and toggle/edit layers by id: `m-body, m-hair-back, m-head, m-face, m-blush, m-eyes-open, m-eyes-closed, m-lashes, m-mouth-smile, m-mouth-open, m-bangs, m-hat, m-leaf, m-arm, m-wand, m-sparkles`. Keep the 400×480 viewBox.

Rules: Mesy in ~1 of every 3–4 visuals; may be cropped at the waist / peek from an edge; never recoloured, stretched, placed over text, or on crimson without her outline. Animation basics: 2s bob, blink every 3–4s, wand-star flash before text appears, twinkling stars.

## 5. Voice on visuals

Lowercase, English, short. Witchy vocabulary used lightly: spells, grimoire, cauldron, familiar, casting. Headline ≤ 8 words, one crimson-italic word max. Ukrainian copy works too (fonts include Cyrillic).

## 6. Workflow

1. Identify the pillar → theme, and the template (or build a new HTML in `templates/` that links `../brand.css` and `post.css` and reuses `.frame/.top/.bottom/.sig`).
2. Write the copy in the brand voice; confirm text with the user if it is a claim about a partner or numbers.
3. Render to `out/` (or the user's chosen folder), then look at the PNG before handing it over.
4. QA: text not on thick veins, nothing in the banner avatar zone, ≤1 crimson word, ≤4 stars, handle bottom-right, signature bottom-left.
5. Deliver PNG/MP4 and the exact command used so the user can re-render.

X sizes: header 1500×500 · in-feed image 1600×900 (16:9) or 1080×1350 (4:5) · avatar 400×400 · article cover 1500×600 (use `size=1500x600` with any template).
