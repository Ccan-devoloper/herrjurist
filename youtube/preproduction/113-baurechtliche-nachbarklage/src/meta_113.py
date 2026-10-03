"""Nachbearbeitung der Upload-Texte für Folge 113 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Abstandsflächen-Normen der Länder, Rechtsprechung
mit Rn., Rechtsstand, Lizenzzeile; Sprechernamen und Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_113.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Der Anbau kurz vor der Grenze"),
       (T("zul"), "1. Zulässigkeit: Anfechtungsklage und Klagebefugnis"),
       (T("p113"), "2. Begründetheit: § 113 I 1 VwGO"),
       (T("tab"), "3. Welche Bauvorschriften schützen dich?"),
       (T("r1"), "4. Rügen: Geschossflächenzahl und Flachdach"),
       (T("r3"), "Abstandsfläche: § 6 BauO NRW"),
       (T("luecke"), "Rechtsverletzung und Ergebnis"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Schema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Baurechtliche Nachbarklage (§§ 42 II, 113 I 1 VwGO): Welche Bauvorschriften sind drittschützend? Abstandsflächen, Gebietserhaltung, Rücksichtnahme – bundesweit erklärt.

Der Fall: Herr Pütz, der Nachbar von Frau Mahnke, bekommt die Baugenehmigung für einen zweigeschossigen Anbau mit Flachdach. Die Wand ist 6 m hoch und steht nur 1,50 m vor der Grenze, die Geschossflächenzahl steigt über das im Bebauungsplan erlaubte Maß, die Gestaltungssatzung verlangt Satteldächer. Drei Verstöße – aber mit welchem gewinnt Frau Mahnke ihre Klage? (Übungsfall, Beispielland Nordrhein-Westfalen)

Inhalt:
– Zulässigkeit kurz: Anfechtungsklage, Klagebefugnis über eine drittschützende Norm
– Begründetheit nach § 113 I 1 VwGO: rechtswidrig UND dadurch in eigenen Rechten verletzt – objektive Rechtswidrigkeit ist nicht gleich Rechtsverletzung
– Ampel-Tabelle: Abstandsflächen, Gebietserhaltungsanspruch, Rücksichtnahmegebot (schützen dich) – Maß der baulichen Nutzung, Gestaltungsvorschriften (in der Regel nicht)
– Die Rügen am Fall: Geschossflächenzahl (§ 30 I BauGB, Befreiung nach § 31 II BauGB), Flachdach, Abstandsfläche (§ 6 BauO NRW: 0,4 H, mindestens 3 m)
– Ergebnis und Eilrechtsschutz (§ 212a I BauGB – eigenes Video)
– Klausurtipp, Schema, Merksatz

Landesrecht: Das Abstandsflächenrecht steht in der Bauordnung deines Landes. Im Video geprüft ist nur Nordrhein-Westfalen (§ 6 BauO NRW 2018); Tiefe, Mindestmaß, Prüfprogramm und Widerspruchsverfahren können in deinem Land anders geregelt sein. Abstandsflächen in den Landesbauordnungen (Normnummern ohne Gewähr, bitte im Landesrecht nachlesen): § 5 LBO (Baden-Württemberg), Art. 6 BayBO (Bayern), § 6 BauO Bln (Berlin), § 6 BbgBO (Brandenburg), § 6 BremLBO (Bremen), § 6 HBauO (Hamburg), § 6 HBO (Hessen), § 6 LBauO M-V (Mecklenburg-Vorpommern), § 5 NBauO (Niedersachsen, „Grenzabstände“), § 6 BauO NRW (Nordrhein-Westfalen), § 8 LBauO (Rheinland-Pfalz), § 7 LBO (Saarland), § 6 SächsBO (Sachsen), § 6 BauO LSA (Sachsen-Anhalt), § 6 LBO (Schleswig-Holstein), § 6 ThürBO (Thüringen).

Rechtsprechung:
– OVG NRW, Urt. v. 6.11.2024 – 7 A 75/23, Rn. 32, 39, 41 (Nachbarklage nur bei Verletzung nachbarschützender Normen; Maß und Gestaltung)
– OVG NRW, Urt. v. 22.1.2025 – 7 A 1367/22, Rn. 48, 53, 57, 80 (Anbau 1,50 m vor der Grenze; keine konkrete Beeinträchtigung nötig)
– OVG NRW, Beschl. v. 15.12.2023 – 10 B 645/23, Rn. 38, 42–48 (Maßfestsetzungen, Befreiung)
– BVerwG, Urt. v. 9.8.2018 – 4 C 7.17, Rn. 12–14, 21 (Befreiung, Maß der baulichen Nutzung)
– BVerwG, Urt. v. 29.3.2022 – 4 C 6.20, Rn. 8 (Gebietserhaltungsanspruch)
– BVerwG, Beschl. v. 15.6.2016 – 4 B 52.15, Rn. 9 (Abstandsflächen als Konkretisierung der Rücksichtnahme)

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026 (BauGB zuletzt geändert durch Gesetz vom 23.7.2026; BauO NRW 2018 in der Fassung ab 1.9.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Baurecht #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nMahnke:", "\nFrau Mahnke:"), ("\nPütz:", "\nHerr Pütz:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
