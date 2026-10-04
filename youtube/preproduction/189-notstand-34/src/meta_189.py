"""Nachbearbeitung der Upload-Texte für Folge 189 (nach meta_186.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen, Paragrafen, Sprecher).
Aufruf: python3 meta_189.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Wettersturz, Berghütte, aufgebrochene Tür"),
       (T("tb"), "Tatbestand: §§ 303, 123 StGB"),
       (T("p34"), "§ 34 StGB im Wortlaut"),
       (T("lage"), "1. Notstandslage: gegenwärtige Gefahr"),
       (T("handl"), "2. Notstandshandlung: geeignet und erforderlich"),
       (T("abwaeg"), "3. Interessenabwägung: wesentlich überwiegen"),
       (T("angem"), "4. Angemessenheit und 5. subjektives Element"),
       (T("bgb"), "§ 904 BGB: Aggressivnotstand und Schadensersatz"),
       (T("p228"), "§ 228 BGB: Defensivnotstand und Vorrang"),
       (T("p32"), "Abgrenzung: Notwehr § 32, entschuldigender Notstand § 35"),
       (T("lsg"), "Lösung des Falls"),
       (T("tipp"), "Klausurtipp: spezielle Notstände zuerst"),
       (T("sch"), "Schema § 34 StGB und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Rechtfertigender Notstand § 34 StGB: gegenwärtige Gefahr, wesentlich überwiegendes Interesse – und das Verhältnis zu §§ 228, 904 BGB am Berghütten-Fall.

Der Fall: Samstag, 17:40 Uhr, auf 2.150 m. Ein Wanderer gerät allein in einen Wettersturz – Schneesturm, −12 °C, kein Netz, bis ins Tal 3 Stunden. Die einzige Berghütte ist im Winter verschlossen, ein Schild verbietet das Betreten. Um nicht zu erfrieren, bricht er die Tür auf. Am Morgen fragt die Eigentümerin: Wer bezahlt das neue Schloss für 380 €?

Inhalt:
– Tatbestand kurz: Sachbeschädigung (§ 303 StGB) und Hausfriedensbruch (§ 123 StGB)
– § 34 StGB im Wortlaut und das Prüfungsschema
– 1. Notstandslage: Gefahr für ein Rechtsgut, gegenwärtig (BGH-Definition)
– 2. Notstandshandlung: nicht anders abwendbar – geeignet und erforderlich
– 3. Interessenabwägung: Das geschützte Interesse muss wesentlich überwiegen (Leben gegen Eigentum)
– 4. Angemessenheit nach § 34 S. 2 und 5. subjektives Rechtfertigungselement
– § 904 BGB im Wortlaut: Aggressivnotstand – gerechtfertigt, aber Schadensersatz (§ 904 S. 2)
– § 228 BGB im Wortlaut: Defensivnotstand, wenn die Gefahr von der Sache ausgeht
– Vorrang der zivilrechtlichen Notstände bei Eingriffen in Sachen (herrschende Meinung)
– Abgrenzung zu Notwehr (§ 32 StGB) und entschuldigendem Notstand (§ 35 StGB)
– Lösung, Klausurtipp zur Prüfungsreihenfolge, Schema und Merksatz

Normen: §§ 32, 34, 35, 123, 303 StGB; §§ 90a, 228, 904 BGB

Rechtsprechung:
– BGH, Urt. v. 25.3.2003 – 1 StR 483/02 (BGHSt 48, 255, „Haustyrann“): Rn. 21 (§ 34 StGB scheitert an der Interessenabwägung), Rn. 23 ff. (entschuldigender Notstand § 35), Rn. 27 (gegenwärtige Gefahr; dort zu § 35, gleicher Wortlaut wie § 34); Randnummern nach HRRS

Hinweise: Der Vorrang der §§ 228, 904 BGB vor § 34 StGB und die Bedeutung von § 34 S. 2 sind Lehrmeinungen (im Video gekennzeichnet). Die Notwehr vertieft das Video „Notwehr Schema § 32 StGB – so prüfst du die Notwehr“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Strafrecht #Notstand #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(S\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for muster, ersatz in [(r"siebzehn Uhr vierzig", "17:40 Uhr"), (r"zweitausendeinhundertfünfzig(\s)Metern", r"2.150\1Metern"),
                       (r"Mitte dreißig", "Mitte 30"), (r"minus zwölf Grad", "−12 °C"), (r"dreihundertachtzig(\s)Euro", r"380\1Euro"),
                       (r"drei(\s)Stunden", r"3\1Stunden")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
srt = srt.replace("B.G.B.", "BGB").replace("BGB..", "BGB.")
srt = srt.replace("\nMoser: ", "\nFrau Moser: ")
for alt in ("des §§ 34", "dem §§ 34"):                      # „des/dem Paragrafen vierunddreißig“ = ein Paragraf
    assert alt in srt, alt
    srt = srt.replace(alt, alt.replace("§§", "§"))
assert not re.search(r"§\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "Paragraf" not in srt and "zwölf" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
