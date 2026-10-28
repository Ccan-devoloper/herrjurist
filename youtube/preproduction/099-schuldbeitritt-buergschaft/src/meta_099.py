"""Nachbearbeitung der Upload-Texte für Folge 099 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Lizenzzeile;
Sprechernamen und Ziffern in den Untertiteln; Tags ergänzt. Kein Landesrecht.
Aufruf: python3 meta_099.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Katja „übernimmt“ die Autoschulden von Jochen"), (T("frage"), "Frage und Sachverhalt"),
       (T("ausl"), "Auslegung, §§ 133, 157 BGB"), (T("w414"), "Befreiende Schuldübernahme, §§ 414, 415, 417 BGB"),
       (T("beit"), "Schuldbeitritt"), (T("w765"), "Bürgschaft, §§ 765, 767–771 BGB"),
       (T("w766"), "Schriftform, § 766 BGB"), (T("tab"), "Abgrenzung im Überblick"),
       (T("k1q"), "Abgrenzung in 2 Schritten: Entlassung, eigene oder fremde Schuld"),
       (T("sub"), "Lösung des Falls und Ergebnis"), (T("tipp"), "Klausurtipp: Verbraucherdarlehen und Sittenwidrigkeit"),
       (T("sch"), "Klausurschema und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Schuldübernahme (§§ 414, 415 BGB), Schuldbeitritt oder Bürgschaft (§ 765 BGB)? Erst fragen: Wird der Altschuldner frei? Dann entscheidet der Wille – eigene Schuld oder Einstehen für eine fremde. Mit Auslegung, Dreispalter und Klausurschema.

Der Fall: Jochen finanziert ein gebrauchtes Auto mit einem Bankkredit über 18.000 Euro. Die Bank will eine weitere Sicherheit, Jochen bleibt Kreditnehmer. Seine Freundin Katja schreibt mit der Hand an die Bank: „Ich übernehme die Schulden von Jochen aus dem Autokredit über 18.000 Euro.“ Ein Jahr später sind 12.000 Euro offen – und die Bank verlangt sie von Katja. Was hat sie da eigentlich unterschrieben?

Inhalt:
– Auslegung nach §§ 133, 157 BGB: nicht allein das Wort „übernehmen“
– Befreiende Schuldübernahme: Wortlaut § 414 BGB, Genehmigung nach § 415 BGB, Einwendungen nach § 417 BGB, deutlicher Entlassungswille des Gläubigers
– Schuldbeitritt (kumulative Schuldübernahme): Vertrag nach § 311 Abs. 1 BGB, Gesamtschuld (§ 421 BGB), nicht akzessorisch, grundsätzlich formfrei
– Bürgschaft: Wortlaut § 765 Abs. 1 BGB, Akzessorietät (§ 767 BGB), Einreden (§§ 768, 770 BGB), Einrede der Vorausklage (§ 771 BGB), Schriftform nach § 766 Satz 1 und 2 BGB
– Abgrenzung im Überblick und in zwei Schritten: Soll der Altschuldner frei werden? Eigene Schuld oder Einstehen für fremde Schuld, eigenes Interesse als Indiz, im Zweifel Bürgschaft
– Lösung: Katja haftet als Bürgin
– Klausurtipp: Verbraucherdarlehensrecht beim Schuldbeitritt eines Verbrauchers; Sittenwidrigkeit bei krasser finanzieller Überforderung Nahestehender (§ 138 Abs. 1 BGB)
– Klausurschema und Merksatz

Normen: §§ 126, 133, 138, 157, 311 Abs. 1, 414, 415, 417, 421, 491 ff., 765, 766, 767, 768, 770, 771 BGB

Rechtsprechung:
– BGH, Versäumnisurt. v. 3.9.2020 – III ZR 56/19, Rn. 18–20 (Auslegung; Schuldbeitritt als Gesamtschuld; eigenes wirtschaftliches oder rechtliches Interesse als wichtiger Anhaltspunkt)
– BGH, Urt. v. 12.4.2012 – VII ZR 13/11, Rn. 7 (befreiende Schuldübernahme: Entlassungswille des Gläubigers muss deutlich werden)
– BGH, Urt. v. 12.11.2015 – I ZR 168/14, Rn. 40 (Schuldbeitritt nicht akzessorisch)
– BGH, Urt. v. 12.5.2016 – IX ZR 208/15, Rn. 6, 7 (Eigeninteresse keine Voraussetzung; grundsätzlich formfrei)
– BGH, Versäumnisurt. v. 21.9.2021 – XI ZR 650/20, Rn. 11 (Verbraucherdarlehensrecht auf den Schuldbeitritt entsprechend)
– BGH, Urt. v. 19.2.2013 – XI ZR 82/11, Rn. 9 (krasse finanzielle Überforderung nahestehender Bürgen)
„Im Zweifel Bürgschaft“ ist im Video als herrschende Meinung bezeichnet.

Kapitel:
{kapitel}

Das Prüfungsschema ist eine Klausurkonvention. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Schuldbeitritt #Bürgschaft #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("\nZöllner:", "\nFrau Zöllner:")
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
for alt, neu in (("achtzehntausend Euro", "18.000 Euro"), ("zwölftausend Euro", "12.000 Euro"),
                 ("Zwölftausend Euro", "12.000 Euro"), ("eins", "I."), ("zwei", "II."), ("drei", "III."),
                 ("vier", "IV."), ("fünf", "V.")):
    srt = re.sub(r"Römisch(\s)" + alt, r"\g<1>" + neu, srt) if not alt[0].isdigit() and "Euro" not in alt else srt.replace(alt, neu)
srt = re.sub(r"(^|\n) (I|II|III|IV|V)\.", r"\1\2.", srt)
srt = re.sub(r"\b(I|II|III|IV|V)\.:", r"\1.", srt).replace(".  ", ". ")
assert "Römisch" not in srt
assert not re.search(r"§\n", srt)
assert "tausend" not in srt, re.findall(r".{20}tausend.{20}", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Schuldbeitritt", "Bürgschaft § 765 BGB", "§ 766 BGB Schriftform", "Schuldübernahme § 414 BGB"):
    if t not in m.get("tags", []):
        m.setdefault("tags", []).append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
