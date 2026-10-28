"""Nachbearbeitung der Upload-Texte für Folge 255 (nach meta_245.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Paragrafenzeichen nicht am Zeilenende).
Aufruf: python3 meta_255.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Kamera für 900 € mit „Sofort kaufen“"),
       (T("ansp"), "Anspruch auf die Kamera: zwei Stufen"),
       (T("ang"), "I. Angebot: Sofort kaufen statt Einladung"),
       (T("w145"), "Bindung an das Angebot, § 145 BGB"),
       (T("klick2"), "Annahme durch den Klick"),
       (T("anf"), "II. Anfechtung: § 119 I BGB"),
       (T("w1192"), "Eigenschaftsirrtum? § 119 II BGB und der Wert"),
       (T("motiv"), "Motivirrtum und Risiko des Verkäufers"),
       (T("erg"), "Ergebnis und Gegenfall: vertippt – 90 statt 900 €"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfungsschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""„Sofort kaufen“ geklickt: Ist das Festpreisangebot auf einer Plattform ein verbindliches Angebot an jedermann (§ 145 BGB) – und darf der Verkäufer anfechten, wenn er nur den Wert falsch eingeschätzt hat (§ 119 I, II BGB)?

Der Fall: Herr Eichler stellt seine seltene Kamera auf einer Plattform ein – fester Preis 900 €, Schaltfläche „Sofort kaufen“. Frau Hegemann klickt und zahlt. Am Abend sieht er: Vergleichbare Kameras kosten rund 2.500 €. Modell und Zustand kannte er genau, nur den Marktpreis hat er unterschätzt. Er ficht an. Muss er liefern?

Inhalt:
– Anspruch auf Übergabe und Übereignung (§ 433 Abs. 1 Satz 1 BGB) in zwei Stufen
– Abgrenzung zum Onlineshop (Einladung zum Angebot): Bei „Sofort kaufen“ bietet der Verkäufer selbst an
– Auslegung nach §§ 133, 157 BGB unter Einbeziehung der Plattformregeln; Angebot ad incertas personas
– § 145 BGB im Wortlaut: Bindung an das Angebot, Ausschluss nur ausdrücklich
– Annahme durch den Klick
– § 119 Abs. 1 BGB im Wortlaut: Wille und Erklärung stimmen überein
– § 119 Abs. 2 BGB im Wortlaut: Der Wert selbst ist keine verkehrswesentliche Eigenschaft
– Motivirrtum und Kalkulationsirrtum; das Risiko des zu niedrigen Preises trägt der Verkäufer
– Gegenfall: vertippt (90 statt 900 €) – Erklärungsirrtum und Vertrauensschaden (§ 122 BGB)
– Klausurtipp, Prüfungsschema, Merksatz

Normen: §§ 145, 133, 157 BGB; § 119 Abs. 1, 2 BGB; §§ 143, 142 Abs. 1 BGB; § 433 Abs. 1 Satz 1 BGB; Gegenfall §§ 121, 122 BGB

Rechtsprechung:
– BGH, Urt. v. 15.2.2017 – VIII ZR 59/16, Rn. 12, 23 (Sofort-Kaufen: Festpreisangebot des Verkäufers, Auslegung mit Plattform-AGB, Annahme durch den Klick)
– BGH, Urt. v. 8.6.2011 – VIII ZR 305/10, Rn. 15–17 (Auslegung nach §§ 133, 157 mit AGB; Bindung nach § 145 ausschließbar)
– BGH, Urt. v. 12.11.2014 – VIII ZR 42/14, Rn. 12 (Risiko eines niedrigen Startpreises beim Verkäufer)
– BGH, Urt. v. 26.1.2005 – VIII ZR 79/04 (Vertippen als Erklärungsirrtum; Kalkulationsirrtum als Motivirrtum)
– OLG Düsseldorf, Urt. v. 27.1.2000 – 6 U 168/98, Rn. 34; Beschl. v. 1.7.2025 – 3 W 63/25, Rn. 25 (Wert keine verkehrswesentliche Eigenschaft)

Hinweise: Herr Eichler, Frau Hegemann und die Plattform sind erfunden. Den Preisfehler im Onlineshop zeigt unsere Folge „Preisfehler Onlineshop: Muss der Händler liefern? (§ 119 BGB)“, Angebot und Annahme allgemein die Folge „Angebot und Annahme §§ 145 ff. BGB: Wann ist der Vertrag geschlossen?“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#SofortKaufen #Anfechtung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("Eichler: Ich habe den", "Herr Eichler: Ich habe den"), ("Hegemann: Ich habe auf", "Frau Hegemann: Ich habe auf"),
          ("und hundertsiebenundfünfzig", "und 157")]
for a, b in ERSATZ:
    assert a in srt, a
    srt = srt.replace(a, b)
for a, b in [(r"zweitausendfünfhundert(\s)Euro", r"2.500\1€"), (r"zweitausendfünfhundert wert", "2.500 € wert"),
             (r"neunhundert(\s)Euro", r"900\1€"), (r"stehen neunzig\.", "stehen 90 €.")]:
    assert re.search(a, srt), a
    srt = re.sub(a, b, srt)
srt = re.sub(r"(\d)\n€ ?", r"\1 €\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|tausend|hundert|zig\b", srt, re.I), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
