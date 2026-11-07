# Horizontal (1920x1080) midterms explainer synced to the ElevenLabs voiceover (vo.mp3).
import re
B='/home/user/content/.claude/skills/mesokla-brand'
A='/home/user/content/videos/midterms/assets/'
O=3.0                      # voice starts after the slow moth intro
VO_END=75.08+0.3*8
T=O+VO_END+3.4
L,V,C='#A6B8A0','#8B729C','#E20942'
EASE='cubic-bezier(.2,.8,.2,1)'
# sentences with start/end in the audio (from pause detection, mapped to punctuation)
TXT=['Crypto spent more than a hundred and seventy million dollars on the US midterms this week,', "and it didn't get what it paid for.", 'Democrats won both the House and the Senate.', "Most of the industry's money went through Fairshake and a few other super PACs,", 'and the races they cared about most went the other way.', 'Ohio hurt the most.', 'Sherrod Brown has been sceptical of crypto for years,', 'and tens of millions were spent to keep him out.', "He's back in the Senate anyway.", 'The bigger change is Elizabeth Warren.', "She's expected to chair the Senate Banking Committee,", 'which means closer attention to exchanges, stablecoins, A-M-L and K-Y-C rules, and the crypto deals of public officials.', 'Bills like the CLARITY Act will probably stall, or come back looking very different.', "The market didn't know what to do with it.", 'Bitcoin dipped during the count, climbed back above seventy-eight thousand on Wednesday, and then sold off harder.', 'Trump-linked tokens took the worst of it.', 'On X, people are split.', 'A lot of them call it a reset.', 'Some think a divided government at least keeps things from swinging too far, and others expect Warren to come after the industry hard.', "The general read across the industry is that regulation isn't going away.", "It's just going to take longer and come with stricter rules, so projects will have to treat compliance as part of the pitch, and tokens tied to politicians now carry political risk."]
import json as _j
AL=[(re.sub(r"\(\d\)","",w['w']),w['s'],w['e']) for w in _j.load(open('align.json'))]
def _norm(t):
    t=t.replace('A-M-L','A M L').replace('K-Y-C','K Y C').replace('seventy-eight','seventy eight').replace('Trump-linked','Trump linked').replace('Long-time','long time')
    t=re.sub(r"[^A-Za-z' ]"," ",t).lower(); return t.split()
S=[];WT=[];k=0
for txt in TXT:
    toks=_norm(txt); seg=AL[k:k+len(toks)]; k+=len(toks)
    WT.append([(w,O+st_) for (w,st_,en_) in seg]); S.append((txt,seg[0][1],seg[-1][2]))
assert k==len(AL),(k,len(AL))
BOUND=[2,3,5,9,12,13,16,19]      # first sentence of each new scene
GAP=0.3
def shift(i): return GAP*sum(1 for b in BOUND if b<=i)
WT=[[(w,t+shift(i)) for w,t in row] for i,row in enumerate(WT)]
S=[(txt,a+shift(i),b+shift(i)) for i,(txt,a,b) in enumerate(S)]
CUTS=[ (S[b-1][2]-shift(b-1)+S[b][1]-shift(b))/2 for b in BOUND ]   # cut points in the original audio
def at(i,word,nth=1):
    k=0
    word=word.lower()
    exact=any(t==word for t,_ in WT[i])
    for t,s in WT[i]:
        if (t==word) if exact else t.startswith(word):
            k+=1
            if k==nth: return s
    raise KeyError((i,word))
def st(i): return O+S[i][1]
css=[];n=[0]
EV={'wipe':[],'hl':[],'pop':[],'tick':[],'reveal':[],'card':[]}
def kf(frames):
    if frames[-1][0]<T: frames=list(frames)+[(T,frames[-1][1])]
    n[0]+=1; name=f'a{n[0]}'
    body=''.join(f'{max(0,min(100,t/T*100)):.4f}%{{{c};animation-timing-function:{EASE}}}' for t,c in frames)
    css.append(f'@keyframes {name}{{{body}}}'); return f'animation:{name} {T}s linear both;'
def appear(t,d=.5,fr='opacity:0;transform:translateY(40px)',to='opacity:1;transform:none'):
    return kf([(0,fr),(t,fr),(t+d,to)])
