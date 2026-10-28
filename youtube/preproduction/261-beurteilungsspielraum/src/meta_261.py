"""Nachbearbeitung der Upload-Texte für Folge 261 (nach meta_258.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit präzisierter Anfangszeile, Fall, Inhalt, Normen,
Rechtsprechung, Länderhinweis und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Abkürzungen).
Landesrecht nur als am Wortlaut geprüftes Beispiel (NRW), keine 16-Länder-Liste (nicht geprüft, siehe RECHTSSTAND.md).
Aufruf: python3 meta_261.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: 5 Punkte trotz vertretbarer Lösung"),
       (T("grund"), "Grundsatz: volle gerichtliche Kontrolle (Art. 19 IV GG)"),
       (T("note"), "Notenstufen und Berufsfreiheit (Art. 12 I GG)"),
       (T("aber"), "Ausnahme: Beurteilungsspielraum und Chancengleichheit"),
       (T("spez"), "Prüfungsspezifische Wertung oder Fachfrage?"),
       (T("anspr"), "Antwortspielraum: BVerfGE 84, 34"),
       (T("kontr"), "Grenzen des Beurteilungsspielraums"),
       (T("ued"), "Überdenkungsverfahren"),
       (T("land"), "Beispiel NRW: § 27, § 27a JAG"),
       (T("zurueck"), "Im Fall: Überdenken, Klage, Urteil"),
       (T("tipp"), "Klausurtipp und Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Beurteilungsspielraum bei Prüfungen (Art. 12 I, 19 IV GG): Was darf das Gericht an einer Examensnote prüfen? Antwortspielraum, Grenzen des Spielraums und Überdenkungsverfahren – und warum am Ende meist eine Neubewertung steht.

Der Fall: Jorinde folgt in ihrer Examensklausur im Öffentlichen Recht einer vertretbaren Gegenansicht und begründet sie sorgfältig. Ihr Prüfer schreibt „falsch“ und „insgesamt oberflächlich“ und vergibt 5 Punkte. Nach dem Überdenken bleibt er dabei. Kann Jorinde 9 Punkte einklagen?

Inhalt:
– Grundsatz: wirksame, vollständige gerichtliche Kontrolle, auch bei unbestimmten Rechtsbegriffen (Art. 19 Abs. 4 GG); Abgrenzung zum Ermessen (Folge 74)
– Notenstufen sind unbestimmt umschrieben (§ 1 JurPrNotSkV); Prüfungen berühren die Berufsfreiheit (Art. 12 Abs. 1 GG)
– Ausnahme Beurteilungsspielraum: nur bei prüfungsspezifischen Wertungen (Schwierigkeitsgrad, Gewichtung, Gesamteindruck) – wegen des Vergleichs mit anderen Arbeiten und der Chancengleichheit
– Fachfragen voll kontrollierbar: Antwortspielraum – eine vertretbare und mit gewichtigen Argumenten folgerichtig begründete Lösung darf nicht als falsch gewertet werden
– Grenzen des Spielraums: Verfahrensfehler, falscher Sachverhalt, allgemeingültige Bewertungsmaßstäbe, sachfremde Erwägungen; Korrektur nur bei möglicher Auswirkung auf die Note
– Überdenkungsverfahren: konkrete Einwände, die Prüfer überdenken mit unverändertem Maßstab
– Ergebnis: in der Regel Neubewertung durch die Prüfer (Bescheidungsurteil, § 113 Abs. 5 S. 2 VwGO), keine Note vom Gericht
– Klausurtipp, Schema, Merksatz

Normen: Art. 12 Abs. 1, Art. 19 Abs. 4 GG; § 1 JurPrNotSkV; § 113 Abs. 5 S. 2, § 114 VwGO; Beispiel Nordrhein-Westfalen: § 27 Abs. 1, § 27a JAG NRW.
Rechtsprechung: BVerfG, Beschl. v. 17.4.1991 – 1 BvR 419/81, 213/83, BVerfGE 84, 34 (Antwortspielraum S. 55); BVerfG, Beschl. v. 17.4.1991 – 1 BvR 1529/84, 138/87, BVerfGE 84, 59; BVerwG, Beschl. v. 5.3.2018 – 6 B 71.17; BVerwG, Beschl. v. 3.9.2020 – 6 B 16.20; BVerwG, Urt. v. 10.4.2019 – 6 C 19.18 (Überdenkensverfahren).

Hinweise: Jorinde, Herr Ellerbrock und die Richterin sind erfunden, das Prüfungsamt ist namenlos. Wie das Überdenken abläuft und welche Fristen gelten, regelt das Juristenausbildungsgesetz bzw. die Prüfungsordnung deines Landes; Nordrhein-Westfalen ist nur ein Beispiel. Mehr zum Ermessen: Folge 74 (Ermessensfehler).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound „Writing with Pen on Paper“ (Gnarlycuga) und „Tearing Open An Envelope“ (21100375), CC0.

#Jura #Verwaltungsrecht #Examen
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("Folge vierundsiebzig", "Folge 74"), ("Ellerbrock: Diese Ansicht", "Herr Ellerbrock: Diese Ansicht"),
          ("Ellerbrock: Die Ansicht", "Herr Ellerbrock: Die Ansicht")]
for alt, neu in ERSATZ:
    muster = r"\s+".join(re.escape(w) for w in alt.split())
    if not re.search(muster, srt):
        print("nicht gefunden:", alt); continue
    srt = re.sub(muster, lambda m: neu if "\n" not in m.group(0) else neu.replace(" ", "\n", 1), srt)
srt = re.sub(r"(?<!Herr )\bEllerbrock:", "Herr Ellerbrock:", srt)
srt = re.sub(r"\bfünf(\s+)Punkt", r"5\1Punkt", srt)
srt = re.sub(r"\bneun(\s+)Punkte", r"9\1Punkte", srt)
srt = re.sub(r"(?<!Die )\bRichterin: Das", "Die Richterin: Das", srt)
for zahl, ziffer in (("Eins:", "1."), ("Zwei:", "2."), ("Drei:", "3."), ("Vier:", "4."), ("Fünf:", "5.")):
    srt = srt.replace(zahl, ziffer)
assert not re.search(r"\b(fünf|neun) Punkte|vierundsiebzig|Paragraf", srt), "Untertitel prüfen"
srt = srt.replace("VWGO", "VwGO")
srt = re.sub(r"\n\n\n+", "\n\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + ["Examensnote anfechten", "Prüfungsanfechtung"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
