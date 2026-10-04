# Folge 164 · Richtlinie unmittelbare Wirkung: Nicht umgesetzt – und jetzt? – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_164.py`](src/skript_164.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Öffentliches Recht/Europarecht, Themenplan-Format „Schema“. Fall nach dem Plan-Hook in der Fahrzeughalle einer Feuerwache: Herr Ruppert (Berufsfeuerwehr der Stadt) verlangt die 48-Stunden-Grenze aus Art. 6 Buchst. b RL 2003/88/EG gegen eine Landesverordnung mit 54 Wochenstunden; Herr Goldbach (Personalamt) hält dagegen. **Annahme deutlich gekennzeichnet** (Sprechtext, Pille, Sachverhaltskarte): Deutschland hätte nicht rechtzeitig umgesetzt; in Wirklichkeit ist die Richtlinie umgesetzt. Ablauf: Fall → Sachverhalt → Normen (Art. 288 Abs. 3 AEUV, Art. 4 Abs. 3 UAbs. 2 EUV; ein Satz Verweis Folge 138) → Prüfschema in vier Schritten (1. Frist – Ratti, 2. keine/unzureichende Umsetzung, 3. unbedingt und hinreichend genau – Art. 6 Buchst. b, 4. gegenüber dem Staat – Marshall, Foster, Farrell, Stadt) → Private (ein Satz, Verweis 138) und richtlinienkonforme Auslegung (ein Satz) → Lösung mit Rechtsfolge (Anwendungsvorrang, Verweis 127) → echter Fall Fuß zurück in der Halle → Klausurtipp → Klausurschema → Merksatz. Hauptfilm 6:28,8 (Begründung in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Ruppert (RU), um 35 | Feuerwehrmann der Berufsfeuerwehr seiner Stadt | `standing/shirt-3` (Diensthemd Dunkelblau `#4F6FA8`, schwarze Hose aus der Pose, weiße Schuhe), Kopf `Short 4`, Haut `#E9B996`, ohne Brille und Bart. Mimiken `Calm` (ruhig), `Serious` (redet/ernst), `Smile`, `Suspicious`, `Concerned|Serious` (Sorge), `Awe`, `Driven` (entschlossen) | `niklas` (Mann, jung) |
| Herr Goldbach (GO), um 60 | leitet das Personalamt der Stadt | `standing/blazer-4` (Sakko Grau `#A9A9A9`, weißes Hemd, schwarze Hose aus der Pose), Kopf `No Hair 1`, Brille `Glasses`, Haut `#D8A580`, ohne Bart. Mimiken `Calm`, `Serious` (redet), `Calm` (redet einsichtig), `Smile`, `Suspicious`, `Awe`, `Solemn` | `helmut` (Mann, älter) |
| Herr Ratti, Frau Foster, Frau Farrell, Herr Fuß, Frau Faccini Dori | Beteiligte echter Fälle | **keine Figuren**, nur Fallnamen (Tafel, Sprechtext); keine Personen-Icons | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem Pool (niklas, helmut, ela_froh, julia): zwei Männerrollen, deshalb `ela_froh` (nicht für ernste Rollen) und `julia` (möglichst vermeiden) nicht verwendet. Folge 138 (Voraussetzungsfolge): william, sabrina; 161: sabrina, marc – keine Überschneidung.
- **Namen** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste und vor Produktionsbeginn in keiner Text-/Codedatei unter `youtube/` (`grep -rlw` in *.py, *.md, *.json, *.csv, *.txt: 0 Treffer): **Ruppert**, **Goldbach** („Seiler“ verworfen: 15 Treffer). Kein Genitiv eines Namens.
- **Blickrichtung:** Posen blicken im Original nach rechts (`_r`); gespiegelt (ohne Suffix) nach links. Halle: Herr Ruppert links blickt nach rechts, Herr Goldbach rechts nach links. Tafeln: Figuren rechts blicken zur Tafel nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `RU_redet`, `GO_redet`, `GO_einsicht` (je beide Blickrichtungen) und Lexi. 58 Figuren-PNGs in `../peeps/op_164/` (nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 159 (robot_dance-3, crossed_arms-1), 160 (crossed_arms-1, resting-1), 161 (blazer-3, resting-1, crossed_arms-1, crossed_arms-2) – 164 nutzt **shirt-3** und **blazer-4**; Oberteilfarben der Vorfolgen (Koralle, Grün, Lila, Orange, Gelb) vermieden; keine Polka Dots, keine Prothesen-Posen, keine Bärte. **Schauplatz neu:** Fahrzeughalle einer Feuerwache mit hochgerolltem Tor (Grundformen), Löschfahrzeug (Tabler `firetruck`, ohne Beschriftung, kein Wappen), Helm am Haken, Dienstplan an der Wand. Die letzte Fallszene kehrt bewusst in die Halle zurück, weil dort der Dienstplan geändert wird.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Fall** `fall`→`frage` | Halle; Herr Ruppert links ab 0,0 s mit Namensschild; Pillen „Landesverordnung: im Schnitt 54 Wochenstunden“, „EU-Arbeitszeitrichtlinie 2003/88/EG“, „Dienstplan: 54 Std.“; Blase Ruppert; Tür, Herr Goldbach kommt; Blase Goldbach; Annahme-, Wirklichkeits- und Frage-Pille | tabler: `firetruck` (Rot), `helmet` (Gelb), `clipboard-list` (Weiß), `door` (Holz) | `Fall · Herr Ruppert und seine Wochenstunden` → `· Herr Goldbach vom Personalamt` → `· Annahme: nicht rechtzeitig umgesetzt` → `· Die Frage` | 12 | Tür (`szene_164tuer_1`, Freesound CC0 457354) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,6 s, Annahme im Text | – | `Sachverhalt` | 1 | – |
| **C Normen I** `norm`→`gold2` | Wortlautkarte Art. 288 Abs. 3 AEUV mit drei Markern; Zeilen „verbindlich: nur das Ziel“, „Form und Mittel“; Block „Adressat ist der Mitgliedstaat“; Herr Goldbach rechts, Pille „Insoweit hat er recht“ | – | `Normen › Art. 288 Abs. 3 AEUV` → `› … Adressat ist der Mitgliedstaat` | 6 | – |
| **D Normen II** `a4`→`vert` | Wortlautkarte Art. 4 Abs. 3 UAbs. 2 EUV (vorgelesen) mit zwei Markern; Block „Pflicht“; Block „4 Schritte“; rechts Pillen und Requisiten im Wechsel | tabler: `file-certificate` (Blau), `checkbox` (Grün), `books` (Gelb), `list-check` | `Normen › Art. 4 Abs. 3 EUV: Pflicht zur Umsetzung` → `› Pflicht verletzt? Vertikale unmittelbare Wirkung` | 6 | – |
| **E 1. Frist (Ratti)** `s1`→`frist` | Ratti-Kasten, Lösemittel ✓ / Lacke ✗, Zitat „erst am Ende des festgesetzten Zeitraums“, Block „Im Fall: Frist längst abgelaufen“ (23.11.1996) | tabler: `calendar-due`, `flask` (Hellblau), `brush` (Gelb), `calendar-check` (Grün) | `1. Umsetzungsfrist abgelaufen` → `› Ratti, EuGH 1979` → `› Wirkung erst am Ende der Frist` → `› im Fall: längst abgelaufen` | 10 | – |
| **F 2. nicht umgesetzt** `s2`, `s2f` | Zeilen, Fallkasten mit zwei Haken; Herr Ruppert rechts, Pille „Annahme“ | – | `2. Nicht oder nicht ordnungsgemäß umgesetzt` → `› im Fall: Annahme, keine Umsetzung` | 6 | – |
| **G 3. unbedingt und genau** `s3`→`gen` | Wortlautkarte Art. 6 Buchst. b mit zwei Markern, Haken „festes Ergebnis“, Zeile Art. 22, grüner Block mit Zitat Rn. 58 | tabler: `clock-hour-8` (Hellblau) | `3. Unbedingt und hinreichend genau` → `› Art. 6 Buchst. b RL 2003/88/EG` → `› Abweichungen nach Art. 22` | 7 | – |
| **H 4. gegenüber dem Staat** `s4`→`nutz` | Haken „Hoheitsträger“, „Arbeitgeber“, Block „kein Nutzen aus dem eigenen Versäumnis“; Herr Ruppert („Einzelner“) und Herr Goldbach („Staat“ → „Arbeitgeber“), Pille „vertikal“ | – | `4. Gegenüber dem Staat (vertikal)` → `› als Hoheitsträger oder Arbeitgeber` | 8 | – |
| **I Foster** `staat`→`formel` | Foster-Kasten, Zitatkarte Rn. 20 mit fünf Markern; rechts Gasflamme, Pillen „Frauen: 60“, „Männer: 65“, „durch Gesetz errichtet“, „Monopol Gasversorgung“ | tabler: `flame` (Blau) | `4. … › funktionaler Staatsbegriff` → `› Foster, EuGH 1990` | 13 | – |
| **J Farrell, Stadt** `farrell`, `stadt` | Zeilen Farrell, grüner Block „Gebietskörperschaften … gehören selbst zum Staat“; Herr Goldbach rechts | – | `4. … › Farrell, EuGH 2017` → `› die Stadt: Gebietskörperschaft` | 7 | – |
| **K Private** `priv`, `rka` | Kreuz „keine unmittelbare Wirkung zwischen Privaten“ (Verweis 138), Block „richtlinienkonform auslegen“ | tabler: `building-store` (Hell) | `4. … › nicht gegenüber Privaten` → `› bei Privaten: richtlinienkonforme Auslegung` | 4 | – |
| **L Lösung** `loes1`→`vorr` | vier Haken, grüner Block, Kreuz „nicht richtlinienkonform auslegbar“, Zeile „unangewendet“, Block Anwendungsvorrang (Verweis 127); beide Figuren rechts | – | `Lösung · Herr Ruppert gegen die Stadt` → `· Rechtsfolge: Anwendungsvorrang` | 9 | – |
| **M Fuß, Dienstplan** `fuss`, `g2` | zurück in der Halle: Pillen zum echten Fall Fuß (C-243/09, Rn. 60); Blase Goldbach; Dienstplan wechselt von 54 auf 48 Std. | wie A | `Lösung · Der echte Fall: Fuß, EuGH 2010` → `· Der neue Dienstplan` | 4 | Stift (`szene_164stift_1`, Freesound CC0 751055) |
| **N Klausurtipp** `tipp`→`tf2` | hellgelbe Tafel, Lexi warnt; Zeilen, Kreuz beim typischen Fehler, gelber Block | Warnsymbol (Streamline Freehand) | `Klausurtipp · Wo prüfen?` → `· Typischer Fehler` → `· Erst richtlinienkonform auslegen` | 5 | – |
| **O Klausurschema** `sch`→`z5` | breite Karte, I.–IV. mit drei Untermerkmalen und Fundstellen, Block Rechtsfolge | – | `Klausurschema` → `› I. …` → `› IV. gegenüber dem Staat` → `› Rechtsfolge` | 9 | – |
| **P Merksatz** `merke`, `m2` | Lexi erklärt, zwei Sätze mit drei Markern | – | `Merksatz` | 5 | – |

**Blasen:** Stil C (`bausteine.blase`, Stil-C-Pflicht per Assertion), Schwanzspitze außerhalb der Blase am Mund; wortgleich mit dem Gesprochenen, Zahlen als Ziffern („48 Stunden“). **Zahlen** auf Tafeln und Pillen als Ziffern („54 Wochenstunden“, „8.12.1974“, „23.11.1996“, „Art. 6 Buchst. b“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; keine Bewegung.
**Geräusche:** zwei Handlungsgeräusche (Tür, Stift), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Hallentor, Lamellen und Haken aus Grundformen. Kein Mensch als Icon.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Herr Ruppert ist Feuerwehrmann bei der Berufsfeuerwehr seiner Stadt. Eine Landesverordnung erlaubt für die Feuerwehr im Schnitt 54 Wochenstunden; so plant ihn die Stadt ein. Herr Ruppert beruft sich auf die EU-Arbeitszeitrichtlinie 2003/88/EG: im Schnitt höchstens 48 Stunden pro Woche.
>
> Herr Goldbach, Leiter des Personalamts der Stadt, hält dagegen: Die Richtlinie richte sich an Deutschland, nicht an die Stadt. Es gelte die Verordnung.
>
> Annahme für den Fall: Deutschland hätte die Richtlinie nicht rechtzeitig umgesetzt (in Wirklichkeit ist sie umgesetzt).
>
> **Kann sich Herr Ruppert gegenüber der Stadt direkt auf die Richtlinie berufen?**
