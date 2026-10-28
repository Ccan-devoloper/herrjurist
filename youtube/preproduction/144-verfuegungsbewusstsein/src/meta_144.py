"""Nachbearbeitung der Upload-Texte für Folge 144 (nach tools/youtube_metadaten.py, nichts dort geändert; Muster meta_140.py):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Fundstelle, Hinweisen und
Lizenzzeile; Beträge, Jahreszahlen und Gliederungsziffern in den Untertiteln als Ziffern; Aussprachehilfe „Weck-nahme“
in den Untertiteln zurück in die Schreibung „Wegnahme“.
Aufruf: python3 meta_144.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Kopfhörer in der Waschmittelpackung, Sachverhalt"),
       (T("abgr"), "Abgrenzung Diebstahl und Betrug: Nehmen oder Geben"),
       (T("p242"), "Wortlaut § 242 und § 263 StGB"),
       (T("kern"), "Kernfrage: Verfügungsbewusstsein (BGHSt 41, 198)"),
       (T("gegen"), "Gegenansicht: generelles Verfügungsbewusstsein"),
       (T("wegn"), "Subsumtion: Diebstahl, § 242 StGB"),
       (T("gv"), "Gegenvariante: Etikettentausch – Sachbetrug"),
       (T("tipp"), "Klausurtipp: Aufbau"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Verfügungsbewusstsein beim Sachbetrug: Wer Ware an der Kasse versteckt – Diebstahl nach § 242 oder Betrug nach § 263 StGB?

Der Fall: Fabian versteckt im Supermarkt Kopfhörer für 120 € in einer Waschmittelpackung und verschließt sie wieder. An der Kasse scannt Kassiererin Carina nur das Waschmittel für 8 €; Fabian zahlt und verlässt mit der Packung samt Kopfhörern den Laden. Hat Carina mit der Packung auch über die Kopfhörer verfügt?

Inhalt:
– Abgrenzung: Diebstahl und Betrug schließen sich für dieselbe Sache aus; eigenmächtiges Nehmen oder getäuschtes Geben
– § 242 Abs. 1 und § 263 Abs. 1 StGB im Wortlaut; die ungeschriebene Vermögensverfügung
– Kernfrage: Verfügungsbewusstsein beim Sachbetrug – der Kassierer verfügt über die vorgelegten, eingetippten Waren
– Gegenansicht: generelles Verfügungsbewusstsein; Argumente des BGH (bloße Fiktion, Nachfrage an der Kasse, § 252 StGB)
– Subsumtion: Gewahrsamsbruch ohne Einverständnis, Ergebnis Diebstahl
– Gegenvariante: Preisetikett ausgetauscht, Ware offen vorgelegt – Sachbetrug
– Klausurtipp zum Aufbau, Prüfschema, Merksatz

Normen: §§ 242, 263 StGB (Wertungsargument § 252 StGB)

Rechtsprechung:
– BGH, Beschl. v. 26.7.1995 – 4 StR 234/95 (BGHSt 41, 198), S. 201–204: versteckte Ware im Einkaufswagen regelmäßig Diebstahl, nicht Betrug; Verfügungswille konkretisiert sich durch das Eintippen der vorgelegten Waren; genereller Verfügungswille „bloße Fiktion“
– Gegenposition: OLG Düsseldorf, Beschl. v. 17.11.1992, NJW 1993, 1407 (nach der Wiedergabe in BGHSt 41, 198)
– BGH, Urt. v. 12.10.2016 – 1 StR 402/16, Rn. 11 (Abgrenzung Trickdiebstahl/Betrug nach der Willensrichtung des Getäuschten)

Hinweise: Der Fall ist ein vereinfachter Übungsfall. Der BGH entschied über Ware im Einkaufswagen und behielt Ausnahmen vor; für Ware in einer verschlossenen Verpackung wird die Gegenansicht (Verfügung über die Packung samt Inhalt) vertreten – in der Klausur den Streit benennen. Wann genau der Diebstahl vollendet ist, hängt vom Einzelfall ab (siehe unsere Folge zur Gewahrsamsenklave); das Betrugsschema zeigt unsere Folge zu § 263 StGB.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (StGB zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Verfügungsbewusstsein #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for a, b in [("Weck-nahme", "Wegnahme"), ("hundertzwanzig Euro", "120 Euro"), ("Acht Euro", "8 Euro"), ("acht Euro", "8 Euro"),
             ("neunzehnhundertzweiundneunzig", "1992"), ("neunzehnhundertfünfundneunzig", "1995"),
             ("Römisch eins,", "I."), ("Römisch zwei,", "II.")]:
    srt = srt.replace(a, b)
srt = re.sub(r"[ \t]+\n", "\n", srt)
srt = re.sub(r"\n[ \t]+", "\n", srt)
assert not re.search(r"Römisch|hundert|Paragraf|Weck|\bacht\b", srt), re.findall(r".*(?:Römisch|hundert|Paragraf|Weck|\bacht\b).*", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
