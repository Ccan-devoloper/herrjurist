"""Nachbearbeitung der Upload-Texte für Folge 271 (nach meta_231.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Literatur,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt).
Aufruf: python3 meta_271.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Schüsse durch die Haustür"),
       (T("sek"), "Draußen: ein Spezialeinsatzkommando"),
       (T("lg"), "Landgericht und Bundesgerichtshof"),
       (T("tb"), "Totschlag, § 212 StGB"),
       (T("rw"), "§ 32 StGB: Notwehr gegen die Polizei?"),
       (T("vorst"), "Die vorgestellte Notwehrlage"),
       (T("erf"), "Erforderlich? Der Warnschuss"),
       (T("eti"), "Erlaubnistatbestandsirrtum, § 16 StGB"),
       (T("fahr"), "Fahrlässige Tötung, § 222 StGB"),
       (T("kritik"), "Kritik"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Hells-Angels-Fall: Schüsse durch die Tür auf das SEK – durfte er sich eine Notwehrlage vorstellen (§§ 16, 32 StGB) und musste er zuerst warnen?

Der Fall: Frühmorgens knackt es an der Haustür. Elmar, ein führendes Mitglied eines Rockerclubs, glaubt an einen Überfall verfeindeter Rocker. Er ruft, niemand reagiert, und er schießt zweimal durch die geschlossene Tür. Draußen steht ein Spezialeinsatzkommando, das sein Haus durchsuchen soll; ein Polizeibeamter wird tödlich getroffen. Das Landgericht verurteilt wegen Totschlags, der Bundesgerichtshof spricht frei.

Inhalt:
– Totschlag, § 212 StGB: Vorsatz und unbeachtlicher Irrtum über die Person
– § 32 Abs. 2 StGB im Wortlaut: Notwehr gegen einen Polizeieinsatz nur, wenn er rechtswidrig war (vom BGH offengelassen)
– Die vorgestellte Notwehrlage: Überfall der Rivalen
– Erforderlichkeit aus seiner Sicht: Warnschuss nur, wenn er den Angriff beenden würde
– Erlaubnistatbestandsirrtum: § 16 Abs. 1 StGB im Wortlaut, entsprechend angewandt – die Vorsatzschuld entfällt
– Fahrlässige Tötung, § 222 StGB: Irrtum unvermeidbar, Freispruch
– Kritik am Urteil
– Klausurtipp (erst echte Notwehr, dann Irrtum; sonst § 17), Klausurschema, Merksatz

Normen: §§ 16 Abs. 1, 17, 32, 212, 222 StGB.

Rechtsprechung:
– BGH, Urt. v. 2.11.2011 – 2 StR 375/11, NStZ 2012, 272 (Randnummern nach der amtlichen Fassung: Rn. 19 f. Notwehr gegen Polizeieinsatz offen; Rn. 21–24 Erlaubnistatbestandsirrtum, Warnschuss; Rn. 25 f. keine Fahrlässigkeit, Freispruch)
– BGH, Pressemitteilung Nr. 174/2011 vom 3.11.2011
– Vorinstanz: LG Koblenz, Urt. v. 28.2.2011 – 3 Ks 2090 Js 16853/10

Literatur: Rotsch, Entscheidungsbesprechung, ZJS 2012, 109.

Hinweise: Elmar und Gabi sind erfundene Figuren; der Ablauf folgt den Feststellungen im Urteil. Mehr dazu: Folge 231 (Erlaubnistatbestandsirrtum – alle Schuldtheorien), Folge 214 (Notwehr bei Bagatellen), Folge 227 (Notwehrprovokation).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#HellsAngelsFall #Erlaubnistatbestandsirrtum #StrafrechtAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Paragraf", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Hells-Angels-Fall", "Warnschuss Notwehr", "fahrlässige Tötung 222"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
