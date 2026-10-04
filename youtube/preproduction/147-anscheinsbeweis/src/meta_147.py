"""Nachbearbeitung der Upload-Texte für Folge 147 (nach meta_124.py; tools/youtube_metadaten.py unverändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Zahl- und Paragrafenschreibweise in den Untertiteln.
Aufruf: python3 meta_147.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Auffahrunfall – „grundlose Vollbremsung“?"),
       (T("klage"), "Klage und Fragen"),
       (T("drei"), "Drei Werkzeuge, ein Raster"),
       (T("grund"), "Ausgangspunkt: die Grundregel der Beweislast"),
       (T("a1"), "1. Anscheinsbeweis: Grundlage"),
       (T("a5"), "1. Anscheinsbeweis: Was ändert sich?"),
       (T("a8"), "1. Anscheinsbeweis: erschüttern"),
       (T("v1"), "2. Gesetzliche Vermutung: § 292 ZPO"),
       (T("v3"), "2. Gesetzliche Vermutung: Beispiel § 477 BGB"),
       (T("v7"), "2. Gesetzliche Vermutung: Beweis des Gegenteils"),
       (T("u1"), "3. Beweislastumkehr: § 280 Abs. 1 S. 2 BGB"),
       (T("u4"), "3. Beweislastumkehr: Was ändert sich?"),
       (T("l1"), "Der Fall: Anschein gegen den Auffahrenden"),
       (T("l5"), "Der Fall: Behauptung und Spurwechsel"),
       (T("l8"), "Der Fall: Abstand halten, § 4 StVO, § 17 StVG"),
       (T("l11"), "Der Fall: Ergebnis"),
       (T("tab"), "Merktabelle: drei Werkzeuge"),
       (T("tipp"), "Klausurtipp"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Anscheinsbeweis, gesetzliche Vermutung nach § 292 ZPO und Beweislastumkehr (z. B. §§ 280 I 2, 477 BGB): die Unterschiede und wie man den Anschein erschüttert.

Der Fall: Frau Kretschmer bremst im Stadtverkehr, Herr Hertel fährt ihr hinten auf. Niemand ist verletzt, aber die Stoßstange ist eingedrückt (2.400 €). Herr Hertel bestreitet sein Verschulden: Sie habe ohne jeden Grund eine Vollbremsung gemacht. Zeugen gibt es nicht. Muss sie ihm beweisen, dass er zu dicht aufgefahren ist – und reicht seine Behauptung, um sich zu wehren?

Inhalt:
– Drei Werkzeuge, ein Raster: Worauf beruht es? Was ändert sich? Wie wehrt sich der Gegner?
– Anscheinsbeweis: Erfahrungssatz bei typischem Geschehensablauf, Teil der freien Beweiswürdigung (§ 286 ZPO); die Beweislast bleibt; erschüttern durch voll bewiesene Tatsachen, die einen atypischen Verlauf ernsthaft möglich machen
– Gesetzliche Vermutung: § 292 S. 1 ZPO im Wortlaut; Vermutungsbasis; Beispiel § 477 Abs. 1 S. 1 BGB (Jahresfrist für Verträge seit 1.1.2022); Beweis des Gegenteils
– Beweislastumkehr: § 280 Abs. 1 S. 2 BGB im Wortlaut; der Schuldner muss beweisen, dass er nicht zu vertreten hat
– Der Fall: Anschein gegen den Auffahrenden, bloße Behauptung erschüttert nicht, Gegenfall Spurwechsel, § 4 Abs. 1 StVO, Abwägung nach § 17 StVG
– Merktabelle, Klausurtipp (das passende Verb, Formulierung im Urteil), Merksatz
– Grundregel der Beweislast und non liquet: Video „Beweislast ZPO“; § 477 BGB im Detail: Video „Verbrauchsgüterkauf“

Normen: §§ 286, 292 ZPO; §§ 280 Abs. 1 S. 2, 477 Abs. 1 BGB; Art. 229 § 58 EGBGB; § 4 Abs. 1 StVO; § 17 StVG

Rechtsprechung:
– BGH, Urt. v. 13.12.2016 – VI ZR 32/16, Rn. 8, 10–14 (Anscheinsbeweis gegen den Auffahrenden; Erschütterung; unbewiesener Spurwechsel; Alleinhaftung gebilligt)
– BGH, Urt. v. 13.12.2011 – VI ZR 177/10 (BGHZ 192, 84), Rn. 7, 11 (feststehender Spurwechsel: regelmäßig kein Anscheinsbeweis)
– BGH, Urt. v. 3.12.2024 – VI ZR 18/24, Rn. 16, 19 (scharfes Bremsen des Vorausfahrenden stets einkalkulieren; Voraussetzungen des Anscheinsbeweises)
– BGH, Urt. v. 26.1.2016 – XI ZR 91/14, Rn. 24, 46 (Anscheinsbeweis: weder Beweisvermutung noch Beweislastumkehr; Erschütterung)
– BGH, Urt. v. 11.12.2018 – KZR 26/17, Rn. 49 f. (Anscheinsbeweis als typisierte Form des Indizienbeweises)
– BGH, Urt. v. 6.5.2026 – VIII ZR 257/23, Rn. 25, 52, 55 (Vermutung des § 477 BGB a. F., Beweis des Gegenteils, § 292 ZPO)
– BGH, Urt. v. 13.11.2018 – EnZR 39/17, Rn. 64 (§ 280 Abs. 1 S. 2 BGB als Beweislastregel)

Hinweise: Die Formulierung „Für ein unfallursächliches Verschulden des Beklagten spricht ein nicht erschütterter Anscheinsbeweis.“ ist an BGH VI ZR 32/16, Rn. 13 angelehnt, keine Pflichtformel. Die Anspruchsgrundlagen (§§ 7, 18 StVG, § 823 BGB) werden nicht geprüft. Ob eine bewiesene grundlose starke Bremsung den Anschein erschüttert oder nur in der Abwägung zählt, lässt das Video offen. VIII ZR 257/23 betrifft § 477 BGB in der bis 2021 geltenden Fassung (sechs Monate).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Anscheinsbeweis #2Examen #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
for a, b in [("zweitausendvierhundert Euro", "2.400 Euro"), ("seit dem ersten Januar\n", "seit dem 1. Januar\n"),
             ("gegen S.\n2 bei", "gegen Satz 2\nbei")]:
    assert a in srt, a
    srt = srt.replace(a, b)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
