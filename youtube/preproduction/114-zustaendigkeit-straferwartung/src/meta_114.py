"""Nachbearbeitung der Upload-Texte für Folge 114 (Kopie von meta_112.py) (nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_114.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Zwölf Anzahlungen, 40.000 Euro"),
       (T("akte"), "Bei der Staatsanwaltschaft: Welches Gericht?"),
       (T("plan"), "Sachliche und örtliche Zuständigkeit"),
       (T("st1"), "Die Treppe: Strafrichter, § 25 Nr. 2 GVG"),
       (T("st2"), "Schöffengericht, § 28 GVG, und Strafbann, § 24 Abs. 2 GVG"),
       (T("st3"), "Landgericht, § 24 Abs. 1 Satz 1 Nr. 2 und 3, § 74 GVG"),
       (T("st4"), "Sonderzuweisungen: Schwurgericht und OLG, § 120 GVG"),
       (T("e1"), "Straferwartung: Vergehen und Strafrahmen, § 263 StGB"),
       (T("e5"), "Regelbeispiel: gewerbsmäßig"),
       (T("e9"), "Vorstrafen und Gesamtstrafe, §§ 46, 53, 54 StGB"),
       (T("e12"), "Prognose und Ergebnis: Schöffengericht"),
       (T("o1"), "Örtliche Zuständigkeit, §§ 7, 8, 13 StPO"),
       (T("an1"), "Das Gericht in der Anklage"),
       (T("tipp"), "Klausurtipp: Straferwartung begründen"),
       (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Straferwartung Zuständigkeit: Wie die Staatsanwaltschaft nach §§ 24, 25, 28, 74 GVG und §§ 7 ff. StPO das richtige Gericht wählt und die Strafe realistisch prognostiziert.

Der Fall: Herr Hartung, zweimal wegen Betrugs vorbestraft, kassiert in Erlenstadt als angeblicher Terrassenbauer von zwölf Kunden Anzahlungen – zusammen 40.000 Euro. Gebaut wird nie, er lebt von dem Geld. Staatsanwältin Eggert muss entscheiden: Anklage zum Strafrichter, zum Schöffengericht oder zum Landgericht? Und welches Gericht ist örtlich zuständig?

Inhalt:
– Sachliche Zuständigkeit als Treppe: Strafrichter (§ 25 Nr. 2 GVG im Wortlaut), Schöffengericht (§ 28 GVG), Strafbann des Amtsgerichts (§ 24 Abs. 2 GVG), Landgericht (§ 24 Abs. 1 Satz 1 Nr. 2 GVG im Wortlaut, § 74 Abs. 1 GVG), besondere Bedeutung, Umfang, Schutzbedürftigkeit (Nr. 3), Sonderzuweisungen (Schwurgericht, OLG nach § 120 GVG)
– Straferwartung bilden: Vergehen auch im besonders schweren Fall (§ 12 Abs. 3 StGB), Strafrahmen § 263 Abs. 1 und 3 StGB, Regelbeispiel gewerbsmäßig, kein Vermögensverlust großen Ausmaßes (je Tat), Vorstrafen (§ 46 Abs. 2 StGB), Gesamtstrafe und Asperationsprinzip (§§ 53, 54 StGB)
– Prognose der Staatsanwältin und Ergebnis: Amtsgericht – Schöffengericht
– Örtliche Zuständigkeit: Tatort (§ 7 StPO), Wohnsitz (§ 8 StPO), Zusammenhang (§§ 3, 13 StPO)
– Das Gericht in der Anklageschrift (§ 200 Abs. 1 Satz 2 StPO, Nr. 110 Abs. 3 RiStBV)
– Klausurtipp (bewegliche Zuständigkeit, Nr. 113 RiStBV, § 209 StPO), Klausurschema, Merksatz

Normen: §§ 24, 25, 28, 74, 120 GVG; §§ 1, 3, 7, 8, 13, 200, 209 StPO; §§ 12, 46, 53, 54, 263 StGB; Nr. 110, 113 RiStBV

Rechtsprechung:
– BGH, Beschl. v. 14.4.2026 – 3 StR 556/25, Rn. 5 (Begriff der Gewerbsmäßigkeit)
– BGH, Urt. v. 24.6.2026 – 1 StR 247/25, Rn. 14 (großes Ausmaß für jede Tat gesondert, grundsätzlich 50.000 Euro; zu § 266a StGB unter Verweis auf § 263 Abs. 3 Satz 2 Nr. 2 StGB)
– BGH, Beschl. v. 6.10.2016 – 2 StR 330/16, Rn. 11, 17, 22 (Zuständigkeit bei Eröffnung; Straferwartung einschließlich Gesamtstrafe)
– BVerfG, Beschl. v. 1.3.2011 – 2 BvR 1/11, Rn. 13 (Begriff „bewegliche Zuständigkeit“)

Hinweise: Erlenstadt ist ein erfundener Ort. Die Spanne von zweieinhalb bis dreieinhalb Jahren ist die Prognose der Staatsanwältin im Fall, keine feste Regel. Die Formel „Anklage zum Amtsgericht – Schöffengericht – …“ ist Klausurkonvention. Folgefrage: Bei einer Hauptverhandlung vor dem Schöffengericht liegt ein Fall der notwendigen Verteidigung vor (§ 140 Abs. 1 Nr. 1 StPO). Das Gesamtschema der Anklageklausur erklärt Folge 039, den Betrug Folge 065.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Strafprozessrecht #Referendariat #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace("STPO", "StPO").replace("STGB", "StGB")          # Großschreibung des Werkzeugs zurückführen
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
