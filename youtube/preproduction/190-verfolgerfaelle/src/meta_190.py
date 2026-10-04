"""Nachbearbeitung der Upload-Texte für Folge 190 (nach meta_187.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen).
Aufruf: python3 meta_190.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Kontrolleur stürzt bei der Verfolgung, Sachverhalt"),
       (T("problem"), "Das Problem: psychisch vermittelte Kausalität"),
       (T("norm"), "§ 823 Abs. 1 BGB und Äquivalenz"),
       (T("formel"), "Die Herausforderungsformel des BGH"),
       (T("mot"), "Im Fall: Motiv, Verhältnis, gesteigertes Risiko"),
       (T("gegen"), "Gegenbeispiele: allgemeines Lebensrisiko"),
       (T("mit"), "Mitverschulden, § 254 Abs. 1 BGB"),
       (T("erg"), "Ergebnis und Ausblick: Retterfälle"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Verfolgerfälle (§§ 823 I, 254 BGB): Wann muss der flüchtende Fahrgast für den Sturz des Kontrolleurs haften? Die Herausforderungsformel des BGH (BGHZ 57, 25).

Der Fall: Kontrolleur Wendelin trifft im U-Bahnhof den Fahrgast Anselm ohne gültigen Fahrschein und bittet um den Ausweis. Anselm läuft zur Treppe, Wendelin rennt hinterher, zwei Stufen auf einmal, und stürzt. Anselm hat ihn nicht berührt. Muss er trotzdem für den gebrochenen Arm aufkommen?

Inhalt:
– Das Problem: psychisch vermittelte Kausalität, der Verfolger entscheidet sich selbst
– § 823 Abs. 1 BGB im Wortlaut, haftungsbegründende Kausalität: Äquivalenz und wertende Zurechnung
– Die Herausforderungsformel: billigenswertes Motiv, Risiko nicht außer Verhältnis zum Zweck, gesteigertes Verfolgungsrisiko verwirklicht
– Verschulden des Fliehenden
– Gegenbeispiele: allgemeines Lebensrisiko, gänzlich unangemessene Selbstgefährdung
– Mitverschulden nach § 254 Abs. 1 BGB im Wortlaut
– Ausblick: Retterfälle, Strafrecht, Klausurtipp, Prüfschema, Merksatz

Normen: § 823 Abs. 1 BGB; § 254 Abs. 1 BGB; § 265a StGB (nur erwähnt)

Rechtsprechung:
– BGH, Urt. v. 13.7.1971 – VI ZR 125/70, BGHZ 57, 25 (Verfolgerfall: Kontrolleur stürzt auf der Bahnhofstreppe)
– BGH, Urt. v. 31.1.2012 – VI ZR 43/11, Rn. 8, 9, 11, 14, 20 (Herausforderungsformel, Mittel-Zweck-Relation, Verschulden)
– BGH, Urt. v. 12.3.1996 – VI ZR 12/95, BGHZ 132, 164 (allgemeines Lebensrisiko, Mitverschulden des Verfolgers)
– BGH, Beschl. v. 5.5.2021 – 4 StR 19/20 (Strafrecht: Zurechnung bei Rettern)

Hinweise: Der Fall im Video ist dem Verfolgerfall nachgebildet; im Original fiel der Kontrolleur über den gestürzten Fahrgast, die Gerichte sprachen ihm zwei Drittel seines Schadens zu. Das allgemeine Schema zu § 823 Abs. 1 BGB zeigt das Video zum Deliktsrecht.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Verfolgerfälle #Deliktsrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
for a, b in [("Neunzehnhunderteinundsiebzig", "1971")]:
    assert a in srt, a
    srt = srt.replace(a, b)
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "tausend" not in srt and "Römisch" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
