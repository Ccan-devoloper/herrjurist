"""Nachbearbeitung der Upload-Texte für Folge 177 (Kopie von meta_170.py) (nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung, Hinweisen und
Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_177.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Der Chip zerstört die Steuerungseinheit"),
       (T("pos"), "Drei Schadensposten – welcher Anspruch?"),
       (T("agl"), "Grundtatbestand: § 280 Abs. 1 BGB im Wortlaut"),
       (T("gt1"), "Grundtatbestand im Fall (§ 434 BGB, § 377 HGB, Vertretenmüssen)"),
       (T("w3"), "Statt der Leistung: §§ 280 Abs. 3, 281 BGB – die Frist"),
       (T("kf"), "Die Kontrollfrage"),
       (T("a1"), "Posten 1: der Chip – statt der Leistung"),
       (T("b1"), "Posten 2: die Steuerungseinheit – neben der Leistung"),
       (T("c1"), "Posten 3: der Produktionsausfall (BGH V ZR 93/08)"),
       (T("loes"), "Lösung, Klausurtipp und Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Schadensersatz neben der Leistung (§ 280 I BGB) oder statt der Leistung (§§ 280 I, III, 281 BGB)? Die Kontrollfrage: Würde eine Nacherfüllung den Schaden noch beseitigen?

Der Fall: Elfriede führt eine Druckerei. Bei Dietrich, der Steuerchips selbst herstellt, kauft sie einen Chip zum Nachrüsten ihrer Druckmaschine für 300 Euro. Der Chip ist fehlerhaft, überhitzt und zerstört die bis dahin einwandfreie Steuerungseinheit. Drei Tage steht die Maschine still. Elfriede verlangt sofort 300 Euro für den Chip, 6.000 Euro für die neue Steuerungseinheit und 4.500 Euro entgangenen Gewinn – eine Frist hat sie nicht gesetzt. Welcher Posten läuft über welchen Anspruch?

Inhalt:
– Grundtatbestand: § 437 Nr. 3 BGB führt zu § 280 Abs. 1 BGB (Wortlaut); Sachmangel, Pflichtverletzung, Rüge nach § 377 HGB, vermutetes Vertretenmüssen (Hersteller statt bloßer Händler)
– Schadensersatz statt der Leistung: § 280 Abs. 3 und § 281 Abs. 1 Satz 1 BGB im Wortlaut – die Frist als letzte Chance des Verkäufers
– Die Kontrollfrage der Lehre: Würde eine ordnungsgemäße Nacherfüllung im letztmöglichen Zeitpunkt den Schaden noch beseitigen?
– Posten 1, der Chip: statt der Leistung, ohne Frist kein Geld (Ausnahmen § 281 Abs. 2, § 440 BGB)
– Posten 2, die Steuerungseinheit: neben der Leistung, § 280 Abs. 1 BGB
– Posten 3, der Produktionsausfall: neben der Leistung, ohne Verzug; Verzögerungsschaden §§ 280 Abs. 2, 286 BGB
– Lösungstabelle, Klausurtipp, Klausurschema, Merksatz

Normen: §§ 280, 281, 437 Nr. 3 BGB; §§ 433, 434, 440, 286 BGB; § 377 HGB

Rechtsprechung und Materialien:
– BGH, Urt. v. 19.6.2009 – V ZR 93/08, BGHZ 181, 317, Rn. 12, 14 (mangelbedingter Nutzungsausfall nach §§ 437 Nr. 3, 280 Abs. 1 BGB ohne Verzug)
– BGH, Urt. v. 7.2.2019 – VII ZR 63/18, Rn. 17–19 (Folgeschäden, die eine Nacherfüllung nicht beseitigt: neben der Leistung, keine Frist)
– BGH, Urt. v. 3.7.2013 – VIII ZR 169/12, BGHZ 197, 357, Rn. 26 f. (Abgrenzung danach, ob eine Nacherfüllung den Schaden beseitigt hätte)
– BGH, Urt. v. 15.7.2008 – VIII ZR 211/07, BGHZ 177, 224, Rn. 21, 29 (Nacherfüllung als letzte Chance; Hersteller nicht Erfüllungsgehilfe des Händlers)
– BT-Drucks. 14/6040, S. 224 f. (Betriebsausfallschaden bei mangelhafter Maschine nach § 280 Abs. 1)

Hinweise: Die Formel „im letztmöglichen Zeitpunkt“ ist eine Klausurformel der Lehre. Beim Verbrauchsgüterkauf kann die Frist nach § 475d BGB entbehrlich sein (Folge 125); hier kaufen zwei Kaufleute. Das System der §§ 280 ff. BGB erklärt Folge 046, den Schuldnerverzug Folge 112.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Schadensersatz #Zivilrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"Abs\.\n(\d+) ", r"Abs. \1\n", srt)                                  # „Abs.“ nicht von der Zahl trennen
srt = srt.replace("\nund drei mit § 281.", "\nund 3 mit § 281.")                       # Zahlwort der Schreibform
for w, z in (("zehntausendfünfhundert", "10.500"), ("viertausendfünfhundert", "4.500"), ("sechstausend", "6.000"),
             ("dreihundert", "300")):
    srt = srt.replace(w + " Euro", z + " Euro").replace(w + "\nEuro", z + "\nEuro")
    srt = re.sub(rf"\b{w}\b", z, srt)
assert "Abs.\n" not in srt and "und drei mit" not in srt and "tausend" not in srt and "dreihundert" not in srt
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
