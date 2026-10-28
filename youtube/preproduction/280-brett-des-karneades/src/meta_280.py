"""Nachbearbeitung der Upload-Texte für Folge 280 (nach meta_263.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen, Sprecher).
Aufruf: python3 meta_280.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: eine Planke, zwei Schiffbrüchige"),
       (T("tb"), "Tatbestand und Rechtswidrigkeit"),
       (T("p35"), "§ 35 Abs. 1 S. 1 StGB im Wortlaut"),
       (T("satz2"), "Hinnahmepflicht: Gefahr selbst verursacht?"),
       (T("rv"), "Besonderes Rechtsverhältnis"),
       (T("abw1"), "Abwandlung 1: der Kapitän"),
       (T("abw2"), "Abwandlung 2: Irrtum, § 35 Abs. 2 StGB"),
       (T("bgh"), "Vermeidbarkeit (BGHSt 48, 255)"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Schema und Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Entschuldigender Notstand § 35 StGB: Wann ist die Rettung des eigenen Lebens auf Kosten eines anderen entschuldigt – und wer muss Gefahren hinnehmen?

Der Fall: Ein Ausflugsboot sinkt im Sturm. Im Wasser treibt nur eine Planke, die einen Menschen trägt. Zwei Schiffbrüchige halten sich daran fest – einer stößt den anderen weg und überlebt. Das „Brett des Karneades“ ist ein antikes Gedankenexperiment und ein Klassiker der Klausur.

Inhalt:
– Tatbestand: Totschlag (§ 212 StGB); Rechtswidrigkeit: § 34 StGB scheitert bei Leben gegen Leben
– § 35 Abs. 1 S. 1 StGB im Wortlaut: gegenwärtige, nicht anders abwendbare Gefahr für Leben, eigene Person, Rettungswille
– § 35 Abs. 1 S. 2 StGB: Hinnahmepflicht bei selbst verursachter Gefahr oder besonderem Rechtsverhältnis (Feuerwehr, Polizei, Soldaten)
– Abwandlung 1: Der Kapitän stößt einen Fahrgast von der Planke – keine Entschuldigung, keine Strafmilderung nach S. 2
– Abwandlung 2: übersehenes Rettungsboot – Irrtum nach § 35 Abs. 2 StGB und seine Vermeidbarkeit (BGHSt 48, 255)
– Ergebnis, Klausurtipp, Schema und Merksatz

Normen: § 35 StGB; §§ 212, 34, 32, 49 StGB

Rechtsprechung und Materialien:
– BGH, Urt. v. 25.3.2003 – 1 StR 483/02 (BGHSt 48, 255, Haustyrann), Rn. 29, 30, 35
– BT-Drs. V/4095, S. 16 (Begründung zu § 35 StGB: besonderes Rechtsverhältnis)

Hinweise: Die Einordnung des Kapitäns folgt der Lehre zur Schutzpflicht im besonderen Rechtsverhältnis; sie ist im Video gekennzeichnet. Warum § 34 StGB bei Leben gegen Leben scheitert, zeigt das Video „Leben gegen Leben: Übergesetzlicher entschuldigender Notstand“; den Haustyrannen-Fall das Video „Haustyrannen-Fall: Den Peiniger im Schlaf töten? Notstand § 35“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 8. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Strafrecht #Notstand #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
for muster, ersatz in [(r"Mitte vierzig", "Mitte 40"),
                       (r"Eins, Tatbestand", "1. Tatbestand"), (r"Zwei, Rechtswidrigkeit", "2. Rechtswidrigkeit"),
                       (r"Drei, Schuld", "3. Schuld"), (r"Vier, Ergebnis", "4. Ergebnis"),
                       (r"(Aber|aus|vergiss|nach) S\. 2", r"\1 Satz 2"), (r"(hilft|Irrtum) Abs\. 2", r"\1 Absatz 2")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
srt = srt.replace("\nTamm: ", "\nHerr Tamm: ").replace("\nPetzold: ", "\nKommissarin Petzold: ")
assert not re.search(r"§\n", srt), "Untertitel prüfen"
for w in ("Paragraf", "hundert", "vierzig", "Satz zwei", "Absatz zwei", "Absatz eins"):
    assert w not in srt, f"Zahlwort im Untertitel: {w}"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
