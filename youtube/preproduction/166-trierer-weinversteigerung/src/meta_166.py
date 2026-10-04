"""Nachbearbeitung der Upload-Texte für Folge 166 (nach meta_146.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Seiten,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechername).
Aufruf: python3 meta_166.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Winken bei der Weinversteigerung"),
       (T("p156"), "§ 156 BGB: Vertrag durch Zuschlag"),
       (T("klassiker"), "Der Klassiker: Lehrbuchfall und BGHZ 91, 324; Sachverhalt"),
       (T("tb"), "Objektiver Tatbestand, §§ 133, 157 BGB"),
       (T("st"), "Subjektiver Tatbestand: Erklärungsbewusstsein"),
       (T("wt"), "Der Streit: Willenstheorie und Gegenansicht"),
       (T("bghz"), "BGH: potentielles Erklärungsbewusstsein"),
       (T("wahl"), "Das Wahlrecht, § 118 BGB passt nicht"),
       (T("sub"), "Subsumtion: Kaufvertrag (+)"),
       (T("anf"), "Anfechtung analog § 119 Abs. 1 BGB"),
       (T("p121"), "Unverzüglich, § 121 BGB"),
       (T("eok"), "Folgen: § 142 und § 122 BGB"),
       (T("loes"), "Lösung"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Erklärungsbewusstsein fehlt – liegt trotzdem eine Willenserklärung vor? Der Lehrbuchfall der Trierer Weinversteigerung, die BGH-Formel aus BGHZ 91, 324 (Sparkassen-Bürgschaft) und die Lösung über §§ 119 I analog, 121, 122 BGB.

Der Fall: Bei einer Weinversteigerung gilt: Wer die Hand hebt, bietet. Ekkehard ist nur zum Zusehen gekommen und hebt die Hand, um seiner Freundin zuzuwinken. Die Auktionatorin erteilt ihm den Zuschlag über 900 € (§ 156 BGB). Muss er zahlen?

Die „Trierer Weinversteigerung“ ist ein klassischer Lehrbuchfall (Hermann Isay, Die Willenserklärung im Thatbestande des Rechtsgeschäfts, 1899, S. 25), kein Gerichtsfall. Entschieden hat der Bundesgerichtshof die Frage 1984 im Fall einer Sparkasse, die eine Bürgschaft „mitteilte“, ohne bürgen zu wollen.

Inhalt:
– Tatbestand der Willenserklärung: objektiv aus Sicht des Empfängers (§§ 133, 157 BGB im Wortlaut), subjektiv Handlungswille, Erklärungsbewusstsein, Geschäftswille
– Der Streit: Willenstheorie (§ 118, § 122 analog) gegen Vertrauensschutz
– BGH-Formel (BGHZ 91, 324, Leitsatz, wörtlich): potentielles Erklärungsbewusstsein; Wahlrecht des Erklärenden; warum § 118 nicht passt
– Anfechtung analog § 119 Abs. 1 BGB, unverzüglich nach § 121 Abs. 1 (im Wortlaut), Willensmangel erkennbar; warum die Sparkasse zu spät kam
– Folgen: § 142 Abs. 1 und Vertrauensschaden nach § 122 Abs. 1 BGB (im Wortlaut), begrenzt durch das Erfüllungsinteresse
– Lösung, Klausurtipp, Prüfschema, Merksatz

Normen: §§ 118, 119 Abs. 1, 121 Abs. 1, 122 Abs. 1, 133, 142 Abs. 1, 156, 157 BGB

Rechtsprechung:
– BGH, Urt. v. 7.6.1984 – IX ZR 66/83, BGHZ 91, 324: S. 324 (Leitsatz), 327 f. (Meinungsstand), 329 f. (Wortlaut § 119, § 118, Wahlrecht), 330 (Zurechnung), 331 f. (Anfechtungserklärung), 332 f. (15 Tage nicht unverzüglich)
– BGH, Urt. v. 14.2.2023 – XI ZR 537/21, Rn. 29; Urt. v. 15.2.2022 – II ZR 235/20, Rn. 43 (Formel bestätigt)
– BGH, Beschl. v. 30.10.2013 – V ZB 9/13, Rn. 9 („analog § 119 BGB anfechtbar“)

Hinweise: Ekkehard, Frau Haller und Reinhild sind erfundene Figuren; echte Weingüter oder Auktionshäuser kommen nicht vor. Den Aufbau der Anfechtung erklärt Folge 23 ausführlich, den Zugang der Willenserklärung Folge 17. Nicht behandelt: Versteigerungsbedingungen, Online-Auktionen, Bestätigung nach § 144 BGB.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Erklärungsbewusstsein #BGBAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"[Aa]chthundertfünfzig", "850", srt)
srt = re.sub(r"[Nn]eunhundert", "900", srt)
for a, b in [("\nHaller: ", "\nFrau Haller: "), ("Ekkehard: ", "Ekkehard: "),
             ("Kosten, das Fass", "Kosten, um das Fass")]:   # gesprochen mit „um“ (beide Erkenner)
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"achtzehnhundertneunundneunzig", "1899", srt)
srt = re.sub(r"neunzehnhundertvierundachtzig", "1984", srt)
srt = re.sub(r"fünfzehn(\n| )Tage", r"15\1Tage", srt)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
assert not re.search(r"§\n|Abs\.\n", srt) and "neunhundert" not in srt.lower() and "achtzehnhundert" not in srt, "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
