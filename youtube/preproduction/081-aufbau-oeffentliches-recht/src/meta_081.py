"""Nachbearbeitung der Upload-Texte für Folge 081 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweis auf
Klausurkonventionen, Lizenzzeile; Sprechernamen und Paragrafen-Umbruch in den Untertiteln. Kein Landesrecht subsumiert.
Aufruf: python3 meta_081.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Das Fahrtenbuch"), (T("sv"), "Sachverhalt und Obersatz"),
       (T("unz"), "Fehlt die Zulässigkeit"), (T("bau"), "Bausteine der Zulässigkeit"),
       (T("wl42"), "Klagebefugnis, § 42 II VwGO, und typische Fehler"), (T("wl113"), "Begründetheit, § 113 I 1 VwGO"),
       (T("arg"), "Das Argument im Fall, Ergebnis"), (T("ueb"), "Verfassungsbeschwerde und § 80 V VwGO"),
       (T("gew"), "Urteilsstil und Gutachtenstil"), (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Zulässigkeit und Begründetheit sauber trennen: der Grundaufbau öffentlich-rechtlicher Klausuren nach VwGO und BVerfGG – was wohin gehört und warum.

Der Fall: Die Studentin Tabea teilt ihr Auto mit zwei Mitbewohnern. Jemand wird damit geblitzt, der Fahrer bleibt unbekannt, und die Stadt ordnet ein Fahrtenbuch an (§ 31a StVZO). „Ich bin doch gar nicht gefahren!“ – Mitbewohner Lennart meint: „Dann ist der Bescheid rechtswidrig. Deine Klage ist also zulässig.“ Wo liegt der Fehler? (Übungsfall)

Inhalt:
– Obersatz: „Die Klage hat Erfolg, soweit sie zulässig und begründet ist.“ (Klausurkonvention)
– Zulässigkeit = Sachentscheidungsvoraussetzungen: Darf das Gericht in der Sache entscheiden? Fehlt sie: Abweisung als unzulässig, beim falschen Rechtsweg Verweisung (§ 17a GVG i. V. m. § 173 VwGO), Zwischenurteil (§ 109 VwGO)
– Bausteine: Verwaltungsrechtsweg (§ 40 I 1 VwGO), statthafte Klageart, besondere Voraussetzungen (§ 42 II, §§ 68 ff., § 74 VwGO), Beteiligte (§§ 61, 62, 78 VwGO), Rechtsschutzbedürfnis
– Klagebefugnis (§ 42 II VwGO): Möglichkeit der Rechtsverletzung, Adressatentheorie
– Typische Fehler: volle Rechtsverletzung schon in der Zulässigkeit; Rechtswidrigkeit als Zulässigkeitsargument
– Begründetheit der Anfechtungsklage (§ 113 I 1 VwGO): Rechtswidrigkeit (Ermächtigungsgrundlage, formell, materiell) und Rechtsverletzung
– Gleicher Grundaufbau: Verfassungsbeschwerde (Art. 94 I Nr. 4a GG, §§ 90 ff. BVerfGG) und Eilverfahren (§ 80 V VwGO, Interessenabwägung)
– Urteilsstil und Gutachtenstil, Klausurtipp, Klausurschema, Merksatz

Rechtsprechung:
– BVerwG, Urt. v. 9.12.2021 – 4 C 3.20, Rn. 9 (Klagebefugnis: Möglichkeit der Rechtsverletzung)
– BVerwG, Beschl. v. 14.4.2020 – 9 B 4.19, Rn. 18 (Adressatentheorie, § 113 I 1 VwGO)
– BVerwG, Beschl. v. 11.11.2020 – 7 VR 5.20, Rn. 8 (§ 80 V VwGO: Interessenabwägung, Erfolgsaussichten in der Hauptsache)

Ob ein Widerspruchsverfahren nötig ist und wer zu verklagen ist, regelt teils das Landesrecht (§ 68 I 2, § 78 I Nr. 2 VwGO) – bitte im Recht deines Landes nachschlagen.

Kapitel:
{kapitel}

Die Prüfungsschemata und Aufbauregeln sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 2. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#ÖffentlichesRecht #Klausuraufbau #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
