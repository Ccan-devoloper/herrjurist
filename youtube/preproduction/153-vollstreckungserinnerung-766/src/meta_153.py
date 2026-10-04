"""Nachbearbeitung der Upload-Texte für Folge 153 (nach meta_150.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit
Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Betrag als Ziffern, Sprechername, Normzeilen).
Aufruf: python3 meta_153.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Pfändung ohne Zustellung"),
       (T("zul"), "A. Zulässigkeit: Statthaftigkeit, § 766 Abs. 1 ZPO"),
       (T("a793"), "Abgrenzung zur sofortigen Beschwerde, § 793 ZPO"),
       (T("anh"), "Maßnahme oder Entscheidung? Anhörung, § 11 RPflG"),
       (T("zust2"), "Zuständigkeit und Richtervorbehalt"),
       (T("bef"), "Erinnerungsbefugnis"),
       (T("frist"), "Frist und Rechtsschutzbedürfnis"),
       (T("begr"), "B. Begründetheit: § 750 Abs. 1 ZPO"),
       (T("zeit"), "Zeitpunkt und Heilung"),
       (T("ent"), "Entscheidung, Tenor, Eilschutz"),
       (T("tab"), "Abgrenzung zu § 767 und § 771 ZPO"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Vollstreckungserinnerung nach § 766 ZPO: Statthaftigkeit, Befugnis, Begründetheit – und wann stattdessen die sofortige Beschwerde nach § 793 ZPO einschlägig ist.

Der Fall: Frau Bergmann hat gegen Herrn Mühlbauer ein vorläufig vollstreckbares Urteil über 900 € und eine Ausfertigung mit Vollstreckungsklausel. Der Gerichtsvollzieher pfändet seinen Fernseher und klebt eine Siegelmarke auf – das Urteil wurde Herrn Mühlbauer aber weder vorher noch bei der Pfändung zugestellt.

Inhalt:
– A. Zulässigkeit: Statthaftigkeit nach § 766 Abs. 1 Satz 1 ZPO (im Wortlaut), Vollstreckungsvoraussetzungen
– Abgrenzung zur sofortigen Beschwerde (§ 793 ZPO im Wortlaut): Vollstreckungsmaßnahme oder Entscheidung, vorherige Anhörung, § 834 ZPO, § 11 Abs. 1 RPflG
– Zuständigkeit: Vollstreckungsgericht (§ 764 ZPO), ausschließlich (§ 802 ZPO), Richtervorbehalt (§ 20 Abs. 1 Nr. 17 RPflG)
– Erinnerungsbefugnis, keine Frist, Rechtsschutzbedürfnis bis zur Beendigung der Maßnahme
– B. Begründetheit: § 750 Abs. 1 ZPO (Zustellung spätestens gleichzeitig), nur anfechtbar, Zeitpunkt der Entscheidung, Heilung durch Nachholung der Zustellung
– Entscheidung durch Beschluss, üblicher Tenor, einstweilige Anordnung (§ 766 Abs. 1 Satz 2, § 732 Abs. 2 ZPO)
– Abgrenzung zu § 767 und § 771 ZPO, Klausurtipp, Prüfschema, Merksatz

Normen: §§ 732, 750, 764, 766, 793, 802, 834 ZPO; §§ 11, 20 Abs. 1 Nr. 17 RPflG

Rechtsprechung:
– BGH, Beschl. v. 18.5.2017 – VII ZB 38/16, Rn. 37 (Erinnerung: Vollstreckungsvoraussetzungen)
– BGH, Beschl. v. 12.10.2023 – IX ZB 60/21, Rn. 34 (Vollstreckungsmaßnahme: § 766; Vollstreckungsentscheidung: § 793, § 11 Abs. 1 RPflG)
– BGH, Beschl. v. 19.12.2024 – V ZB 77/23, Rn. 13 (vorherige Anhörung)
– BGH, Beschl. v. 4.5.2022 – VII ZB 18/18, Rn. 23, 25 (Zeitpunkt der Entscheidung; Pfändungsbeschluss ohne Anhörung)
– BGH, Beschl. v. 26.9.2013 – V ZB 42/13, Rn. 9 (Zustellung und rechtliches Gehör)
– BGH, Beschl. v. 27.10.2016 – V ZB 48/15, Rn. 9 f. (fehlende Zustellung nur anfechtbar, Heilung)
– BGH, Beschl. v. 13.8.2009 – I ZB 91/08, Rn. 9; Beschl. v. 30.4.2013 – VII ZB 22/12, Rn. 25; Beschl. v. 17.9.2014 – VII ZB 22/13, Rn. 19 (Erinnerungsbefugnis)
– BGH, Beschl. v. 2.3.2017 – I ZB 66/16, Rn. 5 (Rechtsschutzbedürfnis, Aufhebung)

Hinweise: Frau Bergmann, Herr Mühlbauer und der Gerichtsvollzieher sind erfundene Figuren. Der Tenor ist als übliche Fassung gekennzeichnet. Den Überblick über die Rechtsbehelfe in der Zwangsvollstreckung, die Vollstreckungsabwehrklage und die Drittwiderspruchsklage erklären eigene Videos. § 750 ZPO gilt in der seit 1. Oktober 2026 geltenden Fassung.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Vollstreckungserinnerung #2Examen #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|Nr\.|S\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(§ \d+)\n(Abs\. \d+ S\. \d+)", r"\1 \2\n", srt)
srt, n = re.subn(r"einstellen, (§ 766)\n\n(\d+\n[0-9:,]+ --> [0-9:,]+\n)(Abs\. 1 S\. 2)", r"einstellen,\n\n\2\1 \3", srt)
assert n == 1, "Normzeile § 766 Abs. 1 S. 2"
for a, b in [("neunhundert Euro", "900 Euro"), ("Mühlbauer: Das Urteil", "Herr Mühlbauer: Das Urteil")]:
    assert a in srt, a
    srt = srt.replace(a, b)
assert not re.search(r"§\n|Abs\.\n|Nr\.\n", srt) and "neunhundert" not in srt, "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
