"""Nachbearbeitung der Upload-Texte für Folge 272 (nach meta_245.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, „Satz 1, erste Alternative“).
Aufruf: python3 meta_272.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Anzahlung überwiesen, Werkvertrag angefochten"),
       (T("t1"), "In der Bank: Holt die Bank das Geld zurück?"),
       (T("sv"), "Sachverhalt"),
       (T("dreieck"), "Das Anweisungsdreieck: Deckungs- und Valutaverhältnis"),
       (T("leist"), "Leistungsbegriff: eine Zahlung, zwei Leistungen"),
       (T("fehler"), "Welches Verhältnis ist fehlerhaft?"),
       (T("w812"), "Anspruch aus § 812 I 1 Alt. 1 BGB"),
       (T("durchg"), "Streitfrage: keine Durchgriffskondiktion der Bank"),
       (T("ausn"), "Ausnahmen: fehlende Anweisung, Widerruf, § 675u BGB"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfungsschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Anweisungsfälle (§ 812 I 1 Alt. 1 BGB): Wie wird im Dreieck über Deckungs- und Valutaverhältnis rückabgewickelt und warum gibt es grundsätzlich keine Durchgriffskondiktion?

Der Fall: Tomke lässt ihre Bank die Anzahlung von 3.500 € an den Fliesenleger Herrn Stemmler überweisen. Er hatte behauptet, sein Betrieb sei voll versichert – das stimmt nicht, Tomke ficht den Werkvertrag wegen arglistiger Täuschung an. In der Bank verlangt sie, dass die Bank das Geld direkt bei Herrn Stemmler zurückholt. Der Bankberater lehnt ab. Hat er recht?

Inhalt:
– Das Anweisungsdreieck: Anweisende, Angewiesene, Empfänger; Deckungsverhältnis (Zahlungsdiensterahmenvertrag) und Valutaverhältnis (Werkvertrag)
– Leistungsbegriff aus der Sicht des Empfängers: eine Zahlung, zwei Leistungen – keine Leistungsbeziehung zwischen Bank und Empfänger
– Rückabwicklung über Eck, jeweils im fehlerhaften Verhältnis
– Deckung in Ordnung (Autorisierung, Aufwendungsersatz der Bank), Valuta nichtig (§ 142 Abs. 1 BGB)
– Anspruch Tomke gegen Herrn Stemmler: § 812 Abs. 1 Satz 1 BGB im Wortlaut
– Streitfrage Durchgriff: keine Durchgriffskondiktion, Subsidiarität der Nichtleistungskondiktion, Risikoverteilung (Einwendungen, Insolvenzrisiko)
– Ausnahmen: fehlende Anweisung (Direktkondiktion), Widerruf und Kenntnis des Empfängers, § 675u BGB im Wortlaut
– Ergebnis, Klausurtipp, Prüfungsschema, Merksatz

Normen: § 812 Abs. 1 Satz 1 Alt. 1 und Alt. 2 BGB; § 675c Abs. 1, § 670, § 675f Abs. 2, § 675j, § 675u BGB; §§ 123 Abs. 1, 142 Abs. 1 BGB

Rechtsprechung:
– BGH, Urt. v. 16.6.2015 – XI ZR 243/13, BGHZ 205, 377, Rn. 17 ff. (Anweisungsfälle, fehlende Anweisung, § 675u)
– BGH, Urt. v. 21.7.2026 – XI ZR 158/24, Rn. 10 f. (Direktkondiktion bei fehlender Anweisung)
– BGH, Urt. v. 21.11.2013 – IX ZR 52/13, Rn. 16 (Leistung der Bank an den Kontoinhaber)
– BGH, Urt. v. 21.1.2010 – IX ZR 226/08, Rn. 15 (Fehler im Valutaverhältnis)
– BGH, Urt. v. 31.1.2018 – VIII ZR 39/17, Rn. 17 f., 30–34 (Leistungsbegriff, Empfängerhorizont, Widerruf)
– BGH, Urt. v. 19.9.2023 – XI ZR 343/22, Rn. 15 f., 20 (Aufwendungsersatz, Einwendungen aus dem Valutaverhältnis)
– BGH, Urt. v. 29.10.2020 – IX ZR 212/19, Rn. 21 (Vorrang der Leistungskondiktion)
– BGH, Urt. v. 19.9.2014 – V ZR 269/13, Rn. 22 f. (Risikoverteilung im Mehrpersonenverhältnis)
– BGH, Urt. v. 5.3.2015 – IX ZR 164/14, Rn. 8 (Gutschrift)

Hinweise: Tomke, Herr Stemmler und Herr Feldhaus sind erfunden, die Bank hat keinen Namen. Wie die Leistungskondiktion im Einzelnen geprüft wird, zeigt unsere Folge „Leistungskondiktion § 812 I 1 Alt. 1 BGB – Prüfungsschema“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Anweisungsfälle #Bereicherungsrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("Stemmler: Keine Sorge", "Herr Stemmler: Keine Sorge"), ("Feldhaus: Das geht", "Herr Feldhaus: Das geht")]
for a, b in ERSATZ:
    assert a in srt, a
    srt = srt.replace(a, b)
for a, b in [(r"dreitausendfünfhundert(\s)Euro", r"3.500\1€"),
             (r"S\. 1, Alt\. 1", "Satz 1, erste Alternative"), (r"S\. 1, Alt\. 2", "Satz 1, zweite Alternative")]:
    assert re.search(a, srt), a
    srt = re.sub(a, b, srt)
srt = srt.replace("3.500\n€ bitte", "3.500 €\nbitte")
srt = srt.replace("und kann von ihm dreitausendfünfhundert\n", "und kann von ihm 3.500 €\n")   # über die Cue-Grenze
srt = re.sub(r"\n(\d+\n[\d:,]+ --> [\d:,]+\n)Euro zurückverlangen\.", r"\n\1zurückverlangen.", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|tausend|hundert", srt, re.I), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
