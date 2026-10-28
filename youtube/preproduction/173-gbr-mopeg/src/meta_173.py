"""Nachbearbeitung der Upload-Texte für Folge 173 (nach meta_152.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung, Materialien, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Aussprachehilfen G.b.R./Mopeg/Arge
zurück in die Schreibung, Gliederung, Zahlen).
Aufruf: python3 meta_173.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Band kauft Musikanlage auf Rechnung, Sachverhalt"),
       (T("aufbau"), "Aufbau: MoPeG seit 1.1.2024, drei Prüfschritte"),
       (T("p1"), "§ 705 Abs. 1 BGB: Entstehung der GbR"),
       (T("p2"), "§ 705 Abs. 2 BGB: rechtsfähige und nicht rechtsfähige GbR"),
       (T("p3"), "§ 705 Abs. 3, § 719 BGB: Vermutung und Entstehung gegenüber Dritten"),
       (T("eintr"), "§ 707 BGB: Gesellschaftsregister, eGbR, § 47 Abs. 2 GBO"),
       (T("verm"), "§ 713 BGB: Gesellschaftsvermögen, ARGE Weißes Roß"),
       (T("vertr"), "§ 720 BGB: Vertretung, § 715 Geschäftsführung"),
       (T("haft"), "§ 721 BGB: persönliche Haftung, §§ 721a, 721b"),
       (T("loes"), "Lösung des Falls"),
       (T("tipp"), "Klausurtipp: Anspruch gegen einen Gesellschafter"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""GbR nach MoPeG (§§ 705 ff. BGB): Wann ist die Gesellschaft rechtsfähig, was bringt die Eintragung als eGbR und wer vertritt sie? Mit der Band, die eine Anlage kauft.

Der Fall: Bente, Gerrit und Ingo gründen per Handschlag eine Band und zahlen jeden Monat in die Bandkasse. Zu dritt kaufen sie im Musikgeschäft für die Band eine Musikanlage für 3.600 € auf Rechnung. Die Bandkasse reicht nicht – und die Händlerin verlangt die ganze Summe von Ingo. „Ich allein? Die Anlage hat doch die Band gekauft!“

Inhalt:
– Seit 1.1.2024 gilt das neue Recht der GbR (MoPeG, §§ 705 ff. BGB n. F.)
– Entstehung: Gesellschaftsvertrag und gemeinsamer Zweck, § 705 Abs. 1 BGB im Wortlaut; grundsätzlich formfrei
– Rechtsfähige und nicht rechtsfähige Gesellschaft, § 705 Abs. 2 BGB im Wortlaut; Vermutung des § 705 Abs. 3 BGB; Entstehung gegenüber Dritten, § 719 Abs. 1 BGB
– Eintragung im Gesellschaftsregister: freiwillig (§ 707 Abs. 1 BGB), Namenszusatz „eGbR“ (§ 707a Abs. 2 BGB), Voraussetzung fürs Grundbuch (§ 47 Abs. 2 GBO)
– Gesellschaftsvermögen: Die Anlage gehört der GbR selbst, § 713 BGB; ARGE Weißes Roß (BGH 2001) und Abschied von der Gesamthand
– Vertretung: Gesamtvertretung nach § 720 Abs. 1 BGB, Abgrenzung zur Geschäftsführung (§ 715 BGB)
– Haftung: persönlich als Gesamtschuldner, § 721 BGB; Eintretende (§ 721a), Einwendungen (§ 721b)
– Lösung, Klausurtipp (Anspruchsgrundlage § 433 Abs. 2 i. V. m. § 721 S. 1 BGB), Prüfschema, Merksatz

Normen: §§ 705, 707, 707a, 713, 715, 719, 720, 721, 721a, 721b BGB; §§ 421, 433 BGB; § 47 Abs. 2 GBO

Rechtsprechung:
– BGH, Urt. v. 29.1.2001 – II ZR 331/00, BGHZ 146, 341 („ARGE Weißes Roß“): Die (Außen-)GbR ist rechtsfähig, soweit sie durch Teilnahme am Rechtsverkehr eigene Rechte und Pflichten begründet; akzessorische Gesellschafterhaftung

Gesetzesmaterialien: Regierungsentwurf zum MoPeG, BT-Drs. 19/27635 (u. a. S. 104 f. Formfreiheit, S. 125 f. Rechtsfähigkeit, S. 128 Eintragungswahlrecht, S. 148 Gesellschaftsvermögen, S. 162 Vertretung, S. 165 f. Haftung)

Hinweise: Ältere Darstellungen vor dem 1.1.2024 (Gesamthand, §§ 714, 718 BGB a. F.) sind überholt. Die Band ist im Fall nicht eingetragen; rechtsfähig ist sie trotzdem. Wie der Ausgleich unter Gesamtschuldnern funktioniert, zeigt die Folge zur Gesamtschuld (§§ 421, 426 BGB).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#GbR #Gesellschaftsrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei):( |\n)", lambda m: {"eins": "I.", "zwei": "II."}[m.group(1)] + m.group(2), srt)
for muster, ersatz in [(r"\be\.G\.b\.R\.", "eGbR"), (r"\bG\.b\.R\.", "GbR"), (r"\bMopeg\b", "MoPeG"),
                       (r"\bArge(\s)Weißes", r"ARGE\1Weißes"), (r"\bRoss:", "Roß:"),
                       (r"fünfzig(\s)Euro", r"50\1Euro"), (r"dreitausendsechshundert", "3.600"),
                       (r"vierzehn(\s)Tagen", r"14\1Tagen"), (r"ersten(\s)Januar", r"1.\1Januar")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
srt = srt.replace("\nBornemann: ", "\nFrau Bornemann: ")
srt = re.sub(r"GbR(?=[?.,!]?\n\n)", "GbR", srt)
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "tausend" not in srt and "G.b.R" not in srt, "Zahlwort/Schreibung im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
