"""Nachbearbeitung der Upload-Texte für Folge 206 (nach meta_202.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen).
Aufruf: python3 meta_206.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Kuno verkauft das Motorrad von Enno"),
       (T("frage"), "Haftet Kuno persönlich? Sachverhalt"),
       (T("vor"), "Ausgangslage: Vertreter ohne Vertretungsmacht"),
       (T("p177"), "Schwebende Unwirksamkeit, § 177 Abs. 1 BGB"),
       (T("auff"), "Aufforderung und Zwei-Wochen-Frist, § 177 Abs. 2 BGB"),
       (T("p178"), "Widerruf des anderen Teils, § 178 BGB"),
       (T("jetzt"), "Haftung nach § 179 Abs. 1 BGB: Erfüllung oder Schadensersatz"),
       (T("p1792"), "§ 179 Abs. 2 BGB: nur Vertrauensschaden"),
       (T("p1793"), "§ 179 Abs. 3 BGB: Ausschluss der Haftung"),
       (T("loes"), "Lösung: Kuno zahlt 800 €"),
       (T("p180"), "Einseitige Rechtsgeschäfte, § 180 BGB"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""§ 179 BGB: Was gilt nach §§ 177, 178 BGB in der Schwebezeit, und wie haftet der Vertreter ohne Vertretungsmacht – auf Erfüllung, Schadensersatz, nur den Vertrauensschaden oder gar nicht (§ 179 Abs. 3 BGB)?

Der Fall: Das Motorrad von Enno steht über den Winter in der Garage seines Bekannten Kuno. Kuno verkauft es ohne Vollmacht „im Namen von Enno“ für 4.500 € an Silja. Enno will davon nichts wissen und verweigert die Genehmigung. Silja kauft ein gleichwertiges Motorrad für 5.300 € und verlangt von Kuno die 800 € Mehrkosten.

Inhalt:
– Ausgangslage: Vertreter ohne Vertretungsmacht (falsus procurator), keine Rechtsscheinsvollmacht
– § 177 Abs. 1 BGB im Wortlaut: schwebende Unwirksamkeit, Genehmigung wirkt zurück (§ 184 Abs. 1 BGB)
– § 177 Abs. 2 BGB im Wortlaut: Aufforderung, Zwei-Wochen-Frist, Schweigen gilt als Verweigerung
– § 178 BGB im Wortlaut: Widerruf des anderen Teils, nur bei Kenntnis ausgeschlossen
– § 179 Abs. 1 BGB im Wortlaut: Wahl zwischen Erfüllung und Schadensersatz, Beweislast, Erfüllungsinteresse
– § 179 Abs. 2 BGB: nur Vertrauensschaden, begrenzt auf das Erfüllungsinteresse
– § 179 Abs. 3 BGB: Kenntnis oder Kennenmüssen, beschränkt geschäftsfähiger Vertreter
– Lösung des Falls, § 180 BGB in einem Satz
– Klausurtipp, Prüfschema, Merksatz

Normen: §§ 164 Abs. 1, 177, 178, 179, 180, 182 Abs. 1, 184 Abs. 1, 122 Abs. 2, 433 Abs. 1 BGB

Rechtsprechung:
– BGH, Urt. v. 18.5.2017 – VII ZR 122/14, Rn. 24 (§ 179 Abs. 1 BGB umfasst das Erfüllungsinteresse; Mehraufwand)
– BGH, Urt. v. 25.10.2012 – III ZR 266/11, Rn. 34, 39, 42 (Erfüllungsinteresse; Beweislast des Vertreters)
– BGH, Urt. v. 11.4.2025 – V ZR 194/23, Rn. 17 (schwebende Unwirksamkeit, Rückwirkung der Genehmigung)
– BGH, Urt. v. 1.7.2026 – VIII ZR 4/23, Rn. 37 (Kündigung ohne Vertretungsmacht nichtig, § 180 Satz 1 BGB)

Hinweise: Die Voraussetzungen der Stellvertretung (eigene Willenserklärung, im fremden Namen, Vertretungsmacht) und die Duldungs- und Anscheinsvollmacht erklärt das Video zur Stellvertretung (§ 164 BGB). Personen frei erfunden.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#VertreterOhneVertretungsmacht #BGBAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei):( |\n)", lambda m: {"eins": "I.", "zwei": "II."}[m.group(1)] + m.group(2), srt)
for a, b in [("viertausendfünfhundert Euro", "4.500 Euro"), ("fünftausenddreihundert Euro", "5.300 Euro"),
             ("achthundert Euro", "800 Euro"), ("neunzig Euro", "90 Euro"), ("zwei Wochen", "2 Wochen"),
             ("fünftausenddreihundert statt", "5.300 statt")]:
    srt = srt.replace(a, b)
for a, b in [(r"viertausendfünfhundert\nEuro", "4.500\nEuro"), (r"fünftausenddreihundert\nEuro", "5.300\nEuro"),
             (r"achthundert\nEuro", "800\nEuro"), (r"achthundert\nMehrkosten", "800\nMehrkosten"),
             (r"achthundert Mehrkosten", "800 Mehrkosten"), (r"zwei\nWochen", "2\nWochen"),
             (r"\nviertausendfünfhundert", "\n4.500"), (r"fünftausenddreihundert\n", "5.300\n")]:
    srt = re.sub(a, b, srt)
for w, z in (("Erstens", "1."), ("Zweitens", "2."), ("Drittens", "3."), ("Viertens", "4."), ("Fünftens", "5.")):
    srt = re.sub(rf"(?m)^{w}: ", f"{z} ", srt)
    srt = re.sub(rf"\. {w}:", f". {z}", srt)
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert not re.search(r"tausend|hundert|neunzig|Römisch|Erstens|Zweitens|Drittens|Viertens|Fünftens", srt, re.I), \
    re.findall(r".{20}(?:tausend|hundert|neunzig|Römisch|Erstens|Zweitens|Drittens|Viertens|Fünftens).{10}", srt, re.I)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
