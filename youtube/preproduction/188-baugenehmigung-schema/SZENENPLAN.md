# Folge 188 · Baugenehmigung Schema: Bauplanungs- und Bauordnungsrecht – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_188.py`](src/skript_188.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Baurecht, Format **Schema** mit Beispielfall nach dem Plan-Hook („Deine Garage erfüllt jeden Brandschutz – steht aber mitten im Außenbereich.“): Herr Hasenkamp will auf seiner Wiese weit draußen vor dem Dorf (ringsum Felder, kein Bebauungsplan, Flächennutzungsplan: Fläche für die Landwirtschaft) eine Betongarage mit 40 m² für zwei Oldtimer bauen; Frau Ortmann von der Bauaufsichtsbehörde lehnt ab.
Ablauf: Fall (Wiese → Behörde) → Sachverhalt → Anspruch (Wortlautkarten Art. 68 Abs. 1 S. 1 BayBO, § 74 Abs. 1 S. 1 BauO NRW 2018) → Länder-Overlay (Tabelle BY/NRW) → Kompetenz (Wortlautkarten Art. 74 Abs. 1 Nr. 18, Art. 70 Abs. 1 GG) → I. Genehmigungsbedürftigkeit (Wortlautkarten Art. 55 Abs. 1 BayBO, § 60 Abs. 1 BauO NRW 2018; Ausnahmen) → II. Bauantrag → III. 1. Verfahren und Prüfprogramm (Brandschutz) → III. 2. Bauplanungsrecht (Wortlautkarte § 29 Abs. 1 BauGB, Weiche §§ 30, 34, 35) → § 35 nur Ergebnis (Verweis Folge 085) → III. 3. Bauordnungsrecht und Ergebnis → zurück auf der Wiese (Blase Hasenkamp) → Prüfschema → Klausurtipp (Lexi, Verpflichtungsklage, Verweis Folge 081) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:38 bei 5.689 gesprochenen Zeichen (Grenze 7:00/6.200); Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Hasenkamp (HA), um 55 | Bauherr, Oldtimer-Besitzer | `standing/pointing_finger-2` (schwarzer Pullover, Hose Beige `#C9A66B`), Kopf `Short 3`, Haut `#E8B48E`, kein Bart, keine Brille; Mimiken `Calm`, `Smile`, `Smile Big\|Smile`, `Concerned\|Serious`, `Serious`, `Tired`, `Suspicious`; redet: `Smile Big\|Smile` (zuversichtlich), redet2: `Tired` (Einsicht) | `christian` (Mann, mittel) |
| Frau Ortmann (OR), um 35 | Sachbearbeiterin der Bauaufsichtsbehörde | `standing/crossed_arms-1` (Oberteil Rosé `#F2A7C3`, schwarze Hose), Kopf `Medium Bangs`, Haut `#F3CDB0`; `Calm`, `Serious`, `Smile`, `Suspicious`, `Solemn`; redet: `Serious` | `lucy` (Frau, jung) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keiner Text-/Code-Datei unter `youtube/` (Volltextsuche 04.10.2026: Hasenkamp 0, Ortmann 0). Nie im Genitiv.
- **Stimmen nur aus dem Pool:** `christian` und `lucy`; `stephan` und `hilde` nicht verwendet (keine Stephan/Christian-Paarung). Vorfolge 186 nutzte `hilde`, `stephan`, `lucy` (Hölscher, zwei kurze Sätze) – `lucy` ließ sich im Pool nicht vermeiden, da `hilde` (älter) nicht zur Rolle passt und `stephan` nicht mit `christian` in eine Szene darf.
- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Wiese: Herr Hasenkamp blickt (und zeigt) nach links zur geplanten Garage; Behörde: Frau Ortmann (`_r`) und Herr Hasenkamp einander zugewandt; Tafelfolien: alle blicken nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `HA_redet`, `HA_redet2`, `OR_redet` (je links/rechts) und Lexi.
- Figuren-PNGs: `../peeps/op_188/` (56 Dateien, nicht im Repository, im Drive-Master). Kontaktbild `out/besetzung_188.png`.
- Frau Ortmann sachlich, keine „böse Behörde“; Herr Hasenkamp kein „Schwarzbauer“: er stellt ordentlich einen Antrag und nimmt das Ergebnis am Ende einsichtig hin.

