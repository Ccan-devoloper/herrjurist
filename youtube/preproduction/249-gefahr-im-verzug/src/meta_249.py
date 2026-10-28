"""Nachbearbeitung der Upload-Texte für Folge 249 (nach meta_246.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt).
Aufruf: python3 meta_249.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Polizei am Sonntagabend"),
       (T("frage"), "Die Frage und der Sachverhalt"),
       (T("art13"), "1. Schutzbereich und 2. Eingriff"),
       (T("abs2"), "3. Rechtfertigung: Art. 13 II GG"),
       (T("def"), "Wann liegt Gefahr im Verzug vor?"),
       (T("bereit"), "Richterlicher Bereitschaftsdienst"),
       (T("p105"), "§ 105 StPO"),
       (T("loes"), "Lösung"),
       (T("gegen"), "Gegenfall und Verwertung"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Gefahr im Verzug (Art. 13 II GG, § 105 StPO): Wann darf die Polizei ohne richterlichen Beschluss deine Wohnung durchsuchen? Enge Auslegung nach BVerfGE 103, 142 und der richterliche Bereitschaftsdienst nach BVerfGE 151, 67.

Der Fall: Sonntag, 19 Uhr. Kommissar Bader und Kommissarin Ebner klingeln bei Ines und wollen sofort Wohnung und Atelier durchsuchen – ein Richter sei am Sonntagabend nicht zu erreichen. Versucht, den Bereitschaftsdienst des Amtsgerichts zu erreichen, hat niemand – obwohl die Bereitschaftsrichterin erreichbar war. Verletzt die Durchsuchung Ines in ihrem Grundrecht aus Art. 13 GG?

Inhalt (Grundrechtsprüfung):
– Schutzbereich: Wohnung als räumliche Sphäre des Privatlebens, auch Arbeits- und Geschäftsräume
– Eingriff: Begriff der Durchsuchung
– Rechtfertigung nach Art. 13 Abs. 2 GG: Richtervorbehalt als Regel, Gefahr im Verzug als eng auszulegende Ausnahme
– Anforderungen: Tatsachen des Einzelfalls, zuerst Versuch, einen Richter zu erreichen, nicht selbst herbeigeführt, Dokumentation
– Bereitschaftsdienst: bei Tage (6 bis 21 Uhr) uneingeschränkt erreichbar
– § 105 Abs. 1 Satz 1 StPO, Lösung, Gegenfall, Verwertung (Verweis)
– Klausurtipp, Schema, Merksatz

Normen: Art. 13 Abs. 1, 2, 7 GG; §§ 102, 105 StPO; § 152 GVG.

Rechtsprechung:
– BVerfG, Urt. v. 20.2.2001 – 2 BvR 1444/00, BVerfGE 103, 142, Rn. 26 f., 31 f., 34, 38–40, 44 f., 54
– BVerfG, Beschl. v. 12.3.2019 – 2 BvR 675/14, BVerfGE 151, 67, Rn. 56, 58, 67 (Bereitschaftsdienst)
– BVerfG, Beschl. v. 16.6.2015 – 2 BvR 2718/10 u. a., BVerfGE 139, 245, Rn. 71 (mündliche Eilentscheidung)
– BVerfG, Beschl. v. 30.9.2025 – 2 BvR 460/25, Rn. 28, 36 (Wohnungs- und Durchsuchungsbegriff)
– BVerfGE 109, 279, Rn. 142 (Geschäftsräume)
– BVerfG, Beschl. v. 2.7.2009 – 2 BvR 2225/08, Rn. 16 f. (Verwertung: Abwägung)

Hinweise: Ines, Kommissar Bader und Kommissarin Ebner sind erfundene Figuren; dass beide Ermittlungspersonen der Staatsanwaltschaft sind, ist eine Fallannahme (§ 152 Abs. 2 GVG: Landesverordnung). Mehr dazu: Folge 151 (Durchsuchung nach der StPO, Nachtzeit), Folge 221 (Beweisverwertungsverbote).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#GefahrImVerzug #Grundrechte #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(§§? \d+)\n(Abs\. \d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Art\.)\n(\d+) ", r"\1 \2\n", srt)
srt = re.sub(r" \n", "\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
for alt, neu in [("neunzehn Uhr", "19 Uhr"), ("fünfzehn Uhr", "15 Uhr"), ("sechs bis\neinundzwanzig Uhr", "6 bis\n21 Uhr"),
                 ("hunderteinundfünfzig.", "151."), ("zweihunderteinundzwanzig.", "221.")]:
    assert alt in srt, alt
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n|Abs\.\n|Art\.\n|Paragraf", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Bereitschaftsdienst Richter", "Gefahr im Verzug Durchsuchung", "Art. 13 II GG"]
                         if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
