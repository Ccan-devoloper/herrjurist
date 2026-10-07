"""Nachbearbeitung der Upload-Texte für Folge 222 (nach meta_219.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit korrigierter Anfangszeile, Fall, Inhalt, Normen, amtlichen
Hinweisen, Verweisen und Lizenzzeile; Untertitel-Korrekturen (Beträge und Folgennummern als Ziffern, Sprechernamen,
Römisch → I./II./III.). Kein Landesrecht als Regel. Aufruf: python3 meta_222.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: 30 Seiten Akte und der Bearbeitervermerk"),
       (T("vorn"), "In der Akte: die Kautionsklage"),
       (T("auszug"), "Aktenauszug statt Sachverhalt, die ersten 20 Minuten"),
       (T("s1"), "1. Bearbeitervermerk: Rolle und Entwurf (Min. 0–5)"),
       (T("erlassen"), "1. Bearbeitervermerk: erlassen und Stichtag"),
       (T("s2"), "2. Erster Durchgang: Beteiligte und Anträge (Min. 5–15)"),
       (T("chron"), "2. Erster Durchgang: Chronologie und Daten"),
       (T("typ"), "Zivilurteil: § 313 Abs. 2 ZPO, unstreitig und streitig"),
       (T("vwgo"), "Verwaltungsurteil: § 117 Abs. 2 VwGO, Klagefrist"),
       (T("stpo"), "Anklage: § 200 Abs. 1 StPO"),
       (T("s3"), "3. Arbeitsblatt als Muster (Min. 15–20)"),
       (T("fallen"), "Fallen: Hinweise im Vermerk und Anlagen"),
       (T("f3"), "Falle: Eingang und Zustellung"),
       (T("tipp"), "Klausurtipp und Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Aktenauszug Assessorklausur: Bearbeitervermerk als Arbeitsauftrag lesen, Beteiligte, Anträge, Zeitstrahl und Fristen erfassen – mit Blick auf § 313 ZPO, § 117 VwGO und § 200 StPO.

Der Fall: Zweites Examen, Klausur im Zivilrecht, fünf Stunden. Vor Referendarin Hermine liegen 30 Seiten Akte. Ganz hinten der Bearbeitervermerk: „Die Entscheidung des Gerichts ist zu entwerfen. Rubrum, Streitwertfestsetzung und Rechtsbehelfsbelehrung sind erlassen.“ In der Akte verlangt Herr Rehberg von seiner früheren Vermieterin, Frau Pohlmann, die Mietkaution von 1.500 Euro zurück; sie behält sie wegen Kratzern im Parkett.

Inhalt:
– Aktenauszug statt fertigem Sachverhalt; die ersten 20 Minuten als Empfehlung aus Erfahrung (5 / 10 / 5 Minuten)
– 1. Bearbeitervermerk zuerst: Rolle und Entwurf, was ist erlassen, Stichtag
– 2. Erster Durchgang: Beteiligte, Anträge, Chronologie und Daten
– Blick nach Klausurtyp: Tatbestand nach § 313 Abs. 2 ZPO (unstreitig/streitig), Urteilsteile nach § 117 Abs. 2 VwGO und Klagefrist nach § 74 VwGO, Anklagesatz nach § 200 Abs. 1 StPO
– 3. Arbeitsblatt als Muster und Zeitplan für die übrigen 4 Stunden 40 Minuten
– Drei Fallen: Hinweise im Vermerk, Anlagen, Eingang und Zustellung (§§ 253, 261, 167 ZPO, § 291 BGB)
– Klausurtipp, Schema, Merksatz

Normen: § 313 Abs. 2 ZPO; § 117 Abs. 2 VwGO; § 74 Abs. 1 VwGO; § 200 Abs. 1 StPO; §§ 253 Abs. 1, 261 Abs. 1, 167 ZPO; § 291 BGB.
Amtliche Hinweise: Landesjustizprüfungsamt Sachsen-Anhalt, Hinweise für die Aufsichtsarbeiten der Zweiten juristischen Staatsprüfung (zivilrechtliche, öffentlich-rechtliche und strafrechtliche Aufgabenstellung; nach eigener Angabe unverbindlich).

Hinweise: Hermine, Herr Rehberg und Frau Pohlmann sind erfunden. Die Minutenangaben sind eine Empfehlung, keine Vorgabe; Bearbeitungszeit, Hilfsmittel und Klausurtypen regelt das Recht deines Landes. Mehr dazu: Folge 18 (Relationstechnik), Folge 39 (Anklageklausur), Folge 45 (Zeitplan für die Klausur).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com).

#Referendariat #2Examen #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("eintausendfünfhundert Euro", "1.500 Euro"), ("eintausendsechshundertfünfzig Euro", "1.650 Euro"),
          ("Rehberg: Ich will", "Herr Rehberg: Ich will"), ("Pohlmann: Das Parkett", "Frau Pohlmann: Das Parkett"),
          ("Folge achtzehn", "Folge 18"), ("Folge neununddreißig", "Folge 39"), ("Folge fünfundvierzig", "Folge 45"),
          ("Römisch eins,", "I.,"), ("Römisch zwei,", "II.,"), ("Römisch drei,", "III.,")]
for alt, neu in ERSATZ:
    muster = r"\s+".join(re.escape(w) for w in alt.split())
    n = len(re.findall(muster, srt))
    assert n, alt
    srt = re.sub(muster, lambda m: neu if "\n" not in m.group(0) else neu.replace(" ", "\n", 1) if neu.count(" ") else neu, srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"tausend|Römisch|\n(Rehberg|Pohlmann):", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + ["Bearbeitervermerk erlassen", "Assessorklausur Zeitplan"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
