"""Nachbearbeitung der Upload-Texte für Folge 215 (nach meta_209.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen).
Aufruf: python3 meta_215.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Das Fahrrad wird angefahren"),
       (T("frage"), "Schwager oder Geld? Sachverhalt"),
       (T("grund"), "Haftungsgrund vorausgesetzt, § 823 Abs. 1 BGB"),
       (T("dh"), "1. Schaden: Differenzhypothese"),
       (T("w1"), "2. Naturalrestitution, § 249 Abs. 1 BGB"),
       (T("w2"), "3. Geld statt Herstellung, § 249 Abs. 2 BGB"),
       (T("fik"), "Fiktive Abrechnung und Umsatzsteuer"),
       (T("w4"), "4. Geldentschädigung, § 251 BGB"),
       (T("var"), "Abwandlung: Reparatur teurer als ein Ersatzrad"),
       (T("erg"), "Ergebnis und Klausurtipp"),
       (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Differenzhypothese und Naturalrestitution (§§ 249–251 BGB): Wie wird ein Schaden ermittelt und wann schuldet der Schädiger Herstellung, wann Geld? Am angefahrenen Fahrrad.

Der Fall: Hedi stellt ihr Fahrrad vor einer Bäckerei ab, Ludolf parkt rückwärts aus und fährt es an. Die Werkstatt verlangt 400 € plus 76 € Umsatzsteuer, ein gleichwertiges Rad kostet 900 €. Ludolf will das Rad von seinem Schwager reparieren lassen – Hedi will das Geld.

Inhalt:
– Haftungsgrund vorausgesetzt (etwa § 823 Abs. 1 BGB), Rechtsfolge im Mittelpunkt
– 1. Schaden nach der Differenzhypothese: tatsächliche gegen hypothetische Vermögenslage
– 2. Naturalrestitution: § 249 Abs. 1 BGB im Wortlaut
– 3. Geld statt Herstellung: § 249 Abs. 2 Satz 1 BGB im Wortlaut, Ersetzungsbefugnis, Wirtschaftlichkeitsgebot
– Fiktive Abrechnung und Umsatzsteuer: § 249 Abs. 2 Satz 2 BGB im Wortlaut; § 250 BGB
– 4. Geldentschädigung: § 251 Abs. 1 und Abs. 2 Satz 1 BGB im Wortlaut, merkantiler Minderwert, Vorrang der Herstellung
– Abwandlung: Reparatur 1.200 € gegen Ersatzrad 900 € – Wiederbeschaffungsaufwand; die 130-%-Grenze beim Auto
– Klausurtipp (fiktive Abrechnung: Werkvertrag gegen Deliktsrecht), Klausurschema, Merksatz

Normen: §§ 249 Abs. 1, 2, 250, 251 Abs. 1, 2, 823 Abs. 1 BGB

Rechtsprechung:
– BGH, Urt. v. 16.7.2024 – VI ZR 239/23, Rn. 6–8 (Differenzhypothese; merkantiler Minderwert nach § 251 Abs. 1 BGB)
– BGH, Urt. v. 19.2.2013 – VI ZR 69/12, Rn. 9 (Ersetzungsbefugnis, Dispositionsfreiheit)
– BGH, Urt. v. 28.1.2025 – VI ZR 300/24, Rn. 11 f. (Wirtschaftlichkeitsgebot; fiktive Abrechnung)
– BGH, Urt. v. 23.5.2017 – VI ZR 9/17, Rn. 6 f. (Vorrang der Naturalrestitution; Grenze des § 251 BGB; Ersatzbeschaffung als Herstellung)
– BGH, Urt. v. 24.1.2017 – VI ZR 146/16, Rn. 9 (nicht angefallene Umsatzsteuer, § 249 Abs. 2 Satz 2 BGB)
– BGH, Urt. v. 25.3.2025 – VI ZR 174/24, Rn. 21 (Wiederbeschaffungsaufwand: Wiederbeschaffungswert abzüglich Restwert)
– BGH, Urt. v. 2.6.2015 – VI ZR 387/14, Rn. 6 f. (130-%-Grenze beim Kfz)
– BGH, Urt. v. 22.2.2018 – VII ZR 46/17, Leitsatz 1 (Werkvertrag: keine fiktiven Mängelbeseitigungskosten)

Hinweise: Welcher Schadensersatzanspruch wann greift, erklärt das Video „Schadensersatz-Schema, §§ 280 ff. BGB“. Personen frei erfunden.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Differenzhypothese #Schadensrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("tausendzweihundert", "1.200"), ("vierhundertsechsundsiebzig", "476"), ("achthundertfünfzig", "850"),
             ("neunhundert", "900"), ("vierhundert", "400"), ("sechsundsiebzig", "76"), ("fünfzig Euro", "50 Euro"),
             ("hundertdreißig", "130"),
             ("§§ 249 bis 251", "§§ 249 bis 251")]:
    srt = srt.replace(a, b)
for a, b in [("Eins: S", "1. S"), ("Zwei: g", "2. g"), ("Drei: b", "3. b"), ("Vier: G", "4. G")]:
    srt = srt.replace(a, b)
for w, z in (("Erstens", "1."), ("Zweitens", "2."), ("Drittens", "3."), ("Viertens", "4.")):
    srt = re.sub(rf"(?m)^{w}: ", f"{z} ", srt)
    srt = re.sub(rf"\. {w}:", f". {z}", srt)
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
rest = re.findall(r".{0,20}(?:tausend|hundert|Erstens|Zweitens|Drittens|Viertens|sechsundsiebzig|fünfzig).{0,10}", srt, re.I)
assert not rest, rest
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
