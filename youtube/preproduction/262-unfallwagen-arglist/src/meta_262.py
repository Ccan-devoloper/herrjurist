"""Nachbearbeitung der Upload-Texte für Folge 262 (nach meta_259.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung und
Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Paragrafenzeichen nicht am Zeilenende).
Aufruf: python3 meta_262.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Unfallschaden verschwiegen"),
       (T("ansp"), "Zwei Wege; arglistige Täuschung, § 123 I BGB"),
       (T("luege"), "Täuschung durch Schweigen: Aufklärungspflicht"),
       (T("irrtum"), "Irrtum, Kausalität und Arglist"),
       (T("p124"), "Frist § 124 BGB und Rechtsfolge § 142 I BGB"),
       (T("konk"), "Anfechtung neben den Mängelrechten?"),
       (T("aus"), "Gewährleistungsausschluss und § 444 BGB"),
       (T("vgl"), "Was ist günstiger?"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfungsschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Arglistige Täuschung nach § 123 I BGB: Wann ist das Verschweigen eines Unfallschadens arglistig – und wie verhält sich die Anfechtung zu den Mängelrechten der §§ 437 ff. BGB und zum Gewährleistungsausschluss (§ 444 BGB)?

Der Fall: Angelika, selbständige Hebamme, kauft beim Gebrauchtwagenhändler Herrn Hecker einen Kombi für 8.000 €, ohne jede Gewährleistung. Herr Hecker hat den schweren Frontschaden des angekauften Unfallwagens in seiner eigenen Werkstatt reparieren lassen und sagt nichts. Drei Monate später entdeckt der Prüfer bei der Hauptuntersuchung den reparierten Unfallschaden. Angelika ficht an. Darf sie das, obwohl sie auch Mängelrechte hat – und hilft Herrn Hecker der Ausschluss?

Inhalt:
– Zwei Wege zum Geld: Anfechtung (§§ 123, 142 I, 812 BGB) oder Rücktritt (§§ 437 Nr. 2, 346 BGB)
– § 123 I BGB im Wortlaut: Täuschung, Irrtum und Kausalität, Arglist
– Täuschung durch Schweigen: nur bei Aufklärungspflicht; bekannter Unfallschaden beim Gebrauchtwagen, Ausnahme Bagatellschaden
– Arglist: Mangel für möglich halten und billigend in Kauf nehmen, dass der Käufer sonst nicht kauft
– § 124 BGB im Wortlaut: ein Jahr ab Entdeckung; Erklärung gegenüber dem Verkäufer (§ 143 BGB); § 142 I BGB: nichtig von Anfang an
– Verhältnis zu den Mängelrechten: keine Sperre bei Arglist; anders beim Eigenschaftsirrtum (§ 119 II BGB, h. M.)
– Gewährleistungsausschluss: Unternehmerin (§ 14 BGB), Verbraucher (§ 476 BGB), § 444 BGB im Wortlaut
– Was ist günstiger: Anfechtung oder Rücktritt mit Schadensersatz (§§ 325, 326 V BGB)?
– Klausurtipp, Prüfungsschema, Merksatz

Normen: §§ 123, 124, 142, 143 BGB; §§ 437, 444 BGB; § 14 BGB; § 434 Abs. 3 BGB; §§ 325, 326 Abs. 5, 346 BGB; § 476 BGB; § 812 BGB; § 119 Abs. 2 BGB

Rechtsprechung: BGH, Urt. v. 11.8.2010 – XII ZR 123/09 (Aufklärungspflicht, Rn. 19 f.); BGH, Urt. v. 19.6.2013 – VIII ZR 183/12 (aufklärungspflichtiger Unfallschaden, Bagatellschaden, Rn. 17–24); BGH, Urt. v. 19.12.2012 – VIII ZR 117/12 (Unfallwagen als Sachmangel, Rn. 14); BGH, Urt. v. 15.4.2015 – VIII ZR 80/14 (Arglist, Rn. 14–17); BGH, Urt. v. 21.6.2024 – V ZR 79/23 (§ 444 BGB, Rn. 12 f.); BGH, Urt. v. 11.2.2026 – VIII ZR 37/24 (Anfechtung als Rücktritt auslegen, Leitsatz 1).

Hinweise: Angelika, Herr Hecker und das Autohaus sind erfunden; der Ausschluss gilt im Fall als einzeln ausgehandelt (AGB-Kontrolle nicht behandelt). Zum Eigenschaftsirrtum (§ 119 II BGB) wird die herrschende Meinung dargestellt. Das Grundschema der Anfechtung zeigt unsere Folge „Anfechtung Schema §§ 119 ff. BGB: Die Prüfung in 5 Schritten“, die Mängelrechte die Folgen „§ 437 BGB: Die Käuferrechte auf einen Blick“ und „Schadensersatz Kaufrecht § 437 Nr. 3 BGB: Welche Anspruchsgrundlage?“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#ArglistigeTäuschung #Gebrauchtwagen #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
bl = [b_.split("\n") for b_ in srt.strip().split("\n\n")]
neu = []
for b_ in bl:
    if neu and b_[2:] == ["Euro."]:
        neu[-1][1] = neu[-1][1].split(" --> ")[0] + " --> " + b_[1].split(" --> ")[1]
        neu[-1][-1] += " Euro."
    else:
        neu.append(b_)
srt = "\n\n".join("\n".join([str(i + 1)] + b_[1:]) for i, b_ in enumerate(neu)) + "\n"
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("Hecker: Achttausend", "Herr Hecker: Achttausend"), ("Pruefer:", "Prüfer:")]
for a, b in ERSATZ:
    srt = srt.replace(a, b)
srt = re.sub(r"(achttausend)\n\n(\d+)\n([^\n]+)\nEuro([.,]) ?", r"\1 Euro\4\n\n\2\n\3\n", srt)  # Einheit nicht vom Betrag trennen
ZAHL = [(r"[Aa]chttausend(\s)Euro", r"8.000\1€"), (r"[Dd]rei(\s)Monate", r"3\1Monate")]
for a, b in ZAHL:
    srt = re.sub(a, b, srt)
srt = re.sub(r"(\d)\n€ ?", r"\1 €\n", srt)
srt = re.sub(r"€\n([,.;:]) ?", r"€\1\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|achttausend|Pruefer", srt, re.I), re.findall(r".{0,30}(?:achttausend|Pruefer).{0,30}", srt, re.I)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
