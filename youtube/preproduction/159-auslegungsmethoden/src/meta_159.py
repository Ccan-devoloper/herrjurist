"""Nachbearbeitung der Upload-Texte für Folge 159 (nach meta_158.py) nach tools/youtube_metadaten.py (dort nichts
geändert): sprechende Kapitel (ab 0:00, jedes ≥ 10 s), Beschreibung mit Planbeschreibung, Fall, Inhalt, Normen,
Rechtsprechung mit Randnummern, Hinweisen und Lizenzzeile; Untertitel-Korrekturen (Paragrafen, Zahlen, Abkürzungen).
Aufruf: python3 meta_159.py <upload-ordner>"""
import json, re, sys

U = sys.argv[1]
cj = json.load(open("../cues.json"))
T = lambda c: cj["cues"][c]["t"] + 8.0
KAP = [(0.0, "Der Fall: Ist ein E-Scooter ein Kraftfahrzeug?"),
       (T("vier"), "Vier Methoden, gleiche Struktur"),
       (T("w1"), "1. Wortlaut: § 1 Abs. 2 StVG"),
       (T("gr1"), "Wortlaut als Grenze: Art. 103 Abs. 2 GG"),
       (T("s1"), "2. Systematik: eKFV und § 1 Abs. 3 StVG"),
       (T("h1"), "3. Historie: die Materialien"),
       (T("te1"), "4. Telos: Sinn und Zweck"),
       (T("rs1"), "Ergebnis der Rechtsprechung"),
       (T("ab1"), "Analogie und teleologische Reduktion"),
       (T("tipp"), "Klausurtipp"),
       (T("sch"), "Schema"), (T("merke"), "Merksatz")]
mmss = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
for (a, _), (b, _) in zip(KAP, KAP[1:]):
    assert b - a >= 10, (a, b)
kapitel = "\n".join(f"{mmss(t)} {n}" for t, n in KAP)
open(f"{U}/kapitel.txt", "w").write(kapitel + "\n")

BESCHR = f"""Die vier Auslegungsmethoden an einem Fall erklärt: Wortlaut, Systematik, Historie und Telos – und wie du sie in der Klausur überzeugend einsetzt.

Der Fall: Thekla fährt jeden Morgen mit ihrem E-Scooter zur Uni. Im Methodenseminar fragt Professor Lindhorst: „Ist Ihr E-Scooter eigentlich ein Kraftfahrzeug?“ Davon hängt ab, welcher Promille-Grenzwert für E-Scooter-Fahrer bei der Trunkenheit im Verkehr gilt.

Inhalt:
– Jede Methode mit derselben Struktur: Frage, Werkzeug, Ergebnis am Beispiel
– 1. Wortlaut: § 1 Abs. 2 StVG (im Wortlaut); im Strafrecht zugleich Grenze, Art. 103 Abs. 2 GG (im Wortlaut)
– 2. Systematik: § 1 Abs. 1 eKFV (Auszug im Wortlaut) und der Umkehrschluss aus § 1 Abs. 3 StVG (Pedelecs)
– 3. Historie: Begründung der Elektrokleinstfahrzeuge-Verordnung, BR-Drs. 158/19
– 4. Telos: Wozu gibt es den Grenzwert?
– Ergebnis der Rechtsprechung: E-Scooter sind Kraftfahrzeuge, 1,1 ‰; der BGH hat die Grenzwertfrage offengelassen
– Abgrenzung: Analogie (planwidrige Regelungslücke, vergleichbare Interessenlage), teleologische Reduktion, Analogieverbot im Strafrecht
– Klausurtipp, Schema, Merksatz

Normen: § 1 Abs. 2, 3 StVG; § 1 Abs. 1 eKFV; § 316 StGB; Art. 103 Abs. 2 GG; §§ 181, 1004 BGB

Rechtsprechung und Materialien:
– BVerfG, Urt. v. 19.3.2013 – 2 BvR 2628/10 u. a., Rn. 66 (Auslegungsmethoden ergänzen sich, Ausgangspunkt Wortlaut)
– BVerfG, Beschl. v. 19.3.2007 – 2 BvR 2273/06, Rn. 11 (möglicher Wortsinn als Grenze, Analogieverbot)
– BayObLG, Beschl. v. 24.7.2020 – 205 StRR 216/20 (E-Scooter als Kraftfahrzeug, 1,1 ‰)
– OLG Hamm, Urt. v. 8.1.2025 – 1 ORs 70/24, Rn. 22, 30–32, 41
– BGH, Beschl. v. 2.3.2021 – 4 StR 366/20, Rn. 8; Beschl. v. 13.4.2023 – 4 StR 439/22, Rn. 4 f. (Grenzwert für Elektrokleinstfahrzeuge offengelassen)
– BR-Drs. 158/19, S. 1 (Begründung der eKFV)
– BGH, Urt. v. 7.11.2019 – I ZR 42/19, Rn. 32 (Voraussetzungen der Analogie)
– BGH, Urt. v. 14.12.2021 – VI ZR 403/19, Rn. 9 (§ 1004 BGB analog, Persönlichkeitsrecht)
– BGH, Urt. v. 7.9.2017 – IX ZR 224/16, Rn. 17 (teleologische Reduktion des § 181 BGB)

Hinweise: § 316 StGB verlangt nur „ein Fahrzeug“; der Kraftfahrzeugbegriff entscheidet über den Grenzwert der absoluten Fahruntüchtigkeit. „Wortlaut zuerst, Telos entscheidet oft“ ist eine Merkhilfe, keine feste Rangfolge. Mehr zu den Promillegrenzen in der Folge zu § 316 StGB, mehr zum Analogieverbot in der Folge zur Unfallflucht (§ 142 StGB).

Kapitel:
{kapitel}

Dieses Video dient der Examensvorbereitung und ersetzt keine Rechtsberatung. Rechtsstand: 4. Oktober 2026.

Figuren: Open Peeps (Pablo Stanley, CC0). Icons: Tabler Icons, Fluent Emoji (MIT). Warnsymbol: Streamline Freehand (CC BY 4.0, streamlinehq.com). Geräusche: Freesound (CC0).

#Auslegung #Methodik #Jura
"""
open(f"{U}/beschreibung.txt", "w").write(BESCHR)

