# Folge 176 · Warenverkehrsfreiheit Schema: Art. 34 AEUV mit Dassonville – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_176.py`](src/skript_176.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Öffentliches Recht/Europarecht, Themenplan-Format „Schema“. Übungsfall nach dem Plan-Hook im Lager eines Getränkegroßhandels (Staaten bewusst unbenannt): Frau Trautmann kauft Whisky als Parallelimporteurin bei einem Großhändler im Nachbarland; eine Verordnung ihres Landes verlangt ein Echtheitszeugnis der Behörden des Herstellerlandes, das praktisch nur der Direktimporteur bekommt; Herr Kleinschmidt (Lebensmittelüberwachung) verbietet den Verkauf. Ablauf: Fall → Sachverhalt → Norm (Art. 34 AEUV, Wortlautkarte) mit Prüfschema in vier Schritten, **eigene Farbe je Punkt** (1 Schutzbereich Blau, 2 Adressat Grün, 3 Beschränkung Lila, 4 Rechtfertigung Gelb: farbiger Tafelbalken, Nummernpille, Pfadstand, Lösungs- und Schemazeilen) → 1. Schutzbereich (Ware nach Rs. 7/68, grenzüberschreitend) → 2. Adressat → 3. Beschränkung (mengenmäßig nach Geddo; der echte Fall Dassonville knapp; Formel Rn. 5 als Zitatkarte; Grenze Keck in einem Satz) → 4. Rechtfertigung (Art. 36 AEUV als Wortlautkarte; Cassis de Dijon in einem Satz; Verhältnismäßigkeit nach C-110/05; Dassonville Rn. 6, 7/9) → Lösung → zurück im Lager (Verstoß, unmittelbare Wirkung, Anwendungsvorrang mit Verweis auf Folge 127; Herr Kleinschmidt prüft die Rechnungen) → Klausurtipp (Art. 30 AEUV, Keck) → Klausurschema → Merksatz. Hauptfilm 6:06,9 (Begründung in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Trautmann (TR), um 40 | betreibt einen Getränkegroßhandel, Parallelimporteurin | `standing/blazer-1` (Blazer Koralle `#F07A6A`, schwarzes Shirt und Beinprothese aus der Pose, Hose Anthrazit `#3A3A44`, weiße Schuhe), Kopf `Medium 3`, Haut `#F2C9A4`, ohne Brille. Mimiken `Calm`, `Serious` (redet/ernst), `Smile`, `Suspicious`, `Concerned|Serious` (Sorge), `Awe`, `Driven` (entschlossen) | `laura_ruhig` (Frau, mittel) |
| Herr Kleinschmidt (KL), um 60 | Lebensmittelüberwachung | `standing/pointing_finger-2` (schwarzer Pullover aus der Pose, Hose Graublau `#5E6E8C`, schwarze Schuhe), Kopf `Gray Short`, Brille `Glasses 2`, Haut `#E3B08C`, ohne Bart. Mimiken `Calm`, `Serious` (redet/ernst), `Calm` (redet einsichtig), `Smile`, `Suspicious`, `Awe`, `Solemn` | `william` (Mann, älter) |
| Die Händler Dassonville, Herr Keck, Herr Mithouard | Beteiligte echter Fälle | **keine Figuren**, nur Fallnamen (Tafel, Sprechtext); keine Personen-Icons, keine Flaggen | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem Pool (william, sabrina, marc, laura_ruhig): eine Frau, ein älterer Mann. `sabrina` und `marc` liefen in Folge 172; Vorfolge 175: stephan, hilde – keine Überschneidung.
- **Namen** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste und vor Produktionsbeginn in keiner Text-/Codedatei unter `youtube/` (`grep -rlw` in *.py, *.md, *.json, *.csv, *.txt: je 0 Treffer): **Trautmann**, **Kleinschmidt**. Kein Genitiv eines Namens.
- **Blickrichtung:** Posen blicken im Original nach rechts (`_r`); gespiegelt (ohne Suffix) nach links. Lager: Frau Trautmann links blickt nach rechts, Herr Kleinschmidt rechts blickt nach links und zeigt auf das Regal. Tafeln: Figuren rechts blicken zur Tafel nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `TR_redet`, `KL_redet`, `KL_einsicht` (je beide Blickrichtungen) und Lexi. 58 Figuren-PNGs in `../peeps/op_176/` (nicht im Repository, im Drive-Master).
- **Verworfen:** `robot_dance-3` für Frau Trautmann (gleiche Armhaltung wie Lexi, Verwechslungsgefahr).

