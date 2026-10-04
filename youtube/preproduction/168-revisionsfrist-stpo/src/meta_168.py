"""Nachbearbeitung der Upload-Texte für Folge 168 (nach meta_152.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Daten, Zahlen).
Aufruf: python3 meta_168.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Urteil am Montag, Zustellung sieben Wochen später"),
       (T("aufbau"), "Aufbau: Statthaftigkeit und die drei Fristen"),
       (T("p341"), "Einlegung: § 341 StPO, eine Woche ab Verkündung"),
       (T("p32d"), "Form: § 32d S. 2 StPO – elektronisch seit 2022"),
       (T("frist1"), "Fristberechnung § 43 StPO: Pfingstmontag"),
       (T("p345"), "Begründungsfrist § 345 StPO: ab Zustellung"),
       (T("p3452"), "Form § 345 Abs. 2, Inhalt § 344, Sprungrevision § 335"),
       (T("entd"), "Fall: Die Frist ist versäumt"),
       (T("p44"), "Wiedereinsetzung §§ 44, 45 StPO"),
       (T("zur"), "Verschulden des Verteidigers – Lösung"),
       (T("grenze"), "Grenze: keine Wiedereinsetzung für Verfahrensrügen"),
       (T("tab"), "Merktabelle: die Fristen"),
       (T("tipp"), "Klausurtipp: der Fristen-Check"),
       (T("sch"), "Prüfschema Zulässigkeit"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Revisionsfrist in der StPO: Einlegung nach § 341, Begründung nach § 345 StPO, Form und Wiedereinsetzung (§ 44) – auch bei Verschulden des Verteidigers.

Der Fall: Das Landgericht verurteilt Herrn Tiedemann an einem Montag im Mai. Seine Verteidigerin legt Revision ein; das schriftliche Urteil wird ihr erst sieben Wochen später zugestellt. In der Kanzlei wird die Begründungsfrist einen Monat zu spät notiert. Ist die Revision verloren?

Inhalt:
– Einlegung: § 341 Abs. 1 StPO im Wortlaut – binnen einer Woche nach Verkündung, beim Gericht, dessen Urteil angefochten wird; bei Abwesenheit grundsätzlich ab Zustellung (§ 341 Abs. 2)
– Form: Verteidiger müssen Revision und Begründung elektronisch übermitteln, § 32d S. 2 Nr. 2 StPO (seit 1.1.2022); ein Fax ist unwirksam
– Fristberechnung nach § 43 StPO: Wochenfrist bis zum gleichen Wochentag, Monatsfrist bis zum Tag gleicher Zahl; Ende an Sonnabend, Sonntag oder Feiertag → nächster Werktag (Beispiel Pfingstmontag 2026)
– Begründung: § 345 Abs. 1 StPO im Wortlaut – ein Monat nach Ablauf der Einlegungsfrist, bei späterer Zustellung ab Zustellung; Verlängerung nach S. 2 nur bei Urteilen, die erst nach 21 Wochen zu den Akten kommen
– Form der Begründung (§ 345 Abs. 2 StPO), Inhalt (§ 344 StPO), Sprungrevision (§ 335 StPO)
– Wiedereinsetzung in den vorigen Stand: §§ 44, 45 StPO im Wortlaut – ohne Verschulden, Antrag binnen einer Woche, Glaubhaftmachung, Nachholung
– Verschulden des Verteidigers wird dem Angeklagten grundsätzlich nicht zugerechnet; Grenze: keine Wiedereinsetzung zum Nachschieben von Verfahrensrügen
– Merktabelle, Klausurtipp (Fristen-Check), Prüfschema, Merksatz

Normen: §§ 32a, 32d, 43, 44, 45, 333, 335, 341, 344, 345 StPO; § 85 Abs. 2 ZPO

Rechtsprechung:
– BGH, Beschl. v. 7.3.2023 – 6 StR 74/23, Rn. 4 (§ 32d S. 2 StPO seit 1.1.2022; Form- und Wirksamkeitsvoraussetzung)
– BGH, Beschl. v. 9.8.2022 – 6 StR 268/22, Rn. 3–5 (Revision per Telefax unwirksam; Anwaltsverschulden – Wiedereinsetzung)
– BGH, Beschl. v. 23.4.2026 – 4 StR 134/26, Rn. 1 (Verschulden der Verteidigerin dem Angeklagten nicht zuzurechnen)
– BGH, Beschl. v. 14.4.2026 – 6 StR 94/26, Rn. 1 f. (Frist in der Kanzlei falsch notiert; Begründungsfrist ab Zustellung)
– BGH, Beschl. v. 9.12.2025 – 6 StR 331/25, Rn. 5 (Wochenfrist des § 45: Kenntnis des Angeklagten maßgeblich)
– BGH, Beschl. v. 19.6.2024 – 5 StR 442/23, Rn. 6 (keine Wiedereinsetzung zur Nachholung von Verfahrensrügen, Ausnahme rechtliches Gehör)
– BGH, Beschl. v. 8.1.2026 – 3 StR 368/25, Rn. 2 (Ausnahme: Sitzungsprotokoll nicht rechtzeitig verfügbar)

Hinweise: Seit dem 1.1.2026 gilt § 32d S. 2 StPO in einer Neufassung, die auch die Rücknahme der Revision erfasst. Was die Revision inhaltlich prüft (Sach- und Verfahrensrüge), zeigt die Folge „Revision: Sachrüge vs. Verfahrensrüge“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Revision #StPO #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei|vier|fünf):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV.", "fünf": "V."}[m.group(1)] + m.group(2), srt)
for muster, ersatz in [(r"sieben(\s)Wochen", r"7\1Wochen"), (r"ersten(\s)Januar", r"1.\1Januar"),
                       (r"achtzehnten(\s)Mai", r"18.\1Mai"), (r"fünfundzwanzigsten(\s)Mai", r"25.\1Mai"),
                       (r"sechsundzwanzigsten(\s)Mai", r"26.\1Mai"), (r"einundzwanzig(\s|\n\n\d+\n[^\n]+\n)Wochen", r"21\1Wochen"),
                       (r"sechsten(\s)Juli", r"6.\1Juli"), (r"sechsten(\s)August", r"6.\1August"),
                       (r"sechste(\s)September", r"6.\1September"), (r"zehnten(\s)August", r"10.\1August"),
                       (r"zwölften(\s)August", r"12.\1August")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
srt = srt.replace("\nSternberg: ", "\nRechtsanwältin Sternberg: ").replace("\nTiedemann: ", "\nHerr Tiedemann: ")
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "tausend" not in srt and "zwanzig" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
