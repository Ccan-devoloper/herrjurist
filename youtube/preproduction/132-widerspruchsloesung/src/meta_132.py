"""Nachbearbeitung der Upload-Texte für Folge 132 (Kopie von meta_126.py, nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn./Seite, Hinweisen
und Lizenzzeile; Untertitel: Normangaben mit Gesetz, Sprecherbezeichnungen, „des §§ 257“ → „des § 257 StPO“.
Aufruf: python3 meta_132.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: „nur mal informatorisch“ gefragt"),
       (T("p163"), "1. Belehrungspflicht, § 163a IV 2, § 136 I 2 StPO"),
       (T("besch"), "2. Beschuldigtenstellung und informatorische Befragung"),
       (T("vv"), "3. Verwertungsverbot (BGHSt 38, 214)"),
       (T("wl"), "4. Widerspruchslösung und § 257 StPO"),
       (T("erg"), "Ergebnis: Grundfall und Variante"),
       (T("p136a"), "5. Abgrenzung: § 136a StPO"),
       (T("rev"), "6. Revision: Widerspruch vortragen"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Widerspruchslösung: Wann folgt aus fehlender Belehrung nach § 136 I 2 StPO ein Verwertungsverbot, und warum braucht es einen rechtzeitigen Widerspruch (§ 257 StPO)?

Der Fall: Herr Mangold sprüht einen Schriftzug an die frisch gestrichene Wand einer Turnhalle. Eine Anwohnerin zeigt der Polizei den Mann, er hat Farbe an den Fingern und die Spraydose in der Hand. Polizeikommissarin Kirchhoff fragt ihn ohne Belehrung „nur mal informatorisch“, ob er gesprüht habe – er gesteht. In der Hauptverhandlung sagt sie als Zeugin über das Geständnis aus; der Verteidiger widerspricht direkt danach der Verwertung. Und was, wenn er geschwiegen hätte?

Inhalt:
– 1. Belehrungspflicht: § 163a Abs. 4 S. 2 i. V. m. § 136 Abs. 1 S. 2 StPO (Wortlaut)
– 2. Beschuldigtenstellung: Verfolgungswille und Willensakt, informatorische Befragung, Stärke des Tatverdachts, Beurteilungsspielraum und Willkürgrenze
– 3. Verwertungsverbot nach BGHSt 38, 214; Ausnahme: Schweigerecht bekannt
– 4. Widerspruchslösung: Widerspruch des verteidigten Angeklagten bis zum Zeitpunkt des § 257 StPO (Wortlaut), ohne Verteidiger nur nach Hinweis des Vorsitzenden; Kritik an der Frist
– Ergebnis für Grundfall (rechtzeitiger Widerspruch) und Variante (Widerspruch erst im Plädoyer)
– 5. Abgrenzung: § 136a Abs. 3 StPO – unverwertbar auch bei Zustimmung
– 6. Revision: Widerspruch und Beschuldigtenstellung in der Verfahrensrüge vortragen (§ 344 Abs. 2 S. 2 StPO, Folge 72)
– Klausurtipp, Klausurschema, Merksatz

Rechtsprechung:
– BGH, Beschl. v. 27.2.1992 – 5 StR 190/91, BGHSt 38, 214 (Leitsatz; S. 224 f.: Kenntnis des Schweigerechts; S. 225 f.: Widerspruch bis zum Zeitpunkt des § 257 StPO; S. 226: unverteidigter Angeklagter; S. 227 f.: Befragung am Tatort, Stärke des Tatverdachts)
– BGH, Urt. v. 6.10.2016 – 2 StR 46/15, Rn. 14 (BGHSt 61, 266): Widerspruch spätestens in der Erklärung nach der Beweiserhebung, danach nicht nachholbar; in der Verfahrensrüge darzulegen; Rn. 16: Zweifel an der Frist (für Durchsuchungsfunde)
– BGH, Urt. v. 9.5.2018 – 5 StR 17/18, Rn. 6–8: vollständiger Vortrag zum Widerspruch; Rügepräklusion beim verteidigten (oder entsprechend belehrten) Angeklagten
– BGH, Urt. v. 3.7.2007 – 1 StR 3/07, Rn. 17–19 (BGHSt 51, 367); Beschl. v. 6.6.2019 – StB 14/19, Rn. 30–32: Beschuldigtenbegriff
– BGH, Beschl. v. 10.3.2026 – 5 StR 547/25, Rn. 6 f.: Willkürgrenze; Vortrag aller Verfahrenstatsachen zur Beschuldigtenstellung

Hinweise: BGHSt 38, 214 ist mit den Seiten der amtlichen Sammlung zitiert (Volltext über das Deutschsprachige Fallrecht). Das Klausurschema ist Klausurkonvention. Den Aufbau der Verfahrensrüge erklärt Folge 72.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (StPO zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#StPO #Beweisverwertungsverbot #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
srt = srt.replace("des §§ 257", "des § 257")
for alt, neu in (("\nAnwohnerin: ", "\nAnwohnerin: "), ("\nKirchhoff: ", "\nPolizistin Kirchhoff: "),
                 ("\nMangold: ", "\nHerr Mangold: "), ("\nHufnagel: ", "\nRechtsanwalt Hufnagel: ")):
    srt = srt.replace(alt, neu)
# Normangaben im Untertitel mit Gesetz (gesprochen ohne „StPO“)
srt = re.sub(r"(§ \d+[a-z]?(?:\s+Abs\. \d+)?(?: S\. \d+)?)(?=[.,:]|\s+(?:verletzt|auch|kein|Absatz))", r"\1 StPO", srt)
# Normangabe nicht über zwei Untertitel verteilen: „§ 344“ | „Abs. 2 S. 2 …“ → „§ 344 Abs. 2 S. 2 StPO“ | „…“
bl = srt.strip().split("\n\n")
for i in range(len(bl) - 1):
    k1, t1 = bl[i].split("\n", 2)[:2], bl[i].split("\n", 2)[2]
    k2, t2 = bl[i + 1].split("\n", 2)[:2], bl[i + 1].split("\n", 2)[2]
    m_ = re.match(r"(Abs\. \d+ S\. \d+)\s*", t2)
    if re.search(r"§ \d+[a-z]?$", t1) and m_:
        t1 += " " + m_.group(1) + " StPO"; t2 = t2[m_.end():]
        bl[i] = "\n".join(k1 + [t1]); bl[i + 1] = "\n".join(k2 + [t2])
srt = "\n\n".join(bl) + "\n"
srt = srt.replace("Abs. 2 S. 2 StPO", "Abs. 2 Satz 2 StPO").replace("Abs. 4 S. 2 StPO", "Abs. 4 Satz 2 StPO")
srt = srt.replace("Abs. 1 S. 2 StPO", "Abs. 1 Satz 2 StPO")
srt = re.sub(r" \n", "\n", srt)
srt = re.sub(r"vom Wort(\s)informatorisch", r"vom Wort\1„informatorisch“", srt)
assert "Paragraf" not in srt and "§§" not in srt
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = ["Widerspruchslösung", "Beweisverwertungsverbot", "Belehrung § 136 StPO", "§ 257 StPO",
             "informatorische Befragung", "Beschuldigtenbelehrung", "Revision", "Referendariat", "2. Staatsexamen"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
