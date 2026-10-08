"""Nachbearbeitung der Upload-Texte für Folge 265 (nach meta_262.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung und
Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen).
Aufruf: python3 meta_265.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: „Gekauft wie gesehen, keine Gewährleistung“"),
       (T("mangel"), "1. Sachmangel, § 434 BGB"),
       (T("aus"), "2. Ist der Ausschluss wirksam? (§ 476, § 309 Nr. 7 BGB)"),
       (T("ausl"), "3. Reichweite von „gekauft wie gesehen“"),
       (T("p444"), "Grenze § 444 BGB: Arglist und Garantie"),
       (T("vorrang"), "Die vereinbarte Beschaffenheit geht vor (BGHZ 170, 86)"),
       (T("var"), "Ergebnis je Variante"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfungsschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Gewährleistungsausschluss „gekauft wie gesehen“: Wann ist er wirksam, wann scheitert er an Arglist oder Garantie (§ 444 BGB) und warum geht eine Beschaffenheitsvereinbarung vor?

Der Fall: Christel kauft von Herrn Burmeister, einer Privatperson, dessen alten Kleinwagen für 4.500 €. Im handschriftlichen Kaufvertrag steht „Motor läuft einwandfrei.“ – und darunter „Gekauft wie gesehen, keine Gewährleistung.“ 3 Wochen später ist der Motor hinüber; der Schaden war schon beim Kauf da. Herr Burmeister wusste davon nichts und beruft sich auf den Ausschluss. Hat Christel trotzdem Mängelrechte?

Inhalt:
– Sachmangel nach § 434 BGB (subjektive und objektive Anforderungen) im Wortlaut
– Ist der Ausschluss wirksam? Privatverkauf, § 476 BGB nur beim Verbrauchsgüterkauf, Individualvereinbarung, AGB-Grenze § 309 Nr. 7 BGB
– Auslegung: „gekauft wie gesehen“ allein erfasst in aller Regel nur wahrnehmbare Mängel; zusammen mit „keine Gewährleistung“ umfassender Ausschluss
– § 444 BGB im Wortlaut: Arglist und Garantie; Garantie beim Privatverkauf nur ausnahmsweise
– BGHZ 170, 86: Der Ausschluss gilt in der Regel nicht für das Fehlen der vereinbarten Beschaffenheit
– Ergebnis je Variante, Klausurtipp, Prüfungsschema, Merksatz

Normen: §§ 434, 444, 476 BGB; §§ 305 Abs. 1, 309 Nr. 7 BGB; §§ 437, 439, 474 BGB

Rechtsprechung: BGH, Urt. v. 29.11.2006 – VIII ZR 92/06, BGHZ 170, 86 (Rn. 20, 25 f., 30 f.); BGH, Urt. v. 10.4.2024 – VIII ZR 161/23 (Rn. 21, 23, 38, 40); BGH, Urt. v. 6.7.2005 – VIII ZR 136/04 („gekauft wie gesehen“ und Ausschluss jeder Gewährleistung); BGH, Urt. v. 6.4.2016 – VIII ZR 261/14 („wie besichtigt“, Rn. 22, 24).

Hinweise: Christel, Herr Burmeister und die Mechanikerin sind erfunden; der Ausschluss ist im Fall einzeln ausgehandelt. Die zitierten BGH-Entscheidungen ergingen zu § 434 BGB in der bis 31.12.2021 geltenden Fassung; die vereinbarte Beschaffenheit steht heute in § 434 Abs. 2 S. 1 Nr. 1 BGB. Wann eine Sache mangelhaft ist, zeigt unsere Folge „Sachmangel § 434 BGB: Wann ist eine Sache mangelhaft?“, die Käuferrechte die Folge „§ 437 BGB: Die Käuferrechte auf einen Blick“, den Händler, der einen Unfallschaden verschweigt, die Folge „Unfallwagen verschwiegen: Arglistige Täuschung oder Mängelrechte?“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Gewährleistungsausschluss #Kaufrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(^|\n)Burmeister: ", r"\1Herr Burmeister: ", srt)
ZAHL = [(r"[Vv]iertausendfünfhundert(\s)Euro", r"4.500\1€"), (r"Drei(\s)Wochen", r"3\1Wochen")]
for a, b in ZAHL:
    srt = re.sub(a, b, srt)
srt = re.sub(r"(\d)\n€ ?", r"\1 €\n", srt)
assert not re.search(r"§\n|viertausend|(^|\n)Burmeister:", srt), "SRT-Korrektur unvollständig"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
