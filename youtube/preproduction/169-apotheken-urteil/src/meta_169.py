"""Nachbearbeitung der Upload-Texte für Folge 169 (nach meta_150.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Seiten,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Daten und Zahlen als Ziffern, Sprechername, Gliederungsziffern).
Aufruf: python3 meta_169.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Genug Apotheken im Stadtteil?"),
       (T("bf"), "Der echte Fall: Traunreut 1956"),
       (T("abl"), "Ablehnung und Verfassungsbeschwerde"),
       (T("a12"), "Art. 12 I GG: einheitliches Grundrecht"),
       (T("stufen"), "Drei-Stufen-Theorie, Stufe 1: Berufsausübung"),
       (T("s2"), "Stufe 2: subjektive Zulassungsvoraussetzung"),
       (T("s3"), "Stufe 3: objektive Zulassungsvoraussetzung"),
       (T("gr"), "Niedrigste Stufe zuerst"),
       (T("einord"), "Anwendung: Bedarf und Volksgesundheit"),
       (T("erg"), "Ergebnis: Art. 3 ApothekenG nichtig"),
       (T("o2"), "Zurück zum Fall: § 2 ApoG heute"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Drei-Stufen-Theorie (Apotheken-Urteil, BVerfGE 7, 377): Berufsausübung, subjektive und objektive Zulassungsschranken bei Art. 12 I GG verständlich erklärt.

Der Fall: Ein angestellter Apotheker beantragt 1956 die Erlaubnis, in Traunreut (Oberbayern) eine eigene Apotheke zu eröffnen. Nach Art. 3 Abs. 1 des bayerischen Apothekengesetzes darf eine neue Apotheke nur zugelassen werden, wenn sie im öffentlichen Interesse liegt und ihre wirtschaftliche Grundlage gesichert ist, ohne die Nachbarapotheken zu stark zu beeinträchtigen. Die Behörde lehnt ab: Für rund 6.000 Menschen genüge die vorhandene Apotheke. Am 11. Juni 1958 entscheidet das Bundesverfassungsgericht.

Inhalt:
– Einstieg: „In Ihrem Stadtteil gibt es schon genug Apotheken.“
– Art. 12 Abs. 1 GG (im Wortlaut): Berufsbegriff, Schritt in die Selbständigkeit als Berufswahl, Wahl und Ausübung als einheitliches Grundrecht
– Die drei Stufen: Berufsausübungsregelung (vernünftige Erwägungen des Gemeinwohls), subjektive Zulassungsvoraussetzung (Schutz besonders wichtiger Gemeinschaftsgüter), objektive Zulassungsvoraussetzung (nachweisbare oder höchstwahrscheinliche schwere Gefahren für ein überragend wichtiges Gemeinschaftsgut)
– Grundsatz: Eingriff auf der niedrigsten Stufe; die Stufenlehre als konkretisierte Verhältnismäßigkeit (Lehre)
– Anwendung: Bedarfsprüfung als objektive Schranke, keine belegte Gefahr für die Volksgesundheit, mildere Mittel
– Ergebnis: Art. 3 Abs. 1 ApothekenG nichtig; Niederlassungsfreiheit
– § 2 Abs. 1 ApoG heute (im Wortlaut), Klausurtipp, Prüfschema, Merksatz

Normen: Art. 12 Abs. 1 GG; § 2 Abs. 1 ApoG (früher Art. 3 Abs. 1 ApothekenG Bayern 1955)

Rechtsprechung:
– BVerfG, Urt. v. 11.6.1958 – 1 BvR 596/56, BVerfGE 7, 377 (Apotheken-Urteil): S. 377–379 (Leitsätze, Entscheidungsformel), 379–382 (Sachverhalt), 397–403 (Berufsbegriff, einheitliches Grundrecht), 405–408 (Stufen), 413–416 (Volksgesundheit, keine Gefahr), 431–443 (mildere Mittel, Niederlassungsfreiheit)
– BVerfG, Beschl. v. 6.10.1987 – 1 BvR 1086/82 u. a., BVerfGE 77, 84, S. 106; BVerfG, Beschl. v. 16.3.1971 – 1 BvR 52/66 u. a., BVerfGE 30, 292, S. 313 (Ausübungsregelung mit Wirkung nahe der Berufswahl)

Hinweise: Grete und Herr Dannemann sind erfundene Figuren; der Beschwerdeführer des echten Falls wird nicht dargestellt. „Drei-Stufen-Theorie“ ist eine Bezeichnung der Lehre; das Urteil spricht von mehreren „Stufen“. Die Prüfung der Verhältnismäßigkeit und den Aufbau der Grundrechtsprüfung erklären eigene Folgen. Nicht behandelt: Gesetzgebungszuständigkeit, Fremd- und Mehrbesitzverbot, Unionsrecht.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#DreiStufenTheorie #Berufsfreiheit #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("elften Juni", "11. Juni"), ("Dannemann: ", "Herr Dannemann: "), ("sechstausend", "6.000"),
             ("vierzig Prozent", "40 %"), ("Stufe eins", "Stufe 1"), ("Stufe zwei", "Stufe 2"), ("Stufe drei", "Stufe 3"),
             ("Satz zwei", "Satz 2")]:
    if a in srt:
        srt = srt.replace(a, b)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
assert not re.search(r"§\n|Abs\.\n", srt) and "elften" not in srt and "Römisch" not in srt, "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
