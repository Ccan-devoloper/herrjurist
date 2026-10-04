"""Nachbearbeitung der Upload-Texte für Folge 156 (nach meta_152.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung (Normen ergänzt), Fall, Inhalt,
Normen, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Normzitate, Zahlen in Ziffern).
Aufruf: python3 meta_156.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Kurt stirbt ohne Testament, Sachverhalt"),
       (T("baum"), "Der Stammbaum der Familie"),
       (T("p1922"), "§ 1922 BGB: Gesamtrechtsnachfolge"),
       (T("ord"), "Die Ordnungen: §§ 1924–1926 BGB"),
       (T("p1930"), "§ 1930 BGB: Warum der Bruder nichts erbt"),
       (T("inn"), "Repräsentationsprinzip, § 1924 Abs. 2 BGB"),
       (T("p3"), "Eintrittsrecht und Erbfolge nach Stämmen, § 1924 Abs. 3, 4 BGB"),
       (T("ehe"), "Ehegattenerbrecht, § 1931 Abs. 1 BGB"),
       (T("abs3"), "Zugewinngemeinschaft: plus ein Viertel, § 1371 Abs. 1 BGB"),
       (T("erg"), "Ergebnis: 1/2, 1/4, 1/4 mit Gegenprobe"),
       (T("guet"), "Variante Gütertrennung, § 1931 Abs. 4 BGB"),
       (T("tipp"), "Klausurtipp: Ehegattenquote zuerst"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Gesetzliche Erbfolge (§§ 1922, 1924–1931, 1371 BGB): Ordnungen, Stämme, Repräsentation und Eintritt – wer erbt, wenn der Vater ohne Testament stirbt?

Der Fall: Kurt stirbt mit 78 Jahren ohne Testament. Zurück bleiben seine Frau Christa, mit der er im gesetzlichen Güterstand der Zugewinngemeinschaft lebte, die Tochter Verena mit ihrer kleinen Tochter Mathilda und der Enkel Severin, dessen Vater Andreas schon vor Kurt gestorben ist. Auch Egbert, der Bruder von Kurt, fragt, ob er etwas bekommt.

Inhalt:
– Gesamtrechtsnachfolge: § 1922 Abs. 1 BGB im Wortlaut
– Die Ordnungen: § 1924 Abs. 1 BGB im Wortlaut (Abkömmlinge), zweite und dritte Ordnung (§§ 1925, 1926 BGB)
– Ausschluss entfernterer Ordnungen: § 1930 BGB im Wortlaut – warum der Bruder nichts erbt
– Repräsentationsprinzip (§ 1924 Abs. 2 BGB) und Eintrittsrecht (§ 1924 Abs. 3 BGB) im Wortlaut, Erbfolge nach Stämmen und gleiche Teile (§ 1924 Abs. 4 BGB)
– Ehegattenerbrecht: § 1931 Abs. 1 S. 1 BGB im Wortlaut, Erhöhung um ein Viertel bei Zugewinngemeinschaft (§ 1931 Abs. 3, § 1371 Abs. 1 BGB)
– Ergebnis als Bruch-Diagramm: Ehefrau 1/2, Tochter 1/4, Enkel 1/4 – mit Gegenprobe
– Variante Gütertrennung (§ 1931 Abs. 4 BGB): je 1/3
– Klausurtipp (Ehegattenquote zuerst, Erbengemeinschaft § 2032 BGB), Prüfschema, Merksatz

Normen: §§ 1922, 1924, 1925, 1926, 1930, 1931, 1371, 2032 BGB

Hinweise: Die Erhöhung nach § 1371 Abs. 1 BGB gilt, wenn der überlebende Ehegatte Erbe wird; schlägt er aus, gelten § 1371 Abs. 2, 3 BGB (güterrechtliche Lösung) – nicht Gegenstand des Videos. Die Variante zur Gütertrennung gilt nach § 1931 Abs. 4 BGB nur neben einem oder zwei Kindern. Wie ein Testament die gesetzliche Erbfolge verdrängt, zeigt die Folge zum Berliner Testament.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Erbrecht #GesetzlicheErbfolge #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

# --- Untertitel -------------------------------------------------------------------------------------------------------
srt = open(f"{U}/untertitel.srt").read()
bl = [b.split("\n") for b in srt.strip().split("\n\n")]
cues = [[b[1], "\n".join(b[2:])] for b in bl]
# „§ 2000 / zweiunddreißig.“ über zwei Untertitel: zusammenführen
for i, (z, t) in enumerate(cues):
    if t.endswith("§ 2000") and cues[i + 1][1].strip() == "zweiunddreißig.":
        cues[i][1] = t[:-len("§ 2000")] + "§ 2032."
        cues[i][0] = z.split(" --> ")[0] + " --> " + cues[i + 1][0].split(" --> ")[1]
        del cues[i + 1]
        break
else:
    raise AssertionError("§ 2032 nicht gefunden")
srt = "\n\n".join(f"{k + 1}\n{z}\n{t}" for k, (z, t) in enumerate(cues)) + "\n"
srt = re.sub(r"Römisch (eins|zwei|drei|vier|fünf):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV.", "fünf": "V."}[m.group(1)] + m.group(2), srt)
for muster, ersatz in [(r"achtundsiebzig(\s)Jahren", r"78\1Jahren"), (r"vor drei Jahren", "vor 3 Jahren"),
                       (r"§§ 1924 bis 1930", "§§ 1924–1930")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "tausend" not in srt and "Römisch" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen;", len(cues), "Untertitel")
