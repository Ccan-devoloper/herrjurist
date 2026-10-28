"""Nachbearbeitung der Upload-Texte für Folge 205 (nach meta_160.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn.,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Römisch → I.).
Kein Name des echten Magazins, des Beschwerdeführers oder anderer realer Beteiligter.
Aufruf: python3 meta_205.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Der Name im Onlinearchiv"),
       (T("sv"), "Sachverhalt"),
       (T("weg"), "Der echte Fall: Recht auf Vergessen I"),
       (T("mass"), "I. Prüfungsmaßstab: Grundgesetz oder Charta?"),
       (T("apr"), "II. Schutzbereich: Persönlichkeitsrecht"),
       (T("aeuss"), "Die Zeit zählt: Möglichkeit des Vergessens"),
       (T("presse"), "III. Gegenrecht: Pressefreiheit und Archiv"),
       (T("dritt"), "Mittelbare Drittwirkung, Prüfpflichten"),
       (T("abw"), "IV. Abwägung: Zeitablauf, Breitenwirkung, Verhalten"),
       (T("stufen"), "Abgestufte Schutzmaßnahmen"),
       (T("erg"), "Ergebnis des Bundesverfassungsgerichts"),
       (T("zur"), "Lösung des Falls"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Recht auf Vergessen I (BVerfGE 152, 152): Muss ein alter Artikel über deinen Strafprozess aus dem Online-Archiv? Art. 2 I i.V.m. 1 I GG vs. Pressefreiheit.

Der Fall: Gerhild sucht den Namen ihres neuen Nachbarn, Herrn Dornbusch. Der erste Treffer ist ein über 30 Jahre alter Artikel im Onlinearchiv eines Nachrichtenmagazins über seinen Strafprozess. Herr Dornbusch hat seine Strafe längst verbüßt. Muss sein Name aus dem Archiv? Unser Fall bildet den Grundfall des Beschlusses Recht auf Vergessen I nach, den das Bundesverfassungsgericht am 6. November 2019 entschieden hat.

Inhalt:
– das Verfahren: Unterlassungsklage, Urteil des Bundesgerichtshofs, Urteilsverfassungsbeschwerde
– I. Prüfungsmaßstab: Medienprivileg, nicht vollständig vereinheitlichtes Unionsrecht, daher primär das Grundgesetz; Abgrenzung zu Recht auf Vergessen II
– II. Schutzbereich: allgemeines Persönlichkeitsrecht, Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG (im Wortlaut), äußerungsrechtliche Ausprägung, Zeitdimension, „Möglichkeit des Vergessens“, kein Recht auf Löschung von allem
– III. Gegenrecht: Pressefreiheit, Art. 5 Abs. 1 Satz 2 GG (im Wortlaut), Onlinearchive, mittelbare Drittwirkung, Prüfpflicht erst nach Beanstandung
– IV. Abwägung: Zeitablauf, Breitenwirkung über die Namenssuche, Verhalten des Betroffenen, abgestufte Schutzmaßnahmen statt Löschung
– Ergebnis, Lösung des Falls, Klausurtipp, Prüfschema, Merksatz

Normen: Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG; Art. 5 Abs. 1 Satz 1 und 2 GG

Rechtsprechung:
– BVerfG, Beschl. v. 6.11.2019 – 1 BvR 16/13, BVerfGE 152, 152 (Recht auf Vergessen I), Leitsätze 1a, 2a–d; Rn. 4–6, 37, 41 f., 74–76, 79, 91 f., 94, 105, 107, 109, 112 f., 115, 118 f., 123, 128–141, 145–153, 155, 157
– BVerfG, Beschl. v. 6.11.2019 – 1 BvR 276/17, BVerfGE 152, 216 (Recht auf Vergessen II), Rn. 33 f., 42, 50 (nur zur Abgrenzung)

Hinweise: Gerhild, Herr Dornbusch und Herr Stöver sind erfundene Figuren; sie bilden den Grundfall nach. Reale Beteiligte, das Magazin und die Tat werden nicht dargestellt. Die Ausstrahlung der Grundrechte ins Zivilrecht erklärt die Folge zum Lüth-Urteil.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#RechtaufVergessen #Persönlichkeitsrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("Dornbusch: Willkommen", "Herr Dornbusch: Willkommen"), ("Dornbusch: Nehmen", "Herr Dornbusch: Nehmen"),
             ("Stöver: Der Bericht", "Herr Stöver: Der Bericht"), ("über dreißig\nJahre", "über 30\nJahre"),
             ("über dreißig Jahre", "über 30 Jahre"), ("Recht auf Vergessen eins.", "Recht auf Vergessen I."),
             ("auf Vergessen zwei vom", "auf Vergessen II vom"), ("Art. 5 Abs. 1 S. 2:", "Art. 5 Abs. 1 Satz 2:")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"Römisch (eins|zwei|drei|vier):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV."}[m.group(1)] + m.group(2), srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Römisch|dreißig", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
