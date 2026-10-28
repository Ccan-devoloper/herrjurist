"""Nachbearbeitung der Upload-Texte für Folge 149 (nach meta_146.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Normzitate).
Aufruf: python3 meta_149.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Rempler auf dem Supermarktparkplatz, Sachverhalt"),
       (T("aufbau"), "Aufbau: § 7, § 18, § 17 StVG"),
       (T("p7"), "§ 7 Abs. 1 StVG: Gefährdungshaftung des Halters"),
       (T("halter"), "Halter, Betrieb, Rechtsgutverletzung, Kausalität"),
       (T("p72"), "§ 7 Abs. 2 StVG: höhere Gewalt"),
       (T("p18"), "§ 18 StVG: Haftung des Fahrers"),
       (T("p17"), "§ 17 StVG: Verteilung zwischen den Haltern"),
       (T("sockel"), "Abwägung: Betriebsgefahr, Verschulden, Idealfahrer"),
       (T("park"), "Parkplatz: StVO, kein „rechts vor links“"),
       (T("ansch"), "Anscheinsbeweis gegen den Rückwärtsfahrer"),
       (T("loes"), "Lösung und Gegenfall"),
       (T("tipp"), "Klausurtipp: Reihenfolge und § 115 VVG"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Halterhaftung nach § 7 StVG, Fahrerhaftung nach § 18 und Haftungsverteilung nach § 17 StVG: Wer zahlt, wenn sich beim Ausparken zwei Autos berühren?

Der Fall: Auf dem Parkplatz eines Supermarkts setzen Heidrun und Volkmar gleichzeitig rückwärts aus gegenüberliegenden Parklücken. Die Hecks berühren sich, beide Stoßstangen haben Kratzer, verletzt ist niemand. Keiner will schuld sein; unstreitig ist nur, dass beide Autos noch rollten. Heidrun verlangt 1.600 € Reparaturkosten.

Inhalt:
– § 7 Abs. 1 StVG (im Wortlaut): Gefährdungshaftung ohne Verschulden; Halter, „bei dem Betrieb“ (weite Auslegung), Rechtsgutverletzung, haftungsbegründende Kausalität
– § 7 Abs. 2 StVG (im Wortlaut): Ausschluss nur bei höherer Gewalt
– § 18 Abs. 1 StVG (im Wortlaut): Haftung des Fahrers für vermutetes Verschulden, Entlastung nach Satz 2
– § 17 Abs. 1 und 2 StVG (im Wortlaut): Abwägung der Verursachungsbeiträge; Betriebsgefahr als Sockel; nur unstreitige oder bewiesene Umstände; § 17 Abs. 3 (Idealfahrer); § 9 StVG und § 254 BGB
– Parkplatz: StVO gilt, „rechts vor links“ ohne Straßencharakter nicht; § 1 Abs. 2 StVO (im Wortlaut); Rückwärtsfahrer muss sofort anhalten können
– Anscheinsbeweis gegen den Rückwärtsfahrer nur, wenn er im Kollisionszeitpunkt noch rollte
– Lösung des Falls und Gegenfall, Klausurtipp (Prüfungsreihenfolge, Direktanspruch § 115 VVG), Prüfschema, Merksatz

Normen: §§ 7, 9, 17, 18 StVG; § 254 BGB; § 1 Abs. 2 StVO; § 115 Abs. 1 VVG

Rechtsprechung:
– BGH, Urt. v. 15.12.2015 – VI ZR 6/15, Rn. 9, 11, 15 f. (Parkplatz: Anscheinsbeweis gegen den Rückwärtsfahrer nur, wenn er noch fuhr)
– BGH, Urt. v. 26.1.2016 – VI ZR 179/15, Rn. 10 f. (§ 9 Abs. 5 StVO mittelbar über § 1 StVO; sofort anhalten können)
– BGH, Urt. v. 11.10.2016 – VI ZR 66/16, Rn. 7, 9 f., 12 (Abwägung nach § 17 StVG; Betriebsgefahr zählt trotzdem)
– BGH, Urt. v. 22.11.2022 – VI ZR 344/21, Rn. 12, 15, 17 f. (kein „rechts vor links“ auf Parkplätzen ohne Straßencharakter)
– BGH, Urt. v. 24.3.2015 – VI ZR 265/14, Rn. 5 (Betrieb eines Kraftfahrzeugs, „Preis“ der erlaubten Gefahrenquelle)
– BGH, Urt. v. 11.6.2013 – VI ZR 150/12, Rn. 13, 17, 18 (Gefährdungshaftung; vermutetes Verschulden des Fahrers)
– BGH, Urt. v. 3.12.2024 – VI ZR 18/24, Rn. 15 (unabwendbares Ereignis, Idealfahrer)

Hinweise: Die Teilung je zur Hälfte ist das Ergebnis der Abwägung in diesem Fall, keine feste Quote für Parkplatzunfälle. Dass der Anschein hier gegen beide spricht, folgt aus den BGH-Grundsätzen, weil beide noch rollten. Nicht behandelt: Schadensumfang, Gegenansprüche, Haftungshöchstbeträge. Die Abgrenzung von Anscheinsbeweis, Vermutung und Beweislastumkehr zeigt die Folge zum Anscheinsbeweis, das Schema zu § 823 BGB die Folge zum Deliktsrecht.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Halterhaftung #Verkehrsunfall #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei|vier):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV."}[m.group(1)] + m.group(2), srt)
for a, b in [("tausendsechshundert Euro", "1.600 Euro"), ("achthundert Euro", "800 Euro")]:
    assert a in srt, a
    srt = srt.replace(a, b)
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "tausend" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
