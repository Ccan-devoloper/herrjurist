# Folge 215 · Differenzhypothese und Naturalrestitution: Schadensrecht §§ 249 ff. BGB – Schema – Szenenplan

**Stand:** 06.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_215.py`](src/skript_215.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Schuldrecht AT · Schema. Hook nach Plan („Dein Fahrrad wird angefahren – bekommst du die Reparatur oder Geld?“). Fiktiver Fall: Hedi stellt ihr Rad vor einer Bäckerei ab; Ludolf parkt rückwärts aus und fährt es an (Rahmen verbogen, Hinterrad kaputt). In der Werkstatt von Trude kostet die Reparatur 400 € plus 76 € Umsatzsteuer; ein gleichwertiges Rad 900 €. Ludolf will das Rad von seinem Schwager reparieren lassen; Hedi will das Geld.
Ablauf: Fall (Anfahren, Werkstatt, Schwager/Geld) → Frage → Sachverhalt → Haftungsgrund vorausgesetzt (§ 823 Abs. 1, Verweis 046) → 1. Schaden: Differenzhypothese (VI ZR 239/23 Rn. 8) → 2. Herstellung § 249 Abs. 1 (Wortlautkarte) → 3. Geld statt Herstellung § 249 Abs. 2 Satz 1 (Wortlautkarte, Ersetzungsbefugnis, erforderlich), fiktive Abrechnung, Satz 2 Umsatzsteuer (Wortlautkarte), § 250 → 4. Geldentschädigung § 251 Abs. 1 (Wortlautkarte, merkantiler Minderwert), Abs. 2 Satz 1 (Wortlautkarte, Vorrang der Herstellung) → Abwandlung 1.200 € (Ersatzrad, Restwert, 850 €; Kfz 130 %) → Ergebnis → Klausurtipp (Lexi, VII ZR 46/17) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 5:54,0 (5.052 vertonte Zeichen); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Hedi (HD), um 25 | Eigentümerin des Rads, Geschädigte, Gläubigerin | `standing/robot_dance-2` (schwarzes Oberteil der Pose, Hose Grün `#8FD694`), Kopf `Long`, Haut `#E9C2A0`, kein Bart; Mimiken `Calm`, `Smile`, `Serious` (redet), `Suspicious`, `Concerned\|Serious`, `Fear`, `Smile Big\|Smile` | `lucy` (Frau, jung) |
| Ludolf (LU), um 50 | Autofahrer, Schädiger; entschuldigt sich, kein Bösewicht | `standing/resting-1` (Pullover Orange `#F4A259`, schwarze Hose der Pose), Kopf `Short 2`, Brille `Glasses 2`, Haut `#D9A884`, kein Bart; Mimiken `Calm`, `Smile` (redet), `Concerned\|Serious` (klagt), `Fear`, `Suspicious`, `Solemn` | `stephan` (Mann, mittel) |
| Trude (TR), um 65 | Inhaberin der Fahrradwerkstatt (ein Satz) | `standing/crossed_arms-2` (schwarzes Oberteil der Pose, Hose Blau `#8DB3F2`), Kopf `Gray Bun`, Brille `Glasses 3`, Haut `#F0CDB2`; Mimiken `Calm` (redet), `Smile`, `Suspicious` | `hilde` (Frau, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Stimmen:** nur aus dem Pool (stephan, hilde, christian, lucy); `christian` nicht verwendet, also nie stephan und christian in einer Szene. Ludolf (stephan) spricht in A1 allein und in A3 mit Hedi (lucy); Trude (hilde) in A2.
**Namen** mit eindeutig deutscher Aussprache, nicht in der Namensliste des Auftrags, nicht in der Reservierungsliste der parallelen Folgen (202–214) und in keinem `.py/.md/.json/.txt/.csv` unter `youtube/preproduction/` bzw. `youtube/themenplanung/` (Volltextsuche 06.10.2026; verworfen: Merle (16 Treffer), Ortwin (3), Arnulf (125), Volkhard (zu nah an Volker/Volkmar), Wanda (mögliche englische Lesart)). Reserviert als „215: Hedi, Ludolf, Trude“. Nie im Genitiv (Skript-Assertion). Namensschilder Hedi Blau, Ludolf Grün, Trude Gelb.
**Blickrichtung:** Grundansicht gespiegelt (blickt nach links), `_r` nach rechts. A1: Hedi blickt nach rechts zum Rad und zum Auto, Ludolf nach links zu ihr. A2: Trude nach rechts zu Hedi, Hedi nach links. A3 (geteiltes Bild): Ludolf nach rechts zur Trennlinie, Hedi nach links. Ergebnis: Hedi nach rechts zu Ludolf, Ludolf nach links. Tafelszenen: beide nach links zur Tafel. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `HD_redet`, `LU_klagt`, `LU_redet`, `TR_redet` (je links/rechts) und Lexi. Keine weiteren Menschen im Bild; das Fahrrad ist ein Phosphor-Symbol **ohne Fahrerfigur** (Tabler `bike` verworfen, weil es eine Strichfigur zeigt). Figuren-PNGs `../peeps/op_215/` (72 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- Posen der letzten drei Folgen nicht verwendet (212: blazer-4, resting-2; 213: robot_dance-3, easing-1, walking-2, shirt-1; 214: easing-2, walking-1, walking-3); robot_dance-1 bleibt Lexi; Prothesen-Posen verworfen; keine Polka Dots, keine Bärte, keine Karikatur. Kleidung: schwarz-grün (Hedi), orange-schwarz (Ludolf, bewusst nicht gelb wie Lexi), schwarz-blau (Trude).
- **Schauplätze neu:** Bäckerei von außen mit Fahrradbügel (Markise, Schaufenster, Tür, Schild „Bäckerei“), Fahrradwerkstatt von innen (Lochwand mit Werkzeug, Montageständer mit eingespanntem Rad), geteiltes Bild beim Telefonat (Auto links, beschädigtes Rad rechts). Grundformen aus `baeckerei()`, `werkstatt()`, `buegel()`, `trenner()`; Requisiten aus Tabler und Phosphor. Gegenüber 212 (Kauf), 213 (Polizeirecht) und 214 (Notwehr) neu.
- Leitmotiv: **Fahrrad heil/schief** (gedrehtes Symbol, nicht umgezeichnet) in Fall, Differenzhypothese und Abwandlung. Cremegrund durchgehend, Tageslicht.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Das Rad** `fall`–`lu1` | ab 0,0 s Bäckerei, Bügel, Rad; Hook-Pillen („angefahren“, „Reparatur“); Hedi bei ihrem Namen; Auto fährt rückwärts von rechts heran (Bewegung `weg`), Pille „Ludolf parkt rückwärts aus“; beim Wort „Rad“ kippt das Rad (schief); „Rahmen verbogen, Hinterrad kaputt“; Ludolf steigt aus, Blase „Oh nein, das tut mir leid! Das / bringe ich wieder in Ordnung.“ | ph:`bicycle-bold`, tabler:`car` (Orange), `bread` (Gelb) | `Fall · Das Rad` → `… Ludolf parkt aus` → `… Das Rad ist kaputt` → `… Ludolf: „Das bringe ich in Ordnung“` | `szene_215crash_1` beim Kippen |
| **A2 Werkstatt** `werk`–`wert` | Werkstatt, Rad im Montageständer; Trude bei „Trude“ mit Werkzeug am Rad; Blase „Die Reparatur kostet 400 €, / plus 76 € Umsatzsteuer.“; Pille „Gleichwertiges Rad: 900 €“ mit grünem Rad | tabler:`tools`, `hammer`, `tool`; ph:`bicycle-bold` | `Fall · In der Werkstatt` → `… 400 € plus 76 € Umsatzsteuer` → `… Gleichwertiges Rad: 900 €` | `szene_215ratsche_1` beim Werkzeug |
| **A3 Schwager oder Geld / Frage** `idee`–`frage2` | geteiltes Bild (Telefonat): Ludolf mit Auto und Glühbirne, Blase „Mein Schwager repariert Räder. / Der macht das für mich.“; Hedi mit schiefem Rad, Blase „Nein danke. Ich will das Geld. / Was ich damit mache, / entscheide ich.“; Pillen der Frage | tabler:`car`, `bulb`, `phone` | `Fall · Ludolf hat eine Idee` → `… Der Schwager` → `… Hedi will das Geld` → `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig (40 px), ≈ 9,8 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Haftungsgrund** `grund`–`sys` | „etwa § 823 Abs. 1 BGB: Ludolf hat fahrlässig das Eigentum von Hedi verletzt“; Block „Heute: die Rechtsfolge“; Verweis Video 046 | tabler:`car-crash`, `scale` | `Haftungsgrund (vorausgesetzt) › …` → `Rechtsfolge: Schaden und Ersatz › …` | – |
| **D 1. Schaden** `dh`–`dh6` | Blöcke „tatsächliche Lage / nach dem Unfall“ – „hypothetische Lage / ohne den Unfall“; BGH VI ZR 239/23 Rn. 8; heiles (grün) und beschädigtes (schief) Rad zum Wort; Block „Differenz = Schaden“ | ph:`bicycle-bold`, tabler:`scale`, `equal` | `Rechtsfolge › 1. Schaden: Differenzhypothese › …` | – |
| **E 2. Herstellung** `w1`–`nr2` | **Wortlautkarte § 249 Abs. 1** (Marker Zustand herzustellen, nicht eingetreten); Block Naturalrestitution; Punkt „nach Abs. 1 allein: Ludolf lässt das Rad selbst reparieren, etwa beim Schwager“ | tabler:`tools`, `tool` | `Rechtsfolge › 2. Herstellung, § 249 Abs. 1 BGB › …` | – |
| **F 3. Geld statt Herstellung** `w2`–`erf` | **Wortlautkarte § 249 Abs. 2 Satz 1** (Marker Beschädigung einer, statt der, erforderlichen Geldbetrag); ✓ Ersetzungsbefugnis (VI ZR 69/12 Rn. 9); ✓ Schwager nicht hinnehmen; erforderlich (VI ZR 300/24 Rn. 11), „hier: Reparatur für 400 €“ | tabler:`coin-euro`, `arrows-split`, `hand-stop`, `calculator` | `Rechtsfolge › 3. Geld statt Herstellung, § 249 Abs. 2 Satz 1 BGB › …` | – |
| **G fiktiv / Umsatzsteuer** `fik`–`ust2` | ✓ „darf sie: in der Verwendung des Geldes frei“, fiktiv (VI ZR 9/17 Rn. 7; VI ZR 300/24 Rn. 12); **Wortlautkarte § 249 Abs. 2 Satz 2** (Marker tatsächlich); Rechnung fiktiv 400 €, repariert + 76 € (VI ZR 146/16 Rn. 9) | tabler:`tools`, `cash-banknote`, `receipt-tax`, `receipt-euro` | `Rechtsfolge › 3. Geld statt Herstellung › …` | – |
| **H § 250** `p250` | „§ 250 BGB führt zum Geld:“ Frist zur Herstellung, mit der Erklärung, sie danach abzulehnen | tabler:`hourglass` | `… › § 250 BGB` | – |
| **I 4. § 251 Abs. 1** `w4`, `mmw` | **Wortlautkarte § 251 Abs. 1** (Marker nicht möglich, nicht genügend, Geld); merkantiler Minderwert (VI ZR 239/23 Rn. 6 f.) | tabler:`coin-euro`, `car` | `Rechtsfolge › 4. Geldentschädigung, § 251 BGB › …` | – |
| **J § 251 Abs. 2** `w5`, `vor` | **Wortlautkarte § 251 Abs. 2 Satz 1** (Marker unverhältnismäßigen Aufwendungen); Block „Erst diese Grenze beendet den Vorrang der Herstellung“ (VI ZR 9/17 Rn. 6) | tabler:`scale`, `tools` | `… › Abs. 2 Satz 1` → `… › Vorrang der Herstellung` | – |
| **K Abwandlung** `var`–`kfz2` | Reparatur 1.200 €, Rad 900 €; ✓ Ersatzrad ist Herstellung, wirtschaftlicherer Weg (VI ZR 174/24 Rn. 21); 900 € – Restwert 50 €; Block „Hedi bekommt 850 €“; Auto 130 % (VI ZR 387/14 Rn. 6 f.); „1.200 € läge auch darüber“ | tabler:`tools`, `recycle`, `cash-banknote`, `car`; ph:`bicycle-bold` | `Abwandlung · Reparatur 1.200 € › …` | – |
| **L Ergebnis** `erg`, `erg2` | Bäckerei, Hedi und Ludolf, Pillen „Ergebnis: Den Schwager muss Hedi nicht hinnehmen“, „400 € · mit Reparaturrechnung 476 €“, Geldschein | tabler:`cash-banknote` | `Ergebnis · …` | – |
| **M Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt (redet): Haftungsgrund/Rechtsfolge trennen; fiktive Abrechnung im Werkvertragsrecht aufgegeben (VII ZR 46/17 LS 1), im Deliktsrecht möglich (VI ZR 300/24 Rn. 12) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | – |
| **N Klausurschema** `sch`–`k5` | breite Karte, 1.–4. mit Umsatzsteuer-Unterpunkt und Höhe, jede Zeile zum Wort | – | `Klausurschema › …` | – |
| **O Merksatz** `merke`, `mk2` | Lexi erklärt (redet), zwei Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund der Sprecherfigur, wortgleich mit dem Gesprochenen, Zahlen in Ziffern („400 €“, „76 €“).
**Bewertungszeichen:** Haken nur bei gesprochener Bejahung („Die Wahl liegt bei Hedi“, „Den Schwager muss sie nicht hinnehmen“, „Das darf sie“, „Auch ein Ersatzrad ist Herstellung“, „bleibt sie möglich“); sonst neutrale Aufzählungspunkte.
**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; einzige Bewegung: das ausparkende Auto (A1); kein Zoom.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Phosphor (MIT, `bicycle-bold`), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Bäckerei, Bügel, Werkstatt, Ständer aus Grundformen (`folien_215.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Hedi stellt ihr Fahrrad vor einer Bäckerei ab. Ludolf parkt rückwärts aus und fährt das Rad an: Der Rahmen ist verbogen, das Hinterrad kaputt. Ludolf sagt: „Das bringe ich wieder in Ordnung.“
>
> In der Werkstatt von Trude kostet die Reparatur 400 € plus 76 € Umsatzsteuer. Ein gleichwertiges Rad würde 900 € kosten.
>
> Ludolf will das Rad von seinem Schwager reparieren lassen. Hedi lehnt ab: „Ich will das Geld. Was ich damit mache, entscheide ich.“
>
> **Muss Hedi den Schwager hinnehmen, und wie viel Geld bekommt sie?**
