"""Nachbearbeitung der Upload-Texte für Folge 122 (Kopie von meta_116.py) (nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Paragrafen-Umbruch in den Untertiteln; Aussprachehilfen/Großschreibung zurückgeführt.
Aufruf: python3 meta_122.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Sneaker getragen und zurückgeschickt"),
       (T("plan"), "Widerruf in drei Schritten"),
       (T("v1"), "I. 1. Verbrauchervertrag, § 310 Abs. 3 BGB"),
       (T("fa1"), "I. 2. Fernabsatzvertrag, § 312c Abs. 1 BGB"),
       (T("wr1"), "I. 3. Widerrufsrecht, § 312g Abs. 1 BGB"),
       (T("au1"), "Ausnahmen, § 312g Abs. 2 BGB (Maßanfertigung, verderblich, Hygiene)"),
       (T("e1"), "II. 1. Widerrufserklärung, § 355 Abs. 1 BGB"),
       (T("fr1"), "II. 2. Widerrufsfrist 14 Tage, § 356 BGB"),
       (T("rf1"), "III. 1. Rückgewähr, §§ 355 Abs. 3, 357 BGB"),
       (T("we1"), "III. 2. Wertersatz für getragene Ware, § 357a BGB"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp: Gebrauch erst beim Wertersatz"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Widerrufsrecht Fernabsatz (§§ 312c, 312g, 355, 356 BGB): Wann besteht es, wann beginnt die 14-Tage-Frist und welche Ausnahmen gelten beim Onlinekauf? Dazu: Wertersatz für getragene Ware (§ 357a BGB).

Der Fall: Ilka bestellt am 4. September 2026 privat im Onlineshop von Herrn Riemann Sneaker für 120 Euro. Sie erhält sie am 8. September, trägt sie einen ganzen Nachmittag draußen im Park und widerruft am 15. September per E-Mail. Herr Riemann: „Getragene Schuhe nehme ich nicht zurück.“ Mit den Spuren sind die Sneaker nur noch 80 Euro wert. Kann Ilka widerrufen – und muss sie für das Tragen zahlen?

Inhalt:
– Prüfungsschema: I. Widerrufsrecht, II. Ausübung, III. Rechtsfolgen
– Verbrauchervertrag (§ 310 Abs. 3 BGB) und Fernabsatzvertrag (§ 312c Abs. 1 BGB, Wortlaut)
– Widerrufsrecht § 312g Abs. 1 BGB und die Ausnahmen § 312g Abs. 2 Nr. 1 (nicht vorgefertigt, z. B. nach Maß), Nr. 2 (schnell verderblich) und Nr. 3 (versiegelte Hygieneware)
– Widerrufserklärung: eindeutig, ohne Begründung; kommentarlose Rücksendung reicht nicht; Widerrufsfunktion im Onlineshop (§ 356a BGB)
– Frist: 14 Tage ab Erhalt der Ware (§ 355 Abs. 2, § 356 Abs. 2 Nr. 1 Buchst. a BGB), nicht vor Belehrung (§ 356 Abs. 3), spätestens 12 Monate und 14 Tage (§ 356 Abs. 4 BGB)
– Rückgewähr (§§ 355 Abs. 3, 357 Abs. 1 BGB) und Wertersatz (§ 357a Abs. 1 BGB): anprobieren ja, tragen nein
– Ergebnis mit Aufrechnung, Klausurtipp, Klausurschema, Merksatz

Rechtsprechung und Materialien:
– EuGH, Urt. v. 27.3.2019 – C-681/17 (slewo), Rn. 34, 40, 41, 47: Hygieneausnahme eng auszulegen; Matratze ohne Schutzfolie fällt nicht darunter; Wertersatz statt Verlust des Widerrufsrechts
– Richtlinie 2011/83/EU, Erwägungsgrund 47: ein Kleidungsstück nur anprobieren, nicht jedoch tragen
– BT-Drs. 17/12637, S. 60 (kommentarlose Rücksendung genügt nicht) und S. 63 (Wertersatz, Prüfung wie in einem Geschäft)
– BGH, Urt. v. 12.10.2016 – VIII ZR 55/15, Rn. 20, 22 (Prüfung wie im Ladengeschäft; zur alten Fassung)

Hinweise: Der Fall ist erfunden. Ein BGH-Urteil speziell zu getragenen Schuhen gibt es nach unserer Recherche nicht; die Einordnung folgt dem Wortlaut von § 357a Abs. 1 BGB und Erwägungsgrund 47. Den Verbraucherbegriff (§§ 13, 14 BGB) erklärt Folge 106, die genaue Fristrechnung (§§ 187, 188 BGB) Folge 117, den Rücktritt beim Online-Kauf Folge 116.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Widerrufsrecht #Zivilrecht #Jura
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
