"""Nachbearbeitung der Upload-Texte für Folge 210 (nach meta_195.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen und Beträge in Ziffern, Normen, Sprecher).
Aufruf: python3 meta_210.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: zwei Beklagte, 20.000 €"),
       (T("klage"), "Das Urteil: B1 verliert, B2 gewinnt"),
       (T("problem"), "Das Problem: drei Parteien, §§ 59, 61 ZPO"),
       (T("p100"), "Hilft § 100 ZPO?"),
       (T("idee"), "Grundgedanke und fiktiver Streitwert"),
       (T("tab"), "Die Tabelle: Gerichtskosten"),
       (T("kb"), "Die Tabelle: außergerichtliche Kosten"),
       (T("jede"), "Probe"),
       (T("tenor"), "Der Kostentenor"),
       (T("tipp"), "Klausurtipp: Tabelle auf dem Konzeptpapier"),
       (T("sch"), "Schema Baumbachsche Formel"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Baumbachsche Kostenformel Schritt für Schritt: Wie du Gerichtskosten und außergerichtliche Kosten verteilst, wenn Streitgenossen unterschiedlich gewinnen – mit Tabelle, Probe und Kostentenor (§§ 59, 61, 91, 92, 100 ZPO).

Der Fall: Zwei Beklagte werden als Gesamtschuldner auf 20.000 Euro verklagt. Der eine verliert voll, gegen die andere wird die Klage abgewiesen. Wer trägt jetzt welche Kosten?

Inhalt:
– Das Problem: §§ 91, 92 ZPO denken in zwei Parteien; Streitgenossen (§ 59 ZPO) stehen dem Gegner als Einzelne gegenüber (§ 61 ZPO, Wortlaut)
– § 100 Abs. 1 und 4 ZPO im Wortlaut: Kopfteile und Gesamtschuldner – und warum das hier nicht passt
– Grundgedanke: Gerichtskosten und außergerichtliche Kosten getrennt; fiktiver Streitwert = Summe aller Prozessrechtsverhältnisse (2 × 20.000 € = 40.000 €), echter Streitwert bleibt 20.000 €
– Die Tabelle: a) Gerichtskosten ½ / ½, b) außergerichtliche Kosten der Klägerin, c) Kosten des Beklagten zu 1, d) Kosten der Beklagten zu 2 – mit Probe
– Der Kostentenor: „Die Gerichtskosten tragen die Klägerin und der Beklagte zu 1 je zur Hälfte. Die außergerichtlichen Kosten der Klägerin trägt der Beklagte zu 1 zur Hälfte. Die Klägerin trägt die außergerichtlichen Kosten der Beklagten zu 2. Im Übrigen tragen die Parteien ihre außergerichtlichen Kosten selbst.“
– Klausurtipp, Schema, Merksatz

Normen: §§ 59, 61, 91 Abs. 1 S. 1, 92 Abs. 1 S. 1, 100 Abs. 1, 4 ZPO; §§ 421, 427, 488 BGB; §§ 23 Nr. 1, 71 Abs. 1 GVG

Rechtsprechung:
– BGH, Beschl. v. 21.1.2025 – XI ZB 26/23, Rn. 23 (fiktiver Streitwert je Kostenmasse; Aufbau des Kostentenors)
– BGH, Beschl. v. 16.7.2015 – IX ZR 136/14, Rn. 5 (gegen Gesamtschuldner gerichtete gleiche Ansprüche: keine Addition)
– BGH, Beschl. v. 30.4.2003 – VIII ZB 100/02 (Kosten des obsiegenden Streitgenossen trägt der Kläger auch bei vollständiger Verurteilung des anderen; gemeinsamer Anwalt)

Hinweise: Die Baumbachsche Formel ist eine Rechenmethode der Praxis, keine gesetzliche Regel. Im Beispiel hat jede Partei einen eigenen Anwalt. Wie du die Kostenquote zwischen zwei Parteien bildest, zeigt das Video „Kostenquote in 5 Minuten: §§ 91, 92 ZPO“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#BaumbachscheFormel #2Examen #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)


def ersetze(muster, ersatz):
    """Zahlwort → Ziffern, auch über einen Zeilenumbruch hinweg (Umbruch bleibt nach dem Ersatz erhalten)."""
    global srt
    rx = re.compile(muster.replace(" ", r"(\s)"))
    srt, n = rx.subn(lambda m: ersatz + ("\n" if "\n" in m.group(0) else ""), srt)
    return n


for muster, ersatz in [("zwanzigtausend Euro", "20.000 Euro"), ("Zwanzigtausend", "20.000"), ("zwanzigtausend", "20.000"),
                       ("vierzigtausend Euro", "40.000 Euro"), ("vierzigtausend", "40.000"),
                       ("Zwanzig von vierzig", "20 von 40"), ("zu eins", "zu 1"), ("zu zwei", "zu 2")]:
    assert ersetze(muster, ersatz), muster
srt = re.sub(r"\n +", "\n", srt)
for alt, neu in [("\nEschenbach: ", "\nFrau Eschenbach: "), ("\nKreutzer: ", "\nFrau Kreutzer: ")]:
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n|Abs\.\n|Art\.\n(?=\S)", srt), "Untertitel prüfen"
assert not re.search(r"tausend|hundert|zwanzig|vierzig|Paragraf", srt), "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
