"""Nachbearbeitung der Upload-Texte für Folge 251 (nach meta_245.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Paragrafenzeichen nicht am Zeilenende).
Aufruf: python3 meta_251.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Fernseher für 49 statt 499 €"),
       (T("ansp"), "Anspruch auf Lieferung: zwei Stufen"),
       (T("inv"), "I. Vertragsschluss: Shopseite und Bestellung"),
       (T("w312"), "Eingangsbestätigung (§ 312i BGB): keine Annahme"),
       (T("ann"), "Die zweite Mail: Annahme"),
       (T("anf"), "II. Anfechtung: Erklärungsirrtum, § 119 I BGB"),
       (T("w120"), "Softwarefehler: der BGH und § 120 BGB"),
       (T("fort"), "Was wird angefochten?"),
       (T("kalk"), "Abgrenzung: Kalkulationsirrtum"),
       (T("frist"), "Frist (§ 121) und Nichtigkeit (§ 142 I)"),
       (T("w122"), "Vertrauensschaden nach § 122 BGB"),
       (T("erg"), "Ergebnis und Klausurtipp"),
       (T("sch"), "Prüfungsschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Preisfehler Onlineshop: Ist die automatische Eingangsbestätigung schon Annahme, und kann der Händler einen Eingabe- oder Softwarefehler nach § 119 I BGB anfechten? Mit dem Gedanken des § 120 BGB und BGH VIII ZR 79/04.

Der Fall: Im Onlineshop von Frau Wetzel kostet ein Fernseher plötzlich 49 € statt 499 € – die Software hat den eingegebenen Preis falsch in den Shop übertragen. Herr Kübler bestellt sofort und bekommt eine automatische Mail „Vielen Dank, wir haben Ihre Bestellung erhalten.“, am nächsten Morgen eine zweite: „Ihr Auftrag wird jetzt von unserer Versandabteilung bearbeitet.“ Mittags ficht Frau Wetzel an. Muss sie liefern?

Inhalt:
– Anspruch auf Lieferung (§ 433 Abs. 1 Satz 1 BGB) in zwei Stufen: Vertrag zustande gekommen? Durch Anfechtung weggefallen?
– Shopseite als Einladung zum Angebot (invitatio ad offerendum), Bestellung als Angebot
– § 312i Abs. 1 Satz 1 Nr. 3 BGB im Wortlaut: Die Eingangsbestätigung ist in der Regel nur eine Wissenserklärung
– Die zweite Mail kündigt die Ausführung an: Annahme – auch wenn sie automatisch verschickt wird
– § 119 Abs. 1 BGB im Wortlaut: Vertippen als Erklärungsirrtum
– § 120 BGB im Wortlaut: Softwarefehler bei der Datenübertragung nach dem BGH ebenfalls Erklärungsirrtum
– Angefochten wird die Annahme: Der Fehler wirkt fort
– Abgrenzung zum Kalkulationsirrtum (Irrtum im Beweggrund)
– Anfechtungsfrist „unverzüglich“ (§ 121 BGB), Nichtigkeit von Anfang an (§ 142 Abs. 1 BGB)
– § 122 BGB im Wortlaut: Vertrauensschaden statt Erfüllung, Ausschluss nach Abs. 2
– Ergebnis, Klausurtipp, Prüfungsschema, Merksatz

Normen: §§ 119 Abs. 1, 120, 121, 122, 142 Abs. 1, 143 BGB; § 312i Abs. 1 Satz 1 Nr. 3 BGB; § 433 Abs. 1 Satz 1 BGB

Rechtsprechung:
– BGH, Urt. v. 26.1.2005 – VIII ZR 79/04, NJW 2005, 976 (falscher Preis durch Fehler im Datentransfer: Erklärungsirrtum; automatische Mail als Annahme; Abgrenzung Kalkulationsirrtum)
– BGH, Urt. v. 16.10.2012 – X ZR 37/12, Rn. 14, 17, 19 (Buchungsmaske als Aufforderung zum Angebot; automatisierte Erklärungen; Eingangsbestätigung in der Regel Wissenserklärung)
– BGH, Versäumnisurt. v. 18.5.2017 – VII ZR 122/14, Rn. 23 (Vertrauensschaden und Erfüllungsinteresse)

Hinweise: Herr Kübler, Frau Wetzel und der Onlineshop sind erfunden. Wie Angebot und Annahme funktionieren, zeigt unsere Folge „Angebot und Annahme: Wann ist ein Vertrag wirklich geschlossen?“, das vollständige Anfechtungsschema die Folge „Anfechtung in fünf Schritten“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Preisfehler #Anfechtung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("Wetzel: Der Preis", "Frau Wetzel: Der Preis"), ("Kübler: Aber ich", "Herr Kübler: Aber ich"),
          ("nur neunundvierzig\n", "nur 49 €.\n"), ("\nEuro. Sonst verlangt sie", "\nSonst verlangt sie"),
          ("vierhundertneunundneunzig.", "499 €."), ("§ 312i Abs. 1 S. 1\nNr. 3", "§ 312i Abs. 1 Satz 1\nNr. 3")]
for a, b in ERSATZ:
    assert a in srt, a
    srt = srt.replace(a, b)
for a, b in [(r"vierhundertneunundneunzig(\s)Euro", r"499\1€"), (r"neunundvierzig(\s)Euro", r"49\1€")]:
    assert re.search(a, srt), a
    srt = re.sub(a, b, srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|tausend|hundert|zig\b", srt, re.I), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
