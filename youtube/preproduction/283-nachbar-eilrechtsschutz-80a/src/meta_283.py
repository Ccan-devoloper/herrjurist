"""Nachbearbeitung der Upload-Texte für Folge 283 (nach meta_277.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Untertitel-Korrekturen (Normangaben, Ziffern, Sprechernamen).
Aufruf: python3 meta_283.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Der Bagger rollt nebenan, Sachverhalt"),
       (T("grund"), "Warum stoppt der Widerspruch nichts? § 212a BauGB"),
       (T("statt"), "Statthaftigkeit: § 80a Abs. 3 VwGO"),
       (T("w805"), "Anordnung nach § 80 Abs. 5, nicht § 123"),
       (T("beh"), "Erst zur Behörde? § 80a Abs. 1 Nr. 2"),
       (T("zul"), "Zulässigkeit: Rechtsweg, Antragsbefugnis"),
       (T("rbh"), "Muss der Widerspruch eingelegt sein?"),
       (T("begr"), "Begründetheit: Interessenabwägung"),
       (T("nur"), "Abendsonne und Abstandsflächen: das Ergebnis"),
       (T("gegen"), "Gegenfall: Abstandsfläche verletzt"),
       (T("umg"), "Der umgekehrte Fall: § 80a Abs. 1 Nr. 1"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""§ 80a VwGO im Baurecht: Wie stoppt der Nachbar den Bagger, wenn der Widerspruch wegen § 212a BauGB nichts aufschiebt? Eilrechtsschutz – bundesweit erklärt.

Der Fall: Kaum hat Herr Brodbeck die Baugenehmigung für ein Mehrfamilienhaus mit 3 Geschossen, rollt der Bagger. Seine Nachbarin Frau Fehling fürchtet um die Abendsonne in ihrem Garten und legt Widerspruch ein – doch gebaut wird weiter. Wie kommt sie schnell zu einem Baustopp, und hat sie Erfolg?

Inhalt:
– Warum der Widerspruch nichts stoppt: § 212a Abs. 1 BauGB und § 80 Abs. 2 S. 1 Nr. 3 VwGO im Wortlaut
– Statthaftigkeit: Verwaltungsakt mit Doppelwirkung, § 80a Abs. 3 VwGO und § 80 Abs. 5 S. 1 VwGO im Wortlaut – Anordnung, nicht Wiederherstellung; Abgrenzung zu § 123 VwGO
– Erst zur Behörde? § 80a Abs. 1 Nr. 2 VwGO
– Zulässigkeit: Verwaltungsrechtsweg, Antragsbefugnis analog § 42 Abs. 2 VwGO, eingelegter Rechtsbehelf, § 80 Abs. 5 S. 2 VwGO
– Begründetheit: Interessenabwägung, Erfolgsaussichten summarisch, Folgenabwägung, gesetzliche Wertung des § 212a BauGB
– Rücksichtnahme und Abstandsflächen: Ergebnis und eigenes Risiko des Bauherrn; Gegenfall mit verletzter Abstandsfläche
– Der umgekehrte Fall: § 80a Abs. 1 Nr. 1 VwGO
– Klausurtipp, Klausurschema, Merksatz

Normen: § 212a Abs. 1 BauGB; §§ 40, 42 Abs. 2, 68 Abs. 1, 80 Abs. 1, 2, 5, 6, 80a Abs. 1, 3, 123 Abs. 5 VwGO.

Rechtsprechung:
– BVerwG, Beschl. v. 19.12.2019 – 7 VR 7.19, Rn. 5, 8 (Antragsbefugnis; Interessenabwägung nach § 80a Abs. 3 S. 2, § 80 Abs. 5 S. 1 VwGO)
– OVG NRW, Beschl. v. 15.12.2023 – 10 B 645/23, Rn. 3, 90 (Wertung des § 212a BauGB, eigenes Risiko des Bauherrn)
– OVG NRW, Beschl. v. 29.12.2025 – 7 B 359/25, Rn. 12 (Vorrang der Vollziehbarkeit)
– OVG NRW, Beschl. v. 16.6.2020 – 10 B 603/20, Rn. 16 (Anordnung trotz § 212a bei verletzten Abstandsflächen)
– BVerwG, Beschl. v. 15.6.2016 – 4 B 52.15, Rn. 9 (Besonnung: Abstandsflächenrecht konkretisiert die Rücksichtnahme)
– OVG NRW, Beschl. v. 18.12.2015 – 8 B 1108/15, Rn. 15; Beschl. v. 16.6.2026 – 7 B 334/26, Rn. 3–5 (eingelegter Rechtsbehelf)

Landesrecht: Ob vor der Klage ein Widerspruchsverfahren stattfindet und wie tief die Abstandsflächen sein müssen, regelt jedes Land selbst (Ausführungsgesetze zur VwGO, Landesbauordnungen). Das Video bleibt länderneutral.

Hinweise: Frau Fehling und Herr Brodbeck sind erfundene Figuren. Rechtsstand 8. Oktober 2026 – bitte bei späterer Nutzung prüfen. Mehr dazu: Folge 082 (Eilrechtsschutz nach § 80 Abs. 5 VwGO), Folge 113 (Baurechtliche Nachbarklage), Folge 254 (Einstweilige Anordnung, § 123 VwGO), Folge 090 (Drittanfechtung im 2. Examen).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Baurecht #Verwaltungsprozessrecht #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
srt = srt.replace("§§ 212a", "§ 212a")
srt = srt.replace("§ 80 Abs. 5 bis acht", "§ 80 Abs. 5 bis 8").replace("Absätzen eins und zwei", "Absätzen 1 und 2")
srt = srt.replace("Nummern eins bis drei a", "Nummern 1 bis 3a")
srt = re.sub(r"\n\n\n+", "\n\n", srt)
srt = re.sub(r"(?m)^Fehling:", "Frau Fehling:", srt)
srt = re.sub(r"(?m)^Brodbeck:", "Herr Brodbeck:", srt)
assert not re.search(r"§\n|Abs\.\n|Paragraf|§§", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["80a VwGO Nachbar", "Interessenabwägung 212a", "Eilantrag Baugenehmigung"]
                         if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
