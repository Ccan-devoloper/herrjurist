"""Nachbearbeitung der Upload-Texte für Folge 162 (nach meta_160.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn.,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Römisch → I.).
Aufruf: python3 meta_162.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Beleidigt – und § 1004 BGB schützt nur das Eigentum?"),
       (T("w1004"), "Das Problem: Wortlaut von § 1004 und § 823 BGB"),
       (T("ana"), "Was ist eine Analogie?"),
       (T("bgh"), "Die BGH-Formel: planwidrige Regelungslücke und vergleichbare Interessenlage"),
       (T("l1"), "1. Regelungslücke"),
       (T("pw1"), "2. Planwidrigkeit"),
       (T("vi1"), "3. Vergleichbare Interessenlage"),
       (T("rspr"), "Quasinegatorischer Unterlassungsanspruch"),
       (T("einzel"), "Einzelanalogie und Gesamtanalogie"),
       (T("gegen"), "Umkehrschluss und teleologische Reduktion"),
       (T("grenz"), "Grenzen: Analogieverbot und Vorbehalt des Gesetzes"),
       (T("loes"), "Lösung des Falls"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Analogie Jura: Wann darf man eine Norm entsprechend anwenden? Planwidrige Regelungslücke und vergleichbare Interessenlage einfach erklärt.

Der Fall: Ilona wird von ihrem Nachbarn Bertold seit Wochen immer wieder beleidigt, auch vor anderen Nachbarn. Sie klagt auf Unterlassung. Bertold meint: § 1004 BGB schützt nur das Eigentum. Das Gesetz regelt den Fall nicht ausdrücklich – darf die Richterin trotzdem entscheiden?

Inhalt:
– § 1004 Abs. 1 BGB und § 823 Abs. 1 BGB im Wortlaut: warum es eine Lücke gibt
– Begriff der Analogie, erst nach der Auslegung
– die Formel des Bundesgerichtshofs (BGH IX ZR 91/24, Rn. 14)
– drei Schritte: 1. Regelungslücke, 2. Planwidrigkeit (Fall übersehen, nicht bewusst ausgespart; Beispiel Kilometerleasing), 3. vergleichbare Interessenlage
– Leitbeispiel: quasinegatorischer Unterlassungsanspruch, § 1004 Abs. 1 S. 2 BGB analog i. V. m. § 823 Abs. 1 BGB und allgemeinem Persönlichkeitsrecht
– Einzelanalogie und Gesamtanalogie (Rechtsanalogie)
– Gegenstücke: Umkehrschluss und teleologische Reduktion
– Grenzen: Analogieverbot nach Art. 103 Abs. 2 GG (im Wortlaut), Vorbehalt des Gesetzes im Öffentlichen Recht
– Lösung des Falls, Klausurtipp, Prüfschema, Merksatz

Normen: § 1004 Abs. 1 BGB; § 823 Abs. 1 BGB; §§ 12, 862 BGB; §§ 604 Abs. 3, 671 Abs. 1 BGB; Art. 103 Abs. 2 GG; Art. 20 Abs. 3 GG

Rechtsprechung:
– BGH, Urt. v. 16.1.2025 – IX ZR 91/24, Rn. 14 f. (Voraussetzungen der Analogie)
– BGH, Urt. v. 24.2.2021 – VIII ZR 36/20, Rn. 38–44 (st. Rspr.; keine Analogie beim Kilometerleasing)
– BGH, Urt. v. 16.1.2015 – V ZR 110/14, Rn. 20 (negatorischer Schutz für alle von § 823 BGB geschützten Rechtsgüter)
– BGH, Urt. v. 2.5.2024 – I ZR 12/23, Rn. 16 (quasinegatorischer Unterlassungsanspruch)
– BGH, Urt. v. 10.12.2024 – VI ZR 230/23, Rn. 14, 19; Urt. v. 4.12.2018 – VI ZR 128/18, Rn. 5, 9 (Persönlichkeitsrecht, Wiederholungsgefahr)
– BGH, Urt. v. 8.2.2013 – V ZR 56/12, Rn. 17 (Rechtsanalogie zu §§ 604 Abs. 3, 671 Abs. 1 BGB)
– BVerwG, Urt. v. 27.10.2010 – 6 C 17/09, Rn. 30 (teleologische Reduktion als Gegenstück)
– BVerfG, Beschl. v. 7.12.2011 – 2 BvR 2500/09, Rn. 164 f. (Verbot strafbegründender Analogie)

Hinweise: Ilona, Bertold und die Richterin sind erfundene Figuren. Die Auslegungsmethoden erklärt die Folge zu den Auslegungsmethoden, den Beseitigungsanspruch beim Eigentum die Folge zu § 1004 BGB, das Analogieverbot im Strafrecht die Folge zur Unfallflucht.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Analogie #Methodenlehre #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(S\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei|vier):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV."}[m.group(1)] + m.group(2), srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Römisch", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
