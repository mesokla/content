# Animated explainer: "Crypto bet $200M on the midterms" — 1080x1350, CSS keyframes on one absolute timeline (scrubbable).
B='/home/user/content/.claude/skills/mesokla-brand'
T=73.0
L,V,C='#A6B8A0','#8B729C','#E20942'
EASE='cubic-bezier(.2,.8,.2,1)'
css=[];n=[0]
def kf(frames):
    """frames: [(t, 'css')] absolute seconds. Returns an inline style animation."""
    n[0]+=1; name=f'a{n[0]}'
    body=''.join(f'{max(0,min(100,t/T*100)):.4f}%{{{c};animation-timing-function:{EASE}}}' for t,c in frames)
    css.append(f'@keyframes {name}{{{body}}}')
    return f'animation:{name} {T}s linear both;'
def appear(t,d=.55,fr='opacity:0;transform:translateY(50px)',to='opacity:1;transform:none'):
    return kf([(0,fr),(t,fr),(t+d,to)])
def pop(t,d=.45):
    return kf([(0,'opacity:0;transform:scale(.6) rotate(-6deg)'),(t,'opacity:0;transform:scale(.6) rotate(-6deg)'),(t+d*.6,'opacity:1;transform:scale(1.08) rotate(-3deg)'),(t+d,'opacity:1;transform:scale(1) rotate(-3deg)')])
FORE="M196 196C160 120 100 70 40 66C22 100 30 170 76 204C116 226 168 214 196 206Z"
HIND="M196 214C164 222 112 244 96 292C98 330 142 342 170 306C184 286 192 252 196 230Z"
MIR='transform="translate(400 0) scale(-1 1)"'
def moth(ln,ln2,o2=1,w=6):
    wing=(f'<path d="{FORE}"/><path d="{HIND}"/><g transform="translate(196 206) scale(.7) translate(-196 -206)" stroke="{ln2}" stroke-opacity="{o2}" stroke-width="{w*.62/.7:.2f}"><path d="{FORE}"/><path d="{HIND}"/></g><circle cx="92" cy="136" r="9" fill="{ln}" stroke="none"/>')
    ant='<path d="M195 150C184 112 166 92 140 80"/><circle cx="140" cy="80" r="6"/>'
    return (f'<svg class="moth" viewBox="20 40 360 320" fill="none" stroke="{ln}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">'
            f'<g class="wl">{wing}</g><g class="wr"><g {MIR}>{wing}</g></g>{ant}<g {MIR}>{ant}</g><ellipse cx="200" cy="222" rx="9" ry="56"/></svg>')
def sigmoth(col): return f'<img class="sm" src="{B}/moth/moth-front-{col}.svg" alt="">'
scenes=[]
def scene(t0,bg,inner,fg,sigcol,direction='l'):
    fr={'l':'inset(0 100% 0 0)','r':'inset(0 0 0 100%)','t':'inset(0 0 100% 0)'}[direction]
    st=kf([(0,f'clip-path:{fr}'),(t0,f'clip-path:{fr}'),(t0+.6,'clip-path:inset(0 0 0 0)')]) if t0>0 else ''
    scenes.append(f'<section class="sc" style="background:{bg};color:{fg};{st}">{inner}<div class="sig" style="color:{fg}">{sigmoth(sigcol)}MESOKLA</div><div class="hd" style="color:{fg}">@mesokla</div></section>')
K=lambda txt,t,col=None,extra='':f'<div class="k" style="{("color:"+col+";") if col else ""}{appear(t,.5,"opacity:0","opacity:1")}{extra}">{txt}</div>'
def H(txt,t,size=120,extra='',d=.55): return f'<div class="h" style="font-size:{size}px;{appear(t,d)}{extra}">{txt}</div>'
def mark(txt,bg,fg): return f'<span class="mk" style="background:{bg};color:{fg}">{txt}</span>'

# S0 HOOK 0-3.5 crimson
mf=kf([(0,'transform:translate(-300px,1250px) rotate(25deg) scale(.7)'),(2.2,'transform:translate(1200px,-300px) rotate(-10deg) scale(1)')])
scene(0,C,f'''<div class="fr" style="justify-content:center">
{H('crypto spent',.2,110)}{H('$200M',.7,250,'line-height:.85;')}{H('…and '+mark('lost.',V,L),1.9,140)}</div>
<div class="flyer" style="{mf}">{moth(L,L,.55)}</div>''',L,'leaf')
# S1 WHAT HAPPENED 3.5-9.5 leaf
def row(label,t):
    fill=kf([(0,'width:0'),(t,'width:0'),(t+1.0,'width:100%')])
    txt=appear(t+.7,.4,'opacity:0','opacity:1')
    return f'<div class="row" style="{appear(t-.3,.4)}"><div class="rl">{label}</div><div class="bar"><div class="fill" style="{fill}"></div><div class="bt" style="{txt}">democrats</div></div></div>'
