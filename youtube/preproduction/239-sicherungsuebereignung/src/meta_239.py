"""Nachbearbeitung der Upload-Texte für Folge 239 (nach meta_236.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen, Paragrafen).
Aufruf: python3 meta_239.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Der Transporter und die Bank"),
       (T("frage"), "Wem gehört der Wagen? Sachverhalt"),
       (T("prob"), "Das Problem: Eigentum ohne Übergabe"),
       (T("norm"), "§ 929 S. 1 i. V. m. § 930 BGB im Wortlaut"),
       (T("einig"), "I. Einigung und Sicherungsvertrag"),
       (T("bmv"), "II. Besitzmittlungsverhältnis, § 868 BGB"),
       (T("ber"), "III. Berechtigung und IV. Bestimmtheit"),
       (T("treu"), "Volle Eigentümerin, aber gebunden"),
       (T("ins"), "Insolvenz: nur Absonderung, § 51 Nr. 1 InsO"),
       (T("zv"), "Pfändung: Drittwiderspruchsklage, § 771 ZPO"),
       (T("ev"), "Abgrenzung zum Eigentumsvorbehalt"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Sicherungsübereignung nach §§ 929, 930 BGB: Wie wird sie konstruiert und welche Rolle spielt der Sicherungsvertrag, wenn die Bank sich den Firmenwagen übereignen lässt?

Der Fall: Sieglinde führt einen Malerbetrieb und braucht einen neuen Transporter. Ihre Bank leiht ihr 30.000 € und lässt sich den Wagen zur Sicherheit übereignen. Sieglinde darf ihn weiter nutzen, solange sie die Raten zahlt. Wem gehört der Transporter – und was gilt, wenn Sieglinde insolvent wird oder ein anderer Gläubiger pfändet?

Inhalt:
– Das Problem: Die Bank will Eigentum, die Unternehmerin braucht den Wagen – das Besitzkonstitut ersetzt die Übergabe
– § 929 S. 1 i. V. m. § 930 BGB im Wortlaut, vier Prüfungspunkte
– I. Einigung (zur Sicherheit); Trennung vom schuldrechtlichen Sicherungsvertrag
– II. Besitzmittlungsverhältnis: § 868 BGB im Wortlaut, nach h. M. genügt der Sicherungsvertrag, konkreter Inhalt
– III. Berechtigung und IV. Bestimmtheit: einzelner Wagen, Warenlager mit wechselndem Bestand, Raumsicherungsvertrag
– Die Bank als volle Eigentümerin mit treuhänderischer Bindung; Rückübereignung nach Tilgung, auflösende Bedingung (§ 158 Abs. 2 BGB)
– Insolvenz des Sicherungsgebers: nur Absonderungsrecht, § 51 Nr. 1 InsO im Wortlaut, Verwertung nach §§ 166, 170 InsO
– Einzelvollstreckung: Drittwiderspruchsklage, § 771 ZPO (h. M.)
– Abgrenzung zum Eigentumsvorbehalt, Klausurtipp (§§ 985, 986 BGB), Klausurschema, Merksatz

Normen: §§ 158 Abs. 2, 449 Abs. 1, 868, 929 S. 1, 930, 985, 986 BGB; §§ 47, 50 Abs. 1, 51 Nr. 1, 166 Abs. 1, 170 Abs. 1 InsO; § 771 ZPO

Rechtsprechung:
– BGH, Urt. v. 16.12.2022 – V ZR 174/21, Rn. 10, 13 (Bestimmtheit; räumliche Abgrenzung bei Warenlagern mit wechselndem Bestand)
– BGH, Urt. v. 24.1.2019 – IX ZR 110/17, Rn. 3 (Raumsicherungsvertrag)
– BGH, Urt. v. 26.6.2026 – V ZR 92/25, Rn. 20 (Besitzmittlungsverhältnis braucht einen konkreten Inhalt)
– BGH, Urt. v. 12.4.2016 – XI ZR 305/14, Rn. 46 (schuldrechtlicher Sicherungsvertrag und abstraktes dingliches Geschäft)
– BGH, Urt. v. 7.3.2017 – VI ZR 125/16, Rn. 19 (Sicherungseigentum ist echtes Eigentum, Volleigentum)
– BGH, Urt. v. 20.9.2012 – IX ZR 208/11, Rn. 11 (Rückgewährpflicht aus dem Zweck des Sicherungsvertrags)
– BGH, Urt. v. 25.9.2014 – IX ZR 156/12, Rn. 9 (Absonderungsrecht, Verwertung durch den Insolvenzverwalter)
– vgl. BGH, Urt. v. 11.1.2007 – IX ZR 181/05, Rn. 10 (Drittwiderspruchsklage des Sicherungseigentümers)

Hinweise: Dass der Sicherungsvertrag selbst als Besitzmittlungsverhältnis genügt und der Sicherungseigentümer in der Einzelvollstreckung Drittwiderspruchsklage erheben kann, ist herrschende Meinung. Übersicherung und Freigabe, Globalzession und verlängerter Eigentumsvorbehalt sind nicht Thema dieses Videos. Mehr zu den Übergabesurrogaten im Video „Besitzkonstitut & Co.: Eigentum ohne Übergabe“, zur Drittwiderspruchsklage im Video „Drittwiderspruchsklage § 771 ZPO“ und zum Eigentumsvorbehalt im Video „Eigentumsvorbehalt: Das Sofa ist da, gehört aber dem Möbelhaus“. Personen und Bank frei erfunden.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Sicherungsübereignung #Sachenrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(§§?) (\d+)\n(S\.|Abs\.) (\d+)", r"\1 \2 \3 \4\n", srt)
srt = re.sub(r"(§ \d+)\n(Abs\. \d+\.)", r"\1 \2\n", srt)
for a, b in [("dreißigtausend Euro", "30.000 Euro"), ("dreißigtausend\nEuro", "30.000\nEuro"), ("Halle zwei", "Halle 2")]:
    srt = srt.replace(a, b)
for a, b in [("Römisch eins: ", "I. "), ("Römisch zwei: ", "II. "), ("Römisch drei:", "III."), ("Römisch vier: ", "IV. ")]:
    assert a in srt, a
    srt = srt.replace(a, b)
for a, b in [("zurück, § 158\n", "zurück,\n"), ("\nAbs. 2.\n", "\n§ 158 Abs. 2.\n"),
             ("Sicherungsvertrag. III.\n", "Sicherungsvertrag.\n"),
             ("\nBerechtigung des Sicherungsgebers.", "\nIII. Berechtigung des Sicherungsgebers.")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"(?m)^ +| +$", "", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|S\.\n", srt), "Untertitel prüfen"
rest = re.findall(r".{0,25}(?:tausend|hundert|Römisch|Paragraf).{0,15}", srt, re.I)
assert not rest, rest
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
