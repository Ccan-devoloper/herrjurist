"""Nachbearbeitung der Upload-Texte für Folge 245 (nach meta_229.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Paragrafenzeichen nicht am Zeilenende).
Aufruf: python3 meta_245.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Klavier gekauft, Kaufvertrag angefochten"),
       (T("sv"), "Sachverhalt; § 812 I 1 Alt. 1 BGB im Wortlaut"),
       (T("erl"), "1. Etwas erlangt: Geldscheine oder Gutschrift"),
       (T("leist"), "2. Durch Leistung: der Leistungsbegriff"),
       (T("org"), "3. Ohne rechtlichen Grund: Anfechtung, § 142 I"),
       (T("aus"), "4. Kein Ausschluss: §§ 814, 817 S. 2"),
       (T("rf"), "Rechtsfolge: § 818 I, II, III BGB"),
       (T("gegen"), "Saldotheorie: Geld gegen Klavier"),
       (T("orem"), "Abgrenzung: condictio ob rem"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfungsschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Leistungskondiktion (§ 812 I 1 Alt. 1 BGB) im Schema: etwas erlangt, durch Leistung, ohne Rechtsgrund. Wie bestimmst du den Leistungsbegriff? Am nichtigen Klavierkauf.

Der Fall: Frau Heidkamp bietet Mila ihr gebrauchtes Klavier per Nachricht für 2.400 € an – gemeint hatte sie 4.200 €, sie hat sich vertippt. Mila sagt sofort zu, zahlt beim Abholen bar, und Frau Heidkamp zahlt die Scheine auf ihr Konto ein. Eine Woche später ficht Frau Heidkamp an. Kann Mila ihr Geld zurückverlangen – und muss sie dafür das Klavier hergeben?

Inhalt:
– § 812 Abs. 1 Satz 1 BGB im Wortlaut: Leistungskondiktion (condictio indebiti)
– 1. Etwas erlangt: jeder vermögenswerte Vorteil – Eigentum und Besitz an den Scheinen, bei Überweisung die Gutschrift
– 2. Durch Leistung: bewusste und zweckgerichtete Mehrung fremden Vermögens, Sicht des Empfängers
– 3. Ohne rechtlichen Grund: Erklärungsirrtum (§ 119 Abs. 1 BGB), Anfechtung, Nichtigkeit von Anfang an (§ 142 Abs. 1 BGB)
– 4. Kein Ausschluss: § 814 BGB und § 817 Satz 2 BGB im Wortlaut
– Rechtsfolge: Herausgabe und Wertersatz (§ 818 Abs. 1, 2 BGB im Wortlaut), keine Entreicherung (§ 818 Abs. 3 BGB)
– Saldotheorie: Rückzahlung nur Zug um Zug gegen Rückgabe und Rückübereignung des Klaviers
– Abgrenzung zur condictio ob rem (§ 812 Abs. 1 Satz 2 Alt. 2 BGB)
– Ergebnis, Klausurtipp (Vorrang der Leistungskondiktion), Prüfungsschema, Merksatz

Normen: § 812 Abs. 1 Satz 1 Alt. 1 BGB; §§ 814, 817 Satz 2, 818 Abs. 1–3 BGB; §§ 119 Abs. 1, 121, 142 Abs. 1, 143 BGB; § 433 Abs. 2 BGB

Rechtsprechung:
– BGH, Urt. v. 31.1.2018 – VIII ZR 39/17, Rn. 16 f. (Vorrang, Leistungsbegriff, Empfängerhorizont)
– BGH, Urt. v. 21.6.2012 – III ZR 291/11, Rn. 24
– BGH, Urt. v. 20.1.2026 – XI ZR 131/24, Rn. 36 (condictio indebiti)
– BGH, Urt. v. 2.12.2011 – V ZR 119/11, Rn. 17; BGH, Urt. v. 5.3.2015 – IX ZR 164/14, Rn. 8
– BGH, Urt. v. 27.6.2014 – V ZR 55/13, Rn. 19; BGH, Urt. v. 11.2.2026 – VIII ZR 37/24, Rn. 41 f.
– BGH, Urt. v. 13.5.2014 – XI ZR 170/13, Rn. 109 (§ 814 BGB)
– BGH, Urt. v. 21.7.2026 – XI ZR 158/24, Rn. 18 (Entreicherung)
– BGH, Urt. v. 27.9.2013 – V ZR 52/12, Rn. 28 (Saldotheorie)
– BGH, Urt. v. 6.7.2011 – XII ZR 190/08, Rn. 31 f. (condictio ob rem)

Hinweise: Mila und Frau Heidkamp sind erfunden. Welche Kondiktion wann greift, zeigt unsere Folge „Bereicherungsrecht Überblick: Welche Kondiktion wann?“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Leistungskondiktion #Bereicherungsrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("Heidkamp: Ich habe", "Frau Heidkamp: Ich habe"), ("Heidkamp: Die bekommen", "Frau Heidkamp: Die bekommen")]
for a, b in ERSATZ:
    assert a in srt, a
    srt = srt.replace(a, b)
for a, b in [(r"viertausendzweihundert(\s)Euro", r"4.200\1€"), (r"zweitausendvierhundert(\s)Euro", r"2.400\1€"),
             (r"nicht zweitausendvierhundert\.", "nicht 2.400."), (r"oder achthundertsiebzehn", "oder § 817"),
             (r"S\. 1, Alt\. 1", "Satz 1, erste Alternative"), (r"S\. 2, Alt\. 2", "Satz 2, zweite Alternative"),
             (r"§ 817 S\. 2", "§ 817 Satz 2")]:
    assert re.search(a, srt), a
    srt = re.sub(a, b, srt)
srt = re.sub(r"\n\S*\n?S\. 2\. Fünf", lambda m: m.group(0).replace("S. 2.", "Satz 2."), srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|tausend|hundert", srt, re.I), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
