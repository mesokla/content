# Diagonal-symmetry variants of the "Mirror" banner: moth top-left, moth bottom-right, mirrored edge elements.
import subprocess
exec(open('gen.py').read().split("V_={}")[0])   # reuse helpers
def diag(bg,mc,ec,edge,acc,trail=False,name=''):
    edges={
     'contour':[el('contour',ec,-70,-50,300,15), el('contour',ec,1265,250,300,195)],
     'lens':   [el('lens',ec,-80,-60,280,0), el('lens',ec,1300,280,280,180)],
     'spot':   [el('spot',ec,-110,-110,330), el('spot',ec,1280,280,330)],
     'wing':   [el('wing',ec,-50,-70,290,-20), el('wing',ec,1250,270,290,160)],
    }[edge]
    items=edges+[
      moth('flight',mc,268,-2,205,-4),
      moth('flight',mc,1040,282,205,4,flip=True),
      word('mesokla',{'leaf':L,'crimson':C,'violet':V}[mc],750,205,104),
      el('dots',acc,560,60,44,0), el('dots',acc,900,380,44,180),
    ]
    if trail: items+=[el('trail',mc,90,150,90,-25,op=.95), el('trail',mc,1170,250,90,155,op=.95)]
    return page(bg,items)
W={
 'diag-leaf':   diag(L,'crimson','violet','contour','violet'),
 'diag-crimson':diag(C,'leaf','violet','lens','violet'),
 'diag-violet': diag(V,'leaf','crimson','spot','crimson'),
 'diag-leaf-wing':diag(L,'crimson','violet','wing','violet',trail=True),
 'diag-violet-contour':diag(V,'leaf','leaf','contour','crimson',trail=True),
}
for k,v in W.items():
    open(f'{k}.html','w').write(v)
    subprocess.run(['node',f'{B}/scripts/render.mjs',f'{k}.html',f'png/banner-{k}.png','size=1500x500'],check=True,capture_output=True)
print(list(W))
