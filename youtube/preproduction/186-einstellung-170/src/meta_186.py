"""Nachbearbeitung der Upload-Texte für Folge 186 (nach meta_180.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Daten, Zahlen, Sprecher).
Aufruf: python3 meta_186.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Augenarzt angezeigt, Staatsanwaltschaft stellt ein"),
       (T("p170"), "Wann wird eingestellt? § 170 II StPO im Wortlaut"),
       (T("verfg"), "Die Einstellungsverfügung: Ziffer 1 und Ziffer 2"),
       (T("p170s2"), "Mitteilung an den Beschuldigten: § 170 II 2 StPO"),
       (T("p171"), "Bescheid an den Antragsteller mit Belehrung: § 171 StPO"),
       (T("p172"), "Beschwerde: § 172 I StPO, zwei Wochen"),
       (T("p172b"), "Klageerzwingungsantrag: ein Monat, Oberlandesgericht"),
       (T("p172c"), "Form: Tatsachen, Beweismittel, Anwalt (§ 172 III StPO)"),
       (T("ausschl"), "Ausschluss: Privatklagedelikte und Opportunität"),
       (T("p174"), "Entscheidung des OLG: §§ 174, 175 StPO"),
       (T("lsg"), "Lösung: Fristen am Kalender (§ 43 StPO)"),
       (T("sch"), "Prüfschema Klageerzwingungsantrag"),
       (T("tipp"), "Klausurtipp: die Mitteilungen nicht vergessen"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Einstellung § 170 II StPO: Wann stellt die Staatsanwaltschaft ein, welche Mitteilungen braucht es (§ 171), und wie funktionieren Beschwerde und Klageerzwingung (§ 172)?

Der Fall: Nach einer Augenoperation sieht eine Patientin auf einem Auge nichts mehr. Sie zeigt den Arzt an und verlangt seine Bestrafung. Ein Gutachten findet keinen Behandlungsfehler, die Aufklärung ist belegt. Die Referendarin bei der Staatsanwaltschaft will einstellen und die Akte weglegen – aber was gehört in die Einstellungsverfügung, und was kann die Patientin tun?

Inhalt:
– § 170 Abs. 1, Abs. 2 S. 1 StPO im Wortlaut: Einstellung, wenn der hinreichende Tatverdacht fehlt (aus tatsächlichen oder rechtlichen Gründen) oder ein Verfahrenshindernis besteht
– Aufbau der Einstellungsverfügung: Ziffer 1 Einstellung, Ziffer 2 Mitteilungen (übliche Klausurpraxis)
– Mitteilung an den Beschuldigten: § 170 Abs. 2 S. 2 StPO im Wortlaut, Nr. 88 RiStBV
– Bescheid an den Antragsteller mit Gründen und Belehrung: § 171 S. 1, 2 StPO im Wortlaut; Verletzte nach § 373b StPO; Zustellung nach Nr. 91 Abs. 2 RiStBV
– Vorschaltbeschwerde: § 172 Abs. 1 StPO im Wortlaut – zwei Wochen, an die Generalstaatsanwaltschaft, nur für Verletzte; ohne Belehrung läuft keine Frist
– Klageerzwingungsantrag: § 172 Abs. 2 S. 1, Abs. 3 S. 1, 2, Abs. 4 StPO im Wortlaut – ein Monat, Oberlandesgericht, Tatsachen und Beweismittel, Anwaltszwang
– Ausschluss nach § 172 Abs. 2 S. 3 StPO: reine Privatklagedelikte (z. B. einfache Körperverletzung, § 374 Abs. 1 Nr. 4 StPO) und bestimmte Opportunitätseinstellungen
– Entscheidung des Oberlandesgerichts: §§ 174, 175 StPO
– Lösung mit Fristenrechnung am Kalender (§ 43 StPO), Prüfschema, Klausurtipp, Merksatz

Normen: §§ 43, 170, 171, 172, 174, 175, 373b, 374 StPO; §§ 223, 226, 229 StGB; § 147 GVG; Nr. 88, 89, 91 RiStBV

Rechtsprechung:
– BVerfG, Beschl. v. 2.7.2018 – 2 BvR 1550/17, Rn. 18, 19 (Darlegungsanforderungen an den Klageerzwingungsantrag nach § 172 Abs. 3 S. 1 StPO; keine Überspannung)

Hinweise: Die Gliederung der Einstellungsverfügung ist Klausurpraxis und kann je nach Land und Prüfungsamt abweichen. Wann der Tatverdacht hinreichend ist und welche Verfahrenshindernisse es gibt, zeigen die Folgen „Hinreichender Tatverdacht: Wann die Staatsanwaltschaft anklagen darf“ und „Verfahrenshindernisse StPO: Strafantrag, Verjährung & Co.“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#StPO #Klageerzwingung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei),( |\n)", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
for muster, ersatz in [(r"dreizehnte(\s)Januar", r"13.\1Januar"), (r"zweiten(\s)Juli", r"2.\1Juli"),
                       (r"sechzehnten(\s)Juli", r"16.\1Juli"), (r"dreizehnten(\s)Juli", r"13.\1Juli"),
                       (r"fünften(\s)August", r"5.\1August"), (r"fünfte(\s)September", r"5.\1September"),
                       (r"des siebten\b", "des 7.")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
ZAHL = {"zwei": "2", "einen": "1", "einem": "1", "eines": "1"}
srt, n = re.subn(r"\b(zwei)(\s)(Wochen|Teile)\b", lambda m: ZAHL[m.group(1)] + m.group(2) + m.group(3), srt)
assert n >= 3, n
srt = srt.replace("Doktor Wallner", "Dr. Wallner")
srt = srt.replace("\nRautenberg: ", "\nFrau Rautenberg: ").replace("\nWallner: ", "\nDr. Wallner: ").replace("\nHoelscher: ", "\nReferendarin Hölscher: ")
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "Paragraf" not in srt, "Zahlwort im Untertitel"
assert "Hoelscher" not in srt
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
