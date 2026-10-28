"""Nachbearbeitung der Upload-Texte für Folge 126 (Kopie von meta_125.py, nach tools/youtube_metadaten.py, nichts dort
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Paragrafen-Umbruch in den Untertiteln.
Aufruf: python3 meta_126.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Fall: Saaltür abgeschlossen, kein Beschluss"),
       (T("p337"), "1. Einordnung: § 337 und § 338 StPO"),
       (T("kat"), "2. Nr. 1: Besetzung, §§ 222a, 222b StPO"),
       (T("n5"), "2. Katalog: Nr. 5, 6, 7 und 8"),
       (T("w8"), "3. Warum Nr. 8 nur eingeschränkt absolut ist"),
       (T("fall2"), "4. Der Fall: § 338 Nr. 6 StPO"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"), (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Absolute Revisionsgründe nach § 338 StPO: Besetzung, Abwesenheit, Öffentlichkeit, Verteidigung – und warum § 338 Nr. 8 StPO nur eingeschränkt absolut ist.

Der Fall: Vor der Strafkammer wird gegen Herrn Lemke verhandelt. Vor der Aussage der betroffenen Zeugin lässt der Vorsitzende die Saaltür abschließen – ohne Beschluss über den Ausschluss der Öffentlichkeit. Draußen steht die Jurastudentin Lene vor verschlossener Tür. Herr Lemke wird verurteilt, sein Verteidiger legt Revision ein. Hat sie Erfolg, und muss er zeigen, dass das Urteil auf dem Fehler beruht?

Inhalt:
– Einordnung: § 337 StPO (Beruhen) und § 338 StPO (Beruhen wird unwiderleglich vermutet, Wortlaut); trotzdem vollständige Verfahrensrüge nach § 344 Abs. 2 S. 2 StPO (Folge 72)
– Nr. 1 Besetzung: Mitteilung nach § 222a StPO, Einwand binnen einer Woche und Vorabentscheidung des Rechtsmittelgerichts nach § 222b StPO (seit 13.12.2019); Revision nur noch nach § 338 Nr. 1 Buchst. a, b StPO
– Nr. 5 Abwesenheit (Staatsanwalt § 226, Angeklagter § 230, notwendiger Verteidiger § 140 StPO; nur wesentlicher Teil), Nr. 6 Öffentlichkeit (§§ 169, 174 GVG), Nr. 7 Urteilsgründe (§ 275 StPO), Nr. 8 Verteidigung
– Nr. 8: „in einem für die Entscheidung wesentlichen Punkt“ – konkreter Kausalzusammenhang nötig (Wortlaut und BGH)
– Fall: § 338 Nr. 6 StPO – Ausschluss nur durch Gerichtsbeschluss, Zurechnung, ein Zuschauer genügt, enge Ausnahmen
– Ergebnis (§§ 353, 354 Abs. 2 StPO), Klausurtipp, Klausurschema, Merksatz

Rechtsprechung und Materialien:
– BGH, Urt. v. 28.2.2024 – 5 StR 413/23, Rn. 7, 10 f.: Ausschluss der Öffentlichkeit stets nur durch Beschluss des erkennenden Gerichts (§ 174 Abs. 1 S. 2 GVG); eine Anordnung des Vorsitzenden ersetzt ihn nicht; Ausnahmen nur in engen Fallgruppen
– BGH, Beschl. v. 21.6.2023 – 5 StR 73/23, Rn. 6: § 338 Nr. 6 StPO nur bei einem dem Gericht zurechenbaren Verstoß (Anordnung oder bekannte bzw. erkennbare Beschränkung)
– BGH, Beschl. v. 2.12.2025 – 5 StR 388/25, Rn. 9: Schon ein (potentieller) Zuschauer genügt
– BGH, Beschl. v. 27.1.2026 – 2 StR 644/25, Rn. 8, 12: Nr. 6 nicht bei zu viel Öffentlichkeit; Voraussetzungen des § 171b GVG im Einzelfall der Revision entzogen (§ 171b Abs. 5 GVG, § 336 S. 2 StPO)
– BGH, Beschl. v. 23.6.2026 – 5 StR 52/26, Rn. 8: § 338 Nr. 8 StPO nur, wenn die Möglichkeit eines kausalen Zusammenhangs zwischen Verstoß und Urteil konkret besteht
– BGH, Beschl. v. 30.8.2022 – 5 StR 169/22, Rn. 9: Rüge nach Nr. 8 muss den Gerichtsbeschluss mitteilen
– BGH, Beschl. v. 20.8.2025 – 3 StR 580/24, Rn. 9; Beschl. v. 30.8.2022 – 4 StR 117/22, Rn. 7 (Nr. 5: wesentlicher Teil; notwendiger Verteidiger)
– BGH, Beschl. v. 5.10.2021 – 3 StR 485/20, Rn. 11; BT-Drs. 19/14747, S. 31, 36 (Vorabentscheidungsverfahren seit 13.12.2019)

Hinweise: Wer zu § 338 Nr. 1 StPO noch die Buchstaben a bis d liest, hat eine Darstellung vor Dezember 2019 vor sich. „Nur eingeschränkt absolut“ ist eine Lehrbuchbezeichnung für das Erfordernis des konkreten Zusammenhangs. Das Klausurschema ist Klausurkonvention. Die Verfahrensrüge erklärt Folge 72, den Revisionsaufbau und das Beruhen Folge 66.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 3. Oktober 2026 (StPO und GVG zuletzt geändert durch Gesetz vom 20.3.2026).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Revision #StPO #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt).replace("\nStrobel: ", "\nRechtsanwalt Strobel: ")
assert not re.search(r"§\n", srt)
# Gegenlesen: Normangaben im Untertitel mit Gesetz (gesprochen ohne „StPO“), Saalnummer als Ziffer
srt = re.sub(r"(§ \d+[a-z]?(?:\s+Abs\. \d+)?(?: S\. \d+)?)(?=[.,:])", r"\1 StPO", srt)
srt = srt.replace("§ 338 macht", "§ 338 StPO macht").replace("Bei § 338 trägst", "Bei § 338 StPO trägst")
srt = srt.replace("§ 171b\nim Einzelfall", "§ 171b GVG\nim Einzelfall").replace("Abs. 2 S. 2 StPO", "Abs. 2 Satz 2 StPO")
srt = srt.replace("§ 354\nAbs. 2 StPO", "§ 354 Abs. 2\nStPO").replace("§ 174\nGVG.", "§ 174 GVG.").replace("§ 171b\nGVG in", "§ 171b GVG\nin")
srt = srt.replace("Saal zwei", "Saal 2")
srt = re.sub(r" \n", "\n", srt)
# Normangabe nicht über zwei Untertitel verteilen: „§ 174“ | „GVG. …“ → „§ 174 GVG.“ | „…“
bl = srt.strip().split("\n\n")
for i in range(len(bl) - 1):
    kopf, text = bl[i].split("\n", 2)[:2], bl[i].split("\n", 2)[2]
    k2, t2 = bl[i + 1].split("\n", 2)[:2], bl[i + 1].split("\n", 2)[2]
    m_ = re.match(r"((?:GVG|Abs\. \d+(?: StPO)?)[.,:]?)\s*", t2)
    if re.search(r"§ \d+[a-z]?$", text) and m_:
        text += " " + m_.group(1); t2 = t2[m_.end():]
        if not t2.strip():
            t2 = "…"
        bl[i] = "\n".join(kopf + [text]); bl[i + 1] = "\n".join(k2 + [t2])
neu = []
for b in bl:
    nr_, zeit_, text_ = b.split("\n", 2)
    if text_.strip() == "…":                          # leer gewordenen Untertitel streichen, Ende an den vorigen
        k0 = neu[-1].split("\n", 2)
        neu[-1] = "\n".join([k0[0], k0[1].split(" --> ")[0] + " --> " + zeit_.split(" --> ")[1], k0[2]])
        continue
    neu.append(b)
srt = "\n\n".join(f"{i + 1}\n" + b.split("\n", 1)[1] for i, b in enumerate(neu)) + "\n"
srt = srt.replace("§ 354 Abs. 2.", "§ 354 Abs. 2 StPO.")
assert "Paragraf" not in srt
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = ["§ 338 StPO", "absolute Revisionsgründe", "Besetzungsrüge", "Öffentlichkeit § 169 GVG", "§ 338 Nr. 8 StPO",
             "Revisionsklausur", "Referendariat", "2. Staatsexamen"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
