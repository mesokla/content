# Generates mascot concept SVGs in the mesokla palette (+ tints of it for outline, highlights, bellies).
L,V,C="#A6B8A0","#8B729C","#E20942"
D,LL,VL,CL,H="#3E2F4A","#D3DDCF","#BCA9C9","#F27C9B","#F5F7F3"
ST=f'stroke="{D}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"'
def svg(name,body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 440" id="{name}"><g {ST}>{body}</g></svg>'
def mirror(s): return s+f'<g transform="translate(400 0) scale(-1 1)">{s}</g>'
def eyes(cx=52,cy=200,rx=30,ry=35):
    e=''
    for x in (200-cx,200+cx):
        e+=f'<ellipse cx="{x}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{D}"/>'
        e+=f'<circle cx="{x+rx*.33}" cy="{cy-ry*.4}" r="{rx*.34}" fill="{H}" stroke="none"/><circle cx="{x-rx*.25}" cy="{cy+ry*.35}" r="{rx*.14}" fill="{H}" stroke="none"/>'
    return e
def blush(c=C,y=240,dx=88):
    return f'<g stroke="none" fill="{c}" opacity=".55"><ellipse cx="{200-dx}" cy="{y}" rx="17" ry="9"/><ellipse cx="{200+dx}" cy="{y}" rx="17" ry="9"/></g>'
def sit(body,belly,foot_pad,arm=None):
    arm=arm or body
    return (f'<ellipse cx="200" cy="318" rx="94" ry="88" fill="{body}"/>'
            f'<ellipse cx="200" cy="334" rx="52" ry="60" fill="{belly}"/>'
            +''.join(f'<ellipse cx="{x}" cy="394" rx="44" ry="27" fill="{body}"/><ellipse cx="{x}" cy="396" rx="20" ry="12" fill="{foot_pad}" stroke="none"/>' for x in (128,272))
            +f'<ellipse cx="152" cy="336" rx="22" ry="40" fill="{arm}" transform="rotate(14 152 336)"/><ellipse cx="248" cy="336" rx="22" ry="40" fill="{arm}" transform="rotate(-14 248 336)"/>')
smile='<path d="M180 252Q200 266 220 252" fill="none"/>'
out={}

# 1 MOTHI — bat-cat
ear=f'<path d="M108 156C84 104 58 58 30 22C88 34 140 66 168 106Z" fill="{V}"/><path d="M114 138C96 102 80 76 62 50C100 64 132 86 150 110Z" fill="{C}" stroke="none"/>'
out['mothi']=svg('mothi',mirror(ear)+sit(V,L,VL)+f'<ellipse cx="200" cy="192" rx="128" ry="102" fill="{V}"/>'+eyes()+blush()
  +f'<path d="M192 232L208 232L200 242Z" fill="{C}"/>'+'<path d="M176 250Q188 260 200 250Q212 260 224 250" fill="none"/>'
  +f'<path d="M186 254L190 266L194 256M206 256L210 266L214 254" fill="{H}" stroke-width="3"/>'
  +f'<path d="M180 92L190 70L200 90L212 72L218 96" fill="{V}"/>')

# 2 BLIP — axolotl
gill=''.join(f'<ellipse cx="{x}" cy="{y}" rx="44" ry="15" fill="{C}" transform="rotate({r} {x} {y})"/>' for x,y,r in ((76,140,-32),(62,186,-4),(76,232,26)))
out['blip']=svg('blip',mirror(gill)+sit(L,LL,C)+f'<ellipse cx="200" cy="194" rx="132" ry="98" fill="{L}"/>'+eyes(cx=74,cy=196,rx=21,ry=24)+blush(y=230,dx=104)
  +'<path d="M150 236Q200 276 250 236" fill="none"/>'+f'<g fill="{V}" stroke="none"><circle cx="170" cy="130" r="7"/><circle cx="196" cy="118" r="5"/><circle cx="226" cy="128" r="8"/></g>')

# 3 FEN — fennec
ear=f'<path d="M100 150C70 100 46 50 36 8C86 26 140 64 170 104Z" fill="{C}"/><path d="M106 132C86 98 70 66 62 38C96 54 132 80 150 106Z" fill="{L}" stroke="none"/>'
out['fen']=svg('fen',mirror(ear)+sit(C,L,CL)+f'<ellipse cx="200" cy="194" rx="126" ry="100" fill="{C}"/>'
  +f'<path d="M128 240C150 206 250 206 272 240C258 286 142 286 128 240Z" fill="{L}"/>'+eyes(cy=190)+blush(c=V,y=232,dx=96)
  +f'<ellipse cx="200" cy="236" rx="14" ry="10" fill="{D}"/>'+'<path d="M186 258Q200 268 214 258" fill="none"/>'
  +f'<path d="M184 96L194 78L202 94L212 80L216 100" fill="{C}"/>')

# 4 MO — moth
wing=f'<ellipse cx="96" cy="296" rx="84" ry="66" fill="{L}" transform="rotate(-28 96 296)"/><circle cx="78" cy="282" r="20" fill="{C}"/><circle cx="78" cy="282" r="8" fill="{LL}" stroke="none"/><ellipse cx="108" cy="368" rx="46" ry="34" fill="{L}" transform="rotate(20 108 368)"/>'
ant=f'<path d="M168 104C150 62 120 34 88 26" fill="none"/><circle cx="86" cy="26" r="15" fill="{C}"/>'
fluff=''.join(f'<circle cx="{x}" cy="{280+abs(x-200)*.12}" r="22" fill="{LL}"/>' for x in range(122,290,26))
out['mo']=svg('mo',mirror(wing)+mirror(ant)+sit(VL,V,LL,arm=VL)+fluff+f'<ellipse cx="200" cy="188" rx="118" ry="98" fill="{VL}"/>'+eyes(cy=192,rx=33,ry=38)+blush(y=236,dx=84)+smile)

# 5 KWA — frog
bump=f'<circle cx="136" cy="128" r="50" fill="{L}"/><circle cx="136" cy="126" r="34" fill="{LL}"/><circle cx="142" cy="130" r="20" fill="{D}"/><circle cx="148" cy="122" r="7" fill="{H}" stroke="none"/>'
out['kwa']=svg('kwa',sit(L,LL,V)+f'<ellipse cx="200" cy="208" rx="140" ry="92" fill="{L}"/>'+mirror(bump)
  +f'<path d="M132 238Q200 292 268 238Q200 262 132 238Z" fill="{C}"/>'+blush(y=226,dx=108)
  +f'<g fill="{V}" stroke="none"><circle cx="200" cy="168" r="10"/><circle cx="176" cy="190" r="6"/><circle cx="226" cy="186" r="7"/></g>'
  )

# 6 MESSY — little mess monster
blob=(f'<path d="M96 384C70 300 84 150 200 120C316 150 330 300 304 384C298 408 280 416 272 396C266 380 254 386 250 404C246 428 222 428 220 406C218 388 204 388 196 404C186 424 164 420 162 400C160 384 146 384 138 400C126 420 102 410 96 384Z" fill="{C}"/>')
horn=f'<path d="M132 152C118 120 120 94 134 78C142 104 152 122 162 134Z" fill="{V}"/>'
out['messy']=svg('messy',mirror(horn)+blob
  +f'<ellipse cx="160" cy="226" rx="36" ry="42" fill="{D}"/><circle cx="172" cy="210" r="13" fill="{H}" stroke="none"/><circle cx="150" cy="242" r="5" fill="{H}" stroke="none"/>'
  +f'<ellipse cx="244" cy="232" rx="27" ry="32" fill="{D}"/><circle cx="253" cy="220" r="10" fill="{H}" stroke="none"/>'
  +f'<path d="M160 290Q200 330 240 290Z" fill="{D}"/><path d="M188 304Q204 340 222 304Z" fill="{L}"/><path d="M178 292L186 306L194 294" fill="{H}" stroke-width="3"/>'
  +f'<g stroke="none" fill="{V}" opacity=".6"><ellipse cx="112" cy="282" rx="14" ry="8"/><ellipse cx="290" cy="286" rx="14" ry="8"/></g>'
  +f'<ellipse cx="88" cy="300" rx="20" ry="34" fill="{C}" transform="rotate(25 88 300)"/><ellipse cx="312" cy="300" rx="20" ry="34" fill="{C}" transform="rotate(-25 312 300)"/>')
for k,v in out.items(): open(f'svg/{k}.svg','w').write(v)
print(list(out))
