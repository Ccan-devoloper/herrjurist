# Folge 056 · Werkvertrag oder Dienstvertrag? Abgrenzung nach §§ 611, 631, 650 BGB – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_056.py`](src/skript_056.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Werkvertragsrecht, Themenplan-Format „Abgrenzung“ (Leitentscheidung im Plan leer). Beispielfall nach dem Plan-Hook („Der Nachhilfelehrer garantiert keine Note – der Maler aber eine gestrichene Wand“): Mareike bucht bei Henrik zehn Stunden Nachhilfe zu je 30 € und lässt ihr Zimmer von der Malerin Frau Ostertag für 400 € streichen. Am Freitag ist die Wand fleckig, Mareike nimmt sie nicht ab; die Statistikklausur besteht sie trotz Nachhilfe nicht und will Henrik nicht bezahlen. Ablauf: Fall → Frage/Hook → Sachverhalt → Wortlaut § 611 I → Wortlaut § 631 I, II → Kriterium Tätigkeit/Erfolg, Auslegung → Subsumtion → Grenzfälle (Arzt, Website/Software, Wartung) → Werklieferung (Wortlaut § 650 I 1, Vorgaben, Lift-Gegenfall) → Folgen Werkvertrag (§§ 640, 641, Herstellungsanspruch, § 634) → Folgen Dienstvertrag (keine Gewährleistung, § 280 I) → Vergütung §§ 612, 632, Arbeitsvertrag § 611a → Klausurtipp → Entscheidungsbaum → Merksatz.
**Länge:** Hauptfilm 6:33,3 (5.615 Zeichen). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Mareike (MA), um 22 | Studentin; Dienstberechtigte (Nachhilfe) und Bestellerin (Malerin, Regal) | `standing/resting-1` (Pullover Lila `#B8A9F5`, schwarze Hose, weiße Schuhe), Kopf `Long`, Haut `#F2C9A5`; Mimiken `Calm`, `Smile Big|Smile` (froh), `Serious` (denkt; redet), `Suspicious` (überlegt), `Concerned|Serious` (Sorge), `Tired` (müde, nach der Klausur) | `julia` (Frau, jung) |
| Henrik (HE), um 25 | Nachhilfelehrer | `standing/robot_dance-3` (offene, erklärende Hand; Oberteil Grün `#8FD694`, gelbe Hose), Kopf `Pomp`, Haut `#B9825C`, kein Bart; Mimiken `Calm`, `Smile` (froh; redet), `Suspicious` (denkt), `Serious` (ernst) | `niklas` (Mann, jung) |
| Frau Ostertag (OS), um 30 | Malerin (Unternehmerin) | `standing/shirt-3` (weißes Arbeitshemd, schwarze Hose), Kopf `Bangs` (blond), Haut `#E9B48A`; Mimiken `Calm`, `Smile` (froh; redet), `Serious` (denkt), `Concerned|Serious` (ertappt) | `ela_warm` (Frau, jung) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge vergeben (geprüft gegen alle `skript_*.py`, `SZENENPLAN.md`, `ABNAHME.md` und die Liste des Koordinators; „Greta“ [003], „Brandt“ [004] und „Hannes“ [005] verworfen): Mareike, Henrik, Ostertag. Kein Genitiv eines Namens im Sprechtext.
- Grundansicht gespiegelt (blickt nach links zur Tafel bzw. zur Partnerfigur), `_r` blickt nach rechts (Mareike am Lernplatz zu Henrik; Frau Ostertag beim Reden zu Mareike).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `MA_redet`, `HE_redet`, `OS_redet` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool** niklas, julia, timo, ela_warm; gebraucht julia, niklas, ela_warm. `timo` (zuletzt 053) nicht gebraucht; keine Überschneidung mit 055 (laura_klar, marc).
- Keine Prothesen-Posen (shirt-1/-2, blazer-1/-2 verworfen), keine Bärte; die Malerin ist eine Frau (keine Rollenklischees).
- Figuren-PNGs: `../peeps/op_056/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 055 (Gewahrsamsenklave), 054 (Zwangsvollstreckung), 053 (Vorgarten, Fahrrad), 034 (Einfahrt im Querschnitt, Pflasterer). Hier neu: Lernplatz mit Schreibtisch, Büchern, Taschenrechner und Kalender; Zimmerwand im Aufriss, die bei „streichen“ weiß wird (Farbroller fährt hoch) und am Freitag Streifen und Flecken zeigt; Klausur mit Prüfungsblatt. Posen `resting-1`, `robot_dance-3`, `shirt-3` (mit Kopf `Bangs`) erscheinen in 050–055 nicht; Werkvertrag-Folge 034 hatte andere Posen und Schauplätze.

## Szenen

Alle Szenen auf Cremegrund (Tag).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Lernplatz** `fall`–`h1` | Mareike am Schreibtisch, Kalender „6 Wochen“; Henrik kommt, Pillen 10 Stunden / je 30 €; Henrik redet (Blase) | ph:`desk` (Gelb), ph:`books` (Blau), tabler:`calculator`, `calendar-event` | `Fall · Die Statistikklausur` (ab 0,0 s) → `Fall · Die Nachhilfe` | Grundbild · Henrik · 10 Stunden · 30 € · Blase | – |
| **A2 Zimmerwand** `maler`–`m1` | alte Wand (beige), Frau Ostertag mit Eimer, Farbroller fährt hoch, Wand wird weiß; Blase Ostertag, 400 €; Freitag: Streifen und Flecken, Ostertag ertappt, Mareike redet (Blase) | ph:`paint-roller`, tabler:`bucket`; Wand aus `karte`, Streifen/Flecken aus `linienzug`/Ellipsen in Palettengrau | `Fall · Die Malerin` → `Fall · Freitag: die Wand` | alte Wand · weiß · Blase · 400 € · Freitag/Streifen · Pille fleckig · Blase Mareike | Farbroller `szene_056rolle_1` bei „streichen“ |
| **A3 Lernplatz** `stunden`–`hook` | Lernplatz wie A1 (Rückkehr: gleiche Personen, gleicher Ort); Prüfungsblatt mit Kreuz, „durchgefallen“; Mareike redet (Blase); zwei Fragen, Hook als zwei Pillen | tabler:`file-x` (Rot) + Schreibtisch | `Fall · Die Klausur` → `Fall · Die Frage` | wie vereinbart · Blatt · durchgefallen · Blase · Frage 1 · Frage 2 · Hook 1 · Hook 2 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | 1 | – |
| **C1 § 611 I** `p611` | Wortlautkarte mit 2 Markern; Henrik, Mareike | tabler:`chalkboard` | `Die Vertragstypen · Dienstvertrag, § 611 Abs. 1 BGB` | Karte · Dienste · Marker/Zeile · Marker/Zeile | – |
| **C2 § 631 I, II** `p631`–`p631c` | zwei Wortlautkarten mit Markern; Ostertag, Mareike | ph:`paint-roller`, tabler:`checks` | `… Werkvertrag, § 631 Abs. 1 BGB` → `… § 631 Abs. 2 BGB` | Karten · Marker I · Veränderung · Erfolg | – |
| **D Kriterium** `krit`–`hilf` | zwei Farbblöcke, Auslegungs-Pillen, Hilfsfrage | – | `Abgrenzung · Tätigkeit oder Erfolg?` → `Abgrenzung · Auslegung, §§ 133, 157 BGB` | Titel · Dienst · Werk · Auslegung · 3 Pillen · Hilfsfrage | – |
| **E Subsumtion** `nhs`–`wv` | Tafel; Henrik, Ostertag | – | `Subsumtion · die Nachhilfe` → `· die Malerin` | 6 | – |
| **F1 Arzt** `grenz`–`arzt2` | Tafel, Stethoskop, Herzschlag | tabler:`stethoscope`, `heartbeat` (Rot) | `Grenzfälle · 1. der Arzt, § 630a BGB` | 4 | – |
| **F2 Website, Wartung** `web`–`wart2` | Tafel | tabler:`world-www`, `code`, `tool`, `settings` | `Grenzfälle · 2. Website und Software` → `· 3. Wartung` | 6 | – |
| **G1 Werklieferung** `wl`–`p650` | Tafel, Wortlautkarte § 650 I 1 mit 3 Markern | ph:`ruler`, `books`; tabler:`hammer`, `truck-delivery` | `Werklieferungsvertrag · erst hergestellt, dann geliefert` → `· § 650 Abs. 1 BGB` | 7 | – |
| **G2 Vorgaben, Einbau** `x82`–`einb2` | Tafel; Mareike | ph:`books`; tabler:`elevator`, `home` | `Werklieferungsvertrag · nach Vorgaben des Kunden` → `Abgrenzung · Schwerpunkt Einbau vor Ort` | 5 | – |
| **H1 Folgen Werkvertrag** `folg`–`faell` | Tafel; Ostertag, Mareike | tabler:`checks`, `cash-banknote` | `Folgen · Werkvertrag: Abnahme, § 640 Abs. 1 BGB` → `· Fälligkeit, § 641 Abs. 1 BGB` | 4 | – |
| **H2 Die fleckige Wand** `fleck`–`m634` | Tafel, Kreuz/Haken, vier Mängelrechte-Pillen | tabler:`wall` | `Werkvertrag · die fleckige Wand, § 640 Abs. 1 Satz 2 BGB` → `· Herstellung, § 631 Abs. 1 BGB` → `· Mängelrechte, § 634 BGB` | 8 | – |
| **I Folgen Dienstvertrag** `dfolg`–`zahl` | Tafel; Henrik, Mareike | tabler:`chalkboard`, `cash-banknote` | `Folgen · Dienstvertrag: keine Gewährleistung` → `· § 280 Abs. 1 BGB` → `· Henrik` | 7 | – |
| **J Vergütung, Arbeitsvertrag** `verg`–`p611a` | Tafel | tabler:`cash-banknote`, `briefcase` (Lila), `chalkboard`; ph:`paint-roller` | `Vergütung · stillschweigend vereinbart, §§ 612, 632 BGB` → `Arbeitsvertrag · § 611a BGB` | 6 | – |
| **K Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · erst einordnen` | 4 | – |
| **L Entscheidungsbaum** `sch`–`s2n` | breite Karte, Baum wächst Frage für Frage (Pfeile Nein/Ja) | – | `Entscheidungsbaum` → `› nur Tätigkeit: Dienstvertrag` → `› Erfolg: bewegliche Sache geliefert?` | Titel · Frage 1 · Nein · Dienstvertrag · Ja · Frage 2 · Ja/§ 650 · Nein/Werkvertrag | – |
| **M Merksatz** `merke`–`mk3` | Lexi erklärt, Merksatz mit drei Markern | – | `Merksatz` | 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 19 Folien; innerhalb harte Schnitte und Pops; Bewegung nur beim Farbroller (Streichen).
**Blasen:** wortgleich mit dem Gesprochenen (Zahlen als Wort).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Mareike bucht für ihre Statistikklausur bei Henrik zehn Stunden Nachhilfe zu je 30 Euro. Henrik sagt: „Ich erkläre dir den Stoff. Bestehen musst du selbst.“ Er gibt alle zehn Stunden wie vereinbart. Mareike fällt trotzdem durch und will die 300 Euro nicht zahlen.
>
> Außerdem lässt Mareike ihr Zimmer von der Malerin Frau Ostertag streichen. Frau Ostertag sagt: „Bis Freitag ist die Wand weiß. Das macht 400 Euro.“ Am Freitag ist die Wand fleckig und voller Streifen. Mareike nimmt die Wand nicht ab und verlangt, dass Frau Ostertag noch einmal streicht.
>
> **Muss Mareike für die Nachhilfe zahlen, was kann sie von Frau Ostertag verlangen?**
