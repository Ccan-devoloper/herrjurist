"""Nachbearbeitung der Upload-Texte für Folge 133 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Lizenzzeile;
Sprechernamen und Ziffern in den Untertiteln; Tags ergänzt. Kein Landesrecht.
Aufruf: python3 meta_133.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Marlies bürgt für den Kredit ihrer Schwester"), (T("frage"), "Frage und Sachverhalt"),
       (T("agl"), "Anspruch aus § 765 Abs. 1 BGB und Prüfungsaufbau"),
       (T("i1"), "Bürgschaftsvertrag und Schriftform, § 766 BGB, § 350 HGB"),
       (T("i2"), "Sittenwidrigkeit, § 138 BGB: krasse Überforderung?"),
       (T("i3"), "Hauptschuld (§ 767 BGB) und Erlöschen"), (T("iii"), "Einreden, §§ 768, 770 BGB"),
       (T("w771"), "Einrede der Vorausklage (§§ 771, 773 BGB) und Ergebnis"),
       (T("iv"), "Rückgriff: § 774 BGB und Auftrag, § 670 BGB"), (T("tipp"), "Klausurtipp: selbstschuldnerisch"),
       (T("sch"), "Klausurschema und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Bürgschaft Schema (§§ 765–774 BGB): Schriftform, Einreden des Bürgen und Regress nach § 774 BGB – was passiert, wenn die Schwester ihren Kredit nicht zahlt? Der Anspruch der Bank gegen die Bürgin Schritt für Schritt: entstanden, nicht erloschen, durchsetzbar – und danach der Rückgriff.

Der Fall: Hilke nimmt für eine neue Küche einen Bankkredit über 15.000 Euro auf, die Zinsen betragen 75 Euro im Monat. Die Bank verlangt eine Bürgschaft. Hilkes Schwester Marlies verdient netto 3.400 Euro und unterschreibt: „Ich bürge selbstschuldnerisch für den Kredit von Hilke über 15.000 Euro.“ Zwei Jahre später sind 9.000 Euro offen – und die Bank verlangt sie von Marlies. Muss sie zahlen, obwohl die Bank es noch nicht bei Hilke versucht hat? Und bekommt sie ihr Geld zurück?

Inhalt:
– Anspruch aus § 765 Abs. 1 BGB (Wortlaut) und Prüfungsaufbau
– I. 1. Bürgschaftsvertrag und Schriftform: § 766 Satz 1 und 2 BGB (Wortlaut), eigenhändige Unterschrift (§ 126 Abs. 1 BGB), Ausnahme für Kaufleute (§ 350 HGB)
– I. 2. Sittenwidrigkeit (§ 138 Abs. 1 BGB): krasse finanzielle Überforderung und Vermutung bei nahestehenden Bürgen – im Fall verneint
– I. 3. Hauptschuld und Akzessorietät (§ 767 Abs. 1 Satz 1 BGB)
– II. Anspruch nicht erloschen
– III. Durchsetzbarkeit: Einreden der Hauptschuldnerin (§ 768 BGB), Anfechtbarkeit und Aufrechenbarkeit (§ 770 BGB), Einrede der Vorausklage (§ 771 BGB) und ihr Ausschluss bei selbstschuldnerischer Bürgschaft (§ 773 Abs. 1 Nr. 1 BGB)
– IV. Rückgriff: gesetzlicher Forderungsübergang nach § 774 Abs. 1 Satz 1 BGB (wie § 426 Abs. 2 BGB) und Aufwendungsersatz aus Auftrag (§ 670 BGB); Insolvenzrisiko der Schuldnerin
– Klausurtipp: selbstschuldnerisch heißt nicht Gesamtschuld
– Klausurschema und Merksatz

Normen: §§ 126, 138, 488, 670, 765, 766, 767, 768, 770, 771, 773, 774 BGB; § 350 HGB

Rechtsprechung:
– BGH, Urt. v. 19.2.2013 – XI ZR 82/11, Rn. 9 (krasse finanzielle Überforderung nahestehender Bürgen, widerlegliche Vermutung)
– BGH, Urt. v. 7.12.2023 – IX ZR 36/22, Rn. 17, 20 (auch der selbstschuldnerische Bürge ist kein Gesamtschuldner; Freiwerden als Folge der Akzessorietät)
– BGH, Urt. v. 24.10.2017 – XI ZR 362/15, Rn. 20, 21 (Regress nach § 670 BGB oder über § 774 Abs. 1 Satz 1 BGB; Insolvenzrisiko des Hauptschuldners)

Kapitel:
{kapitel}

Das Prüfungsschema ist eine Klausurkonvention. Im Fall ist unterstellt, dass die Bitte um die Bürgschaft ein Auftrag (§ 662 BGB) ist und die Bank den Kredit wirksam gekündigt hat. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Bürgschaft #Zivilrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("\nSeibold:", "\nHerr Seibold:")
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
for alt, neu in (("fünfzehntausend Euro", "15.000 Euro"), ("neuntausend Euro", "9.000 Euro"),
                 ("dreitausendvierhundert Euro", "3.400 Euro"), ("fünfundsiebzig Euro", "75 Euro")):
    w, e = alt.split(" ")
    srt = re.sub(w + r"(\s+)" + e, lambda mm: neu.split(" ")[0] + mm.group(1) + e, srt)
for alt, neu in (("eins", "I."), ("zwei", "II."), ("drei", "III."), ("vier", "IV.")):
    srt = re.sub(r"Römisch(\s)" + alt, r"\g<1>" + neu, srt)
srt = re.sub(r"(^|\n) (I|II|III|IV)\.", r"\1\2.", srt)
srt = re.sub(r"\b(I|II|III|IV)\.:", r"\1.", srt).replace(".  ", ". ")
assert "Römisch" not in srt, re.findall(r".{20}Römisch.{20}", srt)
assert not re.search(r"§\n", srt)
assert "tausend" not in srt, re.findall(r".{20}tausend.{20}", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("Bürgschaft Schema", "selbstschuldnerische Bürgschaft", "§ 773 BGB", "Bürgschaft Sittenwidrigkeit"):
    if t not in m.get("tags", []):
        m.setdefault("tags", []).append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
