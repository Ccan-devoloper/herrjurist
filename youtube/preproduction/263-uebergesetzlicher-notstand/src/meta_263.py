"""Nachbearbeitung der Upload-Texte für Folge 263 (nach meta_189.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung (präzisiert, siehe RECHTSSTAND.md),
Fall, Inhalt, Normen, Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen, Sprecher).
Aufruf: python3 meta_263.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Weiche 7 – einer oder fünf?"),
       (T("tb"), "Tatbestand: Totschlag, § 212 StGB"),
       (T("p34"), "§ 34 StGB im Wortlaut"),
       (T("zahl"), "Leben gegen Leben: nicht abwägbar (BVerfGE 115, 118)"),
       (T("p35"), "§ 35 StGB: nur nahestehende Personen"),
       (T("ueber"), "Übergesetzlicher entschuldigender Notstand: Herkunft"),
       (T("vor"), "Voraussetzungen"),
       (T("ans"), "Streit: Entschuldigung oder Strafausschließungsgrund?"),
       (T("gg"), "Gefahrengemeinschaft und Weichenstellerfall"),
       (T("lsg"), "Ergebnis je Ansicht"),
       (T("tipp"), "Klausurtipp: Prüfungsreihenfolge"),
       (T("sch"), "Schema und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Übergesetzlicher entschuldigender Notstand: Warum rechtfertigt § 34 StGB keine Abwägung Leben gegen Leben – und wann kann der Täter trotzdem entschuldigt sein? Mit BVerfGE 115, 118.

Der Fall: Ein führerloser Güterzug rollt auf einen Bautrupp mit fünf Arbeitern zu, die nicht zu warnen sind. Die Stellwerksmitarbeiterin kann nur eine Weiche umstellen – auf ein Nebengleis, wo ein einzelner Arbeiter steht. Sie stellt um; die fünf überleben, der eine stirbt. Totschlag?

Inhalt:
– Tatbestand: Totschlag (§ 212 StGB) und Vorsatz
– § 34 StGB im Wortlaut: Notstandslage, Notstandshandlung, „wesentlich überwiegt“
– Leben gegen Leben: nach herrschender Meinung nicht abwägbar, auch nicht nach der Zahl
– BVerfGE 115, 118 (Luftsicherheitsgesetz): „Jedes menschliche Leben ist als solches gleich wertvoll“ (Rn. 85), Tötung als Mittel zur Rettung anderer (Rn. 124), strafrechtliche Bewertung offengelassen (Rn. 130)
– § 35 StGB im Wortlaut: nur Gefahr für sich, Angehörige oder nahestehende Personen
– Übergesetzlicher entschuldigender Notstand: Herkunft aus den Strafverfahren der Nachkriegszeit, Voraussetzungen
– Streit: ungeschriebener Entschuldigungsgrund (wohl herrschende Lehre) oder persönlicher Strafausschließungsgrund (OGH für die Britische Zone)
– Gefahrengemeinschaft und Weichenstellerfall: Darf die Gefahr auf Unbeteiligte umgelenkt werden?
– Ergebnis je Ansicht, Klausurtipp zur Prüfungsreihenfolge, Schema und Merksatz

Normen: §§ 34, 35, 212, 213 StGB; Art. 1 Abs. 1 GG; §§ 26, 27, 32 StGB

Rechtsprechung:
– BVerfG, Urt. v. 15.2.2006 – 1 BvR 357/05 (BVerfGE 115, 118, Luftsicherheitsgesetz), Rn. 85, 124, 130
– OGH für die Britische Zone, OGHSt 1, 321 (Euthanasie-Ärzte; vom BVerfG in Rn. 130 zitiert)

Hinweise: Die Einordnung des übergesetzlichen entschuldigenden Notstands ist umstritten; die Ansichten sind im Video gekennzeichnet. Das ganze § 34-Schema zeigt das Video „Rechtfertigender Notstand § 34 StGB: Schema mit Berghütten-Fall“, das Urteil selbst das Video „Luftsicherheitsgesetz: Darf der Staat ein Flugzeug abschießen?“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Strafrecht #Notstand #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
for muster, ersatz in [(r"sechs Uhr vierzig", "6:40 Uhr"), (r"Ende zwanzig", "Ende 20"), (r"Gleis eins", "Gleis 1"),
                       (r"fünf(\s)Arbeiter", r"5\1Arbeiter"), (r"Weiche sieben", "Weiche 7"), (r"Die fünf bleiben", "Die 5 bleiben"),
                       (r"einer oder fünf", "einer oder 5"), (r"um fünf zu retten", "um 5 zu retten"),
                       (r"Fünf Leben gegen eines", "5 Leben gegen eines"), (r"eins gegen fünf", "1 gegen 5"),
                       (r"Abs\. 1 Grundgesetz", "Abs. 1 GG"), (r"Eins, Tatbestand", "1. Tatbestand"),
                       (r"Zwei, Rechtswidrigkeit", "2. Rechtswidrigkeit"), (r"Drei, Schuld", "3. Schuld"),
                       (r"Vier, das Ergebnis", "4. das Ergebnis")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
srt = srt.replace("\nNordmann: ", "\nHerr Nordmann: ").replace("\nSeefeld: ", "\nFrau Seefeld: ")
assert not re.search(r"§\n", srt), "Untertitel prüfen"
for w in ("fünf ", "Paragraf", "hundert", "zwanzig", "sieben", "Artikel"):
    assert w not in srt, f"Zahlwort im Untertitel: {w}"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
