"""Nachbearbeitung der Upload-Texte für Folge 276 (nach meta_255.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Paragrafenzeichen nicht am Zeilenende).
Aufruf: python3 meta_276.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Jacke für 20 statt 200 € im Schaufenster"),
       (T("ansp"), "Anspruch: Wer hat das Angebot gemacht?"),
       (T("w145"), "Angebot und Rechtsbindungswille, § 145 BGB"),
       (T("w133"), "Auslegung nach §§ 133, 157 BGB"),
       (T("schauf"), "Schaufenster, Katalog, Prospekt: invitatio ad offerendum"),
       (T("edang"), "Das Angebot macht die Kundin"),
       (T("abgr"), "Abgrenzung: Selbstbedienungsladen und Tankstelle"),
       (T("auto"), "Abgrenzung: Automat, Onlineshop, Sofort kaufen"),
       (T("erg"), "Ergebnis und Preisangabenrecht"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfungsschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Invitatio ad offerendum: Ist der Preis im Schaufenster schon ein Angebot nach § 145 BGB – oder nur eine Einladung, selbst ein Angebot abzugeben? Und wie grenzt du Schaufenster, Katalog und Prospekt vom Selbstbedienungsladen, von der Tankstelle, vom Warenautomaten, vom Onlineshop und von „Sofort kaufen“ ab?

Der Fall: Im Schaufenster eines kleinen Modegeschäfts hängt eine Wolljacke, auf dem Preisschild stehen 20 € – gemeint waren 200 €. Edelgard verlangt die Jacke für 20 €. Herr Böckmann, der Inhaber, lehnt ab. Muss er sie zu dem Preis verkaufen?

Inhalt:
– Anspruch auf Übergabe und Übereignung (§ 433 Abs. 1 Satz 1 BGB): Wer hat das Angebot gemacht?
– § 145 BGB im Wortlaut: Angebot und Rechtsbindungswille
– §§ 133, 157 BGB im Wortlaut: Auslegung aus Sicht eines verständigen Empfängers
– Schaufenster, Katalog, Prospekt: invitatio ad offerendum – Gründe: Vorrat, Zahlungsfähigkeit des Kunden, Zahl der Interessenten
– Das Angebot macht die Kundin; Ablehnung und Erlöschen (§ 146 BGB)
– Abgrenzung: Selbstbedienungsladen (Streit um den Vertragsschluss an der Kasse), Selbstbedienungstankstelle, Warenautomat, Onlineshop, „Sofort kaufen“
– Ergebnis; Preisangabenverordnung: falsches Preisschild, aber kein Kaufvertrag
– Klausurtipp, Prüfungsschema, Merksatz

Normen: §§ 145, 133, 157 BGB; § 146 BGB; § 433 Abs. 1 Satz 1 BGB; § 10 Abs. 1, § 20 Nr. 1 PAngV

Rechtsprechung:
– BGH, Urt. v. 21.5.2026 – III ZR 220/25, Rn. 13 (Werbeschreiben als invitatio ad offerendum mangels Rechtsbindungswillens)
– BGH, Urt. v. 3.5.2012 – III ZR 62/11, Rn. 11 (Anzeigen an einen unbestimmten Kreis von Interessenten als invitatio)
– BGH, Urt. v. 25.10.2017 – 1 StR 146/17, Rn. 21 (Sinn der invitatio: eigene Leistungsfähigkeit und Zahlungsfähigkeit des Vertragspartners prüfen)
– BGH, Urt. v. 26.1.2005 – VIII ZR 79/04 (Internetpräsentation als invitatio; Auslegung aus Sicht eines verständigen Erklärungsempfängers)
– BGH, Urt. v. 4.5.2011 – VIII ZR 171/10, Rn. 13–16 (Selbstbedienungstankstelle: Kaufvertrag schon beim Tanken; im Selbstbedienungsladen bindet die Entnahme aus dem Regal noch nicht)
– BGH, Urt. v. 15.2.2017 – VIII ZR 59/16, Rn. 12 („Sofort kaufen“: Angebot des Verkäufers zum Festpreis)

Hinweise: Edelgard, Herr Böckmann und das Modegeschäft sind erfunden. Schaufenster, Katalog und Prospekt als invitatio sowie das Angebot durch das Aufstellen eines Warenautomaten entsprechen der herrschenden bzw. überwiegenden Ansicht; wie der Vertrag im Selbstbedienungsladen an der Kasse zustande kommt, ist umstritten. Den Preisfehler im Onlineshop zeigt unsere Folge „Preisfehler Onlineshop: Muss der Händler liefern? (§ 119 BGB)“, den Sofortkauf auf einer Plattform die Folge „„Sofort kaufen“ geklickt: Ist der Verkäufer an den Preis gebunden?“, Angebot und Annahme allgemein die Folge „Angebot und Annahme §§ 145 ff. BGB: Wann ist der Vertrag geschlossen?“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#InvitatioAdOfferendum #BGBAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("Boeckmann: Das tut", "Herr Böckmann: Das tut"), ("§§ 133 und 157", "§§ 133 und 157"),
          ("steht zwanzig.", "steht 20."), ("könnten zehn", "könnten 10"), ("wäre zehnmal", "wäre 10-mal"),
          ("Römisch eins:", "Römisch I:"), ("Römisch zwei:", "Römisch II:"),
          ("Schild steht zwanzig\n", "Schild steht 20 €\n"), ("\nEuro statt zweihundert.", "\nstatt 200."),
          ("Jacke für zwanzig\n\n", "Jacke für 20 €,\n\n"), ("\nEuro, nach §", "\nnach §")]
for a, b in ERSATZ:
    assert a in srt, a
    srt = srt.replace(a, b)
for a, b in [(r"zwanzig(\s)Euro", r"20\1€"),
             (r"zweihundert(\s)Euro", r"200\1€"), (r"waren zweihundert;", "waren 200 €;")]:
    assert re.search(a, srt), a
    srt = re.sub(a, b, srt)
srt = re.sub(r"(?m)^((?!\d\d:\d\d:).*\d)\n€ ?", r"\1 €\n", srt)   # nicht an Zeitstempel-Zeilen
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|tausend|hundert|zig\b|zehn", srt, re.I), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
