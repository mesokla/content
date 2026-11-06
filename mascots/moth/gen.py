# Moth / butterfly concept variants in the mesokla palette (+ tints/shades of it).
import math, random, json
L,V,C="#A6B8A0","#8B729C","#E20942"
D,LL,VL,VD,CL,CD,LD="#3E2F4A","#D3DDCF","#BCA9C9","#5E4A6E","#F27C9B","#9E0630","#71856B"
FORE="M196 196C160 120 100 70 40 66C22 100 30 170 76 204C116 226 168 214 196 206Z"
HIND="M196 214C164 222 112 244 96 292C98 330 142 342 170 306C184 286 192 252 196 230Z"
def wrap(k,defs,wing,center,extra=''):
    # wings live in .wl / .wr so CSS can flap them (scaleX around the body)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" class="moth" id="{k}"><defs>{defs}</defs>{extra}'
            f'<g class="wl">{wing}</g><g class="wr"><g transform="translate(400 0) scale(-1 1)">{wing}</g></g>{center}</svg>')
def ant(stroke,w=4,tip=''):
    a=f'<path d="M195 150C184 112 166 92 140 80" fill="none" stroke="{stroke}" stroke-width="{w}" stroke-linecap="round"/>'+tip
    return a+f'<g transform="translate(400 0) scale(-1 1)">{a}</g>'
out={}

# 2D-1 FLAT MARK — clean symbol, no face
out['flat']=wrap('flat','',
  f'<path d="{FORE}" fill="{V}"/><path d="{HIND}" fill="{C}"/><circle cx="96" cy="142" r="22" fill="{L}"/><circle cx="96" cy="142" r="9" fill="{C}"/>',
  ant(D,5,f'<circle cx="140" cy="80" r="7" fill="{D}"/>')+f'<ellipse cx="200" cy="222" rx="11" ry="60" fill="{D}"/><circle cx="200" cy="158" r="15" fill="{D}"/>')

# 2D-2 LINE — single weight outline with an echo contour
echo=f'<g transform="translate(196 206) scale(.68) translate(-196 -206)"><path d="{FORE}"/><path d="{HIND}"/></g>'
out['line']=wrap('line','',
  f'<g fill="none" stroke="{C}" stroke-width="5" stroke-linejoin="round"><path d="{FORE}"/><path d="{HIND}"/></g><g fill="none" stroke="{V}" stroke-width="3">{echo}</g><circle cx="90" cy="134" r="8" fill="{C}"/>',
  ant(C,4,f'<circle cx="140" cy="80" r="5" fill="none" stroke="{C}" stroke-width="4"/>')+f'<ellipse cx="200" cy="222" rx="10" ry="58" fill="none" stroke="{C}" stroke-width="5"/>')

# 2D-3 COOL CHARACTER — grown-up moth: heavy lids, smirk, no blush
frond=f'<path d="M192 112C178 76 156 52 128 40" fill="none" stroke="{D}" stroke-width="4" stroke-linecap="round"/>'+''.join(
  f'<path d="M{x} {y}l-14 {d}" stroke="{C}" stroke-width="5" stroke-linecap="round"/>' for x,y,d in ((178,88,-10),(166,72,-12),(152,58,-12),(140,48,-10)))
fur=''.join(f'<circle cx="{200+math.cos(a)*36:.1f}" cy="{196+math.sin(a)*14:.1f}" r="15" fill="{LL}" stroke="{D}" stroke-width="4"/>' for a in [i*math.pi/5 for i in range(10)])
eye=(f'<path d="M160 150L192 150Q188 168 176 168Q164 168 160 150Z" fill="{D}"/><circle cx="182" cy="157" r="3.5" fill="{LL}"/>'
     f'<path d="M156 149L196 149" stroke="{D}" stroke-width="5" stroke-linecap="round"/><path d="M156 149l-8 -6" stroke="{D}" stroke-width="4" stroke-linecap="round"/>')
out['cool']=wrap('cool','',
  f'<g stroke="{D}" stroke-width="5" stroke-linejoin="round"><path d="{FORE}" fill="{V}"/><path d="{HIND}" fill="{C}"/></g><circle cx="96" cy="140" r="18" fill="{L}" stroke="{D}" stroke-width="4"/>',
  frond+f'<g transform="translate(400 0) scale(-1 1)">{frond}</g>'
  +f'<ellipse cx="200" cy="262" rx="30" ry="62" fill="{VL}" stroke="{D}" stroke-width="5"/>'+fur
  +f'<circle cx="200" cy="150" r="44" fill="{VL}" stroke="{D}" stroke-width="5"/>'+eye+f'<g transform="translate(400 0) scale(-1 1)">{eye}</g>'
  +f'<path d="M194 176Q204 180 212 172" fill="none" stroke="{D}" stroke-width="4" stroke-linecap="round"/>')

# 2D-4 PIXEL — 8-bit, web3 nod
M=["......d...","........d.",".vvvv....d","vvvvvvv...","vvllvvvvv.","vlccvvvvvv","vvllvvvvvv",".vvvvvvvvv","..vvvvvvvv","....cccccc","...ccccccc","..cccllccc","..ccccccc.","...ccccc..","....ccc..."]
col={'v':V,'c':C,'l':L,'d':D}; cs=16; ox=200-10.5*cs; oy=80
px=''.join(f'<rect x="{ox+c*cs}" y="{oy+r*cs}" width="{cs}" height="{cs}" fill="{col[ch]}"/>' for r,row in enumerate(M) for c,ch in enumerate(row) if ch!='.')
body=''.join(f'<rect x="{ox+10*cs}" y="{oy+r*cs}" width="{cs}" height="{cs}" fill="{D}"/>' for r in range(2,14))
out['pixel']=wrap('pixel','',px,body,'')

