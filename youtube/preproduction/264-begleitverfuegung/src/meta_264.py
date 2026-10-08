"""Nachbearbeitung der Upload-Texte für Folge 264 (nach meta_252.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, RiStBV, Hinweisen und Lizenzzeile;
Untertitel-Korrekturen (Daten und Beträge in Ziffern, Normangaben nicht über den Zeilenumbruch getrennt).
Aufruf: python3 meta_264.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: drei Monate Untersuchungshaft"),
       (T("akte"), "In der Akte: Einbruch, Haftbefehl, zweite Anzeige"),
       (T("frage"), "Die Frage und der Sachverhalt"),
       (T("wozu"), "Wozu die Begleitverfügung?"),
       (T("kopf"), "Kopf und I. Vermerk (§ 169a StPO)"),
       (T("e"), "II. Teileinstellung (§ 170 Abs. 2 StPO)"),
       (T("e4"), "II. Bescheid an den Anzeigenden (§ 171 StPO)"),
       (T("h"), "III. Haft: Fortdauerantrag"),
       (T("h121"), "III. Sechsmonatsfrist (§ 121 StPO)"),
       (T("pv"), "IV. Pflichtverteidigung (§ 140 StPO)"),
       (T("mi"), "V. Mitteilungen und Asservate"),
       (T("vi"), "VI. Anklage mit den Akten an das Gericht"),
       (T("fehler"), "Zwei typische Fehler"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Begleitverfügung in der Anklageklausur: Haftfortdauer, Pflichtverteidigung (§ 140 StPO), Mitteilungen, Asservate, Teileinstellung – ohne Widerspruch zur Anklage.

Der Fall: Referendarin Ortlieb hat die Anklage gegen Herrn Wittig fertig – Einbruch in das Lager eines Baumarkts, Werkzeug für 7.800 €. Wittig sitzt seit drei Monaten wegen Fluchtgefahr in Untersuchungshaft und hat eine Pflichtverteidigerin. Eine zweite Anzeige wegen eines E-Bikes trägt keinen hinreichenden Tatverdacht. Oberstaatsanwältin Pfaff fragt: Wo ist die Begleitverfügung?

Inhalt:
– Wozu die Begleitverfügung? Abgrenzung zur Anklageschrift, kein Widerspruch
– Kopf mit Vermerk „Haft“ (Nr. 52 RiStBV) und I. Abschlussvermerk (§ 169a StPO, § 147 Abs. 2 StPO)
– II. Teileinstellung nach § 170 Abs. 2 StPO, Mitteilung an den Beschuldigten, § 154 StPO; Bescheid nach § 171 StPO mit Belehrung (§ 172 Abs. 1 StPO)
– III. Haft: Fortdauerantrag in der Anklage (Nr. 110 Abs. 4 RiStBV), Sechsmonatsfrist nach § 121 Abs. 1 StPO, Vorlage an das OLG (§ 122 StPO, Nr. 56 RiStBV)
– IV. Pflichtverteidigung: § 140 Abs. 1 Nr. 4 und 5 StPO, §§ 141–143 StPO
– V. Mitteilungen (Nr. 108 RiStBV, MiStra) und Asservate (§ 111n StPO)
– VI. Anklage mit den Akten an das Gericht (§ 199 Abs. 2 StPO)
– Zwei typische Fehler: Teileinstellung innerhalb der angeklagten Tat (§ 154a StPO), übersehene Sechsmonatsfrist (§ 121 Abs. 2, 3 StPO)
– Klausurtipp, Schema, Merksatz

Normen: §§ 111n, 112, 120, 121, 122, 140–143, 145a, 147 Abs. 2, 154, 154a, 169a, 170 Abs. 2, 171, 172 Abs. 1, 199 Abs. 2, 264 StPO.
Richtlinien: Nr. 52, 54, 56, 75, 89, 108, 110 Abs. 4 RiStBV (Fassung vom 28.3.2023).

Hinweise: Referendarin Ortlieb, Oberstaatsanwältin Pfaff, Herr Wittig, Herr Dengler und die Stadt Ahornstadt sind erfunden; das Muster der Verfügung ist ein eigenes Lernmuster. Form und Reihenfolge der Begleitverfügung unterscheiden sich von Land zu Land – maßgeblich sind die Hinweise deines Prüfungsamts. Mehr dazu: Folge 252 (Anklageschrift nach § 200 StPO), Folge 39 (Anklageklausur), Folge 60 (hinreichender Tatverdacht).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Begleitverfügung #StPO #Referendariat
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(§§? \d+\w?)\n(Abs\. \d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Nr\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r" \n", "\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
for alt, neu, n in [("einundzwanzigsten\nJuni ", "21. Juni\n", 0), ("einundzwanzigsten Juni", "21. Juni", 0),
                    ("siebentausendachthundert Euro", "7.800 Euro", 1), ("neunten Juli", "9. Juli", 2)]:
    if n:
        assert srt.count(alt) == n, (alt, srt.count(alt))
    srt = srt.replace(alt, neu)
srt = srt.replace("einundzwanzigsten\n", "21.\n")
assert not re.search(r"§\n|Abs\.\n|Nr\.\n|Paragraf |einundzwanzig|siebentausend|neunten", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Begleitverfügung Muster", "Sechsmonatsfrist", "Teileinstellung"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
