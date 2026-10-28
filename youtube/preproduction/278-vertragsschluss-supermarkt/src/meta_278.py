"""Nachbearbeitung der Upload-Texte für Folge 278 (nach meta_276.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung, Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Paragrafenzeichen nicht am Zeilenende).
Aufruf: python3 meta_278.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Die Milchflasche zerbricht im Gang"),
       (T("ansp"), "Anspruch auf den Kaufpreis, § 433 Abs. 2 BGB"),
       (T("streit"), "Streit: Wann kommt der Kaufvertrag im Supermarkt zustande?"),
       (T("beide"), "Folge für die Flasche: noch kein Kaufvertrag"),
       (T("w311"), "Culpa in contrahendo: §§ 311 Abs. 2, 241 Abs. 2 BGB"),
       (T("w280"), "§ 280 Abs. 1 BGB: vermutetes Vertretenmüssen"),
       (T("d823"), "Delikt und Beweislast"),
       (T("gegen"), "Umgekehrt: Schutzpflicht des Ladens (Gemüseblatt-Fall)"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfungsschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Vertragsschluss im Supermarkt: Ist die Ware im Regal schon ein Angebot nach § 145 BGB – oder machst du das Angebot erst an der Kasse? Und wer haftet, wenn dir die Glasflasche schon im Gang aus der Hand rutscht?

Der Fall: Erhard nimmt im Supermarkt eine kalte Glasflasche Milch aus dem Kühlregal, mit einer Hand, den Blick auf dem Handy. Die beschlagene Flasche rutscht ihm durch die Finger und zerbricht; verletzt wird niemand. Die Filialleiterin verlangt 1,49 €. Erhard: „Gekauft habe ich sie doch noch gar nicht.“

Inhalt:
– Anspruch auf den Kaufpreis (§ 433 Abs. 2 BGB im Wortlaut): Gibt es schon einen Kaufvertrag?
– Der Streit: Warenauslage als Angebot, Annahme durch Vorlegen an der Kasse – oder Auslage als Einladung, Angebot durch Vorlegen, Annahme durch Registrieren (so beschrieben im Gemüseblatt-Fall, BGHZ 66, 51); je ein Argument, Jugendschutz (§ 9 JuSchG)
– Folge für die Flasche: Nach beiden Ansichten kommt der Kaufvertrag erst an der Kasse zustande – der Streit kann offenbleiben
– Haftung vor der Kasse: §§ 311 Abs. 2 Nr. 2, 241 Abs. 2 und 280 Abs. 1 BGB im Wortlaut, vermutetes Vertretenmüssen, Fahrlässigkeit
– Daneben § 823 Abs. 1 BGB: Beweislast im Vergleich
– Umgekehrt: Schutzpflicht des Ladens (Gemüseblatt-Fall)
– Ergebnis, Klausurtipp, Prüfungsschema, Merksatz

Normen: § 433 Abs. 2 BGB; §§ 145 ff. BGB; §§ 280 Abs. 1, 241 Abs. 2, 311 Abs. 2 Nr. 2 BGB; § 276 Abs. 2 BGB; § 823 Abs. 1 BGB; § 9 Abs. 1 Nr. 2 JuSchG

Rechtsprechung:
– BGH, Urt. v. 28.1.1976 – VIII ZR 246/74, BGHZ 66, 51 (Gemüseblatt-Fall: Streit um den Vertragsschluss im Selbstbedienungsladen offengelassen; Schutzpflichten schon vor Vertragsschluss; Beweisvorteil der culpa in contrahendo gegenüber dem Delikt)
– BGH, Urt. v. 4.5.2011 – VIII ZR 171/10, Rn. 14 f. (Selbstbedienungsladen: Die Entnahme aus dem Regal bindet noch nicht)

Hinweise: Erhard, Frau Kesting und der Supermarkt sind erfunden. Welche der beiden Ansichten zum Vertragsschluss herrschend ist, ist im Schrifttum umstritten; im Video ist die zweite als überwiegende Ansicht bezeichnet. Wie hoch der zu ersetzende Schaden ist, behandelt das Video nicht. Die Grundlagen zeigen unsere Folgen „Invitatio ad offerendum: Ist der Preis im Schaufenster ein Angebot?“, „Angebot und Annahme §§ 145 ff. BGB: Wann ist der Vertrag geschlossen?“, „Haftung ohne Vertrag? Culpa in contrahendo und der Linoleumrollen-Fall“ und zum Schutz des Kindes „Gemüseblatt-Fall: Vertrag mit Schutzwirkung für Dritte erklärt“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Vertragsschluss #BGBAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("Kesting: Die Flasche", "Frau Kesting: Die Flasche"), ("Römisch eins:", "Römisch I:"),
             ("Römisch zwei:", "Römisch II:"), ("Römisch drei:", "Römisch III:")]:
    assert a in srt, a
    srt = srt.replace(a, b)
for a, b in [(r"einen(\s)Euro(\s)neunundvierzig", r"1,49\1€")]:
    assert re.search(a, srt), a
    srt = re.sub(a, b, srt)
srt, n = re.subn(r"§§ 145\n\n(\d+\n[^\n]+\n)folgende\. ", r"§§ 145 ff.\n\n\1", srt)
assert n == 1, "§§ 145 ff."
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|hundert|neunundvierzig", srt, re.I), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
