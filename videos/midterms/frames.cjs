// node frames.cjs page.html out_prefix t1 t2 ... — screenshots at given seconds
const {chromium}=require('playwright');const path=require('path');
(async()=>{const [,,src,pre,...ts]=process.argv;const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+path.resolve(src));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
for(const t of ts){await p.evaluate(t=>document.getAnimations().forEach(a=>{a.pause();a.currentTime=t*1000}),+t);await p.screenshot({path:`${pre}-${t}.png`});}
await b.close()})();
