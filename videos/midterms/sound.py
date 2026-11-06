# Synthesised music bed + sound effects for the midterms video, timed from events.json.
import json, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
SR=44100; E=json.load(open('events.json')); T=E['T']; O=E['O']
N=int(SR*(T+0.5)); rng=np.random.default_rng(7)
def t_(d): return np.arange(int(SR*d))/SR
def put(buf,x,at,g=1.0):
    i=int(at*SR); j=min(len(buf),i+len(x))
    if i<len(buf): buf[i:j]+=x[:j-i]*g
def bp(x,lo,hi): return sosfilt(butter(2,[lo,hi],btype='band',fs=SR,output='sos'),x)
def lp(x,f): return sosfilt(butter(2,f,btype='low',fs=SR,output='sos'),x)
def hp(x,f): return sosfilt(butter(2,f,btype='high',fs=SR,output='sos'),x)
def env(n,a,r):
    e=np.ones(n); A=max(1,int(a*SR)); R=max(1,int(r*SR))
    e[:A]=np.linspace(0,1,A); e[-R:]*=np.linspace(1,0,R); return e
note=lambda m:440*2**((m-69)/12)
# ---------------- music ----------------
mus=np.zeros(N); BPM=92; beat=60/BPM; bar=4*beat
chords=[(57,[57,60,64]),(53,[53,57,60]),(48,[52,55,60]),(55,[55,59,62])]   # Am F C G
def pad(freqs,d):
    t=t_(d); x=np.zeros_like(t)
    for f in freqs:
        for det in (-0.004,0,0.004):
            for h in range(1,7): x+=np.sin(2*np.pi*f*(1+det)*h*t+rng.random()*6)/h**1.6
    return lp(x,1800)*env(len(t),.5,.8)
def pluck(f,d=.5):
    t=t_(d); x=(2*np.abs(2*((f*t)%1)-1)-1)*np.exp(-t*7); return lp(x,3500)
def kick():
    t=t_(.35); f=45+90*np.exp(-t*25); return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*9)
def hat():
    t=t_(.05); return hp(rng.standard_normal(len(t)),7000)*np.exp(-t*90)
k=0; tt=0.0
while tt<T:
    root,ch=chords[k%4]
    put(mus,pad([note(m) for m in ch],bar+.8),tt,.10)
    if tt>=O-0.01:
        for b in (0,2.5): put(mus,np.sin(2*np.pi*note(root-12)*t_(beat*1.2))*env(int(SR*beat*1.2),.01,.3),tt+b*beat,.22)
        for b in (0,2): put(mus,kick(),tt+b*beat,.5)
    if tt>=E['wipe'][0]-0.01:
        for s in range(8):
            put(mus,hat(),tt+s*beat/2,.07 if s%2 else .04)
            arp=[ch[0],ch[1],ch[2],ch[1]+12][s%4]
            put(mus,pluck(note(arp+12)),tt+s*beat/2,.05)
    tt+=bar; k+=1
fade=np.ones(N); fi=int(SR*2.5); fade[:fi]=np.linspace(0,1,fi)
fo0=int(SR*(T-2.5)); fade[fo0:]=np.linspace(1,0,N-fo0); mus*=fade
# riser into the voice
r=t_(2.2); riser=bp(rng.standard_normal(len(r)),300,4000)*np.linspace(0,1,len(r))**2; put(mus,riser,O-2.2,.12)
# ---------------- sfx ----------------
fx=np.zeros(N)
def flap(g=1.0):
    t=t_(.16); n=rng.standard_normal(len(t))
    return (bp(n,500,2200)*np.exp(-t*30)+lp(n,300)*np.exp(-t*22)*1.5)*g
def flight(a,b,period=.7):
    tt=a; i=0
    while tt<b:
        prog=(tt-a)/(b-a); put(fx,flap(),tt,.18+.25*prog); tt+=period/2; i+=1
flight(*E['intro_fly']); flight(*E['outro_fly'])
def whoosh(d=.55):
    t=t_(d); n=rng.standard_normal(len(t)); lo=bp(n,200,900); hi=bp(n,900,3500)
    m=np.sin(np.linspace(0,np.pi,len(t)))
    return (lo*(1-np.linspace(0,1,len(t)))+hi*np.linspace(0,1,len(t)))*m**1.5
for w in E['wipe']: put(fx,whoosh(),w-.1,.35)
def popx(f0):
    t=t_(.09); f=f0*(1+.5*np.exp(-t*60)); return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*40)
for i,h in enumerate(E['hl']): put(fx,popx(880*2**((i%4)/12)),h,.22)
def tick():
    t=t_(.02); return np.sin(2*np.pi*1600*t)*np.exp(-t*300)
for x in E['tick']: put(fx,tick(),x,.16)
def thud():
    t=t_(.3); f=50+70*np.exp(-t*30); return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*12)+hp(rng.standard_normal(len(t)),2000)*np.exp(-t*60)*.3
for p in E['pop']: put(fx,thud(),p+.15,.45)
t=t_(.5); stall=np.sin(2*np.pi*np.cumsum(420*np.exp(-t*1.6))/SR)*(.6+.4*np.sin(2*np.pi*14*t))*np.exp(-t*3); put(fx,stall,E['stall'],.16)
t=t_(2.0); chime=sum(np.sin(2*np.pi*f*t)*np.exp(-t*(2+i)) for i,f in enumerate((1318.5,1975.5,2637,3951)))/2.5; put(fx,chime,E['outro_word'],.3)
def save(name,x,peak=.9):
    x=x/ max(1e-9,np.abs(x).max())*peak; wavfile.write(name,SR,(x*32767).astype(np.int16))
save('music.wav',mus,.9); save('sfx.wav',fx,.9)
print('ok',T)
