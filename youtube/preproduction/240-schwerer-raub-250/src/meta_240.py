"""Nachbearbeitung der Upload-Texte für Folge 240 (nach meta_236.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen, Paragrafen).
Aufruf: python3 meta_240.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Die Spielzeugpistole in der Bäckerei"),
       (T("frage"), "Die Frage und der Sachverhalt"),
       (T("raub"), "Grundtatbestand: Raub, § 249 StGB"),
       (T("q"), "§ 250 Abs. 1 Nr. 1 StGB im Wortlaut"),
       (T("na"), "Buchstabe a: Ist die Spielzeugpistole eine Waffe?"),
       (T("nb"), "Buchstabe b: Scheinwaffe als sonstiges Mittel"),
       (T("lab"), "Die Grenze: der Labello-Fall"),
       (T("krit"), "Streitstand: Kritik an der Labello-Grenze"),
       (T("abs2"), "§ 250 Abs. 2 Nr. 1 StGB: Verwenden einer Waffe"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Schwerer Raub § 250 StGB: Ist eine Spielzeugpistole ein sonstiges Werkzeug oder Mittel – und warum reicht der Labello im Rücken nicht? Der Streitstand zur Scheinwaffe, klausurfest aufgebaut.

Der Fall: Früh am Morgen bedroht Alois die Bäckereiverkäuferin Wiltrud mit einer Pistole, die täuschend echt aussieht, nimmt 300 € aus der Kasse und flieht. An der Tür fällt ihm die Pistole aus der Jacke – ein Spielzeug aus Plastik. Abwandlung: Statt der Pistole drückt er ihr einen Lippenpflegestift in den Rücken.

Inhalt:
– Grundtatbestand: Raub nach § 249 StGB, Drohung auch mit einem Spielzeug
– § 250 Abs. 1 Nr. 1 StGB im Wortlaut
– Buchstabe a: Waffe oder anderes gefährliches Werkzeug? Spielzeugpistolen sind ausgeklammert
– Buchstabe b: Scheinwaffe als „sonst ein Werkzeug oder Mittel“ (6. Strafrechtsreformgesetz 1998)
– Die Grenze: der Labello-Fall – offensichtlich ungefährliche Gegenstände, objektiver Betrachter, grellbunte Wasserpistole
– Streitstand: Kritik an der Grenze und die Haltung des BGH
– § 250 Abs. 2 Nr. 1 StGB: Verwenden einer Waffe – nicht mit einer Scheinwaffe
– Ergebnis, Klausurtipp zur Prüfungsreihenfolge, Klausurschema, Merksatz

Normen: §§ 249, 250 Abs. 1 Nr. 1 a, b, Abs. 2 Nr. 1, 255 StGB

Rechtsprechung und Materialien:
– BGH NStZ 1997, 184 (Labello-Fall)
– BGH, Urt. v. 18.1.2007 – 4 StR 394/06, Rn. 6–9 (Scheinwaffen erfasst; Labello-Grenze gilt nach dem 6. StrRG fort)
– BGH, Urt. v. 11.5.1999 – 4 StR 380/98, BGHSt 45, 92, Rn. 5–7 (Waffenbegriff; Spielzeugpistolen ausgeklammert; Verwenden als Drohmittel)
– BGH, Beschl. v. 6.9.2007 – 4 StR 227/07, Rn. 3 (Spielzeugpistole: § 250 Abs. 1 Nr. 1 b, nicht Abs. 2 Nr. 1)
– BGH, Beschl. v. 11.5.2011 – 2 StR 618/10, Rn. 3–5 (grellbunte Wasserpistole; objektiver Betrachter)
– BGH, Beschl. v. 28.3.2023 – 4 StR 61/23, Rn. 5 (Scheinwaffen und einschränkende Auslegung)
– Bericht des Rechtsausschusses zum 6. StrRG, BT-Drucks. 13/9064, S. 18

Hinweise: Die Einzelheiten zum Grundtatbestand erklärt das Video „Raub § 249 StGB: Prüfungsschema mit Gewalt, Wegnahme & Finalität“. Minder schwere Fälle (§ 250 Abs. 3 StGB) sind nicht Gegenstand des Videos. Personen frei erfunden.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#SchwererRaub #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("dreihundert Euro", "300 Euro"), ("dreihundert\nEuro", "300\nEuro"),
             ("neunzehnhundertachtundneunzig", "1998"), ("sechsten\nStrafrechtsreformgesetz", "6.\nStrafrechtsreformgesetz"),
             ("sechsten Strafrechtsreformgesetz", "6. Strafrechtsreformgesetz"),
             ("drei Jahren", "3 Jahren"), ("fünf Jahren", "5 Jahren"), ("drei Jahre, nicht fünf", "3 Jahre, nicht 5")]:
    srt = srt.replace(a, b)
for w, z in (("Erstens", "1."), ("Zweitens", "2."), ("Drittens", "3.")):
    srt = re.sub(rf"(?m)^{w} ", f"{z} ", srt)
    srt = re.sub(rf"(\. |\n|: ){w} ", rf"\g<1>{z} ", srt)
for w, z in (("Römisch eins", "I."), ("Römisch zwei", "II."), ("Römisch drei", "III.")):
    srt = srt.replace(w + ":", z).replace(w.replace(" ", "\n") + ":", z)
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
rest = re.findall(r".{0,25}(?:tausend|hundert|Erstens|Zweitens|Drittens|Römisch|Paragraf).{0,15}", srt, re.I)
assert not rest, rest
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
