"""Nachbearbeitung der Upload-Texte für Folge 160 (nach meta_154.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit
Seite bzw. Rn., Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechername, Römisch → I.).
Keine Namen der Esra-Klägerinnen und des Autors.
Aufruf: python3 meta_160.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Der Ex erkennt sich im Roman"),
       (T("a53"), "I. Schutzbereich: Art. 5 Abs. 3 GG, vorbehaltlos"),
       (T("kunst"), "Drei Kunstbegriffe"),
       (T("werk"), "Werkbereich und Wirkbereich, II. Eingriff"),
       (T("schranke"), "III. Schranken: kollidierendes Verfassungsrecht"),
       (T("apr"), "Allgemeines Persönlichkeitsrecht"),
       (T("meph"), "Der Mephisto-Beschluss (1971)"),
       (T("esra"), "Der Esra-Beschluss (2007)"),
       (T("jed"), "Die Je-desto-Formel"),
       (T("erg2"), "Ergebnis im Esra-Fall"),
       (T("zur"), "Lösung des Falls"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Mephisto-Beschluss (BVerfGE 30, 173) und Esra: Wann verletzt ein Roman das Persönlichkeitsrecht? Kunstfreiheit nach Art. 5 III GG und Je-desto-Formel.

Der Fall: Bei einem Leseabend liest die Autorin Liesel aus ihrem neuen Roman. Ihr früherer Partner Winfried erkennt sich in der Hauptfigur wieder, bis in intime Szenen der Beziehung. Darf ein Gericht den Roman verbieten? Antworten geben zwei Klassiker des Bundesverfassungsgerichts: der Mephisto-Beschluss von 1971 und der Esra-Beschluss von 2007.

Inhalt:
– Art. 5 Abs. 3 Satz 1 GG (im Wortlaut): vorbehaltlos gewährleistete Kunstfreiheit
– materieller, formaler und offener Kunstbegriff; Werkbereich und Wirkbereich; auch der Verlag ist geschützt
– Eingriff durch das gerichtliche Verbot; Grundrechte beider Seiten
– Schranken: kollidierendes Verfassungsrecht, nicht Art. 5 Abs. 2 GG; allgemeines Persönlichkeitsrecht, Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG (im Wortlaut)
– Mephisto: Klaus Manns Roman, Vorbild Gustaf Gründgens, postmortaler Schutz aus der Menschenwürde, Abbild und Urbild, Stimmengleichheit 3:3
– Esra: kunstspezifische Betrachtung, Vermutung der Fiktionalität, Je-desto-Formel, Intimsphäre, Ergebnis
– Lösung des Falls, Klausurtipp (praktische Konkordanz), Prüfschema, Merksatz

Normen: Art. 5 Abs. 3 Satz 1 GG; Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG; Art. 5 Abs. 2 GG

Rechtsprechung:
– BVerfG, Beschl. v. 24.2.1971 – 1 BvR 435/68, BVerfGE 30, 173 (Mephisto), S. 188 f. (Kunstbegriff), 189 (Werk- und Wirkbereich), 191–193 (vorbehaltlos, Schranken), 194 (postmortaler Schutz), 195 (Abbild und Urbild), 195 f. (Stimmengleichheit)
– BVerfG, Beschl. v. 13.6.2007 – 1 BvR 1783/05, BVerfGE 119, 1 (Esra), Leitsätze 2 und 4; Rn. 57 (teilweise begründet), 68–71, 74, 84, 88, 90, 92–104
– BVerfG, Beschl. v. 17.7.1984 – 1 BvR 816/82, BVerfGE 67, 213, S. 226 f. (Anachronistischer Zug: formaler und offener Kunstbegriff)
– BVerfG, Beschl. v. 16.5.1995 – 1 BvR 1087/91, BVerfGE 93, 1, S. 21 (praktische Konkordanz)

Hinweise: Liesel, Winfried und Frau Hollerbach sind erfundene Figuren. Reale Personen werden nicht dargestellt; im Esra-Fall nennen wir keine Namen. Das Grundschema erklärt die Folge zur Grundrechtsprüfung, die Ausstrahlung der Grundrechte ins Zivilrecht die Folge zum Lüth-Urteil.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#MephistoBeschluss #Kunstfreiheit #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("Hollerbach: ", "Frau Hollerbach: "), ("Art. 5 Abs. 3 S. 1:", "Art. 5 Abs. 3 Satz 1:"),
             ("drei zu drei.", "3:3."), ("Sechsunddreißig Jahre", "36 Jahre")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Römisch", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
