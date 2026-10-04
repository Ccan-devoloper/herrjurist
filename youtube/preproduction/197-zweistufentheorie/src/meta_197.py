"""Nachbearbeitung der Upload-Texte für Folge 197 (nach meta_192.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit korrigiertem Planbeginn (Einwirkungsanspruch gegen
die Gemeinde, nicht gegen die GmbH), Fall, Inhalt, Normen, geprüfte Ländernormen, Rechtsprechung, Hinweisen und Lizenzzeile;
Untertitel-Korrekturen (Gliederung, Normen, Sprecher).
Aufruf: python3 meta_197.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Stadthalle, Chor und städtische GmbH"),
       (T("prob"), "Das Problem: Rechtsweg und Anspruchsgegner"),
       (T("zst"), "Die Zweistufentheorie: Ob und Wie"),
       (T("go"), "1. Stufe: Zulassungsanspruch, § 8 GO NRW"),
       (T("tab"), "Andere Länder und Art. 28 Abs. 2 GG"),
       (T("vor"), "Grenzen: Widmung, Kapazität, Gleichbehandlung"),
       (T("wie"), "2. Stufe: der Mietvertrag"),
       (T("gmbh"), "Eigengesellschaft: Einwirkungsanspruch gegen die Stadt"),
       (T("rweg"), "Rechtsweg: § 40 Abs. 1 S. 1 VwGO"),
       (T("weitere"), "Förderkredit und Kita-Platz"),
       (T("krit"), "Streitstand: Kritik an der Zweistufentheorie"),
       (T("loes"), "Lösung des Falls"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Zweistufentheorie: Das Ob der Zulassung ist öffentlich-rechtlich, das Wie oft privatrechtlich – betreibt eine städtische GmbH die Halle, hilft der Einwirkungsanspruch gegen die Gemeinde (§ 40 VwGO).

Der Fall: Die Stadt betreibt ihre Stadthalle über eine eigene GmbH. Die GmbH vermietet den Saal nicht an den Chor, weil er dem Bürgermeister nicht gefällt – den Schachclub hat sie spielen lassen. Kann der Chor den Saal verlangen, und von wem?

Inhalt:
– Das Problem: Die Stadt handelt durch eine private Gesellschaft – Rechtsweg und Anspruchsgegner
– Die Zweistufentheorie: 1. Stufe „Ob“ (Zulassung, öffentlich-rechtlich), 2. Stufe „Wie“ (Mietvertrag, kann privatrechtlich sein)
– Zulassungsanspruch aus der Gemeindeordnung: § 8 Abs. 2, 4 GO NRW im Wortlaut; Art. 28 Abs. 2 S. 1 GG im Wortlaut
– Grenzen: Widmung, Kapazität, Gleichbehandlung (Art. 3 Abs. 1 GG)
– Eigengesellschaft: kein Zulassungsanspruch gegen die GmbH, sondern Verschaffungs- bzw. Einwirkungsanspruch gegen die Gemeinde; Verwaltungsrechtsweg nach § 40 Abs. 1 S. 1 VwGO
– Weitere Fälle: Förderkredit (Bewilligung und Darlehensvertrag), Kita-Platz (§ 24 SGB VIII als eigener Anspruch)
– Streitstand: Kritik an der Zweistufentheorie und Gegenansicht
– Lösung, Klausurtipp, Prüfschema, Merksatz

Normen: § 40 Abs. 1 S. 1 VwGO; § 8 Abs. 2, 4 GO NRW; Art. 28 Abs. 2 S. 1, Art. 3 Abs. 1 GG; § 24 SGB VIII; § 13 GVG; § 54 S. 1 VwVfG

In deinem Land ggf. andere Nummer – Zulassung zu öffentlichen Einrichtungen (am amtlichen Wortlaut geprüft am 4.10.2026): Nordrhein-Westfalen § 8 Abs. 2, 4 GO NRW; Niedersachsen § 30 Abs. 1, 3 NKomVG; Sachsen § 10 Abs. 2, 5 SächsGemO; Brandenburg § 12 Abs. 1 BbgKVerf. Bayern: Art. 21 Abs. 1 S. 1 BayGO (Nummer nach BVerwG 8 C 35.20, Rn. 13; amtlicher Wortlaut nicht abrufbar). In den übrigen Ländern bitte die eigene Gemeindeordnung nachschlagen.

Rechtsprechung:
– BVerwG, Urt. v. 20.1.2022 – 8 C 35.20, Rn. 14 (Zulassungsanspruch im Rahmen von Widmung und Kapazität; Verschaffungsanspruch durch Einwirken auf den privaten Betreiber)
– BVerwG, Beschl. v. 2.5.2007 – 6 B 10.07, Rn. 15 (Zweistufentheorie nur bei Mehrphasigkeit, etwa Subvention)
– BVerwG, Urt. v. 27.5.2009 – 8 C 10.08, Rn. 29, 32 f. (formelle Privatisierung; Einwirkungsrechte vorbehalten)
– OVG Niedersachsen, Beschl. v. 24.10.2007 – 10 OB 231/07, Rn. 7 f. (kein Verwaltungsrechtsweg gegen die Betreiber-GmbH)
– VG Gelsenkirchen, Beschl. v. 14.6.2024 – 15 L 888/24, Rn. 18–21, 38–40 (Ob und Wie; Einwirkungsanspruch gegen die Stadt)
– OVG Niedersachsen, Beschl. v. 15.12.2021 – 10 ME 170/21, Leitsatz 1 (Kita: Anspruch aus § 24 SGB VIII und Betreuungsvertrag)

Hinweise: Die Kritik an der Zweistufentheorie ist Lehrmeinung. Das Wie ist nur privatrechtlich, wenn die Gemeinde die Nutzung so ausgestaltet; bei einer Benutzungssatzung bleibt es öffentlich-rechtlich. Die Abgrenzung von öffentlichem und privatem Recht zeigt die Folge „Abgrenzungstheorien: Öffentliches oder privates Recht?“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Verwaltungsrecht #Jura #Zweistufentheorie
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"§\n(\d+)", r"§ \1\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei|vier)([,:])( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV."}[m.group(1)] + m.group(3), srt)
srt, n = re.subn(r"Sozialgesetzbuch(\s)acht", r"Sozialgesetzbuch\1VIII", srt)
assert n == 1
srt = srt.replace("\nLammers: ", "\nFrau Lammers: ").replace("\nScheffler: ", "\nHerr Scheffler: ")
assert not re.search(r"§\n|Abs\.\n|Art\.\n(?=\S)", srt), "Untertitel prüfen"
assert "hundert" not in srt and "Paragraf" not in srt and "Römisch" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
