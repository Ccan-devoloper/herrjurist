"""Nachbearbeitung der Upload-Texte für Folge 091 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Seitenzahlen, Lizenzzeile,
zusätzliche Tags; Untertitel: Datum und Paragrafen in Ziffern.
Aufruf: python3 meta_091.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Irmgard, Wolfram, Ulrich und der Katzenkönig"), (T("tat"), "Im Blumenladen – und die Frage"),
       (T("sv"), "Sachverhalt zum Nachlesen"), (T("echt"), "Der echte Fall: BGHSt 35, 347"),
       (T("ua"), "A. Ulrich: versuchter Mord, Heimtücke"), (T("n34"), "Rechtswidrigkeit: § 34 StGB, Leben gegen Leben"),
       (T("n35"), "Schuld: § 35 StGB"), (T("p17"), "Verbotsirrtum § 17 StGB: vermeidbar"),
       (T("hb"), "B. Irmgard und Wolfram: § 25 Abs. 1 Alt. 2 StGB"), (T("vp"), "Streit: Verantwortungsprinzip und BGH"),
       (T("formel"), "Die Formel des BGH: Täter hinter dem Täter"), (T("subs"), "Subsumtion: Tatherrschaft kraft Wissens"),
       (T("heimt"), "Warum der Streit zählt: Heimtücke und niedrige Beweggründe"), (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Katzenkönig-Fall (BGHSt 35, 347): Kann mittelbare Täterschaft nach § 25 I Alt. 2 StGB bestehen, obwohl der Vordermann voll verantwortlich handelt? Der Klassiker zum „Täter hinter dem Täter“ – Schritt für Schritt wie in der Klausur.

Der Fall (vereinfacht, andere Namen): Irmgard und Wolfram bringen den leicht beeinflussbaren Polizeibeamten Ulrich dazu, an den „Katzenkönig“ zu glauben. Sie reden ihm ein, der Katzenkönig verlange eine Frau als Menschenopfer, sonst vernichte er Millionen Menschen. Ulrich greift die ahnungslose Frau in ihrem Blumenladen an, um sie zu töten; sie überlebt. Ist Ulrich strafbar – und sind Irmgard und Wolfram nur Anstifter oder selbst Täter?

Inhalt:
– A. Ulrich: versuchter Mord (Heimtücke), kein Rücktritt
– Rechtswidrigkeit: § 34 StGB scheitert, Leben gegen Leben ist nicht abwägbar (Bewertungsirrtum)
– Schuld: § 35 StGB scheitert, auch als vermeintlicher Notstand nach Abs. 2
– Verbotsirrtum § 17 StGB im Wortlaut: vermeidbar, also schuldhaft – Milderung möglich
– B. Irmgard und Wolfram: § 25 Abs. 1 StGB im Wortlaut, mittelbare Täterschaft trotz voll verantwortlichen Vordermanns?
– Streit: Verantwortungsprinzip (dann nur Anstiftung, § 26 StGB) gegen die Tatherrschaftsformel des BGH
– Warum der Streit hier zählt: Heimtücke-Kenntnis bei der Anstiftung, niedrige Beweggründe als Täter
– Ergebnis, Klausurtipp, Klausurschema, Merksatz

Normen: §§ 17, 22, 23 Abs. 1, 25 Abs. 1 Alt. 2, 26, 34, 35, 211, 212 StGB

Rechtsprechung:
– BGH, Urt. v. 15.9.1988 – 4 StR 352/88, BGHSt 35, 347 (Katzenkönig): S. 349 (versuchter heimtückischer Mord), S. 350 (§ 34: Leben gegen Leben, vermeidbarer Verbotsirrtum; § 35), S. 351–353 (Verantwortungsprinzip, Vermeidbarkeit kein taugliches Abgrenzungskriterium), S. 354 f. (Formel und Tatherrschaft kraft überlegenen Wissens)

Kapitel:
{kapitel}

Die Darstellung ist vereinfacht, die Namen sind geändert. Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Katzenkönig #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"fünfzehnten September\s+neunzehnhundertachtundachtzig", "15. September 1988", srt)
srt = re.sub(r"15\. September\s+1988", "15. September 1988", srt)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Katzenkönig", "Verantwortungsprinzip", "Tatherrschaft", "Verbotsirrtum § 17", "Irrtumsherrschaft"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
