"""Nachbearbeitung der Upload-Texte für Folge 151 (nach tools/youtube_metadaten.py, nichts dort geändert; Muster meta_148.py):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung, Hinweisen und Lizenzzeile;
Zahlen, Uhrzeiten und Paragrafen in den Untertiteln als Ziffern (auch über Zeilen- und Untertitelgrenzen).
Aufruf: python3 meta_151.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Polizei klingelt nachts ohne Beschluss"),
       (T("weiss"), "Rückblick: Anzeige um 14 Uhr, kein Beschluss beantragt"),
       (T("sv"), "Sachverhalt und Art. 13 GG: Richtervorbehalt"),
       (T("p102"), "Ermächtigungsgrundlage: § 102 und § 103 StPO"),
       (T("p105"), "Anordnungskompetenz: § 105 StPO"),
       (T("bverfg"), "Gefahr im Verzug: BVerfGE 103, 142"),
       (T("selbst"), "Selbst herbeigeführte Eile, Bereitschaftsdienst"),
       (T("p104"), "Nachtzeit: § 104 StPO"),
       (T("loes"), "Lösung"),
       (T("bvv"), "Beweisverwertungsverbot?"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Durchsuchung StPO: Wann darf die Polizei in die Wohnung? §§ 102, 103, 105 StPO, Richtervorbehalt und Gefahr im Verzug nach BVerfGE 103, 142.

Der Fall: Dienstag, 23 Uhr. Ein Polizeikommissar klingelt bei Helene und will wegen „Gefahr im Verzug“ ohne Beschluss ihre Wohnung durchsuchen – Verdacht: Verkauf gestohlener Fahrräder. Dabei lag die Anzeige schon seit 14 Uhr vor, und der richterliche Bereitschaftsdienst war bis 21 Uhr erreichbar. Durfte er durchsuchen – und darf das gefundene E-Bike als Beweis verwertet werden?

Inhalt:
– Art. 13 GG: Unverletzlichkeit der Wohnung und Richtervorbehalt
– § 102 StPO: Durchsuchung beim Verdächtigen (Anfangsverdacht, Auffindevermutung); § 103 StPO: strengere Voraussetzungen bei Dritten
– § 105 Abs. 1 S. 1 StPO: Anordnung durch den Richter, bei Gefahr im Verzug durch Staatsanwaltschaft und Ermittlungspersonen
– Gefahr im Verzug nach BVerfGE 103, 142: eng auszulegen, Tatsachen statt Vermutungen, Dokumentation, volle gerichtliche Kontrolle, keine selbst herbeigeführte Eile
– Richterlicher Bereitschaftsdienst: tagsüber 6 bis 21 Uhr (BVerfGE 151, 67)
– Nachtzeit nach § 104 StPO: 21 bis 6 Uhr
– Lösung und Beweisverwertungsverbot bei bewusster oder grober Missachtung des Richtervorbehalts
– Klausurtipp, Prüfschema, Merksatz

Normen: Art. 13 GG; §§ 102, 103, 104, 105 StPO; § 152 GVG

Rechtsprechung:
– BVerfG, Urt. v. 20.2.2001 – 2 BvR 1444/00, BVerfGE 103, 142, Rn. 31, 32, 34, 38–40, 44, 54
– BVerfG, Beschl. v. 12.3.2019 – 2 BvR 675/14, BVerfGE 151, 67, Rn. 58, 62
– BGH, Urt. v. 18.4.2007 – 5 StR 546/06, BGHSt 51, 285, Rn. 17, 20, 24, 26, 28 f.
– BGH, Urt. v. 6.10.2016 – 2 StR 46/15, BGHSt 61, 266, Rn. 24, 26
– BGH, Beschl. v. 6.9.2023 – StB 40/23, Rn. 11, 14

Hinweise: Der Fall ist ein vereinfachter Übungsfall. Ob ein Beweisverwertungsverbot besteht, entscheidet das Gericht nach Abwägung im Einzelfall. Welche Beamten Ermittlungspersonen der Staatsanwaltschaft sind, regeln die Länder (§ 152 Abs. 2 GVG). Seit 1.7.2021 gilt die Nachtzeit des § 104 StPO ganzjährig von 21 bis 6 Uhr.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (StPO zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#DurchsuchungStPO #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
W = r"(\s+(?:\d+\n[^\n]*-->[^\n]*\n(?:[^\n:]{1,12}: )?)?)"   # Leerraum, auch über eine Untertitelgrenze
ERSATZ = [("Paragraf hundertzwei", "§ 102"), ("Paragraf hundertdrei", "§ 103"), ("Paragraf hundertvier", "§ 104"),
          ("Paragraf hundertfünf", "§ 105"), ("oder hundertdrei", "oder § 103"),
          ("Absatz eins Satz eins", "Abs. 1 S. 1"), ("Artikel dreizehn", "Artikel 13"),
          ("dreiundzwanzig Uhr", "23 Uhr"), ("vierzehn Uhr", "14 Uhr"), ("einundzwanzig Uhr", "21 Uhr"),
          ("sechs bis einundzwanzig Uhr", "6 bis 21 Uhr"), ("einundzwanzig bis sechs Uhr", "21 bis 6 Uhr"),
          ("sieben teure", "7 teure"), ("drei Wochen", "3 Wochen"), ("sieben Rädern", "7 Rädern"),
          ("zweitausendeins", "2001"), ("zweitausendneunzehn", "2019"), ("zweitausendsieben", "2007")]
for alt, neu in sorted(ERSATZ, key=lambda e: -len(e[0])):
    teile = alt.split(" "); ziel = neu.split(" ")
    muster = W.join(re.escape(t) for t in teile)
    def ers(m, ziel=ziel, n=len(teile)):
        if len(ziel) == n:
            return "".join(ziel[i] + (m.group(i + 1) if i < n - 1 else "") for i in range(n))
        return " ".join(ziel) + "".join(m.group(i + 1) for i in range(n - 1) if "\n" in m.group(i + 1))
    srt = re.sub(muster, ers, srt)
srt = re.sub(r"[ \t]+\n", "\n", srt)
srt = re.sub(r"\n[ \t]+", "\n", srt)
for w in ("Paragraf", "hundert", "zweitausend", "zwanzig", "vierzehn"):
    assert w not in srt, re.findall(rf".*{w}.*", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
