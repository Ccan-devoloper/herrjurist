"""Nachbearbeitung der Upload-Texte für Folge 216 (nach meta_204.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Zahlen, Sprecher).
Aufruf: python3 meta_216.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: dreimal anders geschildert – und „konstant“?"),
       (T("p261"), "§ 261 StPO: freie Überzeugung des Tatgerichts"),
       (T("nurrf"), "Revision: nur Rechtsfehler der Beweiswürdigung"),
       (T("aga2"), "Aussage gegen Aussage: Gesamtschau und Kriterien"),
       (T("frueh"), "Frühere Angaben und Abweichungen"),
       (T("fall2"), "Der Fall: lückenhaft und widersprüchlich"),
       (T("beruh"), "Beruhen, Aufhebung, Zurückverweisung"),
       (T("idpr"), "In dubio pro reo: Entscheidungsregel"),
       (T("emrk"), "Unschuldsvermutung, Art. 6 Abs. 2 EMRK"),
       (T("tipp"), "Klausurtipp: die Revisionsbegründung"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Beweiswürdigung Revision: Wann ist die tatrichterliche Würdigung nach § 261 StPO angreifbar, was gilt bei Aussage gegen Aussage, und wann greift in dubio pro reo?

Der Fall: Das Amtsgericht verurteilt Herrn Kerber wegen Körperverletzung. Zeugen gab es keine – Aussage steht gegen Aussage. Laut Urteil hat die Kollegin den Vorfall dreimal verschieden geschildert: Stoß gegen das Regal, Faustschlag, am Arm gepackt. Trotzdem nennt das Urteil ihre Aussage „konstant“. Kann die Revision das angreifen – und hilft „im Zweifel für den Angeklagten“?

Inhalt:
– § 261 StPO im Wortlaut: Die Beweiswürdigung ist Sache des Tatgerichts
– Revision: nur Rechtsfehler – lückenhaft, widersprüchlich, unklar, Verstoß gegen Denkgesetze oder Erfahrungssätze, überspannte Anforderungen an die Gewissheit; die allgemeine Sachrüge genügt
– Aussage gegen Aussage: Verurteilung auf eine Belastungszeugin möglich, aber besonders sorgfältige Würdigung – Gesamtschau, Entstehung der Aussage, Motive, Konstanz, Detailreichtum, Plausibilität; frühere Angaben müssen im Urteil stehen
– Der Fall: dreimal verschieden, aber „konstant“ – lückenhaft und widersprüchlich; Beruhen, Aufhebung (§ 353 StPO) und Zurückverweisung (§ 354 Abs. 2 StPO)
– In dubio pro reo: keine Beweis-, sondern Entscheidungsregel; Unschuldsvermutung, Art. 6 Abs. 2 EMRK im Wortlaut
– Klausurtipp zur Revisionsbegründung, Prüfschema, Merksatz

Normen: §§ 261, 267, 337, 353, 354 StPO; § 223 StGB; Art. 6 Abs. 2 EMRK

Rechtsprechung:
– BGH, Beschl. v. 17.12.2025 – 6 StR 260/25, Rn. 5 (Aussage gegen Aussage: Gesamtschau, Entstehung, Konstanz, Detailliertheit, Plausibilität)
– BGH, Beschl. v. 29.4.2025 – 6 StR 105/25, Rn. 6, 9, 12 (frühere Angaben darstellen; „hinreichend konstant“ trotz Abweichung)
– BGH, Beschl. v. 26.6.2024 – 1 StR 176/24, Rn. 7 (Prüfungsmaßstab Beweiswürdigung; lückenhaft)
– BGH, Urt. v. 19.3.2025 – 6 StR 543/24, Rn. 16 (Rechtsfehler der Beweiswürdigung, überspannte Anforderungen)
– BGH, Urt. v. 25.4.2018 – 2 StR 194/17, Rn. 10, 12 (eine Belastungszeugin; wechselnde Angaben erkannt und erklärt)
– BGH, Beschl. v. 18.6.2024 – 2 StR 205/24, Rn. 21 (Beruhen, Aufhebung mit den Feststellungen)
– BGH, Urt. v. 24.9.2025 – 2 StR 128/25, Rn. 31 (in dubio pro reo als Entscheidungsregel)

Hinweise: Wie die allgemeine Sachrüge funktioniert und warum nur das Urteil zählt, zeigt die Folge „Sachrüge StPO: Wenn die Feststellungen das Urteil nicht tragen“. Der Wortlaut von Art. 6 Abs. 2 EMRK folgt der deutschen Übersetzung des EGMR (verbindlich sind nur die englische und die französische Fassung).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Revision #StPO #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|Art\.|S\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei|vier):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV."}[m.group(1)] + m.group(2), srt)
for muster, ersatz in [(r"sechzig(\s+)Tagessätzen", r"60\1Tagessätzen"),
                       (r"Zwei(\s+)Wochen", r"2\1Wochen")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
srt = (srt.replace("\nKerber: ", "\nHerr Kerber: ").replace("\nBremer: ", "\nFrau Bremer: ")
          .replace("\nWegmann: ", "\nRechtsanwalt Wegmann: "))
assert not re.search(r"§\n|Abs\.\n|Art\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "sechzig" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
