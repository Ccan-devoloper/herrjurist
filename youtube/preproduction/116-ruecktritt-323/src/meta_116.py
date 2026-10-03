"""Nachbearbeitung der Upload-Texte für Folge 116 (Kopie von meta_112.py) (nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_116.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Der Online-Shop liefert nicht"),
       (T("plan"), "Rücktritt: drei Ebenen"),
       (T("w1"), "I. Rücktrittsrecht, § 323 Abs. 1 BGB"), (T("g1"), "I. 1. Gegenseitiger Vertrag"),
       (T("f1"), "I. 2. Fällige, durchsetzbare Leistung nicht erbracht"),
       (T("fr1"), "I. 3. Angemessene Frist – und die zu kurze Frist"),
       (T("e1"), "I. 4. Entbehrlichkeit, § 323 Abs. 2 BGB"), (T("a1"), "I. 5. Kein Ausschluss, § 323 Abs. 5, 6 BGB"),
       (T("vm1"), "Klausurfehler: kein Vertretenmüssen"), (T("r1"), "II. Rücktrittserklärung, § 349 BGB"),
       (T("rf1"), "III. Rechtsfolge, § 346 Abs. 1 BGB"), (T("ab1"), "Abgrenzung (§ 326 Abs. 5, § 437 Nr. 2 BGB) und Ergebnis"),
       (T("tipp"), "Klausurtipp: Frist in drei Schritten"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Rücktritt § 323 BGB im Schema: Fälligkeit, Fristsetzung, Entbehrlichkeit, Ausschluss, Erklärung (§ 349 BGB). Am Online-Shop, der die Konsole nicht liefert.

Der Fall: Leni bestellt am 1. Juli 2026 privat in einem Online-Shop eine Spielkonsole für 499 Euro und zahlt per Vorkasse. Versprochen ist die Lieferung bis zum 8. Juli – es kommt nichts. Am 15. Juli setzt sie per E-Mail eine Frist „bis morgen“. Der Shop-Inhaber bittet um Geduld, sein Lieferant habe ihn im Stich gelassen. Am 30. Juli erklärt Leni den Rücktritt. Kann sie wirksam zurücktreten – und war die Frist nicht viel zu kurz?

Inhalt:
– I. Rücktrittsrecht: § 323 Abs. 1 BGB im Wortlaut
– 1. gegenseitiger Vertrag (§ 433 BGB)
– 2. fällige, durchsetzbare Leistung nicht erbracht (§ 271, beim Verbrauchsgüterkauf § 475 Abs. 1 BGB; keine Einrede, § 320 BGB)
– 3. angemessene Frist zur Leistung, erfolglos abgelaufen – eine zu kurze Frist setzt eine angemessene in Gang
– 4. Entbehrlichkeit nach § 323 Abs. 2 BGB: ernsthafte und endgültige Verweigerung, Termingeschäft, besondere Umstände (nur bei nicht vertragsgemäßer Leistung)
– 5. kein Ausschluss nach § 323 Abs. 5, 6 BGB
– Typischer Klausurfehler: Vertretenmüssen gehört nicht zum Rücktritt, sondern zum Schadensersatz statt der Leistung (§§ 280, 281 BGB); auch Verzug ist keine Voraussetzung
– II. Rücktrittserklärung: § 349 BGB im Wortlaut
– III. Rechtsfolge: Rückgewähr nach § 346 Abs. 1 BGB
– Abgrenzung: Unmöglichkeit (§ 326 Abs. 5 BGB, ohne Fristsetzung) und Mangel (§ 437 Nr. 2 BGB, Frist zur Nacherfüllung)
– Ergebnis, Klausurtipp, Klausurschema, Merksatz

Normen: §§ 323, 326 V, 346 I, 349 BGB; §§ 271, 275, 280, 281, 320, 433, 437, 475 I BGB

Rechtsprechung und Materialien:
– BGH, Urt. v. 14.10.2020 – VIII ZR 318/19, Rn. 28 (unangemessen kurze Frist setzt eine angemessene Frist in Lauf)
– BGH, Urt. v. 26.8.2020 – VIII ZR 351/19, Rn. 28, 43 (zu kurze Frist setzt angemessene in Gang, es sei denn, es kommt dem Gläubiger gerade auf die Kürze an)
– BGH, Urt. v. 14.2.2020 – V ZR 11/18, Rn. 38 (schon das Bestehen der Einrede aus § 320 BGB schließt den Rücktritt aus)
– BGH, Urt. v. 1.7.2015 – VIII ZR 226/14, Rn. 33 (strenge Anforderungen an die ernsthafte und endgültige Erfüllungsverweigerung)
– BT-Drucks. 14/6040, S. 93, 184 (Rücktritt unabhängig vom Vertretenmüssen und vom Verzug)
– BT-Drucks. 17/12637, S. 58 f. (geltende Fassung von § 323 Abs. 2 Nr. 2 und 3)

Hinweise: Beim Online-Kauf kommt daneben ein Widerrufsrecht in Betracht (§§ 312g Abs. 1, 355 BGB); das Video behandelt nur den Rücktritt. Schadensersatz kann neben dem Rücktritt verlangt werden (§ 325 BGB), setzt aber Vertretenmüssen voraus. Bei Mängeln beim Verbrauchsgüterkauf gilt für die Fristsetzung zusätzlich § 475d BGB (siehe Folge 063). Das System der §§ 280 ff. BGB erklärt Folge 046, Einwendung und Einrede Folge 103, den Schuldnerverzug Folge 112.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Rücktritt323BGB #Zivilrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
