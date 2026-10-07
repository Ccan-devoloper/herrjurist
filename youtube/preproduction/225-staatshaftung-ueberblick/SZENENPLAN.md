# Folge 225 · Staatshaftungsrecht Überblick: Welche Ansprüche hast du? – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_225.py`](src/skript_225.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Staatshaftungsrecht · Schema, gebaut als Übersicht mit drei Mini-Fällen (Plan-Vorgabe). Ablauf: Hook (Straße vor dem Fahrradladen, Bagger, Zaun, Auto, Laden; Gespräch) → drei Kacheln und Frage → Sachverhalt → zwei Ebenen (Primär/Sekundär) → Amtshaftung (Wortlautkarten § 839 Abs. 1 Satz 1 BGB, Art. 34 Satz 1 GG) → Prüfschema am Fall Zaun (6 Punkte, progressiv) → Auto: Primärebene (Anfechtung, Rückzahlung, Verweis Folge 172) → Sekundärebene (Wortlautkarte § 39 Abs. 1 OBG NRW) → Länder-Overlay (NRW, Brandenburg, Sachsen) → Laden: Enteignung? (Wortlautkarte Art. 14 Abs. 3 GG, Naßauskiesung) → Aufopferung: enteignungsgleicher/enteignender Eingriff → Anliegerentschädigung (Wortlautkarte § 20 Abs. 6 StrWG NRW) → Übersicht „Welcher Anspruch wann?“ (progressiv) → Rechtsweg (Wortlautkarte Art. 34 Satz 3 GG) → Klausurtipp (Lexi) → Merksatz (Lexi). Hauptfilm 6:41,3 (5.832 vertonte Zeichen).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Bergner (BE), um 60 | Inhaber eines Fahrradladens, wohnt darüber | `standing/shirt-2` (schwarzes Hemd, Shorts Beige `#C9A66B`, Beinprothese – beiläufig, keine Täterrolle), Kopf `Gray Short` (helles Haar, Originalfarbe), Haut `#E8B48E`. Mimiken `Calm`, `Awe`, `Concerned\|Serious` (Sorge/redet), `Suspicious`, `Serious`, `Smile Big\|Smile` | `william` (Mann, älter) |
| Frau Wilmsen (WI), um 45 | Mitarbeiterin des Tiefbauamts der Stadt, sachlich | `standing/crossed_arms-1` (Pullover Rot `#F07A6A`, Hose schwarz), Kopf `Long Bangs`, ohne Brille (Abgrenzung zu Lexi), Haut `#D9A07A`. Mimiken `Calm`, `Serious` (redet), `Suspicious`, `Smile` | `laura_ruhig` (Frau, mittel) |
| Bauhof-Mitarbeiter (BH), ohne Namen | fährt den Bagger, spricht nicht | `standing/walking-2` (schwarzes Shirt, Hose Dunkelgrau `#4A4A58`), Mütze `hat-beanie`, Haut `#C98E66`; Mimiken `Calm`, `Fear` (erschrocken), `Concerned\|Serious`; Funktionsschild „Bauhof-Mitarbeiter“ | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Grundansicht gespiegelt (nach links), `_r` nach rechts. Fallszene: Herr Bergner vor seinem Haus blickt nach links zur Baustelle; Bauhof-Mitarbeiter blickt nach rechts zu Bagger und Zaun; Frau Wilmsen blickt nach rechts zu Herrn Bergner. Tafelszenen: alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `BE_redet`, `WI_redet` (je links/rechts) und Lexi.
- **Stimmen** nur aus dem Pool (william, sabrina, marc, laura_ruhig): william und laura_ruhig; Folge 172 (Staatshaftung) hatte sabrina/marc.
- **Namen:** Bergner, Wilmsen – deutsch, nicht in der Liste vergebener Namen, in `namen_reserviert.txt` eingetragen („Gunda“ vorher wieder freigegeben: zu nah an „Gundula“, Folge 207); Volltextsuche in `youtube/preproduction` ohne Treffer.
- Figuren-PNGs: `../peeps/op_225/` (50 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 222 (`easing-1`, `resting-1`, `robot_dance-2`, `crossed_arms-2`), 223 (`shirt-3`, `shirt-4`, `blazer-3`), 224 (`easing-2`, `resting-2`, `walking-1`, `blazer-1`, `robot_dance-3`, `pointing_finger-2`) – hier `shirt-2`, `crossed_arms-1`, `walking-2`; keine Polka Dots, keine Bärte. Schauplatz **Straße mit Baustelle, Haltverbotsschild, Gartenzaun und Haus mit Fahrradladen** (Seitenansicht) – neu gegenüber 222 (Klausurraum, Mietwohnung), 223 (Tischlerwerkstatt, Bank) und 224 (Wohnung, Polizei, Ermittlungsrichter, Hauptverhandlung, Wohngemeinschaft) – Kontaktbögen der drei Folgen danebengelegt. Die Kachel-Frage (A2) ähnelt formal den „Fragen“-Kacheln aus 224, zeigt aber Requisiten statt Figuren. Rückkehr in die Straße nicht nötig; die drei Mini-Fälle werden über Kacheln und Requisiten (Zaun, Auto, Taxi, Laden) gehalten.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A Fall** `fall`→`wi1` | Straße (Fahrbahn), Haltverbotsschild (Zeichen 283 als Grundform), Auto (blau) rechts davon = außerhalb; Haus mit Schaufenster „Fahrräder“, Gartenzaun. Ab „baut“ Pylonen, Bagger und Bauhof-Mitarbeiter; bei „gegen“ fährt der Bagger an den Zaun, Zaun beschädigt (zwei Latten umgeknickt, eine liegt); ab „Ein paar Tage“ ist das Auto weg, Pille „außerhalb“; ab „versperrt“ Sperre vor der Ladentür; fünf Pillen zum gesprochenen Satz; Herr Bergner redet (Blase), Frau Wilmsen kommt und redet (Blase) | tabler `car`, `traffic-cone`, `backhoe`, `barrier-block`; ph `bicycle`; Straße/Schild/Haus/Zaun aus Grundformen | `Fall · Die Straße vor dem Fahrradladen` (ab 0,0 s) → `› Die Stadt baut die Straße um` → `Der Zaun` → `Das Auto` → `Der Laden` → `Herr Bergner beschwert sich` | Baggermotor (`szene_225bagger_1`, Freesound CC0 606941) bei „Die Stadt baut“; Holzbruch (`szene_225zaun_1`, Freesound CC0 349497) bei „gegen“ |
| **A2 Frage** `frage` | drei Kacheln: 1 Zaun, 2 Auto, 3 Laden; Frage als Pille | tabler `fence`, `car`; ph `storefront` | `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s | – | `Sachverhalt` | – |
| **C Zwei Ebenen** `ebenen`→`sekundaer` | blaue Fläche Primärebene, gelbe Fläche Sekundärebene; Frau Wilmsen, Herr Bergner | tabler `shield-check`, `cash-banknote` | `Überblick · Zwei Ebenen` → `› Primärebene` → `› Sekundärebene` | – |
| **D Amtshaftung** `ah`, `w839`, `w34` | **Wortlautkarten § 839 Abs. 1 Satz 1 BGB** (Marker Beamter, Dritten, Amtspflicht, Schaden zu ersetzen) und **Art. 34 Satz 1 GG** (Marker Verantwortlichkeit, Staat, Körperschaft) | tabler `fence`, `building-bank` | `Amtshaftung · § 839 BGB` → `› Art. 34 Satz 1 GG` | – |
| **E Prüfschema** `s1`→`s7` | sechs nummerierte Punkte zum Wort, Haken zur Bejahung, Ergebnisblock „Die Stadt ersetzt den Zaun“; Bauhof-Mitarbeiter und Herr Bergner | tabler `backhoe`, `fence`, `alert-triangle`, `receipt-euro`, `scale`, `cash-banknote` | `Amtshaftung › 1. Beamter …` → `› 2.` … `› 6. kein Ausschluss` → `› Ergebnis: Zaun` | – |
| **F Auto Primärebene** `ab`→`fba` | Kreuz „rechtswidrig“, Konnexität, Haken Anfechtung (250 €), Rückzahlung, Block Verweis Folge 172 | tabler `car`, `file-invoice`, `cash-banknote`, `restore` | `Das Auto · rechtswidrig abgeschleppt` → `› Primärebene: Anfechtung` → `› Geld zurück` → `› Folgenbeseitigung` | – |
| **G Auto Sekundärebene** `taxi`→`vermoegen` | 30 € Taxi; **Wortlautkarte § 39 Abs. 1 OBG NRW** (Buchst. a ausgelassen); Pille „Beispiel Nordrhein-Westfalen“; Haken Vermögensschäden | ph `taxi`; tabler `scale` | `Das Auto › Sekundärebene: Taxi` → `› § 39 Abs. 1 OBG NRW` | – |
| **H Länder-Overlay** `tab`→`teigen` | Tabelle NRW/Brandenburg/Sachsen, Zeilen zum Wort; „dein Land“; Frau Wilmsen | tabler `map-2` | `Länder-Overlay · Entschädigung` → `› Nordrhein-Westfalen` → `› Brandenburg` → `› Sachsen` → `› dein Landesgesetz` | – |
| **I Laden: Enteignung?** `la`→`nichts` | **Wortlautkarte Art. 14 Abs. 3 Satz 1, 2 GG**; Block Begriff (Naßauskiesung), Kreuz „nichts entzogen“ | ph `storefront`; tabler `building-bank` | `Der Laden · Enteignung?` → `› Begriff der Enteignung` → `› keine Enteignung` | – |
| **J Aufopferung** `auf`→`bau` | Grundgedanke, § 75 EinlALR; roter Block enteignungsgleicher, grüner Block enteignender Eingriff; Haken | ph `hand-heart`; tabler `alert-triangle`, `barrier-block` | `Der Laden › Aufopferungsgedanke` → `› enteignungsgleicher Eingriff` → `› enteignender Eingriff` | – |
| **K Anliegerentschädigung** `anl`→`lerg` | **Wortlautkarte § 20 Abs. 6 Satz 1 StrWG NRW**, Marker zum Wort (für längere Zeit, unterbrochen, erheblich erschwert, Behelfsmaßnahmen, wirtschaftliche Existenz, Fortbestehen des Betriebes); Ergebnis mit Haken | tabler `barrier-block`, `hourglass`, `cash-banknote`; ph `storefront` | `Der Laden › Anlieger` → `› § 20 Abs. 6 StrWG NRW` → `› Höhe` → `› Ergebnis` | – |
| **L Übersicht** `ueb`→`u5` | breite Karte „Welcher Anspruch wann?“, fünf Zeilen Situation → Anspruch, Zeilensymbol je Mini-Fall | tabler `restore`, `fence`, `first-aid-kit`; ph `taxi`, `storefront` | `Übersicht · Welcher Anspruch wann?` → `› Folgenbeseitigung` → … `› Aufopferung` | – |
| **M Rechtsweg** `rw`→`rwvg` | **Wortlautkarte Art. 34 Satz 3 GG**, Haken ordentliche Gerichte (§ 40 Abs. 2 VwGO), Haken Verwaltungsgericht | tabler `gavel`, `building-bank` | `Rechtsweg` → `› Art. 34 Satz 3 GG` → `› § 40 Abs. 2 VwGO` → `› Verwaltungsgericht` | – |
| **N Klausurtipp** `tipp`→`t3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · erst die Primärebene` → `› kein Wahlrecht` → `› Ansprüche nebeneinander` | – |
| **O Merksatz** `merke`, `mk2` | Lexi erklärt (redet), Marker „abwehren“, „Schadensersatz“, „Entschädigung“ | – | `Merksatz` | – |

**Klausurschema:** Das Prüfschema der Amtshaftung (E) und die Übersicht „Welcher Anspruch wann?“ (L) bauen sich jeweils Punkt für Punkt auf; ein zusätzliches Schema nach dem Klausurtipp entfällt (Plan-Vorgabe: Übersicht vor Rechtsweg, Tipp und Merksatz am Ende).
**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen). **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („1.200 €“, „250 €“, „5 Monate“, „§ 839“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; nur der Bagger springt beim Zaun an eine neue Stelle (harter Schnitt).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Phosphor (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Straße, Schild, Haus, Zaun programmatisch (`strasse()`, `haltverbot()`, `haus()`, `zaun()` in `folien_225.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Herr Bergner wohnt in einer Stadt in Nordrhein-Westfalen über seinem kleinen Fahrradladen. Die Stadt baut die Straße davor um. Ein Mitarbeiter des städtischen Bauhofs fährt beim Rangieren mit dem Bagger unachtsam gegen Herrn Bergners Gartenzaun. Die Reparatur kostet 1.200 €; Ersatz von anderer Seite gibt es nicht.
>
> Herrn Bergners Auto steht in einer Seitenstraße, außerhalb einer Haltverbotszone. Die Stadt lässt es trotzdem abschleppen und setzt die Kosten von 250 € durch Bescheid fest. Herr Bergner zahlt, um sein Auto zurückzubekommen; für das Taxi zum Abschlepphof zahlt er 30 €.
>
> Die Baustelle versperrt 5 Monate lang den Zugang zu seinem Laden; einen Behelfsweg gibt es nicht. Die Kunden bleiben aus, der Laden steht vor dem Aus. Frau Wilmsen vom Tiefbauamt der Stadt meint, das treffe alle Anlieger.
>
> **Welche Ansprüche hat Herr Bergner gegen die Stadt?**

Kein Fiktiv-Hinweis; keine echte Stadt, kein Wappen.
