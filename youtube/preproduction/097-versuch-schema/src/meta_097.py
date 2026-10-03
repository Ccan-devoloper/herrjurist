"""Nachbearbeitung der Upload-Texte für Folge 097 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen zu Sätzen ohne
Aktenzeichen und Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_097.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Der Schuss auf den Nachbarn"),
       (T("p22"), "§§ 22, 23 StGB: Wortlaut und Aufbau"), (T("vp"), "0. Vorprüfung"),
       (T("te"), "I. 1. Tatentschluss"), (T("ua"), "I. 2. Unmittelbares Ansetzen"),
       (T("rw"), "II. Rechtswidrigkeit, III. Schuld"), (T("rt"), "IV. Rücktritt: fehlgeschlagener Versuch"),
       (T("erg"), "Ergebnis, Strafmilderung, Konkurrenzen"), (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema Versuch"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Versuch Schema nach §§ 22, 23 StGB: Vorprüfung, Tatentschluss und unmittelbares Ansetzen – so baust du die Versuchsprüfung auf. Am Fall eines Nachbarn, der schießt und um Zentimeter verfehlt.

Der Fall: Herbert und sein Nachbar Gregor streiten seit Monaten, weil Gregor sein Auto vor Herberts Garage parkt. Herbert holt eine alte Pistole mit einer einzigen Patrone, zielt aus 5 Metern auf Gregor, will ihn töten und drückt ab. Die Kugel verfehlt Gregor um wenige Zentimeter. Gregor bleibt unverletzt. Ist Herbert trotzdem strafbar?

Inhalt:
– § 22 und § 23 Abs. 1 StGB im Wortlaut
– 0. Vorprüfung: Nichtvollendung; Strafbarkeit des Versuchs (Totschlag ist ein Verbrechen, § 12 Abs. 1 StGB)
– I. 1. Tatentschluss: vorsatzgleiche Vorstellung von allen Umständen des äußeren Tatbestands, dazu besondere subjektive Merkmale
– I. 2. Unmittelbares Ansetzen: „jetzt geht’s los“, keine Zwischenschritte, konkrete Gefährdung des Rechtsguts; Abgrenzung zur Vorbereitung (Waffe holen)
– II. Rechtswidrigkeit, III. Schuld
– IV. Rücktritt, § 24 StGB: ausgeschlossen beim fehlgeschlagenen Versuch (Rücktrittshorizont)
– Ergebnis: versuchter Totschlag, §§ 212, 22, 23 Abs. 1 StGB; fakultative Milderung nach § 23 Abs. 2, § 49 Abs. 1 StGB; die versuchte gefährliche Körperverletzung tritt zurück
– Klausurtipp, Klausurschema, Merksatz

Normen: §§ 12, 22, 23, 24, 49, 212 StGB; §§ 32, 224 StGB

Rechtsprechung:
– BGH, Beschl. v. 9.1.2020 – 4 StR 324/19, Rn. 17 (Tatentschluss)
– BGH, Beschl. v. 28.4.2020 – 5 StR 15/20 (BGHSt 65, 15), Rn. 4 f. (unmittelbares Ansetzen, Gefährdung des Rechtsguts)
– BGH, Urt. v. 26.3.2025 – 2 StR 598/24, Rn. 11 (fehlgeschlagener Versuch, Rücktrittshorizont)
– BGH, Beschl. v. 13.8.2013 – 2 StR 180/13, Rn. 12 (versuchte Körperverletzung tritt hinter den Tötungsversuch zurück)

Hinweise: Der Aufbau mit „0. Vorprüfung“, die Einordnung besonderer subjektiver Merkmale in den Tatentschluss und der Klausurtipp sind Klausurkonvention (Lehrbuchstandard), keine Gesetzesvorgabe. Mordmerkmale legt der Fall nicht nahe; geprüft wird deshalb § 212 StGB.

Mehr dazu: Folge 11 (Deliktsaufbau Strafrecht), Folge 29 (Vorsatzformen).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026 (StGB zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Versuch #Strafrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
