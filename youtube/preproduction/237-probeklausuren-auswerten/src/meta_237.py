"""Nachbearbeitung der Upload-Texte für Folge 237 (nach meta_201.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Zahlen in Figurenrede wie in den Blasen, Folgennummern, Sprecher „Herr Seebach“).
Methodikfolge: Prüfungsdetails landesrechtlich (Beispiel NRW, ausdrücklich als Beispiel gekennzeichnet); kein Landesrecht im
Sinne der VIDEOLEITLINIEN (keine Polizei-/Kommunal-/Baurechtsnorm).
Aufruf: python3 meta_237.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: 12 Klausuren, fast immer 6 Punkte"),
       (T("warum"), "Warum die Note stehen bleibt"),
       (T("viele"), "Wie viele Probeklausuren? Die Faustregel"),
       (T("fach"), "Verteilt wie im Examen (Beispiel NRW)"),
       (T("bed"), "Unter Examensbedingungen schreiben"),
       (T("aus"), "Auswertung 1 und 2: Korrektur lesen, Musterlösung vergleichen"),
       (T("a3"), "Auswertung 3: das Fehlerprotokoll"),
       (T("a4"), "Auswertung 4: Wiederholungskarten"),
       (T("wr"), "Der Wochenrhythmus: Auswertungstag und Klausurtag"),
       (T("erg"), "Drei Wochen später"),
       (T("tipp"), "Klausurtipp: ein Ziel pro Probeklausur"),
       (T("sch"), "Dein Klausurtraining in 5 Schritten"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Probeklausuren im Examen: Wie viele solltest du schreiben, und wie wertest du sie so aus, dass jeder Fehler nur einmal passiert?

Der Fall: Friedrich schreibt seit zwölf Wochen jede Woche eine Probeklausur – und bekommt fast immer 6 Punkte. In der Sprechstunde fragt sein Mentor, was er mit den Korrekturen macht. Die Antwort: nichts. Er schaut auf die Note und schreibt die nächste.

Inhalt:
– Warum die Note stagniert: schreiben ohne auswerten
– Wie viele Klausuren? Eine Faustregel, keine Vorschrift: in der Stoffphase eine pro Woche, in den letzten Wochen vor dem Examen zwei – und nur so viele, wie du auswerten kannst
– Verteilt wie im Examen: Beispiel Nordrhein-Westfalen mit 6 Klausuren (3 Zivilrecht, 2 Öffentliches Recht, 1 Strafrecht), also etwa 1/2, 1/3 und 1/6 deiner Probeklausuren
– Unter Examensbedingungen: 5 Stunden am Stück, nur erlaubte Hilfsmittel, in deiner Form (von Hand oder am Computer)
– Die Auswertung in 4 Schritten: Korrektur lesen, Musterlösung neben die Gliederung, Fehlerprotokoll (Aufbau, Schwerpunkt, Wissen, Zeit), Wiederholungskarten
– Der Wochenrhythmus mit Auswertungstag und Klausurtag
– Klausurtipp, dein Klausurtraining in 5 Schritten, Merksatz

Normen (Beispiel NRW): § 10 Abs. 1, 2 JAG NRW, § 13 Abs. 1, 3 JAG NRW; § 5d Abs. 6 DRiG

Hinweise: Wie viele Klausuren das Examen hat, wie sie auf die Fächer verteilt sind, wie lange sie dauern und welche Hilfsmittel erlaubt sind, regelt dein Land – im ersten wie im zweiten Examen. Nordrhein-Westfalen ist im Video nur das Beispiel. Die Mengenangaben sind eine Faustregel, keine Vorgabe. Passend dazu: Folge 201 „Lernplan Examen“ (Klausuren im Lernplan, Wiederholung) und Folge 117 „Jura Klausur Fehler“ (typische Fehler im Einzelnen).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechts- oder Studienberatung im Einzelfall. Rechtsstand: 7. Oktober 2026 (DRiG zuletzt geändert am 22. Oktober 2024; JAG NRW in der Fassung ab 7. Mai 2025).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Probeklausuren #Examensvorbereitung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
for muster, ersatz in [(r"Zwölf(\s+)Klausuren in zwölf Wochen", r"12\1Klausuren in 12 Wochen"),
                       (r"fast immer sechs Punkte", r"fast immer 6 Punkte"),
                       (r"Sieben Punkte", r"7 Punkte"),
                       (r"zweihunderteins", r"201"), (r"hundertsiebzehn", r"117"),
                       (r"^Seebach:", r"Herr Seebach:")]:
    srt, n = re.subn(muster, ersatz, srt, flags=re.M)
    assert n, muster
assert not re.search(r"§\n|Abs\.\n|Art\.\n|Nr\.\n", srt), "Untertitel prüfen"
assert "Paragraf" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
