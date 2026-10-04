"""Nachbearbeitung der Upload-Texte für Folge 188 (nach meta_186.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen, Normen
aller 16 Länder (Landesrecht länderneutral), Rechtsprechung, Hinweisen und Lizenzzeile; Untertitel-Korrekturen
(Gliederung, Zahlen, Normen, Sprecher).
Aufruf: python3 meta_188.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Garage im Außenbereich"),
       (T("anspr"), "Anspruch auf Baugenehmigung: Art. 68 BayBO, § 74 BauO NRW"),
       (T("tab"), "Länder-Overlay: gleiche Struktur, andere Nummern"),
       (T("komp"), "Kompetenz: Bodenrecht (Bund) und Bauordnungsrecht (Länder)"),
       (T("gb"), "I. Genehmigungsbedürftigkeit: verfahrensfrei? Freistellung?"),
       (T("gf"), "III. 1. Verfahrensart und Prüfprogramm – auch Brandschutz?"),
       (T("bpl"), "III. 2. Bauplanungsrecht: § 29 BauGB und die Weiche §§ 30, 34, 35"),
       (T("l35"), "Außenbereich: § 35 BauGB im Ergebnis"),
       (T("bo"), "III. 3. Bauordnungsrecht und Ergebnis"),
       (T("sch"), "Prüfschema Anspruch auf Baugenehmigung"),
       (T("tipp"), "Klausurtipp: zuerst die Verfahrensart"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Baugenehmigung Schema: Genehmigungsbedürftigkeit, Bauplanungsrecht (§§ 29 ff. BauGB) und Bauordnungsrecht der Länder – zwei Ebenen, bundesweit erklärt.

Der Fall: Ein Oldtimer-Fan will auf seiner Wiese weit draußen vor dem Dorf eine Betongarage bauen. Brandschutz und Abstände stimmen – trotzdem lehnt die Bauaufsichtsbehörde ab. Hat er einen Anspruch auf die Baugenehmigung?

Inhalt:
– Anspruchsgrundlage in der Landesbauordnung im Wortlaut: Art. 68 Abs. 1 S. 1 BayBO und § 74 Abs. 1 S. 1 BauO NRW 2018 („ist zu erteilen“ – gebundene Entscheidung)
– Länder-Overlay: Bayern und Nordrhein-Westfalen als Beispiele, andere Länder ähnlich
– Gesetzgebungskompetenz: Bodenrecht, Art. 74 Abs. 1 Nr. 18 GG (Bund), und Art. 70 Abs. 1 GG (Länder) im Wortlaut
– I. Genehmigungsbedürftigkeit: Art. 55 Abs. 1 BayBO, § 60 Abs. 1 BauO NRW 2018; verfahrensfreie Garagen bis 50 m² – aber nicht im Außenbereich; Genehmigungsfreistellung nur mit qualifiziertem oder vorhabenbezogenem Bebauungsplan
– II. Bauantrag
– III. Genehmigungsfähigkeit: vereinfachtes Verfahren und Prüfprogramm (Art. 59 BayBO, § 64 BauO NRW 2018) – der Brandschutz wird grundsätzlich nicht mitgeprüft, muss aber eingehalten werden
– Bauplanungsrecht: § 29 Abs. 1 BauGB im Wortlaut, die Weiche §§ 30, 34, 35 BauGB, § 35 BauGB im Ergebnis
– Bauordnungsrecht, Ergebnis, Prüfschema, Klausurtipp (Verpflichtungsklage), Merksatz

Normen: §§ 29, 30, 34, 35 BauGB; Art. 70, 74 Abs. 1 Nr. 18 GG; § 42 Abs. 1 VwGO; Beispiele: Art. 55, 57, 58, 59, 62b, 68 BayBO; §§ 60, 62, 63, 64, 74 BauO NRW 2018

In deinem Land ggf. andere Nummer – Anspruch auf Baugenehmigung in allen 16 Ländern: Bayern Art. 68 BayBO (Genehmigungspflicht Art. 55, vereinfachtes Verfahren Art. 59), Nordrhein-Westfalen § 74 BauO NRW 2018 (§§ 60, 64), Brandenburg § 72 BbgBO (§§ 59, 63) – diese drei am amtlichen Text geprüft. In den übrigen Ländern steht der Anspruch in der jeweiligen Landesbauordnung – Nummer bitte im eigenen Landesrecht nachschlagen.

Rechtsprechung:
– BVerwG, Urt. v. 19.4.2012 – 4 C 10.11, Rn. 11 (Außenbereich: nicht Bestandteil eines im Zusammenhang bebauten Ortsteils)

Hinweise: Das Bauplanungsrecht des Baugesetzbuchs gilt bundesweit; Verfahrensarten und Prüfprogramme regelt jedes Land selbst. Die Prüfung des § 35 BauGB im Einzelnen zeigt die Folge „Außenbereich § 35 BauGB: Warum dein Wochenendhaus im Wald verboten ist“, den Klageaufbau die Folge „Zulässigkeit und Begründetheit: Aufbau im Öffentlichen Recht“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 4. Oktober 2026 (BauO NRW 2018 in der Fassung ab 1. September 2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Baurecht #Baugenehmigung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei|vier)([,:])( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV."}[m.group(1)] + m.group(3), srt)
for muster, ersatz in [(r"vierzig\sQuadratmeter", r"40 m²"), (r"fünfzig\sQuadratmeter", r"50 m²"),
                       (r"Nr\. 1 und fünf", r"Nr. 1 und 5")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
srt = srt.replace("\nHasenkamp: ", "\nHerr Hasenkamp: ").replace("\nOrtmann: ", "\nFrau Ortmann: ")
assert not re.search(r"§\n|Abs\.\n|Art\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "Paragraf" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
