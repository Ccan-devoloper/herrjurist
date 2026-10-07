"""Nachbearbeitung der Upload-Texte für Folge 227 (nach meta_214.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Lehre, Hinweisen und
Lizenzzeile; Untertitel-Korrekturen (Sprechername „Frau Höfer“, Normangaben nicht über den Zeilenumbruch getrennt).
Aufruf: python3 meta_227.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Provokation auf dem Weinfest"),
       (T("messer"), "Der Stich und die Frage"),
       (T("sv"), "Sachverhalt mit Abwandlung"),
       (T("tb"), "Tatbestand: §§ 223, 224 StGB"),
       (T("p32"), "§ 32 Abs. 2 StGB im Wortlaut"),
       (T("lage"), "Notwehrlage trotz Provokation"),
       (T("geb"), "Gebotenheit: Notwehrprovokation"),
       (T("absicht"), "Absichtsprovokation: Notwehr versagt"),
       (T("aiic"), "Streit: actio illicita in causa"),
       (T("abw"), "Abwandlung: leichtfertige Provokation"),
       (T("einge"), "Ausweichen – Schutzwehr – Trutzwehr"),
       (T("stand2"), "Abwandlung im Fall und Gegenfall"),
       (T("erg"), "Ergebnis"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Klausurschema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Notwehrprovokation nach § 32 StGB: Absichtsprovokation vs. vorwerfbare Provokation – wann entfällt Notwehr, wann gilt Ausweichen, Schutzwehr, Trutzwehr?

Der Fall: Auf dem Weinfest kündigt Ferdinand an, Herrn Pelzer so lange zu reizen, bis er zuschlägt – „dann ist es Notwehr“. Nach einer beleidigenden Bemerkung holt Herr Pelzer zum Faustschlag aus; Ferdinand könnte hinter den Weinstand ausweichen, sticht aber mit einem Taschenmesser zu. Abwandlung: Ferdinand wollte keinen Streit, die Bemerkung rutschte ihm im Ärger heraus.

Inhalt:
– Tatbestand kurz: §§ 223, 224 Abs. 1 Nr. 2 StGB
– § 32 StGB im Wortlaut (Abs. 2 und Abs. 1)
– Notwehrlage: Der Angriff des Provozierten bleibt rechtswidrig, die Beleidigung war vorbei
– Gebotenheit: sozialethische Einschränkung, Fallgruppe Notwehrprovokation
– Absichtsprovokation: Notwehr nach st. Rspr. grundsätzlich ganz versagt (Rechtsmissbrauch); Gegenansicht actio illicita in causa
– Leichtfertige Provokation: Voraussetzungen; abgestuft ausweichen, Schutzwehr, Trutzwehr erst zuletzt; vorsätzliche Provokation strenger
– Ergebnis, Klausurtipp, Klausurschema, Merksatz

Normen: §§ 32, 223, 224 Abs. 1 Nr. 2 StGB.

Rechtsprechung:
– BGH, Urt. v. 17.1.2019 – 4 StR 456/18, Rn. 6 f. (Absichts-, Vorsatz- und leichtfertige Provokation; Voraussetzungen)
– BGH, Urt. v. 22.11.2000 – 3 StR 331/00, Rn. 10, 15 (Rechtsmissbrauch; Schutzwehr vor Trutzwehr; actio illicita in causa nicht anerkannt)
– BGH, Urt. v. 27.9.2012 – 4 StR 197/12, Rn. 15 (Beleidigung als Provokation; ohne Ausweg auch lebensgefährliche Abwehr)
– BGH, Beschl. v. 9.9.2024 – 2 StR 211/24, Rn. 15
– BGH, Urt. v. 25.4.2013 – 4 StR 551/12, Rn. 16 f. (gegenwärtiger, rechtswidriger Angriff)
– BGH, Beschl. v. 16.6.2021 – 1 StR 126/21, Rn. 18 (sozialethische Einschränkungen)

Lehre: Breuer, Die Actio illicita in causa – Darstellung und Meinungsstand, BRJ 2008, 5 ff.

Hinweise: Ferdinand, Herr Pelzer, Josefine und Frau Höfer sind erfundene Figuren. Mehr dazu: Folge 033 (Notwehr-Schema), Folge 214 (Notwehr bei Bagatellen).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Notwehrprovokation #StrafrechtAT #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("Höfer: Ferdinand, schnell,", "Frau Höfer: Ferdinand, schnell,")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Paragraf", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["actio illicita in causa", "Notwehr Provokation Beleidigung"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
