"""Nachbearbeitung der Upload-Texte für Folge 252 (nach meta_249.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, RiStBV, Rechtsprechung mit Rn., Hinweisen
und Lizenzzeile; Untertitel-Korrekturen (Zahlen in Ziffern, Normangaben nicht über den Zeilenumbruch getrennt).
Aufruf: python3 meta_252.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Anklage zum Schöffengericht"),
       (T("frage"), "Die Frage und der Sachverhalt"),
       (T("p200"), "§ 200 Abs. 1 StPO: der Anklagesatz"),
       (T("abs2"), "§ 200 Abs. 2 StPO und Nr. 110 RiStBV"),
       (T("kopf"), "Schritt 1: Kopf und Personalien"),
       (T("as"), "Schritt 2: Anklagesatz – gesetzliche Merkmale"),
       (T("konkr"), "Schritt 2: konkreter Tatvorwurf"),
       (T("bm"), "Schritt 3: Beweismittel"),
       (T("we"), "Schritt 4: wesentliches Ergebnis"),
       (T("an"), "Schritt 5: Antrag und Gericht"),
       (T("fehler"), "Zwei typische Fehler"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Anklageschrift nach § 200 StPO: Personalien, Anklagesatz, Vorschriften, Beweismittel, wesentliches Ergebnis und Anträge – in der richtigen Reihenfolge, Schritt für Schritt an einem Muster.

Der Fall: Referendar Hiller hat den hinreichenden Tatverdacht bejaht und soll für Oberstaatsanwalt Endres die Anklage zum Schöffengericht schreiben. In der Akte: Jemand steigt durch das offene Küchenfenster in die Wohnung von Frau Probst und nimmt Schmuck für 2.400 € mit; am Fensterrahmen sind Fingerabdrücke von Herrn Unger, am nächsten Tag verkauft er einen Ring daraus. Was gehört in die Anklageschrift, und in welcher Reihenfolge?

Inhalt:
– § 200 Abs. 1 StPO im Wortlaut: Angeschuldigter, Tat, Zeit und Ort, gesetzliche Merkmale, Strafvorschriften (Anklagesatz); Beweismittel, Gericht, Verteidiger
– § 200 Abs. 2 StPO: wesentliches Ergebnis der Ermittlungen – beim Schöffengericht Pflicht
– Nr. 110 RiStBV: klar, übersichtlich, für den Angeschuldigten verständlich
– Muster Schritt für Schritt: Kopf und Personalien, Verteidiger (§ 140 Abs. 1 StPO), Anklagesatz mit gesetzlichen Merkmalen, konkretem Tatvorwurf und Paragrafenkette, Beweismittel, wesentliches Ergebnis, Antrag auf Eröffnung
– Warum Schöffengericht? (§§ 24, 25, 28 GVG)
– Typische Fehler: Tatzeit/Tatort fehlen, Tat zu ungenau (Umgrenzungsfunktion)
– Klausurtipp, Schema, Merksatz

Normen: §§ 140 Abs. 1 Nr. 1, 2, 199 Abs. 2, 200, 207 Abs. 1 StPO; §§ 24, 25, 28 GVG; §§ 12, 242, 244 Abs. 1 Nr. 3, Abs. 4 StGB.
Richtlinien: Nr. 110, 111 RiStBV (Fassung vom 28.3.2023).

Rechtsprechung:
– BGH, Beschl. v. 21.12.2021 – StB 39/21, Rn. 17 f. (Umgrenzungsfunktion der Anklage)

Hinweise: Referendar Hiller, Oberstaatsanwalt Endres, Herr Unger, Frau Probst und die Stadt Ahornstadt sind erfunden; das Muster ist ein eigenes Lernmuster. Die genaue Form der Anklageschrift unterscheidet sich von Land zu Land – maßgeblich sind die Hinweise deines Prüfungsamts. Mehr dazu: Folge 39 (Anklageklausur), Folge 60 (hinreichender Tatverdacht), Folge 114 (Zuständigkeit nach Straferwartung).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Anklageschrift #StPO #Referendariat
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(§§? \d+)\n(Abs\. \d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Nr\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r" \n", "\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
for alt, neu, n in [("zehnten März", "10. März", 2), ("vierzehn Uhr", "14 Uhr", 2),
                    ("zweitausendvierhundert Euro", "2.400 Euro", 2), ("Lindenweg vier", "Lindenweg 4", 1),
                    ("hundertvierzehn.", "114.", 1)]:
    assert srt.count(alt) == n, (alt, srt.count(alt))
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n|Abs\.\n|Nr\.\n|Paragraf |zweitausend|vierzehn", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Anklageschrift Muster", "Schöffengericht", "Umgrenzungsfunktion"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
