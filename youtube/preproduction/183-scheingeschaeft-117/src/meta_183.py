"""Nachbearbeitung der Upload-Texte für Folge 183 (Kopie von meta_145.py, nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Sprecherbezeichnung und Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_183.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Schwarzgeld beim Hauskauf"),
       (T("sv"), "Sachverhalt und Aufbau in vier Schritten"),
       (T("k1"), "1. Beurkundeter Vertrag: Scheingeschäft, § 117 Abs. 1 BGB"),
       (T("k2"), "2. Verdeckter Vertrag, § 117 Abs. 2 BGB"),
       (T("k3"), "3. Form: § 311b Abs. 1 S. 1 BGB"),
       (T("w125"), "Formnichtig: § 125 S. 1 BGB"),
       (T("k4"), "4. Heilung: § 311b Abs. 1 S. 2 BGB"),
       (T("ganz"), "Heilung: wahrer Preis und Grenzen"),
       (T("vor"), "Folgen vor und nach der Eintragung"),
       (T("steuer"), "Hinweise: Steuer und Barzahlungsverbot (§ 16a GwG)"),
       (T("abgr"), "Abgrenzung: §§ 118, 116 BGB"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Scheingeschäft § 117 BGB: Beurkundet sind 300.000, vereinbart 350.000 Euro. Welcher Vertrag ist nichtig, welcher formnichtig – und wann heilt die Eintragung (§ 311b I 2)?

Der Fall: Markus kauft von Frau Meinhardt ein Haus. Vereinbart sind 350.000 €, im Notarvertrag stehen aber nur 300.000 € – die restlichen 50.000 € bekommt Frau Meinhardt vorher bar im Umschlag. Im selben Termin wird die Auflassung erklärt, Wochen später wird Markus ins Grundbuch eingetragen. Welcher Vertrag gilt – und zu welchem Preis?

Inhalt:
– 1. Der beurkundete Vertrag (300.000 €): Scheingeschäft, nichtig nach § 117 Abs. 1 BGB
– 2. Der verdeckte Vertrag (350.000 €): § 117 Abs. 2 BGB – er gilt nur nach seinen eigenen Regeln
– 3. Form: notarielle Beurkundung (§ 311b Abs. 1 S. 1 BGB) für alle Vereinbarungen, auch den wahren Preis; Formnichtigkeit (§ 125 S. 1 BGB)
– 4. Heilung durch Auflassung und Eintragung (§ 311b Abs. 1 S. 2 BGB): mit dem wahren Preis, nur für die Zukunft, nur der Formmangel
– Folgen vor der Eintragung (keine Übereignungspflicht, Rückforderung nach § 812 BGB) und nach der Eintragung (Vertrag gilt mit 350.000 €)
– Hinweise: Steuerhinterziehung; Barzahlungsverbot beim Immobilienkauf seit 1.4.2023 (§ 16a GwG)
– Abgrenzung: Scherzgeschäft (§ 118 BGB) und geheimer Vorbehalt (§ 116 BGB)
– Klausurtipp, Klausurschema, Merksatz

Normen: §§ 116, 117, 118, 125, 311b I, 812 BGB; § 16a GwG

Rechtsprechung:
– BGH, Urt. v. 15.3.2024 – V ZR 115/22, Rn. 8, 10, 12, 13 (Schwarzgeldabrede beim Grundstückskauf: Scheingeschäft nichtig, verdeckter Vertrag zunächst formnichtig, durch Auflassung und Eintragung geheilt; Heilung nur des Formmangels; § 16a GwG offengelassen; Vertrag in der Regel nicht nichtig)
– BGH, Urt. v. 20.5.2011 – V ZR 221/10, Rn. 6 (Begriff des Scheingeschäfts)
– BGH, Urt. v. 27.5.2011 – V ZR 122/10, Rn. 6, 15 (Beurkundungszwang für alle Vereinbarungen; Heilung ex nunc; Rückabwicklung nach §§ 812 ff. BGB vor der Heilung)
– BGH, Urt. v. 13.5.2016 – V ZR 265/14, Rn. 29 (Willensübereinstimmung muss bei der Auflassung fortbestehen)

Hinweise: Steuerliche Folgen werden nur in einem Satz erwähnt; dieses Video ist keine Steuer- oder Rechtsberatung. Ob ein Verstoß gegen das Barzahlungsverbot (§ 16a GwG) den Kaufvertrag selbst berührt, hat der BGH offengelassen. Auflassung und Eintragung erklärt Folge 145 („Hauskauf in drei Schritten“), § 125 BGB bei der Schriftform Folge 50 („Kündigung per WhatsApp“). Prüfungsreihenfolge und Klausurschema sind Klausurkonvention.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026, GwG zuletzt geändert durch Gesetz vom 29.6.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Scheingeschäft #BGBAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = srt.replace("\nMeinhardt: ", "\nFrau Meinhardt: ")
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
