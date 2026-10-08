"""Nachbearbeitung der Upload-Texte für Folge 282 (nach meta_270.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung, Hinweisen und Lizenzzeile;
Untertitel-Korrekturen (Beträge als Ziffern, Sprechernamen, Römisch → I.–IV.).
Aufruf: python3 meta_282.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: verklagt ohne Mahnung – zahlen oder anerkennen?"),
       (T("zahl"), "Zahlen nach Zustellung: Erledigung, § 91a ZPO"),
       (T("w307"), "§ 307 ZPO: das Anerkenntnisurteil"),
       (T("w93"), "§ 93 ZPO: Kosten beim Kläger"),
       (T("ver"), "1. Keine Veranlassung zur Klage (kein Verzug)"),
       (T("sof"), "2. Sofort: schriftliches Vorverfahren, Klageerwiderungsfrist"),
       (T("ten"), "Muster: Tenor des Anerkenntnisurteils, § 708 Nr. 1 ZPO"),
       (T("teil"), "Teilanerkenntnis: Kosten im Schlussurteil"),
       (T("fehl"), "Zwei typische Fehler"),
       (T("tipp"), "Klausurtipp Anwaltsklausur"),
       (T("sch"), "Prüfschema sofortiges Anerkenntnis"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Sofortiges Anerkenntnis nach § 93 ZPO: Wann gab der Beklagte keine Veranlassung zur Klage, wann ist das Anerkenntnis im schriftlichen Vorverfahren „sofort“ – und wie tenoriert man Anerkenntnis- und Teil-Anerkenntnisurteil (§§ 307, 708 Nr. 1 ZPO)?

Der Fall: Die Gartenbau Fink GmbH hat bei Frau Mehlhorn die Hecke geschnitten und ein Beet angelegt, Rechnung 1.280 Euro. Zwei Wochen später kommt – ohne Mahnung, ohne Anruf – die Klage vom Amtsgericht. Frau Mehlhorn will einfach zahlen und geht zu Rechtsanwalt Rosenbaum. Kann sie den Prozess verlieren, ohne die Kosten zu tragen?

Inhalt:
– Zahlen oder anerkennen? Zahlung nach Zustellung: Erledigung, Kosten nach § 91a ZPO nach billigem Ermessen
– § 307 ZPO im Wortlaut: Anerkenntnisurteil, ohne mündliche Verhandlung; Grundsatz § 91 ZPO
– § 93 ZPO im Wortlaut: keine Veranlassung zur Klage und sofortiges Anerkenntnis
– Veranlassung: Verhalten vor dem Prozess (BGH, Beschl. v. 30.5.2006 – VI ZB 64/05, Rn. 10; Beschl. v. 22.10.2015 – V ZB 93/13, Rn. 19); kein Verzug (§ 286 BGB)
– „Sofort“ im schriftlichen Vorverfahren: innerhalb der Klageerwiderungsfrist, Verteidigungsanzeige ohne Abweisungsantrag schadet nicht (BGH VI ZB 64/05, Rn. 22; BGH, Beschl. v. 21.3.2019 – IX ZB 54/18)
– Muster: Tenor des Anerkenntnisurteils mit Kosten beim Kläger, vorläufig vollstreckbar ohne Sicherheitsleistung (§ 708 Nr. 1 ZPO)
– Teilanerkenntnis: Teil-Anerkenntnisurteil, Kostenentscheidung im Schlussurteil
– Zwei typische Fehler, Klausurtipp für die Anwaltsklausur, Prüfschema, Merksatz

Normen: §§ 91, 91a, 93, 276, 301, 307, 313b, 708 Nr. 1, 711 ZPO; § 286 BGB.

Hinweise: Frau Mehlhorn, Herr Rosenbaum, Herr Fink und die Gartenbau Fink GmbH sind erfunden. Weiterführend: unsere Folge zur Kostenquote nach §§ 91, 92 ZPO.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound „Residential mailbox lid“ (SoundsLikeYukon), CC0.

#Referendariat #2Examen #ZPO
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
ERSATZ = [("tausendzweihundertachtzig Euro", "1.280 Euro"), ("Dreihundert Euro", "300 Euro"),
          ("neunhundertachtzig Euro", "980 Euro"), ("dreißig Tage", "30 Tage"),
          ("Nummern vier bis elf", "Nummern 4 bis 11"),
          ("Römisch eins:", "I."), ("Römisch zwei:", "II."), ("Römisch drei:", "III."), ("Römisch vier:", "IV.")]
for alt, neu in ERSATZ:
    muster = r"\s+".join(re.escape(w) for w in alt.split())
    assert re.search(muster, srt), alt
    srt = re.sub(muster, lambda m: neu if "\n" not in m.group(0) else neu.replace(" ", "\n", 1), srt)
srt = re.sub(r"\btausendzweihundertachtzig\b", "1.280", srt)   # Zahlwort am Blockende (Euro im nächsten Block)
srt = re.sub(r"(?m)^Fink:", "Herr Fink:", srt)
srt = re.sub(r"(?m)^Mehlhorn:", "Frau Mehlhorn:", srt)
srt = re.sub(r"(?m)^Rosenbaum:", "Herr Rosenbaum:", srt)
assert not re.search(r"tausend|Römisch|hundert|dreißig", srt), re.findall(r".*(?:tausend|Römisch|hundert|dreißig).*", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + ["§ 708 ZPO", "schriftliches Vorverfahren"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
