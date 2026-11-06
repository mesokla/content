---
name: mesokla-brand
description: The @mesokla visual identity for X/Twitter — three colours only (leaf #A6B8A0, violet #8B729C, crimson #E20942), Montserrat Black uppercase + Manrope, the line-art moth brand mark, abstract wing elements, and render-ready templates for the profile banner, post visuals, thread covers, lists, collab announcements, 4:5 stacks and animated intros. Use whenever the user asks for a banner, header, post visual, thread cover, announcement card, carousel, avatar treatment, animated video/intro, or says "in my style", "brand it", "зроби візуал", "банер", "обкладинка треду". Always apply these rules before designing anything for mesokla.
---

# mesokla brand

Owner: @mesokla, web3 marketer at @solus_group, Ukraine.
**Language:** visuals and examples are in Ukrainian by default (template defaults are Ukrainian); use English only if the user asks.
**No tagline:** never put "smtm sense / smtm mess" (or any slogan) under the wordmark — the owner removed it. A new tagline may come later; leave the slot empty until then.
Style in one line: **flat blocks of three colours, big bold uppercase type, nothing else.**
Visual reference: `brandbook.html`. Ready renders: `out/`.

## Hard rules (the owner rejected the opposite)

- Only the three colours below. No white, black, grey, gradients, textures, patterns, noise, shadows or character mascots. The only illustration is the line moth and its abstract elements (below).
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

## The moth (brand mark) — `moth/`

Line-art moth: medium line (3.6px at 400px), one fine inner echo contour, wing spot. Owner picked it from line variants 1, 2 and 12.
Files: `moth-{front|flight|trail}-{crimson|violet|leaf}.svg` (`front` = symmetric mark, `flight` = in-flight perspective, `trail` = flight with dotted trail).
Colour by background: leaf bg → `crimson` line (violet echo); violet/crimson bg → `leaf` line.
Rules: outline only (never filled), never thicker/shadowed, never over text, max one per visual. Animate as wing flap (`.wl/.wr` groups, scaleX around x=200), line draw-on, or flight along the trail.
Signature lockup = front moth + MESOKLA. `fill.js` adds it to every `.sig` automatically (`sig=plain` to turn off).

## Abstract elements — `elements/`

`{wing|wings|contour|lens|trail|spot|curl|dots}-{crimson|violet|leaf}.svg`, all derived from the moth.
Shapes use the third colour: leaf bg → violet, violet bg → crimson, crimson bg → violet. One element per visual, large and cropped by the frame edge or small beside text, always behind text.
Add to any post template with `el=<name>` (or `el=moth` for the flight moth). Corner elements (wing, wings, contour, lens) hide the handle; text column narrows automatically.
Regenerate moth + elements: `python3 scripts/gen_moth.py`.

## Templates (`templates/*.html`)

Render: `node scripts/render.mjs <template> <out.png> key=value ...` (needs Playwright). `|` = new line / new list item.
Common keys: `theme`, `kicker` (top-left label), `tag` (top-right pill), `handle`, `el` (decor element), `sig=plain`.

| template | size | keys |
|---|---|---|
| `banner` | 1500×500 | `theme` leaf/violet/crimson/stripes, `moth` trail/flight/front/none (default trail), `name`, `tag`. Avatar covers bottom-left ~330×170 — keep empty |
| `quote` | 1600×900 | `text` |
| `thread` | 1600×900, violet | `title`, `sub`, `count` ("1 / 9") |
| `do-dont` | 1600×900 | `yes`, `no` (2–4 items each, `|`-separated, ≤6 words); headings `a`/`b` (default «так» / «не так»), labels `la`/`lb` |
| `list` | 1600×900 | `title`, `items` (3–6, `|`-separated) |
| `collab` | 1600×900 | `partner`, `what`, `date` |
| `stack` | 1080×1350 | `t1`, `t2`, `t3` (one idea per colour band), `kicker` |
| `intro` | 1600×900, animated 4.5s | `v` fly / draw / zoom, `theme` — render with `scripts/video.mjs` |

Other sizes: `size=WxH` (e.g. article cover `size=1500x600`).
Video: `node scripts/video.mjs "templates/intro.html?v=fly&theme=crimson" out/intro.mp4 4.5`.
Intro scenarios: **fly** (moth flies in along a dotted trail and lands above MESOKLA), **draw** (the line draws the moth, it flaps and rises into the lockup), **zoom** (starts inside the wing contours and pulls back). Vary scenario × theme between videos so openings differ; the owner likes e.g. crimson background with the light moth. Regenerate the template with `python3 scripts/gen_intro.py`. No colour-stripe intros (rejected: looks like a flag). Animated templates must use CSS keyframes only so they can be scrubbed frame by frame.

New template: an HTML file in `templates/` linking `../brand.css`, using `.canvas`, `.frame/.top/.bottom`, `.display`, `.label`, `.pill`, `.sig`, plus `<script src="fill.js">`.

## Pillars → theme

Користь (tools, frameworks) → `leaf` · Треди й колаби → `violet` · Гострі думки (hot takes, fails) → `crimson`.

## Workflow

1. Pick the pillar → theme and the template.
2. Write short lowercase-agnostic copy (it renders uppercase); confirm partner names, dates and numbers with the user.
3. Render, look at the PNG, check: only three colours, no forbidden pair, text not clipped, avatar zone empty on banners, ≤1 highlight.
4. Deliver the file plus the exact command used.
