"""Nachbearbeitung der Upload-Texte für Folge 200 (nach meta_188.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen, Normen, Sprecher).
Bauplanungsrecht ist Bundesrecht – keine Ländernormen nötig (Landesrecht nur Verweis auf Folge 188).
Aufruf: python3 meta_200.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Kita und Tattoo-Studio in der neuen Siedlung"),
       (T("p30"), "§ 30 Abs. 1 BauGB: qualifizierter Bebauungsplan"),
       (T("bng"), "Die Baugebiete der BauNVO: WR, WA, MI, MU, GE, GI"),
       (T("aufbau"), "Aufbau §§ 2–9 BauNVO, Ausnahme § 31 Abs. 1 BauGB, Gebietsverträglichkeit"),
       (T("kita1"), "Kita im reinen Wohngebiet: § 3 BauNVO"),
       (T("laerm"), "Kinderlärm: § 22 Abs. 1a BImSchG"),
       (T("stu1"), "Tattoo-Studio im allgemeinen Wohngebiet: § 4 BauNVO"),
       (T("p4c"), "Ausnahme nach § 4 Abs. 3 Nr. 2 BauNVO – und der Bau-Turbo?"),
       (T("p15"), "Einzelfall: § 15 Abs. 1 BauNVO"),
       (T("erg"), "Ergebnis"),
       (T("sch"), "Prüfschema § 30 Abs. 1 BauGB"),
       (T("tipp"), "Klausurtipp: immer dieselbe Reihenfolge"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Baugebiete BauNVO (§ 30 BauGB, §§ 2 ff. BauNVO): Was ist im reinen und allgemeinen Wohngebiet zulässig? Regel, Ausnahme, § 15 – bundesweit erklärt.

Der Fall: In einer neuen Siedlung setzt der Bebauungsplan im Norden ein reines und im Süden ein allgemeines Wohngebiet fest. Im Norden soll eine Kita mit 2 Gruppen für die Kinder aus der Siedlung öffnen, im Süden ein kleines Tattoo-Studio, dessen Kundschaft aus der ganzen Stadt kommt. Was ist zulässig?

Inhalt:
– § 30 Abs. 1 BauGB im Wortlaut: der qualifizierte Bebauungsplan
– Die Baugebiete des § 1 Abs. 2 BauNVO (u. a. reines und allgemeines Wohngebiet, Mischgebiet, urbanes Gebiet § 6a, Gewerbe- und Industriegebiet) und § 1 Abs. 3 S. 2 BauNVO
– Aufbau der §§ 2 bis 9 BauNVO: Zweck, allgemein zulässig, ausnahmsweise; Ausnahme nach § 31 Abs. 1 BauGB im Wortlaut; das ungeschriebene Merkmal der Gebietsverträglichkeit
– Kita im reinen Wohngebiet: § 3 Abs. 2 Nr. 2 BauNVO im Wortlaut; Gegenfall große Kita (Abs. 3 Nr. 2); Kinderlärm, § 22 Abs. 1a BImSchG im Wortlaut
– Tattoo-Studio im allgemeinen Wohngebiet: § 4 Abs. 2 Nr. 2 BauNVO (Versorgung des Gebiets) und Abs. 3 Nr. 2 (sonstige nicht störende Gewerbebetriebe) im Wortlaut; warum der „Bau-Turbo“ (§ 246e BauGB) hier nicht hilft
– Einzelfall: § 15 Abs. 1 BauNVO im Wortlaut
– Ergebnis, Prüfschema, Klausurtipp, Merksatz

Normen: §§ 30, 31, 246e BauGB; §§ 1, 3, 4, 15, 25 ff. BauNVO; § 22 Abs. 1a BImSchG

Rechtsprechung:
– BVerwG, Beschl. v. 28.2.2008 – 4 B 60.07, Rn. 5, 6, 11 (ungeschriebenes Erfordernis der Gebietsverträglichkeit)
– BVerwG, Urt. v. 20.3.2019 – 4 C 5.18, Rn. 16 (Versorgung des Gebiets: funktionale Zuordnung, zur Gaststätte)
– BVerwG, Urt. v. 29.3.2022 – 4 C 6.20, Rn. 17 (Ausnahme nach § 31 Abs. 1 BauGB: Regel-Ausnahme-Verhältnis)

Hinweise: Das Bauplanungsrecht gilt bundesweit. Ob du für eine Nutzungsänderung eine Baugenehmigung brauchst und in welchem Verfahren, regelt die Landesbauordnung – dazu die Folge „Baugenehmigung Schema: Bauplanungs- und Bauordnungsrecht“. Wie Nachbarn eine gebietsfremde Nutzung abwehren (Gebietserhaltungsanspruch), zeigt die Folge „Baurechtliche Nachbarklage“. Ob Tätowieren ein Handwerk ist, lässt das Video bewusst offen; es kommt im Fall nicht darauf an. Für ältere Bebauungspläne kann nach den Überleitungsvorschriften (§§ 25 ff. BauNVO) eine ältere Fassung der BauNVO gelten.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 4. Oktober 2026 (BauNVO zuletzt geändert am 3. Juli 2023).

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Phosphor Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Baurecht #BauNVO #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
for muster, ersatz in [(r"Zwei Gruppen, dreißig Plätze", r"2 Gruppen, 30 Plätze"), (r"kennt zwölf", r"kennt 12"),
                       (r"Mit zwei Gruppen", r"Mit 2 Gruppen")]:
    srt, n = re.subn(muster, ersatz, srt)
    assert n, muster
srt = srt.replace("\nMöhring: ", "\nFrau Möhring: ").replace("\nTiemann: ", "\nHerr Tiemann: ")
assert not re.search(r"§\n|Abs\.\n|Art\.\n|Nr\.\n", srt), "Untertitel prüfen"
assert "Paragraf" not in srt and "dreißig" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
