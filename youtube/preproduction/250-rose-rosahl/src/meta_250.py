"""Nachbearbeitung der Upload-Texte für Folge 250 (nach meta_247.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Seiten, Lehre, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt).
Aufruf: python3 meta_250.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Auftrag am Kanal"),
       (T("frage"), "Die Frage"),
       (T("aufbau"), "Der Täter: error in persona, § 16 StGB"),
       (T("p26"), "Die Anstifterin: § 26 StGB"),
       (T("rose"), "Rose-Rosahl-Fall: Unbeachtlichkeitslehre"),
       (T("aberr"), "Aberratio-Lösung der Lehre"),
       (T("bgh"), "BGHSt 37, 214: Hoferben-Fall"),
       (T("erg"), "Ergebnis und Blutbad-Argument"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Rose-Rosahl-Fall: Ist der error in persona des Täters für den Anstifter nach § 26 StGB unbeachtlich oder eine aberratio ictus? Mit dem Hoferben-Fall (BGHSt 37, 214).

Der Fall: Eine Bauunternehmerin bittet ihren Bekannten, ihren Konkurrenten zu töten, und gibt ihm ein Foto. Am Abend wartet er am dunklen Kanalweg – und tötet einen Spaziergänger, den er für den Konkurrenten hält. Ist sie trotzdem Anstifterin zum Totschlag?

Inhalt:
– Der Täter: § 16 Abs. 1 Satz 1 StGB im Wortlaut; error in persona bei gleichwertigen Objekten unbeachtlich
– Die Anstifterin: § 26 StGB im Wortlaut; Haupttat, Bestimmen, doppelter Anstiftervorsatz
– Der Streit: Unbeachtlichkeitslehre (Rose-Rosahl, Preußisches Obertribunal 1859), Aberratio-Lösung der Lehre (versuchte Anstiftung nach § 30 Abs. 1, ggf. § 222 StGB), BGH im Hoferben-Fall (Abweichung in den Grenzen des nach allgemeiner Lebenserfahrung Vorhersehbaren)
– Ergebnis nach dem BGH und das Blutbad-Argument
– Klausurtipp, Klausurschema, Merksatz

Normen: §§ 16, 26, 30, 212, 222 StGB.

Rechtsprechung:
– Preußisches Obertribunal, Urt. v. 5.5.1859, GA 7 (1859), 322 (Rose-Rosahl-Fall; historischer Fall, Originaltext nicht online verfügbar)
– BGH, Urt. v. 25.10.1990 – 4 StR 371/90, BGHSt 37, 214, 216, 218 f. (Hoferben-Fall)
– BGH, Urt. v. 1.7.2021 – 3 StR 84/21, Rn. 13 (doppelter Anstiftervorsatz)

Literatur: Weber, Die Strafbarkeit des Anstifters bei einem error in persona des Angestifteten – Zum Hoferbenfall BGHSt 37, 214, StudZR 2005, 403 ff.

Hinweise: Edeltraud und Vinzenz sind erfundene Figuren eines Übungsfalls. Mordmerkmale bleiben im Übungsfall offen. Mehr zum Tatbestandsirrtum in Folge 068.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#RoseRosahl #StrafrechtAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
for alt, neu in [("Folge achtundsechzig", "Folge 68"), ("achtzehnhundertneunundfünfzig", "1859"),
                 ("hundertdreißig", "130")]:
    assert alt in srt, alt
    srt = srt.replace(alt, neu)
assert not re.search(r"achtundsechzig|neunundfünfzig|hundertdreißig", srt)
srt, n = re.subn(r"nach § 30\n\n(\d+\n[\d:,]+ --> [\d:,]+)\nAbs\. 1, und", r"nach § 30 Abs. 1,\n\n\1\nund", srt)
assert n == 1, "§ 30 Abs. 1 im Untertitel"
assert not re.search(r"§\n|Abs\.\n|Paragraf", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Rose-Rosahl", "error in persona", "Anstiftung"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
