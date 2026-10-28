# Folge 123 · Prüfungsschemata lernen – aber richtig: Verstehen statt pauken – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_123.py`](src/skript_123.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Methodik · Lernen, Themenplan-Format „Methodik“. Rahmen nach dem Plan-Hook: Der Jurastudent Gunnar hat 80 Schemata auf Karteikarten auswendig gelernt (Turm auf dem Schreibtisch) und scheitert im Tutorium an einem Fall, der „nicht im Schema steht“: Ein Spaziergänger behält ein verlorenes Handy vom Gehweg (§ 242 scheitert an der Wegnahme; Lösung § 246). Die Tutorin Marlene zeigt drei Werkzeuge: (1) das Schema als Landkarte des Gesetzes (Wortlautkarte § 242 Abs. 1 StGB), (2) „Warum steht der Punkt hier?“ (Zueignungsabsicht subjektiv; entstanden – untergegangen – durchsetzbar, Verweis 103), (3) Transfer: § 246 aus dem Wortlaut neben § 242 gebaut (Wortlautkarte § 246 Abs. 1 StGB). Danach Lernen mit Fällen statt Listen, Klausurtipp (Lexi), Klausurschema § 246 progressiv, Merksatz (Lexi). Hauptfilm 5:11,1 (4.284 vertonte Zeichen).
**Eigene Gliederung (Abweichung vom Plan-Kern):** Die vier Kernpunkte des Auftrags sind als „drei Werkzeuge“ (Rahmen) plus ein Lernabschnitt umgesetzt; das Klausurschema ist das aus dem Wortlaut gebaute § 246-Schema (es schließt den Transfer ab), keine Lern-Checkliste.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Gunnar (GU), Anfang 20 | Jurastudent mit Karteikarten-Turm | Pose `standing/easing-1` (offenes Hemd Grün `#8FD694` über weißem Shirt, Hose `#2B2B2B`, Turnschuhe), Kopf `Short 4` (Haar `#6B4A32`), keine Brille, Haut `#E8B98F`; Mimiken `Tired` (müde vom Pauken), `Smile Big\|Smile` (stolz/froh), `Suspicious` (denkt), `Concerned\|Serious` (Sorge), `Calm`, `Serious` (redet: g1), `Smile` (redet froh: g2, g3) | `niklas` (Mann, jung) |
| Marlene (MA), Mitte 20 | Tutorin, zeigt die drei Werkzeuge | Pose `standing/blazer-3` (Blazer Rot `#F07A6A` über schwarzem Top, Hose `#3B3B4F`, Hand an der Hüfte), Kopf `Medium 3` (Haar `#3A2A20`), keine Brille, Haut `#F2D3B8`; Mimiken `Calm`, `Smile` (redet), `Smile Big\|Smile`, `Serious`, `Suspicious` | `ela_froh` (Frau, jung) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Der Spaziergänger und die Eigentümerin kommen **nur im Text** der Sachverhaltskarte und der Tafeln vor, nicht als Figur und nicht als Icon-Gesicht (am Gehweg nur Handy und Mond als Diagramm-Icons).
- **Blickrichtung:** Beide Posen blicken mit diesen Köpfen im Original nach rechts (Kopfprobe am Kontaktbild `besetzung_123.png`, Ohr links/Gesicht rechts; ein erster Lauf mit „easing-1 blickt nach links“ ergab einen nach rechts blickenden Gunnar in den Tafelszenen und wurde korrigiert). Grundansicht gespiegelt = blickt nach links (Tafelszenen; Marlene in A1 zu Gunnar), `_r` = blickt nach rechts (Gunnar in A1 zum Tisch und zu Marlene).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `GU_redet`, `GU_redetfroh`, `MA_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots, keine Karikatur. „Awe“ verworfen (Augen wirken wie eine Brille).
- **Stimmen nur aus dem Pool** niklas, helmut, ela_froh, julia: `niklas` (Gunnar), `ela_froh` (Marlene). `julia` bewusst nicht besetzt (109, 112, 114), `helmut` ohne Rolle (keine ältere Figur).
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keiner Datei unter `youtube/` (Suche `grep -rlw`): Gunnar, Marlene („Anton“ verworfen: im Test `willenserklaerung-test` vergeben; „Birte“ verworfen: Verwechslungsgefahr mit „bitte“). Kein Genitiv eines Namens im Sprechtext.
- Präfixe `GU_`/`MA_` (nie `ER_`). Figuren-PNGs: `../peeps/op_123/` (50 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen** (Figurenrezepte 120–122 verglichen): 120 (`pointing_finger-1`, `crossed_arms-1`, `walking-2`, `blazer-4`), 121 (`polka_dots`, `shirt-3`, `walking-3`), 122 (`walking-1`, `resting-2`). 123: `easing-1`, `blazer-3` – nicht in 120–122; keine Kleidung in Grün-Hemd/Rot-Blazer-Kombination dort. Schauplatz neu: Lerntisch mit Lampe und Karteikarten-Turm (keine Bibliothek wie 051, kein Prüfungsraum wie 117). Leitmotiv Landkarte/Wortlaut: zwei Wortlautkarten, Vergleichstabelle § 242/§ 246, Mini-Gehweg. Cremegrund durchgehend (Tageslicht; der Mond nur als Diagramm-Icon „spät am Abend“).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Lerntisch** `fall`→`g1` | Bodenlinie, Schreibtisch mit Lampe; Gunnar links (blickt nach rechts), Turm wächst Karte für Karte; Marlene kommt rechts mit dem Blatt, legt es auf den Tisch | tabler:`desk` (Holz), `lamp` (Gelb), `file-text` (Weiß); Turm aus Karten (Palette) | `Fall · Gunnar lernt` → `… 80 Schemata auf Karteikarten` → `… Im Tutorium` → `… Keine Karte für den Fall` | ab 0,0 s Tisch, Lampe, 3 Karten, Gunnar müde mit Schild, Pille · Turm wächst · „80 Schemata“ · „alle auswendig“ · Marlene mit Blatt · Blatt fliegt auf den Tisch · Pille „Fall“ · Gunnar Sorge · Blase Gunnar | Blatt auf dem Tisch (`szene_123blatt_1`) |
| **A2 Hook** `hook`→`m1` | Tafel, Gunnar und Marlene rechts | tabler:`cards` | `Fall · Auswendig, und trotzdem gescheitert?` → `… Vom Schema zurück zum Gesetz` → `… Drei Werkzeuge` | 80 Schemata · Kreuz „gescheitert“ · Fleiß · Weg · Schema → Gesetz · Blase Marlene · „3 Werkzeuge“ | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C1 Werkzeug 1** `w1`→`rws` | Tafel mit **Wortlautkarte § 242 Abs. 1**, vier Marker, Schema-Pillen (grün = aus § 242, blau = Allgemeiner Teil) | tabler:`map-2`, `book` | `Werkzeug 1 · Das Schema als Landkarte` → `… Wortlaut § 242 Abs. 1 StGB` → `… I. 1. objektiver Tatbestand` → `… I. 2. subjektiver Tatbestand` → `… aus dem Allgemeinen Teil` | ≈ 15 | – |
| **C2 Werkzeug 1 am Fall** `fall1`→`kein` | Tafel, Mini-Gehweg (Handy, Mond), Ergebnisblock | tabler:`device-mobile`, `road`, `cards`, `moon` (Diagramm) | `Werkzeug 1 · am Fall: § 242 StGB` → `… b) Wegnahme` → `… Ergebnis: kein Diebstahl` | ≈ 9 | – |
| **D1 Werkzeug 2** `w2`→`w2b` | Tafel, Zeitstrahl Wegnahme → „behält er sie?“ | tabler:`help`, `device-mobile` | `Werkzeug 2 · Warum steht der Punkt hier?` → `… Warum ist die Zueignung subjektiv?` → `… Vollendet mit der Wegnahme` | ≈ 10 | – |
| **D2 drei Stufen** `w2c`→`w2f` | Treppe entstanden – untergegangen – durchsetzbar, Begründung, Verweis 103 | tabler:`stairs-up`, `hourglass`, `bulb` | `Werkzeug 2 · Zivilrecht: drei Stufen` → `… Warum diese Reihenfolge?` | ≈ 9 | – |
| **E1 Werkzeug 3** `w3`→`t4` | **Wortlautkarte § 246 Abs. 1**, Vergleichstabelle § 242/§ 246, Pfeil subjektiv → objektiv | tabler:`tools`, `book`, `arrows-exchange` | `Werkzeug 3 · Schema aus dem Wortlaut` → `… Wortlaut § 246 Abs. 1 StGB` → `… § 246 neben § 242` → `… Zueignung wird objektiv` | ≈ 13 | – |
| **E2 Werkzeug 3 am Fall** `t5`→`g2` | Tafel mit Haken je Merkmal, Ergebnisblock, Blase Gunnar | tabler:`scale`, `device-mobile`, `book` | `Werkzeug 3 · am Fall: § 246 StGB` → `… Zueignung` → `… rechtswidrig` → `… Vorsatz, Rechtswidrigkeit, Schuld` → `… keine schwerere Vorschrift` → `… Ergebnis: Unterschlagung` | ≈ 11 | – |
| **F Lernen** `m2`→`g3` | Blase Marlene, drei Schritte als Blöcke, Lernforschung mit Fundstelle, Blase Gunnar | tabler:`brain`, `list-check`, `calendar-repeat` (Diagramm), `notebook`, `book`, `school` | `Lernen · mit Fällen statt Listen` → `… 1.` → `… 2.` → `… 3.` → `… Was die Lernforschung sagt` | ≈ 9 | – |
| **G Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Kein Schema? Die Norm Wort für Wort lesen` | 5 | – |
| **H Klausurschema** `sch`→`s4` | breite Karte, § 246 Punkt für Punkt | – | `Klausurschema · § 246 StGB` → `… › I. Tatbestand` → `… › I. 1. objektiv` → `… › I. 2. subjektiv` → `… › II. Rechtswidrigkeit` → `… › III. Schuld` → `… › Subsidiarität` | 10 | – |
| **I Merksatz** `merke`→`mm2` | Lexi erklärt (redet), zwei Marker | – | `Merksatz` | 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 13 Folien; innerhalb harte Schnitte und Pops; eine Bewegung (Blatt von Marlenes Hand auf den Tisch, 0,5 s ab „legt“).
**Geräusche:** ein Handlungsgeräusch (Blatt landet auf dem Tisch), Freesound CC0 (ID 272496) über die API ohne Schlüssel, eigener Name `sfx3/szene_123blatt_1.wav`, Herkunft in `geraeusche_herkunft.json`. Turm, Karten, Haken und Schiebeblenden stumm.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 242 Abs. 1 und § 246 Abs. 1 StGB vollständig und wörtlich mit Normangabe; gesprochen ohne Strafrahmen („… wird bestraft“), Marker synchron zum Wort.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Spät am Abend findet ein Spaziergänger auf dem leeren Gehweg ein Handy. Die Eigentümerin hat es kurz vorher verloren, ist längst fort und weiß nicht, wo es liegt.
>
> Der Spaziergänger steckt das Handy ein, um es zu behalten. Zu Hause legt er seine eigene SIM-Karte ein und benutzt das Handy seitdem als seines.
>
> **Hat sich der Spaziergänger strafbar gemacht?**
