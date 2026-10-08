"""Nachbearbeitung der Upload-Texte für Folge 281 (nach meta_278.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Paragrafenzeichen nicht am Zeilenende).
Aufruf: python3 meta_281.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Schimmel, Baulärm, kalte Heizung"),
       (T("w536"), "§ 536 Abs. 1 BGB im Wortlaut"),
       (T("kraft"), "Minderung kraft Gesetzes, Mangel, Bruttomiete"),
       (T("drei"), "Schimmel: Ursache und Beweislast"),
       (T("s2"), "Baulärm vom Nachbargrundstück (Bolzplatz-Urteil)"),
       (T("s3"), "Kalte Heizung"),
       (T("w536c"), "Anzeigepflicht, § 536c BGB"),
       (T("w536b"), "Kenntnis bei Vertragsschluss, § 536b BGB"),
       (T("risk"), "Risiko: zu viel gemindert – Kündigung?"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfungsschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Mietminderung nach § 536 BGB: Wann ist die Miete bei Schimmel, Baulärm oder kalter Heizung kraft Gesetzes gemindert – und was gilt bei Anzeige (§ 536c BGB) und Kenntnis (§ 536b BGB)? Und was riskierst du, wenn du einfach weniger überweist?

Der Fall: Friedemann mietet eine Altbauwohnung für 850 € warm. Im November entdeckt er Schimmel hinter dem Schrank, seiner Vermieterin sagt er es erst im Januar. Nebenan entsteht ein Neubau, tagsüber dröhnt der Presslufthammer. Im Januar bleibt die Heizung eine Woche kalt – das meldet er sofort. Frau Teuber meint, der Schimmel komme vom Lüften, und für die Baustelle könne sie nichts. Friedemann will nur noch die halbe Miete zahlen.

Inhalt:
– § 536 Abs. 1 BGB im Wortlaut: Minderung kraft Gesetzes, ohne Erklärung (anders als die Kaufpreisminderung nach § 441 BGB)
– Mangel als nachteilige Abweichung vom vertraglich vorausgesetzten Zustand, unerhebliche Minderung, Bemessung von der Bruttomiete
– Schimmel: Baumangel oder Lüften? Beweislast nach Verantwortungsbereichen; Wärmebrücken im Altbau
– Baulärm vom Nachbargrundstück: Bolzplatz- und Baustellen-Rechtsprechung des BGH (§ 906 BGB)
– Kalte Heizung: Minderung, Höhe im Einzelfall
– Anzeigepflicht (§ 536c BGB) und Kenntnis bei Vertragsschluss (§ 536b BGB), jeweils im Wortlaut
– Risiko zu hoher Minderung: Verzug, fristlose Kündigung (§ 543 BGB), Zahlung unter Vorbehalt, Zurückbehaltungsrecht (§ 320 BGB)
– Ergebnis, Klausurtipp, Prüfungsschema, Merksatz

Normen: §§ 535 Abs. 2, 536 Abs. 1, 536b, 536c BGB; § 441 Abs. 1 BGB (Vergleich); § 906 BGB; § 543 Abs. 2 Satz 1 Nr. 3 BGB; § 320 BGB; § 812 Abs. 1 Satz 1 Alt. 1 BGB

Rechtsprechung:
– BGH, Urt. v. 6.4.2005 – XII ZR 225/03 (Bemessung der Minderung von der Bruttomiete; Unerheblichkeit)
– BGH, Versäumnisurt. v. 1.3.2000 – XII ZR 272/97 (Beweislast nach Verantwortungsbereichen bei Feuchtigkeit)
– BGH, Urt. v. 5.12.2018 – VIII ZR 271/17 (Wärmebrücken und Schimmelgefahr im Altbau; zumutbares Lüften im Einzelfall)
– BGH, Urt. v. 29.4.2015 – VIII ZR 197/14, BGHZ 205, 177 (Bolzplatz: Lärm vom Nachbargrundstück)
– BGH, Urt. v. 29.4.2020 – VIII ZR 31/18 (Baustelle nebenan; Darlegungs- und Beweislast)
– BGH, Urt. v. 11.7.2012 – VIII ZR 138/11 (Fehleinschätzung der Schimmelursache, Zahlungsverzug, Kündigung; Zahlung unter Vorbehalt)
– BGH, Versäumnisurt. v. 17.6.2015 – VIII ZR 19/14 (Zurückbehaltungsrecht nach § 320 BGB zeitlich und betragsmäßig begrenzt)

Hinweise: Friedemann und Frau Teuber sind erfunden. Konkrete Minderungsquoten nennt das Video bewusst nicht; sie hängen vom Einzelfall ab. Schadensersatz (§ 536a BGB), Selbstbeseitigung und die Kündigung durch den Mieter behandelt das Video nicht. Die Minderung beim Kauf zeigt unsere Folge „§ 437 BGB: Die Käuferrechte auf einen Blick – Schema“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Mietrecht #Mietminderung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("Teuber: Der Schimmel", "Frau Teuber: Der Schimmel"), ("Römisch eins:", "Römisch I:"),
             ("Römisch zwei:", "Römisch II:"), ("Römisch drei:", "Römisch III:")]:
    if a in srt:
        srt = srt.replace(a, b)
srt, n = re.subn(r"§§ 536 und 536\n\n(\d+\n[^\n]+\n)a nicht zu\.", r"§§ 536 und 536a\n\n\1nicht zu.", srt)
assert n == 1, "536a"
srt, n = re.subn(r"aus § 535\n\n(\d+\n[^\n]+\n)Abs\. 2: ", r"aus § 535 Abs. 2:\n\n\1", srt)
assert n == 1, "535 Abs. 2"
srt, n = re.subn(r"achthundertfünfzig(\s)Euro", r"850\1€", srt)
assert n == 2, n
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|hundert", srt, re.I), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
