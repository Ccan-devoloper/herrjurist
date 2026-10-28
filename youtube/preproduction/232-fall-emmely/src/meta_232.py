"""Nachbearbeitung der Upload-Texte für Folge 232 (nach meta_152.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung (Dauer korrigiert: „fast 31
Jahren“), Fall, Inhalt, Normen, Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen
(Gliederung, Normzitate, Zahlen und Beträge in Ziffern).
Aufruf: python3 meta_232.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Pfandbons über 1,30 € nach fast 31 Jahren, Sachverhalt"),
       (T("p626"), "§ 626 Abs. 1 BGB: wichtiger Grund in zwei Stufen"),
       (T("s1"), "1. Stufe: an sich geeignet – auch bei geringem Wert"),
       (T("fest"), "1. Stufe im Fall"),
       (T("abw"), "2. Stufe: Interessenabwägung und mildere Mittel"),
       (T("verh"), "Abmahnung, § 314 Abs. 2 BGB"),
       (T("fall2"), "Abwägung im Fall: offen, fast 31 Jahre, Vorrat an Vertrauen"),
       (T("proz"), "Prozessverhalten und Ergebnis"),
       (T("p2"), "§ 626 Abs. 2 BGB und hilfsweise ordentliche Kündigung"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Fall Emmely (BAG 2 AZR 541/09): Rechtfertigen Pfandbons über 1,30 Euro nach fast 31 Jahren eine fristlose Kündigung nach § 626 BGB? Interessenabwägung und Abmahnung.

Der Fall: Kassiererin Doris arbeitet seit fast 31 Jahren ohne Beanstandung in einem Supermarkt. Zwei gefundene Pfandbons über 0,48 € und 0,82 € soll sie im Kassenbüro aufbewahren. Zehn Tage später löst sie bei einem privaten Einkauf zwei nicht abgezeichnete Pfandbons ein – vor den Augen ihres Vorgesetzten. Der Arbeitgeber kündigt fristlos, hilfsweise ordentlich. Unser Fall folgt dem echten Fall, den das Bundesarbeitsgericht 2010 entschieden hat.

Inhalt:
– § 626 Abs. 1 BGB im Wortlaut: wichtiger Grund, zweistufige Prüfung, keine absoluten Kündigungsgründe
– 1. Stufe: Vermögensdelikte gegen den Arbeitgeber sind an sich geeignet, auch bei geringem Wert; keine Wertgrenze; Prognoseprinzip statt Strafe
– 2. Stufe: Interessenabwägung, mildere Mittel; Abmahnung aus dem Verhältnismäßigkeitsgrundsatz, § 314 Abs. 2 BGB als Bestätigung
– Abwägung im Fall: offen statt heimlich, fast 31 Jahre ohne vergleichbare Pflichtverletzung, „erarbeiteter Vorrat an Vertrauen“, objektiver Maßstab, geringer Nachteil; Prozessverhalten
– Ergebnis: Kündigung unwirksam, eine Abmahnung hätte ausgereicht
– § 626 Abs. 2 BGB (Zwei-Wochen-Frist) und hilfsweise ordentliche Kündigung (§ 1 Abs. 2 KSchG)
– Klausurtipp, Prüfschema, Merksatz

Normen: § 626 Abs. 1, 2 BGB; § 314 Abs. 2 BGB; § 623 BGB; § 1 Abs. 2 KSchG; §§ 4, 13 KSchG

Rechtsprechung:
– BAG, Urt. v. 10.6.2010 – 2 AZR 541/09 („Emmely“), insbesondere Rn. 16 (zwei Stufen), Rn. 25–28 (geringwertige Vermögensdelikte, keine Wertgrenze, Prognoseprinzip), Rn. 34–38 (Interessenabwägung, Abmahnung), Rn. 45–50 (Abwägung im Fall, „Vorrat an Vertrauen“), Rn. 52–56 (Prozessverhalten), Rn. 58 (ordentliche Kündigung)

Hinweise: Die Fallgeschichte ist vereinfacht (im echten Fall rund 30 Jahre und 10 Monate Beschäftigung; anwesend war die Kassenleiterin). Ob die Zwei-Wochen-Frist im echten Fall eingehalten war, hat das BAG nicht erörtert. Wann das Kündigungsschutzgesetz gilt und warum die Klagefrist so wichtig ist, zeigt die Folge „Ohne Grund gekündigt? So schützt das Kündigungsschutzgesetz“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Arbeitsrecht #Kündigung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei|vier):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV."}[m.group(1)] + m.group(2), srt)
for muster, ersatz in [(r"einunddreißig(\s+)Jahre", r"31\1Jahre"),
                       (r"achtundvierzig(\s+)und(\s+)zweiundachtzig(\s+)Cent", r"48\1und\g<2>82\3Cent"),
                       (r"einen(\s+)Euro(\s+)dreißig", r"1,30\2€"),
                       (r"Zehn(\s+)Tage", r"10\1Tage"), (r"zehn(\s+)Tagen", r"10\1Tagen"), (r"zwei(\s+)Wochen", r"2\1Wochen"),
                       (r"drei(\s+)Wochen", r"3\1Wochen")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
srt = srt.replace("\nBartels: ", "\nHerr Bartels: ")
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "tausend" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
