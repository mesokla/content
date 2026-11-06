# Builds templates/intro.html: animated moth intro, 3 scenarios (v=fly|draw|zoom) × 3 themes. CSS keyframes only (scrubbable).
import os, math
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')
FORE="M196 196C160 120 100 70 40 66C22 100 30 170 76 204C116 226 168 214 196 206Z"
HIND="M196 214C164 222 112 244 96 292C98 330 142 342 170 306C184 286 192 252 196 230Z"
MIR='transform="translate(400 0) scale(-1 1)"'
def wing():
    d=lambda p,c='var(--ln)',w=3.6,o=1:f'<path class="dl" pathLength="1" d="{p}" stroke="{c}" stroke-width="{w}" stroke-opacity="{o}"/>'
    return (d(FORE)+d(HIND)+f'<g transform="translate(196 206) scale(.7) translate(-196 -206)">{d(FORE,"var(--ln2)",2.57,"var(--ln2o)")}{d(HIND,"var(--ln2)",2.57,"var(--ln2o)")}</g>'
            '<circle class="spot" cx="92" cy="136" r="5.5" fill="var(--ln)"/>')
ant='<path class="dl" pathLength="1" d="M195 150C184 112 166 92 140 80" stroke="var(--ln)" stroke-width="3.6"/><circle class="spot" cx="140" cy="80" r="4.5" stroke="var(--ln)" stroke-width="3.6"/>'
moth=(f'<svg class="moth" viewBox="20 40 360 320" fill="none" stroke-linecap="round" stroke-linejoin="round">'
      f'<g class="wl">{wing()}</g><g class="wr"><g {MIR}>{wing()}</g></g>{ant}<g {MIR}>{ant}</g>'
      f'<ellipse class="dl" pathLength="1" cx="200" cy="222" rx="9" ry="56" stroke="var(--ln)" stroke-width="3.6"/></svg>')
# flight path (moth centre), ends at final position (800,300)
P=[(-160,1040),(260,720),(260,300),(560,380),(760,450),(900,330),(800,300)]
segs=[(P[0],P[1],P[2],P[3]),(P[3],P[4],P[5],P[6])]
path=f"M{P[0][0]} {P[0][1]}C{P[1][0]} {P[1][1]} {P[2][0]} {P[2][1]} {P[3][0]} {P[3][1]}C{P[4][0]} {P[4][1]} {P[5][0]} {P[5][1]} {P[6][0]} {P[6][1]}"
def bez(s,t):
    a,b,c,d=s; u=1-t
    return tuple(u**3*a[i]+3*u*u*t*b[i]+3*u*t*t*c[i]+t**3*d[i] for i in (0,1))
pts=[bez(segs[0],i/400) for i in range(400)]+[bez(segs[1],i/400) for i in range(401)]
cum=[0]
for i in range(1,len(pts)): cum.append(cum[-1]+math.dist(pts[i],pts[i-1]))
Ltot=cum[-1]
def at(frac):
    tgt=frac*Ltot
    for i,c in enumerate(cum):
        if c>=tgt: return pts[i]
    return pts[-1]
# easing used for flight: cubic-bezier(.25,.6,.35,1); invert numerically progress->time
def cb(t,x1=.25,y1=.6,x2=.35,y2=1):
    u=1-t; return 3*u*u*t*x1+3*u*t*t*x2+t**3, 3*u*u*t*y1+3*u*t*t*y2+t**3
def time_for(prog):
    best=min((abs(cb(i/1000)[1]-prog),cb(i/1000)[0]) for i in range(1001)); return best[1]
FLY=2.6
dots=''
for k in range(1,26):
    f=k/27; x,y=at(f); t=time_for(f)*FLY
    dots+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" style="animation-delay:{t:.3f}s"/>'
