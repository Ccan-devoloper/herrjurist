"""Nachbearbeitung der Upload-Texte für Folge 117 (Kopie von meta_114.py) (nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Rahmen, Inhalt, Quellenhinweisen und Lizenzzeile;
Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_117.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Klausurrückgabe: Fünf Punkte"),
       (T("hook"), "Wo gehen die Punkte verloren?"),
       (T("sv"), "Der Übungsfall: Widerruf eines Online-Kaufs"),
       (T("f1"), "Fehler 1: Sachverhalt und Bearbeitervermerk"),
       (T("f2"), "Fehler 2: Die falsche Frage"),
       (T("f3"), "Fehler 3: Der Aufbau"),
       (T("f4"), "Fehler 4: Die Norm ungenau zitiert"),
       (T("f5"), "Fehler 5: Definition und Subsumtion"),
       (T("f6"), "Fehler 6: Gutachtenstil am falschen Ort"),
       (T("f7"), "Fehler 7: Der Schwerpunkt verfehlt"),
       (T("f8"), "Fehler 8: Der Meinungsstreit"),
       (T("f9"), "Fehler 9: Die Zeit"),
       (T("f10"), "Fehler 10: Das Ergebnis"),
       (T("tipp"), "Klausurtipp: Frage und Ergebnis nebeneinander"),
       (T("sch"), "Checkliste vor der Abgabe"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Jura Klausur Fehler: zehn typische Aufbau-, Stil- und Schwerpunktfehler in Examens- und Semesterklausuren – und wie du sie ab sofort vermeidest.

Der Rahmen: Ronja bekommt ihre Übungsklausur im Zivilrecht mit fünf Punkten zurück, obwohl sie das Widerrufsrecht kannte. Die Randbemerkungen der Korrektorin führen durch zehn Fehler – in der Reihenfolge, in der sie beim Schreiben passieren. Der Übungsfall: Frau Kröger widerruft einen Online-Kauf. War die Frist schon abgelaufen?

Inhalt:
– 1. Sachverhalt und Bearbeitervermerk nicht ausgewertet (zwei Daten deuten oft auf eine Frist)
– 2. Die falsche Frage beantwortet (Wer will was von wem woraus?)
– 3. Aufbaufehler: Vertrag vor Eigentum (§§ 546, 985, 986 BGB), objektiver Tatbestand vor Vorsatz (§ 16 Abs. 1 StGB)
– 4. Norm ungenau zitiert: § 356 Abs. 2 Nr. 1 Buchst. a BGB statt „§ 356 BGB“
– 5. Definition und Subsumtion fehlen (Fernabsatzvertrag, § 312c Abs. 1 BGB)
– 6. Gutachtenstil am falschen Ort, Urteilsstil am Problem
– 7. Schwerpunkt verfehlt – die Widerrufsfrist (§§ 355, 356, 187, 188 BGB)
– 8. Meinungsstreit ohne Entscheidung
– 9. Keine Zeit mehr für den letzten Prüfungspunkt
– 10. Ergebnis widerspricht der Prüfung
– Klausurtipp, Checkliste vor der Abgabe, Merksatz

Normen im Übungsfall: §§ 312c, 312g, 355, 356, 357 BGB; §§ 187, 188 BGB; Aufbaubeispiele §§ 546, 985, 986 BGB und §§ 15, 16 StGB

Quellen zu den Fehlern (keine Statistik, sondern Hinweise aus der Praxis): Hinweise des Landesjustizprüfungsamts Sachsen-Anhalt für die Aufsichtsarbeiten (Straf- und Zivilrecht), Merkblätter des Landesjustizprüfungsamts Niedersachsen, „Häufige Fehlerquellen in Klausuren“ des Examinatoriumsbüros der Universität Bielefeld, Trinh, ZJS 2022, 516 ff., Wörner, ZJS 2012, 630 ff. Die Reihenfolge der zehn Fehler folgt dem Arbeitsablauf der Klausur, nicht ihrer Häufigkeit.

Hinweise: Der Übungsfall ist erfunden. Gutachten- und Urteilsstil vertieft Folge 003, den Zeitplan für die Klausur Folge 045, den Anspruchsaufbau Folge 006 und den Aufbau der Strafrechtsklausur Folge 009.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Jurastudium #Klausurtechnik #Jura
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
