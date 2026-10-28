"""Nachbearbeitung der Upload-Texte für Folge 279 (nach meta_273.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen und
Quellen der zwei geprüften Länder, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen wie in Blasen/Tafeln).
Landesrecht: Konkrete Angaben nur für die an amtlicher Quelle geprüften Länder NRW und Bayern (Abruf 08.10.2026);
die übrigen Länder wurden nicht geprüft – die Beschreibung verweist dafür auf das Juristenausbildungsgesetz bzw. die
Prüfungsordnung und das Prüfungsamt des eigenen Landes.
Aufruf: python3 meta_279.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: tippen oder mit der Hand?"),
       (T("was"), "Rechtsgrundlage: § 5d Abs. 6 DRiG"),
       (T("nrw"), "Beispiele: NRW und Bayern"),
       (T("aend"), "Was ändert sich: Gliederung, Umstellen, Rechtschreibung"),
       (T("zeit"), "Zeit und Lesbarkeit"),
       (T("bleibt"), "Was bleibt gleich"),
       (T("vorb"), "So bereitest du dich vor"),
       (T("erg"), "Ergebnis: Telse entscheidet"),
       (T("tipp"), "Klausurtipp: erst skizzieren, dann tippen"),
       (T("sch"), "Dein E-Examen in 5 Schritten"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""E-Examen: Wie läuft die elektronische Examensklausur ab, welche Vor- und Nachteile hat das Tippen, und wie bereitest du dich darauf vor?

Der Fall: Telse schreibt bald ihre Examensklausuren in Nordrhein-Westfalen. Im Prüfungssaal stehen Laptops. Tippen oder mit der Hand schreiben – was ändert sich wirklich? Ihr Bruder Jost hat das zweite Examen in Bayern schon am Laptop geschrieben.

Inhalt:
– Rechtsgrundlage: Nach § 5d Abs. 6 DRiG kann das Landesrecht bestimmen, dass schriftliche Leistungen in den staatlichen Prüfungen elektronisch erbracht werden dürfen. Ob und wie, entscheidet dein Land.
– Zwei Beispiele: Nordrhein-Westfalen (seit 1.1.2024 E-Klausur im 1. und 2. Examen, Wahl zwischen Hand und Laptop) und Bayern (freiwillig, 2. Examen seit dem Termin 2024/2, 1. Examen seit dem Termin 2026/2; Wahl vorab, grundsätzlich bindend)
– Was sich ändert: Gliederung, Korrigieren und Umstellen, Rechtschreibprüfung (NRW ein- und ausschaltbar, Bayern keine), Zeit (Bayern: keine Uhr in der Software, Abgabe per Klick), Lesbarkeit
– Was bleibt: Aufgabentext auf Papier, Gesetzestexte als Bücher (im 2. Examen in NRW auch Kommentare), Gutachtenstil und Schwerpunkte
– Vorbereitung: Probeklausuren am Rechner, Tippen mit 10 Fingern, Demoportale der Prüfungsämter
– Klausurtipp, dein E-Examen in 5 Schritten, Merksatz

Normen und Quellen: § 5d Abs. 6 DRiG · Nordrhein-Westfalen: §§ 10 Abs. 1, 13 Abs. 3, 51 Abs. 1 JAG NRW sowie die Hinweise des Landesjustizprüfungsamts und der Justizprüfungsämter (E-Klausur, Anwendungshinweise, Hilfsmittel) · Bayern: § 5 Abs. 3 JAPO (Fundstelle nach Angabe des Landesjustizprüfungsamts) und die Fragen und Antworten des Landesjustizprüfungsamts zum E-Examen

Hinweise: Ob und wie du elektronisch schreibst, regelt jedes Land selbst. Im Video stehen nur Nordrhein-Westfalen und Bayern als Beispiele (Angaben am 8. Oktober 2026 auf den amtlichen Seiten geprüft). Für alle anderen Länder gilt dein Juristenausbildungsgesetz bzw. deine Prüfungsordnung; die Prüfungsämter ändern ihre Hinweise laufend. Frag im Zweifel dein Prüfungsamt. Passend dazu: Folge 201 „Lernplan Examen“, Folge 237 „Probeklausuren Examen“ und Folge 273 „Freischuss Jura“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechts- oder Studienberatung im Einzelfall. Rechtsstand: 8. Oktober 2026 (DRiG zuletzt geändert am 22. Oktober 2024; JAG NRW in der Fassung ab 7. Mai 2025).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons (MIT), Fluent Emoji High Contrast (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound 215744 (supersnd, CC0).

#EExamen #Staatsexamen #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
assert not re.search(r"§\n|Abs\.\n|Art\.\n|Nr\.\n", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
