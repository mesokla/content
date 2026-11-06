// Scrub a CSS-animated template into an MP4.
// Usage: node scripts/video.mjs <template.html[?params]> <out.mp4> [seconds=4] [w=1600] [h=900] [fps=30]
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright'); // needs playwright: npm i -D playwright (or a global install)
import { execFileSync } from 'node:child_process';
import fs from 'node:fs'; import os from 'node:os'; import path from 'node:path';
const [,, src, out, secs = 4, w = 1600, h = 900, fps = 30] = process.argv;
const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'mesy-'));
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: +w, height: +h } });
await p.goto('file://' + path.resolve(src));
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
const n = Math.round(secs * fps);
for (let i = 0; i < n; i++) {
  const t = (i / fps) * 1000;
  await p.evaluate(t => document.getAnimations().forEach(a => { a.pause(); a.currentTime = t; }), t);
  await p.screenshot({ path: path.join(dir, String(i).padStart(5, '0') + '.png') });
}
await b.close();
execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(fps), '-i', path.join(dir, '%05d.png'),
  '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-movflags', '+faststart', out]);
fs.rmSync(dir, { recursive: true }); console.log('wrote', out);
