"""Vergleicht die segmentweise Spracherkennung (asr_seg_220.py) mit dem Sprechtext je Segment (Wortebene, difflib).
Aufruf: python3 asr_diff_220.py ../out/asr_small_220.json > ../out/asr_small_diff.log"""
import difflib, json, re, sys
d = json.load(open(sys.argv[1]))
cj = json.load(open("../cues.json"))
norm = lambda t: [w for w in re.sub(r"[^\wäöüß ]", " ", t.lower()).split()]
gesamt = gleich = 0
for s, c in zip(d["segmente"], cj["segmente"]):
    a, b = norm(c["text"]), norm(s["erkannt"])
    sm = difflib.SequenceMatcher(None, a, b)
    gesamt += len(a); gleich += sum(m.size for m in sm.get_matching_blocks())
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            print(f"Seg {s['nr']:2d} ({s['rolle'] or 'Carla'}) t≈{c['start'] + 8.0:6.1f}s Video: {' '.join(a[i1:i2])!r} -> {' '.join(b[j1:j2])!r}")
print(f"Wortgleichheit {gleich}/{gesamt} = {100 * gleich / gesamt:.1f} %")
