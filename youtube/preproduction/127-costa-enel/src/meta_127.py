"""Nachbearbeitung der Upload-Texte für Folge 127 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn./Seiten, Lizenzzeile,
zusätzliche Tags; Untertitel: Daten, Jahreszahlen, Artikel in Ziffern, „Enel“ als „ENEL“.
Aufruf: python3 meta_127.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Hedwig, ihre Limonade und das Amt"), (T("sv"), "Sachverhalt zum Nachlesen"),
       (T("costa"), "Der echte Fall: Costa/ENEL (1964)"), (T("ital"), "Italien gegen den Gerichtshof: eigene Rechtsordnung"),
       (T("simm"), "Simmenthal II und Fratelli Costanzo: Gerichte und Behörden"),
       (T("gueltig"), "Anwendungsvorrang statt Geltungsvorrang"), (T("grund"), "Rechtsgrundlage: Erklärung Nr. 17"),
       (T("a43"), "Art. 4 Abs. 3 EUV: loyale Zusammenarbeit"), (T("grenz"), "Grenzen: Ultra-vires- und Identitätskontrolle"),
       (T("zurueck"), "Lösung: Art. 288 Abs. 2 AEUV, Kollision, Rechtsfolge, Ergebnis"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Anwendungsvorrang des Unionsrechts (Costa/ENEL, Art. 4 III EUV): Warum Behörden ein deutsches Gesetz nicht anwenden dürfen, wenn unmittelbar anwendbares EU-Recht entgegensteht – und warum das deutsche Gesetz trotzdem gültig bleibt.

Der Fall: Hedwig will eine Limonade mit einem neuen Süßstoff verkaufen. Eine EU-Verordnung lässt ihn ausdrücklich zu, ein deutsches Gesetz verbietet ihn. Herr Lammert von der Lebensmittelüberwachung will den Verkauf untersagen – woran hält sich das Amt?

Inhalt:
– Der echte Fall Costa/ENEL (1964): Stromverstaatlichung in Italien, eine Stromrechnung über 1.925 Lire, Vorlage an den EuGH
– Eigene Rechtsordnung und Vorrang, auch vor späterem nationalem Recht
– Simmenthal II (1978): Jedes Gericht lässt entgegenstehendes Recht selbst unangewendet; Fratelli Costanzo (1989): auch die Verwaltung
– Anwendungsvorrang statt Geltungsvorrang: Das Gesetz bleibt gültig
– Rechtsgrundlage: kein Vorrangartikel, Erklärung Nr. 17 zur Schlussakte von Lissabon, Art. 4 Abs. 3 EUV
– Grenzen aus deutscher Sicht: Ultra-vires- und Identitätskontrolle des BVerfG
– Lösung mit Art. 288 Abs. 2 AEUV im Wortlaut, Ergebnis, Klausurtipp, Klausurschema, Merksatz

Normen: Art. 288 Abs. 2 AEUV, Art. 267 AEUV, Art. 4 Abs. 3 EUV, Erklärung Nr. 17 zur Schlussakte von Lissabon, Art. 31 GG

Rechtsprechung:
– EuGH, Urt. v. 15.7.1964 – Rs. 6/64, Costa/ENEL, Slg. 1964, 1253 (S. 1269 f.)
– EuGH, Urt. v. 9.3.1978 – Rs. 106/77, Simmenthal II, Slg. 1978, 629, Rn. 21/23, 24
– EuGH, Urt. v. 22.6.1989 – Rs. 103/88, Fratelli Costanzo, Slg. 1989, 1839, Rn. 31, 33
– EuGH, Urt. v. 22.10.1998 – C-10/97 bis C-22/97, IN.CO.GE.'90, Rn. 21
– EuGH, Urt. v. 4.12.2018 – C-378/17, Rn. 38 f.; Urt. v. 22.2.2022 – C-430/21, Rn. 53, 55
– BVerfG, Urt. v. 30.6.2009 – 2 BvE 2/08 u. a., BVerfGE 123, 267 (Lissabon), Rn. 240 f., 335, 339

Kapitel:
{kapitel}

Der Übungsfall (Hedwig, Herr Lammert, Süßstoff) ist ausgedacht; Verordnung und Gesetz sind Fallannahmen. Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Europarecht #CostaENEL #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
ERS = [(r"fünfzehnten\s+Juli\s+neunzehnhundertvierundsechzig", "15. Juli 1964"),
       (r"neunzehnhundertzweiundsechzig", "1962"), (r"neunzehnhundertfünfundzwanzig", "1.925"),
       (r"neunzehnhundertachtundsiebzig", "1978"), (r"neunzehnhundertneunundachtzig", "1989"),
       (r"Artikel\s+zweihundertsiebenundsechzig", "Art. 267"), (r"Artikel\s+einunddreißig", "Art. 31"),
       (r"Artikel\s+zweihundertachtundachtzig\s+Absatz\s+zwei", "Art. 288 Abs. 2"),
       (r"Artikel\s+vier\s+Absatz\s+drei", "Art. 4 Abs. 3"), (r"Erklärung\s+Nummer\s+siebzehn", "Erklärung Nr. 17"),
       (r"vom fünfzehnten Juli", "vom 15. Juli"), (r"\bEnel\b", "ENEL"), (r"\b1925 Lire", "1.925 Lire")]
for a, b in ERS:
    srt = re.sub(a, b, srt)
for w in ("neunzehnhundert", "zweihundert", "einunddreißig", "Nummer siebzehn", "Enel", "fünfzehnten"):
    assert w not in srt, w
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Anwendungsvorrang", "Fratelli Costanzo", "Erklärung Nr. 17", "Art. 288 AEUV", "Lissabon-Urteil"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