**Abweichung von den letzten Folgen:** 173 (resting-1, easing-2, shirt-3, blazer-4), 174 (crossed_arms-1, resting-2, shirt-4, crossed_arms-2), 175 (easing-1, pointing_finger-1) – 176 nutzt **blazer-1** und **pointing_finger-2**; keine Polka Dots, keine Bärte; die Prothesen-Pose trägt die Händlerin (keine Täterrolle). **Schauplatz neu:** Lager eines Getränkegroßhandels mit Regal (Grundformen), neutralen Flaschen (Tabler `bottle`, ohne Etikett und Marke) und Kartons (Tabler `package`); kein Glas, kein Trinken, keine Bar. Die Lösung kehrt bewusst ins Lager zurück, weil dort die Rechnungen geprüft werden.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A Fall** `fall`→`frage` | Lager; Frau Trautmann links ab 0,0 s mit Namensschild, Titelpille „Getränkegroßhandel“; Pillenband über dem Regal im Wechsel (Einkauf im Nachbarland → Parallelimporteurin → Verordnung/Echtheitszeugnis, Herstellerland, „bekommt praktisch nur, wer direkt beim Hersteller kauft“); Tür, Herr Kleinschmidt kommt; Blase Kleinschmidt; Blase Trautmann mit Beleg „Rechnungen“; Frage-Pillen | tabler: `bottle` (Bernstein), `package` (Karton), `truck-delivery` (Gelb), `route`, `certificate`, `door` (Holz), `receipt` | `Fall · Frau Trautmann und ihr Whisky` → `· Das Echtheitszeugnis` → `· Herr Kleinschmidt prüft das Lager` → `· Die Frage` | Tür (`szene_176tuer_1`, Freesound CC0 702171), Papier (`szene_176papier_1`, CC0 566189) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s | – | `Sachverhalt` | – |
| **C Norm** `norm`→`p4` | Wortlautkarte Art. 34 AEUV (vorgelesen, drei Marker); vier farbige Blöcke 1–4 zum gesprochenen Schritt; Frau Trautmann rechts | – | `Norm › Art. 34 AEUV` → `› Prüfschema in 4 Schritten` | – |
| **D 1. Schutzbereich** `s1`→`grenz` | blauer Balken; Zitatkarte Ware (Rs. 7/68) mit zwei Markern; Kunstwerke; Haken „Whisky: eine Ware“, „grenzüberschreitend“ | tabler: `coins`, `palette`, `bottle`, `world` | `1. Schutzbereich` → `› Ware` → `› grenzüberschreitender Bezug` | – |
| **E 2. Adressat** `s2`→`vo` | grüner Balken; Zeilen; Fallkasten mit Haken; Herr Kleinschmidt rechts | – | `2. Adressat` → `› im Fall: Verordnung des Landes` | – |
| **F 3. Beschränkung** `s3`→`schwer` | lila Balken; mengenmäßig (Geddo); Kasten „Der echte Fall: Dassonville, EuGH 1974“ mit Belgien/Scotch Whisky/britische Zollbehörden/Frankreich | tabler: `ban`, `file-certificate`, `truck-delivery`, `certificate-off` | `3. Beschränkung` → `› Maßnahme gleicher Wirkung?` → `› Dassonville, EuGH 1974` | – |
| **G Dassonville-Formel** `formel`, `weit` | Zitatkarte Rn. 5 mit fünf Markern; lila Block „Schon die Eignung zur Behinderung genügt“; Frau Trautmann rechts | – | `3. … › Dassonville-Formel` → `› Schon die Eignung genügt` | – |
| **H Keck** `keck`→`mgw2` | Zeilen Keck Rn. 16; Fallkasten mit zwei Kreuzen; lila Block „Also: Maßnahme gleicher Wirkung“; beide Figuren | – | `3. … › Grenze: Keck, EuGH 1993` → `› im Fall: Maßnahme gleicher Wirkung` | – |
| **I Art. 36** `s4`→`satz2` | gelber Balken; Wortlautkarte Art. 36 AEUV vollständig mit vier Markern; Herr Kleinschmidt rechts, Pillen im Wechsel | – | `4. Rechtfertigung` → `› Art. 36 AEUV` → `› Art. 36 Satz 2: keine Diskriminierung` | – |
| **J Cassis, Verhältnismäßigkeit** `cassis`, `vhm` | Zeilen Cassis Rn. 8; gelber Block „geeignet und nicht über das Erforderliche hinaus“ (C-110/05 Rn. 59) | tabler: `shield-check`, `scale` | `4. … › zwingende Erfordernisse: Cassis de Dijon` → `› Verhältnismäßigkeit` | – |
| **K Dassonville Rn. 6, 7/9** `dfal`→`direkt` | Zeilen, zwei Haken, roter Block „Formalitäten praktisch nur für Direktimporteure“; beide Figuren | – | `4. … › Dassonville: Nachweis für alle` | – |
| **L Lösung** `loes`→`mild` | Zeilen 1–4 mit farbigen Nummern, drei Haken, Kreuz „Parallelimporteure faktisch ausgeschlossen“, grüner Kasten „milder: Nachweise …“; beide Figuren | – | `Lösung · Frau Trautmann` → `· Rechtfertigung: unverhältnismäßig` | – |
| **M Zurück im Lager** `l6`→`k2` | Pillen „Verstoß gegen Art. 34 AEUV“, unmittelbare Berufung (Iannelli), Anwendungsvorrang (Verweis Costa/ENEL); Blase Kleinschmidt; der Beleg wandert zu ihm | wie A | `Lösung · Verstoß gegen Art. 34 AEUV` → `· Anwendungsvorrang` → `· Herr Kleinschmidt prüft die Rechnungen` | Papier (`szene_176papier_1`) |
| **N Klausurtipp** `tipp`, `tf` | hellgelbe Tafel, Lexi warnt; Art. 30 AEUV (Zölle), Keck nur bei Verkaufsmodalitäten | Warnsymbol (Streamline Freehand) | `Klausurtipp · Zölle und Abgaben: Art. 30 AEUV` → `· Keck nur bei Verkaufsmodalitäten` | – |
| **O Klausurschema** `sch`→`z4b` | breite Karte, I.–IV. mit farbigen römischen Pillen, sechs Untermerkmale und Fundstellen | – | `Klausurschema` → `› I. Schutzbereich` → … → `› IV. Rechtfertigung` | – |
| **P Merksatz** `merke`, `m2` | Lexi erklärt, zwei Sätze mit drei Markern | – | `Merksatz` | – |

