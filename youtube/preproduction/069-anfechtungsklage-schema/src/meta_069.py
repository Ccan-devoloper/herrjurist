"""Nachbearbeitung der Upload-Texte für Folge 069 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Landesrecht-Hinweis (Beispiel NRW), Rechtsprechung
mit Rn., Lizenzzeile; Sprechernamen und Paragrafen-Umbruch in den Untertiteln. Keine 16-Länder-Liste (nur NRW geprüft).
Aufruf: python3 meta_069.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Der Foodtruck wird untersagt"), (T("klage"), "Klage, Frage und Sachverhalt"),
       (T("aufbau"), "Aufbau und I. Verwaltungsrechtsweg"), (T("wl42"), "II. Statthafte Klageart, § 42 I VwGO"),
       (T("wl422"), "III. Klagebefugnis, § 42 II VwGO"), (T("vv"), "IV. Vorverfahren (Beispiel NRW)"),
       (T("frist"), "V. Klagefrist, § 74 I VwGO"), (T("kg"), "VI. Klagegegner, § 78 VwGO"),
       (T("bet"), "VII. Beteiligte, VIII. Rechtsschutzbedürfnis"), (T("wl113"), "B. Begründetheit, § 113 I 1 VwGO"),
       (T("egl"), "Ermächtigungsgrundlage und formelle Rechtmäßigkeit"),
       (T("tb"), "Materielle Rechtmäßigkeit: Unzuverlässigkeit"), (T("rf"), "Rechtsfolge, § 114 VwGO"),
       (T("rv"), "Rechtsverletzung und Urteil"), (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Anfechtungsklage Schema (§ 42 I Alt. 1 VwGO): Zulässigkeit vom Rechtsweg bis zum Rechtsschutzbedürfnis und Begründetheit nach § 113 I 1 VwGO – komplett, an einem Fall.

Der Fall: Frau Ebeling verkauft mittags Suppen aus ihrem Foodtruck. Sie schuldet dem Finanzamt seit drei Jahren 30.000 €. Die Stadt hört sie an und untersagt ihr dann per Bescheid das Gewerbe (§ 35 GewO). Drei Wochen später klagt sie. Hat die Klage Erfolg? (Übungsfall)

Inhalt:
– A. Zulässigkeit: I. Verwaltungsrechtsweg (§ 40 I 1 VwGO), II. statthafte Klageart (§ 42 I Alt. 1 VwGO), III. Klagebefugnis (§ 42 II VwGO, Möglichkeit der Rechtsverletzung, Adressatentheorie), IV. Vorverfahren (§§ 68 ff. VwGO), V. Klagefrist (§ 74 I VwGO, § 58 II VwGO), VI. Klagegegner (§ 78 I Nr. 1 VwGO, Rechtsträgerprinzip), VII. Beteiligten- und Prozessfähigkeit (§§ 61, 62 VwGO), VIII. Rechtsschutzbedürfnis
– B. Begründetheit (§ 113 I 1 VwGO): Ermächtigungsgrundlage (§ 35 I 1 GewO), formelle Rechtmäßigkeit (Zuständigkeit, Anhörung § 28 VwVfG, Heilung § 45 VwVfG, Form § 39 VwVfG), materielle Rechtmäßigkeit (Unzuverlässigkeit, gebundene Entscheidung, Ermessen § 114 VwGO), Rechtsverletzung
– Urteil, Klausurtipp, Klausurschema, Merksatz

Landesrecht: Das Video nutzt Nordrhein-Westfalen als Beispiel. Dort entfällt das Vorverfahren in der Regel (§ 110 Abs. 1 Satz 1 JustG NRW), ausdrücklich auch bei Entscheidungen nach der Gewerbeordnung (§ 110 Abs. 3 Satz 2 Nr. 4 JustG NRW); verklagt wird die Körperschaft (§ 78 I Nr. 1 VwGO). Ob ein Widerspruchsverfahren nötig ist und ob die Behörde selbst zu verklagen ist (§ 78 I Nr. 2 VwGO), regelt jedes Land selbst – bitte im Recht deines Landes nachschlagen.

Rechtsprechung:
– BVerwG, Urt. v. 9.12.2021 – 4 C 3.20, Rn. 9 (Klagebefugnis: Möglichkeit der Rechtsverletzung)
– BVerwG, Beschl. v. 14.4.2020 – 9 B 4.19, Rn. 18 (Adressatentheorie, § 113 I 1 VwGO)
– BVerwG, Urt. v. 15.4.2015 – 8 C 6.14, Rn. 14 (Gewerbeuntersagung, Steuerrückstände, Sanierungskonzept)
– BVerwG, Beschl. v. 6.7.2022 – 3 B 40.21, Rn. 10, 12 (öffentlich-rechtliche, nichtverfassungsrechtliche Streitigkeit)

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 2. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#AnfechtungsklageSchema #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nEbeling:", "\nFrau Ebeling:"), ("\nGerlach:", "\nHerr Gerlach:"), ("\nRichterin:", "\nDie Richterin:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
