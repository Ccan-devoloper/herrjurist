"""Nachbearbeitung der Upload-Texte für Folge 061 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), fachlich korrigierte Beschreibung (Planbeschreibung ungenau, siehe
RECHTSSTAND.md), Sprechernamen und Paragrafen-Umbruch in den Untertiteln, Lizenzzeile. Keine 16-Länder-Liste (nur NRW geprüft).
Aufruf: python3 meta_061.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Räumung im Winter"), (T("amt"), "Fall: Beim Ordnungsamt"),
       (T("verf"), "Fall: Wiedereinweisung gegen den Willen des Vermieters"), (T("frage"), "Frage und Sachverhalt"),
       (T("land"), "Landesrecht und Zuständigkeit"), (T("egl"), "Generalklausel und Gefahr: unfreiwillige Obdachlosigkeit"),
       (T("stoerer"), "Gegen wen? Verantwortliche und Nichtstörer"), (T("wl19"), "§ 19 OBG NRW: vier Voraussetzungen"),
       (T("s1"), "Nr. 1 und 2: gegenwärtige erhebliche Gefahr"), (T("s3"), "Nr. 3: Hotels, Pensionen, Anmietung"),
       (T("s4"), "Nr. 4, Dauer und Verhältnismäßigkeit"), (T("erg"), "Ergebnis und Variante"),
       (T("entsch"), "Entschädigung des Vermieters"), (T("ende"), "Nach Fristablauf: Folgenbeseitigung"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Polizeilicher Notstand (Beispiel NRW): Darf die Stadt eine Familie gegen den Willen des Vermieters in ihre bisherige Wohnung einweisen? Inanspruchnahme des Nichtstörers nach § 19 OBG NRW, Befristung, Entschädigung und Folgenbeseitigung.

Der Fall: Dezember. Frau Brandt wohnt mit ihren zwei Kindern zur Miete bei Herrn Bauer. Nach einem Jobverlust bleibt die Miete aus, Herr Bauer erstreitet ein Räumungsurteil, am 15. Januar soll geräumt werden. Das Ordnungsamt findet in den städtischen Notunterkünften keinen Platz, fragt aber nicht bei Hotels und Pensionen – und weist die Familie für drei Monate wieder in die Wohnung ein. Muss Herr Bauer das hinnehmen? (Übungsfall)

Inhalt:
– Gefahr durch unfreiwillige Obdachlosigkeit, Generalklausel § 14 Abs. 1 OBG NRW
– Verantwortliche (§ 17 OBG NRW) und Nichtstörer
– Polizeilicher Notstand, § 19 Abs. 1 Nr. 1–4 OBG NRW (für die Polizei § 6 PolG NRW)
– Vorrang eigener Abwehr: Notunterkünfte, Hotels, Pensionen, Anmietung
– Dauer (§ 19 Abs. 2 OBG NRW) und Verhältnismäßigkeit (§ 15 OBG NRW)
– Entschädigung nach § 39 Abs. 1 a und b, § 40 Abs. 1, § 42 Abs. 2, § 43 Abs. 1 OBG NRW
– Folgenbeseitigung nach Fristablauf, Klausurtipp, Klausurschema, Merksatz

Landesrecht: Das Video nutzt Nordrhein-Westfalen als Beispiel (OBG NRW in der Fassung ab 1.7.2026, PolG NRW ab 13.12.2025). Die anderen Länder haben ähnliche Regeln, oft unter anderer Nummer – bitte im Gesetz deines Landes nachschlagen.

Rechtsprechung (Volltexte in NRWE):
– OVG NRW, Beschl. v. 24.3.2023 – 9 B 95/23, Rn. 6, 8 (Unterbringungsmaßstab; Obdachlosigkeit als Gefahr für Leben und Gesundheit)
– VG Köln, Beschl. v. 28.11.2022 – 22 L 1749/22, Rn. 25–43 (Wiedereinweisung rechtswidrig ohne intensive Suche; Folgenbeseitigung)
– VG Köln, Beschl. v. 13.1.2023 – 22 L 43/23, Rn. 9, 29 (unfreiwillige Obdachlosigkeit; Hotels und Anmietung, Kosten unerheblich)
– VG Köln, Beschl. v. 9.10.2020 – 22 L 1688/20, Rn. 16, 18 (Folgenbeseitigung nach Ende der Beschlagnahme; höchstens sechs Monate)
– VG Köln, Urt. v. 16.2.2022 – 22 K 838/20, Rn. 47–49, 61 (§ 39 Abs. 1 a nur bei rechtmäßiger Inanspruchnahme; letztes Mittel)
– VG Köln, Beschl. v. 28.5.2025 – 20 L 1292/25, Rn. 2, 7 f. (Beschlagnahme und Einweisung; Sicherstellung)
– OLG Köln, Urt. v. 16.9.1993 – 7 U 83/93, Rn. 21, 41–43 (Entschädigung auch für die Zeit danach; kein Folgenbeseitigungsanspruch bei Wiedereinweisung)

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 2. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#PolizeilicherNotstand #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("\nBrandt:", "\nFrau Brandt:"), ("\nBauer:", "\nHerr Bauer:"), ("\nSchmitz:", "\nHerr Schmitz:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
