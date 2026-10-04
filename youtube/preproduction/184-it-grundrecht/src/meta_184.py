"""Nachbearbeitung der Upload-Texte für Folge 184 (nach meta_181.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel an den Folienanfängen (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall,
Inhalt, Normen, Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Ziffern,
Zeilenumbruch nach „Art.“/„§“). Aufruf: python3 meta_184.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Staatstrojaner auf dem Laptop"),
       (T("art10"), "Art. 10 GG: Fernmeldegeheimnis"),
       (T("art13"), "Art. 13 GG: Unverletzlichkeit der Wohnung"),
       (T("ris"), "Informationelle Selbstbestimmung reicht nicht"),
       (T("luecke"), "Die Schutzlücke: das IT-Grundrecht (BVerfG 2008)"),
       (T("stpo"), "Quellen-TKÜ, § 100a Abs. 1 S. 2, 3 StPO"),
       (T("q08"), "Maßstab der Quellen-TKÜ: 2008 und 2025"),
       (T("od"), "Online-Durchsuchung, § 100b StPO"),
       (T("schr"), "Rechtfertigung: konkrete Gefahr oder besonders schwere Straftat"),
       (T("richt"), "Richtervorbehalt und Kernbereichsschutz"),
       (T("n1"), "Seit 2025: Trojaner II und Zitiergebot"),
       (T("loes"), "Lösung des Falls"),
       (T("tipp"), "Klausurtipp: Grundrecht nach der Zugriffsart"),
       (T("sch"), "Prüfungsschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""IT-Grundrecht (Art. 2 I i.V.m. 1 I GG, BVerfGE 120, 274): Wann darf die Polizei per Staatstrojaner deinen Laptop ausspähen? Online-Durchsuchung vs. Quellen-TKÜ.

Der Fall: Bestimmte Tatsachen begründen den Verdacht, dass Herr Weinhold mit einer Bande Falschgeld herstellt. Die Absprachen laufen über einen verschlüsselten Messenger auf seinem Laptop. Kommissar Hollstein will heimlich Software auf dem Laptop installieren. Welches Grundrecht schützt davor – und wann ist der Zugriff erlaubt?

Inhalt:
– Schutzbereich: Art. 10 GG (laufende Kommunikation), Art. 13 GG (Raum, nicht Gerät), informationelle Selbstbestimmung (Verweis auf das Video zum Volkszählungsurteil) – und die Schutzlücke
– Das Grundrecht auf Gewährleistung der Vertraulichkeit und Integrität informationstechnischer Systeme (IT-Grundrecht), BVerfG 2008
– Quellen-TKÜ (§ 100a Abs. 1 S. 2, 3 StPO, Wortlaut) und Online-Durchsuchung (§ 100b Abs. 1 StPO, Wortlaut)
– Maßstab: 2008 bei reiner Quellen-TKÜ allein Art. 10 GG, seit 2025 zugleich das IT-Grundrecht
– Rechtfertigung: konkrete Gefahr für überragend wichtige Rechtsgüter (Gefahrenabwehr), Verdacht einer besonders schweren Straftat (Strafverfolgung), Richtervorbehalt, Kernbereichsschutz
– Seit 2025 (Trojaner II): Quellen-TKÜ nur bei besonders schweren Straftaten, teilweise nichtig; § 100b StPO verletzt das Zitiergebot, gilt aber bis zu einer Neuregelung fort
– Lösung, Klausurtipp (Grundrecht nach der Art des Zugriffs), Prüfungsschema, Merksatz

Normen: Art. 2 Abs. 1 i.V.m. Art. 1 Abs. 1, Art. 10 Abs. 1, Art. 13 Abs. 1, Art. 19 Abs. 1 S. 2 GG; § 100a Abs. 1 S. 2, 3, § 100b Abs. 1, 2, § 100d, § 100e Abs. 2 StPO; § 146 StGB; präventiv z. B. § 49 BKAG

Rechtsprechung:
– BVerfG, Urt. v. 27.2.2008 – 1 BvR 370/07, 1 BvR 595/07 (Online-Durchsuchung), BVerfGE 120, 274, Rn. 166–207, 247, 257–259, 271–283
– BVerfG, Urt. v. 20.4.2016 – 1 BvR 966/09, 1 BvR 1140/09 (BKAG), BVerfGE 141, 220, Rn. 209–212
– BVerfG, Beschl. v. 24.6.2025 – 1 BvR 2466/19 (Trojaner I), LS 3, Rn. 93–110
– BVerfG, Beschl. v. 24.6.2025 – 1 BvR 180/23 (Trojaner II), Tenor, LS 1–3, Rn. 134, 172–176, 201–213, 241–251, 275 f.

Hinweise: Der Fall ist ein Übungsfall. Das Urteil von 2008 betraf eine Befugnis des Verfassungsschutzes in Nordrhein-Westfalen; seine Anforderungen an den Eingriffsanlass („konkrete Gefahr für ein überragend wichtiges Rechtsgut“) gelten für die Gefahrenabwehr, für die Strafverfolgung kommt es auf das Gewicht der Straftat an. Nicht behandelt: Benachrichtigungspflichten, Verwertungsfragen im Strafprozess, Landespolizeigesetze im Einzelnen, Ankauf und Offenhalten von Sicherheitslücken.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Grundrechte #ITGrundrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"Römisch (eins|zwei|drei),", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)], srt)
srt = srt.replace("höchstens drei\nJahren", "höchstens 3\nJahren").replace("höchstens drei Jahren", "höchstens 3 Jahren")
srt = re.sub(r"(Art\.|§|Abs\.)\n(\S+)", r"\1 \2\n", srt)
assert not re.search(r"§\n|Abs\.\n|Art\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "Römisch" not in srt and "tausend" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ["Trojaner II", "Fernmeldegeheimnis", "Zitiergebot", "Kernbereich privater Lebensgestaltung", "Examenswissen Grundrechte"]:
    if t not in m.get("tags", []):
        m.setdefault("tags", []).append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
