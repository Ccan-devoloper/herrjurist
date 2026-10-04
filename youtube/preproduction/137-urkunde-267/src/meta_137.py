"""Nachbearbeitung der Upload-Texte für Folge 137 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Lizenzzeile,
zusätzliche Tags; Untertitel: verbliebene Zahlwörter in Ziffern. Aufruf: python3 meta_137.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: die gefälschte Entschuldigung – mit Sachverhalt"),
       (T("p267"), "§ 267 Abs. 1 StGB im Wortlaut und der Urkundenbegriff"),
       (T("perp"), "1. Perpetuierungsfunktion"),
       (T("bew"), "2. Beweisfunktion: Absichts- und Zufallsurkunde, Fotokopie"),
       (T("gar"), "3. Garantiefunktion und Beweiszeichen"),
       (T("tat"), "Unechte Urkunde: die Geistigkeitstheorie"),
       (T("luege"), "Klausurpunkt: die schriftliche Lüge"),
       (T("verf2"), "Verfälschen und Gebrauchen"),
       (T("vors"), "Subjektiver Tatbestand: zur Täuschung im Rechtsverkehr"),
       (T("var"), "Gegenvariante: Die Mutter erlaubt die Unterschrift"),
       (T("rw"), "Schuld, Ergebnis und Konkurrenzen"),
       (T("tipp"), "Klausurtipp: Echtheit und Wahrheit trennen"), (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Urkunde § 267 StGB: Perpetuierungs-, Beweis- und Garantiefunktion am Beispiel der gefälschten Entschuldigung – und wann ist eine Urkunde unecht?

Der Fall: Femke (16) schwänzt am Montag die Schule. Abends schreibt sie „Femke war am Montag krank. Bitte entschuldigen Sie ihr Fehlen.“, setzt den Namen ihrer Mutter darunter und ahmt deren Unterschrift nach. Die Mutter weiß nichts davon. Am Dienstag nimmt die Klassenlehrerin Frau Melzer den Zettel entgegen. Hat sich Femke wegen Urkundenfälschung strafbar gemacht?

Inhalt:
– Wortlaut § 267 Abs. 1 StGB und der Urkundenbegriff der Rechtsprechung
– Perpetuierungsfunktion: verkörperte Erklärung
– Beweisfunktion: Beweiseignung und -bestimmung, Absichts- und Zufallsurkunde, Abgrenzung zur bloßen Fotokopie
– Garantiefunktion: erkennbarer Aussteller, Beweiszeichen
– Herstellen einer unechten Urkunde: Täuschung über die Identität des Ausstellers, Geistigkeitstheorie
– Klausurpunkt schriftliche Lüge: echte, aber inhaltlich unwahre Urkunde ist keine Urkundenfälschung
– Verfälschen und Gebrauchen
– Subjektiver Tatbestand: Vorsatz und Handeln zur Täuschung im Rechtsverkehr
– Gegenvariante: Erlaubnis der Mutter (Stellvertretung bei der Unterschrift)
– Schuld (§ 19 StGB), Ergebnis, Konkurrenzen, Klausurtipp, Prüfschema, Merksatz

Normen: § 267 StGB; § 19 StGB; § 1 JGG

Rechtsprechung:
– BGH, Urt. v. 10.11.2022 – 5 StR 283/22, Rn. 36
– BGH, Beschl. v. 14.3.2024 – 2 StR 192/23, Rn. 17, 18, 29, 35, 36
– BGH, Urt. v. 11.11.2020 – 1 StR 328/19, Rn. 70–72, 75, 76
– BGH, Urt. v. 23.9.2015 – 2 StR 434/14, Rn. 34
– BGH, Urt. v. 17.10.2019 – 3 StR 521/18, Rn. 33, 34
– BGH, Beschl. v. 4.5.2023 – 5 StR 38/23, Rn. 13
– BGH, Beschl. v. 30.10.2008 – 3 StR 156/08, Rn. 11
(Randnummern nach HRRS)

Kapitel:
{kapitel}

Der Fall und die Personen sind ausgedacht. Die Begriffe Absichts- und Zufallsurkunde sowie die Definition „zur Täuschung im Rechtsverkehr“ sind Lehrbuchstandard. Das Jugendstrafrecht wird nicht vertieft. Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Strafrecht #Urkundenfälschung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for a, b in (("Femke ist sechzehn", "Femke ist 16"), ("sechzehn", "16"), ("vierzehn", "14"), ("neunzehn", "19"),
             ("Römisch eins:", "I."), ("Römisch zwei:", "II."), ("Römisch drei:", "III.")):
    srt = srt.replace(a, b)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Urkundenbegriff", "schriftliche Lüge", "Geistigkeitstheorie", "§ 267 StGB Schema"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