scene(3.5,L,f'''<div class="fr">{K('nov 3–4 · us midterms',4.1,V)}
<div style="margin-top:auto;margin-bottom:auto">{H('who won<br>congress?',4.3,124)}<div style="height:60px"></div>{row('house',5.4)}{row('senate',6.8)}</div></div>''',C,'crimson')
# S2 MONEY 9.5-17 violet
nums=''.join(f'<span>{v}</span>' for v in range(0,201,10))
cnt=f"animation:odo {T}s linear both;"
css.append('@keyframes odo{0%{transform:translateY(0)}'+f'{10.4/T*100:.4f}%{{transform:translateY(0);animation-timing-function:steps(20,end)}}{12.6/T*100:.4f}%{{transform:translateY(-20em)}}100%{{transform:translateY(-20em)}}'+'}')
spin=kf([(0,'transform:rotate(0)'),(T,'transform:rotate(240deg)')])
scene(9.5,V,f'''<img class="deco" src="{B}/elements/spot-crimson.svg" style="right:-330px;top:640px;width:700px;{spin}">
<div class="fr">{K('the bet',10.1)}
<div style="margin:auto 0">{H('crypto super pacs<br>spent up to',10.2,70)}
<div class="h count" style="font-size:250px;line-height:.9;{appear(10.3,.4)}">$<span class="odo"><span class="strip" style="{cnt}">{nums}</span></span>M</div>
<div class="sub" style="{appear(12.8,.5)}">≈ $176–200M, mostly via Fairshake</div>
<div class="stamp" style="{pop(14.3)}">key races: lost</div></div></div>''',L,'leaf','r')
# S3 BROWN 17-23.5 crimson
reveal=kf([(0,'clip-path:inset(0 100% 0 0)'),(19.6,'clip-path:inset(0 100% 0 0)'),(21.2,'clip-path:inset(0 0 0 0)')])
scene(17,C,f'''<img class="deco" src="{B}/elements/spot-violet.svg" style="right:60px;top:760px;width:300px;{appear(19.2,.5,'opacity:0;transform:scale(.6)','opacity:1;transform:none')}">
<svg class="deco" viewBox="0 0 1080 1350" style="left:0;top:0;width:1080px;height:1350px;{reveal}"><path d="M60 1180C300 1150 520 1000 700 960S960 820 1060 760" fill="none" stroke="{L}" stroke-width="10" stroke-linecap="round" stroke-dasharray="0 26"/></svg>
<div class="fr">{K('ohio',17.6)}
<div style="margin-top:110px">{H('sherrod<br>brown',17.8,150)}{H(mark('is back.',V,L),18.6,150)}
<div class="sub" style="max-width:820px;{appear(19.4,.5)}">Long-time crypto sceptic, back in the Senate despite tens of millions spent against him.</div></div></div>''',L,'leaf','l')
# S4 WARREN 23.5-33 leaf
items=['exchanges','stablecoins','aml / kyc','crypto business of officials']
lis=''.join(f'<li style="{appear(27.2+i*.8,.45,"opacity:0;transform:translateX(-60px)","opacity:1;transform:none")}"><b>0{i+1}</b>{x}</li>' for i,x in enumerate(items))
scene(23.5,L,f'''<div class="fr">{K('what changes',24.1,V)}
<div style="margin:auto 0">{H('elizabeth<br>warren',24.3,128)}
<div class="sub" style="color:{V};{appear(25.2,.5)}">→ expected chair of the Senate Banking Committee</div>
<div class="k" style="margin-top:70px;color:{V};{appear(26.6,.4,'opacity:0','opacity:1')}">more pressure on:</div>
<ol class="list">{lis}</ol></div></div>''',C,'crimson','r')
# S5 CLARITY 33-40 violet
prog=kf([(0,'width:0'),(34.6,'width:0'),(36.4,'width:62%'),(36.7,'width:68%'),(36.9,'width:64%'),(37.1,'width:67%'),(37.3,'width:66%')])
land=kf([(0,'transform:translate(1100px,-500px) rotate(20deg)'),(35.6,'transform:translate(1100px,-500px) rotate(20deg)'),(37.4,'transform:translate(0,0) rotate(0)')])
fold=kf([(0,'transform:scaleX(1)'),(37.6,'transform:scaleX(1)'),(38.2,'transform:scaleX(.28)')])
scene(33,V,f'''<div class="fr">{K('the bill',33.6)}
<div style="margin:auto 0">{H('clarity act',33.8,140)}
<div class="pb" style="{appear(34.3,.4)}"><div class="pf" style="{prog}"></div></div>
<div class="lander" style="{land}"><div class="foldw" style="{fold}">{moth(L,L,.55)}</div></div>
<div class="sub" style="{appear(37.6,.5)}">Likely delayed, or heavily rewritten.</div></div></div>''',L,'leaf','l')
# S6 MARKET 40-49 leaf
draw=kf([(0,'stroke-dashoffset:1'),(41.4,'stroke-dashoffset:1'),(45.0,'stroke-dashoffset:0')])
def lab(txt,x,y,t,anchor='left'):
    return f'<div class="cl" style="left:{x}px;top:{y}px;{appear(t,.4,"opacity:0;transform:scale(.8)","opacity:1;transform:none")}">{txt}</div>'