**Abweichung von den letzten Folgen:** 184 (`sitting/mid-2`, `blazer-1`), 185 (`resting-2`, `closed_legs-2`, `walking-1`, `walking-2`, `crossed_arms-2`, `shirt-4`), 186 (`easing-2`, `doctor-nurse-01`, `resting-1`, `blazer-3`). 188: `pointing_finger-2` und `crossed_arms-1` in keiner der drei Vorfolgen; Farben Schwarz/Beige und Rosé (Orange/Türkis/Anthrazit aus 186, Grün/Lila/Blau aus 185 vermieden); keine Polka Dots, keine Prothesen-Posen, keine Bärte. Schauplätze neu: Feldflur mit Dorf am Horizont und gestrichelter Garagenkontur, Bauaufsichtsbehörde mit Pinnwand (Plan, Traktor), Tabelle als neues Tafelelement. Die Wiese kehrt am Ende zurück, weil die Geschichte dorthin zurückkehrt. Gegenüber 085 (Wald, Wochenendhaus) und 113 (Wohngebiet, Nachbarklage) andere Orte und Requisiten.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Wiese** `fall`→`ha1` | Feldflur, Dorf am Horizont, Herr Hasenkamp ab 0,0 s mit Namensschild | fluent-hc:`houses`, `deciduous-tree`; tabler:`building-church`, `sun`, `car` ×2 (Rot/Blau), `file-text`; `landschaft()`, `garage()` (gestrichelt = geplant) | `Fall · Die Wiese vor dem Dorf` → `· Die geplante Garage` → `· Der Bauantrag` → `· Herr Hasenkamp ist zuversichtlich` | Grundbild · „ringsum nur Felder“ · Garagenkontur · 2 Oldtimer · „40 m² · Beton“ · Bauantrag · Blase · ✓ Brandschutz · ✓ Abstände | – |
| **A2 Behörde** `amt`→`frage2` | Schreibtisch, Fenster, Pinnwand; Frau Ortmann und Herr Hasenkamp | tabler:`file-text`, `map`; fluent-hc:`tractor`; `stempel()` | `Fall · Bei der Bauaufsichtsbehörde` → `· kein Bebauungsplan` → `· Flächennutzungsplan: Landwirtschaft` → `· Die Ablehnung` → `· Anspruch auf die Baugenehmigung?` → `· zwei Ebenen` | Antrag · ✗ kein B-Plan · FNP + Plan · Traktor · Blase Ortmann · Stempel „ABGELEHNT“ · Frage · Ebene 1 · Ebene 2 | Stempel (`szene_188stempel_1`) |
| **B Sachverhalt** `sv` | Karte vollständig (≈ 9,8 s) | – | `Sachverhalt` | 1 | – |
| **C Anspruch** `anspr`→`anspr2` | 2 Wortlautkarten, Herr Hasenkamp | tabler:`file-certificate`, `map-pin`, `scale`, `circle-check` | `Anspruch · Landesbauordnung (Beispiele: Bayern, NRW)` → `› Art. 68 Abs. 1 S. 1 BayBO` → `› § 74 Abs. 1 S. 1 BauO NRW 2018` → `› gebundene Entscheidung` → `› wenn nichts entgegensteht` | Tafel · Karte BY · 3 Marker · Karte NRW · Marker · gebunden · ✓ | – |
| **D Länder-Overlay** `tab`→`eigen` | Tabelle BY/NRW, Frau Ortmann | tabler:`table`, `map-2` | `Länder-Overlay · gleiche Struktur, andere Nummern` → `› Genehmigungspflicht` → `› vereinfachtes Verfahren` → `› Anspruch` → `› andere Länder: eigene LBO prüfen` | Kopf · 3 Zeilen · Hinweis | – |
| **E Kompetenz** `komp`→`ordn` | 2 Wortlautkarten (GG), beide Figuren | tabler:`scale`, `building-bank`, `map-2` | `Kompetenz · Warum zwei Ebenen?` → `› Bund: Bodenrecht, Art. 74 Abs. 1 Nr. 18 GG` → `› Bauplanungsrecht: BauGB` → `› Länder: Art. 70 Abs. 1 GG` → `› Bauordnungsrecht: Landesbauordnungen` | Karte · 2 Marker · Block Bund · Karte · Marker · Block Länder | – |
| **F1 I. Genehmigungsbedürftigkeit** `gb`→`nrw60` | 2 Wortlautkarten, Herr Hasenkamp | tabler:`file-text`, `map-pin` | `I. Genehmigungsbedürftigkeit · …` → `› Art. 55 Abs. 1 BayBO` → `› § 60 Abs. 1 BauO NRW 2018` | Karte · 4 Marker · Karte NRW · Marker | – |
| **F2 Ausnahmen, II. Bauantrag** `frei`→`ba` | Tafel, Herr Hasenkamp | tabler:`car-garage`, `map`, `file-certificate`, `file-text`; fluent-hc:`sheaf-of-rice` | `I. › verfahrensfrei? Garagen bis 50 m²` → `› nicht im Außenbereich` → `› Freistellung? kein Bebauungsplan` → `› genehmigungspflichtig (+)` → `II. Bauantrag › ordnungsgemäß (unterstellt)` | 6 | – |
| **G III. 1. Verfahren** `gf`→`trotz` | Tafel, beide Figuren | tabler:`list-check`, `file-text`; fluent-hc:`fire-extinguisher` | `III. Genehmigungsfähigkeit` → `III. 1. Verfahrensart · …` → … → `› Brandschutz: trotzdem einzuhalten` | 11 | – |
| **H III. 2. Bauplanungsrecht** `bpl`→`w35` | Wortlautkarte § 29, Weiche | tabler:`map`, `car-garage`; fluent-hc:`houses`, `sheaf-of-rice` | `III. 2. Bauplanungsrecht · das Herzstück` → `› § 29 Abs. 1 BauGB: Vorhaben` → … → `› Außenbereich, § 35 BauGB` | Karte · 3 Marker · ✓ Vorhaben · Weiche · ✗ § 30 · ✗ § 34 · § 35 | – |
| **I § 35** `l35`→`unzul` | Tafel, nur Ergebnis | fluent-hc:`tractor`, `deciduous-tree`; tabler:`car-garage`, `ban` | `III. 2. › § 35 BauGB: …` → `III. 2. Bauplanungsrecht › unzulässig (−)` | 6 | – |
| **J1 III. 3. Bauordnungsrecht, Ergebnis** `bo`→`erg` | Tafel, beide Figuren | tabler:`ruler-measure`, `ban`, `file-x` | `III. 3. Bauordnungsrecht` → … → `Ergebnis › kein Anspruch, Ablehnung rechtmäßig` | 6 | – |
| **J2 Wiese** `ha2` | Rückkehr auf die Wiese, gestrichelte Garagenkontur mit Ähre, Blase Hasenkamp | wie A1 | `Ergebnis · Herr Hasenkamp auf seiner Wiese` | 1 | – |
| **K Prüfschema** `sch`→`s4` | breite Karte, Punkt für Punkt | – | `Prüfschema › …` | 10 Stufen | – |
| **L Klausurtipp** `tipp`→`k3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol | `Klausurtipp · zuerst die Verfahrensart` → … | 5 | – |
| **M Merksatz** `merke`→`m4` | Lexi erklärt (redet), 4 Marker | – | `Merksatz` | 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; keine Figurenbewegung, kein Zoom.
**Geräusch:** ein Handlungsgeräusch (Stempel auf dem Bauantrag), Freesound CC0, Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json). Ein Papiergeräusch für den Bauantrag wurde verworfen (Freesound-Kandidaten 429298, 444709 zu leise/verrauscht).
**Blasen:** Stil C, wortgleich mit dem Gesprochenen. Wortlautkarten wörtlich nach den amtlichen Quellen (Abruf 04.10.2026), Auslassungen mit „…“.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Herr Hasenkamp besitzt eine Wiese weit draußen vor dem Dorf; ringsum liegen nur Felder. Dort will er eine Garage aus Beton mit 40 m² für seine zwei Oldtimer bauen. Sie hält die Abstandsflächen ein und erfüllt die Anforderungen an den Brandschutz. Er stellt einen ordnungsgemäßen Bauantrag.
> Für die Wiese gilt kein Bebauungsplan. Der Flächennutzungsplan der Gemeinde stellt sie als Fläche für die Landwirtschaft dar. Herr Hasenkamp betreibt keine Landwirtschaft.
> Frau Ortmann von der Bauaufsichtsbehörde lehnt den Bauantrag ab: Die Garage stehe im Außenbereich.
> **Frage:** Hat Herr Hasenkamp einen Anspruch auf die Baugenehmigung? (kein Fiktiv-Hinweis)
