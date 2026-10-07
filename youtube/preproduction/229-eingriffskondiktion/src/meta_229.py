"""Nachbearbeitung der Upload-Texte für Folge 229 (nach meta_226.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen).
Die reale Person des Klassikers erscheint nur als Fallbezeichnung (Paul Dahlke, BGHZ 20, 345).
Aufruf: python3 meta_229.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Dein Foto auf dem Werbeplakat"),
       (T("sv"), "Sachverhalt"),
       (T("norm"), "§ 812 I 1 Alt. 2 BGB: Eingriffskondiktion"),
       (T("erl"), "1. Etwas erlangt: die Nutzung"),
       (T("kosten"), "2. Auf Kosten: Zuweisungsgehalt, § 22 KUG"),
       (T("org"), "3. Ohne rechtlichen Grund"),
       (T("rf"), "Rechtsfolge: § 818 II, fiktive Lizenz"),
       (T("einwand"), "Einwand und Entreicherung"),
       (T("par"), "Daneben: § 823 BGB und Unterlassung"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Eingriffskondiktion (§§ 812 I 1 Alt. 2, 818 II BGB): Wann ist jemand durch Nutzung deines Fotos bereichert und was muss er zahlen? Der Paul-Dahlke-Fall und die Lizenzgebühr.

Der Fall: Kai Möbius entdeckt sich auf einem Werbeplakat der Limonadenfirma „Brauselust“ – lachend, mit einer Flasche in der Hand. Ein Fotograf der Firma hat ihn im Stadtpark fotografiert, ohne dass er es bemerkte; jetzt hängt das Bild auf 120 Plakaten. Kai verlangt die übliche Lizenz von 3.000 €. Der Marketingleiter meint, Kai hätte ohnehin nie für Limonade geworben und deshalb nichts verloren. Unser Fall folgt dem Klassiker, den der Bundesgerichtshof am 8. Mai 1956 entschieden hat.

Inhalt:
– § 812 Abs. 1 Satz 1 BGB im Wortlaut, Vorrang der Leistungskondiktion
– 1. Etwas erlangt: die Nutzung des Bildnisses
– 2. Auf Kosten: Lehre vom Zuweisungsgehalt, Recht am eigenen Bild (§ 22 Satz 1 KUG im Wortlaut)
– 3. Ohne rechtlichen Grund: keine Einwilligung, keine Ausnahme nach § 23 KUG
– Rechtsfolge: Wertersatz nach § 818 Abs. 2 BGB (im Wortlaut) in Höhe der üblichen Lizenzgebühr („fiktive Lizenz“)
– Einwand „hätte nie zugestimmt“ unerheblich; keine Entreicherung bei Kenntnis (§§ 819 Abs. 1, 818 Abs. 4 BGB)
– Daneben: Schadensersatz nach § 823 Abs. 1 und Abs. 2 BGB i. V. m. § 22 KUG (nur mit Verschulden), Unterlassung analog § 1004 Abs. 1 Satz 2 BGB
– Ergebnis, Klausurtipp, Prüfschema, Merksatz

Normen: §§ 812 Abs. 1 Satz 1 Alt. 2, 818 Abs. 2, 3, 4, 819 Abs. 1 BGB; §§ 22, 23 KUG; § 823 Abs. 1, 2 BGB; § 1004 Abs. 1 Satz 2 BGB analog

Rechtsprechung:
– BGH, Urt. v. 8.5.1956 – I ZR 62/54, BGHZ 20, 345 (Paul Dahlke)
– BGH, Urt. v. 20.3.2012 – VI ZR 123/11, Rn. 24
– BGH, Urt. v. 21.1.2021 – I ZR 120/19, Rn. 24, 26, 36, 38, 58 f. (Clickbaiting)
– BGH, Urt. v. 31.5.2012 – I ZR 234/10, Rn. 15, 42 (Playboy am Sonntag)
– BGH, Urt. v. 23.4.2026 – I ZR 41/24, Rn. 124, 126
– BGH, Urt. v. 16.5.2013 – IX ZR 204/11, Rn. 15; BGH, Urt. v. 18.1.2012 – I ZR 187/10, BGHZ 192, 204, Rn. 40, 46
– BGH, Urt. v. 7.7.2020 – VI ZR 250/19, Rn. 8; BGH, Urt. v. 11.8.2010 – XII ZR 102/09, Rn. 55

Hinweise: Kai Möbius, Marketingleiter Wendorf und die Firma „Brauselust“ sind erfunden; der Fall bildet den Klassiker nach. Die reale Person des echten Falls wird nicht dargestellt. Die Kondiktionsarten im Überblick erklärt unsere Folge „Bereicherungsrecht Überblick: Welche Kondiktion wann?“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Bereicherungsrecht #Zivilrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("Kai: Das bin", "Kai Möbius: Das bin"), ("Kai: Sie werben", "Kai Möbius: Sie werben"),
          ("Wendorf: Sie hätten", "Marketingleiter Wendorf: Sie hätten")]
for a, b in ERSATZ:
    assert a in srt, a
    srt = srt.replace(a, b)
for a, b in [(r"hundertzwanzig", "120"), (r"dreitausend(\s)Euro", r"3.000\1€"),
             (r"Neunzehnhundertsechsundfünfzig", "1956")]:
    assert re.search(a, srt), a
    srt = re.sub(a, b, srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|neunzehnhundert|dreitausend|hundertzwanzig", srt, re.I), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
