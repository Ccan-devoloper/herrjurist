"""Nachbearbeitung der Upload-Texte für Folge 226 (nach meta_205.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen).
Die reale Person des echten Falls erscheint nur als Fallbezeichnung (Caroline von Monaco, BGHZ 128, 1).
Aufruf: python3 meta_226.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Das erfundene Exklusiv-Interview"),
       (T("sv"), "Sachverhalt; I. § 823 Abs. 1 BGB"),
       (T("sonst"), "Persönlichkeitsrecht als sonstiges Recht"),
       (T("rahmen"), "Rahmenrecht und Abwägung"),
       (T("mund"), "II. Eingriff: Worte in den Mund gelegt"),
       (T("presse"), "III. Abwägung mit der Pressefreiheit"),
       (T("vorrang"), "Rechtswidrigkeit und Vorsatz"),
       (T("folgen"), "IV. Unterlassung und Widerruf"),
       (T("geld"), "Geldentschädigung: Voraussetzungen, § 253 II"),
       (T("hoehe"), "Höhe: Prävention und Gewinnerzielung"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Allgemeines Persönlichkeitsrecht (§ 823 I BGB i.V.m. Art. 1 I, 2 I GG): Wann gibt es Geldentschädigung? Das erfundene Interview mit Caroline von Monaco (BGHZ 128, 1).

Der Fall: Das Wochenmagazin „Funkelblatt“ titelt „Exklusiv! Juliane Hellberg spricht über ihre Trennung“ – 4 Seiten Interview mit der Schauspielerin. Sie hat nie mit dem Magazin gesprochen, jedes Wort ist erfunden. Kann sie Unterlassung, Widerruf und eine Geldentschädigung verlangen, und wonach richtet sich deren Höhe? Unser Fall bildet den Klassiker nach, den der Bundesgerichtshof am 15. November 1994 entschieden hat.

Inhalt:
– I. Anspruchsgrundlage: § 823 Abs. 1 BGB im Wortlaut, das allgemeine Persönlichkeitsrecht als sonstiges Recht (Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG im Wortlaut), Rahmenrecht und Abwägung
– II. Eingriff: Schutz davor, dass jemandem Äußerungen in den Mund gelegt werden, die er nicht getan hat
– III. Abwägung mit der Pressefreiheit (Art. 5 Abs. 1 Satz 2 GG im Wortlaut): Ein erfundenes Interview trägt nichts zur Meinungsbildung bei; das unrichtige Zitat ist nicht geschützt; Vorsatz
– IV. Rechtsfolgen: Unterlassung (§ 1004 Abs. 1 Satz 2 BGB analog), Widerruf, Geldentschädigung (schwerwiegender Eingriff, nicht anders auszugleichen; kein Schmerzensgeld nach § 253 Abs. 2 BGB)
– Höhe: Genugtuung, Prävention, Gewinnerzielung als Bemessungsfaktor, echter Hemmungseffekt, keine Gewinnabschöpfung
– Ergebnis, Klausurtipp, Prüfschema, Merksatz

Normen: § 823 Abs. 1 BGB i. V. m. Art. 1 Abs. 1, Art. 2 Abs. 1 GG; § 1004 Abs. 1 Satz 2 BGB analog; Art. 5 Abs. 1 Satz 2 GG; § 253 Abs. 2 BGB (Abgrenzung)

Rechtsprechung:
– BGH, Urt. v. 15.11.1994 – VI ZR 56/94, BGHZ 128, 1 (Caroline von Monaco)
– BGH, Urt. v. 5.12.1995 – VI ZR 332/94 (Präventionsgedanke, im Anschluss an BGHZ 128, 1)
– BGH, Urt. v. 17.12.2013 – VI ZR 211/12, BGHZ 199, 237, Rn. 22, 38, 40, 43 f., 49
– BGH, Urt. v. 11.12.2012 – VI ZR 314/10, Rn. 8 (Unterlassungsanspruch)
– BVerfGE 34, 269 (Soraya); BVerfGE 54, 148 (Eppler); BVerfGE 54, 208 (Böll); BVerfGE 97, 125
– BVerfG, Beschl. v. 8.3.2000 – 1 BvR 1127/96, Rn. 9

Hinweise: Juliane Hellberg, Chefredakteur Kettler, Anwalt Dr. Ruhnau und das Magazin „Funkelblatt“ sind erfunden; sie bilden den Klassiker nach. Die reale Person des echten Falls wird nicht dargestellt. Das Grundschema des § 823 Abs. 1 BGB erklärt unsere Folge „§ 823 I BGB: Das Prüfungsschema der unerlaubten Handlung“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Persönlichkeitsrecht #Deliktsrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("Leserin: Ein Exklusiv", "Leserin: Ein Exklusiv"), ("Kettler: Mit ihrem", "Chefredakteur Kettler: Mit ihrem"),
          ("Juliane: Ich habe", "Juliane Hellberg: Ich habe"), ("Ruhnau: Dann verlangen", "Dr. Ruhnau: Dann verlangen")]
for a, b in ERSATZ:
    assert a in srt, a
    srt = srt.replace(a, b)
for a, b in [(r"vierhunderttausend", "400.000"), (r"vier(\s)Seiten", r"4\1Seiten"), (r"fünfzehnten(\s)November", r"15.\1November"),
             (r"Art\. 1 und(\s)zwei", r"Art. 1 und\g<1>2"), (r"Artikeln eins und zwei", "Art. 1 und 2")]:
    assert re.search(a, srt), a
    srt = re.sub(a, b, srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|neunzehnhundert|vierhunderttausend|fünfzehnten", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
