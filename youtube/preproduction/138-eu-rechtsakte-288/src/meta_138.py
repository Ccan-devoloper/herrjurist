"""Nachbearbeitung der Upload-Texte für Folge 138 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Lizenzzeile,
zusätzliche Tags; Untertitel: Daten, Artikel und Paragrafen in Ziffern.
Aufruf: python3 meta_138.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: DSGVO sofort, Pauschalreiserichtlinie erst über das BGB? (mit Sachverhalt)"),
       (T("ebene"), "Primär- und Sekundärrecht"), (T("abs1"), "Art. 288 AEUV im Wortlaut"),
       (T("vo"), "Verordnung: DSGVO und BDSG"), (T("rl"), "Richtlinie: Umsetzungsfrist, §§ 651a ff. BGB"),
       (T("be"), "Beschluss, Empfehlung, Stellungnahme"), (T("prob"), "Nicht umgesetzte Richtlinie: vertikale Wirkung"),
       (T("horiz"), "Keine Wirkung zwischen Privaten: Faccini Dori"),
       (T("ausw"), "Auswege: richtlinienkonforme Auslegung, Francovich, Dillenkofer"),
       (T("erg"), "Ergebnis"), (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema als Tabelle"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""EU-Rechtsakte nach Art. 288 AEUV: Warum eine Verordnung unmittelbar gilt, eine Richtlinie aber umgesetzt werden muss – Primär- und Sekundärrecht, Verordnung, Richtlinie, Beschluss und die Folgen einer nicht umgesetzten Richtlinie.

Der Fall: Herr Stegemann führt ein kleines Reisebüro. Seine Datenschutzbeauftragte erklärt ihm, dass die Datenschutz-Grundverordnung unmittelbar gilt. Sein Pauschalreiserecht findet er dagegen im BGB und nicht in der Pauschalreiserichtlinie – warum?

Inhalt:
– Primärrecht (EUV, AEUV) und Sekundärrecht
– Art. 288 AEUV im Wortlaut: Verordnung, Richtlinie, Beschluss, Empfehlung, Stellungnahme
– Verordnung: DSGVO, gilt ab 25.5.2018 unmittelbar in jedem Mitgliedstaat; das BDSG ergänzt nur
– Richtlinie: verbindlich nur das Ziel, Umsetzungsfrist; Pauschalreiserichtlinie (EU) 2015/2302 und §§ 651a ff. BGB
– Beschluss (Beispiel Beihilfe, Art. 108 Abs. 2 AEUV), Empfehlung und Stellungnahme
– Nicht umgesetzte Richtlinie: vertikale unmittelbare Wirkung (Ratti, Becker), keine Wirkung zwischen Privaten (Faccini Dori)
– Auswege: richtlinienkonforme Auslegung und Staatshaftung (Francovich, Dillenkofer)
– Klausurtipp, Klausurschema als Tabelle, Merksatz

Normen: Art. 288 AEUV, Art. 1 Abs. 3 EUV, Art. 1 Abs. 2 AEUV, Art. 108 Abs. 2 AEUV, Art. 99 DSGVO, § 1 Abs. 5 BDSG, Art. 28 RL (EU) 2015/2302, §§ 651a ff. BGB, Art. 229 § 42 EGBGB

Rechtsprechung:
– EuGH, Urt. v. 5.4.1979 – Rs. 148/78, Ratti, Slg. 1979, 1629, Rn. 22 f., 43
– EuGH, Urt. v. 19.1.1982 – Rs. 8/81, Becker, Slg. 1982, 53, Rn. 24 f.
– EuGH, Urt. v. 14.7.1994 – Rs. C-91/92, Faccini Dori, Slg. 1994, I-3325, Rn. 20, 25–27
– EuGH, Urt. v. 19.11.1991 – verb. Rs. C-6/90 und C-9/90, Francovich, Slg. 1991, I-5357, Rn. 39 f.
– EuGH, Urt. v. 8.10.1996 – verb. Rs. C-178/94 u. a., Dillenkofer, Slg. 1996, I-4845, Rn. 29

Kapitel:
{kapitel}

Der Übungsfall (Herr Stegemann, Frau Kettner) ist ausgedacht. Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Europarecht #Art288AEUV #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
ERS = [(r"fünfundzwanzigsten\s+Mai\s+zweitausendachtzehn", "25. Mai 2018"),
       (r"ersten\s+Januar\s+zweitausendachtzehn", "1. Januar 2018"), (r"ersten\s+Juli\s+zweitausendachtzehn", "1. Juli 2018"),
       (r"Artikel\s+zweihundertachtundachtzig", "Art. 288"),
       (r"Paragrafen\s+sechshunderteinundfünfzig\s+a\s+folgende", "§§ 651a ff."),
       (r"651a(\s+)folgende", r"651a\1ff."), (r"Absatz\s+eins\b", "Absatz 1"), (r"Absatz\s+zwei\b", "Absatz 2"), (r"Absatz\s+drei\b", "Absatz 3"),
       (r"Absatz\s+vier\b", "Absatz 4"), (r"Absatz\s+fünf\b", "Absatz 5"), (r"B\.G\.B\.", "BGB")]
for a, b in ERS:
    srt = re.sub(a, b, srt)
for w in ("zweitausendachtzehn", "zweihundert", "sechshundert", "B.G.B."):
    assert w not in srt, w
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Verordnung", "Richtlinie", "Beschluss", "unmittelbare Wirkung Richtlinie", "Francovich", "Faccini Dori"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
