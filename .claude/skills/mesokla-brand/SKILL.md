---
name: mesokla-brand
description: The @mesokla visual identity for X/Twitter — three colours only (leaf #A6B8A0, violet #8B729C, crimson #E20942), Montserrat Black uppercase + Manrope, and render-ready templates for the profile banner, post visuals, thread covers, lists, collab announcements, 4:5 stacks and animated intros. Use whenever the user asks for a banner, header, post visual, thread cover, announcement card, carousel, avatar treatment, animated video/intro, or says "in my style", "brand it", "зроби візуал", "банер", "обкладинка треду". Always apply these rules before designing anything for mesokla.
---

# mesokla brand

Owner: @mesokla, web3 marketer at @solus_group, Ukraine. Bio line: "smtm sense, smtm mess".
Style in one line: **flat blocks of three colours, big bold uppercase type, nothing else.**
Visual reference: `brandbook.html`. Ready renders: `out/`.

## Hard rules (the owner rejected the opposite)

- Only the three colours below. No white, black, grey, gradients, textures, patterns, noise, shadows, illustrations or mascots.
- Headlines in Montserrat Black 900, UPPERCASE. No serif, no italics.
- Simple layouts: one background colour (or 2–3 flat colour bands), text, at most one highlight block.

## Colours (`brand.css`)

| name | hex | use |
|---|---|---|
| Leaf Skin | `#A6B8A0` | main background, text on violet/crimson |
| Muted Violet | `#8B729C` | threads/collabs background, highlight on leaf, secondary text on leaf |
| Electric Crimson | `#E20942` | main text on leaf, hot-take background, highlight on violet |

Readable pairs only: crimson on leaf, violet on leaf, leaf on violet, leaf on crimson. **Never** crimson text on violet or violet text on crimson.

Themes (`theme=`): `leaf` (default: bg leaf, text crimson, secondary violet, highlight violet) · `violet` (bg violet, text leaf, highlight crimson) · `crimson` (bg crimson, text leaf, highlight violet). Banner also has `stripes`.

## Type

- **Display:** Montserrat 900, uppercase, line-height 0.92–1, tracking -0.01em. Headline ≤ 10 words.
- **Small text:** Manrope 600–800. Lists ≥ 32px on 1600×900. Kickers/labels uppercase, tracked .16em.
- Highlight: wrap one word in `*stars*` → it gets a flat block in the highlight colour. Max one per visual.
- Fonts bundled in `fonts/` (OFL, Latin + Cyrillic, so Ukrainian works).

## Templates (`templates/*.html`)

Render: `node scripts/render.mjs <template> <out.png> key=value ...` (needs Playwright). `|` = new line / new list item.
Common keys: `theme`, `kicker` (top-left label), `tag` (top-right pill), `handle`.

| template | size | keys |
|---|---|---|
| `banner` | 1500×500 | `theme` leaf/violet/crimson/stripes, `name`, `tag`, `corner`. Avatar covers bottom-left ~330×170 — keep empty |
| `quote` | 1600×900 | `text` |
| `thread` | 1600×900, violet | `title`, `sub`, `count` ("1 / 9") |
| `sense-mess` | 1600×900 | `sense`, `mess` (2–4 items each, `|`-separated, ≤6 words) |
| `list` | 1600×900 | `title`, `items` (3–6, `|`-separated) |
| `collab` | 1600×900 | `partner`, `what`, `date` |
| `stack` | 1080×1350 | `t1`, `t2`, `t3` (one idea per colour band), `kicker` |
| `intro` | 1600×900, animated 4s | `name`, `tag` — render with `scripts/video.mjs` |

Other sizes: `size=WxH` (e.g. article cover `size=1500x600`).
Video: `node scripts/video.mjs templates/intro.html out/intro.mp4 4 1600 900 30`. Animated templates must use CSS keyframes only so they can be scrubbed frame by frame.

New template: an HTML file in `templates/` linking `../brand.css`, using `.canvas`, `.frame/.top/.bottom`, `.display`, `.label`, `.pill`, `.sig`, plus `<script src="fill.js">`.

## Pillars → theme

Sense (tools, frameworks) → `leaf` · Threads & collabs → `violet` · Mess (hot takes, fails) → `crimson`.

## Workflow

1. Pick the pillar → theme and the template.
2. Write short lowercase-agnostic copy (it renders uppercase); confirm partner names, dates and numbers with the user.
3. Render, look at the PNG, check: only three colours, no forbidden pair, text not clipped, avatar zone empty on banners, ≤1 highlight.
4. Deliver the file plus the exact command used.
