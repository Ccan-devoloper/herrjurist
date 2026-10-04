"""Nachbearbeitung der Upload-Texte für Folge 175 (nach tools/youtube_metadaten.py, nichts dort geändert), wie Folge 128:
Hilfsangebot ganz oben in der Beschreibung (TelefonSeelsorge, Nummern verifiziert auf telefonseelsorge.de am 04.10.2026),
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Fall sachlich ohne Bewertung und ohne Namen der Beteiligten, Inhalt,
Rechtsprechung mit Leitsatz/Rn., Lizenzzeile, zusätzliche Tags; Untertitel: Zahlen und Paragrafen in Ziffern.
Aufruf: python3 meta_175.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Behandlungsabbruch – ist das strafbar?"),
       (T("begr"), "1. Aktiv, passiv, indirekt: die frühere Einteilung"),
       (T("echt"), "2. Der echte Fall Putz und das Landgericht Fulda"),
       (T("kern"), "3. Kern: Behandlungsabbruch, Leitsätze 1 und 2"),
       (T("vor"), "Voraussetzungen und Grenze: Leitsatz 3, § 216 StGB"),
       (T("pv"), "4. Patientenwille: § 1827 BGB"),
       (T("erg"), "5. Ergebnis: Freispruch"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"), (T("merke"), "Merksatz"), (T("hilfe"), "Hilfsangebot")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
assert cj["dauer"] + 8.0 - KAP[-1][0] >= 10
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Wenn dich das Thema belastet: Die TelefonSeelsorge ist rund um die Uhr und kostenlos erreichbar, unter 0800 111 0 111, 0800 111 0 222 oder 116 123 (telefonseelsorge.de).

Sterbehilfe aktiv, passiv, indirekt: Wann ist ein Behandlungsabbruch nach dem Patientenwillen gerechtfertigt (BGHSt 55, 191, Fall Putz) – §§ 212, 216 StGB?

Der Fall: Eine Frau liegt seit Jahren im Wachkoma und wird über eine Sonde künstlich ernährt. Früher hatte sie mündlich gesagt, sie wolle keine künstliche Ernährung. Als das Heim die eingestellte Ernährung wieder aufnehmen will, durchtrennt die Tochter auf Rat des Anwalts den Schlauch der Sonde. Das Landgericht Fulda verurteilt den Anwalt wegen versuchten Totschlags – der BGH spricht ihn frei.

Inhalt:
– Die frühere Einteilung der Lehre: aktive, passive und indirekte Sterbehilfe
– Der echte Fall nach dem Urteil und die Entscheidung des Landgerichts Fulda
– Kern: Rechtfertigung durch Einwilligung; die Leitsätze 1 bis 3 im Wortlaut; Tun oder Unterlassen entscheidet nicht
– Voraussetzungen: lebensbedrohliche Erkrankung, Behandlungsbezug, Handelnde; Grenze: gezielte Eingriffe bleiben strafbar (§ 216 StGB, vgl. Folge 128)
– Patientenwille: § 1827 BGB (früher § 1901a BGB) im Wortlaut
– Ergebnis, Klausurtipp, Klausurschema, Merksatz

Normen: §§ 212, 216, 13 StGB; § 1827 BGB (früher § 1901a BGB)

Rechtsprechung:
– BGH, Urt. v. 25.6.2010 – 2 StR 454/09, BGHSt 55, 191 (Fall Putz): Leitsätze 1–3; Rn. 21 f., 27 f. (Einwilligung, Abkehr von der Unterscheidung nach Tun und Unterlassen), Rn. 30 f. (normativ-wertender Oberbegriff), Rn. 33–35 (Voraussetzungen, Behandlungsbezug, indirekte Sterbehilfe), Rn. 37 (§ 216 StGB unberührt), Rn. 38 (strenge Beweismaßstäbe), Rn. 39, 41 (Hilfspersonen, Freispruch)

Voraussetzungen: Einwilligung (Folge 062), Unterlassungsdelikt § 13 StGB (Folge 071); Tötung auf Verlangen: Folge 128.

Kapitel:
{kapitel}

Der Seminarrahmen mit Thilo und Professor Wedekind ist erfunden; der Fall ist nach dem Urteil des BGH wiedergegeben. Die Prüfungsschemata sind Klausurkonventionen. Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com).

#Strafrecht #Jura #Examen
"""
for verboten in ("Schere", "Pflegebett", "Putz,", "Wolfgang"):
    assert verboten not in BESCHR, verboten
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = srt.replace("hundertachtundzwanzig", "128")
srt, n1 = re.subn(r"Totschlags zu neun\n", "Totschlags zu 9\n", srt)
srt, n2 = re.subn(r"gut(\s+)zwei(\s+)Wochen", r"gut\g<1>2\2Wochen", srt)
assert n1 == 1 and n2 == 1, (n1, n2)
assert not re.search(r"§\n", srt)
for w in ("zweitausendzwei", "hundertachtundzwanzig", "achtzehnhundert", "neunzehnhundert", "zweihundert"):
    assert w not in srt, w
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["thumbnail_text"] = "STERBEHILFE ERLAUBT?"
m["thumbnail_b"] = "FALL PUTZ"
m["hook_vorschlag"] = ("Eine Tochter durchtrennt auf Rat des Anwalts den Schlauch der Ernährungssonde ihrer im Wachkoma "
                       "liegenden Mutter, die zuvor mündlich gesagt hatte, sie wolle keine künstliche Ernährung.")
for t in ("Sterbehilfe", "BGHSt 55, 191", "2 StR 454/09", "§ 1827 BGB", "indirekte Sterbehilfe", "aktive Sterbehilfe"):
    if t not in m["tags"]:
        m["tags"].append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
