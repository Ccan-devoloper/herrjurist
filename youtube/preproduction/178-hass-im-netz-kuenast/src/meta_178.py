"""Nachbearbeitung der Upload-Texte für Folge 178 (nach meta_154.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Rn.,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Zahlen und Daten als Ziffern, StGB, Sprechername, römische Ziffern).
Keine Beschimpfung in Beschreibung, Tags oder Untertiteln; „Künast“ nur als Fallbezeichnung; keine Partei- oder
Plattformnamen. Aufruf: python3 meta_178.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Muss eine Politikerin das aushalten?"),
       (T("echt"), "Der echte Fall Künast: Beitrag, Kommentare, Auskunft"),
       (T("lg"), "Die Instanzen, Bundesverfassungsgericht, Sachverhalt"),
       (T("a5"), "1. Art. 5 GG, § 185 und § 193 StGB"),
       (T("kern"), "2. Abwägung als Regel, Schmähkritik als Ausnahme"),
       (T("fehler"), "3. Der Fehler im Fall Künast"),
       (T("krit"), "4. Kriterien der Abwägung"),
       (T("p188"), "5. § 188 und § 192a StGB"),
       (T("loes"), "6. Lösung: die Stadträtin"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Hass im Netz: Wie wägen Gerichte bei §§ 185, 193 StGB Meinungsfreiheit (Art. 5 I GG) und Persönlichkeitsrecht ab – und was sind Schmähkritik und Formalbeleidigung?

Der Fall: Unter einem Beitrag mit dem Bild einer Politikerin und einem ihr falsch zugeschriebenen Zitat schreiben 2019 zahlreiche Nutzer Kommentare, viele davon derbe sexistische Beschimpfungen. Die Politikerin beantragt beim Landgericht Berlin, der Plattform die Auskunft über die Daten der Verfasser zu gestatten. Landgericht und Kammergericht erlauben das nur für 12 von 22 Kommentaren. Das Bundesverfassungsgericht entscheidet am 19. Dezember 2021: Die Beschlüsse verletzen ihr Persönlichkeitsrecht (Fall Künast).

Inhalt:
– Einstieg in der Sprechstunde: Muss eine Stadträtin solche Kommentare aushalten?
– Der echte Fall: Auskunftsverfahren (§ 14 Abs. 3 TMG a. F., heute § 21 Abs. 2, 3 TDDDG) durch die Instanzen
– Art. 5 Abs. 1 Satz 1 und Abs. 2 GG (im Wortlaut), § 185 StGB als allgemeines Gesetz, Persönlichkeitsrecht
– § 193 StGB (im Wortlaut): Wahrnehmung berechtigter Interessen
– Abwägung als Regel; Schmähung, Formalbeleidigung und Menschenwürdeverletzung als enge Ausnahmen
– Der Fehler des Kammergerichts: Beleidigung mit Schmähkritik gleichgesetzt, Abwägung ausgefallen
– Kriterien: Beitrag zur Meinungsbildung, Machtkritik, Position, Schutz im öffentlichen Interesse, Form, Anlass, Wirkung
– § 188 StGB (im Wortlaut) bis zur kommunalen Ebene, § 192a StGB
– Lösung des Einstiegsfalls, Klausurtipp, Prüfschema, Merksatz

Normen: Art. 5 Abs. 1 Satz 1, Abs. 2 GG; Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG; §§ 185, 188, 192a, 193, 194 StGB; § 21 Abs. 2, 3 TDDDG

Rechtsprechung:
– BVerfG, Beschl. v. 19.12.2021 – 1 BvR 1073/20 (Fall Künast): Rn. 1–16 (Sachverhalt, Instanzen), 26 (§ 193 StGB), 29–38 (Maßstäbe, Kriterien), 40–48 (Fehler der Fachgerichte)
– BVerfG, Beschl. v. 19.5.2020 – 1 BvR 2397/19: Rn. 12, 14 (Schutzbereich, allgemeines Gesetz), 15–27 (Abwägung, Schmähung, Formalbeleidigung, Menschenwürde), 32 (Position der Betroffenen)

Hinweise: Mattes und Professor Ruhland sind erfundene Figuren, ebenso die Stadträtin des Einstiegs. Reale Beteiligte werden nicht dargestellt, die Kommentare nicht zitiert. Mehr zum Tatbestand der Beleidigung in der Folge „Beleidigung, üble Nachrede, Verleumdung“, zum allgemeinen Gesetz in der Folge zum Lüth-Urteil.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#HassimNetz #Meinungsfreiheit #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("zwölf von zweiundzwanzig", "12 von 22"), ("Für zehn bleibt", "Für 10 bleibt"),
             ("neunzehnten Dezember", "19. Dezember"), ("STGB", "StGB"), ("Ruhland: ", "Professor Ruhland: ")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"Römisch (eins|zwei|drei|vier):( |\n)", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III.", "vier": "IV."}[m.group(1)] + m.group(2), srt)
srt = re.sub(r"\n\n\n+", "\n\n", srt)
assert not re.search(r"§\n|Abs\.\n|STGB|Römisch|zwölf|zweiundzwanzig|neunzehnten", srt), "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