srt = open(f"{U}/untertitel.srt").read()
srt = re.sub(r"(§§?)\n(\S+) ", r"\1 \2\n", srt)
srt = re.sub(r"(Abs\.)\n(\d+[,.:;]?) ?", r"\1 \2\n", srt)
ERSATZ = [("Paragraf eins Absatz zwei Straßenverkehrsgesetz", "§ 1 Abs. 2 StVG"),
          ("Paragraf eins Absatz drei Straßenverkehrsgesetz", "§ 1 Abs. 3 StVG"),
          ("Paragraf dreihundertsechzehn", "§ 316"), ("Paragraf tausendvier", "§ 1004"),
          ("Paragraf hunderteinundachtzig", "§ 181"), ("Artikel hundertdrei Absatz zwei", "Art. 103 Abs. 2"),
          ("eins Komma eins Promille", "1,1 Promille"), ("zwanzig Kilometer pro Stunde", "20 km/h"),
          ("Bundesratsdrucksache hundertachtundfünfzig", "Bundesratsdrucksache 158"),
          ("zweitausendneunzehn", "2019"), ("zweitausendzwanzig", "2020"), ("zweitausendfünfundzwanzig", "2025"),
          ("Folge hundertdreißig", "Folge 130"), ("Folge hundertachtundvierzig", "Folge 148"),
          ("B.G.B.", "BGB")]
for a, b in ERSATZ:
    n = srt.count(a)
    srt = srt.replace(a, b)
    # Zeilenumbruch mitten in der Wendung: Leerzeichen und Umbruch tolerieren
    if n == 0:
        muster = r"\s+".join(map(re.escape, a.split()))
        srt, k = re.subn(muster, b, srt)
        assert k, f"nicht im Untertitel: {a}"
assert not re.search(r"§\n|Abs\.\n", srt), "Untertitel prüfen"
assert "hundert" not in srt and "tausend" not in srt and "B.G.B." not in srt, "Zahlwort im Untertitel"
open(f"{U}/untertitel.srt", "w").write(srt)

m = json.load(open(f"{U}/metadaten.json"))
m["beschreibung"] = BESCHR
m["kapitel"] = [[mmss(t), n] for t, n in KAP]
open(f"{U}/metadaten.json", "w").write(json.dumps(m, ensure_ascii=False, indent=1))
print(len(KAP), "Kapitel; Beschreibung", len(BESCHR), "Zeichen")
