"""Nachbearbeitung der Upload-Texte für Folge 090 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Hinweis zum Landesrecht, Rechtsprechung mit Rn.,
Lizenzzeile; Sprechernamen und Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_090.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Der Rohbau nebenan"), (T("kanzlei"), "Kanzlei, Frage und Sachverhalt"),
       (T("grund"), "Warum die Klage nicht stoppt: § 212a I BauGB"), (T("wl80a"), "Der Eilantrag nach § 80a III VwGO"),
       (T("zul"), "A. Zulässigkeit"), (T("rsb"), "Rechtsschutzbedürfnis und Beiladung des Bauherrn"),
       (T("begr"), "B. Interessenabwägung im Dreieck"), (T("nurdritt"), "Nur drittschützende Normen"),
       (T("abf"), "Abstandsflächen im Fall"), (T("ergeb"), "Ergebnis und Tenor"), (T("stopp"), "Baustopp und Sicherungsmaßnahmen"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Drittanfechtung Baugenehmigung: Warum der Nachbarwiderspruch nach § 212a BauGB nicht aufschiebt und wie der Eilantrag nach §§ 80a III, 80 V VwGO aufgebaut ist.

Der Fall: Neben dem kleinen Haus von Frau Dorn wächst der Rohbau eines vierstöckigen Hauses und nimmt ihr fast das ganze Tageslicht. Herr Weber hat eine Baugenehmigung der Stadt und baut weiter, obwohl Frau Dorn klagt. Rechtsanwalt Falk stellt einen Eilantrag – Anwaltsklausur aus Sicht der Nachbarin. (Übungsfall)

Inhalt:
– Problem: Widerspruch und Anfechtungsklage eines Dritten gegen die Baugenehmigung haben keine aufschiebende Wirkung (§ 212a I BauGB = Fall des § 80 II 1 Nr. 3 VwGO)
– Antrag nach § 80a III 2 i. V. m. § 80 V 1 Alt. 1 VwGO: Anordnung (nicht Wiederherstellung) der aufschiebenden Wirkung
– A. Zulässigkeit: Statthaftigkeit (§ 80a statt § 123 VwGO), Antragsbefugnis analog § 42 II VwGO über eine drittschützende Norm, Rechtsschutzbedürfnis (kein Behördenantrag nach § 80 VI VwGO), notwendige Beiladung des Bauherrn (§ 65 II VwGO)
– B. Begründetheit: Interessenabwägung im Dreieck mit der Wertung des § 212a BauGB, summarische Prüfung nur drittschützender Normen, Folgenabwägung bei offenem Ausgang
– Im Fall: Abstandsflächen verletzt (Beispiel NRW: 0,4 H, mindestens 3 m) – Anordnung der aufschiebenden Wirkung, Tenor
– Sicherungsmaßnahmen nach § 80a III 1, I Nr. 2 VwGO, Klausurtipp, Klausurschema, Merksatz

Landesrecht: Die Abstandsflächen regelt die Bauordnung deines Landes (im Video Beispiel NRW: § 6 BauO NRW 2018; Prüfprogramm § 64 I 1 Nr. 1 b BauO NRW 2018). Ob vor der Klage ein Widerspruch nötig ist, bestimmt ebenfalls das Land (NRW: kein Vorverfahren bei Entscheidungen der Bauaufsichtsbehörden, § 110 III 2 Nr. 8 JustG NRW) – bitte im Recht deines Landes nachschlagen. Das Prozessrecht (§§ 80, 80a VwGO, § 212a BauGB) gilt bundesweit gleich.

Rechtsprechung:
– BVerwG, Beschl. v. 19.12.2019 – 7 VR 7.19, Rn. 8 (Interessenabwägung nach § 80a III 2, § 80 V 1 VwGO, summarische Prüfung)
– BVerwG, Beschl. v. 15.6.2016 – 4 B 52.15, Rn. 9 (Abstandsflächenrecht konkretisiert die Rücksichtnahme bei der Besonnung)
– OVG NRW, Beschl. v. 16.6.2020 – 10 B 603/20, Rn. 16 (Abstandsflächen verletzt: Aussetzungsinteresse überwiegt trotz § 212a I BauGB)
– OVG NRW, Beschl. v. 14.1.2021 – 10 B 1891/20, Rn. 5 (Maß der baulichen Nutzung nur über das Rücksichtnahmegebot)
– OVG NRW, Beschl. v. 15.12.2023 – 10 B 645/23, Rn. 3, 90 (nur Rechte des Nachbarn; Folgenabwägung, Bauen auf eigenes Risiko)
– OVG NRW, Beschl. v. 29.12.2025 – 7 B 359/25, Rn. 12 (Vorrang der Vollziehbarkeit nach § 212a BauGB)
– OVG NRW, Beschl. v. 11.1.2000 – 10 B 2060/99, Rn. 10 (Sicherungsmaßnahmen nach § 80a VwGO)

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Baurecht #Nachbarklage #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nDorn:", "\nFrau Dorn:"), ("\nWeber:", "\nHerr Weber:"), ("\nFalk:", "\nRechtsanwalt Falk:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
for alt, neu in (("§ 212 a", "§ 212a"), ("§ 212\na", "§ 212a\n"), ("bis acht gilt", "bis 8 gilt"),
                 ("Absätzen eins und zwei", "Absätzen 1 und 2"), ("Absätzen eins\nund zwei", "Absätzen 1\nund 2")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"§ 212\n\n(\d+\n[^\n]+\n)a([.,]) ", r"§ 212a\2\n\n\1", srt)   # „a“ hinter § 212 in die vorige Zeile holen
assert "212 a" not in srt and "bis acht" not in srt and not re.search(r"§ 212\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
