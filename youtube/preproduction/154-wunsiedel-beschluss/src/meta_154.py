"""Nachbearbeitung der Upload-Texte für Folge 154 (nach meta_146.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn.,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Aussprachehilfe „Brockdorf“ → „Brokdorf“,
StGB, Sprechername). Keine Namen von NS-Personen in Titel oder Tags; im Beschreibungstext einmal sachlich.
Aufruf: python3 meta_154.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Darf ein Gesetz eine Meinung verbieten?"),
       (T("stadt"), "Der echte Fall: Wunsiedel 2005"),
       (T("klage"), "Instanzen, Verfassungsbeschwerde, Sachverhalt"),
       (T("a5"), "I. Schutzbereich: Art. 5 Abs. 1 GG"),
       (T("p130"), "II. Eingriff: § 130 Abs. 4 StGB"),
       (T("a52"), "III. Allgemeine Gesetze: Sonderrechts- und Abwägungslehre"),
       (T("bverwg"), "Ist § 130 Abs. 4 StGB allgemein?"),
       (T("sw2"), "Die Wunsiedel-Ausnahme"),
       (T("ah3"), "Grenzen der Ausnahme"),
       (T("zweck"), "Verhältnismäßigkeit: öffentlicher Friede"),
       (T("anw"), "Anwendung im Fall, Ergebnis, zurück im Seminar"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Wunsiedel-Beschluss (BVerfGE 124, 300): Ist § 130 IV StGB ein allgemeines Gesetz nach Art. 5 II GG? Sonderrechtslehre und die Ausnahme für NS-Verherrlichung.

Der Fall: In Wunsiedel liegt das Grab von Rudolf Heß. Ein Veranstalter meldet dort jährlich eine Gedenkveranstaltung an, auch für den 20. August 2005. Das Landratsamt verbietet sie nach dem Versammlungsgesetz, weil eine Straftat nach § 130 Abs. 4 StGB drohe. Die Klage scheitert in drei Instanzen. Mit der Verfassungsbeschwerde rügt der Veranstalter, § 130 Abs. 4 StGB sei kein allgemeines Gesetz. Das Bundesverfassungsgericht entscheidet am 4. November 2009.

Inhalt:
– Einstieg im Grundrechte-Seminar: Darf ein Gesetz eine bestimmte Meinung verbieten?
– Art. 5 Abs. 1 Satz 1 GG (im Wortlaut): Schutz jeder Meinung; Art. 8 GG im Maßstab des Art. 5 GG
– § 130 Abs. 4 StGB (im Wortlaut) als Eingriff
– Art. 5 Abs. 2 GG (im Wortlaut): Sonderrechtslehre, Abwägungslehre und ihre Verbindung durch das BVerfG; Meinungsneutralität
– Warum § 130 Abs. 4 StGB kein allgemeines Gesetz ist, und die Ausnahme vom Verbot des Sonderrechts (Leitsatz 1)
– Grenzen der Ausnahme (Leitsatz 2), Verhältnismäßigkeit und der enge Begriff des öffentlichen Friedens, Wechselwirkung
– Anwendung im Fall, Ergebnis, Klausurtipp, Prüfschema, Merksatz

Normen: Art. 5 Abs. 1 Satz 1, Abs. 2 GG; Art. 8 Abs. 1 GG; § 130 Abs. 4 StGB; § 15 Abs. 1 VersG

Rechtsprechung:
– BVerfG, Beschl. v. 4.11.2009 – 1 BvR 2150/08, BVerfGE 124, 300 (Wunsiedel): Leitsätze; Rn. 7–10 (Sachverhalt), 45 (Art. 8 GG), 49–51 (Schutzbereich, Eingriff), 54–63 (allgemeines Gesetz, Sonderrecht), 64–68 (Ausnahme und ihre Grenzen), 69–85 (Verhältnismäßigkeit), 95–108 (Auslegung und Anwendung)
– BVerfG, Urt. v. 15.1.1958 – 1 BvR 400/51, BVerfGE 7, 198, S. 209 f. (Lüth: Begriff des allgemeinen Gesetzes)

Hinweise: Swantje und Professor Ahlborn sind erfundene Figuren. Reale Beteiligte werden nicht dargestellt, die Veranstaltung wird nicht gezeigt. Die Wechselwirkungslehre erklärt die Folge zum Lüth-Urteil, die Versammlungsfreiheit die Folge zum Brokdorf-Beschluss.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#WunsiedelBeschluss #Grundrechte #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("zwanzigsten August 2005", "20. August 2005"), ("Brockdorf-Beschluss", "Brokdorf-Beschluss"),
             ("\nSTGB.", "\nStGB."), ("Abs. 1 und zwei", "Abs. 1 und 2"), ("Abs. 1 S.\n1, ", "Abs. 1 Satz 1,\n"),
             ("Ahlborn: ", "Professor Ahlborn: ")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|STGB|Brockdorf|Römisch", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