# 3D-1 GLOSSY — inflated toy look with gradients + specular
defs=(f'<radialGradient id="gv" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="{VL}"/><stop offset=".55" stop-color="{V}"/><stop offset="1" stop-color="{VD}"/></radialGradient>'
      f'<radialGradient id="gc" cx=".4" cy=".3" r=".8"><stop offset="0" stop-color="{CL}"/><stop offset=".5" stop-color="{C}"/><stop offset="1" stop-color="{CD}"/></radialGradient>'
      f'<radialGradient id="gl" cx=".35" cy=".3"><stop offset="0" stop-color="{LL}"/><stop offset="1" stop-color="{LD}"/></radialGradient>'
      f'<linearGradient id="gb" x1="0" x2="1"><stop offset="0" stop-color="{VD}"/><stop offset=".45" stop-color="{VL}"/><stop offset="1" stop-color="{D}"/></linearGradient>'
      '<filter id="blur"><feGaussianBlur stdDeviation="8"/></filter>')
out['glossy']=wrap('glossy',defs,
  f'<path d="{FORE}" fill="url(#gv)"/><path d="{HIND}" fill="url(#gc)"/><circle cx="96" cy="142" r="20" fill="url(#gl)"/>'
  f'<ellipse cx="96" cy="104" rx="34" ry="10" fill="#fff" opacity=".45" transform="rotate(-18 96 104)"/><ellipse cx="128" cy="268" rx="18" ry="6" fill="#fff" opacity=".4" transform="rotate(-40 128 268)"/>',
  ant(VD,6,f'<circle cx="140" cy="80" r="9" fill="url(#gc)"/>')+f'<ellipse cx="200" cy="224" rx="14" ry="62" fill="url(#gb)"/><circle cx="200" cy="156" r="18" fill="url(#gb)"/><ellipse cx="195" cy="150" rx="6" ry="4" fill="#fff" opacity=".6"/>',
  f'<ellipse cx="200" cy="372" rx="120" ry="12" fill="{D}" opacity=".28" filter="url(#blur)"/>')

# 3D-2 ORIGAMI — faceted paper fold
A=(196,200);B=(40,66);E=(66,206);Mf=(118,146);A2=(196,216);F=(96,298);G=(156,328);Hh=(150,246)
tri=lambda pts,c:'<polygon points="'+' '.join(f'{x},{y}' for x,y in pts)+f'" fill="{c}"/>'
out['origami']=wrap('origami','',
  tri((A,B,Mf),VL)+tri((B,Mf,E),VD)+tri((A,Mf,E),V)+tri((A2,Hh,F),CL)+tri((A2,F,G),C)+tri((Hh,F,(120,250)),CD),
  ant(D,3)+tri(((200,140),(210,220),(200,290),(190,220)),D))

# ABSTRACT-1 BAUHAUS — quarter and half circles
out['bauhaus']=wrap('bauhaus','',
  f'<path d="M194 196A150 150 0 0 1 36 52A150 150 0 0 1 194 196Z" fill="{V}"/><path d="M194 214A110 110 0 0 0 86 332A110 110 0 0 0 194 214Z" fill="{C}"/><circle cx="116" cy="124" r="16" fill="{L}"/>',
  f'<rect x="194" y="40" width="12" height="290" rx="6" fill="{D}"/>')

# ABSTRACT-2 INK BLOT — Rorschach symmetry, "smtm mess"
random.seed(11)
def blob(cx,cy,r,n,j):
    pts=[]
    for i in range(n):
        a=-math.pi/2+math.pi*i/(n-1); rr=r*(1+random.uniform(-j,j))
        pts.append((cx-abs(math.cos(a))*rr*1.25, cy+math.sin(a)*rr))
    full=pts+[(400-x,y) for x,y in reversed(pts)]
    d=f'M{full[0][0]:.1f} {full[0][1]:.1f}'
    for i in range(len(full)):
        p0,p1,p2,p3=full[i-1],full[i],full[(i+1)%len(full)],full[(i+2)%len(full)]
        c1=(p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6);c2=(p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6)
        d+=f'C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}'
    return d+'Z'
b1=blob(200,190,140,11,.32); b2=blob(200,200,70,9,.4)
dots=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{V}"/><circle cx="{400-x}" cy="{y}" r="{r}" fill="{V}"/>' for x,y,r in ((120,120,12),(96,230,8),(150,300,10),(70,170,5)))
out['ink']=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" class="moth" id="ink"><g class="pulse"><path d="{b1}" fill="{C}"/><path d="{b2}" fill="{V}"/>{dots}</g></svg>')

# ABSTRACT-3 ORBIT — four circles = four wings, minimal logo mark
out['orbit']=wrap('orbit','',
  f'<circle cx="128" cy="150" r="74" fill="{V}"/><circle cx="148" cy="270" r="50" fill="{C}"/><circle cx="128" cy="150" r="26" fill="{L}" />',
  f'<rect x="194" y="96" width="12" height="230" rx="6" fill="{D}"/>')
for k,v in out.items(): open(f'{k}.svg','w').write(v)
print(list(out))
