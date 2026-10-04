"""Nachbearbeitung der Upload-Texte für Folge 195 (nach meta_192.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen und Beträge in Ziffern, Normen, Sprecher).
Aufruf: python3 meta_195.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: 10.000 € verlangt, 7.300 € bekommen"),
       (T("klage"), "Das Urteil in der Hauptsache"),
       (T("p91"), "Grundsatz: § 91 Abs. 1 S. 1 ZPO"),
       (T("p92"), "Teilunterliegen: § 92 Abs. 1 S. 1 ZPO"),
       (T("rech"), "Die Kostenquote rechnen: 27 % zu 73 %"),
       (T("bruch"), "Prozent oder Bruch? Der Kostentenor"),
       (T("aufh"), "Kostenaufhebung, § 92 Abs. 1 S. 2 ZPO"),
       (T("p922"), "Ausnahme: § 92 Abs. 2 ZPO"),
       (T("sonder"), "Sonderregeln: §§ 93, 91a, 269 Abs. 3, 344 ZPO"),
       (T("tipp"), "Klausurtipp: Kostentenor nie vergessen"),
       (T("sch"), "Schema Kostenentscheidung"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Kostenentscheidung ZPO: Wie bildest du die Kostenquote nach §§ 91, 92 ZPO, wann greift § 92 II, und welche Sonderregeln wie §§ 93, 269 III, 344 musst du kennen?

Der Fall: Ein Malermeister verlangt für Fassade und Garage 10.000 Euro Werklohn. Das Amtsgericht spricht ihm 7.300 Euro zu – den Auftrag für die Garage kann er nicht beweisen. Wer trägt jetzt die Kosten des Rechtsstreits?

Inhalt:
– Grundsatz: § 91 Abs. 1 S. 1 ZPO im Wortlaut – das Unterliegensprinzip
– Teilunterliegen: § 92 Abs. 1 S. 1 ZPO im Wortlaut – Kosten verhältnismäßig teilen oder gegeneinander aufheben
– Die Quote rechnen: Unterliegen am Streitwert, 2.700 € : 10.000 € = 27 %; Prozent oder Bruch
– Der Kostentenor: „Von den Kosten des Rechtsstreits tragen der Kläger 27 % und die Beklagte 73 %.“
– Kostenaufhebung: § 92 Abs. 1 S. 2 ZPO (Gerichtskosten je zur Hälfte)
– Ausnahme § 92 Abs. 2 ZPO: verhältnismäßig geringfügige Zuvielforderung (Faustregel der Literatur: bis etwa 10 %), Nr. 2
– Sonderregeln: § 93 (sofortiges Anerkenntnis), § 91a (Erledigung), § 269 Abs. 3 S. 2 (Klagerücknahme), § 344 (Versäumniskosten)
– Klausurtipp (§ 308 Abs. 2 ZPO), Schema, Merksatz

Normen: §§ 91 Abs. 1 S. 1, Abs. 2, 91a Abs. 1, 92, 93, 269 Abs. 3 S. 2, 308 Abs. 2, 344 ZPO; Verweis §§ 708 ff. ZPO; § 631 Abs. 1 BGB; § 23 Nr. 1 GVG

Rechtsprechung und Literatur:
– AG Königs Wusterhausen, Urt. v. 13.4.2023 – 4 C 4468/22 (Quote am Streitwert; § 92 Abs. 2 nur kumulativ; 18,5 % nicht geringfügig)
– OLG Hamm, Beschl. v. 19.10.2021 – 7 W 11/21 (Kostentenor in Prozent)
– OLG Hamm, Urt. v. 20.12.2007 – 24 U 53/06 (Kostentenor als Bruch: ¼ und ¾)
– Wilke, Einführung in das Kostenrecht der ZPO, ZJS 2014, 363 (366 f.) (Kostenaufhebung; Faustregel „bis zu 10 %“)

Hinweise: Die 10-%-Grenze ist eine Faustregel der Literatur, keine gesetzliche Grenze; § 92 Abs. 2 ZPO stellt die Entscheidung ins Ermessen des Gerichts. Die vorläufige Vollstreckbarkeit (§§ 708 ff. ZPO) ist ein eigenes Thema. Zu den Säumniskosten nach § 344 ZPO siehe das Video „Versäumnisurteil Voraussetzungen“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#KostenentscheidungZPO #2Examen #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(§§?) (\d+[a-z]?)\n(Abs\.) (\d+)", r"\1 \2 \3\n\4", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)


def ersetze(muster, ersatz):
    """Zahlwort → Ziffern, auch über einen Zeilenumbruch hinweg (Umbruch bleibt nach dem Ersatz erhalten)."""
    global srt
    rx = re.compile(muster.replace(" ", r"(\s)"))
    srt, n = rx.subn(lambda m: ersatz + ("\n" if "\n" in m.group(0) else ""), srt)
    return n


for muster, ersatz in [("Zehntausend Euro", "10.000 Euro"), ("zehntausend Euro", "10.000 Euro"),
                       ("zehntausend sind", "10.000 sind"), ("siebentausenddreihundert", "7.300"),
                       ("Zweitausendsiebenhundert", "2.700"), ("zweitausendsiebenhundert", "2.700"),
                       ("Siebenundzwanzig Prozent", "27 %"), ("siebenundzwanzig Prozent", "27 %"),
                       ("dreiundsiebzig Prozent", "73 %"), ("zehn Prozent", "10 %"),
                       ("Siebenundzwanzig Hundertstel", "27/100")]:
    assert ersetze(muster, ersatz), muster
srt = re.sub(r"\n +", "\n", srt)
srt = srt.replace("\nfolgende, ein eigenes Thema", "\nff., ein eigenes Thema")   # „§§ 708 folgende“ über zwei Untertitel
srt = srt.replace("\nLindau: ", "\nFrau Lindau: ").replace("\nDressler: ", "\nHerr Dressler: ")
assert not re.search(r"§\n|Abs\.\n|Art\.\n(?=\S)", srt), "Untertitel prüfen"
assert not re.search(r"tausend|hundert|siebzig|zwanzig|Paragraf", srt), "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
