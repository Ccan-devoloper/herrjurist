"""Nachbearbeitung der Upload-Texte für Folge 181 (nach meta_176.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung).
Aufruf: python3 meta_181.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Bier mit Reis und Mais"),
       (T("verweis"), "Einordnung: Rechtfertigung bei Art. 34 AEUV"),
       (T("c79"), "Cassis de Dijon (EuGH 1979): der Fall"),
       (T("unter"), "Unterschiedslos anwendbare Maßnahme"),
       (T("formel"), "Die Cassis-Formel: zwingende Erfordernisse"),
       (T("gesund"), "Deutschlands Argumente und das Etikett"),
       (T("anerk"), "Gegenseitige Anerkennung"),
       (T("r87"), "Reinheitsgebot (EuGH 1987): der Fall"),
       (T("name"), "Das Bezeichnungsverbot"),
       (T("zus"), "Das Zusatzstoffverbot und Art. 36 AEUV"),
       (T("tenor"), "Ergebnis und heute: § 1 BierV"),
       (T("loes"), "Lösung des Falls"),
       (T("tipp"), "Klausurtipp und Schema der Rechtfertigung"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Cassis de Dijon (EuGH, Rs. 120/78): Zwingende Erfordernisse und gegenseitige Anerkennung bei Art. 34 AEUV – und warum das Reinheitsgebot scheiterte.

Der Fall: Herr Brodersen betreibt einen Getränkehandel und will ein Bier aus Belgien verkaufen, gebraut aus Gerstenmalz, Reis und Mais. Frau Timmermann von der Lebensmittelüberwachung meint: Nach dem Reinheitsgebot ist das kein Bier. Darf ein Staat den Namen „Bier“ für Getränke nach seinen eigenen Brauregeln reservieren?

Inhalt:
– Einordnung: Das Prüfschema zu Art. 34 AEUV steht im Video zu Dassonville; hier geht es um die Rechtfertigung
– Cassis de Dijon (1979): Mindestweingeistgehalt für Fruchtsaftliköre, unterschiedslos anwendbare Maßnahme, die Cassis-Formel der zwingenden Erfordernisse (Rn. 8), Etikett als milderes Mittel (Rn. 13), Rn. 14 und der Grundsatz der gegenseitigen Anerkennung
– Reinheitsgebot (1987): Bezeichnungsverbot des § 10 Biersteuergesetz a. F. unverhältnismäßig, Etikettierung statt Verbot (Rn. 29–37); absolutes Zusatzstoffverbot nicht durch Art. 36 AEUV gedeckt (Rn. 40–53)
– Heute: § 1 Abs. 2 Bierverordnung und Inländerdiskriminierung
– Lösung, Klausurtipp (zwingende Erfordernisse nur bei unterschiedslos anwendbaren Maßnahmen), Schema der Rechtfertigung, Merksatz

Normen: Art. 34, 36 AEUV; § 1 Abs. 1, 2 BierV

Rechtsprechung:
– EuGH, Urt. v. 20.2.1979 – Rs. 120/78 (Rewe-Zentral, „Cassis de Dijon“), Slg. 1979, 649, Rn. 8, 13, 14
– EuGH, Urt. v. 12.3.1987 – Rs. 178/84 (Kommission/Deutschland, Reinheitsgebot), Slg. 1987, 1227, Rn. 24, 28–37, 40–54
– EuGH, Urt. v. 17.6.1981 – Rs. 113/80 (Kommission/Irland), Slg. 1981, 1625, Rn. 7–11
– Verordnung (EU) 2019/515 über die gegenseitige Anerkennung von Waren, Erwägungsgrund 4

Hinweise: Der Einstieg ist ein Übungsfall; die echten Fälle sind nach den Urteilen erzählt. Die Aussage, zwingende Erfordernisse griffen nur bei unterschiedslos anwendbaren Maßnahmen, gibt die klassische Rechtsprechung wieder (Rs. 113/80, Rs. 178/84). Nicht behandelt: heutiges Kennzeichnungs- und Zusatzstoffrecht, Ausnahmen für besondere Biere, die Zulässigkeit der Inländerdiskriminierung. Das Prüfschema der Warenverkehrsfreiheit erklärt die Folge zu Dassonville.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Europarecht #CassisdeDijon #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"Römisch (eins|zwei):", lambda m: {"eins": "I.", "zwei": "II."}[m.group(1)], srt)
srt = srt.replace("fünfundzwanzig Prozent", "25 Prozent").replace("fünfzehn bis zwanzig", "15 bis 20")
assert not re.search(r"§\n|Abs\.\n|Art\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "Römisch" not in srt and "zig" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
for t in ["Rewe-Zentral", "Biersteuergesetz", "Bierverordnung", "Inländerdiskriminierung", "Examenswissen Europarecht"]:
    if t not in m.get("tags", []):
        m.setdefault("tags", []).append(t)
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
