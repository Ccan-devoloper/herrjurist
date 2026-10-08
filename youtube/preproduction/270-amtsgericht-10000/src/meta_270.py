"""Nachbearbeitung der Upload-Texte für Folge 270 (nach meta_258.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Änderungsgesetz, Hinweisen und
Lizenzzeile; Untertitel-Korrekturen (Beträge und Daten als Ziffern, Sprechernamen, Römisch → I.–V.).
Aufruf: python3 meta_270.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: 9.200 € Werklohn – Amtsgericht oder Landgericht?"),
       (T("w23"), "§ 23 Nr. 1 GVG: Amtsgericht bis 10.000 €"),
       (T("w71"), "§ 71 Abs. 1 GVG und die Reform zum 1.1.2026"),
       (T("rech"), "Rechenbeispiel: Nebenforderungen (§ 4 ZPO), mehrere Ansprüche (§ 5 ZPO)"),
       (T("w78"), "Anwaltszwang? § 78 Abs. 1 ZPO"),
       (T("alt"), "Altverfahren: Übergangsvorschrift § 44 EGGVG"),
       (T("w261"), "perpetuatio fori, § 261 Abs. 3 Nr. 2 ZPO"),
       (T("w506"), "Ausnahme: Klageerweiterung, § 506 ZPO"),
       (T("w495"), "§ 495a ZPO: Verfahren bis 1.000 €, keine Zuständigkeitsnorm"),
       (T("sonder"), "Sonderzuständigkeiten: § 23 Nr. 2, § 71 Abs. 2 GVG"),
       (T("tipp"), "Klausurtipp: alte Skripte, Eingangsstempel"),
       (T("sch"), "Prüfschema sachliche Zuständigkeit"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Amtsgericht Zuständigkeit 2026: Seit dem 1.1.2026 ist das Amtsgericht nach § 23 Nr. 1 GVG für Streitigkeiten bis 10.000 Euro zuständig. Was gilt für Altverfahren (§ 44 EGGVG), was bleibt nach § 261 Abs. 3 Nr. 2 ZPO (perpetuatio fori) – und warum ist § 495a ZPO (1.000 Euro) keine Zuständigkeitsnorm?

Der Fall: Tischlermeister Haberkorn hat bei einem Kunden eine Holztreppe eingebaut, die Rechnung über 9.200 Euro ist offen. Muss er zum Landgericht und damit zwingend zum Anwalt? Seine Tochter Irmela, Referendarin, sagt: nicht mehr. Und Frau Bergfeld aus dem Büro fragt nach der Klage vom Dezember über 7.000 Euro, die beim Landgericht liegt.

Inhalt:
– § 23 Nr. 1 GVG im Wortlaut: bis einschließlich 10.000 Euro Amtsgericht; § 71 Abs. 1 GVG: sonst Landgericht
– Die Reform: Gesetz zur Änderung des Zuständigkeitsstreitwerts der Amtsgerichte, zum Ausbau der Spezialisierung der Justiz in Zivilsachen sowie zur Änderung weiterer prozessualer Regelungen vom 8.12.2025 (BGBl. 2025 I Nr. 318), in Kraft seit 1.1.2026; vorher 5.000 Euro
– Rechenbeispiel: Zinsen und Kosten als Nebenforderungen zählen nicht mit (§ 4 Abs. 1 ZPO), mehrere Ansprüche werden zusammengerechnet (§ 5 ZPO)
– Kein Anwaltszwang am Amtsgericht (§ 78 Abs. 1 S. 1 ZPO), die Partei darf den Prozess selbst führen (§ 79 ZPO)
– Altverfahren: § 44 S. 1 EGGVG – vor dem 1.1.2026 anhängig (eingegangen), dann alte Grenze; Zustellung egal
– perpetuatio fori (§ 261 Abs. 3 Nr. 2 ZPO) und die Ausnahme der Klageerweiterung (§ 506 ZPO)
– § 495a ZPO: Verfahren nach billigem Ermessen bis 1.000 Euro (vorher 600 Euro) – Verfahrensregel, keine Zuständigkeitsnorm
– Ohne Rücksicht auf den Wert: § 23 Nr. 2 GVG (etwa Wohnraummiete, WEG, Wildschaden, neu: Nachbarrecht) und § 71 Abs. 2 GVG (etwa Bauvertrag-Anordnungen, neu: Heilbehandlungen, Presse, Vergabe)
– Klausurtipp, Prüfschema, Merksatz

Normen: §§ 23, 71 GVG; § 44 EGGVG; §§ 4, 5, 78, 79, 253 Abs. 1, 261 Abs. 3 Nr. 2, 495a, 506 ZPO.

Hinweise: Herr Haberkorn, Irmela, Frau Bergfeld und die Tischlerei sind erfunden. Ältere Skripte und Kommentare nennen noch 5.000 Euro (§ 23 Nr. 1 GVG) und 600 Euro (§ 495a ZPO). Welche Hilfsmittel in welchem Stand im Examen zugelassen sind, ist von Land zu Land verschieden.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound „05-Papel sobre mesa“ (Tomycatts), CC0.

#Referendariat #2Examen #ZPO
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("neuntausendzweihundert Euro", "9.200 Euro"), ("Neuntausendzweihundert Euro", "9.200 Euro"),
          ("zehntausendzweihundert Euro", "10.200 Euro"), ("Zehntausend statt fünftausend Euro", "10.000 statt 5.000 Euro"),
          ("siebentausend Euro", "7.000 Euro"), ("dreitausend Euro", "3.000 Euro"),
          ("sechshundert auf tausend Euro", "600 auf 1.000 Euro"), ("achthundert Euro", "800 Euro"),
          ("die tausend Euro", "die 1.000 Euro"), ("Streitwert tausend Euro", "Streitwert 1.000 Euro"),
          ("über tausend Euro", "über 1.000 Euro"), ("fünftausend, danach zehntausend Euro", "5.000, danach 10.000 Euro"),
          ("zehntausend Euro", "10.000 Euro"), ("fünftausend Euro", "5.000 Euro"),
          ("achten Dezember", "8. Dezember"), ("zehnten Dezember", "10. Dezember"), ("ersten Januar", "1. Januar"),
          ("Römisch eins:", "I."), ("Römisch zwei:", "II."), ("Römisch drei:", "III."), ("Römisch vier:", "IV."),
          ("Römisch fünf:", "V."), ("oder einundsiebzig Abs.", "oder 71 Abs.")]
for alt, neu in ERSATZ:
    muster = r"\s+".join(re.escape(w) for w in alt.split())
    n = len(re.findall(muster, srt))
    assert n, alt
    srt = re.sub(muster, lambda m: neu if "\n" not in m.group(0) else neu.replace(" ", "\n", 1) if neu.count(" ") else neu, srt)
srt = re.sub(r"Nr\. 1 GVG\n", "Nr. 1 GVG.\n", srt)          # „G.V.G.“ verlor beim Satzende den Punkt
srt = re.sub(r"\bzehntausend\b", "10.000", srt)          # Zahlwort am Ende eines Untertitelblocks (Euro im nächsten Block)
srt = re.sub(r"(?<!Herr )\bHaberkorn:", "Herr Haberkorn:", srt)
srt = re.sub(r"(?<!Frau )\bBergfeld:", "Frau Bergfeld:", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"tausend|Römisch|hundert", srt), re.findall(r".*(?:tausend|Römisch|hundert).*", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + ["§ 44 EGGVG", "perpetuatio fori"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
