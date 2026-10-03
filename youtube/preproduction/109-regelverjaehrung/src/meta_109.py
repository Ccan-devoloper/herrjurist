"""Nachbearbeitung der Upload-Texte für Folge 109 (nach tools/youtube_metadaten.py, nichts dort geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_109.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Das Darlehen unter Freunden"),
       (T("plan"), "Regelverjährung in 6 Schritten"),
       (T("a194"), "I. Anspruch, § 194 BGB"), (T("f195"), "II. Frist: 3 Jahre, § 195 BGB"),
       (T("b199"), "III. Beginn, § 199 Abs. 1 BGB"), (T("silv"), "Der Silvester-Trick"),
       (T("hoech"), "IV. Höchstfristen, § 199 Abs. 4 BGB"), (T("hemm"), "V. Hemmung, §§ 203, 204, 209 BGB"),
       (T("neu"), "V. Neubeginn durch Abschlagszahlung, § 212 BGB"), (T("r214"), "VI. Rechtsfolge, § 214 BGB"),
       (T("erg"), "Ergebnis"), (T("tipp"), "Klausurtipp: Fälligkeit zuerst"), (T("sch"), "Rechenschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Regelverjährung nach §§ 195, 199 BGB: drei Jahre, Beginn zum Jahresende, Höchstfristen – und ab wann du dich auf die Einrede aus § 214 BGB berufen kannst.

Der Fall: Im März 2022 leiht Finn seiner guten Freundin Pia 2.000 Euro für die Kaution ihrer ersten Wohnung. Zurückzahlen soll sie am 1. Juli 2022 – doch Pia zahlt nicht, und Finn fragt nicht nach. Im Oktober 2026 will er sein Geld. Seit wann darf sich Pia auf die Verjährung berufen? Und was ändert ein Abschlag von 200 Euro im Mai 2024?

Inhalt:
– I. Anspruch: § 194 Abs. 1 BGB im Wortlaut; Rückzahlung des Darlehens, § 488 Abs. 1 Satz 2 BGB
– II. Frist: § 195 BGB im Wortlaut – drei Jahre, auch für die Rückzahlung von Darlehen
– III. Beginn: § 199 Abs. 1 BGB im Wortlaut – Entstehung (in der Regel Fälligkeit) und Kenntnis oder grob fahrlässige Unkenntnis
– Der Silvester-Trick (Ultimo-Verjährung) am Zeitstrahl: Beginn 31.12.2022, verjährt mit Ablauf des 31.12.2025
– IV. Höchstfristen: § 199 Abs. 4 BGB im Wortlaut (zehn Jahre ab Entstehung), Schadensersatz § 199 Abs. 2 und 3 BGB
– V. Hemmung: Verhandlungen (§ 203 BGB), Klage und Mahnbescheid (§ 204 Abs. 1 Nr. 1, 3 BGB), § 209 BGB
– V. Neubeginn: § 212 Abs. 1 Nr. 1 BGB – Abschlagszahlung als Anerkenntnis, neue Frist taggenau ohne Silvester-Trick
– VI. Rechtsfolge: § 214 Abs. 1 BGB im Wortlaut
– Ergebnis, Klausurtipp (Fälligkeit beim unbefristeten Darlehen, § 488 Abs. 3 BGB), Rechenschema, Merksatz

Normen: §§ 194, 195, 199, 203, 204, 209, 212, 214 BGB; §§ 187, 188, 488 BGB

Rechtsprechung:
– BGH, Urt. v. 21.6.2018 – IX ZR 129/17, Rn. 6–8 (Darlehensrückzahlung: drei Jahre, Beginn mit Fälligkeit; Teilzahlung als Anerkenntnis, aber kein Neubeginn vor Fristbeginn)
– BGH, Beschl. v. 1.2.2023 – XII ZB 104/22, Rn. 16 („entstanden“ im Sinne von § 199 BGB setzt grundsätzlich Fälligkeit voraus)
– BGH, Urt. v. 15.8.2012 – XII ZR 86/11, Rn. 33 (nach einem Anerkenntnis beginnt die Frist am Folgetag; die Ultimo-Regel gilt nicht)
– BGH, Urt. v. 8.11.2022 – II ZR 91/21, Rn. 52 (Neubeginn taggenau)
– BGH, Urt. v. 11.11.2014 – XI ZR 265/13, Rn. 40 (kein Neubeginn einer bereits abgelaufenen Frist)

Hinweise: Der „Silvester-Trick“ ist eine Merkhilfe für die Ultimo-Regel des § 199 Abs. 1 BGB, kein Rechtsbegriff; das Rechenschema ist Klausurkonvention. Warum die Verjährung den Anspruch nicht erlöschen lässt und Gezahltes nicht zurückgefordert werden kann (§ 214 Abs. 2 BGB), erklärt Folge 103 (Einwendung oder Einrede).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Verjährung #BGB #Jura
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
