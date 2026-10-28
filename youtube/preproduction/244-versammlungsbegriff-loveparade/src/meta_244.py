"""Nachbearbeitung der Upload-Texte für Folge 244 (nach meta_234.py) nach tools/youtube_metadaten.py (dort nichts geändert):
sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen, Rechtsprechung mit Rn.,
Landesrecht-Hinweis, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen, Normangaben).
Aufruf: python3 meta_244.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Sound-Umzug mit Motto"),
       (T("frage"), "Die Frage und der Love-Parade-Beschluss"),
       (T("art8"), "1. Der Wortlaut von Art. 8 I GG"),
       (T("begriff"), "2. Weiter, erweiterter und enger Versammlungsbegriff"),
       (T("grund"), "Warum eng? NRW, Massenparty, Musik als Mittel"),
       (T("gemischt"), "3. Gemischte Veranstaltungen: Gesamtgepräge, im Zweifel Versammlung"),
       (T("schritte"), "Gesamtschau in drei Schritten (BVerwG)"),
       (T("lp"), "Love Parade und Gegenveranstaltung 2001"),
       (T("subs"), "4. Der Fall: keine Versammlung"),
       (T("folge"), "Folgen: Sondernutzung und Kosten"),
       (T("gegen"), "5. Gegenfall: Musik als Mittel"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Schema"),
       (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Versammlungsbegriff nach Art. 8 I GG: Ist eine Techno-Parade mit politischem Motto eine Versammlung? Enger und weiter Begriff, Love-Parade-Beschluss erklärt.

Der Fall: Herr Brendel plant einen Sound-Umzug mit 20 Musikwagen und Techno – Motto „Mehr Raum für Kultur“, aber ohne Reden, Flugblätter oder Transparente. Er will ihn als Versammlung durchführen. Die Stadt sagt: keine Versammlung, Sie brauchen eine Erlaubnis und tragen die Reinigung. Wer hat recht?

Inhalt:
– Wortlaut Art. 8 Abs. 1 GG
– Weiter, erweiterter und enger Versammlungsbegriff; Definition des BVerfG (Teilhabe an der öffentlichen Meinungsbildung)
– Volksfest und Massenparty vs. Musik und Tanz als Mittel der Meinungskundgabe
– Gemischte Veranstaltungen: Gesamtgepräge, „Bleiben Zweifel …“ – im Zweifel wie eine Versammlung
– Gesamtschau in drei Schritten (BVerwG 2007), Love Parade und Gegenveranstaltung 2001
– Folgen: Sondernutzung der Straße, Erlaubnis, Auflagen und Kosten
– Gegenfall, Klausurtipp, Schema, Merksatz

Normen: Art. 8 Abs. 1 GG; Beispiel NRW: § 2 Abs. 3 und § 11 VersG NRW; §§ 18, 21 StrWG NRW; § 29 Abs. 2 StVO.

Landesrecht: Versammlungs- und Straßenrecht sind Ländersache. Beispiel im Video ist Nordrhein-Westfalen (§ 2 Abs. 3 VersG NRW definiert die Versammlung: mindestens drei Personen, „überwiegend“ auf die öffentliche Meinungsbildung gerichtet). In anderen Ländern gelten eigene Versammlungs- und Straßengesetze bzw. das Versammlungsgesetz des Bundes; die Nummern können abweichen. Der verfassungsrechtliche Versammlungsbegriff des Art. 8 GG gilt überall.

Rechtsprechung:
– BVerfG (1. Kammer des Ersten Senats), Beschl. v. 12.7.2001 – 1 BvQ 28/01, 1 BvQ 30/01 (Love Parade), Rn. 16–22, 25 f.
– BVerfG, Beschl. v. 24.10.2001 – 1 BvR 1190/90 u. a., BVerfGE 104, 92 (Sitzblockaden III), Rn. 39 (Definition)
– BVerwG, Urt. v. 16.5.2007 – 6 C 23.06, Rn. 15–18, 20–25 (gemischte Veranstaltung, drei Schritte)

Hinweise: Herr Brendel, Herr Zander und Frau Lechner sind erfundene Figuren; der Sound-Umzug ist fiktiv. Mehr dazu: Folge 028 (Brokdorf-Beschluss), Folgen 233 und 234 (Fortsetzungsfeststellungsklage im Versammlungsrecht).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 7. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com).

#Versammlungsfreiheit #Grundrechte #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
for alt, neu in [("achtunddreißigtausend Euro", "38.000 Euro"), ("zwanzig Musikwagen", "20 Musikwagen"),
                 ("Zwanzig Musikwagen", "20 Musikwagen"), ("Juli zweitausendeins", "Juli 2001"),
                 ("Artikel acht Absatz eins Grundgesetz", "Art. 8 Abs. 1 Grundgesetz"),
                 ("Artikel acht Grundgesetz", "Art. 8 Grundgesetz"), ("Artikel acht", "Art. 8")]:
    srt = srt.replace(alt, neu)
assert not re.search(r"§\n|Abs\.\n|Paragraf", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
m["tags"] = m["tags"] + [t for t in ["Versammlungsbegriff Art. 8 GG", "gemischte Veranstaltung Gesamtgepräge",
                                     "Love Parade Beschluss"] if t not in m["tags"]]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen; Tags", m["tags"])
