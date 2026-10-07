"""Nachbearbeitung der Upload-Texte für Folge 233 (nach meta_231.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Landesrecht-Hinweis,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt).
Aufruf: python3 meta_233.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Die Polizei löst die Demo auf"),
       (T("frage"), "Die Frage"),
       (T("va"), "Erledigung, § 43 Abs. 2 VwVfG"),
       (T("rweg"), "Statthaftigkeit: § 113 Abs. 1 Satz 4 VwGO"),
       (T("direkt"), "Direkt oder analog?"),
       (T("ffi"), "Fortsetzungsfeststellungsinteresse"),
       (T("reha"), "Rehabilitation und Präjudiz"),
       (T("tief"), "Tiefgreifender Grundrechtseingriff"),
       (T("kb"), "Klagebefugnis, Vorverfahren, Frist"),
       (T("begr"), "Begründetheit"),
       (T("mat"), "Materiell: milderes Mittel"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Fortsetzungsfeststellungsklage (§ 113 I 4 VwGO): Klagen nach Erledigung – direkte und analoge Anwendung, Fortsetzungsfeststellungsinteresse, klausurfertig.

Der Fall: Jördis leitet eine friedliche Demo für mehr Radwege. Ein einzelner Teilnehmer sprüht Farbe an eine Hauswand – die Polizei löst daraufhin die ganze Versammlung auf. Die Demo ist vorbei. Kann Jördis trotzdem klagen?

Inhalt:
– Erledigung des Verwaltungsakts: § 43 Abs. 2 VwVfG im Wortlaut
– Statthaftigkeit: § 113 Abs. 1 Satz 4 VwGO im Wortlaut; direkt bei Erledigung nach, entsprechend bei Erledigung vor Klageerhebung; Gegenansicht allgemeine Feststellungsklage; Verpflichtungssituation
– Fortsetzungsfeststellungsinteresse: Wiederholungsgefahr, Rehabilitation, Präjudiz (nur bei Erledigung nach Klageerhebung), tiefgreifender Grundrechtseingriff bei typischerweise kurzfristiger Erledigung (BVerwG 2024: beides nötig)
– Klagebefugnis analog § 42 Abs. 2 VwGO, Vorverfahren, Klagefrist (Streitstand)
– Begründetheit: Auflösung der Versammlung, milderes Mittel, Brokdorf
– Klausurtipp, Klausurschema, Merksatz

Normen: § 113 Abs. 1 Satz 4 VwGO; § 43 Abs. 2 VwVfG; §§ 40, 42 Abs. 2, 68, 74 VwGO; Art. 8 GG.

Landesrecht: Das Versammlungsrecht ist Ländersache. Beispiel im Video ist Nordrhein-Westfalen (§ 13 Abs. 2, § 14 Abs. 3, § 32 VersG NRW; Vorverfahren entfällt nach § 110 Abs. 1 Satz 1 JustG NRW). In Ländern ohne eigenes Versammlungsgesetz gilt § 15 Abs. 3 VersG des Bundes fort. In deinem Land können Normen und Vorverfahren abweichen.

Rechtsprechung:
– BVerwG, Urt. v. 16.5.2013 – 8 C 14.12, BVerwGE 146, 303, Rn. 20, 21, 25, 29–32, 44 (Fortsetzungsfeststellungsinteresse)
– BVerwG, Urt. v. 24.4.2024 – 6 C 2.22, Rn. 15–22 (qualifizierter Grundrechtseingriff bei kurzfristig erledigten Maßnahmen)
– BVerfG, Beschl. v. 3.3.2004 – 1 BvR 461/03, BVerfGE 110, 77, Rn. 37, 41–43 (Versammlungsauflösung)
– BVerwG, Urt. v. 4.12.2014 – 4 C 33.13, Rn. 13 (direkte und entsprechende Anwendung)
– OVG NRW, Urt. v. 7.12.2021 – 5 A 2000/20, Rn. 25 f., 68 (Erledigung vor Klageerhebung; Präjudiz)
– BayVGH, Urt. v. 10.7.2018 – 10 BV 17.2405, Rn. 20–22 (Klagefrist bei Erledigung vor Klageerhebung)
– BVerfG, Beschl. v. 14.5.1985 – 1 BvR 233, 341/81, BVerfGE 69, 315 (Brokdorf)

Hinweise: Jördis und Herr Hinze sind erfundene Figuren. Mehr dazu: Folge 069 (Anfechtungsklage Schema), Folge 057 (Klagearten), Folge 028 (Brokdorf-Beschluss); Tenor und Assessor-Perspektive in Folge 234.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Fortsetzungsfeststellungsklage #Verwaltungsprozessrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Paragraf", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Fortsetzungsfeststellungsklage Versammlung", "113 I 4 VwGO analog", "Erledigung vor Klageerhebung"]
                         if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
