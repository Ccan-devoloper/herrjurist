"""Nachbearbeitung der Upload-Texte für Folge 052 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), fachlich korrigierte Beschreibung (Planbeschreibung irreführend, siehe
RECHTSSTAND.md), Sprechernamen und Paragrafen-Umbruch in den Untertiteln, Lizenzzeile.
Aufruf: python3 meta_052.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Hilfeschreie im Mietshaus"), (T("polizei"), "Fall: Die Polizei an der Tür"),
       (T("drin"), "Fall: Nur ein Krimi"), (T("bescheid"), "Fall: Wochen später – wer zahlt?"),
       (T("frage"), "Frage und Sachverhalt"), (T("land"), "Landesrecht und zwei Ebenen"),
       (T("egl"), "Ermächtigungsgrundlage: § 41 PolG NRW"), (T("art13"), "Art. 13 GG und Zuständigkeit"),
       (T("gefahr"), "Konkrete und gegenwärtige Gefahr"), (T("problem"), "Anscheinsgefahr: die Sicht ex ante"),
       (T("schein"), "Putativgefahr und Gefahrenverdacht"), (T("verh"), "Verhältnismäßigkeit und Ergebnis"),
       (T("ebene2"), "Kosten: Wer zahlt den Schlüsseldienst?"), (T("entsch"), "Entschädigung für das Schloss"),
       (T("gegen"), "Gegenfall: OLG Köln, Zeitschaltuhr"), (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Anscheinsgefahr im Polizeirecht (Beispiel NRW): Durfte die Polizei die Wohnung öffnen lassen, obwohl nur ein Krimi lief? Abgrenzung zu Putativgefahr (Scheingefahr) und Gefahrenverdacht, dazu Kosten und Entschädigung.

Der Fall: Sonntagabend, kurz vor elf. Frau Jäger hört aus der Nachbarwohnung eine Frau um Hilfe schreien. Polizist Ahrens klingelt, klopft und ruft – niemand öffnet. Ein Schlüsseldienst bricht das Schloss auf. Drinnen sitzt Herr Böttcher vor einem Krimi in voller Lautstärke. Wochen später soll er 250 Euro für den Schlüsseldienst zahlen, und das Schloss ist kaputt. (Übungsfall)

Inhalt:
– 1. Ebene (ex ante): Betreten der Wohnung, § 41 Abs. 1 Satz 1 Nr. 4, Abs. 2 PolG NRW, Art. 13 Abs. 7 GG
– Gefahrbegriff: konkrete und gegenwärtige Gefahr, § 8 Abs. 1 PolG NRW
– Anscheinsgefahr, Putativgefahr (Scheingefahr), Gefahrenverdacht
– Ersatzvornahme im sofortigen Vollzug, §§ 50 Abs. 2, 52 PolG NRW
– 2. Ebene (ex post): Kosten des Anscheinsstörers, Entschädigung wie ein Nichtstörer (§ 67 PolG NRW i. V. m. §§ 39 Abs. 1 a, 40 Abs. 4, 43 Abs. 1 OBG NRW)
– Gegenfall OLG Köln (Zeitschaltuhr), Klausurtipp, Klausurschema, Merksatz

Landesrecht: Das Video nutzt Nordrhein-Westfalen als Beispiel (PolG NRW in der Fassung ab 13.12.2025, OBG NRW ab 1.7.2026). Die anderen Länder haben eigene, ähnliche Regeln, oft unter anderer Nummer – bitte im Gesetz deines Landes nachschlagen.

Rechtsprechung (Volltexte in NRWE):
– OVG NRW, Beschl. v. 14.6.2000 – 5 A 95/00, Rn. 15–23 (Kosten und Entschädigung des Anscheins-/Verdachtsstörers ex post)
– OVG NRW, Urt. v. 15.7.2002 – 7 A 1717/01, Rn. 99 (Anscheinsgefahr)
– OVG NRW, Urt. v. 7.8.2018 – 5 A 294/16, Rn. 37 (Gefahrenverdacht)
– OVG NRW, Urt. v. 5.7.2013 – 5 A 607/11, Rn. 153; Urt. v. 2.3.2021 – 5 A 942/19, Rn. 42 (konkrete und gegenwärtige Gefahr)
– OLG Köln, Urt. v. 26.1.1995 – 7 U 146/94 (Zeitschaltuhr: Entschädigung, zwei Drittel Mitverschulden)
– VG Köln, Gerichtsbescheid v. 11.2.2016 – 20 K 6403/14 (Türöffnung durch Schlüsseldienst, Kosten)

Kapitel:
{kapitel}

Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 2. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Anscheinsgefahr #ÖffentlichesRecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
for alt, neu in (("Jaeger:", "Frau Jäger:"), ("Boettcher:", "Herr Böttcher:"), ("\nAhrens:", "\nPolizist Ahrens:")):
    srt = srt.replace(alt, neu)
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert "Jaeger" not in srt and "Boettcher" not in srt and not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
