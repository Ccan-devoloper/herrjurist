# Folge 046 · Schadensersatz Schema: Das System der §§ 280 ff. BGB – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_046.py`](src/skript_046.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall, Themenplan-Format „Schema“ (Leitentscheidung im Plan leer). Ein Beispielfall nach dem Plan-Hook trägt das ganze System: ein Händler, drei Schäden, drei Anspruchsgrundlagen. Ablauf: Kauf → Verspätung (Waschsalon) → Lieferung mit Stoß → Wasserschaden → Frist und Werkstatt → Frage → Sachverhalt → Wortlaut § 280 I (vier Merkmale, Vermutung) → Wortlaut § 280 II, III → drei Arten → Kontrollfrage (BGH) → A. Wasserschaden (neben der Leistung, § 437 Nr. 3, § 280 I) → B. Waschsalon (Verzögerungsschaden, Verzug § 286) → C. Reparatur (statt der Leistung, Wortlaut § 281 I 1) → §§ 282, 283, 311a II → Klausurtipp → Schema als Entscheidungsbaum → Merksatz.
**Länge:** Hauptfilm 6:37,3 (5.594 Zeichen, Grenze 6.200). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Gisela (GI), um 60 | Käuferin (Verbraucherin) | `standing/resting-1` (Oberteil Lila `#B8A9F5`, schwarze Hose), Kopf `Gray Bun`, Brille `Glasses 4`, Haut `#F0C8A8`; Mimiken `Calm`, `Smile`, `Fear` (Schreck; redet), `Concerned|Serious`, `Very Angry`, `Suspicious`, `Serious` | `hilde` (Frau, älter) |
| Herr Kranz (KR), um 30 | Elektrohändler, liefert und schließt selbst an | `standing/shirt-4` (dunkles Hemd, Arbeitshose Blau `#5A6E9A`), Kopf `Short 5`, kein Bart, keine Brille, Haut `#E2B08C`; Mimiken `Calm`, `Smile`, `Concerned|Serious` (redet, Sorge), `Fear`, `Serious`, `Tired`, `Suspicious` | `timo` (Mann, jung) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht aus früheren Folgen: Gisela, Kranz. Kein Genitiv „Giselas“ im Sprechtext.
- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `GI_redet`, `KR_redet` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool** timo, julia, otto, hilde; gebraucht: hilde, timo (julia war Imke in 037; otto „unsicher“ nicht gebraucht).
- Figuren-PNGs: `../peeps/op_046/` (52 Dateien, nicht im Repository, im Drive-Master).
- Keine Verletzten, keine Gewalt; der Stoß trifft nur die Maschine.

**Abweichung von den letzten Folgen:** 045 (Lösungsskizze/Zeitplan), 044 (Verwaltungsakt), 043 (Stellvertretung), 037 (Firmenwagen, Büro). Hier neu: Elektrogeschäft, Wohnung mit Treppe, Bad mit Waschmaschine, Waschsalon; Lieferwagen nur als stehendes Requisit. Neue Posen gegenüber 037 (`easing-1`, `blazer-3`).

## Szenen

Alle Szenen auf Cremegrund (Tag).

