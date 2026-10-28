"""Nachbearbeitung der Upload-Texte für Folge 204 (nach meta_168.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen, Sprecher).
Aufruf: python3 meta_204.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Betrugsurteil ohne Wort zum Schaden"),
       (T("p337"), "§ 337 StPO: Gesetzesverletzung und Beruhen"),
       (T("sach"), "Die allgemeine Sachrüge, § 344 Abs. 2 StPO"),
       (T("grund"), "Grundlage: nur die Urteilsurkunde"),
       (T("stufen"), "a) Subsumtionsfehler"),
       (T("sb"), "b) Darstellungsmangel, § 267 Abs. 1 StPO"),
       (T("sc"), "c) Beweiswürdigung"),
       (T("sd"), "d) Strafzumessung"),
       (T("schaden"), "Der Fall: Vermögensschaden nicht festgestellt"),
       (T("beruhen"), "Beruhen, Aufhebung, Zurückverweisung"),
       (T("tipp"), "Klausurtipp: die Revisionsbegründung"),
       (T("sch"), "Prüfschema Sachrüge"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Sachrüge in der StPO-Revision: Was prüft das Revisionsgericht auf die allgemeine Sachrüge (§ 337 StPO), warum zählen nur die Urteilsgründe, und was ist ein Darstellungsmangel?

Der Fall: Das Landgericht verurteilt Herrn Wichmann wegen Betrugs. Er hat einen Oldtimer für 85.000 € als „unfallfrei“ verkauft, obwohl der Wagen einen schweren Unfallschaden hatte. Doch was der Wagen trotzdem wert war, steht nicht im Urteil. Trägt das den Schuldspruch?

Inhalt:
– § 337 StPO im Wortlaut: Gesetzesverletzung und Beruhen
– Die allgemeine Sachrüge: § 344 Abs. 2 S. 1 StPO – ein Satz genügt („Ich rüge die Verletzung materiellen Rechts.“)
– Grundlage der Prüfung: allein die Urteilsurkunde – keine Akte, keine Rekonstruktion der Hauptverhandlung, urteilsfremdes Vorbringen bleibt außer Betracht
– Vier Prüfungsstufen: a) Subsumtionsfehler, b) Darstellungsmangel (§ 267 Abs. 1 S. 1 StPO im Wortlaut), c) Beweiswürdigung, d) Strafzumessung
– Der Fall: Vermögensschaden nach dem Prinzip der Gesamtsaldierung; beim Kauf nur, wenn die Sache den Preis objektiv nicht wert ist – fehlt der Wert im Urteil, hält der Schuldspruch nicht
– Beruhen, Aufhebung (§ 353 StPO) und Zurückverweisung (§ 354 Abs. 2 StPO)
– Klausurtipp zur Revisionsbegründung, Prüfschema, Merksatz

Normen: §§ 267, 337, 344, 352, 353, 354 StPO; § 263 StGB

Rechtsprechung:
– BGH, Beschl. v. 13.8.2025 – 2 StR 283/25, Rn. 10, 11, 13 (Kauf eines Oldtimer-Nachbaus: Wert nicht festgestellt, Schuldspruch wegen Betrugs ohne Boden)
– BGH, Beschl. v. 19.7.2023 – 2 StR 77/22, Rn. 7, 8, 15 (fehlende Feststellungen zum Vermögensschaden; Gesamtsaldierung)
– BGH, Beschl. v. 21.4.2021 – 3 StR 300/20, Rn. 2 (allgemeine Sachrüge: umfassende materiellrechtliche Nachprüfung)
– BGH, Urt. v. 12.5.2016 – 4 StR 569/15, Rn. 23 (Grundlage der Sachrüge: nur die Urteilsurkunde)
– BGH, Urt. v. 17.7.2025 – 4 StR 298/24, Rn. 10 (Rekonstruktionsverbot)
– BGH, Urt. v. 23.3.2023 – 3 StR 277/22, Rn. 28 (urteilsfremdes Vorbringen)
– BGH, Urt. v. 17.12.2019 – 1 StR 171/19, Rn. 47 (Tatsachen und Werturteile)
– BGH, Beschl. v. 19.2.2025 – 1 StR 482/24, Rn. 6 (§ 267 Abs. 1 S. 1 StPO: geschlossene Darstellung)
– BGH, Beschl. v. 13.4.2026 – 1 StR 52/26, Rn. 6 (Prüfungsmaßstab Beweiswürdigung)
– BGH, Urt. v. 16.7.2026 – 5 StR 125/26, Rn. 8 (Prüfungsmaßstab Strafzumessung)

Hinweise: Fehler im Ablauf der Hauptverhandlung brauchen die Verfahrensrüge – dazu die Folgen „Revision: Sachrüge vs. Verfahrensrüge“ und „Verfahrensrüge § 344 II 2 StPO“. Die Gliederung in vier Prüfungsstufen ist Klausurkonvention.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Revision #StPO #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei|vier|fünf):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV.", "fünf": "V."}[m.group(1)] + m.group(2), srt)
for muster, ersatz in [(r"zwei(\s+)Jahren(\s+)und(\s+)sechs(\s+)Monaten", r"2\1Jahren\2und\g<3>6\4Monaten"),
                       (r"fünfundachtzigtausend(\s)Euro", r"85.000\1€")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
srt = srt.replace("\nHellmers: ", "\nRechtsanwältin Hellmers: ").replace("\nWichmann: ", "\nHerr Wichmann: ").replace("\nDanner: ", "\nFrau Danner: ")
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "tausend" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
