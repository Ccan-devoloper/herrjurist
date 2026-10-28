"""Nachbearbeitung der Upload-Texte für Folge 212 (Kopie von meta_170.py) (nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung, Hinweisen und
Lizenzzeile; Schreibform der Untertitel („Abs. 1 bis drei“ → „bis 3“), Paragrafen-Umbruch.
Aufruf: python3 meta_212.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Das Privatkonzert fällt aus"),
       (T("syn"), "Synallagma und Gegenleistungsgefahr"),
       (T("plan"), "Aufbau: Anspruch auf das Honorar"),
       (T("e1"), "I. entstanden, II. § 326 Abs. 1 BGB im Wortlaut"),
       (T("u1"), "Unmöglich? Absolutes Fixgeschäft (BGH VII ZR 144/22)"),
       (T("w2"), "III. Ausnahme: § 326 Abs. 2 Satz 1 BGB"),
       (T("gf"), "Gegenfall: Der Gastgeber sagt ab"),
       (T("w22"), "Anrechnung der Ersparnis: § 326 Abs. 2 Satz 2 BGB"),
       (T("k648"), "Achtung Werkvertrag: Kündigung nach § 648 BGB"),
       (T("w4"), "IV. Die Anzahlung: § 326 Abs. 4, 5 und 3 BGB"),
       (T("tipp"), "Klausurtipp: Reihenfolge"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""§ 326 BGB: Wann entfällt die Gegenleistung nach § 326 I und wann bleibt sie ausnahmsweise nach § 326 II BGB bestehen? Am ausgefallenen Privatkonzert erklärt.

Der Fall: Friedhelm feiert seinen 70. Geburtstag und bucht für den Samstagabend den Pianisten Theodor – ein Privatkonzert für 2.000 Euro, 500 Euro zahlt er gleich an. Am Samstagmittag sagt Theodor ab: hohes Fieber. Die Feier lässt sich nicht verschieben. Muss Friedhelm trotzdem zahlen – und bekommt er die Anzahlung zurück? Im Gegenfall sagt Friedhelm selbst ab, weil er spontan verreist.

Inhalt:
– Synallagma: Was wird aus der Gegenleistung, wenn die Leistung nach § 275 BGB entfällt? Gegenleistungsgefahr (Preisgefahr)
– Aufbau: Anspruch entstanden – untergegangen (§ 326 Abs. 1) – ausnahmsweise erhalten (§ 326 Abs. 2) – Rückforderung (§ 326 Abs. 4)
– § 326 Abs. 1 Satz 1 BGB im Wortlaut; persönliche Leistung, Nachholbarkeit, absolutes Fixgeschäft
– § 326 Abs. 2 Satz 1 BGB im Wortlaut: Gläubiger allein oder weit überwiegend verantwortlich oder Annahmeverzug
– Gegenfall: Absage durch den Gastgeber; Anrechnung der Ersparnis nach § 326 Abs. 2 Satz 2 BGB (2.000 € – 100 € = 1.900 €)
– Achtung beim Werkvertrag: Absage als Kündigung nach § 648 BGB
– § 326 Abs. 4 BGB im Wortlaut: Rückforderung der Anzahlung nach §§ 346–348; Rücktritt nach § 326 Abs. 5; § 326 Abs. 3
– Klausurtipp, Klausurschema, Merksatz

Normen: § 326 Abs. 1–5 BGB; §§ 275, 285, 293, 294, 346, 648 BGB

Rechtsprechung: BGH, Urteil vom 27.4.2023 – VII ZR 144/22 (Hochzeitsfotografin: Verlegung der Hochzeit macht die Leistung nicht unmöglich, Leitsatz 1, Rn. 14; Absage als Kündigung nach § 648 BGB, Vergütung abzüglich ersparter Aufwendungen, Rn. 33, 37, 39). BGH, Urteil vom 28.8.2012 – X ZR 128/11, Rn. 34 (Verfehlen einer wesentlichen Leistungszeit wie beim absoluten Fixgeschäft).

Materialien: BT-Drucks. 14/6040, S. 188 f. (Gegenleistung entfällt kraft Gesetzes; Rückabwicklung nach Rücktrittsrecht)

Hinweise: Ob ein Konzertvertrag Werk- oder Dienstvertrag ist, hängt von der Vereinbarung ab; beim Dienstvertrag regelt § 615 BGB den Annahmeverzug mit gleichlaufender Anrechnung. Die Unmöglichkeit selbst (§ 275 BGB) und den Ersatz nach § 285 BGB erklärt Folge 170.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 6. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#326BGB #Gegenleistungsgefahr #Zivilrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace("Abs. 1 bis drei", "Abs. 1 bis 3")
assert "bis drei" not in srt and not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