html=f'''<!doctype html><html><head><meta charset="utf-8"><title>Intro · animated · 1600×900 · 4.5s</title>
<link rel="stylesheet" href="../brand.css">
<style>
/* v=fly | draw | zoom ; theme=leaf | violet | crimson. CSS keyframes only so scripts/video.mjs can scrub it. 4.5s. */
body{{--ln:var(--crimson);--ln2:var(--violet);--ln2o:1}}
body[data-theme=violet],body[data-theme=crimson]{{--ln:var(--leaf);--ln2:var(--leaf);--ln2o:.55}}
.m{{position:absolute;left:0;top:0;width:330px;height:293px;margin:-146px 0 0 -165px}}
.moth{{width:100%;height:100%;display:block;overflow:visible}}
.tilt{{width:100%;height:100%}}
.wl,.wr{{transform-box:view-box;transform-origin:200px 210px}}
.word{{position:absolute;left:0;right:0;top:530px;text-align:center}}
.word .display{{font-size:150px;letter-spacing:-.02em;color:var(--fg)}}
.word span{{display:inline-block;animation:letter 4.5s cubic-bezier(.2,.8,.2,1) both}}
.trail{{position:absolute;inset:0;width:100%;height:100%;display:none}}
.trail circle{{fill:var(--ln);animation:dot .25s ease-out both}}
@keyframes dot{{0%{{opacity:0;transform:scale(0)}}100%{{opacity:1;transform:none}}}}
.trail{{animation:trailout 4.5s both}}
@keyframes trailout{{0%,68%{{opacity:1}}82%,100%{{opacity:0}}}}
.trail circle{{transform-box:fill-box;transform-origin:center}}
@keyframes flapfast{{0%,100%{{transform:scaleX(1)}}50%{{transform:scaleX(.18)}}}}
@keyframes flapslow{{0%,40%,100%{{transform:scaleX(1)}}65%{{transform:scaleX(.25)}}}}

/* FLY: moth flies in along a dotted trail, lands above the wordmark */
body[data-v=fly] .trail{{display:block}}
body[data-v=fly] .m{{offset-path:path("{path}");offset-rotate:0deg;animation:fly 4.5s both}}
@keyframes fly{{0%{{offset-distance:0%;animation-timing-function:cubic-bezier(.25,.6,.35,1)}}{FLY/4.5*100:.1f}%,100%{{offset-distance:100%}}}}
body[data-v=fly] .tilt{{animation:tilt 4.5s both}}
@keyframes tilt{{0%{{transform:rotate(28deg) scale(.55)}}30%{{transform:rotate(-14deg) scale(.8)}}{FLY/4.5*100:.1f}%,100%{{transform:none}}}}
body[data-v=fly] .wl,body[data-v=fly] .wr{{animation:flapfast .26s ease-in-out 0s 10,flapslow 1.7s ease-in-out 2.6s infinite}}
body[data-v=fly] .word span{{--d:2.5s}}

/* DRAW: the line draws itself, wings flap, moth rises into the lockup */
body[data-v=draw] .m{{left:800px;top:300px;animation:rise 4.5s both}}
@keyframes rise{{0%,52%{{transform:translateY(150px) scale(1.9)}}70%,100%{{transform:none}}}}
body[data-v=draw] .dl{{stroke-dasharray:1 1;animation:draw 4.5s ease-in-out both}}
@keyframes draw{{0%{{stroke-dashoffset:1}}36%,100%{{stroke-dashoffset:0}}}}
body[data-v=draw] .spot{{animation:pop 4.5s both}}
@keyframes pop{{0%,34%{{opacity:0}}40%,100%{{opacity:1}}}}
body[data-v=draw] .wl,body[data-v=draw] .wr{{animation:flapslow .9s ease-in-out 1.65s 2}}
body[data-v=draw] .word span{{--d:3.0s}}

/* ZOOM: starts inside the wing contours, pulls back to reveal the moth */
body[data-v=zoom] .m{{left:800px;top:300px;animation:zoom 4.5s both}}
@keyframes zoom{{0%{{transform:translate(1200px,700px) scale(9) rotate(-20deg)}}10%{{transform:translate(1100px,640px) scale(8) rotate(-16deg);animation-timing-function:cubic-bezier(.6,0,.2,1)}}52%,100%{{transform:none}}}}
body[data-v=zoom] .wl,body[data-v=zoom] .wr{{animation:flapslow 1.5s ease-in-out 2.3s infinite}}
body[data-v=zoom] .word span{{--d:2.6s}}

@keyframes letter{{0%{{opacity:0;transform:translateY(50px)}}100%{{opacity:1;transform:none}}}}
.word span{{animation:letter .7s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(var(--d,2.5s) + var(--i)*.06s)}}
</style></head><body data-v="fly" data-theme="crimson"><div class="canvas">
<svg class="trail" viewBox="0 0 1600 900">{dots}</svg>
<div class="m"><div class="tilt">{moth}</div></div>
<div class="word"><div class="display">'''+''.join(f'<span style="--i:{i}">{ch}</span>' for i,ch in enumerate('mesokla'))+'''</div></div>
</div><script src="fill.js"></script><script>const v=new URLSearchParams(location.search).get('v');if(v)document.body.dataset.v=v;</script></body></html>'''
open('templates/intro.html','w').write(html)
print('ok')
