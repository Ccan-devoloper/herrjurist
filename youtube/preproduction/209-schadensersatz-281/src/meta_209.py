"""Nachbearbeitung der Upload-Texte für Folge 209 (nach meta_206.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen).
Aufruf: python3 meta_209.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Die Felgen kommen nicht"),
       (T("frage"), "Kann Jörn die Mehrkosten verlangen? Sachverhalt"),
       (T("agl"), "Anspruchsgrundlage: §§ 280 Abs. 1, 3, 281 BGB"),
       (T("s1"), "1. Schuldverhältnis und 2. Pflichtverletzung"),
       (T("f1"), "3. Fristsetzung: Genügt „umgehend“?"),
       (T("e1"), "4. Entbehrlichkeit, § 281 Abs. 2 BGB"),
       (T("v1"), "5. Vertretenmüssen"),
       (T("d1"), "6. Schaden: Deckungskauf, 250 € Mehrkosten"),
       (T("r1"), "Folge: § 281 Abs. 4 BGB"),
       (T("ab1"), "Abgrenzung: Verzögerungsschaden, Rücktritt, § 325 BGB"),
       (T("erg"), "Ergebnis und Klausurtipp"),
       (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Schadensersatz statt der Leistung (§§ 280 I, III, 281 BGB) im Schema: Fristsetzung, Entbehrlichkeit, Deckungskauf – wenn der Händler die bezahlten Felgen nicht liefert.

Der Fall: Jörn kauft im Reifenhandel von Ingolf vier Felgen für 1.200 € und zahlt sofort. Die Lieferung bis zum 8. September bleibt aus. Jörn schreibt: „Bitte liefern Sie die Felgen umgehend.“ Ingolf vertröstet ihn. Drei Wochen später kauft Jörn gleichwertige Felgen bei einer anderen Händlerin für 1.450 € und verlangt von Ingolf sein Geld zurück und die 250 € Mehrkosten.

Inhalt:
– Anspruchsgrundlage §§ 280 Abs. 1, 3, 281 BGB; § 280 Abs. 1 und 3 BGB im Wortlaut
– § 281 Abs. 1 Satz 1 BGB im Wortlaut: fällige Leistung nicht erbracht, erfolglose angemessene Frist
– 1. Schuldverhältnis, 2. Pflichtverletzung (fällig, durchsetzbar)
– 3. Fristsetzung: „umgehend“ genügt, kein Endtermin nötig, zu kurze Frist setzt eine angemessene in Gang
– 4. Entbehrlichkeit nach § 281 Abs. 2 BGB im Wortlaut: ernsthafte und endgültige Verweigerung, besondere Umstände
– 5. Vertretenmüssen (vermutet, § 280 Abs. 1 Satz 2 BGB)
– 6. Schaden: Rechenweg 1.450 € – 1.200 € = 250 € (Deckungskauf)
– Folge: § 281 Abs. 4 BGB im Wortlaut – kein Anspruch mehr auf die Leistung
– Abgrenzung: Verzögerungsschaden (§§ 280 Abs. 1, 2, 286 BGB), Rücktritt (§ 323 BGB), § 325 BGB
– Klausurtipp, Klausurschema, Merksatz

Normen: §§ 249 Abs. 1, 271 Abs. 2, 280 Abs. 1–3, 281 Abs. 1, 2, 4, 286, 320, 323, 325, 346 Abs. 1, 433 BGB

Rechtsprechung:
– BGH, Urt. v. 13.7.2016 – VIII ZR 49/15, Rn. 25 (sofortige, unverzügliche oder umgehende Leistung zu verlangen genügt als Fristsetzung)
– BGH, Versäumnisurt. v. 12.8.2009 – VIII ZR 254/08, Rn. 10 f. (kein bestimmter Endtermin nötig; zu kurze Frist setzt eine angemessene in Gang)
– BGH, Urt. v. 3.7.2013 – VIII ZR 169/12, BGHZ 197, 357, Rn. 27, 29 (Mehrkosten eines Deckungskaufs sind Schaden statt der Leistung; § 281 Abs. 4 BGB)
– BGH, Urt. v. 1.7.2015 – VIII ZR 226/14, Rn. 33 (strenge Anforderungen an die ernsthafte und endgültige Erfüllungsverweigerung)

Hinweise: Das System der §§ 280 ff. BGB (neben, statt der Leistung, Verzögerungsschaden) erklärt das Video „Schadensersatz-Schema“; Verzug das Video „Schuldnerverzug, § 286 BGB“; den Rücktritt mit Fristsetzung das Video „Rücktritt, § 323 BGB“. Personen frei erfunden.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#SchadensersatzStattDerLeistung #SchuldrechtAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("tausendzweihundert Euro", "1.200 Euro"), ("tausendvierhundertfünfzig Euro", "1.450 Euro"),
             ("zweihundertfünfzig Euro", "250 Euro"), ("tausendzweihundert\nEuro", "1.200\nEuro"),
             ("tausendvierhundertfünfzig\nEuro", "1.450\nEuro"), ("zweihundertfünfzig\nEuro", "250\nEuro")]:
    srt = srt.replace(a, b)
for a, b in [("§§ 280 Absätze\neins und drei und zweihunderteinundachtzig.", "§§ 280 Abs. 1\nund 3 und 281."),
             ("§§ 280 Absätze eins und drei,", "§§ 280 Abs. 1 und 3,"), ("\nzweihunderteinundachtzig.", "\n281."),
             ("mit\nzweihundertsechsundachtzig", "mit\n§ 286"), ("mit zweihundertsechsundachtzig", "mit § 286"), ("\nzweihundertsechsundachtzig;", "\n§ 286;"), ("\n§§ 281.\n", "\n§ 281.\n"),
             ("Eins: S", "1. S"), ("Zwei: P", "2. P"), ("Drei: a", "3. a"), ("vier:\n", "4.\n"), ("vier: ", "4. "), ("Fünf: V", "5. V"), ("Sechs: S", "6. S")]:
    srt = srt.replace(a, b)
for w, z in (("Erstens", "1."), ("Zweitens", "2."), ("Drittens", "3."), ("Viertens", "4."), ("Fünftens", "5."),
             ("Sechstens", "6.")):
    srt = re.sub(rf"(?m)^{w}: ", f"{z} ", srt)
    srt = re.sub(rf"\. {w}:", f". {z}", srt)
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
rest = re.findall(r".{0,20}(?:tausend|hundert|Erstens|Zweitens|Drittens|Viertens|Fünftens|Sechstens).{0,10}", srt, re.I)
assert not rest, rest
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
