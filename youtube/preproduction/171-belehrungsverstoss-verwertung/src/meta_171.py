"""Nachbearbeitung der Upload-Texte für Folge 171 (Kopie von meta_132.py, nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn./Seite, Hinweisen
und Lizenzzeile; Untertitel: Sprecherbezeichnungen, „informatorisch“ in Anführungszeichen.
Aufruf: python3 meta_171.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: „nur informatorisch“ gefragt – und zweimal gestanden"),
       (T("besch"), "1. Schritt: Wann ist man Beschuldigter?"),
       (T("vv"), "2. Schritt: Verwertungsverbot – drei Lehren, Abwägungslehre"),
       (T("rk"), "Rechtskreistheorie"),
       (T("sz"), "Schutzzwecklehre"),
       (T("gleich"), "Ergebnis des Streits und Widerspruch"),
       (T("fort"), "3. Schritt: Qualifizierte Belehrung (BGHSt 53, 112)"),
       (T("folge"), "Abwägung beim zweiten Geständnis"),
       (T("bgh"), "BGH-Fall gegen Fall Pieper"),
       (T("fern"), "Fernwirkung und Ergebnis"),
       (T("tipp"), "Klausurtipp: Prüfungsaufbau"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Belehrungsverstoß nach § 136 I StPO: Wann ist man Beschuldigter, welche Lehre trägt das Beweisverwertungsverbot – und ist ein zweites Geständnis nach ordnungsgemäßer Belehrung verwertbar? Qualifizierte Belehrung (BGHSt 53, 112) erklärt.

Der Fall: Herr Pieper fährt am Bahnhof auf einem fremden Rad los, im Korb liegt das aufgebrochene Schloss. Ein Polizist fragt ihn ohne Belehrung „nur informatorisch“, wem das Rad gehört – er gesteht. Auf der Wache wird er ordnungsgemäß belehrt, aber nicht darauf hingewiesen, dass das erste Geständnis unverwertbar ist. Er gesteht noch einmal. Seine Verteidigerin widerspricht rechtzeitig.

Inhalt:
– 1. Schritt, Beweiserhebungsverbot: Beschuldigter durch Willensakt (Inkulpationsakt) oder bei starkem Verdacht; Beurteilungsspielraum und Willkürgrenze; vager Verdacht: Befragung als Zeuge
– 2. Schritt, Verwertungsverbot als Streitstand: Abwägungslehre, Rechtskreistheorie, Schutzzwecklehre – hier mit gleichem Ergebnis; Widerspruch (mehr in Folge 132 zur Widerspruchslösung)
– 3. Schritt, Fortwirkung: qualifizierte Belehrung, Abwägung im Einzelfall, BGH-Fall gegen Fall Pieper
– Fernwirkung grundsätzlich abgelehnt; Ergebnis
– Klausurtipp mit Prüfungsaufbau I.–IV., Merksatz

Rechtsprechung:
– BGH, Urt. v. 18.12.2008 – 4 StR 455/08, BGHSt 53, 112 (Leitsätze; Rn. 8 f.: Beschuldigtenstellung; Rn. 10, 12 f.: qualifizierte Belehrung; Rn. 14 f.: Abwägung, Ergebnis im entschiedenen Fall; Rn. 16: Zeuge bei schwachem Verdacht)
– BGH, Urt. v. 3.5.2018 – 3 StR 390/17, Rn. 28 f.: Fortwirkung, qualifizierte Belehrung, Abwägung
– BGH, Urt. v. 3.7.2007 – 1 StR 3/07, BGHSt 51, 367, Rn. 17 f.: Willensakt, förmliches Verfahren, Durchsuchung
– BGH, Urt. v. 14.8.2009 – 3 StR 552/08, BGHSt 54, 69, Rn. 47: Abwägungslehre
– BGH, Beschl. v. 27.2.1992 – 5 StR 190/91, BGHSt 38, 214, 219 f.: Abwägung, Grundlagen der Stellung des Beschuldigten
– BGH (GrS), Beschl. v. 21.1.1958 – GSSt 4/57, BGHSt 11, 213, 215; BGH, Beschl. v. 5.7.2022 – 4 StR 61/22, Rn. 12: Rechtskreistheorie
– BGH, Beschl. v. 7.3.2006 – 1 StR 316/05, Rn. 22 f.: keine Fernwirkung von Beweisverwertungsverboten

Hinweise: BGHSt 11, 213 und 38, 214 sind mit den Seiten der amtlichen Sammlung zitiert (Volltext über das Deutschsprachige Fallrecht). Die Schutzzwecklehre ist als Ansicht im Schrifttum dargestellt. Das Ergebnis zum zweiten Geständnis ist eine Abwägung im Übungsfall. Den Widerspruch und seinen Zeitpunkt erklärt Folge 132 (Widerspruchslösung).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (StPO zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#StPO #Beweisverwertungsverbot #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nLohmeyer: ", "\nPolizeihauptmeister Lohmeyer: "), ("\nPieper: ", "\nHerr Pieper: ")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"das Wort(\s)informatorisch", r"das Wort\1„informatorisch“", srt)
assert "Paragraf" not in srt
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = ["§ 136 StPO", "Beweisverwertungsverbot", "qualifizierte Belehrung", "BGHSt 53, 112", "Beschuldigtenstellung",
             "Abwägungslehre", "Rechtskreistheorie", "Widerspruchslösung", "Strafprozessrecht"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
