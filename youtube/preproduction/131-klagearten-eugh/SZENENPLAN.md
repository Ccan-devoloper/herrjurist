# Folge 131 · Klagearten EuGH: Vorlage, Nichtigkeitsklage, Vertragsverletzung – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_131.py`](src/skript_131.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Öffentliches Recht/Europarecht, Themenplan-Format „Schema“. Hook nach dem Plan („Ein deutsches Gericht zweifelt, ein Unternehmen klagt, die Kommission verklagt Deutschland“) als drei fiktive Mini-Fälle mit je einer Figur. Kern: Raster **Wer? Wogegen? Voraussetzungen? Folge?** für die drei Verfahren (Überblick leer → je Verfahren Wortlautkarte und Tafeln → Ergebnis je Mini-Fall → Klausurschema als gefülltes Raster). Ablauf: Fälle → Frage → Sachverhalt → Überblick → 1. Vorabentscheidung (Wortlaut Art. 267, Wer, CILFIT, Foto-Frost, Bindung, Art. 101 GG, Fall 1) → 2. Nichtigkeitsklage (Wogegen, Kläger, Wortlaut Abs. 4, Plaumann, Inuit, Frist, EuG, Folge, Fall 2) → 3. Vertragsverletzung (Wortlaut Art. 258, Wer, Vorverfahren, Art. 260 I/II, Fall 3) → Art. 265/340 → Ergebnis → Klausurtipp → Klausurschema → Merksatz. Hauptfilm 6:52,9 (Begründung in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Richterin Eichhorn (EI), um 58 | Richterin am Verwaltungsgericht, Auslegungszweifel | `standing/blazer-3` (Jacke und Hose Dunkelgrau `#3D3D48` wie eine Robe, schwarzes Oberteil), Kopf `Gray Medium` (Haar `#A7A7B2`), Brille `Glasses 4`, Haut `#F0CDB4`; Mimiken `Calm`, `Serious` (redet/ernst), `Suspicious`, `Smile`, `Awe` | `hilde` (Frau, älter) |
| Frau Pfister (PF), um 35 | Unternehmerin (Baustofffirma), Adressatin des Bußgeldbeschlusses | `standing/crossed_arms-1` (Oberteil Rot `#F07A6A`, schwarze Hose), Kopf `Medium Straight`, Haut `#E8B894`; Mimiken `Calm`, `Driven` (redet/entschlossen), `Concerned\|Serious` (Sorge), `Smile`, `Suspicious` | `lucy` (Frau, jung) |
| Herr Teichmann (TE), um 45 | Beamter der Europäischen Kommission | `standing/shirt-3` (Hemd Blau `#8DB3F2`, schwarze Hose), Kopf `Short 4`, Haut `#D9A07A`, ohne Bart und Brille; Mimiken `Calm`, `Serious` (redet/ernst), `Suspicious`, `Smile`, `Solemn` | `christian` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem Pool (stephan, hilde, christian, lucy); `stephan` nicht verwendet; jede Figur spricht in ihrer eigenen Szene allein (kein Dialog stephan/christian). Vorfolge 130: marc, william, sabrina – keine Überschneidung.
- **Namen** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste und in keiner Text-/Codedatei unter `youtube/` (`grep -rlw` in *.py, *.md, *.json, *.csv, *.txt, 0 Treffer): **Eichhorn**, **Pfister**, **Teichmann**. „Wenzel“ verworfen (in Folge 129 vergeben, nicht auf der Liste). Kein Genitiv eines Namens („das Unternehmen von Frau Pfister“ vermieden durch „ihr Unternehmen“; „Für Herrn Teichmann“).
- **Blickrichtung:** Posen blicken im Original nach rechts (`_r`); gespiegelt (ohne Suffix) nach links. Fallszenen A1/A2: Figur links blickt nach rechts zum Tisch; A3: Herr Teichmann rechts blickt nach links zum Gesetz; Tafeln: Figur rechts blickt zur Tafel nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `EI_redet`, `PF_redet`, `TE_redet` (je beide Blickrichtungen) und Lexi. 62 Figuren-PNGs in `../peeps/op_131/` (nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 127 (blazer-2, crossed_arms-2; Limonadenmanufaktur), 128 (easing-1, resting-2), 129 (pointing_finger-2, shirt-4), 130 (in Arbeit). 131: drei kurze neue Schauplätze (Richtertisch mit Waage, Büro der Baustofffirma mit Mauer und Lkw, Büro der Kommission mit EU-Tafel), Posen `blazer-3`, `crossed_arms-1`, `shirt-3` in 127–129 nicht verwendet, keine Polka Dots, keine Prothesen-Posen.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Verwaltungsgericht** `fall`–`ei1` | Bodenlinie, Tisch (Grundformen), Waage; Eichhorn links, Bescheid und EU-Verordnung auf dem Tisch, Fragezeichen, Sprechblase | tabler `scale` (Gelb), `file-text` (Weiß), `file-certificate` (Blau), `question-mark` | `Fall · Drei Fälle für Luxemburg` → `Fall 1 · Richterin Eichhorn am Verwaltungsgericht` → `… Ein Begriff der Verordnung ist unklar` | Grundbild · Eichhorn · Bescheid · Verordnung · Verwaltungsgericht · unklar · Blase | – |
| **A2 Baustofffirma** `pfist`–`pf1` | Tisch, Mauer, Lkw; Umschlag mit Beschluss, Münzen (Geldbuße), Blase | tabler `wall` (Rot), `truck` (Gelb), `mail` (Weiß), `coins` (Gelb) | `Fall 2 · Frau Pfister und ihre Baustofffirma` → `… Geldbuße per Beschluss der Kommission` | Grundbild · Firma · Umschlag · Beschluss · Geldbuße · Sorge · Blase | Umschlag gleitet (`szene_131brief_1`, Freesound CC0 444431) |
| **A3 Kommission** `teich`–`te1` | Blaue EU-Tafel mit Sternen (Grundform + Icon), Tisch mit Gesetzbuch, Werkzeug, Genehmigung; Teichmann rechts, Blase | tabler `stars` (Gelb), `book` (Rot), `tools`, `license` (Gelb) | `Fall 3 · Herr Teichmann von der Europäischen Kommission` → `… Zusatzgenehmigung für Handwerker` | Grundbild · Gesetz · Handwerker · Genehmigung · denkt · Blase | – |
| **A4 Frage** `frage`, `frage2` | alle drei nebeneinander, Pillen zum Wort; Gerichtsgebäude | fluent-hc `classical-building` | `Fall · Ein Gericht zweifelt, …` → `Fall · Welches Verfahren passt?` | 3 Pillen nacheinander, Frage | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s | – | `Sachverhalt` | 1 | – |
| **C Überblick** `ueber`–`raster` | breite Karte, drei Spaltenköpfe zum Wort, vier Zeilen zum Wort, Zellen leer | – | `Überblick · …` → `Überblick › Wer? Wogegen? Voraussetzungen? Folge?` | 8 Aufbaustufen | – |
| **D1 Art. 267** `wl267`–`abs3` | **Wortlautkarte** (auszugsweise; Marker „Auslegung der Verträge“, „Gültigkeit und die Auslegung der Handlungen der Organe“, „kann“, „verpflichtet“), Pillen Vorlagerecht/-pflicht; Eichhorn rechts | – | `1. Vorabentscheidung, Art. 267 AEUV` → `› Gegenstand …` → `› Vorlagerecht, Abs. 2` → `› Vorlagepflicht letzter Instanz, Abs. 3` | Karte, 4 Marker, 2 Pillen, Mimik | – |
| **D2 Wer? Ausnahmen** `wer1`–`foto` | Tafel; CILFIT-Kasten Punkt für Punkt; roter Block Foto-Frost | – | `… › Wer? Nur das Gericht legt vor` → `› Ausnahmen nach CILFIT` → `› Ungültigkeit: immer vorlegen` | Zeilen zum Wort | – |
| **D3 Folge, GG, Fall 1** `bind`–`l1b` | Haken Bindung, lila Block Art. 101 GG, Fall 1 mit Haken/Kreuz | – | `… › Folge: Bindung` → `› Art. 101 Abs. 1 S. 2 GG` → `Fall 1 · Richterin Eichhorn: Vorlagerecht` | Zeilen, Haken, Kreuz | – |
| **E1 Nichtigkeitsklage** `ni`–`nprv` | Tafel; drei Kläger-Kästen (grün, blau, gelb); Pfister rechts | – | `2. Nichtigkeitsklage, Art. 263 AEUV` → `› Wogegen? …` → `› Wer? Privilegierte …` → `› Teilprivilegierte …` → `› Nichtprivilegierte …` | Zeilen, Kästen | – |
| **E2 Art. 263 Abs. 4** `wl263`–`inuit` | **Wortlautkarte** (Marker „an sie gerichteten“, „unmittelbar und individuell“, „Rechtsakte mit Verordnungscharakter“, „keine Durchführungsmaßnahmen“), Plaumann-Zitat Zeile für Zeile, grüner Block Inuit | – | `… › Klageberechtigung Privater, Abs. 4` → `› individuell betroffen: Plaumann` → `› Rechtsakte mit Verordnungscharakter` | Karte, 4 Marker, Zitatzeilen, Block | – |
| **E3 Frist, EuG, Folge, Fall 2** `frist`–`l2b` | Haken zu Frist, Gericht, Folge; roter Kasten Fall 2 | – | `… › Frist: 2 Monate, Abs. 6` → `› zuständig: Gericht der EU, Art. 256` → `› Folge: Nichtigerklärung, Art. 264` → `Fall 2 · Frau Pfister: Nichtigkeitsklage` | Zeilen, Haken | – |
| **F1 Art. 258** `wl258`–`w258b` | **Wortlautkarte** (vollständig; Marker „Gelegenheit zur Äußerung“, „mit Gründen versehene Stellungnahme“, „Gerichtshof der Europäischen Union anrufen“), drei Stufen-Pillen; Teichmann rechts | – | `3. Vertragsverletzungsverfahren, Art. 258 AEUV` → `› begründete Stellungnahme` → `› Klage der Kommission` | Karte, 3 Marker, 3 Pillen | – |
| **F2 Wer, Vorverfahren, Folge** `wer3`–`zwang` | Tafel; zwei Stufenkästen mit Pfeil; Haken Feststellungsurteil; roter Block Art. 260 II | – | `… › Wer? Wogegen?` → `› Voraussetzung: Vorverfahren` → `› Folge: Feststellungsurteil, Art. 260 Abs. 1` → `› Art. 260 Abs. 2` | Zeilen, Kästen, Block | – |
| **F3 Fall 3, Art. 265/340** `l3`–`rest` | Stufen als Icons in der Tafel (Mahnschreiben, Stellungnahme, Gesetz, Klage), gelber Kasten „Daneben“ | tabler `mail`, `file-text` (Gelb), `book` (Rot), `building-bank` (Blau) | `Fall 3 · Herr Teichmann: Vertragsverletzungsverfahren` → `Weitere Verfahren · Art. 265 und 340 AEUV` | Icons, Zeilen | – |
| **G Ergebnis** `erg`–`e3` | alle drei wie A4, je Pille mit Verfahren und Artikel, Haken; Mimik froh | – | `Ergebnis · Drei Fälle, drei Verfahren` | 3 Stufen | – |
| **H Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Die Vorlage ist keine Klage` → `Klausurtipp · Nichtigkeitsklage Privater: Abs. 4` | Zeile für Zeile | – |
| **I Klausurschema** `sch`–`r4c` | dasselbe Raster wie C, Zeile für Zeile und Zelle für Zelle gefüllt | – | `Klausurschema` → `› 1. Wer?` … `› 4. Folge` | 17 Aufbaustufen | – |
| **J Merksatz** `merke`–`m2` | Lexi erklärt (redet), drei Zeilen mit Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Stil C (`bausteine.blase`), Schwanzspitze außerhalb der Blase am Mund; wortgleich mit dem Gesprochenen. **Zahlen** auf Tafeln und Pillen als Ziffern („Art. 267 AEUV“, „2 Monate“, „Art. 101 Abs. 1 S. 2 GG“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 19 Folien; innerhalb harte Schnitte und Pops; keine Bewegung.
**Geräusche:** ein Handlungsgeräusch (Umschlag), Freesound CC0, Herkunft in `geraeusche_herkunft.json`. Weitere bewusst weggelassen (keine sichtbare Handlung mit passendem Klang).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji High Contrast (MIT; Gebäude, Haken/Kreuz), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Tische und EU-Tafel aus Grundformen. Kein Mensch als Icon.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Richterin Eichhorn am Verwaltungsgericht entscheidet über einen Bescheid, der auf einer EU-Verordnung beruht. Ein Begriff der Verordnung ist unklar; sie will ihn vom Gerichtshof klären lassen. Gegen ihr Urteil gibt es noch ein Rechtsmittel.
>
> Frau Pfister führt eine Baustofffirma. Die Kommission verhängt gegen ihr Unternehmen per Beschluss eine Geldbuße wegen eines Kartellverstoßes. Frau Pfister will klagen.
>
> Herr Teichmann von der Europäischen Kommission prüft ein deutsches Gesetz: Handwerker aus anderen Mitgliedstaaten brauchen danach eine zusätzliche Genehmigung. Er hält das für einen Verstoß gegen die Dienstleistungsfreiheit.
>
> **Welches Verfahren vor dem Gerichtshof der EU passt jeweils?**
