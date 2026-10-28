"""Nachbearbeitung der Upload-Texte für Folge 236 (nach meta_209.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen, Paragrafen).
Aufruf: python3 meta_236.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Das Heizgerät und der verrußte Keller"),
       (T("frage"), "Welche Anspruchsgrundlage? Sachverhalt"),
       (T("agl"), "§ 437 Nr. 3 BGB: Rechtsgrundverweisung"),
       (T("kf"), "Die Kontrollfrage: statt oder neben der Leistung"),
       (T("wege"), "Behebbar: §§ 280, 281 BGB; unbehebbar: § 283 BGB"),
       (T("t3"), "§ 311a Abs. 2 BGB, Mangelfolgeschaden, Verzögerungsschaden"),
       (T("vm"), "Vertretenmüssen des Händlers"),
       (T("ph"), "Anspruch gegen den Hersteller und Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Schadensersatz Kaufrecht (§§ 437 Nr. 3, 280 ff. BGB): Welche Anspruchsgrundlage trägt Mangelschaden, Mangelfolgeschaden und Verzögerungsschaden? Am brennenden Heizgerät.

Der Fall: Katharina kauft im Elektrogeschäft von Raimund ein Heizgerät für 600 €. Eine Woche später schmort ein Bauteil durch, es qualmt, ein Regal brennt an, die Wand ist verrußt – Kellerschaden 4.000 €, verletzt wird niemand. Der Fehler stammt vom Hersteller und war für Raimund nicht erkennbar. Katharina verlangt ein neues Gerät und 4.000 €.

Inhalt:
– § 437 Nr. 3 BGB im Wortlaut: Rechtsgrundverweisung ins allgemeine Schuldrecht
– Die Kontrollfrage: Würde eine Nacherfüllung den Schaden noch beseitigen? Statt oder neben der Leistung
– Mangel behebbar: §§ 280 Abs. 1, 3, 281 BGB, grundsätzlich erst nach erfolgloser Frist (Ausnahmen §§ 281 Abs. 2, 440 BGB; beim Verbrauchsgüterkauf § 475d BGB)
– Mangel nachträglich unbehebbar: § 283 BGB im Wortlaut
– Mangel schon bei Vertragsschluss unbehebbar: § 311a Abs. 2 BGB im Wortlaut
– Mangelfolgeschaden: § 280 Abs. 1 BGB ohne Frist; Verzögerungsschaden: §§ 280 Abs. 1, 2, 286 BGB
– Vertretenmüssen des Händlers: keine allgemeine Untersuchungspflicht, Hersteller kein Erfüllungsgehilfe
– Anspruch gegen den Hersteller (ProdHaftG, § 823 Abs. 1 BGB), Ergebnis, Klausurtipp, Klausurschema, Merksatz

Normen: §§ 275, 276, 278, 280 Abs. 1–3, 281, 283, 286, 311a Abs. 2, 433, 434, 437 Nr. 3, 439, 440, 475d, 823 Abs. 1 BGB; § 1 ProdHaftG

Rechtsprechung und Materialien:
– BGH, Urt. v. 19.6.2009 – V ZR 93/08, BGHZ 181, 317, Rn. 19 (Verkäufer muss die Kaufsache regelmäßig nicht untersuchen; kein Zurechnen des Lieferantenverschuldens)
– BGH, Urt. v. 15.7.2008 – VIII ZR 211/07, BGHZ 177, 224, Rn. 29 (Hersteller ist nicht Erfüllungsgehilfe des Händlers)
– BGH, Urt. v. 3.7.2013 – VIII ZR 169/12, BGHZ 197, 357, Rn. 26 f. (Abgrenzung: ob eine Nacherfüllung den Schaden beseitigen würde)
– vgl. BGH, Urt. v. 7.2.2019 – VII ZR 63/18, Rn. 17, 19 (Folgeschäden neben der Leistung, ohne Frist; Werkvertrag)
– BT-Drucks. 14/6040, S. 224 f. (Begründung zu § 437 Nr. 3 BGB)

Hinweise: Die Kontrollfrage „im letztmöglichen Zeitpunkt“ ist eine Formel der Lehre. Das System der §§ 280 ff. BGB erklärt das Video „Schadensersatz Schema“, die Abgrenzung statt/neben das Video „Die eine Kontrollfrage“, die Fristsetzung das Video „Schadensersatz statt der Leistung §§ 280, 281 BGB“, die Haftung des Herstellers das Video zur Produzentenhaftung. Beim Verbrauchsgüterkauf kann die Frist nach § 475d BGB entbehrlich sein. Personen frei erfunden.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#SchadensersatzKaufrecht #Kaufrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("sechshundert Euro", "600 Euro"), ("viertausend Euro", "4.000 Euro"), ("sechshundert\nEuro", "600\nEuro"),
             ("viertausend\nEuro", "4.000\nEuro"), ("Die viertausend", "Die 4.000")]:
    srt = srt.replace(a, b)
for a, b in [("§§ 280 Absätze eins\nund drei und zweihunderteinundachtzig,", "§§ 280 Abs. 1\nund 3 und 281,"),
             ("Voraussetzungen des §§ 280", "Voraussetzungen des § 280"), ("\nzweihundertsechsundachtzig.", "\n§ 286."),
             ("§§ 280 folgende.", "§§ 280 ff."), ("zweihundertdreiundachtzig, dreihundertelf\na oder zweihundertachtzig Abs. 1",
                                                   "283, 311a\noder 280 Abs. 1")]:
    assert a in srt, a
    srt = srt.replace(a, b)
for w, z in (("Erstens", "1."), ("Zweitens", "2."), ("Drittens", "3."), ("Viertens", "4.")):
    srt = re.sub(rf"(?m)^{w}: ", f"{z} ", srt)
    srt = re.sub(rf"(\. |\n){w}:", rf"\g<1>{z}", srt)
for a, b in [("Eins: K", "1. K"), ("Zwei: d", "2. d"), ("Drei: d", "3. d"), ("Vier: V", "4. V"), ("Fünf: S", "5. S")]:
    srt = srt.replace(a, b)
srt = srt.replace("4. der Mangelfolgeschaden", "4. Der Mangelfolgeschaden")
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
rest = [r for r in re.findall(r".{0,25}(?:tausend|hundert|Erstens|Zweitens|Drittens|Viertens|Paragraf).{0,15}", srt, re.I)
        if "genannten Paragrafen" not in r]
assert not rest, rest
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
