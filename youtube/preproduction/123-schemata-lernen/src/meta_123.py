"""Nachbearbeitung der Upload-Texte für Folge 123 (Kopie von meta_117.py) (nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Rahmen, Inhalt, Quellenhinweisen und Lizenzzeile;
Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_123.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: 80 Schemata und trotzdem gescheitert (Handy auf dem Gehweg)"),
       (T("w1"), "Werkzeug 1: Das Schema als Landkarte (§ 242 StGB)"),
       (T("fall1"), "Werkzeug 1 am Fall: keine Wegnahme"),
       (T("w2"), "Werkzeug 2: Warum ist die Zueignung subjektiv?"),
       (T("w2c"), "Werkzeug 2: entstanden, untergegangen, durchsetzbar"),
       (T("w3"), "Werkzeug 3: § 246 StGB aus dem Wortlaut bauen"),
       (T("t5"), "Werkzeug 3 am Fall: Unterschlagung"),
       (T("m2"), "Lernen mit Fällen statt Listen"),
       (T("tipp"), "Klausurtipp: kein Schema? Die Norm lesen"),
       (T("sch"), "Klausurschema Unterschlagung"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Prüfungsschemata lernen, ohne stumpf auswendig zu pauken: Wie du Schemata verstehst, dir merkst und auf unbekannte Fälle überträgst.

Der Rahmen: Gunnar kann 80 Schemata auswendig – und scheitert im Tutorium an einem Fall, der auf keiner Karteikarte steht: Ein Spaziergänger findet nachts ein verlorenes Handy auf dem Gehweg und behält es. Die Tutorin Marlene zeigt drei Werkzeuge.

Inhalt:
– Werkzeug 1: Das Schema als Landkarte des Gesetzes – jeder Prüfungspunkt kommt aus einem Wort (Wortlaut § 242 Abs. 1 StGB, Vorsatz aus § 15 StGB)
– Am Fall: kein Gewahrsam der Eigentümerin, also keine Wegnahme und kein Diebstahl
– Werkzeug 2: Warum steht der Punkt hier? Zueignungsabsicht im subjektiven Tatbestand; entstanden – untergegangen – durchsetzbar (§§ 362, 214 BGB)
– Werkzeug 3: Ein unbekanntes Schema aus dem Wortlaut bauen – § 246 StGB neben § 242 StGB; die Zueignung wird objektiv
– Am Fall: Unterschlagung, § 246 Abs. 1 StGB
– Lernen mit Fällen statt Listen, Klausurtipp, Klausurschema Unterschlagung, Merksatz

Rechtsprechung: BGH, Beschl. v. 3.3.2021 – 4 StR 338/20 (Wegnahme); BGH, Beschl. v. 14.4.2020 – 5 StR 10/20 (verlorenes Handy im öffentlichen Raum: kein Gewahrsam, Unterschlagung); BGH, Beschl. v. 10.10.2018 – 4 StR 591/17 (Zueignung kein objektives Merkmal des Diebstahls); BGH, Beschl. v. 29.11.2023 – 6 StR 191/23 und BGH, Beschl. v. 13.3.2024 – 4 StR 442/23 (Zueignung bei § 246, Senate uneinheitlich).

Lernforschung: Weinstein, Madan & Sumeracki, Teaching the science of learning, Cognitive Research: Principles and Implications 3 (2018), Art. 2 (Abrufen aus dem Gedächtnis und verteiltes Wiederholen). Die Schritte „Schema aus dem Kopf, Fehler notieren, wiederholen“ sind eine Erfahrungsregel, keine Studie.

Hinweise: Der Übungsfall ist erfunden. Das Diebstahlschema vertieft Folge 051, Einwendungen und Einreden Folge 103, typische Klausurfehler Folge 117.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Jurastudium #Lernmethoden #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace("Weck-nahme", "Wegnahme")                      # Aussprachehilfe (synth_el) zurückführen
srt = srt.replace("STPO", "StPO").replace("STGB", "StGB")          # Großschreibung des Werkzeugs zurückführen
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
