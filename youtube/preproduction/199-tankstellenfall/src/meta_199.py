"""Nachbearbeitung der Upload-Texte für Folge 199 (nach meta_196.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen, Daten).
Aufruf: python3 meta_199.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Tanken ohne Portemonnaie, Sachverhalt"),
       (T("ansp"), "Kaufvertrag: wann? Angebot und Annahme, § 145 BGB"),
       (T("urteil"), "Der Fall des BGH: VIII ZR 171/10"),
       (T("gr"), "Warum schon an der Zapfsäule? Supermarkt und Tankstelle"),
       (T("eig"), "Wem gehört das Benzin? § 929 Satz 1 BGB"),
       (T("offen"), "Eigentum: Meinungsstand, Vermischung"),
       (T("w433"), "Kaufpreis, Fälligkeit, Verzug ohne Mahnung"),
       (T("praxis"), "Praxis: Name, Pfand, Personalausweis; Strafrecht"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Tankstellenfall (BGH VIII ZR 171/10): Kommt der Kaufvertrag nach §§ 145 ff., 433 BGB schon an der Zapfsäule zustande oder erst an der Kasse? Und wem gehört das Benzin?

Der Fall (frei erfunden, Tankstelle ohne Marke): Armin tankt an einer Selbstbedienungstankstelle für 80 €, geht zur Kasse – und sein Portemonnaie liegt zu Hause. Pächterin Margarete sagt: „Das Benzin ist aber schon in Ihrem Tank.“ Armin fragt: „Heißt das, ich habe schon gekauft? Bezahlt wird doch erst hier an der Kasse.“

Inhalt:
– Anspruch aus § 433 Abs. 2 BGB, Angebot und Annahme, § 145 BGB im Wortlaut
– Der Fall des BGH: Landgericht (§§ 145, 151 BGB) und BGH – Kaufvertrag schon mit dem Tanken
– Warum? Supermarkt und Tankstelle, Interessen beider Seiten, objektiver Beobachter
– Eigentum am Benzin: § 929 Satz 1 BGB, Meinungsstand (BGH offen), Vermischung im Tank
– Kaufpreis sofort fällig, Verzug ohne Mahnung beim Wegfahren, Detektivkosten
– Praxis: Name und Adresse, Pfand – und warum der Personalausweis kein Pfand ist
– Klausurtipp, Prüfschema, Merksatz

Normen: §§ 145, 151, 433, 929 BGB; §§ 271, 280, 286 Abs. 2 Nr. 4 BGB; §§ 947, 948 BGB; § 1 Abs. 1 PAuswG

Rechtsprechung:
– BGH, Urt. v. 4.5.2011 – VIII ZR 171/10, NJW 2011, 2871 (Rn. 13–16 Vertragsschluss, Rn. 17 Fälligkeit, Rn. 18–21 Verzug, Rn. 23–26 Detektivkosten)
– LG Traunstein, Urt. v. 7.7.2010 – 5 S 2956/09 (Vorinstanz, wiedergegeben in BGH Rn. 8)
– OLG Düsseldorf, NStZ 1982, 249; OLG Hamm, NStZ 1983, 266; OLG Koblenz, Urt. v. 10.8.1998 – 2 Ss 206/98 (Eigentumsübergang)
– BGH, Beschl. v. 10.1.2012 – 4 StR 632/11, Rn. 4, 5 (Tanken ohne Zahlungswillen)

Hinweise: Angebot und Annahme allgemein erklärt das Video zu §§ 145 ff. BGB, die strafrechtliche Seite das Video zum Tankbetrug. Ob das Eigentum am Benzin schon beim Einfüllen oder erst mit der Bezahlung übergeht, hat der BGH offengelassen.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Tankstellenfall #BGBAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei):( |\n)", lambda m: {"eins": "I.", "zwei": "II."}[m.group(1)] + m.group(2), srt)
srt = re.sub(r"Römisch zwei: ", "II. ", srt)
for a, b in [("für achtzig Euro", "für 80 Euro"), ("Achtzig Euro an Säule vier", "80 Euro an Säule 4"),
             ("am vierten Mai 2011", "am 4. Mai 2011"), ("und zwei Vignetten", "und 2 Vignetten"),
             ("Fällig sind die achtzig", "Fällig sind die 80")]:
    srt = srt.replace(a, b)
srt = re.sub(r"achtzig\n(\S+ )?Euro", lambda m: "80\n" + (m.group(1) or "") + "Euro", srt)
srt = re.sub(r"für zehn\nEuro und einen Cent", "für 10,01\nEuro", srt)
for w, z in (("Erstens", "1."), ("Zweitens", "2."), ("Drittens", "3.")):
    srt = re.sub(rf"(?m)^{w}: ", f"{z} ", srt)
    srt = re.sub(rf"\. {w}:", f". {z}", srt)
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert not re.search(r"achtzig|zehn\b|vierten|Römisch|Erstens|Zweitens|Drittens", srt, re.I), \
    re.findall(r".{20}(?:achtzig|zehn\b|vierten|Römisch|Erstens|Zweitens|Drittens).{10}", srt, re.I)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
