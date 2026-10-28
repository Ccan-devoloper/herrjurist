"""Nachbearbeitung der Upload-Texte für Folge 248 (nach meta_245.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Paragrafenzeichen nicht am Zeilenende).
Aufruf: python3 meta_248.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Die GbR zahlt nicht – privat haften?"),
       (T("sv"), "Sachverhalt; I. Schuldnerin ist die GbR selbst"),
       (T("p721"), "II. § 721 BGB im Wortlaut, Rechtsstand MoPeG"),
       (T("merk"), "Persönlich, unbeschränkt, primär, akzessorisch"),
       (T("eintr"), "III. Eintritt: Haftung für Altschulden, § 721a"),
       (T("einw"), "IV. Einwendungen und Aufrechnung, § 721b"),
       (T("aus"), "V. Ausgeschieden: Nachhaftung, § 728b"),
       (T("vollstr"), "VI. Vollstreckung: § 722 Abs. 2 BGB"),
       (T("innen"), "VII. Innenausgleich: § 716 Abs. 1, § 426"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp: die Zeitleiste"),
       (T("sch"), "Prüfungsschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Gesellschafterhaftung GbR nach §§ 721–721b BGB: Wann greift der Gläubiger auf dein Privatkonto zu – auch nach Eintritt oder Austritt (§ 728b BGB)?

Der Fall: Philipp und Mathilde führen ein Architekturbüro als GbR. Das Büro kauft beim Tischler Herrn Altmann Möbel für 18.000 €. Danach tritt Alma ein – „für alte Rechnungen hafte ich aber nicht“ –, und Mathilde scheidet aus. Im Juli ist das Konto des Büros leer, und Herr Altmann verlangt das Geld von Philipp privat. Dabei schuldet er dem Büro selbst noch 3.000 € Honorar. Muss Philipp zahlen – und haften auch Alma und Mathilde?

Inhalt:
– Schuldnerin ist die rechtsfähige GbR selbst (§ 705 Abs. 2, § 433 Abs. 2 BGB)
– § 721 BGB im Wortlaut: persönlich, unbeschränkt, unmittelbar und primär, als Gesamtschuldner, akzessorisch; früher entsprechend dem OHG-Recht, seit 1.1.2024 im Gesetz
– § 721a BGB im Wortlaut: Haftung des Eintretenden für Altschulden, interne Abreden Dritten gegenüber unwirksam
– § 721b BGB im Wortlaut: Einwendungen und Einreden der Gesellschaft, Leistungsverweigerung bei Anfechtungs- oder Aufrechnungsrecht der Gesellschaft
– § 728b BGB im Wortlaut: Nachhaftung des Ausgeschiedenen, Fünfjahresfrist ab Kenntnis des Gläubigers
– § 722 Abs. 2 BGB im Wortlaut: kein Zugriff aufs Privatvermögen mit einem Titel nur gegen die GbR
– Innenausgleich: Ersatz von der Gesellschaft (§ 716 Abs. 1 BGB), Regress gegen Mitgesellschafter nur nachrangig (§ 426 BGB)
– Ergebnis, Klausurtipp (Zeitleiste je Gesellschafter), Prüfungsschema, Merksatz

Normen: §§ 721, 721a, 721b, 722 Abs. 2, 728b BGB; § 705 Abs. 2, § 716 Abs. 1, §§ 387, 389, 421, 426, 433 Abs. 2 BGB; § 197 Abs. 1 Nr. 3 BGB

Rechtsprechung und Materialien:
– BGH, Urt. v. 29.1.2001 – II ZR 331/00, BGHZ 146, 341 („ARGE Weißes Roß“), Leitsatz c (Akzessorietät)
– BGH, Urt. v. 17.1.2012 – II ZR 197/10, Rn. 14 (Altverbindlichkeit)
– BGH, Urt. v. 8.10.2013 – II ZR 310/12, Rn. 34 f. (Innenausgleich)
– Regierungsentwurf MoPeG, BT-Drs. 19/27635, S. 157, 165–169, 177

Hinweise: Philipp, Alma, Mathilde und Herr Altmann sind erfunden. Wie die GbR entsteht und wann sie rechtsfähig ist, zeigt unsere Folge „GbR nach MoPeG: Rechtsfähig, eingetragen, haftend“; den Ausgleich unter Gesamtschuldnern unsere Folge „Gesamtschuld §§ 421, 426 BGB“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#GbR #Gesellschaftsrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\nAltmann: ", "\nHerr Altmann: ", srt)
for a, b in [(r"achtzehntausend(\s)Euro", r"18.000\1€"), (r"dreitausend(\s)Euro", r"3.000\1€"),
             (r"fünfzehntausend(\s)Euro", r"15.000\1€"), (r"übrigen dreitausend", "übrigen 3.000"),
             (r"nach S\. 2 Dritten", "nach Satz 2 Dritten")]:
    assert re.search(a, srt), a
    srt = re.sub(a, b, srt)
srt = re.sub(r"§ 721\n?( ?)a\b", lambda m_: "§ 721a" + ("\n" if "\n" in m_.group(0) else ""), srt)
srt = re.sub(r"§ 721\n\n(\d+\n[^\n]+\n)a, ", r"§ 721a,\n\n\1", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert "§ 721 a" not in srt and "S. 2" not in srt
assert "Herr Altmann: Die" in srt
assert not re.search(r"§\n|Abs\.\n|tausend|hundert", srt, re.I), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