| Szene | Ort / Handlung | Requisiten (Tabler, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Der Kauf** `fall`, `termin` | Elektrogeschäft, Gisela links, Kranz rechts | `building-store` (Blau), `wash-machine` (Weiß), `calendar-event` (Gelb) | `Fall · Der Kauf` (ab 0,0 s) | Laden · Waschmaschine · Kalender · „Lieferung und Anschluss: 2. März“ | – |
| **A2 Die Verspätung** `warten`, `salon` | Gisela wartet; dann Waschsalon | `calendar-x`, `basket`, 2 × `wash-machine` | `Fall · Die Verspätung` | 2. März · Termin vergessen · eine Woche später · Waschsalon · 30 € | – |
| **A3 Die Lieferung** `k1`, `stoss` | Lieferwagen, Kranz (redet, Blase), Treppe, Gisela; Maschine kippt gegen die Treppe | `truck-delivery`, `stairs`, `wash-machine` (gekippt) | `Fall · Die Lieferung` | Blase · Maschine · Stoß (Schreck) · unachtsam · Schlauch | Stoß `szene_046stoss_1` |
| **A4 Das Bad** `flut`–`g1` | Badewanne, Maschine, Wasser auf dem Boden, Flur; Gisela (redet, Blase) | `bath`, `wash-machine`, `droplets` (Blau), `ripple`, Wasserlinie | `Fall · Das Bad` | Wasser · flutet das Bad · Parkett · 1.500 € · Blase | Wasser `szene_046wasser_1` |
| **A5 Frist und Werkstatt** `frist`–`werk` | Gisela allein | `calendar-event`, `phone-off`, `tool`, `wash-machine` | `Fall · Frist zur Reparatur` | Frist · keine Antwort · Werkstatt · 200 € | – |
| **A6 Die Frage** `frage`, `frage2` | Gisela und Kranz, drei Schadensblöcke | `scale` | `Fall · Die Frage` | drei Schäden · ein Händler · Frage | – |
| **B Sachverhalt** `sv` | Karte vollständig, 10 s | – | `Sachverhalt` | 1 | – |
| **C § 280 I** `agl`–`verm` | Wortlautkarte mit Markern, vier Merkmale, Vermutung | `scale` | `Anspruchsgrundlage · § 280 Abs. 1 BGB` → `… › Grundtatbestand` → `§ 280 Abs. 1 Satz 2 BGB › Vertretenmüssen vermutet` | Karte · 4 Marker · 4 Merkmale · Block | – |
| **D § 280 II, III** `w2`, `w3` | zwei Wortlautkarten | `hourglass`, `refresh` | `§ 280 Abs. 2 BGB › …` → `§ 280 Abs. 3 BGB › …` | 2 Karten · 4 Marker | – |
| **E1 Drei Arten** `drei`–`a3` | drei Farbblöcke | – | `System · drei Arten …` | 3 | – |
| **E2 Kontrollfrage** `test`–`test3` | Frageblock, BGH-Fundstellen, Ja/Nein | `tool` | `System · Kontrollfrage` | 5 | – |
| **F1/F2 A. Wasserschaden** `wass`–`wp5` | Zuordnung, dann Prüfung I.–IV. | `droplets`, `file-text`, `wash-machine` | `A. Wasserschaden … › Zuordnung` → `… › neben der Leistung, §§ 437 Nr. 3, 280 Abs. 1 BGB` → `… › I.–IV.` | 12 | – |
| **G1/G2 B. Waschsalon** `verz`–`v5` | Zuordnung, Verzug 1.–3. | `wash-machine`, `calendar-event` | `B. Waschsalon … › Zuordnung` → `› Verzögerungsschaden …` → `› Verzug, § 286 BGB › Fälligkeit/Mahnung/Vertretenmüssen` → `› Ergebnis` | 11 | – |
| **H1/H2 C. Reparatur** `statt`–`f4` | Zuordnung, Wortlautkarte § 281 I 1, Prüfung | `tool`, `calendar-event` | `C. Reparatur … › Zuordnung` → `› statt der Leistung …` → `C. Reparatur, §§ 280 Abs. 1, 3, 281 BGB › …` → `› Ergebnis` | 12 | – |
| **I1 § 282** `weg`–`p282b` | Tafel, Maler-Beispiel | `brush`, `armchair` | `Statt der Leistung › weitere Wege` → `› Rücksichtspflicht, § 282 BGB` | 5 | – |
| **I2 §§ 283, 311a II** `p283`–`p311b` | Tafel | `flame`, `file-text` | `Statt der Leistung › nachträglich, § 283 BGB` → `› anfänglich, § 311a Abs. 2 BGB` | 6 | – |
| **J Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (2 Stände) | 5 | – |
| **K Klausurschema** `sch`–`sb10` | Entscheidungsbaum, Aufbau Knoten für Knoten | – | `Klausurschema` → `› neben der Leistung` → `› statt der Leistung` → `› jeweils § 280 Abs. 1 BGB` | 11 | – |
| **L Merksatz** `merke`, `merke2` | Lexi erklärt, Merksatz mit Markern | – | `Merksatz` | 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 22 Folien; innerhalb harte Schnitte und Pops; keine Kamerafahrt.
**Blasen:** wortgleich mit dem Gesprochenen.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Gisela kauft für ihre Wohnung beim Elektrohändler Kranz eine Waschmaschine. Vereinbart sind Lieferung und Anschluss am 2. März. Herr Kranz vergisst den Termin und kommt erst eine Woche später; bis dahin zahlt Gisela 30 Euro im Waschsalon.
>
> Beim Ausladen stößt Herr Kranz die Maschine unachtsam gegen die Treppe; innen reißt ein Schlauch. Beim ersten Waschgang flutet auslaufendes Wasser das Bad, der Parkettboden im Flur quillt auf (Schaden 1.500 Euro).
>
> Gisela verlangt die Reparatur und setzt eine Frist von zwei Wochen. Herr Kranz meldet sich nicht. Eine Werkstatt repariert die Maschine für 200 Euro.
>
> **Welche Ansprüche hat Gisela gegen Herrn Kranz?**
