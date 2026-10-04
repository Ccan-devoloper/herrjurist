"""Nachbearbeitung der Upload-Texte für Folge 129 (Kopie von meta_125.py, nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_129.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Das neue Dach ist undicht"),
       (T("p1"), "1. Werkvertrag und Abnahme"),
       (T("m1"), "2. Mangel, § 633 Abs. 2 BGB"),
       (T("r1"), "3. Rechte aus § 634 BGB"),
       (T("nach"), "Nacherfüllung: Wahlrecht des Unternehmers, § 635 BGB"),
       (T("s1"), "Selbstvornahme, § 637 Abs. 1 BGB"),
       (T("v1"), "Vorschuss, § 637 Abs. 3 BGB"),
       (T("rm1"), "Rücktritt, Minderung, Schadensersatz"),
       (T("vj1"), "4. Verjährung, § 634a BGB"),
       (T("u1"), "5. Unterschiede zum Kauf"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Mängelrechte Werkvertrag (§§ 633–639 BGB): Was kann der Besteller bei Pfusch am Bau verlangen und worin unterscheidet sich § 634 BGB vom Kaufrecht?

Der Fall: Beate lässt das Dach ihres Hauses von Dachdecker Herrn Wenzel für 18.000 Euro neu eindecken und nimmt es ab. Zwei Monate später zeigen sich nach starkem Regen Wasserflecken an der Decke: Der Anschluss am Schornstein ist undicht, die Reparatur kostet 2.400 Euro. Herr Wenzel geht nicht ans Telefon. Was kann Beate verlangen – und was wäre beim Kauf anders?

Inhalt (als Prüfungsschema):
– 1. Werkvertrag (§ 631 BGB) und Abnahme als Zäsur; Neueindeckung zugleich Bauvertrag (§ 650a BGB)
– 2. Mangel (§ 633 Abs. 2 BGB, Wortlaut), maßgeblich der Zeitpunkt der Abnahme
– 3. Rechte aus § 634 BGB (Wortlaut): Nacherfüllung mit Wahlrecht des Unternehmers (§ 635 BGB), Selbstvornahme nach erfolgloser Frist (§ 637 Abs. 1 BGB, Wortlaut), Vorschuss (§ 637 Abs. 3 BGB), Rücktritt und Minderung (§§ 636, 323, 638 BGB), Schadensersatz (§§ 636, 280, 281 BGB)
– 4. Verjährung: fünf Jahre bei einem Bauwerk, Beginn mit der Abnahme (§ 634a BGB, Wortlaut)
– 5. Unterschiede zum Kauf als Tabelle: Wahlrecht, Selbstvornahme und Vorschuss, maßgeblicher Zeitpunkt, Verjährungsbeginn
– Ergebnis, Klausurtipp, Klausurschema, Merksatz

Rechtsprechung:
– BGH, Urt. v. 19.1.2017 – VII ZR 301/13, Leitsatz 1, Rn. 32: Mängelrechte grundsätzlich erst nach Abnahme; Mangelfreiheit beurteilt sich im Zeitpunkt der Abnahme
– BGH, Beschl. v. 8.10.2020 – VII ARZ 1/20, Rn. 27, 67: Der Unternehmer wählt – anders als der Verkäufer – die Art der Nacherfüllung; Selbstvornahme mit Vorschuss gibt es nur im Werkvertragsrecht
– BGH, Urt. v. 9.11.2023 – VII ZR 92/20, Rn. 28: Der Vorschuss ist zweckgebunden und abzurechnen
– BGH, Urt. v. 13.7.2011 – VIII ZR 215/10, Rn. 24: strenge Anforderungen an eine ernsthafte und endgültige Verweigerung
– BGH, Urt. v. 2.6.2016 – VII ZR 348/13, Rn. 19: Arbeiten „bei Bauwerken“ (fünfjährige Verjährung)

Hinweise: Der Fall ist erfunden. Dass die Neueindeckung eines Daches eine Arbeit an einem Bauwerk ist, folgt aus dem Maßstab von VII ZR 348/13 (dort eine Photovoltaikanlage); ein BGH-Urteil zu einem Dach haben wir nicht herangezogen. Beim Verbrauchsgüterkauf gibt es einen Vorschuss für Nacherfüllungsaufwendungen (§ 475 Abs. 5 BGB) – aber keine Selbstvornahme. Schadensersatz für die Wasserflecken (Mangelfolgeschaden) behandelt das Video nicht. Die Abnahme erklärt Folge 95, die Käuferrechte Folge 63, die Abgrenzung von Werk- und Dienstvertrag Folge 56.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Werkvertrag #Zivilrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt).replace("\nWenzel: ", "\nHerr Wenzel: ")
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