**Blasen:** Stil C (`bausteine.blase`, Stil-C-Pflicht per Assertion), Schwanzspitze außerhalb der Blase am Mund; wortgleich mit dem Gesprochenen. **Zahlen** auf Tafeln und Pillen als Ziffern („Art. 34 AEUV“, „EuGH 1974“, „11.7.1974“, „Rn. 5“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; keine Bewegung.
**Geräusche:** zwei Handlungsgeräusche (Tür, Papier – zweimal), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT): bottle, package, truck-delivery, route, certificate, door, receipt, coins, palette, world, ban, file-certificate, certificate-off, shield-check, scale; Haken/Kreuz Fluent Emoji High Contrast (MIT); Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Regal und Boden aus Grundformen. Kein Mensch als Icon.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Frau Trautmann betreibt einen Getränkegroßhandel. Whisky kauft sie als Parallelimporteurin bei einem Großhändler im Nachbarland, wo die Flaschen rechtmäßig im Handel sind, nicht beim offiziellen Alleinimporteur.
>
> Eine Verordnung ihres Landes verlangt für importierten Whisky ein Echtheitszeugnis der Behörden des Herstellerlandes, eines anderen EU-Staats. Das bekommt praktisch nur, wer direkt beim Hersteller kauft.
>
> Herr Kleinschmidt von der Lebensmittelüberwachung verbietet den Verkauf ohne Zeugnis. Frau Trautmann legt ihre Rechnungen vor.
>
> **Verstößt die Pflicht zum Echtheitszeugnis gegen die Warenverkehrsfreiheit?**
