"""Nachbearbeitung der Upload-Texte für Folge 131 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fällen, Inhalt, Normen, Rechtsprechung mit Rn., Lizenzzeile,
zusätzliche Tags; Untertitel: Artikel mit „AEUV“ ergänzt, wo das Gesprochene nur „Artikel …“ sagt, bleibt unverändert.
Aufruf: python3 meta_131.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Drei Fälle: Gericht, Unternehmen, Kommission"), (T("sv"), "Sachverhalt zum Nachlesen"),
       (T("ueber"), "Überblick: Wer? Wogegen? Voraussetzungen? Folge?"),
       (T("wl267"), "1. Vorabentscheidungsverfahren, Art. 267 AEUV"),
       (T("wer1"), "Vorlage: Wer legt vor? CILFIT, Foto-Frost"),
       (T("bind"), "Bindung, Art. 101 GG, Lösung Fall 1"),
       (T("ni"), "2. Nichtigkeitsklage, Art. 263 AEUV: Kläger"),
       (T("wl263"), "Art. 263 Abs. 4: Plaumann und Verordnungscharakter"),
       (T("frist"), "Frist, Gericht der EU, Nichtigerklärung, Lösung Fall 2"),
       (T("wl258"), "3. Vertragsverletzungsverfahren, Art. 258 AEUV"),
       (T("wer3"), "Vorverfahren, Feststellungsurteil, Art. 260 AEUV"),
       (T("l3"), "Lösung Fall 3, Untätigkeits- und Schadensersatzklage"),
       (T("erg"), "Ergebnis"), (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Klagearten EuGH im Überblick: Vorabentscheidung (Art. 267 AEUV), Nichtigkeitsklage (Art. 263 AEUV) und Vertragsverletzungsverfahren (Art. 258 AEUV) – jeweils mit Wer? Wogegen? Voraussetzungen? Folge?

Drei Fälle: Richterin Eichhorn am Verwaltungsgericht zweifelt, wie ein Begriff einer EU-Verordnung auszulegen ist. Die Kommission verhängt gegen die Baustofffirma von Frau Pfister per Beschluss eine Geldbuße. Und Herr Teichmann von der Kommission hält ein deutsches Gesetz für einen Verstoß gegen die Dienstleistungsfreiheit. Welches Verfahren passt jeweils?

Inhalt:
– Vorabentscheidungsverfahren: Auslegung und Gültigkeit, Vorlagerecht und Vorlagepflicht letzter Instanz (Art. 267 Abs. 2, 3 AEUV), Ausnahmen nach CILFIT (acte éclairé, acte clair), Foto-Frost, Bindung, Entzug des gesetzlichen Richters (Art. 101 Abs. 1 S. 2 GG)
– Nichtigkeitsklage: privilegierte, teilprivilegierte und nichtprivilegierte Kläger, Art. 263 Abs. 4 AEUV im Wortlaut, Plaumann-Formel, Rechtsakte mit Verordnungscharakter (Inuit), Frist von zwei Monaten, Zuständigkeit des Gerichts der EU, Nichtigerklärung
– Vertragsverletzungsverfahren: Art. 258 AEUV im Wortlaut, Mahnschreiben und begründete Stellungnahme, Feststellungsurteil, Pauschalbetrag oder Zwangsgeld (Art. 260 Abs. 2 AEUV)
– Untätigkeitsklage (Art. 265 AEUV) und Schadensersatzklage (Art. 340 AEUV)
– Klausurtipp, Klausurschema als Übersicht, Merksatz

Normen: Art. 256, 258, 259, 260, 263, 264, 265, 267, 340 AEUV; Art. 51 Satzung des Gerichtshofs; Art. 101 Abs. 1 S. 2 GG

Rechtsprechung:
– EuGH, Urt. v. 15.7.1963 – Rs. 25/62, Plaumann, Slg. 1963, 213, 238
– EuGH, Urt. v. 6.10.1982 – Rs. 283/81, CILFIT, Rn. 9, 21
– EuGH, Urt. v. 22.10.1987 – Rs. 314/85, Foto-Frost, Rn. 15, 20
– EuGH, Urt. v. 10.5.2001 – C-152/98, Kommission/Niederlande, Rn. 23 f.
– EuGH, Urt. v. 5.10.2010 – C-173/09, Elchinov, Rn. 29
– EuGH, Urt. v. 3.10.2013 – C-583/11 P, Inuit Tapiriit Kanatami, Rn. 60 f., 72
– EuGH, Urt. v. 6.10.2021 – C-561/19, Consorzio Italian Management, Rn. 33, 35, 54
– BVerfG, Beschl. v. 6.7.2010 – 2 BvR 2661/06, BVerfGE 126, 286 (Honeywell), Rn. 88

Kapitel:
{kapitel}

Die drei Fälle (Richterin Eichhorn, Frau Pfister, Herr Teichmann) sind ausgedacht. Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Europarecht #EuGH #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for w in ("zweihundert", "hunderteins", "dreihundert"):
    assert w not in srt, w
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Klagearten EuGH", "Plaumann-Formel", "CILFIT", "Vorlagepflicht", "Art. 260 AEUV"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
