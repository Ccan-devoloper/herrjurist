"""Nachbearbeitung der Upload-Texte für Folge 180 (nach meta_168.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Daten, Zahlen, Sprecher).
Aufruf: python3 meta_180.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Beleidigung im Treppenhaus, Strafantrag vier Monate später"),
       (T("aufbau"), "Aufbau: vier Verfahrenshindernisse, zwei prozessuale Taten"),
       (T("p194"), "Strafantrag: §§ 194, 230, 77 StGB, Form § 158 Abs. 2 StPO"),
       (T("p77b"), "Antragsfrist: § 77b StGB im Wortlaut"),
       (T("kenn"), "Fristberechnung am Kalender: verspätet"),
       (T("f1"), "Klausurfehler 1: Frist nicht gerechnet"),
       (T("p230"), "Besonderes öffentliches Interesse: § 230 StGB"),
       (T("absol"), "Beleidigung: absolutes Antragsdelikt – Klausurfehler 2"),
       (T("p78"), "Verjährung: § 78 Abs. 3 StGB – Klausurfehler 3"),
       (T("p103"), "Strafklageverbrauch: Art. 103 Abs. 3 GG"),
       (T("p170"), "Verfügung: Einstellung nach § 170 Abs. 2 StPO und Anklage"),
       (T("f4"), "Klausurfehler 4: Privatklageweg trotz verspätetem Antrag"),
       (T("tab"), "Die vier Fehler auf einen Blick"),
       (T("sch"), "Prüfschema je prozessuale Tat"),
       (T("tipp"), "Klausurtipp: drei Fragen je Antragsdelikt"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Verfahrenshindernisse StPO: Strafantrag (§ 77 StGB), öffentliches Interesse, Verjährung, Strafklageverbrauch – und wann nach § 170 II StPO eingestellt wird.

Der Fall: Herr Stolte beleidigt seinen Nachbarn im Treppenhaus, am nächsten Tag schubst er ihn. Erst vier Monate später stellt der Nachbar Strafantrag. Die Referendarin bei der Staatsanwaltschaft will beides anklagen – und macht dabei vier typische Klausurfehler.

Inhalt:
– Strafantrag als Prozessvoraussetzung: § 194 Abs. 1 S. 1 StGB im Wortlaut, § 230 StGB, antragsberechtigt ist der Verletzte (§ 77 Abs. 1 StGB), Form nach § 158 Abs. 2 StPO
– Antragsfrist: § 77b Abs. 1 S. 1, Abs. 2 S. 1 StGB im Wortlaut – drei Monate ab Kenntnis von Tat und Täter; Fristberechnung am Kalender
– Ausweg nur bei relativen Antragsdelikten: besonderes öffentliches Interesse nach § 230 Abs. 1 S. 1 StGB (Nr. 234 RiStBV: einschlägige Vorstrafe)
– Die einfache Beleidigung ist absolutes Antragsdelikt; Ausnahmen nach § 194 Abs. 1 S. 2, 3 StGB nur in Sonderfällen
– Verjährung: § 78 Abs. 3 Nr. 4, 5 StGB im Wortlaut – Beleidigung drei Jahre, öffentliche Beleidigung und Körperverletzung fünf Jahre; Beginn § 78a, Unterbrechung § 78c StGB
– Strafklageverbrauch: Art. 103 Abs. 3 GG im Wortlaut
– Verfügung: Einstellung nach § 170 Abs. 2 S. 1 StPO, Anklage bei Privatklagedelikten nur im öffentlichen Interesse (§§ 374, 376 StPO); auch die Privatklage braucht einen rechtzeitigen Strafantrag
– Fehlertabelle (falsch – richtig – Fundstelle), Prüfschema, Klausurtipp, Merksatz

Normen: §§ 77, 77b, 78, 78a, 78c, 185, 194, 223, 230 StGB; §§ 158, 170, 374, 376 StPO; Art. 103 Abs. 3 GG; Nr. 234 RiStBV

Rechtsprechung:
– BVerfG, Urt. v. 31.10.2023 – 2 BvR 900/22, Rn. 3, 95 (Art. 103 Abs. 3 GG: rechtskräftiges Strafurteil über dieselbe Tat als Verfahrenshindernis)

Hinweise: Wo die Verfahrenshindernisse im Gutachten stehen, ist Klausurpraxis und nicht gesetzlich geregelt – maßgeblich sind Bearbeitervermerk und Prüfungsamt. Den Aufbau der Anklageklausur mit prozessualer Tat und Abschlussverfügung zeigt die Folge „Anklageklausur: Das Gesamtschema vom Gutachten bis zur Verfügung“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Strafantrag #StPO #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
ZAHL = {"eins": "1", "zwei": "2", "drei": "3", "vier": "4", "fünf": "5"}
for muster, ersatz in [(r"elften(\s)März", r"11.\1März"), (r"elften(\s)Juni", r"11.\1Juni"),
                       (r"zwölften(\s)März", r"12.\1März"), (r"zwölften(\s)Juni", r"12.\1Juni"),
                       (r"dreizehnten(\s)Juli", r"13.\1Juli"), (r"Sätze zwei(\s)und drei", r"Sätze 2\1und 3"),
                       (r"dann fünf\.", "dann 5.")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
srt, n = re.subn(r"\b(zwei|drei|vier|fünf)(\s)(Monate|Monaten|Jahre|Jahren|Tagen|prozessuale|Fehler|Fragen)\b",
                 lambda m: ZAHL[m.group(1)] + m.group(2) + m.group(3), srt)
assert n >= 10, n
srt, n = re.subn(r"\bDrei(\s)Fragen", r"3\1Fragen", srt)
srt = srt.replace("\nOstwald: ", "\nHerr Ostwald: ").replace("\nHartlieb: ", "\nReferendarin Hartlieb: ")
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "Paragraf" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
