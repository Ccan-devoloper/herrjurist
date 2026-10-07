# Folge 237 · Probeklausuren Examen: Wie viele schreiben und wie auswerten? – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_237.py`](src/skript_237.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Methodik · Lernen, Format „Schritte“, ohne Normprüfung. Rahmen nach dem Plan-Hook („Du schreibst jede Woche eine Klausur, aber die Noten bleiben gleich“): Der Jurastudent Friedrich legt seinem Mentor Herrn Seebach in der Sprechstunde zwölf korrigierte Probeklausuren auf den Tisch – fast immer 6 Punkte, ausgewertet hat er keine. Aufbau nach Auftrag: Hook → Problem (schreiben ohne auswerten) → wie viele (Faustregel, Verteilung wie im Examen, Verweis 201) → unter Examensbedingungen (Zeit, Hilfsmittel; Referendariat) → Auswertung in 4 Schritten (Tafel mit durchgehender Schrittleiste; Fehlerarten mit Verweis 117; Karten mit Verweis 201) → Wochenrhythmus (Tafel) → Ergebnis → Klausurtipp (Lexi) → Klausurtraining I.–V. → Merksatz (Lexi).
**Länge:** Hauptfilm 5:21,0 (4.450 vertonte Zeichen), im Regelrahmen.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Friedrich (FR), Mitte 20 | Jurastudent in NRW, sieben Monate vor den Examensklausuren | Pose `standing/easing-2` (offenes Hemd Grün `#8FD694` über schwarzem Shirt, Jeans `#4A5A7A`, weiße Turnschuhe, Hände locker), Kopf `Short 4` (schwarzes Haar), Haut `#EAC09A`, keine Brille, kein Bart; Mimiken `Tired` (müde, Hook), `Concerned\|Serious` (ratlos, redet f1/f2), `Suspicious` (denkt), `Calm`, `Awe` (staunt, redet f3), `Driven` (entschlossen), `Smile`, `Smile Big\|Smile` (stolz), `Smile` (redet f4) | `niklas` (Mann, jung) |
| Herr Seebach (SB), um 60 | Mentor an der Uni | Pose `standing/blazer-3` (Sakko Braun `#9C6B4E` über schwarzem Shirt, Hose `#4A4A55`, Hand an der Hüfte), Kopf `No Hair 3` (Glatze, grauer Haarkranz `#BDBDC4`), Brille `Glasses 3`, Haut `#E8B896`, kein Bart; Mimiken `Calm` (redet s1), `Serious` (redet s2), `Smile` (redet s3), `Suspicious`, `Serious`, `Smile` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Beide Posen blicken im Original nach rechts. Grundansicht gespiegelt = blickt nach links (Herr Seebach zu Friedrich im Büro, alle Tafelszenen), `_r` = blickt nach rechts (Friedrich zu Herrn Seebach im Büro). Kontaktbild `out/besetzung_237.png`.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `FR_redet`, `FR_redet2`, `FR_redetfroh`, `SB_redet`, `SB_redet2`, `SB_redetfroh` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots, keine Karikatur, kein Klischee (Friedrich fleißig, aber unsystematisch; Herr Seebach ruhig, kein Besserwisser).
- **Stimmen nur aus dem Pool** niklas, helmut, ela_froh, julia: `niklas` (Friedrich, einzige junge Männerstimme im Pool), `helmut` (Herr Seebach, älter). `ela_froh` (nicht für ernste Rollen) und `julia` (möglichst meiden) nicht verwendet.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen, nicht in `namen_reserviert.txt` und in keiner Datei unter `youtube/` (Volltextsuche 07.10.2026: Friedrich 0, Seebach 0 Treffer; verworfen: Hannes – Folge 005, Lothar – in 015 wegen „th“ ersetzt, Julius/Georg – mögliche englische Lesart). Reservierung „237: Friedrich, Seebach“ vor der Vertonung eingetragen. Kein Genitiv eines Namens („die Ausgangslage von Friedrich“, „eine Woche von Friedrich“).
- Präfixe `FR_`/`SB_` (nie `ER_`). Figuren-PNGs: `../peeps/op_237/` (80 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen** (Figurenrezepte 230–233, 235 verglichen; 234 und 236 entstehen parallel): 230 (`pointing_finger-2`, `shirt-3`, `shirt-4`), 231 (`walking-2`, `robot_dance-3`), 232 (`resting-1`, `easing-1`, `crossed_arms-1`), 233 (`easing-1`, `blazer-4`, `pointing_finger-1`, `sitting/bike`, `resting-2`), 235 (`walking-3`, `blazer-4`). 237: `easing-2` und `blazer-3` – dort nicht verwendet; grünes Hemd und braunes Sakko dort nicht. Schauplatz neu: **Büro des Mentors** mit niedrigem Bücherregal, Fenster, Schreibtisch mit Schubladen und Lampe (nicht die WG-Küche aus 201, nicht der Klausurrückgabe-Tisch aus 117, nicht der Klausursaal aus 045). Leitmotiv: der Stapel ungelesener Korrekturen → Fehlerprotokoll → ein einzelnes Blatt „drei Wochen später“. Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Sprechstunde** `fall`→`f2` | Büro: Regal links, Fenster, Schreibtisch mit Lampe; Friedrich links (blickt zu Herrn Seebach), Herr Seebach rechts | programmatisch: Regal, Fenster, Schreibtisch, Stapel; tabler:`lamp` | `Fall · Sprechstunde an der Uni` → `… 12 Klausuren, fast immer 6 Punkte` → `… nur die Note angeschaut` | ab 0,0 s Büro, Friedrich mit Schild, Pille · Herr Seebach mit Schild · Stapel landet · Blase f1 · Pille „6 Punkte“ · Blase s1 · Blase f2 · Pille „nur die Note“ | Stapel (`szene_237stapel_1`) |
| **A2 Einstieg** `hook`→`wie` | Tafel mit Notenkurve (12 Punkte um 6 auf der Skala 0–18), beide Figuren rechts | tabler:`chart-line`, `file-search`, `list-numbers` | `Einstieg · Noten bleiben gleich?` → `› aus jeder Korrektur lernen` → `› Wie viele? Wie auswerten?` | ≈ 7 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt · Die Ausgangslage von Friedrich` | 1 | – |
| **C Problem** `warum`→`s2` | Tafel, zwei Hälften (Schreiben/Auswertung), Blase Herr Seebach | tabler:`chart-line`, `files`, `writing`, `search` | `Problem · Warum bleibt die Note stehen?` → … → `› nur zur Hälfte geschrieben` | ≈ 7 | – |
| **D Wie viele** `viele`→`lieber` | Tafel: Pille „Faustregel, keine Vorschrift“, 1 bzw. 2 Klausurblätter, Haken/Kreuz | tabler:`files`, `calendar-week`, `flag`, `file-search`, `file-text` | `Wie viele? · Wie viele Klausuren?` → `› Faustregel, keine Vorschrift` → … | ≈ 8 | – |
| **E Verteilung** `fach`→`v201` | Tafel: Balken 3/2/1 (Examen NRW), Balken 1/2, 1/3, 1/6 (Probeklausuren), § 10 Abs. 2 S. 3 JAG NRW, § 5d Abs. 6 S. 1 DRiG, Verweis 201 | tabler:`scale`, `map-pin`, `chart-bar`, `calendar` | `Wie viele? › verteilt wie im Examen` → … → `› Lernplan: Folge 201` | ≈ 11 | – |
| **F Examensbedingungen** `bed`→`ref` | Tafel: 5 Stunden, Hilfsmittel, Form (mit NRW-Fundstellen), Handy/Lehrbuch, nicht abbrechen, Referendariat | tabler:`school`, `clock`, `book`, `pencil`, `device-mobile-off`, `hand-stop`, `briefcase` | `Wie im Examen · Examensbedingungen` → … → `› Referendariat: genauso auswerten` | ≈ 9 | – |
| **G Auswertung 1** `aus`→`a1b` | Tafel mit Schrittleiste 1–4; korrigierte Probeklausur mit Randzeichen, „6 Punkte“ | tabler:`list-numbers`, `file-search` | `Auswertung · 4 Schritte` → `› 1. Korrektur lesen` → `› 1. jede Randbemerkung` | ≈ 8 | – |
| **H Auswertung 2** `a2`→`a2c` | Schrittleiste (1 fertig, 2 aktiv); Musterlösung I.–IV. neben Gliederung I.–III., Ring „übersehen?“, Ring „anders aufgebaut: warum?“ | tabler:`arrows-diff`, `zoom-question` | `› 2. Musterlösung neben die Gliederung` → … | ≈ 7 | – |
| **I Auswertung 3** `a3`→`f3` | Schrittleiste (3 aktiv); Fehlerprotokoll Aufbau/Schwerpunkt/Wissen/Zeit, Zählkästchen 2/7/3/5, Ring um Schwerpunkt, Verweis 117, Blase Friedrich | tabler:`clipboard-list`, `chart-bar` | `› 3. das Fehlerprotokoll` → … → `› 3. die Punkte gehen am Schwerpunkt verloren` | ≈ 13 | – |
| **J Auswertung 4** `a4`→`a4c` | Schrittleiste (4 aktiv); Karteikarte vorn/hinten, „in deine Wiederholung“, Verweis 201 | tabler:`cards`, `repeat` | `› 4. Wiederholungskarten` → … | ≈ 7 | – |
| **K Wochenrhythmus** `wr`→`wso` | Tabelle Mo–So × morgens/Tagesplan, zellenweise in Sprechreihenfolge | tabler:`calendar-week`, `file-search`, `books`, `cards`, `chart-bar`, `clock`, `sun` | `Wochenrhythmus · eine Woche von Friedrich` → … → `› Sonntag: frei` | ≈ 11 | – |
| **L Ergebnis** `erg`→`s3` | zurück ins Büro (Rückkehr, weil die Geschichte in der Sprechstunde schließt): ein einzelnes Blatt auf dem Tisch, Pillen „kein Schwerpunkt-Fehler am Rand“, „7 Punkte“, Blasen Friedrich und Herr Seebach | programmatisch: Blatt | `Ergebnis · 3 Wochen später` → … | ≈ 6 | – |
| **M Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lösungsskizze mit „Ziel: häufigste Fehlerart“, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · 1 Ziel pro Probeklausur` → … | ≈ 6 | – |
| **N Klausurtraining** `sch`→`k5` | breite Karte, I.–V. Punkt für Punkt | – | `Klausurtraining · 5 Schritte` → `› I. …` … `› V. fester Auswertungstag` | 6 | – |
| **O Merksatz** `merke`→`m3` | Lexi erklärt, drei Marker | – | `Merksatz` | 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Stapel fällt 0,35 s auf den Tisch (einzige Bewegung), kein Zoom.
**Geräusche:** ein Handlungsgeräusch (Stapel auf dem Schreibtisch). Freesound-API am 07.10.2026 nicht erreichbar (HTTP 502/Zeitüberschreitung) → vorhandene CC0-Datei aus `sfx3/` unter eigenem Namen kopiert, Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Friedrich studiert Jura in Nordrhein-Westfalen. In 7 Monaten schreibt er die Klausuren der staatlichen Pflichtfachprüfung.
>
> Seit 12 Wochen schreibt er jede Woche eine Probeklausur im Klausurenkurs seiner Uni. Fast immer bekommt er 6 Punkte.
>
> Die Korrekturen liest er nicht: Er schaut auf die Note und schreibt die nächste Klausur.
>
> **Wie viele Klausuren soll Friedrich schreiben, und wie wertet er sie aus?**
