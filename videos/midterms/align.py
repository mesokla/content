from pocketsphinx import Decoder
import wave, json
txt=open('align.txt').read().split()
d=Decoder(samprate=16000,loglevel='ERROR')
oov=sorted({w for w in txt if d.lookup_word(w) is None})
print('OOV',oov)
PH={'fairshake':'F EH R SH EY K','pacs':'P AE K S','stablecoins':'S T EY B AH L K OY N Z','sceptical':'S K EH P T IH K AH L','crypto':'K R IH P T OW',
    "industry's":'IH N D AH S T R IY Z','sherrod':'SH EH R AH D','gridlock':'G R IH D L AA K'}
for w in oov:
    if w in PH: d.add_word(w,PH[w],True)
    else: print('missing',w)
data=wave.open('vo2_16k.wav').readframes(10**9)
d.set_align_text(' '.join(txt))
d.start_utt(); d.process_raw(data,full_utt=True); d.end_utt()
d.set_alignment(); d.start_utt(); d.process_raw(data,full_utt=True); d.end_utt()
out=[]
for seg in d.get_alignment():
    if seg.name in ('<s>','</s>','<sil>'): continue
    out.append({'w':seg.name,'s':round(seg.start/100,2),'e':round((seg.start+seg.duration)/100,2)})
json.dump(out,open('align.json','w'))
print(len(out)); print(' '.join(f"{o['w']}@{o['s']}" for o in out))
