"""Original instrumental cue for this invitation; no third-party recordings."""
from pathlib import Path
import numpy as np
import wave

RATE=22050
BEAT=60/76
BARS=16
length=BARS*4*BEAT+3
audio=np.zeros(int(length*RATE),dtype=np.float64)

def note(midi,start,beats=1,level=.12,soft=False):
    duration=beats*BEAT+2.1
    t=np.arange(int(duration*RATE))/RATE
    hz=440*2**((midi-69)/12)
    env=(1-np.exp(-t/(.13 if soft else .012)))*np.exp(-t/(1.7 if soft else .85+beats*.18))
    release=np.minimum(1,(duration-t)/.3)
    tone=np.zeros_like(t)
    for partial,amp in [(1,1),(2,.28),(3,.11),(4,.035)]:
        tone+=amp*np.sin(2*np.pi*hz*partial*t+.0002*partial*np.sin(2*np.pi*1.7*t))*np.exp(-t*partial*.17)
    tone*=env*release*level
    at=int(start*RATE);end=min(len(audio),at+len(tone))
    audio[at:end]+=tone[:end-at]

# Dadd9 / A / Bm7 / Gmaj7: a warm, unhurried original homecoming theme.
chords=[(50,[62,66,69,76]),(45,[61,64,69,73]),(47,[62,66,69,74]),(43,[59,62,66,69])]
melodies=[[(0,74,1),(1.5,73,.5),(2,69,1.5)],[(.5,73,1),(2,76,1),(3,73,.75)],[(0,74,1.5),(2,78,1),(3,76,.75)],[(0,74,2),(2.5,71,1)],[(0,69,1),(1,74,1),(2.5,76,1)],[(0,73,1.5),(2,71,1),(3,69,.8)],[(.5,71,1),(2,74,1.5)],[(0,73,1),(1.5,71,.5),(2,69,1.5)]]
for bar in range(BARS):
    root,chord=chords[bar%4];base=bar*4*BEAT
    note(root,base,3.6,.105,True)
    for j,index in enumerate([0,1,2,3,2,1,3,1]):
        note(chord[index],base+j*.5*BEAT,.8,.035 if j%2 else .045)
    for offset,pitch,duration in melodies[bar%8]:
        note(pitch,base+offset*BEAT,duration,.115 if bar<8 else .13)
    if bar>=8:
        for pitch in chord[:3]:note(pitch-12,base,3.4,.014,True)
# A short room tail and slow fades keep the quiet loop comfortable.
dry=audio.copy()
for delay,gain in [(.091,.10),(.173,.08),(.287,.06),(.431,.035)]:
    shift=int(delay*RATE);audio[shift:]+=dry[:-shift]*gain
audio*=np.minimum(1,np.arange(len(audio))/(RATE*1.5))
audio*=np.minimum(1,(len(audio)-np.arange(len(audio)))/(RATE*3))
audio=.68*audio/max(abs(audio))
path=Path('dist/assets/homecoming-piano.wav')
with wave.open(str(path),'wb') as out:
    out.setnchannels(1);out.setsampwidth(2);out.setframerate(RATE)
    out.writeframes((audio*32767).astype('<i2').tobytes())
print(f'Original piano cue: {length:.1f}s; {path.stat().st_size/1024/1024:.2f} MB; peak {max(abs(audio)):.2f}')
