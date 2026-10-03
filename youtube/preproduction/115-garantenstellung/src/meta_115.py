"""Nachbearbeitung der Upload-Texte für Folge 115 (Kopie von meta_112.py) (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_115.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Die Parkbank im Frost"),
       (T("vorab"), "Einordnung: Körperverletzung durch Unterlassen, §§ 223, 13 StGB"),
       (T("p13"), "§ 13 Abs. 1 StGB: rechtlich einstehen"),
       (T("funk"), "Funktionenlehre: Beschützer- und Überwachergaranten"),
       (T("fam2"), "Familie? Gefahrengemeinschaft? Zechkumpane"),
       (T("ueb2"), "Tatsächliche Übernahme"),
       (T("selbst"), "Selbst betrunken?"),
       (T("entspr"), "Entsprechung, Vorsatz, Ergebnis"),
       (T("gegen"), "Gegenfall und § 323c StGB"),
       (T("tipp"), "Klausurtipp: Garantenstellung begründen"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Garantenstellung nach § 13 StGB: Welche Beschützer- und Überwachergaranten gibt es – Familie, Gefahrengemeinschaft, Übernahme, Gefahrenquelle?

Der Fall: In einer kalten Winternacht sitzt Karsten mit seinem volltrunkenen Freund Wolfgang in der letzten Kneipe. Die Wirtin will ein Taxi rufen. Karsten: „Nicht nötig. Ich bring ihn nach Hause.“ Die Wirtin ruft deshalb kein Taxi. Bei -8 °C setzt Karsten Wolfgang auf eine Parkbank und geht – eine Unterkühlung nimmt er in Kauf. Eine Stunde später findet eine Passantin Wolfgang; er erholt sich. Musste Karsten die Unterkühlung verhindern?

Inhalt:
– Einordnung: Tun oder Unterlassen (Schwerpunkt der Vorwerfbarkeit), Körperverletzung durch Unterlassen, §§ 223, 13 StGB; das allgemeine Schema im Video „Unechtes Unterlassen“
– § 13 Abs. 1 StGB im Wortlaut: „rechtlich dafür einzustehen“
– Funktionenlehre: Beschützergaranten (familiäre Verbundenheit, enge Lebens- oder Gefahrengemeinschaft, tatsächliche Übernahme) und Überwachergaranten (Ingerenz, Gefahrenquelle, Aufsicht über andere)
– Im Fall: keine Familie, keine Gefahrengemeinschaft durch bloßes Zechen – aber tatsächliche Übernahme durch Zusage, Vertrauen der Wirtin und Herausführen in die Kälte
– Selbst betrunken? Die Garantenpflicht bleibt (mehr im Video zur eigenverantwortlichen Selbstgefährdung)
– Entsprechung, Vorsatz, Ergebnis und Strafmilderung nach § 13 Abs. 2 StGB
– Gegenfall: nur gezecht, nichts zugesagt – dann nur die Jedermannspflicht aus § 323c StGB (Wortlaut)
– Klausurtipp (Aussetzung, § 221 Abs. 1 Nr. 2 StGB), Prüfschema, Merksatz

Normen: §§ 13, 223, 323c StGB; § 221 StGB

Rechtsprechung:
– BGH, Urt. v. 11.9.2019 – 2 StR 563/18, Rn. 12, 14, 17 f. (lose Zech- oder Konsumgemeinschaft begründet regelmäßig keine Garantenstellung; maßgeblich ist die tatsächliche Übernahme; bloße Kenntnis der Hilfsbedürftigkeit begründet nur Pflichten nach § 323c StGB)
– BGH, Urt. v. 17.7.2009 – 5 StR 394/08, Rn. 23, 25 (Übernahme eines Pflichtenkreises; maßgebend ist die tatsächliche Übernahme)
– BGH, Urt. v. 31.1.2002 – 4 StR 289/01, Rn. 20, 22, 27 (tatsächliche Übernahme statt Vertrag; Pflicht bis zur vollständigen Erfüllung der Schutzaufgabe; zurechenbar begründetes Vertrauen)
– BGH, Beschl. v. 5.8.2015 – 1 StR 328/15, Rn. 18 (Garantenpflicht trotz zunächst eigenverantwortlicher Selbstgefährdung)
– BGH, Beschl. v. 17.3.2022 – 2 StR 157/21, Rn. 13 (Schwerpunkt der Vorwerfbarkeit)
– BGH, Beschl. v. 26.2.2015 – 4 StR 548/14, Rn. 4 (Gesundheitsschädigung)
– BGH, Urt. v. 29.9.2021 – 2 StR 491/20, Rn. 27, 35 (Aussetzung durch Im-Stich-Lassen als Garant; echtes Unterlassungsdelikt)

Hinweise: Das Video prüft bewusst nur die Körperverletzung durch Unterlassen („jedenfalls strafbar“); Aussetzung (§ 221 Abs. 1 Nr. 2 StGB) und gefährliche Körperverletzung (§ 224 Abs. 1 Nr. 5 StGB) bleiben offen. Ob daneben Ingerenz vorliegt, lässt das Video offen. Beschützer- und Überwachergarant sind Begriffe der Lehre (Funktionenlehre).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026 (StGB zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Garantenstellung #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace("§§ 223 und dreizehn", "§§ 223 und 13").replace("\nund dreizehn. ", "\nund 13. ").replace("§ 323 c", "§ 323c")
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
