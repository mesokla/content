# Epic music bed + attention-holding sfx (no knocks/ticks), stereo, timed from events.json.
import json, numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile
SR=44100; E=json.load(open('events.json')); T=E['T']; O=E['O']
N=int(SR*(T+1.0)); rng=np.random.default_rng(11)
def t_(d): return np.arange(int(SR*d))/SR
def flt(x,kind,f,o=2): return sosfilt(butter(o,f,btype=kind,fs=SR,output='sos'),x,axis=0)
def env(n,a,r,hold=None):
    e=np.ones(n); A=max(1,int(a*SR)); R=max(1,min(n-A,int(r*SR)))
    e[:A]=np.linspace(0,1,A)**1.5; e[-R:]*=np.linspace(1,0,R)**2; return e
def st(x,pan=0.0,w=0.0):
    """mono -> stereo with pan (-1..1) and tiny haas width"""
    L=x*np.sqrt((1-pan)/2); R=x*np.sqrt((1+pan)/2)
    if w>0: R=np.concatenate([np.zeros(int(w*SR)),R])[:len(x)]
    return np.stack([L,R],1)
def put(buf,x,at,g=1.0):
    if x.ndim==1: x=st(x)
    i=int(at*SR)
    if i<0: x=x[-i:]; i=0
    j=min(len(buf),i+len(x))
    if i<len(buf): buf[i:j]+=x[:j-i]*g
IR_len=int(2.6*SR); ir=rng.standard_normal((IR_len,2))*np.exp(-np.linspace(0,7,IR_len))[:,None]; ir=flt(ir,'low',6000)
def verb(x,mix=.3):
    w=np.stack([fftconvolve(x[:,c],ir[:,c])[:len(x)] for c in range(2)],1); w/=np.abs(w).max()+1e-9
    return x+w*mix*np.abs(x).max()
note=lambda m:440*2**((m-69)/12)
BPM=120; beat=60/BPM; bar=4*beat
PROG=[(45,[57,60,64,69]),(41,[53,57,60,65]),(48,[55,60,64,67]),(43,[55,59,62,67])]  # Am F C G
# ---------------- music ----------------
pad=np.zeros((N,2)); bass=np.zeros((N,2)); arp=np.zeros((N,2)); drums=np.zeros((N,2)); lead=np.zeros((N,2))
def saw(f,t,phase=0): return 2*((f*t+phase)%1)-1
def supersaw(freqs,d):
    t=t_(d); L=np.zeros_like(t); R=np.zeros_like(t)
    for f in freqs:
        for k,det in enumerate((-.012,-.006,0,.006,.012)):
            v=saw(f*(1+det),t,rng.random())
            if k%2: L+=v
            else: R+=v
    x=np.stack([L,R],1); x=flt(x,'low',2400); return x*env(len(t),.25,.6)[:,None]
start_full=O; k=0; tt=0.0
while tt<T+bar:
    root,ch=PROG[k%4]
    g=0.5 if tt<start_full-0.01 else 1.0
    put(pad,supersaw([note(m) for m in ch],bar+.6),tt,.035*g)
    if tt>=start_full-0.01:
        for e8 in range(8):                        # pulsing bass, pumped
            t=t_(beat/2); b=flt(saw(note(root),t),'low',520)+np.sin(2*np.pi*note(root-12)*t)*.8
            pump=np.minimum(1,(t/(beat/2))**.6)*np.exp(-t*2.5)
            put(bass,b*pump,tt+e8*beat/2,.20)
        for s16 in range(16):                      # arp 16ths, ping-pong
            m=[ch[0],ch[2],ch[1]+12,ch[3],ch[2]+12,ch[1],ch[3]+12,ch[2]][s16%8]
            t=t_(.32); x=np.sign(np.sin(2*np.pi*note(m+12)*t))*.5+np.sin(2*np.pi*note(m+12)*t)*.5
            x=flt(x,'low',3200)*np.exp(-t*11)
            put(arp,st(x,-.5 if s16%2 else .5),tt+s16*beat/4,.045)
        for b4 in (0,2):                           # soft deep kick, no click
            t=t_(.45); f=40+38*np.exp(-t*18); kx=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*6)
            put(drums,flt(kx,'low',150),tt+b4*beat,.55)
        for s16 in range(16):                      # light hats
            t=t_(.06 if s16%4!=2 else .18); h=flt(rng.standard_normal(len(t)),'high',8000)*np.exp(-t*(70 if s16%4!=2 else 22))
            put(drums,st(h,.25 if s16%2 else -.25),tt+s16*beat/4,.035 if s16%4!=2 else .05)
        if k%4==0:                                 # 4-note hook every 4 bars
            for i,(m,dur) in enumerate([(69,1),(72,1),(76,1.5),(74,.5)]):
                t=t_(beat*dur+.3); x=(saw(note(m),t)*.4+np.sin(2*np.pi*note(m)*t))*env(len(t),.02,.3)
                put(lead,st(flt(x,'low',2800),0,.012),tt+i*beat,.04)
    tt+=bar; k+=1
