"""Nachbearbeitung der Upload-Texte für Folge 196 (nach meta_193.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen, Daten).
Aufruf: python3 meta_196.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: ohne Ticket nach New York, Sachverhalt"),
       (T("vertrag"), "Vertrag? Schadensersatz? §§ 107, 108 BGB"),
       (T("norm"), "§ 812 Abs. 1 Satz 1 BGB: Eingriffskondiktion"),
       (T("erl"), "Was hat Till erlangt? Meinungsstand"),
       (T("w2"), "Wertersatz und Entreicherung, § 818 Abs. 2, 3 BGB"),
       (T("w819"), "Verschärfte Haftung, § 819 Abs. 1 BGB"),
       (T("mst"), "Wessen Kenntnis zählt beim Minderjährigen?"),
       (T("w828"), "§ 828 Abs. 3 BGB analog: Einsichtsfähigkeit"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Flugreise-Fall (BGHZ 55, 128): Was hat der 17-Jährige ohne Ticket erlangt, kann er sich auf Entreicherung (§ 818 III BGB) berufen und wessen Kenntnis zählt bei § 819 I?

Der Fall (1968, Namen geändert): Till ist 17 und fliegt mit gültigem Ticket bis zu einer Zwischenlandung. Dort steigt er mit den Transitpassagieren wieder ein und fliegt ohne Ticket weiter nach New York. Die Einreise wird ihm verweigert, die Fluggesellschaft fliegt ihn noch am selben Tag zurück und verlangt den Preis für den Hinflug: 1.188 DM. Seine Mutter genehmigt nichts. Till meint: Ohne den Gratisflug wäre ich nie geflogen.

Inhalt:
– Kein Vertrag (§§ 107, 108 BGB), kein Schadensersatz
– § 812 Abs. 1 Satz 1 Alt. 2 BGB im Wortlaut: Leistungsbegriff, Eingriffskondiktion
– Was ist erlangt? Die Beförderung selbst oder nur ersparte Aufwendungen (Meinungsstand)
– Wertersatz (§ 818 Abs. 2 BGB) und Entreicherung bei Luxusausgaben (§ 818 Abs. 3 BGB)
– Verschärfte Haftung nach § 819 Abs. 1, § 818 Abs. 4 BGB
– Wessen Kenntnis zählt beim Minderjährigen? Meinungsstand und BGH, § 828 Abs. 3 BGB analog
– Ergebnis, Rückflug über die Geschäftsführung ohne Auftrag, Klausurtipp, Prüfschema, Merksatz

Normen: §§ 812 Abs. 1 Satz 1, 818 Abs. 2–4, 819 Abs. 1, 828 Abs. 3 BGB; §§ 107, 108 BGB; § 265a StGB; §§ 677, 683, 670 BGB

Rechtsprechung:
– BGH, Urt. v. 7.1.1971 – VII ZR 9/70, BGHZ 55, 128 = NJW 1971, 609 (Flugreise-Fall)
– BGH, Beschl. v. 20.1.2021 – GSSt 2/20, Rn. 23 (§ 819 BGB beim Minderjährigen, § 828 Abs. 3 BGB analog)
– BGH, Urt. v. 21.2.2022 – VIa ZR 8/21, Rn. 88, 95 (Entstehung und Wegfall der Bereicherung, Bösgläubigkeit)
– BGH, Urt. v. 27.10.2016 – IX ZR 160/14, Rn. 21 (Luxusausgaben)
– BGH, Urt. v. 7.3.2013 – III ZR 231/12, Rn. 27 (echte Vermögensvermehrung)
– BGH, Urt. v. 31.1.2018 – VIII ZR 39/17, Rn. 17 (Leistungsbegriff)
– BGH, Beschl. v. 27.11.2014 – III ZA 19/14, Rn. 6 (Geschäftsführung ohne Auftrag)

Hinweise: Den Überblick über die Kondiktionen zeigt das Video zum Bereicherungsrecht, das Minderjährigenrecht das Video zur Geschäftsfähigkeit. 1971 stand die Regel zur Einsichtsfähigkeit in § 828 Abs. 2 BGB, heute in Abs. 3.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#FlugreiseFall #Bereicherungsrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei):( |\n)", lambda m: {"eins": "I.", "zwei": "II."}[m.group(1)] + m.group(2), srt)
for a, b in [("tausendeinhundertachtundachtzig Mark", "1.188 Mark"), ("am siebten Januar", "am 7. Januar"),
             ("Till ist siebzehn", "Till ist 17"), ("er war siebzehn", "er war 17"),
             ("das achtzehnte Lebensjahr", "das 18. Lebensjahr"), ("fast achtzehn", "fast 18"),
             ("Alternative zwei", "Alt. 2"), ("§ 265 a STGB", "§ 265a StGB")]:
    srt = srt.replace(a, b)
srt = re.sub(r"§ 265\n(\n\d+\n\S+ --> \S+\n)a STGB\.", r"§ 265a\n\1StGB.", srt)
srt = re.sub(r"Alternative\n(\n\d+\n\S+ --> \S+\n)zwei\. ", r"Alt. 2.\n\1", srt)
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert not re.search(r"hundert|tausend|zehn\b|Römisch|siebten", srt), "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
