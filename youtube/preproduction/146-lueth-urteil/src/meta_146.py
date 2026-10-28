"""Nachbearbeitung der Upload-Texte für Folge 146 (nach meta_143.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Fall, Inhalt, Normen, Rechtsprechung mit Seiten,
Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Daten als Ziffern, Sprechername).
Aufruf: python3 meta_146.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Boykottaufruf im Filmblog"),
       (T("lueth"), "Der echte Fall: Lüth, Hamburg 1950"),
       (T("klage"), "Landgericht Hamburg 1951: § 826 BGB"),
       (T("sv"), "Sachverhalt"),
       (T("urteil"), "Abwehrrechte und objektive Wertordnung"),
       (T("medium"), "Mittelbare Drittwirkung: Generalklauseln"),
       (T("a13"), "Art. 1 Abs. 3 GG: Bindung des Zivilrichters"),
       (T("kontrast"), "Kontrast: Fraport"),
       (T("a5"), "Meinungsfreiheit, Art. 5 GG"),
       (T("g2"), "Wechselwirkung"),
       (T("abw"), "Güterabwägung: Vermutung für die freie Rede"),
       (T("motiv"), "Die Abwägung im Fall Lüth"),
       (T("pruef"), "Prüfungsmaßstab: keine Superrevision"),
       (T("erg"), "Ergebnis"),
       (T("w2"), "Zurück zum Fall: Wenke"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Prüfschema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Lüth-Urteil (BVerfGE 7, 198): Wie Grundrechte über Generalklauseln wie § 826 BGB auch zwischen Bürgern wirken – mittelbare Drittwirkung und Art. 5 I GG.

Der Fall: Am 20. September 1950 spricht der Hamburger Senatsdirektor Erich Lüth als Vorsitzender des Hamburger Presseklubs gegen das Wiederauftreten des Regisseurs Veit Harlan, der in der Zeit des Nationalsozialismus den antisemitischen Film „Jud Süß“ gedreht hatte. In einem offenen Brief ruft er dazu auf, sich auch zum Boykott bereitzuhalten. Das Landgericht Hamburg verurteilt ihn am 22. November 1951 auf die Klage der Produktionsfirma und der Verleiherin des Films „Unsterbliche Geliebte“ zur Unterlassung (§ 826 BGB). Am 15. Januar 1958 entscheidet das Bundesverfassungsgericht.

Inhalt:
– Einstieg: Eine Bloggerin ruft zum Boykott eines Kinofilms auf, der Produzent klagt auf Unterlassung
– Grundrechte als Abwehrrechte und als objektive Wertordnung; Wirkung durch das Medium des Privatrechts; Generalklauseln als „Einbruchstellen“; mittelbare Drittwirkung
– Art. 1 Abs. 3 GG (im Wortlaut): gebunden ist der Zivilrichter; Kontrast zum Fraport-Urteil
– Art. 5 Abs. 1 Satz 1, Abs. 2 GG (im Wortlaut): § 826 BGB als allgemeines Gesetz, Wechselwirkung, Güterabwägung, Vermutung für die freie Rede
– Abwägung im Fall Lüth, Prüfungsmaßstab der Urteilsverfassungsbeschwerde (keine Superrevisionsinstanz, Ausstrahlungswirkung), Ergebnis
– Lösung des Einstiegsfalls, Klausurtipp, Prüfschema, Merksatz

Normen: Art. 1 Abs. 3, Art. 5 Abs. 1 Satz 1, Abs. 2 GG; § 826 BGB

Rechtsprechung:
– BVerfG, Urt. v. 15.1.1958 – 1 BvR 400/51, BVerfGE 7, 198 (Lüth): S. 199–202 (Sachverhalt), 204 f. (Abwehrrechte, objektive Wertordnung), 205 f. (Privatrecht, Generalklauseln), 206 f. (Bindung des Zivilrichters, Prüfungsmaßstab), 208 f. (Wechselwirkung), 210–212 (Güterabwägung, Vermutung für die freie Rede), 213–221 (Abwägung im Fall), 230 (Ergebnis)
– BVerfG, Beschl. v. 10.6.1964 – 1 BvR 37/63, BVerfGE 18, 85, S. 92 (spezifisches Verfassungsrecht)
– BVerfG, Urt. v. 22.2.2011 – 1 BvR 699/06, BVerfGE 128, 226 (Fraport), Rn. 45, 49

Hinweise: Wenke und Herr Gerstner sind erfundene Figuren; Erich Lüth und Veit Harlan werden nicht dargestellt. Aus dem Film „Jud Süß“ wird nichts gezeigt oder zitiert. Den Aufbau der Grundrechtsprüfung erklärt eine eigene Folge. Nicht behandelt: Zulässigkeit der Verfassungsbeschwerde, § 823 BGB, Schutzpflichten.

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusch: Freesound (CC0).

#LüthUrteil #Grundrechte #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
for a, b in [("zwanzigster September", "20. September"), ("zweiundzwanzigsten\nNovember", "22.\nNovember"),
             ("fünfzehnten Januar", "15. Januar"), ("Gerstner: ", "Herr Gerstner: ")]:
    assert a in srt, a
    srt = srt.replace(a, b)
srt = re.sub(r"Römisch (eins|zwei|drei):( |\n)", lambda m: {"eins": "I.", "zwei": "II.", "drei": "III."}[m.group(1)] + m.group(2), srt)
assert not re.search(r"§\n|Abs\.\n", srt) and "zwanzigst" not in srt, "Untertitel prüfen"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