mus=verb(pad,.35)+bass+verb(arp,.25)+drums+verb(lead,.35)
# intro swell + outro: fade
fade=np.ones(N); fi=int(SR*O); fade[:fi]=np.linspace(.15,1,fi)**2
fo=int(SR*(T-2.8)); fade[fo:]=np.linspace(1,0,N-fo); mus*=fade[:,None]
# ---------------- sfx ----------------
fx=np.zeros((N,2))
PENTA=[69,72,74,76,79,81,84,86,88]
def bell(m,d=1.4,bright=1.0):
    t=t_(d); f=note(m); x=np.sin(2*np.pi*f*t)+.5*np.sin(2*np.pi*f*2.01*t)*np.exp(-t*3)+.25*np.sin(2*np.pi*f*3.98*t)*np.exp(-t*6)*bright
    return x*np.exp(-t*3.2)*env(len(t),.004,.2)
def riser(d,lo=300,hi=6000,g=1.0):
    n=int(d*SR); x=rng.standard_normal(n); out=np.zeros(n); blk=1024
    for i in range(0,n,blk):
        p=i/n; f=lo*(hi/lo)**p; out[i:i+blk]=flt(x[i:i+blk],'band',[f*.7,min(f*1.4,20000)],1)
    return out*np.linspace(0,1,n)**2.2*g
def impact():
    t=t_(2.4); f=58*np.exp(-t*.9)+28; sub=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*1.6)
    n=flt(rng.standard_normal(len(t)),'low',900)*np.exp(-t*5)*.6
    return verb(st(sub+n),.5)
def swoosh(d=.7):
    t=t_(d); n=rng.standard_normal(len(t)); m=np.sin(np.linspace(0,np.pi,len(t)))**2
    x=flt(n,'band',[400,2600])*m; return st(x,0,.015)
# intro: rising swell + sparkles following the moth + impact when the voice comes in
put(fx,st(riser(O,200,9000),0,.01),0,.5)
a,b=E['intro_fly']
for i in range(18):
    tt=a+(b-a)*(i/18)**.8; put(fx,st(bell(PENTA[(i*2)%len(PENTA)]+12,1.0),rng.uniform(-.6,.6)),tt,.05+.06*i/18)
put(fx,impact(),O-0.05,.9)
# scene changes: short riser into a soft swoosh
for w in E['wipe']:
    put(fx,st(riser(.7,500,5000)),w-.7,.22); put(fx,swoosh(),w-.15,.30)
# highlights: musical bell pings (in key), cards: airy swish + low bell
for i,h in enumerate(E['hl']): put(fx,verb(st(bell(PENTA[i%len(PENTA)]),.3*((i%2)*2-1)),.4),h,.16)
for c in E.get('card',[]): put(fx,swoosh(.5),c-.05,.22); put(fx,st(bell(57,1.6,.4)),c+.25,.10)
# counter: rising tone instead of ticks
if E.get('tick'):
    a0,a1=E['tick'][0],E['tick'][-1]; t=t_(a1-a0+.3); f=220*2**(t/(a1-a0)*1.0)
    x=np.sin(2*np.pi*np.cumsum(f)/SR)*np.linspace(0,1,len(t))*env(len(t),.05,.15); put(fx,verb(st(x),.3),a0,.10); put(fx,st(bell(81,1.5)),a1+.05,.18)
# stamp/tag: deep swell (no knock)
for p in E['pop']:
    t=t_(1.2); x=np.sin(2*np.pi*55*t)*np.exp(-t*2.5)*env(len(t),.03,.4); put(fx,st(x),p+.1,.45); put(fx,st(bell(64,1.2,.6)),p+.12,.10)
# stall: tape-stop on a tone
t=t_(.9); f=330*np.exp(-t*2.2); x=saw(1,0)*0+np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*2); put(fx,verb(st(flt(x,'low',2000)),.3),E['stall'],.14)
# outro: sparkles following the moth, then a final impact + chord bells
a,b=E['outro_fly']
for i in range(14): put(fx,st(bell(PENTA[(i*3)%len(PENTA)]+12,1.0),rng.uniform(-.6,.6)),a+(b-a)*i/14,.06)
put(fx,impact(),E['outro_word']-.05,.7)
for m in (57,64,69,72,76): put(fx,verb(st(bell(m,2.6,.5)),.4),E['outro_word'],.08)
def save(name,x,peak=.9):
    x=x/max(1e-9,np.abs(x).max())*peak; wavfile.write(name,SR,(x*32767).astype(np.int16))
save('music.wav',mus[:int(SR*T)]); save('sfx.wav',fx[:int(SR*T)])
print('ok',T)
