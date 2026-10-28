"""Nachbearbeitung der Upload-Texte für Folge 136 (Kopie von meta_129.py, nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Paragrafen-Umbruch in den Untertiteln, Sprecher „Frau Huber:“.
Aufruf: python3 meta_136.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Die brennende Mülltonne"),
       (T("agl"), "Anspruchsgrundlage: §§ 677, 683 S. 1, 670 BGB"),
       (T("p1"), "1. Geschäftsbesorgung und 2. fremdes Geschäft"),
       (T("p3"), "3. Ohne Auftrag, § 677 BGB"),
       (T("p4"), "4. Berechtigung: Interesse und mutmaßlicher Wille, § 683 S. 1 BGB"),
       (T("p679"), "Sonderregeln §§ 679, 680 BGB"),
       (T("p5"), "5. Rechtsfolge: Aufwendungsersatz, § 670 BGB"),
       (T("p5c"), "Die Jacke: Aufwendung oder Begleitschaden?"),
       (T("p684"), "Unberechtigte GoA, § 684 S. 1 BGB"),
       (T("erg"), "Ergebnis und Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""GoA Schema (§§ 677, 683 S. 1, 670 BGB): Wann ist die Geschäftsführung ohne Auftrag berechtigt und bekommt der Helfer am brennenden Mülleimer seine Jacke ersetzt?

Der Fall: Frau Huber ist zwei Wochen verreist. Am dritten Tag brennt die Mülltonne vor ihrem Haus, die Flammen drohen auf ihren Carport überzugreifen. Ihr Nachbar Harald hat keinen Feuerlöscher zur Hand und erstickt das Feuer mit seiner Jacke. Niemand wird verletzt, aber die Jacke (noch 250 Euro wert) ist ruiniert. Frau Huber bedankt sich – um Hilfe gebeten habe sie aber nicht. Muss sie die Jacke bezahlen?

Inhalt (als Prüfungsschema):
– Anspruchsgrundlage: Aufwendungsersatz aus berechtigter GoA, §§ 677, 683 S. 1, 670 BGB
– 1. Geschäftsbesorgung: jede Tätigkeit, auch eine rein tatsächliche
– 2. Fremdes Geschäft: objektiv fremd, Vermutung des Fremdgeschäftsführungswillens, auch-fremdes Geschäft
– 3. Ohne Auftrag oder sonstige Berechtigung (§ 677 BGB, Wortlaut)
– 4. Berechtigung (§ 683 S. 1 BGB, Wortlaut): Interesse und wirklicher oder mutmaßlicher Wille im Zeitpunkt der Übernahme; § 679 und § 680 BGB kurz
– 5. Rechtsfolge (§ 670 BGB, Wortlaut): erforderliche Aufwendungen, freiwillige Vermögensopfer, risikotypische Begleitschäden
– Abgrenzung: unberechtigte GoA, § 684 S. 1 BGB (Bereicherungsrecht)
– Ergebnis, Klausurtipp, Klausurschema, Merksatz

Rechtsprechung:
– BGH, Urt. v. 5.7.2018 – III ZR 273/16, Rn. 20, 28: Vermutung des Fremdgeschäftsführungswillens bei objektiv fremden und auch-fremden Geschäften; Aufwendungen als freiwillige Vermögensopfer
– BGH, Urt. v. 1.2.2018 – III ZR 53/17, Rn. 8: Vermutung bei objektiv fremden Geschäften
– BGH, Urt. v. 11.3.2016 – V ZR 102/15, Rn. 8, 12: Interesse (objektiv nützlich) und mutmaßlicher Wille im Zeitpunkt der Übernahme
– BGH, Urt. v. 14.6.2018 – III ZR 54/17, Rn. 48, 55: Haftungsmilderung des Nothelfers nach § 680 BGB
– BGH, Urt. v. 19.5.2016 – III ZR 399/14, Rn. 17: Aufwendungen sind freiwillige Vermögensopfer
– BGH, Urt. v. 21.6.2012 – III ZR 291/11, Rn. 12: Geschäftsbesorgung umfasst auch rein tatsächliche Handlungen (zu § 662 BGB)

Hinweise: Der Fall ist erfunden. Dass auch unfreiwillige, risikotypische Begleitschäden des Helfers nach § 670 BGB ersetzt werden, ist herrschende Meinung; eine BGH-Entscheidung mit Randnummern dazu haben wir nicht herangezogen. Ob bei geopferten Sachen der Neupreis oder der Zeitwert zählt, lässt das Video offen (Harald verlangt nur den Restwert). Das Bereicherungsrecht erklärt Folge 73, den Anspruchsaufbau Folge 6.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026 (BGB zuletzt geändert durch Gesetz vom 23.7.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#GoA #Zivilrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt).replace("\nHuber: ", "\nFrau Huber: ")
srt = srt.replace("und sechshundertsiebzig", "und 670").replace("zweihundertfünfzig Euro", "250 Euro")
assert "sechshundert" not in srt
assert not re.search(r"§\n", srt)
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
