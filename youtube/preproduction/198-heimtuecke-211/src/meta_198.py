"""Nachbearbeitung der Upload-Texte für Folge 198 (nach meta_194.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit präzisierter Planbeschreibung, Fall, Inhalt,
Normen, Rechtsprechung, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen, Normen).
Aufruf: python3 meta_198.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: das Versöhnungsessen"),
       (T("p211"), "§ 211 StGB im Wortlaut"),
       (T("def"), "Definition und Prüfschema der Heimtücke"),
       (T("arg"), "a) Arglosigkeit"),
       (T("wehr"), "b) Wehrlosigkeit"),
       (T("aus"), "c) Ausnutzungsbewusstsein, d) feindliche Willensrichtung"),
       (T("sf"), "Sonderfall Schlafende"),
       (T("kind"), "Kleinkinder und Besinnungslose: schutzbereite Dritte"),
       (T("loes"), "Lösung: arglos trotz Streit?"),
       (T("lb"), "Lösung: Wehrlosigkeit und Ausnutzungsbewusstsein"),
       (T("restr"), "Einschränkung: Rechtsfolgenlösung und Vertrauensbruch"),
       (T("tipp"), "Klausurtipp"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Heimtücke nach § 211 StGB: Was bedeuten Arg- und Wehrlosigkeit und Ausnutzungsbewusstsein – warum sind Schlafende arglos, und warum kommt es bei Kleinkindern auf schutzbereite Dritte an?

Der Fall: Heribert und Siegmund führen zusammen eine Firma und streiten seit Wochen ums Geld. Heribert lädt Siegmund zu einem Versöhnungsessen ein – und greift ihn beim Hinsetzen mit Tötungsvorsatz an. War Siegmund trotz des Streits arglos?

Inhalt:
– § 211 Abs. 1 und Abs. 2 StGB im Wortlaut (Auszug „heimtückisch“)
– Definition der Heimtücke nach der ständigen Rechtsprechung des BGH
– Prüfschema: a) Arglosigkeit bei Beginn des ersten mit Tötungsvorsatz geführten Angriffs, b) Wehrlosigkeit infolge der Arglosigkeit, c) Ausnutzungsbewusstsein, d) feindliche Willensrichtung
– offen feindseliger Angriff und latente Angst aus früheren Streitigkeiten
– Sonderfälle: Schlafende (nehmen die Arglosigkeit mit in den Schlaf), Kleinkinder und Besinnungslose (schutzbereite Dritte)
– Lösung: arglos trotz vorheriger Auseinandersetzung; in die Lage gelockt; wehrlos beim Hinsetzen
– Einschränkung: Rechtsfolgenlösung des BGH; Teil der Lehre: verwerflicher Vertrauensbruch
– Klausurtipp und Merksatz

Normen: § 211 Abs. 1, Abs. 2 (2. Gruppe) StGB; § 212 StGB

Rechtsprechung:
– BGH, Urt. v. 4.12.2024 – 2 StR 352/24, Rn. 25–27, 32 (Definition; Arglosigkeit; latente Angst; Schlafende nach BGHSt 23, 119; Ausnutzungsbewusstsein)
– BGH, Urt. v. 24.9.2025 – 5 StR 423/25, Rn. 13 (Wehrlosigkeit als Folge der Arglosigkeit)
– BGH, Urt. v. 21.1.2021 – 4 StR 337/20, Rn. 12 f. (Wehrlosigkeit; in eine Falle gelocktes Opfer)
– BGH, Urt. v. 6.9.2012 – 3 StR 171/12, Rn. 5 f. (Arglosigkeit trotz vorangegangener Auseinandersetzung)
– BGH, Urt. v. 15.11.2017 – 5 StR 338/17, Rn. 12 (latente Angst)
– BGH, Urt. v. 21.11.2012 – 2 StR 309/12, Rn. 5 (Kleinkinder nach BGHSt 4, 11; schutzbereiter Dritter)
– BGH, Beschl. v. 5.8.2014 – 1 StR 340/14, Rn. 7 f. (schutzbereiter Dritter, räumliche Nähe)
– BGH, Urt. v. 18.10.2007 – 3 StR 226/07, Rn. 16 (Besinnungslose, Pflegepersonal)
– BGH, Urt. v. 19.6.2019 – 5 StR 128/19, BGHSt 64, 111, Rn. 28 (feindliche Willensrichtung; Rechtsfolgenlösung nach BGHSt 30, 105)
– BGH, Beschl. v. 25.8.2010 – 1 StR 393/10, Rn. 5 (kein verwerflicher Vertrauensbruch nötig)

Hinweise: BGHSt 23, 119, BGHSt 4, 11 und BGHSt 30, 105 sind nach ihrer Wiedergabe in den genannten neueren BGH-Entscheidungen zitiert. Die Lehrmeinung zum verwerflichen Vertrauensbruch ist als Meinung eines Teils der Lehre dargestellt (vgl. etwa AG Strafrecht BT, Universität Freiburg, Lösungsskizze Fall 1, 2023). Prüfschemata sind Klausurkonventionen. Mehr zu allen Mordmerkmalen in der Folge „Mordmerkmale § 211 StGB“, zur Rechtsfolgenlösung im „Haustyrannen-Fall“.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung im Einzelfall. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Strafrecht #Jura #Heimtücke
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?|Art\.)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.|S\.|Nr\.)\n(\d+[a-z]?[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"§\n(\d+)", r"§ \1\n", srt)
for vorn, hinten, e1, e2 in [("um neunzehn", "Uhr", "um 19", "Uhr"), ("zwölfter", "März", "12.", "März"),
                             ("März, neunzehn", "Uhr", "März, 19", "Uhr")]:
    srt, n = re.subn(re.escape(vorn) + r"(\s)" + re.escape(hinten), lambda m: e1 + m.group(1) + e2, srt)
    assert n, vorn
assert not re.search(r"§\n|Abs\.\n|Art\.\n(?=\S)", srt), "Untertitel prüfen"
assert "hundert" not in srt and "Paragraf" not in srt and "neunzehn" not in srt and "zwölfter" not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Heimtücke Schlafende", "schutzbereiter Dritter", "Heimtückemord", "Rechtsfolgenlösung"]
                         if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen;", len(m["tags"]), "Tags")
