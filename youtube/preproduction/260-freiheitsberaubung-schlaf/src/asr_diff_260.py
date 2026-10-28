"""Wortweiser Abgleich Skript ↔ Spracherkennung (whisper small und medium je Segment, aus asr_seg_260.py).
Gibt je Segment die abweichenden Stellen aus (difflib), mit Videozeit des Segmentstarts (+8,0 s).
Aufruf: python3 asr_diff_260.py ../out/asr_small.json ../out/asr_medium.json"""
import difflib, json, re, sys

cj = json.load(open("../cues.json"))
norm = lambda t: [w for w in re.sub(r"[^\wäöüß ]", " ", t.lower().replace("-", " ")).split() if w]
erg = [json.load(open(p)) for p in sys.argv[1:]]
for i, s in enumerate(cj["segmente"]):
    a = norm(re.sub(r"\[\w+\]", "", s["text"]))
    zeilen = []
    for e in erg:
        b = norm(e["segmente"][i]["erkannt"])
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b).get_opcodes():
            if op != "equal":
                zeilen.append(f"  [{e['modell']}] {' '.join(a[i1:i2])!r} -> {' '.join(b[j1:j2])!r}")
    if zeilen:
        print(f"Segment {i + 1} ({s['rolle'] or 'Carla'}, Video {s['start'] + 8:.1f} s):")
        print("\n".join(zeilen))