scene(40,L,f'''<div class="fr">{K('the market',40.6,V)}
<div style="margin-top:70px">{H('mixed,<br>then '+mark('red.',C,L),40.8,124)}</div>
<div class="chart" style="{appear(41.2,.4,'opacity:0','opacity:1')}">
<svg viewBox="0 0 920 520" width="920" height="520"><path pathLength="1" d="M0 250L150 230L270 340L380 300L520 160L620 200L740 330L920 470" fill="none" stroke="{C}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" style="stroke-dasharray:1 1;{draw}"/>
<g fill="{V}"><circle cx="270" cy="340" r="14" style="{appear(42.3,.3,'opacity:0','opacity:1')}"/><circle cx="520" cy="160" r="14" style="{appear(43.3,.3,'opacity:0','opacity:1')}"/><circle cx="920" cy="470" r="14" style="{appear(45.0,.3,'opacity:0','opacity:1')}"/></g></svg>
{lab('dip during the count',170,370,42.4)}{lab('wed: btc back above $78–80k',390,90,43.4)}{lab('then a heavier sell-off',560,410,45.1)}
<div class="ill">illustrative</div></div>
<div class="tag" style="{pop(46.3)}">wlfi · trump fell harder</div></div>''',C,'crimson','r')
# S7 TAKES 49-59 stack of three bands
takes=[(L,C,'“it’s a reset, not the end.”','longer road, more consumer protection',50.0),
       (V,L,'“gridlock protects us from extremes.”','trump in the white house, democratic congress',52.8),
       (C,L,'“warren’s anti-crypto army is coming.”','+ scrutiny of ai infra as miners pivot to ai data centres',55.6)]
bands=''.join(f'<div class="band" style="background:{bg};color:{fg};{kf([(0,"transform:translateX(-100%)"),(t,"transform:translateX(-100%)"),(t+.6,"transform:none")])}"><div class="bq">{q}</div><div class="bs">{s}</div></div>' for bg,fg,q,s,t in takes)
scene(49,V,f'''<div class="bands">{bands}</div><div class="k" style="position:absolute;left:80px;top:70px;color:{C};z-index:3;{appear(49.6,.4,'opacity:0','opacity:1')}">what x is saying</div>''',L,'leaf','t')
# S8 TAKE 59-68 violet
pts=['compliance becomes part of the pitch','don’t promise “clarity soon”','political tokens = political risk']
pl=''.join(f'<li style="{appear(62.6+i*1.1,.45,"opacity:0;transform:translateX(-60px)","opacity:1;transform:none")}">{x}</li>' for i,x in enumerate(pts))
scene(59,V,f'''<div class="fr">{K('what it means for web3',59.6)}
<div style="margin:auto 0">{H('regulation<br>isn’t dead.',59.8,124)}{H('it’s '+mark('slower',C,L)+'<br>and stricter.',60.9,124)}
<ul class="list take">{pl}</ul></div></div>''',L,'leaf','l')
# S9 OUTRO 68-73 crimson
fly=kf([(0,'transform:translate(-500px,900px) rotate(30deg) scale(.6)'),(68.3,'transform:translate(-500px,900px) rotate(30deg) scale(.6)'),(70.2,'transform:translate(0,0) rotate(0) scale(1)')])
scene(68,C,f'''<div class="outro"><div class="olm" style="{fly}">{moth(L,L,.55,7)}</div>
<div class="h" style="font-size:150px;{appear(70.0,.5)}">mesokla</div>
<div class="k" style="margin-top:40px;{appear(70.8,.5,'opacity:0','opacity:1')}">what’s your take? reply ↓</div></div>''',L,'leaf','r')

