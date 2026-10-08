"""Vergleich Skript ↔ Spracherkennung (whisper small und medium, je Segment) für Folge 279: Wortabweichungen je Segment,
markiert, ob beide Modelle dieselbe Abweichung hören. Aufruf: python3 asr_vergleich_279.py > ../out/asr_vergleich.log"""
import difflib, json, re
n = lambda t: [w for w in re.sub(r"[^\wäöüß ]", " ", t.lower().replace("-", " ")).split()]
cj = json.load(open("../cues.json"))
S = json.load(open("../out/asr_small_seg.json"))["segmente"]
M = json.load(open("../out/asr_medium_seg.json"))["segmente"]


def abw(ref, hyp):
    out = []
    for op, a, b, c, d in difflib.SequenceMatcher(None, ref, hyp, autojunk=False).get_opcodes():
        if op != "equal":
            out.append((a, " ".join(ref[a:b]), " ".join(hyp[c:d])))
    return out


for s, sm, md in zip(cj["segmente"], S, M):
    ref = n(s["text"])
    a_s, a_m = abw(ref, n(sm["erkannt"])), abw(ref, n(md["erkannt"]))
    beide = {(i, r) for i, r, _ in a_s} & {(i, r) for i, r, _ in a_m}
    print(f"== Segment {s['i'] + 1} ({s['rolle'] or 'Carla'}), Start {s['start']:.1f} s (Video {s['start'] + 8:.1f})")
    for i, r, h in a_s:
        print(f"  small : „{r}“ → „{h}“{'   [BEIDE]' if (i, r) in beide else ''}")
    for i, r, h in a_m:
        print(f"  medium: „{r}“ → „{h}“{'   [BEIDE]' if (i, r) in beide else ''}")
