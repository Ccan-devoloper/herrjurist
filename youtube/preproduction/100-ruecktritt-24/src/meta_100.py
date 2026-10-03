"""Nachbearbeitung der Upload-Texte für Folge 100 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_100.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Der Hebel am Küchenfenster"),
       (T("p24"), "§ 24 Abs. 1 StGB im Wortlaut"), (T("vers"), "Zuerst der Versuch (Folge 97)"),
       (T("rt"), "IV. 1. Kein fehlgeschlagener Versuch"), (T("rt2"), "IV. 2. Unbeendet oder beendet?"),
       (T("rh"), "IV. 3. Rücktrittshandlung"), (T("fw"), "IV. 4. Freiwilligkeit"),
       (T("zwei"), "Mehrere Beteiligte und Ergebnis"), (T("tipp"), "Klausurtipp: vollendete Delikte bleiben"),
       (T("sch"), "Klausurschema Rücktritt"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Rücktritt vom Versuch nach § 24 I StGB: Fehlschlag, beendeter oder unbeendeter Versuch, Rücktrittshandlung und Freiwilligkeit – das komplette Schema. Am Fall eines Einbrechers, der den Hebel schon am Fenster hat und dann nach Hause geht.

Der Fall: Heiner will in die Erdgeschosswohnung von Annegret einbrechen und stehlen. Er setzt einen Hebel am Küchenfenster an, im Rahmen bleibt eine tiefe Delle. Dann bekommt er Gewissensbisse, steckt den Hebel ein und geht nach Hause. Ist Heiner strafbar?

Inhalt:
– § 24 Abs. 1 Satz 1 und 2 StGB im Wortlaut
– Versuch in Kürze (wie in Folge 97): unmittelbares Ansetzen, wenn das Einbruchswerkzeug schon angesetzt ist
– IV. 1. Kein fehlgeschlagener Versuch
– IV. 2. Unbeendet oder beendet nach dem Rücktrittshorizont, Korrektur in engen zeitlichen Grenzen
– IV. 3. Rücktrittshandlung: Aufgeben (S. 1 Alt. 1), Verhindern (S. 1 Alt. 2), ernsthaftes Bemühen (S. 2)
– IV. 4. Freiwilligkeit: Herr seiner Entschlüsse, autonome und heteronome Motive, kein sittlich billigenswertes Motiv nötig
– § 24 Abs. 2 StGB bei mehreren Beteiligten (kurz)
– Ergebnis: straflos wegen des versuchten Wohnungseinbruchdiebstahls, strafbar bleibt die vollendete Sachbeschädigung (§ 303 StGB)
– Klausurtipp, Klausurschema, Merksatz

Normen: § 24 Abs. 1 und 2 StGB; §§ 242, 244 Abs. 1 Nr. 3, Abs. 4, 22, 23 Abs. 1 StGB; § 303 StGB

Rechtsprechung:
– BGH, Beschl. v. 28.4.2020 – 5 StR 15/20 (BGHSt 65, 15), Rn. 7 f. (Versuchsbeginn beim Einbruch)
– BGH, Beschl. v. 27.4.2022 – 4 StR 408/21, Rn. 5 f. (Fehlschlag, unbeendeter und beendeter Versuch, Rücktrittshorizont)
– BGH, Beschl. v. 14.1.2020 – 2 StR 284/19, Rn. 8 f. (Freiwilligkeit, kein sittlich billigenswertes Motiv nötig)
– BGH, Urt. v. 17.3.2022 – 4 StR 223/21, Rn. 21 (persönlicher Strafaufhebungsgrund)
– BGH, Urt. v. 14.2.1996 – 3 StR 445/95 (BGHSt 42, 43), Rn. 7 (vollendetes Delikt bleibt trotz Rücktritt strafbar)

Hinweise: Das Begriffspaar „autonom/heteronom“ und der Aufbau mit dem Rücktritt als Punkt IV. sind Klausurkonvention (Lehrbuchstandard). Die Sachbeschädigung wird nach § 303c StGB grundsätzlich nur auf Antrag verfolgt.

Mehr dazu: Folge 97 (Versuch Schema), Folge 51 (Diebstahl Schema).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026 (StGB zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Rücktritt #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
for a, b in [("§ 24, Abs. 1:", "§ 24 Abs. 1:"), ("Und S. 2:", "Und Satz 2:"), ("Privatwohnung vor, § 244,", "Privatwohnung vor, § 244"),
             ("aufzugeben, S. 1,", "aufzugeben, Satz 1,"), ("\nAlt. 1. Beim", "\nerste Alternative. Beim"), ("die Alt. 2.", "die zweite Alternative."),
             ("nach S. 2 sein", "nach Satz 2 sein"), ("§ 24, Abs. 1.", "§ 24 Abs. 1.")]:
    assert a in srt, a
    srt = srt.replace(a, b)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
