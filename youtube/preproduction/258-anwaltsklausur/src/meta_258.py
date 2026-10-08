"""Nachbearbeitung der Upload-Texte für Folge 258 (nach meta_222.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit präzisierter Anfangszeile, Fall, Inhalt, Normen, amtlichen
Hinweisen, Verweisen und Lizenzzeile; Untertitel-Korrekturen (Beträge und Folgennummern als Ziffern, Sprechernamen,
Römisch → I./II./III., Abkürzungen). Kein Landesrecht als Regel. Aufruf: python3 meta_258.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Anzahlung weg, was soll die Mandantin tun?"),
       (T("pers"), "Perspektivwechsel: parteiisch, aber gebunden"),
       (T("w43"), "§ 43a Abs. 3 BRAO: Sachlichkeit"),
       (T("abs4"), "§ 43a Abs. 4 und 5 BRAO: widerstreitende Interessen"),
       (T("auf"), "Aufbau: Mandantenbegehren und drei Stufen"),
       (T("gut"), "I. Gutachten am Fall (§§ 323, 346 BGB)"),
       (T("zw"), "II. Zweckmäßigkeit statt zweitem Gutachten"),
       (T("t1"), "Zweckmäßigkeit am Fall: Zeit, Kosten, Beweis, Vergleich, Eilrechtsschutz"),
       (T("is2"), "Ergebnis in der Kanzlei"),
       (T("prak"), "III. Praktischer Teil je nach Bearbeitervermerk"),
       (T("drei"), "Kurzblick Zivilrecht: Klageschrift, § 253 ZPO"),
       (T("oer"), "Kurzblick Öffentliches Recht und Strafrecht"),
       (T("tipp"), "Klausurtipp und Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Anwaltsklausur Aufbau im Zivil-, Straf- und öffentlichen Recht: Mandantenbegehren, Gutachten, echte Zweckmäßigkeitserwägungen und praktischer Teil (Schriftsatz, Mandantenschreiben, Vertragsentwurf) – mit den Grenzen aus § 43a BRAO.

Der Fall: Frau Steinhoff hat einem Gartenbaubetrieb 3.000 Euro für eine neue Terrasse angezahlt. Fertig sein sollte sie Ende April, passiert ist nichts. In der Kanzlei fragt sie: „Ich will mein Geld zurück. Was soll ich jetzt tun?“ Referendarin Isolde schreibt das Gutachten – und am Ende einen Vorschlag.

Inhalt:
– Perspektivwechsel: Der Anwalt ist parteiisch, aber sachlich und wahrheitsgebunden (§ 43a Abs. 3 BRAO); keine widerstreitenden Interessen, auch nicht in der Anwaltsstation (§ 43a Abs. 4, 5 BRAO)
– Aufbau: vorweg das Mandantenbegehren, dann I. Gutachten, II. Zweckmäßigkeit, III. praktischer Teil – Benennung und Umfang nach dem Bearbeitervermerk
– Gutachten am Fall: Rücktritt nach Fristsetzung (§ 323 Abs. 1 BGB), Rückgewähr (§ 346 Abs. 1 BGB), Amtsgericht
– Zweckmäßigkeit statt zweitem Gutachten: der sicherste, schnellste und kostengünstigste Weg – Zeit, Kosten (§ 91 ZPO), Beweisbarkeit, Vergleich, Eilrechtsschutz (§ 917 ZPO)
– Praktischer Teil: Fristsetzung und Mandantenschreiben in verständlicher Sprache
– Kurzblick: Klageschrift (§ 253 Abs. 2 ZPO), verwaltungsgerichtliche Klage (§ 81 VwGO), Verteidigung (§ 137 StPO)
– Klausurtipp, Schema, Merksatz

Normen: § 43a Abs. 3–5 BRAO; §§ 323, 346 BGB; § 23 Nr. 1 GVG; §§ 91, 253 Abs. 2, 917 ZPO; § 81 Abs. 1 VwGO; § 137 Abs. 1 StPO.
Amtliche Hinweise: Landesjustizprüfungsamt Sachsen-Anhalt, Hinweise für die Aufsichtsarbeiten der Zweiten juristischen Staatsprüfung (zivilrechtliche, öffentlich-rechtliche und strafrechtliche Aufgabenstellung; nach eigener Angabe unverbindlich).

Hinweise: Frau Steinhoff, Isolde und Herr Hohlfeld sind erfunden, die Kanzlei ist namenlos. Ob ein Schriftsatz, ein Mandantenschreiben oder ein Vertragsentwurf verlangt ist und wie die Teile heißen, regelt der Bearbeitervermerk deiner Klausur. Mehr dazu: Folge 222 (Bearbeitervermerk und Aktenauszug), Folge 39 (Anklageklausur aus Sicht der Staatsanwaltschaft).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound „paper on a table“ (horcasitas), CC0.

#Referendariat #2Examen #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("dreitausend Euro", "3.000 Euro"), ("Folge zweihundertzweiundzwanzig", "Folge 222"),
          ("Folge neununddreißig", "Folge 39"), ("Römisch eins:", "I."), ("Römisch zwei:", "II."),
          ("Römisch drei:", "III."), ("Steinhoff: Ich habe", "Frau Steinhoff: Ich habe"),
          ("Hohlfeld: Sie schreiben", "Herr Hohlfeld: Sie schreiben")]
for alt, neu in ERSATZ:
    muster = r"\s+".join(re.escape(w) for w in alt.split())
    n = len(re.findall(muster, srt))
    assert n, alt
    srt = re.sub(muster, lambda m: neu if "\n" not in m.group(0) else neu.replace(" ", "\n", 1) if neu.count(" ") else neu, srt)
srt = re.sub(r"(?<!Frau )\bSteinhoff:", "Frau Steinhoff:", srt)
srt = re.sub(r"(?<!Herr )\bHohlfeld:", "Herr Hohlfeld:", srt)
srt = srt.replace("VWGO", "VwGO").replace("STPO", "StPO")
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"tausend|Römisch|zweihundertzwei", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + ["Anwaltsklausur Aufbau", "Zweckmäßigkeit Anwaltsklausur"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
