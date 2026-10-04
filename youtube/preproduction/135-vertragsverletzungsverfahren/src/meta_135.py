"""Nachbearbeitung der Upload-Texte für Folge 135 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fällen, Inhalt, Normen, Rechtsprechung mit Rn., Lizenzzeile,
zusätzliche Tags; Untertitel: Prüfung, dass Zahlen in Ziffern stehen.
Aufruf: python3 meta_135.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Nitrat-Fall: Kommission gegen Deutschland – mit Sachverhalt"),
       (T("verw"), "Aufbau und Wortlaut Art. 258 AEUV"),
       (T("zul"), "A. Zulässigkeit: Zuständigkeit, Parteifähigkeit"),
       (T("vorv"), "Vorverfahren und deckungsgleicher Streitgegenstand"),
       (T("zeit"), "Maßgeblicher Zeitpunkt, Rechtsschutzbedürfnis"),
       (T("bgr"), "B. Begründetheit: Verstoß und Zurechnung"),
       (T("recht"), "Rechtfertigung? Innerstaatliche Gründe"),
       (T("urt"), "C. Urteil: Feststellung, Art. 260 Abs. 1"),
       (T("wl260"), "Zwangsgeld und Pauschalbetrag, Art. 260 Abs. 2, 3"),
       (T("erg"), "Ergebnis"), (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Vertragsverletzungsverfahren nach Art. 258–260 AEUV: Vorverfahren, Klage, Urteil und Zwangsgeld – am Beispiel des Nitrat-Urteils gegen Deutschland.

Der Fall: Nach der Nitratrichtlinie muss Deutschland seine Düngeregeln nachschärfen, wenn sie nicht reichen. Im Nitratbericht von 2012 lag an rund der Hälfte der Messstellen des Belastungsmessnetzes der Nitratwert bei 50 mg/l oder darüber. Die Kommission schickt ein Mahnschreiben, dann eine begründete Stellungnahme mit Frist bis zum 11.9.2014 – und klagt 2016 vor dem Gerichtshof. Hat die Klage Erfolg?

Inhalt:
– Art. 258 AEUV im Wortlaut
– A. Zulässigkeit: Zuständigkeit des Gerichtshofs (Art. 256 Abs. 1 AEUV), Parteifähigkeit (Staatenklage Art. 259 AEUV), ordnungsgemäßes Vorverfahren mit deckungsgleichem Streitgegenstand, maßgeblicher Zeitpunkt (Fristablauf), Klageart und Rechtsschutzbedürfnis
– B. Begründetheit: Verstoß des Mitgliedstaats, Zurechnung aller Stellen (auch Länder und Gerichte), keine Rechtfertigung durch innerstaatliche Gründe
– C. Urteil: Feststellungsurteil (Art. 260 Abs. 1 AEUV), zweites Verfahren mit Pauschalbetrag oder Zwangsgeld (Art. 260 Abs. 2 AEUV im Wortlaut), Art. 260 Abs. 3 AEUV
– Klausurtipp, Klausurschema, Merksatz

Normen: Art. 256, 258, 259, 260 AEUV; Art. 5 Abs. 5, 7 Richtlinie 91/676/EWG (Nitratrichtlinie)

Rechtsprechung:
– EuGH, Urt. v. 21.6.2018 – C-543/16, Kommission/Deutschland (Nitrat), Rn. 20–25, 52 f., 59–61, 70, 113 f., 132–136
– EuGH, Urt. v. 10.5.2001 – C-152/98, Kommission/Niederlande, Rn. 21, 23–25
– EuGH, Urt. v. 11.8.1995 – C-431/92, Kommission/Deutschland (Großkrotzenburg), Rn. 19–21
– EuGH, Urt. v. 4.10.2018 – C-416/17, Kommission/Frankreich, Rn. 106 f.
Nachgang: Kommission, Pressemitteilung INF/19/4251 vom 25.7.2019 (Aufforderungsschreiben nach Art. 260 AEUV).

Kapitel:
{kapitel}

Antonia und Konstantin sind ausgedacht; der Nitrat-Fall ist echt und nach dem Urteil dargestellt. Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

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
for t in ("Vertragsverletzungsverfahren", "Art. 259 AEUV", "Nitratrichtlinie", "Prüfungsschema Europarecht", "C-543/16"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
