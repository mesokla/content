# X header variants (1500x500) for @mesokla, built from the mesokla-brand moth + elements.
import os, subprocess
B='/home/user/content/.claude/skills/mesokla-brand'
L,V,C='#A6B8A0','#8B729C','#E20942'
def moth(pose,col,x,y,h,rot=0,flip=False,op=1):
    return f'<img src="{B}/moth/moth-{pose}-{col}.svg" style="left:{x}px;top:{y}px;height:{h}px;transform:rotate({rot}deg){" scaleX(-1)" if flip else ""};opacity:{op}">'
def el(name,col,x,y,h,rot=0,flip=False,op=1):
    return f'<img src="{B}/elements/{name}-{col}.svg" style="left:{x}px;top:{y}px;height:{h}px;transform:rotate({rot}deg){" scaleX(-1)" if flip else ""};opacity:{op}">'
def word(text,col,x,y,size,align='center',ls='.04em',extra=''):
    return f'<div class="w" style="left:{x}px;top:{y}px;font-size:{size}px;color:{col};letter-spacing:{ls};transform:translateX({"-50%" if align=="center" else "0"});{extra}">{text}</div>'
def page(bg,items):
    return f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="{B}/fonts/fonts.css">
<style>*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1500px;height:500px;overflow:hidden;background:{bg};position:relative}}
img{{position:absolute;display:block;transform-origin:center}}.w{{position:absolute;font-family:Montserrat;font-weight:900;text-transform:uppercase;line-height:1;white-space:nowrap}}
.blk{{position:absolute}}</style></head><body>{''.join(items)}</body></html>'''
V_={}
# 1 MIRROR — small wordmark, two moths facing in, trails from the edges
V_['mirror']=page(L,[
  el('lens','violet',1300,-80,240,20), el('curl','violet',560,40,90,-10), el('dots','violet',880,60,56),
  el('trail','crimson',40,40,120,170,flip=True), el('trail','crimson',1220,300,120,-10,flip=True),
  moth('flight','crimson',255,110,220,0), moth('flight','crimson',1015,110,220,0,flip=True),
  word('mesokla',C,750,200,112), el('spot','violet',1395,330,120), el('lens','violet',700,360,70,-30)])
# 2 GARDEN — crimson, big cropped wings, moths crossing
V_['garden']=page(C,[
  el('wing','violet',-40,-90,300,-25), el('wing','violet',1260,250,330,160),
  el('contour','leaf',1210,-60,250,30,op=.9),
  el('trail','leaf',330,40,140,10), moth('flight','leaf',560,30,170,-6),
  moth('front','leaf',1085,285,140,12),
  word('mesokla',L,750,215,110), el('dots','violet',470,330,64,0), el('curl','leaf',1110,70,100,40)])
# 3 ORBIT — violet, eyespots and petals
V_['orbit']=page(V,[
  el('spot','crimson',1240,-120,420), el('spot','leaf',420,30,120,op=.9),
  el('lens','crimson',-60,-90,260,0), el('lens','leaf',980,330,190,90),
  moth('flight','leaf',560,50,150,-10), moth('flight','leaf',1000,60,160,0,flip=True),
  word('mesokla',L,750,240,104), el('dots','crimson',460,360,60)])
# 4 FLIGHT PATH — one long trail across, three moths of different sizes
trail='<svg style="position:absolute;left:0;top:0" width="1500" height="500" viewBox="0 0 1500 500"><path d="M-20 300C120 120 260 120 380 210S640 360 760 250 1000 60 1140 140 1380 330 1530 180" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round" stroke-dasharray="0 17"/></svg>'%C
V_['flightpath']=page(L,[trail,
  moth('flight','crimson',330,110,120,-20), moth('flight','crimson',1080,30,210,0), moth('front','crimson',690,160,90,10),
  word('mesokla',C,750,360,92), el('lens','violet',-70,-80,230,0), el('spot','violet',1380,350,150), el('dots','violet',540,40,60)])
# 5 BLOCKS — three colour blocks, each with its own element
V_['blocks']=page(L,[
  '<div class="blk" style="left:0;top:0;width:380px;height:500px;background:#8B729C"></div>',
  '<div class="blk" style="left:1120px;top:0;width:380px;height:500px;background:#E20942"></div>',
  el('contour','leaf',70,-40,300,10), el('dots','crimson',250,240,70),
  moth('flight','leaf',1170,90,250,0,flip=True), el('lens','violet',1390,330,220,90),
  word('mesokla',C,750,190,104), el('trail','crimson',560,300,90,-6), el('curl','violet',880,300,100,30)])
# 6 SCATTER — violet, many small elements around a centered wordmark
items=[]
for n,col,x,y,h,r in [('lens','crimson',90,40,90,30),('dots','leaf',300,70,50,0),('curl','leaf',1150,40,90,-20),('spot','crimson',1330,60,90,0),
                      ('wing','crimson',1240,330,130,150),('contour','leaf',520,330,110,-20),('lens','leaf',980,360,80,-40),('dots','crimson',1420,260,50,90),
                      ('spot','leaf',450,40,60,0),('curl','crimson',880,60,80,60)]:
    items.append(el(n,col,x,y,h,r))
items+= [moth('flight','leaf',640,40,140,-8), moth('front','leaf',1080,190,90,14,op=1), word('mesokla',L,750,220,112)]
V_['scatter']=page(V,items)
for k,v in V_.items():
    open(f'{k}.html','w').write(v)
    subprocess.run(['node',f'{B}/scripts/render.mjs',f'{k}.html',f'png/banner-{k}.png','size=1500x500'],check=True,capture_output=True)
print(list(V_))