fade=lambda t,d=.4: appear(t,d,'opacity:0','opacity:1')
def pop(t,d=.45,r=-3):
    EV['pop'].append(round(t,3))
    a=f'opacity:0;transform:scale(.6) rotate({r*2}deg)'; return kf([(0,a),(t,a),(t+d*.6,f'opacity:1;transform:scale(1.08) rotate({r}deg)'),(t+d,f'opacity:1;transform:scale(1) rotate({r}deg)')])
def hl(txt,t,bg,fg,base):
    """word that gets a marker swept under it when it is spoken"""
    EV['hl'].append(round(t,3))
    return f'<span class="hl" style="--b:{bg};color:{base};{kf([(0,"background-size:0% 100%;color:"+base),(t,"background-size:0% 100%;color:"+base),(t+.35,"background-size:100% 100%;color:"+fg)])}">{txt}</span>'
def words(text,t0,t1,extra=''):
    """reveal words of a headline one by one between t0 and t1"""
    ws=text.split(' '); out=[]
    for i,w in enumerate(ws):
        t=t0+(t1-t0)*i/max(1,len(ws)-1) if len(ws)>1 else t0
        out.append(f'<span class="w" style="{appear(t,.35,"opacity:0;transform:translateY(30px)","opacity:1;transform:none")}">{w}</span>')
    return ' '.join(out)
def card(src,cap,t,bc,w,rot=-2):
    EV['card'].append(round(t,3))
    return (f'<div class="card" style="--bc:{bc};width:{w}px;justify-self:end;{appear(t,.5,f"opacity:0;transform:translateY(60px) rotate({rot*3}deg) scale(.92)",f"opacity:1;transform:rotate({rot}deg)")}">'
            f'<img src="{src}" style="width:100%;display:block"><div class="cap">{cap}</div></div>')
FORE="M196 196C160 120 100 70 40 66C22 100 30 170 76 204C116 226 168 214 196 206Z"
HIND="M196 214C164 222 112 244 96 292C98 330 142 342 170 306C184 286 192 252 196 230Z"
MIR='transform="translate(400 0) scale(-1 1)"'
def moth(ln,ln2,o2=1,w=6,cls='flap'):
    wing=(f'<path d="{FORE}"/><path d="{HIND}"/><g transform="translate(196 206) scale(.7) translate(-196 -206)" stroke="{ln2}" stroke-opacity="{o2}" stroke-width="{w*.62/.7:.2f}"><path d="{FORE}"/><path d="{HIND}"/></g><circle cx="92" cy="136" r="9" fill="{ln}" stroke="none"/>')
    ant='<path d="M195 150C184 112 166 92 140 80"/><circle cx="140" cy="80" r="6"/>'
    return (f'<svg class="moth {cls}" viewBox="20 40 360 320" fill="none" stroke="{ln}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">'
            f'<g class="wl">{wing}</g><g class="wr"><g {MIR}>{wing}</g></g>{ant}<g {MIR}>{ant}</g><ellipse cx="200" cy="222" rx="9" ry="56"/></svg>')
scenes=[]
def scene(t0,bg,inner,fg,sigcol,d='l'):
    if t0>0: EV['wipe'].append(round(t0,3))
    fr={'l':'inset(0 100% 0 0)','r':'inset(0 0 0 100%)','t':'inset(0 0 100% 0)','b':'inset(100% 0 0 0)'}[d]
    stl=kf([(0,f'clip-path:{fr};visibility:hidden'),(t0-.02,f'clip-path:{fr};visibility:hidden'),(t0,f'clip-path:{fr};visibility:visible'),(t0+.6,'clip-path:inset(0 0 0 0);visibility:visible')]) if t0>0 else ''
    scenes.append(f'<section class="sc" style="background:{bg};color:{fg};{stl}">{inner}<div class="sig" style="color:{fg}"><img class="sm" src="{A}moth-front-{sigcol}-bold.svg" alt="">MESOKLA</div></section>')
K=lambda txt,t,col=None,pos='':f'<div class="k" style="{("color:"+col+";") if col else ""}{fade(t)}{pos}">{txt}</div>'

