"""Nachbearbeitung der Upload-Texte für Folge 170 (Kopie von meta_116.py) (nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Materialien, Hinweisen und
Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_170.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Der Oldtimer brennt aus"),
       (T("plan"), "Unmöglichkeit: drei Schritte"),
       (T("w275"), "I. § 275 Abs. 1 BGB im Wortlaut"), (T("u1"), "Stückschuld, objektiv, nachträglich (§ 311a BGB)"),
       (T("rf1"), "Rechtsfolge: kraft Gesetzes – § 275 Abs. 2, 3 als Einrede"),
       (T("g1"), "II. Kaufpreis: § 326 Abs. 1 BGB"), (T("g3"), "Ausnahmen: § 326 Abs. 2, § 446 BGB"),
       (T("s1"), "III. 1. Schadensersatz: § 283 BGB"), (T("s2"), "Pflichtverletzung, Vertretenmüssen, Varianten A und B"),
       (T("c1"), "III. 2. Stellvertretendes Commodum: § 285 BGB"), (T("c2"), "Die Versicherungszahlung im Fall"),
       (T("loes"), "Lösung beider Varianten"), (T("tipp"), "Klausurtipp: Reihenfolge"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Unmöglichkeit § 275 BGB: Wann ist die Leistung ausgeschlossen und was folgt für Schadensersatz (§ 283) und Gegenleistung (§ 326 BGB)? Am ausgebrannten Oldtimer.

Der Fall: Waldemar verkauft Adelheid privat seinen Oldtimer für 20.000 Euro. Übergabe und Zahlung sollen am Samstag sein. In der Nacht davor brennt der Wagen in der Garage vollständig aus – in Variante A durch einen Blitzschlag, in Variante B, weil Waldemar mit offener Flamme hantiert hat. Der Wagen war 25.000 Euro wert, die Versicherung zahlt Waldemar 25.000 Euro. Muss Waldemar noch liefern, muss Adelheid noch zahlen – und was kann sie verlangen?

Inhalt:
– I. Anspruch auf den Wagen: § 275 Abs. 1 BGB im Wortlaut; Stückschuld, objektive und subjektive, nachträgliche Unmöglichkeit; anfängliche Unmöglichkeit: Vertrag wirksam (§ 311a Abs. 1 BGB)
– Rechtsfolge kraft Gesetzes; § 275 Abs. 2 und 3 BGB als Einrede
– II. Kaufpreis: § 326 Abs. 1 Satz 1 BGB im Wortlaut; Ausnahmen § 326 Abs. 2 BGB; Gefahrübergang erst mit der Übergabe (§ 446 BGB); Rücktritt nach § 326 Abs. 5 BGB
– III. 1. Schadensersatz statt der Leistung: §§ 280 Abs. 1, 3, 283 BGB, § 283 Satz 1 im Wortlaut; vermutetes Vertretenmüssen; Variante B: 5.000 Euro Wertdifferenz, Variante A: kein Schadensersatz
– III. 2. Stellvertretendes Commodum: § 285 Abs. 1 BGB im Wortlaut; die Versicherungszahlung als Ersatz; Gegenleistung nach § 326 Abs. 3 BGB; Anrechnung nach § 285 Abs. 2 BGB
– Lösung beider Varianten, Klausurtipp, Klausurschema, Merksatz

Normen: §§ 275, 283, 285, 326 BGB; §§ 276, 280, 311a, 433, 446 BGB

Materialien: BT-Drucks. 14/6040, S. 129 (§ 275 Abs. 1 kraft Gesetzes, Abs. 2 als Einrede), S. 142 (§ 283 und § 280 Abs. 1), S. 144 (§ 285: z. B. Anspruch auf eine Versicherungsleistung)

Hinweise: Hätte Adelheid schon gezahlt, könnte sie den Kaufpreis nach § 326 Abs. 4 BGB zurückfordern. Wäre Waldemar schon im Verzug gewesen, hätte er nach § 287 Satz 2 BGB grundsätzlich auch für Zufall gehaftet (siehe Folge 112). Das System der §§ 280 ff. BGB erklärt Folge 046, den Rücktritt Folge 116, Beweislast und Vermutungen die Folgen 141 und 147.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Unmöglichkeit275BGB #Zivilrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace("nach § 311\n\n", "nach § 311a\n\n").replace("\na trotzdem wirksam.", "\ntrotzdem wirksam.")
srt = srt.replace("Abs. 1 bis drei", "Abs. 1 bis 3").replace("des §§ 280", "des § 280")   # Zahlwort/„Paragrafen“ der Schreibform
assert "§ 311\n" not in srt and "bis drei" not in srt and "§§ 280" not in srt
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
