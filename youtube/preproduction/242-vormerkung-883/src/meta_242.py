"""Nachbearbeitung der Upload-Texte für Folge 242 (nach meta_239.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen, Paragrafen).
Aufruf: python3 meta_242.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Das Haus wird doppelt verkauft"),
       (T("frage"), "Hat Mats das Haus verloren? Sachverhalt"),
       (T("prob"), "Das Problem: die Zeit bis zur Eintragung"),
       (T("norm"), "§ 883 Abs. 1 BGB: vier Voraussetzungen"),
       (T("a1"), "1. Zu sichernder Anspruch, Akzessorietät"),
       (T("b1"), "2. Bewilligung oder einstweilige Verfügung"),
       (T("e1"), "3. Eintragung und 4. Berechtigung"),
       (T("wirk"), "Wirkung: relative Unwirksamkeit, § 883 Abs. 2"),
       (T("durch"), "Durchsetzung: Zustimmung nach § 888 Abs. 1"),
       (T("erg"), "Ergebnis und Insolvenz, § 106 InsO"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Vormerkung (§§ 883–888 BGB): Wie schützt sie den Käufer, wenn der Verkäufer das Haus noch einmal verkauft? Relative Unwirksamkeit und Zustimmungsanspruch nach § 888 BGB.

Der Fall: Mats kauft von Herrn Stenzel ein Haus für 420.000 €. Beim Notar unterschreiben beide den Kaufvertrag, und Herr Stenzel bewilligt eine Vormerkung für Mats, die zwei Wochen später eingetragen wird. Dann bietet Frau Ostendorf 470.000 € – Herr Stenzel verkauft ihr das Haus, erklärt die Auflassung, und sie wird als Eigentümerin eingetragen. Hat Mats das Haus verloren?

Inhalt:
– Das Problem: Eigentum gibt es erst mit der Eintragung (§§ 873, 925 BGB) – bis dahin kann der Verkäufer noch einmal verfügen
– § 883 Abs. 1 BGB im Wortlaut und die vier Voraussetzungen
– 1. Zu sichernder Anspruch: Übereignungsanspruch aus § 433 BGB, strenge Akzessorietät, künftige und bedingte Ansprüche
– 2. Bewilligung (§ 885 Abs. 1 BGB im Wortlaut) oder einstweilige Verfügung ohne Glaubhaftmachung der Gefährdung
– 3. Eintragung und 4. Berechtigung des Bewilligenden; gutgläubiger Ersterwerb nur bei bestehendem Anspruch
– Wirkung: § 883 Abs. 2 BGB im Wortlaut – die vormerkungswidrige Verfügung ist relativ unwirksam
– Durchsetzung: § 888 Abs. 1 BGB – Zustimmung des Zweiterwerbers zur Eintragung; Ansprüche gegen Verkäufer und Zweiterwerberin
– Ergebnis und Insolvenzfestigkeit (§ 106 Abs. 1 InsO), Klausurtipp, Klausurschema, Merksatz

Normen: §§ 433 Abs. 1 S. 1, 873 Abs. 1, 883 Abs. 1 und 2, 885 Abs. 1, 888 Abs. 1, 892 Abs. 1 S. 1, 925 Abs. 1 BGB; § 106 Abs. 1 InsO

Rechtsprechung:
– BGH, Urt. v. 2.7.2010 – V ZR 240/09, Rn. 7, 8, 10, 13 (relative Unwirksamkeit; Zustimmung nach § 888 Abs. 1 BGB als Hilfsanspruch; Einwendungen des Dritten; Ansprüche gegen Verkäufer und Dritterwerber)
– BGH, Urt. v. 8.3.2024 – V ZR 176/22, Rn. 24, 31 (streng akzessorisches Sicherungsmittel; gutgläubiger Ersterwerb nur bei bestehendem Anspruch)
– BGH, Urt. v. 9.12.2022 – V ZR 91/21, Rn. 23 (gutgläubiger Ersterwerb der Vormerkung)
– BGH, Urt. v. 25.3.2021 – IX ZR 70/20, Rn. 34 (vormerkungsgesicherter Anspruch insolvenzfest, § 106 Abs. 1 InsO)

Hinweise: Das Grundbuchblatt im Video ist vereinfacht dargestellt. Ansprüche der Zweitkäuferin gegen den Verkäufer, der Rang der Vormerkung (§ 883 Abs. 3 BGB) und der gutgläubige Zweiterwerb einer Vormerkung sind nicht Thema dieses Videos. Mehr zu Kaufvertrag, Auflassung und Eintragung im Video „Hauskauf in drei Schritten: Kaufvertrag, Auflassung, Grundbuch“. Personen frei erfunden.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Vormerkung #Sachenrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for a, b in [("vierhundertzwanzigtausend Euro", "420.000 Euro"), ("vierhundertsiebzigtausend Euro", "470.000 Euro")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt, n = re.subn(r"Eintragung, §§ 873\n\n(\d+\n[^\n]+\n)und neunhundertfünfundzwanzig\.", r"Eintragung,\n\n\1§§ 873 und 925.", srt)
assert n == 1
srt, n = re.subn(r"aus § 888\n\n(\d+\n[^\n]+\n)Abs\. 1, hier", r"aus\n\n\1§ 888 Abs. 1, hier", srt)
assert n == 1
srt, n = re.subn(r"nach § 106 der\n\n(\d+\n[^\n]+\n)Insolvenzordnung", r"nach\n\n\1§ 106 der Insolvenzordnung", srt)
assert n == 1
for a, b in [("Römisch eins: ", "I. "), ("Römisch zwei: ", "II. "), ("Römisch drei: ", "III. ")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"(?m)^ +| +$", "", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|S\.\n", srt), "Untertitel prüfen"
rest = re.findall(r".{0,25}(?:tausend|hundert|Römisch|Paragraf).{0,15}", srt, re.I)
assert not rest, rest
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
