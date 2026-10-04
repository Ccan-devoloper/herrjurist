# Folge 159 · Auslegungsmethoden Jura: Wortlaut, Systematik, Historie, Telos – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_159.py`](src/skript_159.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Methodik · Auslegung, Themenplan-Format „Methodik“ (wie 117/123 ohne Rechtsfall-Rahmen; ein Beispielfall trägt den Film). Leitbeispiel nach dem Plan-Hook: Die Studentin Thekla fährt ruhig mit ihrem E-Scooter zur Uni (kein Unfall, kein Alkohol). Im Methodenseminar fragt Professor Lindhorst: „Ist Ihr E-Scooter eigentlich ein Kraftfahrzeug?“ Die vier Methoden prüfen § 1 Abs. 2 StVG (Wortlautkarte) mit gleicher Tafelstruktur **Frage – Werkzeug – Ergebnis am Beispiel** und je eigener Farbe: **Wortlaut Gelb**, **Systematik Blau** (Wortlautkarte § 1 Abs. 1 eKFV, Umkehrschluss aus § 1 Abs. 3 StVG), **Historie Lila** (Zitatkarte BR-Drs. 158/19), **Telos Grün** (OLG Hamm Rn. 32). Danach Rechtsprechung (BayObLG 2020, OLG Hamm 2025, BGH offen), Rückkehr ins Seminar, Abgrenzung Analogie/teleologische Reduktion/Analogieverbot, Klausurtipp (Lexi), Schema, Merksatz (Lexi). Hauptfilm 6:33,9 (5.428 vertonte Zeichen; Begründung der Länge in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Thekla (TH), Anfang 20 | Jurastudentin mit E-Scooter | Pose `standing/robot_dance-3` (Oberteil Koralle `#F07A6A`, Hose Dunkelblau `#3B3B4F`; die ausgestreckte Hand liegt auf dem Scooter an der Lenkstange), Kopf `Medium Bangs` (Haar `#7A4A2A`), keine Brille, Haut `#F2D3B8`; Mimiken `Calm`, `Smile` (lächelt/redet), `Smile Big\|Smile` (froh), `Suspicious` (denkt), `Concerned\|Serious` (staunt) | `ela_froh` (Frau, jung; heitere Rolle) |
| Professor Lindhorst (LI), um 60 | Dozent im Methodenseminar | Pose `standing/crossed_arms-1` (Pullover Grün `#8FD694`, schwarze Hose, Arme verschränkt), Kopf `Gray Short`, Brille `Glasses 3`, kein Bart, Haut `#E8B98F`; Mimiken `Calm`, `Serious` (redet/ernst), `Smile` (redet froh), `Smile Big\|Smile`, `Suspicious` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Beide Posen blicken mit diesen Köpfen im Original nach rechts (Kontaktbild `besetzung_159.png`, Mundzustand „a“ zeigt die Gesichtsseite). Grundansicht gespiegelt = blickt nach links (Tafelszenen, Thekla im Seminar zu Lindhorst), `_r` = nach rechts (Thekla auf dem Radweg in Fahrtrichtung, Lindhorst im Seminar zu Thekla).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `TH_redet`, `LI_redet`, `LI_redetfroh` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots, keine Karikatur.
- **Stimmen nur aus dem Pool** niklas, helmut, ela_froh, julia: `ela_froh` (Thekla, heitere Studentin), `helmut` (Professor). `julia` vermieden, `niklas` ohne Rolle. 158 nutzte laura_ruhig/william, 157 stephan/lucy.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keiner Textdatei unter `youtube/` (Suche `grep -rlw` über .md/.py/.json/.csv/.txt/.js/.html; ohne Treffer: Thekla, Lindhorst; verworfen: Merle, Edith (117), Henrike (127, 146), Jette (englische Lesart „Jet“ möglich)). Kein Genitiv eines Namens im Sprechtext (auf der Sachverhaltskarte nicht nötig).
- Präfixe `TH_`/`LI_` (nie `ER_`). Figuren-PNGs: `../peeps/op_159/` (50 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen** (Figurenrezepte 156–158 verglichen): 156 (`easing-2`, `shirt-3`, `walking-2`, `robot_dance-2`, `pointing_finger-2`), 157 (`resting-2`, `walking-1`), 158 (`shirt-4`, `easing-1`). 159: `robot_dance-3`, `crossed_arms-1` – nicht in 156–158; Koralle-Oberteil/grüner Pullover dort nicht in dieser Kombination; keine Muster. Schauplätze neu: Radweg vor einem Uni-Gebäude mit E-Scooter, Methodenseminar mit Seminartafel und Fenster (kein Hörsaal/Tutorium wie 117/123, keine Straße wie 158). Cremegrund durchgehend (Tageslicht, Morgensonne als Icon).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Radweg** `fall`→`ab` | Bodenlinie, grauer Radweg, Uni-Gebäude rechts; Thekla fährt auf dem E-Scooter von links nach rechts (Bewegung „fährt“ → „Radweg“), stellt ihn ab (Ständer), steht daneben | tabler:`sun` (Gelb), `tree` (Grün), `building-bank` (Weiß); E-Scooter programmatisch (`roller()`: Trittbrett Blau, Radnabenmotor Gelb, Tuschekontur; ohne Marke) | `Fall · Thekla fährt zur Uni` → `Fall · Vor dem Hörsaal` | ab 0,0 s vollständig (Radweg, Gebäude, Sonne, Pille „jeden Morgen zur Uni“, Thekla auf dem Scooter mit Schild) · „ruhig, auf dem Radweg“ · Hörsaal · abgestellt · Thekla froh | Motorsummen während der Fahrt (`szene_159summen_1`), Ständer-Klick (`szene_159staender_1`) |
| **A2 Seminar** `sem`→`t1` | Seminarraum: grüne Seminartafel „Methodenseminar / Auslegung“, Fenster mit dem abgestellten Scooter draußen; Lindhorst links (blickt zu Thekla), Thekla rechts | programmatisch | `Fall · Im Methodenseminar` → `… Ist der E-Scooter ein Kraftfahrzeug?` → `… Kein Auto, kein Sitz` | Raum · Blase Lindhorst · Thekla staunt · Blase Thekla · Lindhorst denkt | – |
| **A3 Hook** `hook`→`nur` | Tafel: Scooter-Skizze, „Fahrzeug? sogar Kraftfahrzeug?“, vier Methodenpillen in ihren Farben, Folgen (Kraftfahrer 1,1 ‰ / Radfahrer höher), § 316 nur „ein Fahrzeug“ | tabler:`car`, `bike` (Diagramm) | `Fall · Fahrzeug, sogar Kraftfahrzeug?` → `… Vier Wege, ein Gesetz zu lesen` → `… Warum es zählt: 1,1 ‰` → `… § 316 StGB verlangt nur „ein Fahrzeug“` | ≈ 12 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 8,7 s | – | `Sachverhalt` | 1 | – |
| **C Vier Methoden** `vier`→`bv` | Tafel: vier farbige Methodenzeilen, Schritte Frage → Werkzeug → Ergebnis, BVerfG-Satz | tabler:`help`, `tool`, `checkbox` (Diagramm), `list-numbers`, `scale` | `Methoden · Frage – Werkzeug – Ergebnis` → `… ergänzen sich, Ausgangspunkt Wortlaut` | ≈ 7 | – |
| **D1 1. Wortlaut** `w1`→`werg` | Methodentafel Gelb: Frage, Werkzeug, **Wortlautkarte § 1 Abs. 2 StVG**, drei Haken am Beispiel, Ergebnis | tabler:`abc`, `book`, `circle-check` | `1. Wortlaut · Frage und Werkzeug` → `… § 1 Abs. 2 StVG` → `… am Beispiel` → `… Ergebnis: Kraftfahrzeug` | ≈ 12 | – |
| **D2 Grenze** `gr1`→`gr2` | Tafel Gelb: **Wortlautkarte Art. 103 Abs. 2 GG**, Block „möglicher Wortsinn = äußerste Grenze“ | tabler:`barrier-block`, `book`, `ruler-measure` | `1. Wortlaut · Grenze im Strafrecht` → `… Art. 103 Abs. 2 GG` → `… möglicher Wortsinn als Grenze` | ≈ 5 | – |
| **E 2. Systematik** `s1`→`serg` | Methodentafel Blau: Frage, Werkzeug, **Wortlautkarte § 1 Abs. 1 eKFV (Auszug)** mit Markern, dann § 1 Abs. 3 StVG (Pedelec-Ausnahme), Kreuz „keine solche Ausnahme“, Umkehrschluss, Ergebnis | tabler:`puzzle`, `book`, `bike`, `circle-check` | `2. Systematik · Frage und Werkzeug` → `… § 1 Abs. 1 eKFV` → `… § 1 Abs. 3 StVG` → `… Ergebnis: Kraftfahrzeug` | ≈ 15 | – |
| **F 3. Historie** `h1`→`herg` | Methodentafel Lila: Frage, Werkzeug, **Zitatkarte BR-Drs. 158/19, S. 1**, Ergebnis | tabler:`history`, `file-text`, `circle-check` | `3. Historie · Frage und Werkzeug` → `… BR-Drs. 158/19` → `… Ergebnis: bewusst Kraftfahrzeug` | ≈ 8 | – |
| **G 4. Telos** `te1`→`teerg` | Methodentafel Grün: Frage, Werkzeug, Zweck des Grenzwerts, drei Merkmalkacheln (Motor bis 20 km/h, kleine Räder, Fahrer steht), OLG Hamm, Ergebnis | tabler:`bolt`, `circle-dot`, `arrow-big-up-line` (Diagramm), `target-arrow`, `shield-check`, `gauge`, `circle-check` | `4. Telos · Frage und Werkzeug` → `… Zweck des Grenzwerts` → `… am Beispiel` → `… Ergebnis: Kraftfahrzeug` | ≈ 11 | – |
| **H1 Rechtsprechung** `rs1`→`rs5` | Tafel: vier Methodenkacheln mit Haken, BayObLG-Block, OLG Hamm, BGH offen, Verweis Folge 130 | tabler:`gavel` (Holz), `help` | `Ergebnis · Rechtsprechung` → `… BayObLG 2020` → `… OLG Hamm 2025` → `… BGH: offengelassen` | ≈ 7 | – |
| **H2 Seminar (Rückkehr)** `l2`→`t2` | derselbe Seminarraum wie A2 (Rückkehr der Geschichte: Antwort auf die Frage), Blase Lindhorst, Blase Thekla | wie A2 | `Ergebnis · Vier Methoden, ein Ergebnis` → `… Nach der Party: stehen lassen` | 2 | – |
| **I1 Analogie** `ab1`→`an3` | Tafel: Balken Auslegung │ Rechtsfortbildung, Analogie-Definition, zwei Voraussetzungen mit Haken, Beispiel § 1004 BGB | tabler:`road`, `arrows-right-left`, `user-shield` | `Abgrenzung · Auslegung und Rechtsfortbildung` → `… Analogie` → `… Analogie: § 1004 BGB` | ≈ 9 | – |
| **I2 Reduktion, Analogieverbot** `tr1`→`av` | Tafel: Definition, Beispiel § 181 BGB, roter Block Analogieverbot, Verweis Folge 148 | tabler:`scissors`, `user-check`, `ban` | `Abgrenzung · teleologische Reduktion` → `… § 181 BGB` → `… Analogieverbot, Art. 103 Abs. 2 GG` | ≈ 8 | – |
| **J Klausurtipp** `tipp`→`tipp4` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Reihenfolge der Auslegung` → `… Merkhilfe, keine Rangfolge` → `… Materialien nur, wenn bekannt` | 8 | – |
| **K Klausurschema** `sch`→`k6` | breite Karte, Punkt für Punkt, Farbmarken der Methoden | – | `Klausurschema · Auslegung im Gutachten` → `… › I. 1. Wortlaut` … `… › II. Rechtsfortbildung` | 9 | – |
| **L Merksatz** `merke`→`mm2` | Lexi erklärt (redet), zwei Marker | – | `Merksatz` | 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; eine Bewegung (Fahrt auf dem Radweg, ≈ 4,3 s).
**Geräusche:** zwei Handlungsgeräusche (Motorsummen während der sichtbaren Fahrt, Ständer beim Abstellen), Freesound CC0 (IDs 587511, 78979) über die API ohne Schlüssel, eigene Namen `sfx3/szene_159summen_1.wav`, `sfx3/szene_159staender_1.wav`, Herkunft in `geraeusche_herkunft.json`. Haken, Marker und Schiebeblenden stumm.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 1 Abs. 2 StVG und Art. 103 Abs. 2 GG vollständig und vorgelesen; § 1 Abs. 1 eKFV als gekennzeichneter Auszug („…“, „(Auszug)“), gesprochen bis „mit elektrischem Antrieb“; Zitatkarte BR-Drs. 158/19 wörtlich (gesprochen bis „sind sie Kraftfahrzeuge“). Marker synchron zum Wort.
**Methodenfarben** (Auftrag: „je mit eigener Farbe“): Titelmarker, Randstreifen, Frage-/Werkzeug-/Ergebnis-Pillen und Ergebnisblock je Methode in Gelb/Blau/Lila/Grün; dieselben Farben in Hook, Überblick, Ergebniskacheln und Schema.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Thekla fährt jeden Morgen mit ihrem E-Scooter auf dem Radweg zur Uni. Der E-Scooter hat einen Elektromotor, eine Lenkstange, keinen Sitz und fährt höchstens 20 km/h. Treten muss Thekla nicht; hinten klebt eine Versicherungsplakette.
>
> Im Methodenseminar fragt Professor Lindhorst: „Ist Ihr E-Scooter eigentlich ein Kraftfahrzeug?“ Thekla antwortet: „Ein Kraftfahrzeug? Der hat doch nicht mal einen Sitz!“
>
> Davon hängt ab, welcher Promille-Grenzwert für E-Scooter-Fahrer bei der Trunkenheit im Verkehr (§ 316 StGB) gilt.
>
> **Ist der E-Scooter ein Kraftfahrzeug im Sinne von § 1 Abs. 2 StVG?**
