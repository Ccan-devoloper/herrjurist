"""Gegenprobe zur Namensprüfung (Folge 240): Gruppenvergleich der Wiltrud-Nennungen (MFCC/DTW aus namen_240.py),
Gruppe H = Erkennung „Wildhut“, R = „Wiltrud/Wildrud“. Mittelwerte H-H, R-R, H-R; Aufruf nach namen_240.py."""
import json, sys, numpy as np, wave
sys.argv=[sys.argv[0],"x","y"]
src=open("namen_240.py").read().split("from faster_whisper")[0]
exec(src)
N=json.load(open("../out/namen.json"))
W=[e for e in N if e["name"]=="Wiltrud"]
cj=json.load(open("../cues.json"))
M=[mfcc(x[int((e["t"])*sr):int((e["t"]+e["dauer"])*sr)]) for e in W]
lab=["H" if "hut" in (e["asr_satz"]+e["asr_isoliert"]).lower() else "R" for e in W]
D=np.array([[dtw(a,b) if i!=j else np.nan for j,b in enumerate(M)] for i,a in enumerate(M)])
for i,e in enumerate(W): print(e["video"],lab[i]," ".join(f"{v:4.2f}" if v==v else " -- " for v in D[i]))
H=[i for i in range(len(W)) if lab[i]=="H"]; R=[i for i in range(len(W)) if lab[i]=="R"]
inn=[D[i,j] for i in H for j in H if i!=j]; quer=[D[i,j] for i in H for j in R]; rr=[D[i,j] for i in R for j in R if i!=j]
print("H-H",np.mean(inn).round(3),"R-R",np.mean(rr).round(3),"H-R",np.mean(quer).round(3))
# Dauer des r-Lautbereichs: Energie im mittleren Drittel
for e in W:
    y=x[int(e["t"]*sr):int((e["t"]+e["dauer"])*sr)]
    print(e["video"], "Dauer", e["dauer"])
