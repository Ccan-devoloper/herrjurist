"""Nachbearbeitung der Upload-Texte für Folge 257 (nach meta_249.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen der geprüften Länder, Rechtsprechung mit
Rn., Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Normangaben nicht über den Zeilenumbruch getrennt, Zahlen als Ziffern).
Aufruf: python3 meta_257.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Benzinkanister vor dem Haus"),
       (T("frage"), "Die Frage und der Sachverhalt"),
       (T("egl"), "Generalklausel"),
       (T("def"), "Definition der konkreten Gefahr"),
       (T("e1"), "Die Merkmale am Fall"),
       (T("jd"), "Je-desto-Formel"),
       (T("exante"), "Prognose ex ante"),
       (T("erg"), "Ergebnis"),
       (T("abgr"), "Gegenwärtige, erhebliche, dringende, abstrakte Gefahr"),
       (T("gegen"), "Gegenfall und abstrakte Gefahr"),
       (T("tab"), "Normen der Länder"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Konkrete Gefahr im Polizeirecht: Wie wahrscheinlich muss der Schaden sein? Definition (z. B. § 2 Nr. 1 NPOG), Je-desto-Formel, Prognose ex ante und Abgrenzung zur gegenwärtigen, erheblichen, dringenden und abstrakten Gefahr – Dogmatik bundesweit, Normen am Beispiel einzelner Länder.

Der Fall: Samstagnachmittag vor einem Mehrfamilienhaus. Herr Fichtner steht mit einem offenen Benzinkanister am Hauseingang und raucht, es riecht nach Benzin. Polizistin Eilers fordert ihn auf, die Zigarette auszumachen und den Kanister zu schließen. Durfte sie das verlangen?

Inhalt (Schema):
– Ermächtigungsgrundlage: Generalklausel (Beispiel § 8 Abs. 1 PolG NRW)
– Definition: Sachlage im Einzelfall, Schaden für ein Schutzgut, absehbare Zeit, hinreichende Wahrscheinlichkeit
– Je-desto-Formel und ihre Grenze
– Prognose ex ante aus Sicht eines besonnenen und sachkundigen Amtswalters, gestützt auf Tatsachen
– Abgrenzung: gegenwärtige, erhebliche, dringende und abstrakte Gefahr
– Gegenfall, Normen der Länder, Klausurtipp, Schema, Merksatz

Normen (Wortlaut am Landesportal geprüft am 8. Oktober 2026):
– Nordrhein-Westfalen: Generalklausel § 8 Abs. 1 PolG NRW („im einzelnen Falle bestehende, konkrete Gefahr“)
– Brandenburg: § 10 Abs. 1 BbgPolG („im einzelnen Falle bestehende konkrete Gefahr“)
– Niedersachsen: § 11 NPOG; Begriffe in § 2 Nr. 1 (Gefahr), Nr. 2 (gegenwärtige), Nr. 3 (erhebliche), Nr. 4 (dringende), Nr. 6 (abstrakte Gefahr); Verordnungen gegen abstrakte Gefahren § 55 NPOG
– Sachsen: § 12 Abs. 1 SächsPVDG; Begriffe in § 4 Nr. 3 a–d, h SächsPVDG
– Bundespolizei: § 14 Abs. 1, 2 BPolG (erhebliche Gefahr)
Die übrigen Länder regeln die Generalklausel in ihrem Polizei- bzw. Ordnungsgesetz unter eigener Nummer; bitte am Landesrecht prüfen.

Rechtsprechung:
– BVerfG, Urt. v. 20.4.2016 – 1 BvR 966/09 u. a., BVerfGE 141, 220, Rn. 110 f. (Begriff der konkreten und der dringenden Gefahr)
– BVerfG, Beschl. v. 4.4.2006 – 1 BvR 518/02, BVerfGE 115, 320, Rn. 136, 144 f. (Je-desto, Tatsachenbasis der Prognose)
– BVerwG, Urt. v. 22.3.2012 – 3 C 16.11, Rn. 32 (Je-desto-Formel im allgemeinen Polizei- und Ordnungsrecht)
– BVerwG, Urt. v. 25.10.2017 – 6 C 44.16, Rn. 23 (abstrakte Gefahr, Polizeiverordnung)
– OVG NRW, Urt. v. 15.7.2002 – 7 A 1717/01; VG Köln, Gerichtsbescheid v. 11.2.2016 – 20 K 6403/14, Rn. 45 (Sicht ex ante)

Hinweise: Herr Fichtner, Polizistin Eilers und Sebastian sind erfundene Figuren. Mehr dazu: Folge 213 (Schutzgüter der öffentlichen Sicherheit), Folge 052 (Anscheinsgefahr).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Polizeirecht #KonkreteGefahr #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(§§? \d+)\n(Abs\. \d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Nr\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r" \n", "\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
for alt, neu in [("zweihundertdreizehn.", "213."), ("zweiundfünfzig.", "052."), ("Folge 52.", "Folge 052.")]:
    if alt in srt:
        srt = srt.replace(alt, neu)
assert not re.search(r"§\n|Abs\.\n|Nr\.\n|Paragraf(?!en\. In deinem)", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["konkrete Gefahr Polizeirecht", "erhebliche Gefahr", "dringende Gefahr"]
                         if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