html=f'''<!doctype html><html><head><meta charset="utf-8"><title>Midterms explainer</title>
<link rel="stylesheet" href="{B}/fonts/fonts.css"><style>
@property --n{{syntax:'<integer>';inherits:false;initial-value:0}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:{C}}}
.sc{{position:absolute;inset:0;overflow:hidden;font-family:Manrope,sans-serif}}
.fr{{position:absolute;inset:80px 80px 150px;display:flex;flex-direction:column}}
.h{{font-family:Montserrat;font-weight:900;text-transform:uppercase;line-height:.95;letter-spacing:-.01em}}
.k{{font-family:Manrope;font-weight:800;font-size:30px;letter-spacing:.18em;text-transform:uppercase}}
.mk{{padding:0 .12em;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
.sub{{margin-top:34px;font-size:40px;font-weight:700;line-height:1.3}}
.sig{{position:absolute;left:80px;bottom:62px;display:flex;align-items:center;gap:14px;font-family:Montserrat;font-weight:900;font-size:34px;letter-spacing:.04em}}
.sm{{height:50px}} .hd{{position:absolute;right:80px;bottom:70px;font-weight:700;font-size:28px}}
.flyer{{position:absolute;left:0;top:0;width:360px}}
.moth{{width:100%;height:auto;display:block;overflow:visible}}
.moth .wl,.moth .wr{{transform-box:view-box;transform-origin:200px 210px;animation:flap .3s ease-in-out infinite}}
@keyframes flap{{50%{{transform:scaleX(.25)}}}}
.row{{display:grid;grid-template-columns:260px 1fr;align-items:center;gap:24px;margin-top:30px}}
.rl{{font-family:Montserrat;font-weight:900;font-size:54px;text-transform:uppercase}}
.bar{{position:relative;height:110px;border:5px solid {V}}}
.fill{{position:absolute;left:0;top:0;bottom:0;background:{V}}}
.bt{{position:absolute;left:28px;top:50%;transform:translateY(-50%);font-family:Montserrat;font-weight:900;font-size:50px;text-transform:uppercase;color:{L}}}
.odo{{display:inline-block;height:1em;line-height:1em;overflow:hidden;vertical-align:top}} .strip{{display:flex;flex-direction:column}} .strip span{{height:1em;line-height:1em;text-align:right}}
.stamp{{display:inline-block;margin-top:50px;background:{C};color:{L};font-family:Montserrat;font-weight:900;font-size:76px;text-transform:uppercase;padding:14px 30px}}
.deco{{position:absolute}}
.list{{list-style:none;margin-top:24px}}
.list li{{font-size:46px;font-weight:800;padding:20px 0;border-top:4px solid currentColor;display:flex;gap:30px;align-items:baseline}}
.list li b{{font-family:Montserrat;font-weight:900;color:{V};font-size:40px}}
.take li{{font-size:40px;border-color:{L}}}
.pb{{margin-top:70px;height:70px;border:6px solid {L};position:relative}}
.pf{{position:absolute;left:0;top:0;bottom:0;background:{C}}}
.lander{{position:absolute;left:520px;top:500px;width:300px}}
.foldw{{transform-origin:center}}
.chart{{position:relative;margin-top:60px;width:920px;height:520px}}
.cl{{position:absolute;background:{V};color:{L};font-weight:800;font-size:28px;padding:8px 16px;white-space:nowrap;text-transform:uppercase;letter-spacing:.06em}}
.ill{{position:absolute;right:0;top:-34px;font-size:20px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{V}}}
.tag{{display:inline-block;align-self:flex-start;margin-top:20px;background:{C};color:{L};font-family:Montserrat;font-weight:900;font-size:56px;text-transform:uppercase;padding:12px 26px}}
.bands{{position:absolute;inset:0;display:grid;grid-template-rows:1fr 1fr 1fr}}
.band{{padding:150px 80px 40px;display:flex;flex-direction:column;justify-content:center;gap:16px}}
.band:nth-child(2),.band:nth-child(3){{padding-top:40px}}
.band:nth-child(3){{padding-bottom:140px}}
.bq{{font-family:Montserrat;font-weight:900;font-size:66px;line-height:1;text-transform:uppercase}}
.bs{{font-size:30px;font-weight:700}}
.outro{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding-bottom:80px}}
.olm{{width:340px;margin-bottom:30px}}
{''.join(css)}
</style></head><body>{''.join(scenes)}</body></html>'''
open('midterms.html','w').write(html)
print(len(html))