# ---- A · intro + hook (crimson) ----
path="M -260 1240 C 260 1120 380 640 760 600 S 1300 760 1500 360"
fly=kf([(0,'offset-distance:0%'),(3.4,'offset-distance:100%')])
tilt=kf([(0,'transform:rotate(35deg) scale(.55)'),(1.6,'transform:rotate(8deg) scale(.8)'),(3.4,'transform:rotate(-6deg) scale(1)'),(T,'transform:rotate(-6deg) scale(1)')])
dots=''.join(f'<i class="dot" style="offset-path:path(\'{path}\');offset-distance:{p}%;{appear(3.4*p/100,.2,"opacity:0","opacity:.9")}"></i>' for p in range(4,96,4))
trail_out=kf([(0,'opacity:1'),(4.2,'opacity:1'),(5.0,'opacity:0')])
scene(0,C,f'''<div class="trail" style="{trail_out}">{dots}</div>
<div class="flyer" style="offset-path:path('{path}');offset-rotate:0deg;{fly}"><div style="{tilt}">{moth(L,L,.55,6,'slowflap')}</div></div>
<div class="fr" style="justify-content:center;max-width:1300px">
<div class="h" style="font-size:96px;margin-bottom:70px">{words('crypto spent',at(0,'crypto'),at(0,'spent'))}</div>
<div class="h" style="font-size:260px;line-height:.9;{appear(at(0,'hundred'),.5,'opacity:0;transform:scale(.8)','opacity:1;transform:none')}">{hl('$170M+',at(0,'million'),V,L,L)}</div>
<div class="sub" style="{fade(at(0,'midterms'))}">on the US midterms this week</div>
<div class="h" style="font-size:96px;margin-top:40px">{words('and',at(1,'and'),at(1,'and'))} {hl(words("didn’t get",at(1,"didn't"),at(1,'get')),at(1,'get'),V,L,L)} {words('what it paid for.',at(1,'what'),at(1,'for'))}</div></div>''',L,'leaf')
# ---- B · who won (leaf) ----
def row(label,t):
    return (f'<div class="row" style="{appear(t-.5,.4)}"><div class="rl">{label}</div><div class="bar"><div class="fill" style="{kf([(0,"width:0"),(t,"width:0"),(t+.9,"width:100%")])}"></div>'
            f'<div class="bt" style="{fade(t+.6)}">democrats</div></div></div>')
