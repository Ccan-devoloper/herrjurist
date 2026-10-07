"""Nachbearbeitung der Upload-Texte für Folge 241 (nach meta_160.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Seite,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (StGB, Satz, Sprechername, Römisch → I.).
Die reale Person wird nur in der Fallbezeichnung „Strauß-Karikatur“ genannt.
Aufruf: python3 meta_241.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Politikerin als Schwein gezeichnet"),
       (T("a53"), "I. Schutzbereich: Ist eine Karikatur Kunst?"),
       (T("niveau"), "Kunst und Meinung, II. Eingriff"),
       (T("vorb"), "III. Schranken: kollidierendes Verfassungsrecht"),
       (T("echt"), "Der echte Fall: Strauß-Karikatur (1987)"),
       (T("deut"), "Aussagekern und Einkleidung"),
       (T("kern1"), "Entwertung als Person: Menschenwürde"),
       (T("abw"), "Keine Abwägung: Ergebnis"),
       (T("zur"), "Lösung des Falls"),
       (T("gegen"), "Gegenfall: Politiker als Tier"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Strauß-Karikatur (BVerfGE 75, 369): Wie weit reicht die Kunstfreiheit nach Art. 5 III GG bei Satire? Aussagekern, Einkleidung und Menschenwürde.

Der Fall: Der Karikaturist Meinrad zeichnet die Ministerpräsidentin Achenbach für ein Satiremagazin als Schwein, in einer herabwürdigenden Pose. „Satire darf alles“, meint die Redaktion. Das Amtsgericht verurteilt ihn wegen Beleidigung. Verletzt das seine Kunstfreiheit? Die Antwort gibt der Beschluss des Bundesverfassungsgerichts zur Strauß-Karikatur von 1987.

Inhalt:
– Art. 5 Abs. 3 Satz 1 GG (im Wortlaut): Ist eine Karikatur Kunst? Keine Niveaukontrolle
– Kunst und Meinung: Art. 5 Abs. 3 GG als spezielle Norm gegenüber Art. 5 Abs. 1 GG
– Schranken: kein Gesetzesvorbehalt, kollidierendes Verfassungsrecht, allgemeines Persönlichkeitsrecht mit seinem Kern Art. 1 Abs. 1 GG (im Wortlaut), § 185 StGB
– Der echte Fall von 1987
– Satire deuten: Aussagekern und Einkleidung, milderer Maßstab für die Einkleidung
– Entwertung als Person: Menschenwürde als absolute Schranke ohne Güterausgleich
– Lösung des Falls, Gegenfall (Tiergestalt allein), Klausurtipp, Prüfschema, Merksatz

Normen: Art. 5 Abs. 3 Satz 1 GG; Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG; Art. 5 Abs. 1, 2 GG (Abgrenzung); § 185 StGB

Rechtsprechung:
– BVerfG, Beschl. v. 3.6.1987 – 1 BvR 313/85, BVerfGE 75, 369 (Strauß-Karikatur), Leitsatz; S. 377 (Karikatur als Kunst, keine Niveaukontrolle, spezielle Norm), 377 f. (Aussagekern und Einkleidung), 379 (übliche Tierdarstellungen), 380 (Entwertung als Person, absolute Schranke), 380 f. (personale Würde des Politikers)
– BVerfG, Beschl. v. 24.2.1971 – 1 BvR 435/68, BVerfGE 30, 173 (Mephisto), S. 191, 193 (vorbehaltlos, Schranken nur aus der Verfassung)

Hinweise: Meinrad, Henriette und Ministerpräsidentin Achenbach sind erfundene Figuren. Die Karikaturen des echten Falls zeigen wir nicht, die reale Person wird nicht dargestellt. Die Kunstbegriffe erklärt die Folge zum Mephisto-Beschluss, die Meinungsfreiheit die Folge zu „Soldaten sind Mörder“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#StraußKarikatur #Kunstfreiheit #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("Achenbach: ", "Ministerpräsidentin Achenbach: "), ("Art. 5 Abs. 3 S. 1:", "Art. 5 Abs. 3 Satz 1:"),
             ("§ 185 STGB", "§ 185 StGB")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Römisch|STGB", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
