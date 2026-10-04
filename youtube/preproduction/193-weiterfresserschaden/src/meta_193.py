"""Nachbearbeitung der Upload-Texte für Folge 193 (nach meta_187.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Gliederung, Beträge, Jahreszahlen).
Aufruf: python3 meta_193.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: 40-Euro-Teil zerstört den Motor, Sachverhalt"),
       (T("warum"), "Warum Deliktsrecht? § 437 und die Fristen"),
       (T("norm"), "§ 823 Abs. 1 BGB im Wortlaut"),
       (T("int"), "Äquivalenz- und Integritätsinteresse"),
       (T("krit"), "Kriterien der Stoffgleichheit"),
       (T("anw"), "Anwendung auf den Fall"),
       (T("gegen"), "Gegenbeispiel: ganzer Motor fehlerhaft"),
       (T("lehre"), "Kritik und Produkthaftungsgesetz"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Weiterfresserschaden: Wann ist der spätere Schaden an der gekauften Sache eine Eigentumsverletzung nach § 823 I BGB? Stoffgleichheit, Schwimmerschalter- und Gaszug-Fall.

Der Fall: Hinnerk kauft einen fabrikneuen Kleinwagen für 26.000 €. Eine Spannrolle am Zahnriemen, ein Kleinteil für 40 €, ist beim Hersteller fehlerhaft gefertigt. Nach sechs Wochen bricht sie, und der Motor ist zerstört; ein neuer kostet 7.800 €. Kann Hinnerk vom Hersteller Ersatz für den Motor verlangen?

Inhalt:
– Warum Deliktsrecht? Mängelrechte aus § 437 BGB gegen den Verkäufer, kein Vertrag mit dem Hersteller
– Fristen: § 438 Abs. 1 Nr. 3, Abs. 2 BGB gegenüber §§ 195, 199 Abs. 1 BGB
– § 823 Abs. 1 BGB im Wortlaut: Kann eine von Anfang an mangelhafte Sache verletzt werden?
– Äquivalenzinteresse und Integritätsinteresse, Mangelunwert, Stoffgleichheit
– Kriterien des BGH: Fehler erfasst die ganze Sache oder Mangel auf ein Teil beschränkt und behebbar
– Anwendung auf den Fall, Gegenbeispiel, Kritik (Meinung), Kontrast § 1 Abs. 1 Satz 2 ProdHaftG
– Ergebnis, Klausurtipp, Prüfschema, Merksatz

Normen: § 823 Abs. 1 BGB; §§ 437, 438, 195, 199 BGB; § 1 Abs. 1 Satz 2 ProdHaftG

Rechtsprechung und Materialien:
– BGH, Urt. v. 24.11.1976 – VIII ZR 137/75, BGHZ 67, 359 (Schwimmerschalter)
– BGH, Urt. v. 18.1.1983 – VI ZR 310/79, BGHZ 86, 256 (Gaszug)
– BGH, Urt. v. 23.2.2021 – VI ZR 21/20, Rn. 10, 11, 13, 16, 21 (Stoffgleichheit, Integritätsinteresse, Verjährungsbeginn)
– BGH, Vorlagebeschl. v. 13.3.2020 – V ZR 33/19, Rn. 13, 51
– BT-Drucks. 14/6040, S. 229 (Schuldrechtsreform, „weiterfressender“ Mangel)

Hinweise: Die übrigen Merkmale des § 823 Abs. 1 BGB zeigt das Video zum Deliktsrecht, den Mangelbegriff das Video zum Sachmangel. Das Produkthaftungsgesetz ist im Stand vom 4. Oktober 2026 wiedergegeben.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Weiterfresserschaden #Deliktsrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)",
             lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
for a, b in [("sechsundzwanzigtausend Euro", "26.000 Euro"), ("siebentausendachthundert Euro", "7.800 Euro"),
             ("vierzig Euro", "40 Euro"), ("neunzehnhundertsechsundsiebzig", "1976"),
             ("neunzehnhundertdreiundachtzig", "1983")]:
    srt = srt.replace(a, b)
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "tausend" not in srt and "Römisch" not in srt and "vierzig" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
