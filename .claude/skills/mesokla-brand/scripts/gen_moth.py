# Generates the final mesokla moth (front + flight) and abstract identity elements, baked in brand colours.
# Run: python3 scripts/gen_moth.py   (from the skill folder)
import os, math
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')
L,V,C="#A6B8A0","#8B729C","#E20942"
NAMES={'crimson':C,'violet':V,'leaf':L}
ECHO={'crimson':(V,1),'violet':(C,1),'leaf':(L,.55)}   # echo contour colour per line colour
FORE="M196 196C160 120 100 70 40 66C22 100 30 170 76 204C116 226 168 214 196 206Z"
HIND="M196 214C164 222 112 244 96 292C98 330 142 342 170 306C184 286 192 252 196 230Z"
MIR='transform="translate(400 0) scale(-1 1)"'
W=3.6   # main line: between "Original" (5) and "Fine" (2.2)
def wing(c,e,eo):
    ech=f'<g transform="translate(196 206) scale(.7) translate(-196 -206)" stroke="{e}" stroke-opacity="{eo}" stroke-width="{1.8/.7:.2f}"><path d="{FORE}"/><path d="{HIND}"/></g>'
    return f'<path d="{FORE}"/><path d="{HIND}"/>{ech}<circle cx="92" cy="136" r="5.5" fill="{c}" stroke="none"/>'
def antenna(): return '<path d="M195 150C184 112 166 92 140 80"/><circle cx="140" cy="80" r="4.5"/>'
def head(c): return f'<g stroke="{c}" stroke-width="{W}" fill="none" stroke-linecap="round" stroke-linejoin="round">'
def front(c,e,eo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="20 40 360 320">{head(c)}'
            f'<g class="wl">{wing(c,e,eo)}</g><g class="wr"><g {MIR}>{wing(c,e,eo)}</g></g>'
            f'{antenna()}<g {MIR}>{antenna()}</g><ellipse cx="200" cy="222" rx="9" ry="56"/></g></svg>')
def flight(c,e,eo,trail=False):
    tr=(f'<path d="M-150 420C-60 330 10 420 90 340C130 300 150 280 176 262" stroke-dasharray="0 13" stroke-width="5"/>' if trail else '')
    vb='-170 20 590 440' if trail else '-6 16 412 392'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{head(c)}{tr}<g transform="rotate(-14 200 210)">'
            f'<g class="wl">{wing(c,e,eo)}</g>'
            f'<g class="wr"><g transform="translate(200 0) scale(.42 1) translate(-200 0)"><g {MIR}><path d="{FORE}"/><path d="{HIND}"/></g></g></g>'
            f'{antenna()}<g transform="translate(200 0) scale(.6 1) translate(-200 0)"><g {MIR}>{antenna()}</g></g>'
            f'<ellipse cx="200" cy="222" rx="9" ry="56"/></g></g></svg>')
for n,c in NAMES.items():
    e,eo=ECHO[n]
    open(f'moth/moth-front-{n}.svg','w').write(front(c,e,eo))
    open(f'moth/moth-flight-{n}.svg','w').write(flight(c,e,eo))
    open(f'moth/moth-trail-{n}.svg','w').write(flight(c,e,eo,True))

# ---- abstract elements, each derived from the moth ----
def el(vb,body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{body}</svg>'
ELS={
 'wing':   lambda c: el('18 54 192 178',f'<path d="{FORE}" fill="{c}"/>'),
 'wings':  lambda c: el('20 56 360 300',f'<path d="{FORE}" fill="{c}"/><path d="{HIND}" fill="{c}"/><g {MIR}><path d="{FORE}" fill="{c}"/><path d="{HIND}" fill="{c}"/></g>'),
 'contour':lambda c: el('16 52 196 182',f'<g fill="none" stroke="{c}" stroke-width="3">'+''.join(f'<path transform="translate(196 206) scale({s}) translate(-196 -206)" stroke-width="{3/s:.2f}" d="{FORE}"/>' for s in (1,.76,.52,.28))+'</g>'),
 'trail':  lambda c: el('0 0 400 200',f'<path d="M10 170C90 60 170 190 250 100C290 55 330 40 372 44" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round" stroke-dasharray="0 16"/><circle cx="380" cy="44" r="9" fill="{c}"/>'),
 'curl':   lambda c: el('0 0 200 200',f'<path d="M20 180C40 110 90 50 150 40C180 36 186 70 160 78C140 84 132 62 146 56" fill="none" stroke="{c}" stroke-width="6" stroke-linecap="round"/>'),
 'dots':   lambda c: el('0 0 220 160',f'<circle cx="30" cy="130" r="10" fill="{c}"/><circle cx="90" cy="96" r="18" fill="{c}"/><circle cx="170" cy="50" r="30" fill="{c}"/>'),
 'spot':   lambda c: el('0 0 200 200',f'<circle cx="100" cy="100" r="88" fill="none" stroke="{c}" stroke-width="6"/><circle cx="100" cy="100" r="58" fill="none" stroke="{c}" stroke-width="3"/><circle cx="100" cy="100" r="22" fill="{c}"/>'),
 'lens':   lambda c: el('0 0 200 200',f'<path d="M20 180A160 160 0 0 1 180 20A160 160 0 0 1 20 180Z" fill="{c}"/>'),
}
for k,f in ELS.items():
    for n,c in NAMES.items(): open(f'elements/{k}-{n}.svg','w').write(f(c))
print('ok', len(os.listdir('moth')), len(os.listdir('elements')))