tB=st(2)-.3
scene(tB,L,f'''<div class="fr">{K('this week · us midterms',tB+.4,V)}
<div class="two"><div class="h" style="font-size:130px">{words('who won congress?',tB+.3,at(2,'won'))}</div>
<div>{row('house',at(2,'house'))}{row('senate',at(2,'senate'))}</div></div></div>''',C,'crimson','l')
# ---- C · money (violet) + Cointelegraph headline ----
tC=st(3)-.3
nums=''.join(f'<span>{v}</span>' for v in range(0,171,10))
a0,a1=at(3,'most'),at(3,'fairshake')
EV['tick']=[round(a0+(a1-a0)*k/17,3) for k in range(1,18)]
css.append('@keyframes odo{0%{transform:translateY(0)}'+f'{a0/T*100:.4f}%{{transform:translateY(0);animation-timing-function:steps(17,end)}}{a1/T*100:.4f}%{{transform:translateY(-17em)}}100%{{transform:translateY(-17em)}}'+'}')
scene(tC,V,f"""<div class="fr">{K('the bet',tC+.4)}
<div class="two" style="grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr)"><div>
<div class="h" style="font-size:168px;line-height:.9;white-space:nowrap;{appear(a0-.2,.4)}">$<span class="odo"><span class="strip" style="animation:odo {T}s linear both">{nums}</span></span>M+</div>
<div class="h" style="font-size:54px;margin-top:20px;{fade(a1-.3)}">through {hl('fairshake',a1,C,L,L)} + super pacs</div>
<div class="stamp" style="{pop(at(4,'races'))}">key races went the other way</div></div>
{card(A+'ct-headline.png','source: Cointelegraph · Nov 4',at(3,'industry'),C,840,-2)}</div></div>""",L,'leaf','r')
# ---- D · Ohio (crimson) + Brown photo ----
tD=st(5)-.3
scene(tD,C,f"""<div class="fr"><div class="two" style="grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr)"><div>
<div class="h" style="font-size:84px">{words('ohio hurt the most.',at(5,'ohio'),at(5,'most'))}</div>
<div class="h" style="font-size:150px;margin-top:36px">{words('sherrod brown',at(6,'sherrod'),at(6,'brown'))}</div>
<div class="sub" style="{fade(at(6,'sceptical'))}">crypto sceptic for years · tens of millions spent against him</div>
<div class="h" style="font-size:96px;margin-top:36px;{fade(at(8,"he's")-.1)}">{hl('back in the senate.',at(8,'back'),V,L,L)}</div></div>
{card(A+'brown.webp','Sherrod Brown · D-Ohio',at(6,'sherrod')-.2,V,700,2)}</div></div>""",L,'leaf','l')
# ---- E · Warren (leaf) + photo ----
tE=st(9)-.3
items=[('exchanges','exchanges'),('stablecoins','stablecoins'),('aml / kyc','m'),('officials’ crypto deals','deals')]
lis=''.join(f'<li style="{appear(at(11,w),.4,"opacity:0;transform:translateX(-60px)","opacity:1;transform:none")}"><b>0{i+1}</b>{x}</li>' for i,(x,w) in enumerate(items))
scene(tE,L,f"""<div class="fr">{K('the bigger change',tE+.4,V)}
<div class="three">{card(A+'warren.webp','Elizabeth Warren',at(9,'elizabeth')-.3,V,500,-2)}
<div><div class="h" style="font-size:96px">{words('elizabeth warren',at(9,'elizabeth'),at(9,'warren'))}</div>
<div class="h" style="font-size:46px;margin-top:30px;{fade(at(10,'expected')-.2)}">expected to {hl('chair senate banking',at(10,'chair'),V,L,C)}</div></div>
<div><div class="k" style="color:{V};{fade(at(11,'closer'))}">closer attention to</div><ol class="list sm2">{lis}</ol></div></div></div>""",C,'crimson','r')
# ---- F · CLARITY (violet) ----
tF=st(12)-.3
s0,s1=at(12,'bills'),at(12,'stall')
prog=kf([(0,'width:0'),(s0,'width:0'),(s1,'width:62%'),(s1+.25,'width:68%'),(s1+.45,'width:64%'),(s1+.65,'width:67%'),(s1+.85,'width:66%')])
land=kf([(0,'transform:translate(900px,-500px) rotate(20deg)'),(s0+.4,'transform:translate(900px,-500px) rotate(20deg)'),(s1+.6,'transform:none')])
fold=kf([(0,'transform:scaleX(1)'),(s1+.7,'transform:scaleX(1)'),(s1+1.2,'transform:scaleX(.28)')])
scene(tF,V,f'''<div class="fr">{K('the bills',tF+.4)}
<div style="margin:auto 0"><div class="h" style="font-size:180px">{words('clarity act',at(12,'clarity'),at(12,'act'))}</div>
<div class="pb" style="{appear(s0,.4)}"><div class="pf" style="{prog}"></div></div>
<div class="lander" style="{land}"><div style="transform-origin:center;{fold}">{moth(L,L,.55)}</div></div>
<div class="h" style="font-size:64px;margin-top:50px">{hl(words('will probably stall',at(12,'will'),s1),s1,C,L,L)} <span style="{fade(at(12,'come'))}">· or come back very different</span></div></div></div>''',L,'leaf','l')
# ---- G · market (leaf) + real CoinGecko chart ----
tG=st(13)-.3
c0,c1=at(14,'bitcoin'),at(14,'harder')+.3
wipe_chart=kf([(0,'clip-path:inset(0 100% 0 0)'),(c0,'clip-path:inset(0 100% 0 0)'),(c1,'clip-path:inset(0 0 0 0)')])
EV['card'].append(round(c0-.4,3))
sc=1040/1952
def lab(txt,x,y,t): return f'<div class="cl" style="left:{x*sc:.0f}px;top:{y*sc:.0f}px;{appear(t,.35,"opacity:0;transform:scale(.8)","opacity:1;transform:none")}">{txt}</div>'
def ring(x,y,t): return f'<div class="ring" style="left:{x*sc-22:.0f}px;top:{y*sc-22:.0f}px;{appear(t,.3,"opacity:0;transform:scale(.4)","opacity:1;transform:none")}"></div>'
scene(tG,L,f"""<div class="fr">{K('the market',tG+.4,V)}
<div class="two" style="grid-template-columns:560px 1fr;gap:60px">
<div><div class="h" style="font-size:88px">{words("didn’t know what to do with it.",at(13,'market'),at(13,'it'))}</div>
<div class="tag" style="{pop(at(15,'trump'))}">trump-linked tokens: hit hardest</div></div>
<div class="card" style="--bc:{V};width:1060px;{appear(c0-.4,.45,'opacity:0;transform:translateY(40px) rotate(0deg)','opacity:1;transform:rotate(-1deg)')}">
<div style="position:relative;width:1040px;height:{1070*sc:.0f}px"><img src="{A}btc-7d.png" style="width:1040px;display:block;{wipe_chart}">
{ring(1165,805,at(14,'count'))}{ring(1372,195,at(14,'seventy'))}{ring(1545,840,at(14,'sold'))}
{lab('dip during the count',820,860,at(14,'count'))}{lab('wed: back above $78k',900,90,at(14,'seventy'))}{lab('then sold off harder',1180,930,at(14,'sold'))}</div>
<div class="cap">source: CoinGecko · BTC 7D</div></div></div></div>""",C,'crimson','r')
# ---- H · takes (three columns) ----
tH=st(16)-.3
takes=[(L,C,'“it’s a reset.”',at(17,'reset')-.4),(V,L,'“a divided government keeps things from swinging too far.”',at(18,'divided')-.3),(C,L,'“warren will come after the industry.”',at(18,'warren')-.3)]
cols=''.join(f'<div class="col" style="background:{bg};color:{fg};{kf([(0,"transform:translateY(100%)"),(t,"transform:translateY(100%)"),(t+.6,"transform:none")])}"><div class="bq">{q}</div></div>' for bg,fg,q,t in takes)
scene(tH,V,f'''<div class="cols">{cols}</div><div class="h" style="position:absolute;left:120px;top:110px;font-size:110px;color:{L};z-index:0">{words('on x, people are split.',at(16,'on'),at(16,'split'))}</div>''',L,'leaf','t')
# ---- I · general read (violet) ----
tI=st(19)-.3
scene(tI,V,f'''<div class="fr">{K('the general read',tI+.4)}
<div style="margin:auto 0"><div class="h" style="font-size:150px">{words('regulation',at(19,'regulation'),at(19,'regulation'))} {hl(words("isn’t going away.",at(19,"isn't"),at(19,'away')),at(19,'away'),C,L,L)}</div>
<div class="h" style="font-size:110px;margin-top:30px"><span style="{fade(at(20,'longer'))}">{hl('slower',at(20,'longer'),C,L,L)}</span> <span style="{fade(at(20,'stricter'))}">and {hl('stricter',at(20,'stricter'),C,L,L)}.</span></div>
<ul class="list take"><li style="{appear(at(20,'compliance'),.45,'opacity:0;transform:translateX(-60px)','opacity:1;transform:none')}">compliance becomes part of the pitch</li>
<li style="{appear(at(20,'politicians'),.45,'opacity:0;transform:translateX(-60px)','opacity:1;transform:none')}">political tokens carry political risk</li></ul></div></div>''',L,'leaf','l')
# ---- J · outro (crimson), no CTA ----
tJ=O+VO_END-.1
ofly=kf([(0,'transform:translate(-900px,700px) rotate(30deg) scale(.5)'),(tJ+.2,'transform:translate(-900px,700px) rotate(30deg) scale(.5)'),(tJ+2.2,'transform:none')])
scene(tJ,C,f'''<div class="outro"><div class="olm" style="{ofly}">{moth(L,L,.55,7,'slowflap')}</div>
<div class="h" style="font-size:170px;{appear(tJ+1.7,.6)}">mesokla</div></div>''',L,'leaf','r')

