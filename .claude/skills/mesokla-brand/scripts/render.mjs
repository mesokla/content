// Render a template to PNG with custom text.
// Usage: node scripts/render.mjs <template> <out.png> [key=value ...]
//   template: banner | quote | thread | do-dont | list | collab | stack  (or a path to .html)
//   keys: theme=leaf|violet|crimson (banner also: stripes), text/title/... ("|" = new line / new item, *word* = highlight)
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright'); // needs playwright: npm i -D playwright (or a global install)
import path from 'node:path'; import { fileURLToPath } from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SIZES = { banner: [1500, 500], stack: [1080, 1350] };
const [,, tpl, out, ...kv] = process.argv;
if (!tpl || !out) { console.error('usage: node scripts/render.mjs <template> <out.png> [key=value ...]'); process.exit(1); }
const file = /\.(html|svg)$/.test(tpl) ? path.resolve(tpl) : path.join(root, 'templates', tpl + '.html');
const q = new URLSearchParams(kv.map(s => { const i = s.indexOf('='); return [s.slice(0, i), s.slice(i + 1)]; }));
const [w, h] = (q.get('size') || '').split('x').map(Number).filter(Boolean).length ? q.get('size').split('x').map(Number) : (SIZES[tpl] || [1600, 900]);
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: +(q.get('scale') || 1) });
await p.goto('file://' + file + (q.toString() ? '?' + q : ''));
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(250);
await p.screenshot({ path: out, omitBackground: file.endsWith('.svg') });
await b.close(); console.log('wrote', out, `${w}x${h}`);
