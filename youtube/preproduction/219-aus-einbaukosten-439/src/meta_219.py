"""Nachbearbeitung der Upload-Texte für Folge 219 (nach meta_217.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn., Hinweisen und
Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Normangaben nicht über den Zeilenumbruch getrennt).
Kein Landesrecht. Aufruf: python3 meta_219.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Farbfehler im ganzen Bad"),
       (T("frage"), "Die Frage und der Sachverhalt"),
       (T("mang"), "I. Sachmangel und Nacherfüllung"),
       (T("alt"), "Rechtslage vor 2018"),
       (T("eugh"), "EuGH Weber/Putz (2011)"),
       (T("bgh"), "BGH: 600 € und nur beim Verbrauchsgüterkauf"),
       (T("heute"), "§ 439 Abs. 3 BGB im Wortlaut"),
       (T("ein"), "II. Einbau, bevor der Mangel offenbar wurde"),
       (T("auf"), "III. Erforderliche Aufwendungen, Vorschuss"),
       (T("verw"), "IV. Verweigerung, § 439 Abs. 4 BGB"),
       (T("v4"), "Seit 2022: Weber/Putz-Sonderregel gestrichen"),
       (T("erg"), "Ergebnis und Regress, § 445a BGB"),
       (T("tipp"), "Klausurtipp und Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Aus- und Einbaukosten nach § 439 III BGB: Muss der Verkäufer zahlen, wenn fehlerhafte Fliesen schon verlegt sind? Der Fliesen-Fall Weber/Putz (EuGH 2011) und was seit 2018 und 2022 im BGB gilt.

Der Fall: Herr Oltmann kauft im Fliesenhandel von Frau Reinecke Fliesen für 1.400 Euro für sein Bad. Ein Fliesenleger verlegt sie; erst auf der fertigen Fläche zeigen sich deutliche Farbunterschiede – ein Herstellungsfehler, der sich nicht beheben lässt. Ausbauen und neu verlegen kostet 5.200 Euro. Frau Reinecke: „Neue Fliesen bekommen Sie. Aber ich habe Ihnen Fliesen verkauft, nicht das Verlegen.“

Inhalt:
– I. Sachmangel (§ 434 Abs. 3 BGB) und Nacherfüllung (§ 439 Abs. 1 BGB): nur die Lieferung neuer Fliesen bleibt
– Rechtslage vor 2018: nur neue Fliesen, Aus- und Einbau allenfalls als Schadensersatz
– EuGH Weber/Putz (2011): Ausbau und Einbau oder Kostentragung; keine Verweigerung der einzig möglichen Abhilfe, aber Begrenzung auf einen angemessenen Betrag
– BGH: im deutschen Fliesen-Fall 600 € Ausbaukosten; nicht zwischen Unternehmern
– § 439 Abs. 3 BGB im Wortlaut: seit 2018 für alle Kaufverträge, auch für Handwerker
– II. Einbau, bevor der Mangel offenbar wurde (seit 2022; der frühere Satz 2 mit § 442 BGB ist aufgehoben)
– III. Erforderliche Aufwendungen: kein Verschulden nötig, Geld statt Selbstvornahme, Vorschuss nach § 475 Abs. 5 BGB
– IV. Verweigerung nach § 439 Abs. 4 BGB (im Wortlaut); § 475 Abs. 4 BGB a. F. seit 2022 gestrichen
– Ergebnis, Regress beim Lieferanten (§ 445a BGB), Klausurtipp, Schema, Merksatz

Normen: §§ 434, 437 Nr. 1, 439 Abs. 1, 3, 4, 445a, 475 Abs. 5 BGB; Art. 229 §§ 39, 58 EGBGB.

Rechtsprechung:
– EuGH, Urt. v. 16.6.2011 – C-65/09, C-87/09 (Weber/Putz), Rn. 47, 62, 71, 73, 74, 76–78
– BGH, Urt. v. 21.12.2011 – VIII ZR 70/08, Rn. 25, 35, 54
– BGH, Urt. v. 17.10.2012 – VIII ZR 226/11, Rn. 16, 17
Gesetzesbegründungen: BT-Drs. 18/8486, S. 38 f.; BT-Drs. 19/27424, S. 25 f., 29.

Hinweise: Herr Oltmann, Frau Reinecke und der Fliesenleger sind erfunden. Ältere Lehrbücher zitieren § 439 Abs. 3 Satz 2 BGB (Verweis auf § 442) und § 475 Abs. 4 BGB a. F. – beides gilt für Kaufverträge seit dem 1. Januar 2022 nicht mehr (Art. 229 § 58 EGBGB). Bei Kaufverträgen seit dem 31. Juli 2026 muss der Unternehmer den Verbraucher vor der Nacherfüllung außerdem über sein Wahlrecht informieren (§ 475 Abs. 4 BGB). Mehr dazu: Folge 59 (Sachmangel, § 434 BGB), Folge 63 (Käuferrechte, § 437 BGB), Folge 125 (Verbrauchsgüterkauf).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#Kaufrecht #Nacherfüllung #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("tausendvierhundert Euro", "1.400 Euro"), ("fünftausendzweihundert Euro", "5.200 Euro"),
          ("sechshundert Euro", "600 Euro"), ("Oltmann: Ich brauche", "Herr Oltmann: Ich brauche"),
          ("Reinecke: Neue Fliesen", "Frau Reinecke: Neue Fliesen"), ("Römisch eins:", "I."), ("Römisch zwei:", "II."),
          ("Römisch drei:", "III."), ("Römisch vier:", "IV."), ("verwies S. 2", "verwies Satz 2")]
for alt, neu in ERSATZ:
    muster = r"\s+".join(re.escape(w) for w in alt.split())
    n = len(re.findall(muster, srt))
    assert n, alt
    srt = re.sub(muster, lambda m: neu if "\n" not in m.group(0) else neu.replace(" ", "\n", 1) if neu.count(" ") else neu, srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"tausend|hundert|Römisch|S\. 2|\n(Oltmann|Reinecke):", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + ["Aufwendungsersatz Nacherfüllung", "§ 439 Abs. 3 BGB n.F."]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
