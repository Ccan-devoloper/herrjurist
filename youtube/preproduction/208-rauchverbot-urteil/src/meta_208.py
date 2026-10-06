"""Nachbearbeitung der Upload-Texte für Folge 208 (nach meta_205.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn.,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Normangaben, Römisch → I.).
Keine Namen der realen Beschwerdeführer, keine Tabakmarken.
Aufruf: python3 meta_208.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: die Eckkneipe und das große Lokal"),
       (T("disko"), "Die Diskothek ohne Raucherraum"),
       (T("frage"), "Die Frage und das Rauchverbot-Urteil"),
       (T("sv"), "Sachverhalt und Wortlaut Art. 12 GG"),
       (T("schutz"), "Schutzbereich und Eingriff: Berufsausübungsregelung"),
       (T("recht"), "Rechtfertigung: Ziel, Eignung, Erforderlichkeit"),
       (T("strikt"), "Angemessenheit: striktes Verbot oder Ausnahmen"),
       (T("folge"), "Folgerichtigkeit: die Last der Einraumkneipe"),
       (T("a3"), "Art. 3 GG: die Diskothek"),
       (T("tenor"), "Tenor und Übergangsregelung"),
       (T("alfons"), "Lösung des Falls und heute"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Rauchverbot-Urteil (BVerfGE 121, 317): Warum Raucherräume für große Lokale die Eckkneipe unzumutbar belasten (Art. 12 I GG) und Diskotheken nicht pauschal von der Ausnahme ausgeschlossen werden durften (Art. 12 I i. V. m. Art. 3 I GG).

Der Fall: Alfons führt in Baden-Württemberg eine Kneipe mit einem einzigen Gastraum von 63 m². Seit August 2007 gilt ein Rauchverbot, größere Lokale dürfen aber einen abgetrennten Raucherraum einrichten. Die Stammgäste gehen ins große Lokal. Frau Kaltenbach darf in ihrer Großraumdiskothek, in die nur Erwachsene dürfen, gar keinen Raucherraum einrichten. Unser Fall folgt dem Rauchverbot-Urteil des Bundesverfassungsgerichts vom 30. Juli 2008.

Inhalt:
– Schutzbereich der Berufsfreiheit, Art. 12 Abs. 1 GG (im Wortlaut)
– Eingriff: unmittelbar, kein bloßer Reflex; Berufsausübungsregelung (erste Stufe des Apotheken-Urteils); Art. 14 GG tritt zurück
– Rechtfertigung: Gesundheitsschutz als überragend wichtiges Gemeinschaftsgut, Eignung, Erforderlichkeit
– Angemessenheit: Ein striktes Rauchverbot ohne Ausnahmen wäre zulässig. Wer Ausnahmen zulässt, muss sie folgerichtig ausgestalten.
– Ergebnis: unzumutbar für kleine Einraumkneipen mit getränkegeprägtem Angebot
– Art. 3 Abs. 1 GG (im Wortlaut): gleichheitswidriger Begünstigungsausschluss der Diskotheken
– Tenor (Unvereinbarkeit, Frist 31.12.2009), Übergangsregelung des Gerichts, Klausurtipp, Prüfschema, Merksatz

Normen: Art. 12 Abs. 1 GG; Art. 3 Abs. 1 GG; damals § 7 Landesnichtraucherschutzgesetz Baden-Württemberg (2007), § 2 Abs. 1 Nr. 8, § 4 Abs. 3 Nichtraucherschutzgesetz Berlin (2007). Den Nichtraucherschutz in Gaststätten regeln die Länder; welche Ausnahmen heute gelten, steht im jeweiligen Landesgesetz.

Rechtsprechung:
– BVerfG, Urt. v. 30.7.2008 – 1 BvR 3262/07, 1 BvR 402/08, 1 BvR 906/08, BVerfGE 121, 317 (Rauchverbot in Gaststätten), Tenor Nr. 1 und 2; Rn. 37–59, 90–102, 113–116, 121–125, 128–147, 148–160, 161–169
– zum Vergleich: BVerfGE 7, 377 (Apotheken-Urteil, Drei-Stufen-Theorie)

Hinweise: Alfons, Herr Stadler und Frau Kaltenbach sind erfundene Figuren; sie folgen dem echten Fall. Die realen Beschwerdeführer werden nicht genannt.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Rauchverbot #Berufsfreiheit #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("Stadler: Tut mir", "Herr Stadler: Tut mir"), ("Kaltenbach: Jede", "Frau Kaltenbach: Jede"),
             ("über zwanzig Jahren", "über 20 Jahren"), ("dreiundsechzig\nQuadratmeter", "63\nQuadratmeter"),
             ("rund siebzig\nProzent", "rund 70\nProzent"), ("um dreißig bis vierzig Prozent", "um 30 bis 40 Prozent"),
             ("dreißigsten Juli 2008", "30. Juli 2008"), ("unter fünfundsiebzig\nQuadratmetern", "unter 75\nQuadratmetern"),
             ("Art. 12 Abs. 1:", "Art. 12 Abs. 1 GG:"), ("Art. 3 Abs. 1:", "Art. 3 Abs. 1 GG:"),
             ("Art. 14 tritt", "Art. 14 GG tritt"), ("Verbindung mit Art. 3 Abs. 1.", "Verbindung mit Art. 3 Abs. 1 GG.")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"Römisch (eins|zwei|drei|vier):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV."}[m.group(1)] + m.group(2), srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Römisch|zwanzig|siebzig|dreißig|fünfund", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
