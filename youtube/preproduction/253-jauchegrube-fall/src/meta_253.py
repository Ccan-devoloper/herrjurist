"""Nachbearbeitung der Upload-Texte für Folge 253 (nach meta_250.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Randnummern, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt).
Aufruf: python3 meta_253.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Streit am Gartenzaun"),
       (T("frage"), "Die Frage"),
       (T("echt"), "Der echte Jauchegrube-Fall (BGHSt 14, 193)"),
       (T("zwei"), "Das Problem: zwei Akte"),
       (T("obj"), "Objektiver Tatbestand"),
       (T("p16"), "Vorsatz: § 16 StGB und Kausalverlauf"),
       (T("dg"), "1. dolus generalis"),
       (T("bgh"), "2. BGH: unwesentliche Abweichung"),
       (T("vers"), "3. Versuchslösung und 4. Tatplan"),
       (T("erg"), "Ergebnis im Fall"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Jauchegrube-Fall (BGHSt 14, 193): Für tot gehalten und erst dann getötet – dolus generalis oder Versuch plus Fahrlässigkeit (§ 16 StGB)?

Der Fall: Brunhilde greift im Streit am Gartenzaun ihre Nachbarin an und nimmt deren Tod in Kauf. Sie hält die Regungslose für tot und versenkt sie im Teich – erst dort stirbt die Nachbarin. Vollendeter Totschlag oder nur Versuch und fahrlässige Tötung?

Inhalt:
– Der echte Jauchegrube-Fall des BGH von 1960 (kurz)
– Das Problem: zweiaktiges Geschehen; Kausalität und objektive Zurechnung
– § 16 Abs. 1 Satz 1 StGB im Wortlaut; Vorsatz bei der Tathandlung und Vorsatz bezüglich des Kausalverlaufs
– Die Lösungen: 1. dolus generalis (historisch, vom BGH abgelehnt), 2. BGH: unwesentliche Abweichung vom vorgestellten Kausalverlauf, 3. Versuchslösung der Lehre (versuchter Totschlag und fahrlässige Tötung, § 222 StGB), 4. vermittelnd: Tatplan
– Ergebnis im Fall, Klausurtipp, Klausurschema, Merksatz

Normen: §§ 16 Abs. 1, 22, 23, 212, 222 StGB.

Rechtsprechung:
– BGH, Urt. v. 26.4.1960 – 5 StR 77/60, BGHSt 14, 193 (Jauchegrube-Fall)
– BGH, Urt. v. 3.12.2015 – 4 StR 223/15, Rn. 10, 12 f. (HRRS 2016 Nr. 77; Formel zur unwesentlichen Abweichung)

Hinweise: Brunhilde und ihre Nachbarin sind erfundene Personen eines Übungsfalls, der dem echten Fall nachgebildet ist. Mordmerkmale bleiben offen. Mehr zum Irrtum über den Kausalverlauf in Folge 068.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com).

#JauchegrubeFall #StrafrechtAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in [("Folge achtundsechzig", "Folge 68")]:
    assert alt in srt, alt
    srt = srt.replace(alt, neu)
assert not re.search(r"achtundsechzig|neunzehnhundert|zweihundert|Paragraf", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Jauchegrubenfall", "Kausalverlauf", "Versuch", "fahrlässige Tötung"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
