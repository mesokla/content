# Variations of the line-art moth. Colours come from CSS vars on the card: --ln (main line), --ln2 (echo/accent), --bg.
FORE="M196 196C160 120 100 70 40 66C22 100 30 170 76 204C116 226 168 214 196 206Z"
HIND="M196 214C164 222 112 244 96 292C98 330 142 342 170 306C184 286 192 252 196 230Z"
MIR='transform="translate(400 0) scale(-1 1)"'
def sv(wing,center='',cls=''):
    return (f'<svg viewBox="0 0 400 400" class="moth {cls}" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round">'
            f'<g class="wl">{wing}</g><g class="wr"><g {MIR}>{wing}</g></g>{center}</svg>')
def p(d,w=5,c='var(--ln)',extra=''): return f'<path class="dl" pathLength="1" d="{d}" stroke="{c}" stroke-width="{w}" {extra}/>'
def ant(w=4,c='var(--ln)',tip=True,d="M195 150C184 112 166 92 140 80"):
    a=p(d,w,c)+(f'<circle cx="140" cy="80" r="5" stroke="{c}" stroke-width="{w}"/>' if tip else '')
    return a+f'<g {MIR}>{a}</g>'
def echo(s,ds=(FORE,HIND),w=3,c='var(--ln2)'):
    return f'<g transform="translate(196 206) scale({s}) translate(-196 -206)">'+''.join(p(d,w/s,c) for d in ds)+'</g>'
BODY=lambda w=5,c='var(--ln)':f'<ellipse class="dl" pathLength="1" cx="200" cy="222" rx="10" ry="58" stroke="{c}" stroke-width="{w}"/>'
V=[]
V.append(('original','Original','Твій улюблений: лінія і контур-луна всередині. Еталон, від якого відштовхуємось.',
  sv(p(FORE)+p(HIND)+echo(.68)+'<circle cx="90" cy="134" r="8" fill="var(--ln)"/>',ant()+BODY())))
V.append(('fine','Fine','Тонка ювелірна лінія 2px і дві луни. Делікатно, як гравюра, найкраще виглядає великою.',
  sv(p(FORE,2.2)+p(HIND,2.2)+echo(.74,w=1.6)+echo(.5,w=1.6)+'<circle cx="92" cy="136" r="4" fill="var(--ln)"/>',ant(2,tip=False)+BODY(2.2))))
V.append(('bold','Bold','Жирна лінія без луни. Важить як логотип, читається навіть маленькою в аватарці.',
  sv(p(FORE,11)+p(HIND,11),ant(10,tip=False)+f'<path class="dl" pathLength="1" d="M200 166L200 284" stroke="var(--ln)" stroke-width="11"/>')))
ONE=("M140 80C166 92 184 112 195 150L196 196C160 120 100 70 40 66C22 100 30 170 76 204C116 226 168 214 196 206L196 214C164 222 112 244 96 292C98 330 142 342 170 306C184 286 192 252 196 230"
     "L200 290L204 230C208 252 216 286 230 306C258 342 302 330 304 292C288 244 236 222 204 214L204 206C232 214 284 226 324 204C370 170 378 100 360 66C300 70 240 120 204 196L205 150C216 112 234 92 260 80")
V.append(('one','One Line','Увесь метелик однією безперервною лінією, не відриваючи руки. Ефектно промальовується в анімації.',
  f'<svg viewBox="0 0 400 400" class="moth" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round">{p(ONE,5)}</svg>'))
V.append(('double','Double','Подвійна лінія, як неоновий контур чи вишивка. Святковіший варіант.',
  sv(p(FORE,13)+p(HIND,13)+p(FORE,4.5,'var(--bg)')+p(HIND,4.5,'var(--bg)'),ant(5)+BODY(6))))
V.append(('dots','Dotted','Лінія з крапок, як шов або сузір\'я. Легка і повітряна, добре мерехтить.',
  sv(f'<g stroke-dasharray="0 15">{p(FORE,7)}{p(HIND,7)}</g>'.replace('class="dl" pathLength="1" ',''),ant(4,tip=True)+BODY(5),cls='nodraw')))
MF="M196 192C170 150 110 100 26 112C38 166 96 210 196 210Z"; MH="M196 216C160 222 108 252 118 292C150 304 186 262 196 234Z"
fe=''.join(f'<path class="dl" pathLength="1" d="M{x} {y}l{dx} {dy}" stroke="var(--ln)" stroke-width="3"/>' for x,y,dx,dy in ((184,124,-12,4),(176,110,-12,2),(166,98,-12,0),(154,88,-10,-2)))
V.append(('moth','True Moth','Саме міль, а не метелик: трикутні передні крила і пухнасті вусики-пір\'їнки. Містичніше.',
  sv(p(MF)+p(MH)+echo(.66,(MF,MH)),ant(3,tip=False,d="M196 150C186 118 168 96 146 84")+f'{fe}<g {MIR}>{fe}</g>'+BODY())))
GF="M196 196L40 66L28 170L80 206L196 206Z"; GH="M196 216L84 276L132 336L196 238Z"
V.append(('geo','Geometric','Ламані лінії замість кривих. Технологічно, пасує до web3.',
  sv(p(GF)+p(GH)+p("M196 200L66 104L56 168",2.5,'var(--ln2)')+p("M196 222L124 300",2.5,'var(--ln2)'),ant(4,tip=False,d="M196 150L170 104L140 82")+p("M200 160L200 288",5))))
V.append(('accent','Line + Fill','Лінія плюс одна заливка: нижні крила зафарбовані другим кольором. Додає ваги, але лишається легким.',
  sv(f'<path d="{HIND}" fill="var(--ln2)" stroke="none"/>'+p(FORE)+p(HIND)+echo(.62,(FORE,)),ant()+BODY())))
V.append(('gesture','Gesture','Кілька незамкнених штрихів, як ескіз пензлем. Найабстрактніший: метелик тільки вгадується.',
  sv(p("M190 196C150 120 90 70 40 66C24 100 30 170 80 204",6)+p("M190 222C140 236 100 260 96 292C98 330 140 340 168 306",6),p("M200 150L200 290",6))))
V.append(('topo','Contour','Три концентричні контури, як топографічна мапа чи відбиток пальця. Гіпнотично в анімації.',
  sv(p(FORE,4)+p(HIND,4)+echo(.78,w=3)+echo(.56,w=3,c='var(--ln)')+echo(.34,w=3),ant(3,tip=False)+BODY(4))))
V.append(('flight','In Flight','Метелик у польоті: одне крило в перспективі. Вже є рух, тож підходить для стікерів і банерів.',
  f'<svg viewBox="0 0 400 400" class="moth" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><g transform="rotate(-12 200 210)">'
  f'<g class="wl">{p(FORE)}{p(HIND)}{echo(.68)}</g><g class="wr"><g transform="translate(200 0) scale(.42 1) translate(-200 0)"><g {MIR}>{p(FORE)}{p(HIND)}</g></g></g>{ant()}{BODY()}</g></svg>'))
import json; json.dump(V,open('variants.json','w'))
print(len(V))
