# Folge 137 · Urkunde § 267 StGB: Was ist eine Urkunde? Die 3 Funktionen – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_137.py`](src/skript_137.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · StGB BT, Themenplan-Format „Schema“ (Thumbnail-Vorlage „Lern · DEFINITION“). Beispielfall nach dem Plan-Hook („Eine Schülerin fälscht die Unterschrift ihrer Mutter unter einer Entschuldigung für die Schule“): Femke (16) schwänzt am Montag, schreibt abends „Femke war am Montag krank. Bitte entschuldigen Sie ihr Fehlen.“, setzt den Namen der Mutter darunter und ahmt deren Unterschrift nach; die Mutter weiß nichts; am Dienstag nimmt die Klassenlehrerin Frau Melzer den Zettel entgegen und heftet ihn ab. Ablauf: Fall → Frage → Sachverhalt → Wortlautkarte § 267 Abs. 1 und Urkundenbegriff → 1. Perpetuierungs-, 2. Beweis- (Absichts-/Zufallsurkunde, Abgrenzung Fotokopie), 3. Garantiefunktion (Beweiszeichen) → Tathandlung: unechte Urkunde (Geistigkeitstheorie) → schriftliche Lüge (Klausurpunkt) → Verfälschen (Vergleich) und Gebrauchen → subjektiver Tatbestand → Gegenvariante (Erlaubnis der Mutter) → Rechtswidrigkeit, Schuld (§ 19), Ergebnis, eine Tat → Klausurtipp → Prüfschema → Merksatz. Vorlagen 065/051 (Strafrechts-Schema), 134 (Hilfsfunktionen), 062 (Jugendliche, nur Verweis).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Femke (FE), 16 | Schülerin | `standing/easing-2` (offenes grünes Hemd `#8FD694` über schwarzem Shirt, Hose Blau `#8DB3F2`, Sneaker), Kopf `Buns` (zwei Dutts), Haar `#3B2A20`, Haut `#F0C29E`; **90 % der Erwachsenenhöhe** (Jugendliche, FOLGE-ABLAUF Abschnitt 3); Mimiken `Calm` (auch redet), `Smile`, `Suspicious`, `Serious`, `Concerned|Serious`, `Driven`, `Solemn` | `lucy` (Frau, jung; wie Marie, 17, in Folge 062) |
| Frau Melzer (ME), um 58 | Klassenlehrerin | `standing/shirt-3` (lila Bluse `#B8A9F5`, schwarze Hose), Kopf `Gray Medium`, Haar `#B9B9C2`, Brille `Glasses 4`, Haut `#EDC3A3`; Mimiken `Calm`, `Smile` (redet), `Serious`, `Suspicious` | `hilde` (Frau, älter) |
| Mutter (MU), um 45 | weiß nichts; in der Gegenvariante erlaubt sie | `standing/resting-2` (schwarzes Oberteil, Hose Rot `#F07A6A`), Kopf `Medium 2`, Haar `#3B2A20`, Haut `#F0C29E`; Mimiken `Calm`, `Smile`, `Suspicious`, `Serious`; **spricht nicht** (geschlossener Mund) | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle drei Posen blicken im Original nach rechts (Kontaktbild geprüft): Grundansicht gespiegelt (blickt nach links, zur Tafel), `_r` blickt nach rechts (Fallszene: Femke zum Zettel bzw. zu Frau Melzer).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `FE_redet`, `ME_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur: Femke als gewöhnliche Jugendliche in Alltagskleidung, keine „freche“ Täterinnenfigur; Frau Melzer sachlich-freundlich. 54 Figuren-PNGs in `../peeps/op_137/` (Drive-Master).
- **Namen** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste und per `grep -rlw` in keiner Text-/Codedatei unter `youtube/` (*.py, *.md, *.json, *.csv, *.txt: 0 Treffer): **Femke**, **Melzer**. „Merle“ verworfen (in Folge 104 wegen englischer Lesart abgelehnt, in 107/117 vorhanden), „Doris“ verworfen (Folge 133). Der Name der Mutter steht nur als Unterschrift „S. Ohlsen“ auf dem Zettel (wird nicht gesprochen, 0 Treffer). Nie im Genitiv mit -s.
- **Stimmen** nur aus dem Pool: lucy (Femke), hilde (Frau Melzer); stephan und christian nicht eingesetzt.

**Abweichung von den letzten Folgen** (Posenliste 134–136 geprüft): 134 Nachbarschafts-Chatgruppe, 135 EU-Kommission/Gericht, 136 brennender Mülleimer (GoA). Hier neu: Kinderzimmer mit Schreibtisch und Zettel (Abend), Nebenzimmer der Mutter, Klassenzimmer mit Tafel „Dienstag · Klasse 10“, Pult und Ordner. Posen `easing-2`, `shirt-3`, `resting-2` in 134–136 nicht verwendet (dort `shirt-4`, `blazer-4`, `crossed_arms-2`, `blazer-3`, `robot_dance-2`, `pointing_finger-1`); kein Polka-Dots-Muster.
**Tageslicht:** durchgehend Cremegrund („abends“ nur als Zeitangabe mit Mond-Icon, kein Nachtbild).

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Zu Hause** `fall`→`mutter` | Femke (ab 0,0 s mit Namensschild), Pille „Montag“, „16 Jahre“; Schule mit Pille „Femke fehlt“; „Montag, abends“, Schreibtisch, Stift, Zettel zeilenweise zum Wort, Unterschrift „S. Ohlsen“, Pille „Name und Unterschrift der Mutter, nachgeahmt“; Trennlinie, Mutter im Nebenzimmer, „weiß davon nichts“ | fluent:`school`, `crescent-moon`, `pencil`; tabler:`desk`, `signature` | `Fall · Montag: geschwänzt` (ab 0,0 s) → `… Die Entschuldigung` → `… Die Unterschrift` → `… Die Mutter weiß nichts` | Stift schreibt (`szene_137stift_1`) |
| **A2 Klassenzimmer** `dienstag`→`frage2` | Tafel „Dienstag · Klasse 10“, Pult, Femke und Frau Melzer; Zettel wandert zum Pult; Blasen Femke/Frau Melzer; Ordner „abgeheftet“; Frage-Pillen | fluent:`page-facing-up`, `open-file-folder`; tabler:`desk` | `Fall · Dienstag in der Schule` → `… Die Abgabe` → `… Abgeheftet` → `… Die Frage` | Ordner beim Abheften (`szene_137ordner_1`) |
| **B Sachverhalt** `sv` | Karte vollständig | – | `Sachverhalt` | – |
| **C Wortlaut, Begriff** `p267`→`fgar` | Wortlautkarte § 267 Abs. 1 (4 Marker), „sagt das Gesetz nicht“, Definition mit Fundstelle, Funktionenleiste baut sich am Wort auf | fluent:`balance-scale`, `page-facing-up` | `§ 267 Abs. 1 StGB › Wortlaut` → `Urkundenbegriff › Definition` → `… › drei Funktionen` | – |
| **D Perpetuierung** `perp`→`perp3` | Leiste (Perpetuierung gelb), Definition, Kreuz Anruf, Haken Zettel, Zettel | fluent:`memo`, `telephone-receiver`, `page-facing-up` | `I. Tatbestand › 1. objektiv › a) Urkunde: Perpetuierungsfunktion (+)` | – |
| **E Beweis** `bew`→`kopie` | Leiste, Definition, zwei Haken, Absichts-/Zufallsurkunde, Kasten Fotokopie | fluent:`balance-scale`, `page-facing-up`, `memo`, `envelope`, `printer` | `… a) Urkunde: Beweisfunktion` → `… Absichts- und Zufallsurkunde` → `… Abgrenzung Fotokopie` | – |
| **F Garantie** `gar`→`urk` | Leiste, Definition, Haken Unterschrift, Kasten Beweiszeichen (FIN), Ergebnisblock | fluent:`magnifying-glass-tilted-left`, `automobile`; tabler:`signature`, `circle-check` | `… a) Urkunde: Garantiefunktion` → `… Beweiszeichen` → `… a) Urkunde (+)` | – |
| **G Unechte Urkunde** `tat`→`sub2` | drei Tathandlungs-Pillen zum Wort, unecht, Geistigkeitstheorie, Kreuz/Haken, Ergebnis; Femke und Mutter | fluent:`page-facing-up`, `magnifying-glass-tilted-left`, `brain`, `pencil`; tabler:`circle-check` | `I. Tatbestand › 1. objektiv › b) Tathandlung` → `…: unecht = Täuschung über den Aussteller` → `…: Geistigkeitstheorie` → `…: Herstellen einer unechten Urkunde (+)` | – |
| **H Schriftliche Lüge** `luege`→`luege4` | hellgelbe Tafel, Kasten „Mutter schreibt selbst“, § 267 (−), Block „Echtheit … nicht Wahrheit“ | fluent:`thought-balloon`, `memo`, `magnifying-glass-tilted-left`; tabler:`x` | `Abgrenzung › …` → `Abgrenzung › schriftliche Lüge: § 267 (−)` | – |
| **I Verfälschen, Gebrauchen** `verf2`→`gebr4` | Definition, Mini-Zettel mit Pille „+ zweiter Fehltag“ (Vergleich), Gebrauchen, Zettel wandert zu Frau Melzer, Ergebnis | fluent:`pencil`, `page-facing-up`; tabler:`eye` | `… b) Tathandlung: Verfälschen (zum Vergleich)` → `…: Gebrauchen (+)` | – (Zettel stumm) |
| **J Subjektiv** `vors`→`rv3` | Vorsatz (zwei Haken), Täuschung im Rechtsverkehr („gängige Definition“), zwei Haken, Block | fluent:`brain`, `magnifying-glass-tilted-left`, `open-file-folder`; tabler:`circle-check` | `I. Tatbestand › 2. subjektiv › a) Vorsatz` → `… b) zur Täuschung im Rechtsverkehr` → `… (+)` | – |
| **K Gegenvariante** `var`→`var3` | hell-lila Tafel, Mutter mit Handy, Femke; zwei Haken, Zurechnung, eigenhändige Unterschrift (Testament), Block „echte Urkunde“ | fluent:`mobile-phone`, `telephone-receiver`, `brain`, `scroll` | `Gegenvariante › Mutter erlaubt vorher` → `… steht geistig dahinter` → `… echte Urkunde` | – |
| **L RW, Schuld, Ergebnis** `rw`→`konk` | Haken RW, Schuld (§ 19, JGG), Ergebnisblock, Konkurrenz mit Fundstelle | fluent:`balance-scale`; tabler:`circle-check`, `link` | `II. Rechtswidrigkeit` → `III. Schuld › 16 Jahre, § 19 StGB` → `Ergebnis · Femke strafbar, § 267 Abs. 1 StGB` → `Konkurrenzen · eine Tat` | – |
| **M Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | – |
| **N Prüfschema** `sch`→`k4` | breite Karte, progressiv (I. 1. a) b), 2. a) b), II., III., IV.) | – | `Prüfschema › …` | – |
| **O Merksatz** `merke`→`m3` | Lexi erklärt, Marker | – | `Merksatz` | – |

**Funktionenleiste:** Auf den Tafeln D–F steht oben „Perpetuierung · Beweis · Garantie“ (geprüfte Funktion grün, aktuelle gelb, folgende weiß); in C baut sie sich am gesprochenen Wort auf.
**Blasen:** Sprechblasen Stil C (Standard seit 02.10.2026), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Blasen, Tafeln und Pillen in Ziffern („16 Jahre“, „§ 267 Abs. 1 StGB“, „Klasse 10“, „§ 19 StGB“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegungen: Zettel wandert zum Pult (A2) und zu Frau Melzer (I).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_137stift_1` aus 849751, `szene_137ordner_1` aus 511639), Herkunft in `geraeusche_herkunft.json`.
**Wortlautkarte:** § 267 Abs. 1 vollständig, wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), Normangabe darunter, vollständig vorgelesen.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji Flat (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (**CC BY 4.0**, Namensnennung in `beschreibung.txt`). Kein Mensch als Icon.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Femke ist 16. Am Montag schwänzt sie die Schule. Am Abend schreibt sie auf einen Zettel: „Femke war am Montag krank. Bitte entschuldigen Sie ihr Fehlen.“ Darunter setzt sie den Namen ihrer Mutter und ahmt deren Unterschrift nach. Die Mutter weiß davon nichts.
>
> Am Dienstag gibt Femke den Zettel ihrer Klassenlehrerin, Frau Melzer. Frau Melzer behandelt das Fehlen als entschuldigt und heftet den Zettel ab.
>
> **Hat sich Femke wegen Urkundenfälschung (§ 267 StGB) strafbar gemacht?**
