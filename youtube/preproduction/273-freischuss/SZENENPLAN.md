# Folge 273 · Freischuss Jura: Freiversuch und Verbesserungsversuch erklärt – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_273.py`](src/skript_273.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Methodik · Examen. Rahmen nach dem Plan-Hook („Du schreibst das Examen früh – was passiert, wenn es schiefgeht?“): Die Jurastudentin Leonore (7. Fachsemester, NRW, ein Auslandssemester) steht im Flur der Fakultät vor dem Aushang mit den Meldefristen; ihr Freund Rasmus hat das Examen im letzten Jahr früh geschrieben und danach seine Note verbessert. Aufbau nach Auftrag: Hook → Sachverhalt → Was ist der Freiversuch (Wortlautkarte § 5d Abs. 5 S. 1–3 DRiG, Folge für Leonore) → Voraussetzungen (Tafel mit drei geprüften Ländern, Semester, die nicht mitzählen, Leonore konkret) → Verbesserungsversuch (Tafel Land/Antrag/Gebühr; bessere Note bleibt; 2. Examen) → Strategie (Chancen/Risiken) → Ergebnis (Flur) → Klausurtipp (Lexi) → Freischuss in 5 Schritten → Merksatz (Lexi).
**Länge:** Hauptfilm 5:14,8 (4.640 vertonte Zeichen), im Regelrahmen.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Leonore (LE), Anfang 20 | Jurastudentin in NRW, 7. Fachsemester | Pose `standing/crossed_arms-2` (Arme verschränkt, schwarzes Oberteil der Pose, Hose Blau `#8DB3F2`, schwarze Schuhe), Kopf `Medium Bangs 2` (Haar Kastanienbraun `#7A4A2E`), Haut `#F2CBA8`, keine Brille, kein Bart; Mimiken `Suspicious` (denkt), `Concerned\|Serious` (Sorge, redet l1), `Awe` (staunt), `Calm`, `Smile` (froh, redet l2), `Driven` (entschlossen, redet l3), `Serious` | `julia` (Frau, jung, ruhig) |
| Rasmus (RA), Mitte 20 | Freund, Examen im letzten Jahr früh geschrieben | Pose `standing/shirt-4` (schwarzes Hemd der Pose, Hose Sand `#D9B48F`, weiße Schuhe), Kopf `Short 3` (schwarzes Haar; diese Frisur ist nicht einfärbbar), Haut `#D9A27A`, keine Brille, kein Bart; Mimiken `Calm` (redet r1), `Smile` (froh, redet r2/r3), `Serious`, `Suspicious`, `Smile Big\|Smile` | `niklas` (Mann, jung) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Beide Posen blicken im Original nach rechts. Grundansicht gespiegelt = blickt nach links (Rasmus im Flur, alle Tafelszenen), `_r` = blickt nach rechts (Leonore im Flur zum Aushang und zu Rasmus).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `LE_redet`, `LE_redet2`, `LE_redetfroh`, `RA_redet`, `RA_redetfroh` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots, keine Karikatur, kein Klischee (Leonore abwägend, Rasmus hilfsbereit, kein Besserwisser).
- **Stimmen nur aus dem Pool** niklas, helmut, ela_froh, julia: Leonore `julia`, Rasmus `niklas`. `helmut` (älter) passt zu keiner Rolle, `ela_froh` nicht für die ernste Rolle.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen, nicht in `namen_reserviert.txt`, Volltextsuche unter `youtube/preproduction` und `youtube/themenplanung` am 08.10.2026: Leonore 0, Rasmus 0 Treffer (verworfen: Henrike – Folgen 106/127, Annelie, Kaspar, Linus – bereits in Dateien vorhanden; Emma, Jonas, Paul – mögliche englische Lesart). Reservierung „273: Leonore, Rasmus“ vor der Vertonung angehängt. Kein Genitiv eines Namens („die Ausgangslage von Leonore“).
- Präfixe `LE_`/`RA_` (nie `ER_`). Figuren-PNGs: `../peeps/op_273/` (72 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen** (Figurenrezepte 269–271 und Methodik 237/201 verglichen; 268, 272 entstehen parallel): 269 (`blazer-1`, `pointing_finger-1`, `resting-2`), 270 (`resting-1`, `robot_dance-2`, `blazer-4`), 271 (`resting-1`, `easing-1`), 237 (`easing-2`, `blazer-3`). 273: `crossed_arms-2` und `shirt-4` – dort nicht verwendet; blaue Hose/Sandhose dort nicht. Schauplatz neu: **Flur der Fakultät mit Tür und Aushang (Pinnwand mit Zetteln „Meldefristen Examen“ und „Formular“)** – nicht das Büro aus 237, nicht die WG-Küche aus 201. Leitmotiv: Aushang mit Formular → Versuchsleiste → Semesterleiste → das abgenommene Formular. Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Flur** `fall`→`r1` | Flur: Tür links, Pinnwand Mitte, Leonore links (blickt nach rechts), Rasmus kommt rechts dazu | programmatisch: Tür, Pinnwand, Zettel, Formular; Ring um „Meldefristen“ | `Fall · Flur der juristischen Fakultät` → `· 7. Semester: jetzt schon melden?` → `· im Freischuss zählt ein Fehlversuch nicht` | ab 0,0 s Flur mit Leonore und Schild · Ring · Rasmus mit Schild · Blase l1 · Pille „7. Semester“ · Blase r1 · Pille „Fehlversuch zählt nicht“ | – |
| **A2 Einstieg** `hook`→`wie` | Tafel: früh schreiben, „Was, wenn es schiefgeht?“ (Kreuz), Freiversuch = „Freischuss“, drei Fragen | tabler:`calendar-event`, `alert-triangle`, `lifebuoy`, `list-check` | `Einstieg · früh schreiben: und wenn es schiefgeht?` → … | ≈ 8 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt · Die Ausgangslage von Leonore` | 1 | – |
| **C Freiversuch** `was`→`wl5` | Wortlautkarte § 5d Abs. 5 S. 1–3 DRiG, Marker „einmal wiederholt“, „frühzeitig“, „vollständig erbracht“, „nicht unternommen“, „Landesrecht“ synchron | tabler:`help`, `book`, `lifebuoy`, `map-pin` | `Freiversuch · Was ist das?` → `› § 5d Abs. 5 DRiG` → … | ≈ 10 | – |
| **D Folge für Leonore** `folge`→`nur1` | Versuchsleiste Freiversuch (Kreuz, „zählt nicht“) – regulärer Versuch – Wiederholung; „nur für die Pflichtfachprüfung“ | tabler:`user-question`, `circle-x`, `refresh`, `school` | `Freiversuch › Was heißt das für Leonore?` → … | ≈ 9 | – |
| **E Voraussetzungen** `vor`→`unun` | Tafel NRW / Niedersachsen / Sachsen mit Fundstellen, Haken „ununterbrochen“ | tabler:`list-check`, `map-pin`, `calendar`, `circle-check` | `Voraussetzungen · Was gilt in deinem Land?` → … | ≈ 8 | – |
| **F Semester** `frei`→`krank` | Ausland: NRW bis 3, Niedersachsen bis 3, Sachsen bis 2; NRW höchstens 4; Krankheit: amtsärztliches Zeugnis | tabler:`calendar-x`, `plane`, `calendar`, `stethoscope` | `Semester › Was zählt nicht mit?` → … | ≈ 10 | – |
| **G Leonore konkret** `leo2`→`l2` | Semesterleiste 1–7, 5. Semester wird „Ausland“, „zählt nicht mit“, „dann zählen erst 6 Semester“, „frag dein Prüfungsamt“, Blase Leonore | tabler:`plane`, `calendar-check`, `building-bank` | `Fall Leonore › …` | ≈ 7 | – |
| **H Verbesserungsversuch** `verb`→`vsn2` | Tabelle Land / Antrag-Termin / Gebühr, zellenweise in Sprechreihenfolge | tabler:`trending-up`, `repeat`, `clock`, `coin-euro`, `briefcase` | `Verbesserungsversuch · …` → `› NRW …` → `› Niedersachsen …` → `› Sachsen …` | ≈ 15 | – |
| **I Am Ende** `besser`→`r2` | Haken „schlechtere Note verdrängt die alte nicht“, 2. Examen, Punktebalken Rasmus 7 → 9, Blase Rasmus | tabler:`shield-check`, `briefcase` | `Am Ende · …` | ≈ 6 | – |
| **J Strategie** `strat`→`stand` | Chance (+) / Risiko (−) nacheinander, „entscheidend: dein Stand“ | tabler:`scale`, `lifebuoy`, `hourglass`, `writing` | `Strategie · Lohnt sich der Freischuss?` → … | ≈ 11 | – |
| **K Ergebnis** `erg`→`r3` | zurück in den Flur (Rückkehr, weil die Geschichte am Aushang schließt): Leonore nimmt das Formular vom Aushang (0,45 s Bewegung), Blasen Leonore und Rasmus | programmatisch: Formular | `Ergebnis · Leonore nimmt das Formular` → … | ≈ 6 | Zettel vom Brett (`szene_273formular_1`) |
| **L Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, sechs Klausurblätter mit Haken, „auch wenn sie schlecht läuft“, Schutz nur bei vollständigen Leistungen, Lexi warnt | tabler:`file-text`, Warnsymbol (Streamline Freehand) | `Klausurtipp · wie ein echter Versuch` → … | ≈ 5 | – |
| **M Schema** `sch`→`k5` | breite Karte, I.–V. Punkt für Punkt | – | `Freischuss · 5 Schritte` → `› I. …` … | 6 | – |
| **N Merksatz** `merke`→`m3` | Lexi erklärt, vier Marker | – | `Merksatz` | 7 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; einzige Bewegung: das Formular wandert vom Aushang vor Leonore; kein Zoom.
**Geräusche:** ein Handlungsgeräusch (Formular vom Aushang), Freesound 257913 (CC0), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Leonore studiert Jura in Nordrhein-Westfalen, ohne Unterbrechung. Sie ist im 7. Fachsemester.
>
> 1 Semester hat sie an einer Universität im Ausland Recht studiert und dort Leistungsnachweise erworben.
>
> Sie überlegt, sich jetzt zur staatlichen Pflichtfachprüfung zu melden. Ihr Freund Rasmus hat das Examen im letzten Jahr früh geschrieben und danach seine Note verbessert.
>
> **Was gilt, wenn Leonore früh schreibt und durchfällt? Und wenn sie besteht?**
