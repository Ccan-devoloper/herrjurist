"""Nachbearbeitung der Upload-Texte für Folge 201 (nach meta_200.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Zahlen in Figurenrede wie in den Blasen, Folgennummern).
Methodikfolge: Pflichtfächer bundesrechtlich (DRiG), Prüfungsdetails landesrechtlich (Beispiel NRW, ausdrücklich als
Beispiel gekennzeichnet); kein Landesrecht im Sinne der VIDEOLEITLINIEN (keine Polizei-/Kommunal-/Baurechtsnorm).
Aufruf: python3 meta_201.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Examen in einem Jahr – womit fängst du an?"),
       (T("s1"), "Schritt 1: Bestandsaufnahme – Pflichtfächer, § 5a DRiG"),
       (T("land"), "Landesrecht: Beispiel NRW, 6 Klausuren à 5 Stunden"),
       (T("ampel"), "Die Ampel: Was kannst du schon?"),
       (T("s2"), "Schritt 2: rückwärts planen, Freiversuch"),
       (T("s3"), "Schritt 3: die Stoffphase gewichten"),
       (T("s4"), "Schritt 4: das Wiederholungssystem"),
       (T("s5"), "Schritt 5: Klausuren von Anfang an"),
       (T("s6"), "Schritt 6: Puffer, Pausen, Endspurt"),
       (T("wp"), "Beispielwoche: der Wochenplan"),
       (T("erg"), "Ergebnis: der Plan von Fenna"),
       (T("tipp"), "Klausurtipp: üben wie im Examen"),
       (T("sch"), "Dein Lernplan in 6 Schritten"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Lernplan Examen: Wie du 12 Monate Examensvorbereitung sinnvoll einteilst – Stoff, Wiederholung und Klausurtraining im richtigen Verhältnis.

Der Fall: Noch ein Jahr bis zu den Klausuren der staatlichen Pflichtfachprüfung. Fenna steht vor einem leeren Wandkalender und weiß nicht, womit sie anfangen soll. Nils, der das Examen im letzten Jahr geschrieben hat, plant mit ihr rückwärts – vom Examenstermin aus.

Inhalt:
– Schritt 1, Bestandsaufnahme: Was wird geprüft? Die Pflichtfächer nach § 5a Abs. 2 S. 3 DRiG im Wortlaut; das Nähere regelt das Landesrecht – Beispiel Nordrhein-Westfalen: 6 Klausuren (3 Zivilrecht, 2 Öffentliches Recht, 1 Strafrecht), je 5 Stunden, Stoffkatalog in § 11 Abs. 2 JAG NRW; dazu die Ampel für jedes Gebiet
– Schritt 2, rückwärts planen: Examenstermin, Freiversuch (§ 5d Abs. 5 DRiG), Endspurt, Puffermonat
– Schritt 3, Stoffphase: Gewichtung nach Prüfung und Ampel – als Empfehlung, nicht als Regel
– Schritt 4, Wiederholung: wachsende Abstände, Karteikarten und Schemata aus dem Kopf
– Schritt 5, Klausuren von Anfang an: jede Woche eine Klausur unter Examensbedingungen
– Schritt 6, Puffer und Pausen: freier Tag, Urlaub, Puffermonat, die letzten 6 bis 8 Wochen ohne neuen Stoff
– Beispielwoche als Wochenplan, Klausurtipp, Lernplan in 6 Schritten, Merksatz

Normen: §§ 5, 5a Abs. 2 S. 3, Abs. 4, 5d Abs. 5, 6 DRiG; Beispiel NRW: §§ 10 Abs. 2, 11 Abs. 2, 13 Abs. 1, 3 JAG NRW

Hinweise: Wie viele Klausuren du schreibst, wie lange sie dauern, was genau zum Stoff gehört und bis wann du dich für den Freiversuch melden musst, regelt dein Land – prüfe dein Ausbildungsgesetz oder deine Prüfungsordnung. Nordrhein-Westfalen ist im Video nur das Beispiel. Alle Monatszahlen, Zeitanteile und Wiederholungsabstände sind Empfehlungen, keine Vorgaben. Mehr zur Zeiteinteilung in der Klausur: Folge 45 „Lösungsskizze Klausur: Zeitplan“; typische Fehler: Folge 117 „Jura Klausur Fehler“; Schemata richtig lernen: Folge 123.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechts- oder Studienberatung im Einzelfall. Rechtsstand: 6. Oktober 2026 (DRiG zuletzt geändert am 22. Oktober 2024; JAG NRW in der Fassung ab 7. Mai 2025).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#LernplanExamen #Examensvorbereitung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
for muster, ersatz in [(r"Zwölf Monate, drei Rechtsgebiete", r"12 Monate, 3 Rechtsgebiete"),
                       (r"mit Monat eins, Zivilrecht", r"mit Monat 1, Zivilrecht"),
                       (r"hundertdreiundzwanzig", r"123"), (r"fünfundvierzig", r"45"), (r"hundertsiebzehn", r"117")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
assert not re.search(r"§\n|Abs\.\n|Art\.\n|Nr\.\n", srt), "Untertitel prüfen"
assert "Paragraf" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
