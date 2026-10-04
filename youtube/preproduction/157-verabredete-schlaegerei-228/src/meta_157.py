"""Nachbearbeitung der Upload-Texte für Folge 157 (nach meta_146.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn.,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen und Daten als Ziffern, „des §§ 231“ → „des § 231“, „Römisch …“).
Aufruf: python3 meta_157.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Das verabredete Match"),
       (T("echt"), "Der echte Fall: BGHSt 58, 140"),
       (T("einw"), "Einwilligung und § 228 StGB"),
       (T("mass"), "Maßstab der guten Sitten"),
       (T("gesamt"), "Eskalationsgefahr bei Gruppen"),
       (T("p231"), "Wertung des § 231 StGB"),
       (T("sport"), "Abgrenzung: Boxkampf"),
       (T("offen"), "Absprachen und Schiedsrichter: BGHSt 60, 166"),
       (T("s2"), "Lösung des Falls"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Verabredete Schlägerei (BGHSt 58, 140): Wann ist die Einwilligung in Prügel wegen Sittenwidrigkeit § 228 StGB unwirksam?

Der Fall: Zwei Gruppen verabreden per Chat ein „Match“ auf einer Wiese: 10 gegen 10, keine Waffen, zwei Schiedsrichter. Alle sind einverstanden. Rechtfertigt die Einwilligung die Schläge? Die Antwort gibt der Bundesgerichtshof: Bei verabredeten Schlägereien zwischen rivalisierenden Gruppen zählt die typische Eskalationsgefahr. Fehlen wirksame Absprachen und effektive Sicherungen, verstoßen die Körperverletzungen trotz Einwilligung gegen die guten Sitten (BGH, Beschluss vom 20. Februar 2013 – 1 StR 585/12).

Inhalt:
– Der echte Fall: zwei Gruppen, faktische Übereinkunft über Faustschläge und Fußtritte, LG Stuttgart, BGH
– Einwilligung als Rechtfertigungsgrund und § 228 StGB (im Wortlaut)
– Maßstab der Rechtsprechung: Art und Gewicht der Verletzung, Gefahr für Leib und Leben, Sicht vor der Tat, konkrete Todesgefahr, Rolle des Zwecks
– Eskalationsgefahr, fehlende Absprachen und Sicherungen, Wertung des § 231 StGB (im Wortlaut)
– Abgrenzung zum Boxkampf mit Wettkampfregeln
– Absprachen und „Schiedsrichter“: Hooligan-Kämpfe mit Regeln (BGHSt 60, 166)
– Lösung des Falls (§§ 223, 224 Abs. 1 Nr. 4 StGB), Ergebnis, Klausurtipp, Prüfschema, Merksatz

Normen: §§ 223, 224 Abs. 1 Nr. 4, 228, 231 StGB

Rechtsprechung (Randnummern nach HRRS):
– BGH, Beschl. v. 20.2.2013 – 1 StR 585/12, BGHSt 58, 140 (verabredete Schlägerei): Rn. 4 f. (Sachverhalt), 7 (Einwilligung), 9, 12 (Maßstab), 13, 15 (Sport), 17 (Eskalationsgefahr, § 231), 18, 20, 22 (fehlende Absprachen und Sicherungen), 23 (Absprachen offengelassen)
– BGH, Urt. v. 22.1.2015 – 3 StR 233/14, BGHSt 60, 166 (Hooligans): Rn. 7, 42, 44 f., 47 f., 50–52, 54
– BGH, Urt. v. 26.5.2004 – 2 StR 505/03, BGHSt 49, 166: Rn. 22–24, 26, 29

Hinweise: Sönke und Inken sind erfundene Figuren; die Beteiligten der echten Fälle werden nicht dargestellt, Gewalt wird nicht gezeigt. Die Voraussetzungen der Einwilligung erklärt eine eigene Folge (Einwilligung: Wann ist eine Körperverletzung erlaubt?). Nicht behandelt: § 224 Abs. 1 Nr. 5 StGB, § 231 Abs. 2 StGB, Kritik der Literatur.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Sittenwidrigkeit228 #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|Nr\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("zwanzigsten Februar 2013", "20. Februar 2013"), ("zehn gegen\nzehn", "10 gegen\n10"),
             ("zehn gegen zehn", "10 gegen 10"), ("§§ 231", "§ 231"),
             ("zwei Schiedsrichter", "2 Schiedsrichter"), ("Zwei Schiedsrichter", "2 Schiedsrichter")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
assert not re.search(r"§\n|Abs\.\n|des §§", srt) and "zwanzigst" not in srt and "Römisch" not in srt, "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
