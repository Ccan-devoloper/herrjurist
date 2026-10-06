"""Nachbearbeitung der Upload-Texte für Folge 202 (nach meta_199.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen, Daten).
Aufruf: python3 meta_202.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Tipprunde ohne Tippschein, Sachverhalt"),
       (T("ansp"), "Anspruch aus § 280 Abs. 1 BGB: Schuldverhältnis?"),
       (T("rbw"), "Vertrag oder Gefälligkeit? Rechtsbindungswille"),
       (T("urteil"), "Der Fall des BGH: II ZR 12/73, § 762 und § 763 BGB"),
       (T("bind"), "Was bindet die Tipprunde? Der Leitsatz"),
       (T("warum"), "Warum keine Pflicht? Die Gründe des BGH"),
       (T("anders"), "Ausnahmen und Ergebnis"),
       (T("delikt"), "Deliktsrecht: § 823 Abs. 1 BGB"),
       (T("garten"), "Abgrenzung: Haftung bei Gefälligkeiten"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Gefälligkeitsverhältnis oder Vertrag? Der Lottogemeinschaft-Fall (BGH NJW 1974, 1705): Haftet der Kollege nach §§ 280 Abs. 1, 241 BGB, wenn er den Tippschein vergisst?

Der Fall: Erna, Ulf und Gerold spielen seit Jahren als Tipprunde Lotto. Jede Woche zahlt jeder 5 € an Gerold, der den Lottoschein ohne Entgelt ausfüllt und abgibt. An einem Samstag vergisst er ihn – mit ihren Zahlen hätte die Runde 12.000 € gewonnen. Ulf verlangt: „Dann schuldest du Erna und mir je 4.000 €.“

Inhalt:
– Anspruch aus § 280 Abs. 1 BGB, Schuldverhältnis nach § 241 Abs. 1 BGB im Wortlaut
– Rechtsbindungswille oder Gefälligkeit: objektiver Beobachter, wirtschaftliche Interessen, Gefälligkeit des täglichen Lebens
– Der Fall des BGH: kein Spiel nach § 762 BGB, staatlich genehmigte Lotterie nach § 763 BGB
– Was bindet die Tipprunde: Gewinnverteilung ja, Einreichen des Scheins in der Regel nicht (Leitsatz)
– Die Gründe: Haftungsrisiko, Unentgeltlichkeit, Spielgewinn als Glücksfall, gemeinsames Spiel
– Ausnahmen: Entgelt, geschäftliche Zwecke, besondere Vereinbarung
– Deliktsrecht: § 823 Abs. 1 BGB schützt das Vermögen als solches nicht
– Abgrenzung: Haftung bei Gefälligkeiten mit Rechtsgutsverletzung
– Klausurtipp, Prüfschema, Merksatz

Normen: §§ 241 Abs. 1, 280 Abs. 1, 157, 762, 763, 823 Abs. 1, 276 Abs. 2 BGB; § 145 BGB (Rechtsbindungswille); § 705 BGB (vom BGH offengelassen)

Rechtsprechung:
– BGH, Urt. v. 16.5.1974 – II ZR 12/73, NJW 1974, 1705 (Lottospielgemeinschaft)
– BGH, Urt. v. 23.7.2015 – III ZR 346/14, Rn. 8 (Rechtsbindungswille, Gefälligkeit des täglichen Lebens)
– BGH, Urt. v. 5.4.2018 – III ZR 211/17, Rn. 19 (Vermögen als solches nicht von § 823 Abs. 1 BGB geschützt)
– BGH, Urt. v. 26.4.2016 – VI ZR 467/15, Rn. 8, 10 (Haftung bei Gefälligkeit unter Nachbarn)

Hinweise: Angebot und Annahme sowie den Rechtsbindungswillen beim Angebot erklärt das Video zu §§ 145 ff. BGB. Ob die Tipprunde eine Gesellschaft bürgerlichen Rechts ist, hat der BGH offengelassen; heute gelten §§ 705 ff. BGB in der Fassung seit 1.1.2024. Personen frei erfunden, keine Lotterie-Marke.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Gefälligkeitsverhältnis #BGBAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei):( |\n)", lambda m: {"eins": "I.", "zwei": "II."}[m.group(1)] + m.group(2), srt)
srt = re.sub(r"Römisch zwei: ", "II. ", srt)
for a, b in [("fünf Euro", "5 Euro"), ("zwölftausend Euro", "12.000 Euro"), ("viertausend Euro", "4.000 Euro"),
             ("neunzehnhundertvierundsiebzig", "1974"), ("zehntausendfünfhundertfünfzig Mark", "10.550 Mark")]:
    srt = srt.replace(a, b)
for a, b in [(r"fünf\nEuro", "5\nEuro"), (r"zwölftausend\nEuro", "12.000\nEuro"), (r"viertausend\nEuro", "4.000\nEuro"),
             (r"zehntausendfünfhundertfünfzig\nMark", "10.550\nMark")]:
    srt = re.sub(a, b, srt)
for w, z in (("Erstens", "1."), ("Zweitens", "2."), ("Drittens", "3.")):
    srt = re.sub(rf"(?m)^{w}: ", f"{z} ", srt)
    srt = re.sub(rf"\. {w}:", f". {z}", srt)
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert not re.search(r"zwölftausend|viertausend|fünf Euro|neunzehnhundert|Römisch|Erstens|Zweitens", srt, re.I), \
    re.findall(r".{20}(?:zwölftausend|viertausend|fünf Euro|neunzehnhundert|Römisch|Erstens|Zweitens).{10}", srt, re.I)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