html=f'''<!doctype html><html><head><meta charset="utf-8"><title>Midterms explainer 16:9</title>
<link rel="stylesheet" href="{B}/fonts/fonts.css"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1920px;height:1080px;overflow:hidden;background:{C}}}
.sc{{position:absolute;inset:0;overflow:hidden;font-family:Manrope,sans-serif;isolation:isolate}}
.fr{{position:absolute;inset:90px 120px 140px;display:flex;flex-direction:column}}
.two{{margin:auto 0;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:100px;align-items:center}}
.h{{font-family:Montserrat;font-weight:900;text-transform:uppercase;line-height:.95;letter-spacing:-.01em}}
.w{{display:inline-block}}
.k{{font-weight:800;font-size:30px;letter-spacing:.2em;text-transform:uppercase}}
.hl{{background-image:linear-gradient(var(--b),var(--b));background-repeat:no-repeat;background-position:0 0;padding:0 .12em;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
.sub{{margin-top:26px;font-size:42px;font-weight:700;line-height:1.3}}
.sig{{position:absolute;left:120px;bottom:56px;display:flex;align-items:center;gap:14px;font-family:Montserrat;font-weight:900;font-size:36px;letter-spacing:.04em}}
.sm{{height:64px}} .hd{{position:absolute;right:120px;bottom:64px;font-weight:800;font-size:30px}}
.trail{{position:absolute;inset:0}} .dot{{position:absolute;left:0;top:0;width:14px;height:14px;margin:-7px 0 0 -7px;border-radius:50%;background:{L};offset-rotate:0deg}}
.flyer{{position:absolute;left:0;top:0;width:340px;margin:-150px 0 0 -170px;offset-anchor:center}}
.moth{{width:100%;height:auto;display:block;overflow:visible}}
.moth .wl,.moth .wr{{transform-box:view-box;transform-origin:200px 210px}}
.flap .wl,.flap .wr{{animation:flap .32s ease-in-out infinite}}
.slowflap .wl,.slowflap .wr{{animation:flap .7s ease-in-out infinite}}
@keyframes flap{{50%{{transform:scaleX(.22)}}}}
.row{{display:grid;grid-template-columns:230px minmax(0,1fr);align-items:center;gap:30px;margin:26px 0}}
.rl{{font-family:Montserrat;font-weight:900;font-size:60px;text-transform:uppercase}}
.bar{{position:relative;height:120px;border:6px solid {V}}}
.fill{{position:absolute;left:0;top:0;bottom:0;background:{V}}}
.bt{{position:absolute;left:26px;top:50%;transform:translateY(-50%);font-family:Montserrat;font-weight:900;font-size:50px;text-transform:uppercase;color:{L}}}
.odo{{display:inline-block;height:1em;line-height:1em;overflow:hidden;vertical-align:top}} .strip{{display:flex;flex-direction:column}} .strip span{{height:1em;line-height:1em;text-align:right}}
.stamp{{display:inline-block;margin-top:46px;background:{C};color:{L};font-family:Montserrat;font-weight:900;font-size:64px;text-transform:uppercase;padding:14px 30px}}
.deco{{position:absolute}}
.list{{list-style:none;margin-top:20px}}
.list li{{font-size:50px;font-weight:800;padding:22px 0;border-top:4px solid currentColor;display:flex;gap:30px;align-items:baseline}}
.list li b{{font-family:Montserrat;font-weight:900;color:{V};font-size:42px}}
.take{{margin-top:50px;max-width:1300px}} .take li{{font-size:46px;border-color:{L}}}
.pb{{margin-top:60px;height:80px;border:6px solid {L};position:relative;max-width:1500px}}
.pf{{position:absolute;left:0;top:0;bottom:0;background:{C}}}
.lander{{position:absolute;left:880px;top:330px;width:300px}}
.chart{{position:relative;width:920px;height:520px}}
.cl{{position:absolute;background:{V};color:{L};font-weight:800;font-size:28px;padding:8px 16px;white-space:nowrap;text-transform:uppercase;letter-spacing:.06em}}
.ill{{position:absolute;right:0;top:-36px;font-size:20px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{V}}}
.tag{{display:inline-block;margin-top:50px;background:{C};color:{L};font-family:Montserrat;font-weight:900;font-size:48px;text-transform:uppercase;padding:12px 24px}}
.cols{{position:absolute;left:0;right:0;bottom:0;height:640px;display:grid;grid-template-columns:repeat(3,1fr);z-index:1}}
.col{{padding:60px 50px 150px;display:flex;align-items:flex-start}}
.bq{{font-family:Montserrat;font-weight:900;font-size:58px;line-height:1.02;text-transform:uppercase}}
.outro{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;padding-bottom:60px}}
.olm{{width:320px;margin-bottom:30px}}
.sc .sig,.sc .hd{{z-index:2}}
.card{{background:var(--bc);padding:10px 10px 0;box-sizing:border-box}}
.cap{{font-family:Manrope;font-weight:800;font-size:20px;letter-spacing:.12em;text-transform:uppercase;color:{L};padding:10px 4px 12px}}
.three{{margin:auto 0;display:grid;grid-template-columns:500px minmax(0,1fr) minmax(0,.9fr);gap:60px;align-items:center}}
.sm2 li{{font-size:40px;padding:18px 0}}
.ring{{position:absolute;width:44px;height:44px;border-radius:50%;border:6px solid {V};background:{L}}}
{''.join(css)}
</style></head><body>{''.join(scenes)}</body></html>'''
open('midterms16.html','w').write(html)
import json; EV.update({'cuts':CUTS,'gap':GAP,'T':T,'O':O,'intro_fly':[0,3.4],'outro_fly':[tJ+.2,tJ+2.2],'outro_word':tJ+1.7,'stall':s1,'draw':[c0,c1]}); json.dump(EV,open('events.json','w'),indent=1)
print('T=',T)
