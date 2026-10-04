"""Nachbearbeitung der Upload-Texte für Folge 165 (nach meta_162.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn./Seite,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Aussprachehilfen zurück in die normale Schreibung: zerta → certa,
präwia → praevia, pöna → poena, Merk-mal → Merkmal; Paragrafen zusammenhalten).
Aufruf: python3 meta_165.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Tretboot geliehen, ohne zu fragen – strafbar?"),
       (T("dieb"), "Diebstahl und § 248b StGB: kein Paragraf passt"),
       (T("a103"), "Art. 103 Abs. 2 GG und § 1 StGB: keine Strafe ohne Gesetz"),
       (T("vier"), "Die vier Gewährleistungen"),
       (T("sa"), "lex scripta: kein Gewohnheitsrecht"),
       (T("ca"), "lex certa: das Bestimmtheitsgebot"),
       (T("sta"), "lex stricta: Analogieverbot"),
       (T("pa"), "lex praevia: Rückwirkungsverbot"),
       (T("best"), "Untreue-Beschluss: Präzisierungsgebot und Verschleifungsverbot"),
       (T("sitz"), "Sitzblockaden-Beschluss: vergeistigter Gewaltbegriff"),
       (T("zug"), "Nur zulasten: Analogie zugunsten, § 3 OWiG"),
       (T("loes"), "Lösung: Pech für den Staat"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfraster"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Analogieverbot Strafrecht nach Art. 103 II GG und § 1 StGB: Warum strafbegründende Analogie verboten ist und was das Bestimmtheitsgebot verlangt.

Der Fall: Wieland bindet am öffentlichen Steg das Tretboot von Hartwin los, fährt eine Stunde über den See und bringt es unbeschädigt zurück. Verwerflich – aber passt ein Paragraf genau? Und wenn nicht: Pech für den Staat?

Inhalt:
– Diebstahl (§ 242 StGB) und unbefugter Gebrauch (§ 248b StGB): warum kein Paragraf passt
– Art. 103 Abs. 2 GG und § 1 StGB im Wortlaut: nullum crimen, nulla poena sine lege
– die zwei Zwecke: Der Gesetzgeber entscheidet, jeder soll vorhersehen können, was verboten ist
– die vier Gewährleistungen: lex scripta (kein Gewohnheitsrecht), lex certa (Bestimmtheitsgebot), lex stricta (Analogieverbot), lex praevia (Rückwirkungsverbot, § 2 Abs. 1 StGB)
– Schwerpunkt Bestimmtheit: Untreue-Beschluss (Generalklauseln, Präzisierungsgebot, Verbot der Verschleifung) und Sitzblockaden-Beschluss (vergeistigter Gewaltbegriff)
– nur zulasten: Analogie zugunsten des Täters; § 3 OWiG
– Lösung des Falls, Klausurtipp, Prüfraster, Merksatz

Normen: Art. 103 Abs. 2 GG; §§ 1, 2 Abs. 1 StGB; § 242 Abs. 1 StGB; § 248b StGB; § 240 Abs. 1 StGB; § 266 StGB; § 3 OWiG

Rechtsprechung:
– BVerfG, Beschl. v. 23.6.2010 – 2 BvR 2559/08 u. a. (BVerfGE 126, 170), Rn. 68–80 (Bestimmtheitsgebot, Präzisierungsgebot, Verschleifung), Rn. 84, 152–158
– BVerfG, Beschl. v. 10.1.1995 – 1 BvR 718/89 u. a. (BVerfGE 92, 1, 13 ff.) (Sitzblockaden)
– BGH, Beschl. v. 27.5.2020 – 1 StR 118/20, Rn. 19–21 (§ 306e StGB analog; Analogie zugunsten des Täters)
– BGH, Beschl. v. 17.12.2014 – 3 StR 484/14, Rn. 6 (Gebrauchsanmaßung ist kein Diebstahl)

Hinweise: Wieland und Hartwin sind erfundene Figuren. Wie die Analogie funktioniert, erklärt die Folge zur Analogie; die Wortlautgrenze im Strafrecht die Folgen zu den Auslegungsmethoden und zur Unfallflucht.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Analogieverbot #Bestimmtheitsgebot #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for a, b in (("zerta", "certa"), ("präwia", "praevia"), ("pöna", "poena"), ("Merk-mal", "Merkmal")):
    srt = srt.replace(a, b)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Art\.)\n(\d+) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|zerta|präwia|pöna|Merk-mal", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
