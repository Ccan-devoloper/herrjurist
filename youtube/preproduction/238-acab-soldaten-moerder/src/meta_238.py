"""Nachbearbeitung der Upload-Texte für Folge 238 (nach meta_232.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung (Planbeschreibung präzisiert: „gedeutet“, mehrdeutige
Äußerungen statt „Deutungsvorrang“, siehe RECHTSSTAND.md), Fall, Inhalt, Normen, Rechtsprechung mit Randnummern/Seiten,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Kürzel ACAB, Gliederung, Normzitate, Jahreszahlen in Ziffern).
Aufruf: python3 meta_238.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: ACAB-Banner im Stadion, Sachverhalt"),
       (T("a5"), "Art. 5 Abs. 1 GG: Ist das Kürzel eine Meinung?"),
       (T("deut"), "Deutung: objektiver Sinn, Wortlaut und Kontext"),
       (T("mehrd"), "Mehrdeutige Äußerungen"),
       (T("sold"), "„Soldaten sind Mörder“ (BVerfGE 93, 266)"),
       (T("koll"), "Kollektivbeleidigung: Wen trifft die Äußerung?"),
       (T("acab"), "ACAB-Beschlüsse 2016: personalisierte Zuordnung"),
       (T("schr"), "Schranken: Art. 5 Abs. 2 GG, § 185 und § 193 StGB"),
       (T("erg"), "Ergebnis im Fall"),
       (T("gegen"), "Gegenfall: Banner gezielt vor den Polizisten"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Soldaten sind Mörder (BVerfGE 93, 266) und ACAB: Wie werden Äußerungen nach Art. 5 I GG gedeutet? Mehrdeutige Äußerungen, Kollektivbeleidigung und personalisierte Zuordnung (§ 185 StGB).

Der Fall: Fan Hannes hält im Fanblock ein Banner mit dem Kürzel ACAB hoch, in Richtung Spielfeld. Am Spielfeldrand sind Polizisten im Einsatz, eine Polizistin stellt Strafantrag. Beleidigt Hannes damit die Polizisten vor Ort? Unser Fall folgt den Kammerbeschlüssen des Bundesverfassungsgerichts von 2016.

Inhalt:
– Art. 5 Abs. 1 S. 1 GG im Wortlaut: Meinung als Urteil über Sachverhalte, Ideen oder Personen; auch polemisch oder verletzend geschützt; das Kürzel als Meinung
– Deutung: objektiver Sinn aus Sicht eines unvoreingenommenen und verständigen Publikums, Wortlaut, Kontext und Begleitumstände
– Mehrdeutige Äußerungen: Die zur Verurteilung führende Deutung darf erst zugrunde gelegt werden, wenn die anderen mit schlüssigen Gründen ausgeschlossen sind
– Der Klassiker „Soldaten sind Mörder“ (1995)
– Kollektivbeleidigung: je größer das Kollektiv, desto schwächer die persönliche Betroffenheit; Teilgruppe genügt nicht
– ACAB-Beschlüsse 2016: personalisierte Zuordnung zu bestimmten Beamten nötig; Anwesenheit der Polizei im Stadion genügt nicht
– Schranken: Art. 5 Abs. 2 GG und § 185 StGB im Wortlaut, Wechselwirkung, § 193 StGB
– Ergebnis und Gegenfall: Banner gezielt vor einer bestimmten Polizeigruppe
– Klausurtipp, Prüfschema, Merksatz

Normen: Art. 5 Abs. 1 S. 1, Abs. 2 GG; §§ 185, 193 StGB

Rechtsprechung:
– BVerfG, Beschl. v. 10.10.1995 – 1 BvR 1476/91 u. a., BVerfGE 93, 266 („Soldaten sind Mörder“), insbesondere S. 289 (Meinung), S. 295 f. (Deutung, mehrdeutige Äußerungen), S. 299–303 (Kollektivbeleidigung)
– BVerfG (Kammer), Beschl. v. 17.5.2016 – 1 BvR 2150/14 (Buchstaben im Fanblock), Rn. 11–19
– BVerfG (Kammer), Beschl. v. 17.5.2016 – 1 BvR 257/14, Rn. 16 f.
– BVerfG (Kammer), Beschl. v. 16.1.2017 – 1 BvR 1593/16, Rn. 17

Hinweise: Der Fall ist vereinfacht. Im echten Stadionfall hielten mehrere Fans einzelne Buchstaben hoch; kurz zuvor hatten sie auf Bannern Polizeieinsätze kritisiert. Im Gegenfall kommt eine Beleidigung in Betracht; ob sie vorliegt, entscheidet die Abwägung bei § 193 StGB. Wie man Meinungen von Tatsachenbehauptungen abgrenzt, zeigt die Folge zur Auschwitzlüge; die Wechselwirkung erklärt die Folge zum Lüth-Urteil.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Grundrechte #Meinungsfreiheit #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
for muster, ersatz in [(r"Kürzel ACAB Es", "Kürzel ACAB. Es"), (r"Kürzel ACAB\n\n", "Kürzel ACAB.\n\n"), (r"Erstens:", "1."), (r"Zweitens:", "2."),
                       (r"STGB", "StGB")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
srt = srt.replace("\nRoth: ", "\nPolizistin Roth: ")
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "tausend" not in srt and "A.C.A.B" not in srt, "Zahlwort/Kürzel im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = [("mehrdeutige Äußerung" if t == "Deutungsvorrang" else t) for t in m["tags"]]   # siehe RECHTSSTAND.md, Plankorrektur 2
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
