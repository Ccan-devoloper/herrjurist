"""Cue-Timeline für das Ton-Bild-Gate: je Bildhalt (aus ../bildhalt_manifest.json) eine Zeile mit Zeitfenster,
hörbarem Sprecher, gesprochenem Text (ElevenLabs-Wortzeiten) und Prüfpfad. Ausgabe ../CUE-TIMELINE.md.
Zeiten beziehen sich auf den Hauptfilm; im fertigen Video kommen 8,000 s Intro hinzu."""
import json

cj = json.load(open("../cues.json"))
man = json.load(open("../bildhalt_manifest.json"))
woerter = [(a, b, w, s["rolle"] or "Carla (Erzählerin/Lexi)") for s in cj["segmente"] for w, (a, b) in zip(s["text"].split(), s["woerter"])]


def mmss(t):
    return f"{int(t // 60)}:{t % 60:05.2f}"


zeilen = ["# Folge 087 · Cue-Timeline (Ton-Bild-Gate)", "",
          f"Quelle: `bildhalt_manifest.json` ({man['bildhalte']} Bildhalte, davon {man['eigenstaendig']} eigenständig), "
          "`cues.json` (ElevenLabs-Wortzeiten). Zeiten im Hauptfilm, im fertigen Video jeweils +8,000 s (Intro). "
          "Die Wortzeiten stammen aus der tatsächlich verwendeten Sprachspur; die Startpunkte von Bild, Tafel und Pfad sind "
          "an diese Wortgrenzen gebunden (`beim()` im Folienskript).", "",
          "| Nr. | Start | Ende | Sprecher | gesprochen (Wortgrenzen) | Prüfpfad | SHA-256 (Keyframe) |", "|---:|---|---|---|---|---|---|"]
for h in man["halte"]:
    ws = [(w, r) for a, b, w, r in woerter if a < h["ende"] and b > h["start"]]
    sprecher = " / ".join(dict.fromkeys(r for _, r in ws)) or "– (Pause)"
    text = " ".join(w for w, _ in ws)
    if len(text) > 110:
        text = text[:107] + " …"
    zeilen.append(f"| {h['nr']} | {mmss(h['start'])} | {mmss(h['ende'])} | {sprecher} | {text.replace('|', '/')} | "
                  f"{h['pruefpfad']} | `{h['sha256'][:12]}` |")
open("../CUE-TIMELINE.md", "w").write("\n".join(zeilen) + "\n")
print(len(man["halte"]), "Zeilen -> ../CUE-TIMELINE.md")
