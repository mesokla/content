# Minimal soft bed: electric-piano arpeggio + warm pad, no drums, no sfx.
import json, numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile
SR=44100; E=json.load(open('events.json')); T=E['T']; N=int(SR*(T+2)); rng=np.random.default_rng(3)
t_=lambda d: np.arange(int(SR*d))/SR
lp=lambda x,f: sosfilt(butter(2,f,btype='low',fs=SR,output='sos'),x,axis=0)
note=lambda m:440*2**((m-69)/12)
def put(buf,x,at,g):
    i=int(at*SR); j=min(len(buf),i+len(x))
    if i<len(buf): buf[i:j]+=x[:j-i]*g
BPM=84; beat=60/BPM; bar=4*beat
PROG=[[57,60,64,67],[53,57,60,64],[48,55,60,64],[55,59,62,67]]   # Am7 Fmaj7 C(add9) G
L=np.zeros(N); R=np.zeros(N)
def epiano(f,d=2.2):
    t=t_(d); x=np.sin(2*np.pi*f*t)+.35*np.sin(2*np.pi*2*f*t)*np.exp(-t*4)+.08*np.sin(2*np.pi*3*f*t)*np.exp(-t*8)
    a=int(.005*SR); e=np.exp(-t*1.6); e[:a]*=np.linspace(0,1,a); return x*e
def pad(fs,d):
    t=t_(d); x=sum(np.sin(2*np.pi*f*t+rng.random()*6)+.3*np.sin(2*np.pi*2.003*f*t) for f in fs)
    e=np.minimum(1,t/1.2)*np.minimum(1,(d-t)/1.2); return lp(x*e,900)
k=0; tt=0.0
while tt<T:
    ch=PROG[k%4]
    p=pad([note(m-12) for m in ch[:3]],bar+1.2); put(L,p,tt,.05); put(R,p,tt+.012,.05)
    pattern=[0,2,1,3,2,1,3,2]
    for i,s in enumerate(pattern):
        m=ch[s]+12; x=epiano(note(m)); pan=.3 if i%2 else -.3
        put(L,x,tt+i*beat/2,.06*(1-pan)); put(R,x,tt+i*beat/2,.06*(1+pan))
    tt+=bar; k+=1
mix=np.stack([L,R],1)
ir_n=int(2.2*SR); ir=rng.standard_normal((ir_n,2))*np.exp(-np.linspace(0,6,ir_n))[:,None]; ir=lp(ir,5000)
wet=np.stack([fftconvolve(mix[:,c],ir[:,c])[:N] for c in range(2)],1); wet*=np.abs(mix).max()/(np.abs(wet).max()+1e-9)
mix=mix+wet*.35
f=int(1.5*SR); mix[:f]*=np.linspace(0,1,f)[:,None]
end=int(T*SR); mix=mix[:end]; fo=int(3*SR); mix[-fo:]*=np.linspace(1,0,fo)[:,None]**1.5
wavfile.write('music_min.wav',SR,(mix/np.abs(mix).max()*.9*32767).astype(np.int16)); print('ok',T)
