// Usage: node scripts/shot.mjs <file.html|svg> <out.png> [width] [height] [scale]
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright'); // needs playwright: npm i -D playwright (or a global install)
import path from 'node:path';
const [,, src, out, w = 1600, h = 900, s = 1] = process.argv;
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: +s });
await p.goto('file://' + path.resolve(src));
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(250);
await p.screenshot({ path: out, omitBackground: src.endsWith('.svg') });
await b.close();
