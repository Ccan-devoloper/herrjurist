"""Nachbearbeitung der Upload-Texte für Folge 207 (nach meta_203.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung (Rn. nach der
amtlichen Fassung, wo vorhanden), Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen und Paragrafen als Ziffern).
Aufruf: python3 meta_207.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: der „Designer-Sessel“ vom Garagenverkauf"),
       (T("p263"), "§ 263 Abs. 1 StGB: Vermögen beschädigt"),
       (T("saldo"), "Die Gesamtsaldierung"),
       (T("rech"), "Im Fall: 300 € − 300 € = 0 €"),
       (T("folge"), "Kein Schaden trotz Täuschung"),
       (T("indiv"), "Individueller Schadenseinschlag"),
       (T("eing"), "Eingehungs- und Gefährdungsschaden"),
       (T("gegen"), "Gegenfall: nur 120 € wert"),
       (T("versuch"), "Versuch, § 263 Abs. 2 StGB"),
       (T("tipp"), "Klausurtipp: Schaden beziffern"),
       (T("sch"), "Prüfschema Vermögensschaden"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Gesamtsaldierung einfach erklärt: Wie ermittelt man den Vermögensschaden beim Betrug nach § 263 StGB – und warum ist Täuschung allein kein Schaden?

Der Fall: Gundula kauft beim Garagenverkauf einen „Designer-Sessel“ für 300 €. Alwin versichert ihr, es sei ein echtes Designerstück – in Wahrheit ist es ein Nachbau. Eine Gutachterin stellt fest: Der Nachbau ist genau 300 € wert. Ist ihr Vermögen beschädigt?

Inhalt:
– § 263 Abs. 1 StGB im Wortlaut: das Merkmal „Vermögen eines anderen beschädigt“
– Vermögen nach der Rechtsprechung: die Summe der geldwerten Güter, wirtschaftlich betrachtet
– Gesamtsaldierung: Vermögen unmittelbar vor und nach der Verfügung, die Gegenleistung gleicht aus
– Im Fall: 300 € − 300 € = 0 € – kein Schaden trotz Täuschung (Melkmaschinen-Fall; Nachbau statt Original)
– Korrekturen: individueller Schadenseinschlag (Zweckverfehlung, Zwang zu Folgemaßnahmen, fehlende Mittel), Eingehungsschaden, Gefährdungsschaden
– Gegenfall: Nachbau nur 120 € wert – Schaden 180 €
– Versuch nach § 263 Abs. 2 StGB
– Klausurtipp: den Schaden immer beziffern, Prüfschema und Merksatz

Normen: § 263 Abs. 1, 2 StGB; § 22 StGB

Rechtsprechung:
– BGH, Beschl. v. 6.4.2018 – 1 StR 13/18, Rn. 8 (Gesamtsaldierung), Rn. 9 (Eingehungs- und Erfüllungsschaden)
– BGH, Beschl. v. 19.7.2023 – 2 StR 77/22, Rn. 8 (Gesamtsaldierung, Wert konkret festzustellen und zu beziffern)
– BGH, Beschl. v. 13.8.2025 – 2 StR 283/25, Rn. 10, 13 (Nachbau statt Original: Schaden regelmäßig nur, wenn die Sache objektiv den Preis nicht wert ist)
– BGH, Beschl. v. 16.8.1961 – 4 StR 166/61, BGHSt 16, 321 („Melkmaschine“: persönlicher Schadenseinschlag)
– BGH, Beschl. v. 12.6.2018 – 3 StR 171/17 (persönlicher Schadenseinschlag, st. Rspr.)
– BVerfG, Beschl. v. 23.6.2010 – 2 BvR 2559/08 u. a., BVerfGE 126, 170, Rn. 112, 136 f. (Bezifferung, Gefährdungsschaden)
– BVerfG, Beschl. v. 7.12.2011 – 2 BvR 2500/09 u. a., BVerfGE 130, 1, Rn. 174–176 (Gefährdungsschaden beim Betrug, Bezifferung)

Hinweise: Der Fall ist ein Übungsfall; Werte und Vorstellungen der Beteiligten sind Fallannahmen. Täuschung, Irrtum und Vermögensverfügung werden nur kurz festgestellt – das ganze Betrugsschema zeigt unsere Folge „Betrug § 263 Schema“. Wie ein Urteil ohne Wertfeststellung in der Revision scheitert, zeigt unsere Folge zur Sachrüge. Prüfungsschemata sind Klausurkonventionen.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Fluent Emoji (MIT), Phosphor (MIT), Tabler (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Strafrecht #Jura #Betrug
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
ERSATZ = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else []
for alt, neu in ERSATZ:
    n = srt.count(alt)
    assert n, alt
    srt = srt.replace(alt, neu)
for w in ("hundert", "Paragraf", "zweihundert"):
    assert w not in srt, f"Zahlwort im Untertitel: {w}"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Gesamtsaldierung", "individueller Schadenseinschlag", "Eingehungsbetrug",
                                     "Gefährdungsschaden"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen;", len(m["tags"]), "Tags")
