"""Nachbearbeitung der Upload-Texte für Folge 174 (nach meta_153.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, amtlicher Bekanntmachung,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Beträge als Ziffern, Sprechernamen, Normzeilen nicht getrennt).
Aufruf: python3 meta_174.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: an Lohn und Konto"),
       (T("antrag"), "1. Antrag und Zuständigkeit, § 828 ZPO"),
       (T("pfaend"), "2. Pfändung: Arrestatorium und Inhibitorium, § 829 ZPO"),
       (T("zust"), "Wirksam mit Zustellung an den Drittschuldner"),
       (T("ueber"), "3. Überweisung: zur Einziehung oder an Zahlungs statt"),
       (T("wl836"), "Wirkung der Überweisung, § 836 ZPO"),
       (T("erkl"), "4. Drittschuldnererklärung, § 840 ZPO"),
       (T("lohn"), "5. Lohnpfändung: Pfändungsschutz, § 850c ZPO"),
       (T("tabelle"), "Pfändungstabelle und künftige Gehälter"),
       (T("konto2"), "6. Kontopfändung: Pfändungsschutzkonto"),
       (T("erg"), "Ergebnis und Klausurtipp"),
       (T("sch"), "Schema in 5 Schritten"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Pfändungs- und Überweisungsbeschluss (§§ 829, 835 ZPO): Wie Konto und Lohn gepfändet werden, wann die Pfändung wirkt und was der Drittschuldner tun muss.

Der Fall: Der Tischler Herr Dorfmann hat gegen Frau Kästner ein Urteil über 3.600 € mit Vollstreckungsklausel. Frau Kästner arbeitet bei einem großen Arbeitgeber, ihr Gehalt geht auf ihr Girokonto. Wie kommt Herr Dorfmann an Lohn und Guthaben?

Inhalt:
– 1. Antrag und Zuständigkeit: Vollstreckungsgericht am Wohnsitz (§ 828 ZPO im Wortlaut), Rechtspfleger (§ 20 Abs. 1 Nr. 17 RPflG)
– 2. Pfändung (§ 829 Abs. 1 ZPO im Wortlaut): Arrestatorium und Inhibitorium, zwei Drittschuldner, keine Anhörung (§ 834 ZPO)
– Wirksamkeit mit Zustellung an den Drittschuldner (§ 829 Abs. 3 ZPO im Wortlaut)
– 3. Überweisung zur Einziehung oder an Zahlungs statt (§ 835 ZPO), Wirkung (§ 836 Abs. 1 ZPO)
– 4. Drittschuldnererklärung binnen zwei Wochen (§ 840 Abs. 1 ZPO), Haftung (§ 840 Abs. 2 Satz 2 ZPO)
– 5. Lohnpfändung: §§ 850, 850a, 850c ZPO, Grundbetrag ab 1.7.2026, Pfändungstabelle, künftige Gehälter (§ 832 ZPO)
– 6. Kontopfändung: Pfändungsschutzkonto (§ 850k ZPO), Freibetrag (§ 899 ZPO)
– Ergebnis, Klausurtipp, Schema in fünf Schritten, Merksatz

Normen: §§ 828, 829, 832, 834, 835, 836, 840, 850, 850a, 850c, 850k, 899 ZPO; § 20 Abs. 1 Nr. 17 RPflG

Beträge: Pfändungsfreigrenzenbekanntmachung 2026 vom 19.3.2026, BGBl. 2026 I Nr. 80: unpfändbar ab 1.7.2026 nach § 850c Abs. 1 Nr. 1 ZPO 1.587,40 € monatlich; Freibetrag auf dem Pfändungsschutzkonto nach § 899 Abs. 1 ZPO aufgerundet 1.590 €. Die Beträge werden jedes Jahr zum 1. Juli angepasst.

Hinweise: Herr Dorfmann, Frau Kästner, die Personalleiterin und der Bankberater sind erfundene Figuren; Arbeitgeber und Bank sind fiktiv. Im Fall gibt es keine Unterhaltspflichten und keine früheren Pfändungen. Titel, Klausel und Zustellung sowie die Rechtsbehelfe gegen den Beschluss erklären eigene Videos.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Pfändung #2Examen #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|Nr\.|S\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
# „§ 835“ am Ende eines Untertitels, „Abs. 3.“ am Anfang des nächsten → zusammenführen
srt, n = re.subn(r"aus, (§ 835)\n\n(\d+\n[0-9:,]+ --> [0-9:,]+\n)Abs\. 3\. ", r"aus,\n\n\2\1 Abs. 3. ", srt)
assert n == 1, "Normzeile § 835 Abs. 3"
srt, n = re.subn(r"den (§§ 850)\n\n(\d+\n[0-9:,]+ --> [0-9:,]+\n)a bis i ", r"den\n\n\2\1a bis 850i ", srt)
assert n == 1, "Normzeile §§ 850a bis 850i"
for a, b in [("dreitausendsechshundert Euro", "3.600 Euro"),
             ("eintausendfünfhundertsiebenundachtzig\nEuro und vierzig Cent", "1.587,40 Euro"),
             ("eintausendfünfhundertneunzig Euro", "1.590 Euro"),
             ("ersten Juli", "1. Juli"), ("drei Zehntel", "3/10"), ("volle zehn Euro", "volle 10 Euro"),
             ("Dorfmann: Dann", "Herr Dorfmann: Dann"), ("Kästner: Mein", "Frau Kästner: Mein"),
             ("Kästner: Bitte", "Frau Kästner: Bitte")]:
    assert a in srt, a
    srt = srt.replace(a, b)
assert not re.search(r"§\n|Abs\.\n|Nr\.\n", srt) and "tausend" not in srt, "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
