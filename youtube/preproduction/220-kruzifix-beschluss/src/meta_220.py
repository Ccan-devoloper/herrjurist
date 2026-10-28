"""Nachbearbeitung der Upload-Texte für Folge 220 (nach meta_217.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Untertitel-Korrekturen (Zahlen und Normen als Ziffern, Sprechernamen). Keine Namen realer Beschwerdeführer.
Länderregelungen außer Bayern nicht aufgelistet (nicht an Primärquellen geprüft; RECHTSSTAND.md).
Aufruf: python3 meta_220.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: das Kreuz über der Tafel"),
       (T("eltern"), "Die Bitte der Eltern"),
       (T("frage"), "Die Frage und der Sachverhalt"),
       (T("art4"), "Art. 4 Abs. 1 GG im Wortlaut"),
       (T("pos"), "Schutzbereich: negative Glaubensfreiheit"),
       (T("eingr"), "Eingriff: Lernen unter dem Kreuz"),
       (T("kultur"), "Bloß Kultur? Das Kreuz als Glaubenssymbol"),
       (T("vorb"), "Rechtfertigung: Art. 7 Abs. 1 GG"),
       (T("konk"), "Praktische Konkordanz"),
       (T("posit"), "Positive Glaubensfreiheit und Mehrheitsprinzip"),
       (T("erg"), "Ergebnis und abweichende Meinung"),
       (T("bayern"), "Bayern: Widerspruchslösung und Kreuzerlass"),
       (T("tipp"), "Klausurtipp: Prüfungsaufbau"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Kruzifix-Beschluss (BVerfGE 93, 1): Warum ein Kreuz im Klassenzimmer die negative Glaubensfreiheit aus Art. 4 I GG berührt – staatliche Neutralität erklärt. Schutzbereich, Eingriff durch die Schulpflicht, Rechtfertigung über Art. 7 Abs. 1 GG und praktische Konkordanz, dazu die Folgen in Bayern.

Der Fall: Bayern, Anfang der 1990er Jahre. Über der Tafel der Klasse 2a einer staatlichen Grundschule hängt ein Kreuz, weil die Volksschulordnung es vorschreibt. Herr und Frau Rohde gehören keiner Kirche an und erziehen ihren Sohn ohne religiöses Bekenntnis. Sie bitten den Schulleiter, das Kreuz abzuhängen. Er lehnt ab: Das Kreuz stehe für die abendländische Kultur. Verletzt das Kreuz die Familie in ihrer Glaubensfreiheit?

Inhalt:
– Art. 4 Abs. 1 GG (im Wortlaut): positive und negative Glaubensfreiheit; Elternrecht i. V. m. Art. 6 Abs. 2 GG
– Eingriff: Wegen der Schulpflicht lernen die Kinder „unter dem Kreuz“, ohne Ausweichmöglichkeit; das Kreuz ist Glaubenssymbol, nicht bloß Kulturzeichen
– Rechtfertigung: vorbehaltlos gewährleistet; Art. 7 Abs. 1 GG (im Wortlaut) und praktische Konkordanz; positive Glaubensfreiheit der anderen; kein Mehrheitsprinzip
– Ergebnis: Verstoß gegen Art. 4 Abs. 1 GG; die abweichende Meinung von drei Richtern
– Folgen in Bayern: Widerspruchslösung im Schulgesetz (Art. 7 Abs. 3 BayEUG von 1995, im Wortlaut; heute Art. 7 Abs. 4 BayEUG), BVerwG 1999; Kreuzerlass für Behörden, BVerwG 2023
– Klausurtipp mit Prüfungsaufbau, Merksatz

Normen: Art. 4 Abs. 1, Art. 6 Abs. 2 S. 1, Art. 7 Abs. 1 GG; § 13 Abs. 1 S. 3 VSO Bayern a. F.; Art. 7 Abs. 3 BayEUG (Fassung 1995, heute Abs. 4); § 28 AGO Bayern.

Rechtsprechung:
– BVerfG, Beschl. v. 16.5.1995 – 1 BvR 1087/91, BVerfGE 93, 1 (Kruzifix), Leitsätze, Rn. 34–57; abweichende Meinung Rn. 60–91
– BVerwG, Urt. v. 21.4.1999 – 6 C 18.98, BVerwGE 109, 40 (Widerspruchslösung)
– BVerwG, Urt. v. 19.12.2023 – 10 C 5.22 (Kreuzerlass)
– zur Abgrenzung: BVerfG, Beschl. v. 27.1.2015 – 1 BvR 471/10, 1 BvR 1181/10, BVerfGE 138, 296 (Kopftuch II), Rn. 104, 112

Hinweise: Familie Rohde, ihr Sohn, Schulleiter Kampe und die Schule sind erfunden; der Fall folgt dem Muster des Kruzifix-Beschlusses. Die Folgen behandelt das Video am Beispiel Bayerns, für das die Entscheidung erging; ob und wie andere Länder religiöse Symbole in Schulen regeln, bestimmt das jeweilige Landesrecht. Mehr dazu: Folge 217 (Kopftuch-Urteil), Folge 020 (Grundrechtsprüfung Schema), Folge 004 (Neutralitätspflicht).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#KruzifixBeschluss #Grundrechte #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
W = r"[ \n]+"
for muster, ziel in [(rf"neunziger{W}Jahre", "1990er Jahre")]:   # Artikel und Jahreszahlen wandelt youtube_metadaten.py selbst um
    assert re.search(muster, srt), muster
    srt = re.sub(muster, ziel, srt)
for a, b in [("Rohde: Unser", "Herr Rohde: Unser"), ("Kampe: Das Kreuz", "Herr Kampe: Das Kreuz"),
             ("Kampe: Dann", "Herr Kampe: Dann")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"Artikel|neunzehn|zweitausend|neunziger", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Widerspruchslösung", "Kreuzerlass", "Kreuz im Klassenzimmer"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
