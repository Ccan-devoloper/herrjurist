"""Nachbearbeitung der Upload-Texte für Folge 134 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Lizenzzeile,
zusätzliche Tags; Untertitel: verbliebene Zahlwörter (63, § 185–187) in Ziffern. Aufruf: python3 meta_134.py <upload-ordner>"""
import json, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Chatgruppe „Nachbarn Ahornweg“ – mit Sachverhalt"),
       (T("schritt1"), "1. Werturteil oder Tatsachenbehauptung? Beweisbarkeit und Kontext"),
       (T("p185"), "2. Beleidigung, § 185 StGB: Kundgabe der Missachtung"),
       (T("rw185"), "§ 193 StGB und Abwägung mit Art. 5 Abs. 1 GG"),
       (T("p186"), "3. Üble Nachrede, § 186 StGB"),
       (T("erweis"), "„Nicht erweislich wahr“: objektive Bedingung der Strafbarkeit"),
       (T("do1"), "§ 193 bei Tatsachen: Sorgfaltspflicht"),
       (T("p187"), "4. Verleumdung, § 187 StGB (Variante)"),
       (T("quali"), "Qualifikation „öffentlich“ und Strafantrag, § 194 StGB"),
       (T("tab"), "Abgrenzungstabelle und Ergebnis"),
       (T("tipp"), "Klausurtipp: Schmähkritik eng"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Beleidigung, üble Nachrede, Verleumdung: Wie grenzt man Werturteil und Tatsachenbehauptung ab und was unterscheidet §§ 185, 186, 187 StGB?

Der Fall: In der Chatgruppe „Nachbarn Ahornweg“ mit 63 Mitgliedern schreibt Hannelore über Henner: „Henner ist ein Idiot.“ Dörte legt nach: „Henner schlägt seine Kinder.“ Belege hat sie keine, und ob es stimmt, lässt sich nicht klären. Variante: Dörte weiß, dass es nicht stimmt. Wer hat sich strafbar gemacht?

Inhalt:
– Werturteil oder Tatsachenbehauptung: Stellungnahme und Dafürhalten oder Beziehung zur Wirklichkeit; Kriterium Beweisbarkeit; Sinn nach Wortlaut, Kontext und Begleitumständen
– Beleidigung, § 185 StGB: Wortlaut, Kundgabe der Missachtung, Werturteile gegenüber jedem, Tatsachen nur gegenüber dem Betroffenen
– Wahrnehmung berechtigter Interessen, § 193 StGB: Abwägung mit der Meinungsfreiheit (Art. 5 Abs. 1 GG)
– Üble Nachrede, § 186 StGB: ehrenrührige Tatsache gegenüber Dritten, „nicht erweislich wahr“, Sorgfaltspflicht bei § 193
– Verleumdung, § 187 StGB: unwahre Tatsache wider besseres Wissen
– Qualifikation (öffentlich, in einer Versammlung, durch Verbreiten eines Inhalts) und Strafantrag (§ 194 Abs. 1 StGB)
– Abgrenzungstabelle, Klausurtipp zur Schmähkritik, Klausurschema, Merksatz

Normen: §§ 185, 186, 187, 193, 194 StGB; Art. 5 Abs. 1 GG

Rechtsprechung:
– BVerfG, Beschl. v. 13.4.1994 – 1 BvR 23/94, BVerfGE 90, 241, Rn. 26–28
– BVerfG, Beschl. v. 10.10.1995 – 1 BvR 1476/91 u. a., BVerfGE 93, 266, Rn. 120
– BVerfG, Beschl. v. 10.11.1998 – 1 BvR 1531/96, BVerfGE 99, 185, Rn. 52, 55
– BVerfG, Beschl. v. 28.6.2016 – 1 BvR 3388/14, Rn. 17, 20 f.
– BVerfG, Beschl. v. 19.5.2020 – 1 BvR 2397/19, Rn. 15, 19, 26, 29, 33, 34
– BGH, Urt. v. 27.3.2009 – 2 StR 302/08, Rn. 26
– OLG Hamm, Beschl. v. 10.2.2026 – 5 ORs 94/25, Rn. 15
(Randnummern bei BVerfGE 90, 93, 99 nach „Das Fallrecht“, Universität Bern)

Kapitel:
{kapitel}

Der Fall und die Personen sind ausgedacht. Ob eine geschlossene Chatgruppe „öffentlich“ ist, hängt vom Einzelfall ab und bleibt im Video offen. Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Strafrecht #Beleidigung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for a, b in (("dreiundsechzig", "63"), ("hundertfünfundachtzig", "§ 185"), ("hundertsechsundachtzig", "§ 186"),
             ("hundertsiebenundachtzig", "§ 187")):
    srt = srt.replace(a, b)
for w in ("hundert", "sechzig"):
    assert w not in srt, w
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ("üble Nachrede § 186", "Werturteil Tatsachenbehauptung", "Schmähkritik", "§ 194 StGB Strafantrag"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
