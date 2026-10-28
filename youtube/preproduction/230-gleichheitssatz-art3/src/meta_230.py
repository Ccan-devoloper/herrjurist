"""Nachbearbeitung der Upload-Texte für Folge 230 (nach meta_208.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn./Seiten,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Normangaben, Römisch → I.).
Keine Namen des realen Beschwerdeführers und keine realen Orte.
Aufruf: python3 meta_230.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Einheimische zahlen weniger"),
       (T("frage"), "Die Frage und der echte Fall"),
       (T("sv"), "Sachverhalt und Wortlaut Art. 3 Abs. 1 GG"),
       (T("a13"), "Bindung: auch die Gesellschaft der Gemeinde"),
       (T("zwei"), "Zwei Schritte und Ungleichbehandlung"),
       (T("mass"), "Maßstab: die Willkürformel"),
       (T("neu"), "Die Neue Formel"),
       (T("heute"), "Heute: stufenloser Maßstab"),
       (T("wohn"), "Der Wohnort als Grund?"),
       (T("real"), "Der echte Fall: 2 BvR 470/08"),
       (T("erg"), "Ergebnis und Lösung des Falls"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Gleichheitssatz Art. 3 I GG prüfen: Vergleichspaar, Ungleichbehandlung, Rechtfertigung von der Willkürformel über die Neue Formel bis zum stufenlosen Maßstab – am Fall des Einheimischentarifs im Freizeitbad.

Der Fall: Im Freizeitbad einer kleinen Gemeinde zahlen Einheimische 6 €, alle anderen 9 €. Betrieben wird das Bad von einer Gesellschaft, die ganz der Gemeinde gehört; es wirbt um Urlauber und soll Gewinn bringen. Martha wohnt im Nachbarort – ist ihr Mehrpreis gerecht? Unser Fall folgt einem Beschluss des Bundesverfassungsgerichts vom 19. Juli 2016.

Inhalt:
– Art. 3 Abs. 1 GG und Art. 1 Abs. 3 GG (im Wortlaut): Grundrechtsbindung auch öffentlicher Unternehmen in Privatrechtsform
– Prüfung in zwei Schritten: Ungleichbehandlung von wesentlich Gleichem, Rechtfertigung
– Vergleichsgruppen, gemeinsamer Oberbegriff, derselbe Träger
– Willkürformel (BVerfGE 1, 14), Neue Formel (BVerfGE 55, 72) und der heutige stufenlose Maßstab
– Wann strenger geprüft wird: Merkmale der Person, Nähe zu Art. 3 Abs. 3 GG, Freiheitsrechte
– Der Wohnort als Grund: Sachgründe, die mit dem Wohnort untrennbar zusammenhängen
– Der echte Fall, Lösung, Klausurtipp, Prüfschema, Merksatz

Normen: Art. 3 Abs. 1 GG; Art. 3 Abs. 3 GG; Art. 1 Abs. 3 GG

Rechtsprechung:
– BVerfGE 1, 14 <52> (Willkürformel)
– BVerfGE 55, 72 <88>, Beschl. v. 7.10.1980 – 1 BvL 50/79 u. a. (Neue Formel)
– BVerfGE 88, 87 <96> (vom bloßen Willkürverbot bis zu strengen Verhältnismäßigkeitserfordernissen)
– BVerfGE 138, 136 Rn. 121 f. (stufenloser Prüfungsmaßstab)
– BVerfGE 134, 1 Rn. 55–61 (Vergleichbarkeit, Wohnsitz, derselbe Träger)
– BVerfG (3. Kammer des Zweiten Senats), Beschl. v. 19.7.2016 – 2 BvR 470/08 (Einheimischentarif im Freizeitbad), Rn. 2–4, 24–43, 60

Hinweise: Martha, Frau Dittmer und Herr Kühnel sind erfundene Figuren; der Fall folgt dem echten Fall. Der reale Beschwerdeführer wird nicht genannt.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Gleichheitssatz #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(Art\. \d+)\n(Abs\. \d+)", r"\1 \2\n", srt)
srt = re.sub(r" Art\. (\d+)\n\n(\d+\n[^\n]+\n)Abs\. (\d+)", r"\n\n\2Art. \1 Abs. \3", srt)   # Normangabe über Blockgrenze
for a, b in [("Kühnel: Wer hier", "Herr Kühnel: Wer hier"), ("Dittmer: Einmal", "Frau Dittmer: Einmal"),
             ("zahlt sechs Euro.", "zahlt 6 Euro."), ("Alle anderen zahlen neun.", "Alle anderen zahlen 9."),
             ("sie neun Euro zahlen", "sie 9 Euro zahlen"), ("zahle drei Euro mehr", "zahle 3 Euro mehr"),
             ("vom neunzehnten Juli\n\n", "vom 19. Juli\n\n"), ("Art. 3 Abs. 1:", "Art. 3 Abs. 1 GG:"),
             ("Nach Art. 1 Abs. 3 binden", "Nach Art. 1 Abs. 3 GG binden"), ("zahlen sechs\nEuro, die anderen neun:", "zahlen 6\nEuro, die anderen 9:"),
             ("denen aus Abs. 3 kommen", "denen aus Abs. 3 kommen")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"(Art\. 3 Abs\. 1) verletzt", r"\1 GG verletzt", srt)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"Römisch|sechs Euro|neun Euro|neunzehnten", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
