"""Nachbearbeitung der Upload-Texte für Folge 103 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen zu Sätzen ohne
Aktenzeichen und Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_103.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Die alte Rechnung des Tischlers"),
       (T("drei"), "Drei Stufen: entstanden, untergegangen, durchsetzbar"),
       (T("i"), "Rechtshindernde Einwendungen"), (T("ii"), "Rechtsvernichtende Einwendungen"),
       (T("iii"), "Rechtshemmende Einreden: Verjährung, § 214 Abs. 1 BGB"), (T("frist"), "Die Frist: §§ 195, 199 BGB"),
       (T("aufsch"), "Aufschiebende Einreden: §§ 320, 273 BGB"), (T("amt"), "Wirkung im Prozess"),
       (T("tot"), "§ 214 Abs. 2 BGB: Gezahlt ist gezahlt"), (T("erg"), "Ergebnis"), (T("tipp"), "Klausurtipp: § 215 BGB"),
       (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Einwendung und Einrede unterscheiden: rechtshindernd, rechtsvernichtend, rechtshemmend. Warum § 214 BGB den Anspruch nicht erlöschen lässt – im Dreischritt erklärt.

Der Fall: Der Tischler Herr Grünwald restauriert im Herbst 2022 den alten Esstisch von Tilda. Im Oktober 2022 holt sie ihn zufrieden ab und bekommt die Rechnung über 1.400 Euro – die landet in einer Schublade. Fast vier Jahre später, im September 2026, verlangt Herr Grünwald sein Geld. Muss Tilda noch zahlen? Und bekommt sie das Geld zurück, wenn sie zahlt und erst danach von der Verjährung erfährt?

Inhalt:
– Drei Stufen: Anspruch entstanden – untergegangen – durchsetzbar
– Rechtshindernde Einwendungen: §§ 105, 125, 134, 138 BGB (Geschäftsunfähigkeit, Formmangel, Schwarzarbeit, Wucher)
– Rechtsvernichtende Einwendungen: Erfüllung (§ 362 BGB), Aufrechnung (§ 389 BGB), Anfechtung (§ 142 Abs. 1 BGB)
– Rechtshemmende Einreden: Verjährung als dauernde Einrede (§ 214 Abs. 1 BGB im Wortlaut), Frist nach §§ 195, 199 Abs. 1 BGB; aufschiebende Einreden §§ 320, 273 BGB, Zug um Zug (§§ 274, 322 BGB)
– Wirkung im Prozess: Einwendungen von Amts wegen, Einreden nur, wenn der Schuldner sich darauf beruft
– § 214 Abs. 2 BGB im Wortlaut: Gezahltes bleibt gezahlt, auch in Unkenntnis der Verjährung; § 813 Abs. 1 Satz 2 BGB
– Ergebnis, Klausurtipp (Aufrechnung mit verjährter Forderung, § 215 BGB), Klausurschema, Merksatz

Normen: §§ 214, 215, 273, 320, 362, 389, 813 BGB; §§ 105, 125, 134, 138, 142, 195, 199, 274, 322, 631, 641 BGB

Rechtsprechung:
– BGH, Beschl. v. 1.2.2023 – XII ZB 104/22, Rn. 16 (Verjährung nur auf Einrede, Erlöschenstatbestand von Amts wegen; Entstehung im Sinne von § 199 BGB setzt grundsätzlich Fälligkeit voraus)
– BGH, Urt. v. 19.1.2018 – V ZR 273/16, Rn. 27 (rechtsvernichtender Einwand auch zu berücksichtigen, wenn der Kläger selbst die Tatsachen vorträgt)
– BGH, Urt. v. 5.7.2016 – XI ZR 254/15, Rn. 27 (§§ 320, 322 BGB nur auf Einrede)
– BGH, Urt. v. 1.8.2013 – VII ZR 6/13, Rn. 13 (Werkvertrag über Schwarzarbeit nichtig, § 134 BGB)

Hinweise: Die Einteilung in rechtshindernde, rechtsvernichtende und rechtshemmende Gegenrechte und das Schema sind Lehre und Klausurkonvention. Die Fristberechnung ist bewusst nur angedeutet; Einzelheiten in Folge 109 (Regelverjährung).

Mehr dazu: Folge 6 (Anspruchsaufbau: Wer will was von wem woraus?), Folge 95 (Abnahme im Werkvertrag).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Einrede #Verjährung #Jura
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
