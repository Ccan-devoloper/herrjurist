"""Nachbearbeitung der Upload-Texte für Folge 211 (nach meta_208.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit §§/Rn., Hinweisen und
Lizenzzeile; Untertitel-Korrekturen (Zahlen als Ziffern, Sprechernamen, Normangaben nicht über den Zeilenumbruch getrennt).
Keine Namen realer Beteiligter (nur „Gäfgen“ als Fallbezeichnung); Tag „Daschner“ durch „Rettungsfolter“ ersetzt
(Vorschlag an den Koordinator in RECHTSSTAND.md).
Aufruf: python3 meta_211.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Entführung und Festnahme"),
       (T("vize"), "Die Anweisung und die Drohung"),
       (T("nennt"), "Das Versteck, die Fragen, der Sachverhalt"),
       (T("norm"), "§ 136a StPO im Wortlaut"),
       (T("sub"), "Drohung verboten, Aussage unverwertbar"),
       (T("fort"), "Fortwirkung und qualifizierte Belehrung"),
       (T("hv"), "Fernwirkung: die Spuren vom Versteck"),
       (T("rich"), "Das neue Geständnis und das Urteil"),
       (T("egmr"), "EGMR: Art. 3 EMRK"),
       (T("a6"), "EGMR: Art. 6 EMRK, faires Verfahren"),
       (T("pol"), "Die Polizisten: Notstand und Menschenwürde"),
       (T("strafe"), "Die Sanktion"),
       (T("tipp"), "Klausurtipp: Prüfungsaufbau"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Fall Gäfgen: Gibt es nach § 136a StPO eine Fernwirkung – und kann die Folterdrohung zur Rettung nach § 34 StGB gerechtfertigt sein? EGMR und LG Frankfurt.

Der Fall: Frankfurt am Main, Herbst 2002. Ein Kind ist entführt, die Polizei nimmt Herrn Wallmann bei der Lösegeldabholung fest. Am nächsten Morgen lässt ihm der stellvertretende Polizeipräsident Schmerzen androhen; nach rund zehn Minuten nennt er das Versteck. Dort sichert die Polizei Spuren. Darf das Gericht die Aussage verwerten, und die Spuren? Unser Fall folgt dem echten Fall, den die Große Kammer des Europäischen Gerichtshofs für Menschenrechte 2010 entschieden hat.

Inhalt:
– § 136a Abs. 1 StPO (im Wortlaut): Drohung mit einer unzulässigen Maßnahme verboten
– § 136a Abs. 3 S. 2 StPO (im Wortlaut): Aussage unverwertbar, auch mit Zustimmung
– Fortwirkung: auch spätere Aussagen unverwertbar; Heilung nur durch qualifizierte Belehrung
– Fernwirkung („fruit of the poisonous tree“): vom BGH grundsätzlich abgelehnt; Abwägung des LG Frankfurt im Fall
– Hauptverhandlung: neue Belehrung, neues Geständnis, Verurteilung allein darauf gestützt
– EGMR: Art. 3 EMRK (im Wortlaut) verletzt – unmenschliche Behandlung, keine Folter; Art. 6 EMRK nicht verletzt, weil die Kette unterbrochen war
– Die Polizisten: Rechtfertigung durch Notstand (§ 34 StGB) scheitert an der Menschenwürde (Art. 1 Abs. 1 GG); Verwarnung mit Strafvorbehalt
– Klausurtipp mit Prüfungsaufbau, Merksatz

Normen: § 136a Abs. 1, 3 StPO; Art. 3, 6 EMRK; § 34 StGB; Art. 1 Abs. 1 GG; § 59 StGB.

Rechtsprechung:
– EGMR (Große Kammer), Gäfgen/Deutschland, Urt. v. 1.6.2010 – Nr. 22978/05, §§ 25–34, 47–51, 87, 107 f., 124, 131 f., 166 f., 178–188 (HUDOC)
– LG Frankfurt a. M., Urt. v. 20.12.2004 – 5/27 KLs 7570 Js 203814/03 (4/04), NJW 2005, 692 (Verfahren gegen die Polizeibeamten)
– BGH, Beschl. v. 7.3.2006 – 1 StR 316/05, Rn. 22 f.; BGHSt 34, 362, 364 (keine Fernwirkung)

Hinweise: Herr Wallmann, Herr Rombach, Kommissar Leitner, die Verteidigerin und die Richterin sind erfundene Figuren; sie folgen dem echten Fall. Reale Beteiligte werden nicht dargestellt und nicht benannt. Art. 3 EMRK zitiert nach der deutschen Übersetzung des EGMR. Mehr dazu: Folge 171 (Belehrungsverstoß), Folge 013 (Luftsicherheitsgesetz), Folge 189 (Notstand, § 34 StGB).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 6. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#FallGäfgen #Strafprozessrecht #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Art\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("Rombach: Drohen", "Herr Rombach: Drohen"), ("Leitner: Sagen", "Kommissar Leitner: Sagen"),
             ("Richterin: Sie dürfen", "Vorsitzende Richterin: Sie dürfen"),
             ("eine Million Euro", "1 Million Euro"), ("rund zehn Minuten", "rund 10 Minuten"),
             ("mit elf zu sechs Stimmen", "mit 11 zu 6 Stimmen")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|Art\.\n|zweitausend|zehn Minuten|elf zu", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = [("Rettungsfolter" if t == "Daschner" else t) for t in m["tags"]] + ["qualifizierte Belehrung"]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
