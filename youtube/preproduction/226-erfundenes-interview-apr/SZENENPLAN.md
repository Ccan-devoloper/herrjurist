# Folge 226 · Erfundenes Interview: Allgemeines Persönlichkeitsrecht im Zivilrecht – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_226.py`](src/skript_226.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Deliktsrecht · Klassiker-Fall. Aufbau nach Auftrag: Hook mit Zahlen als Ziffern (Titel „Exklusiv!“, „4 Seiten Interview“, „Auflage: 400.000 Exemplare“) → Frage, Nachbildung des Klassikers („im echten Fall ein erfundenes Interview mit einer Prinzessin“, Fundstelle BGHZ 128, 1) → Sachverhalt → I. Anspruchsgrundlage (Wortlautkarte § 823 Abs. 1 BGB, Verweis auf das Grundschema der Folge 067), sonstiges Recht seit 1954, Wortlautkarten Art. 2 Abs. 1 und Art. 1 Abs. 1 GG, Rahmenrecht → II. Eingriff (Unterschieben nicht getaner Äußerungen, Privatleben) → III. Abwägung mit der Pressefreiheit (Wortlautkarte Art. 5 Abs. 1 Satz 2 GG; erfundenes Interview trägt nichts zur Meinungsbildung bei; unrichtiges Zitat nicht geschützt) → Verschulden (Vorsatz) → IV. Rechtsfolgen (1. Unterlassung, § 1004 Abs. 1 Satz 2 analog; 2. Widerruf, notfalls auf der Titelseite; 3. Geldentschädigung: Voraussetzungen, Abgrenzung § 253 Abs. 2 in einem Satz, Höhe mit Genugtuung, Prävention, Gewinnerzielung als Bemessungsfaktor, Hemmungseffekt, Grenzen) → Ergebnis in der Kanzlei → Klausurtipp (Lexi) → Prüfschema → Merksatz (Lexi). Hauptfilm 6:18,6 (5.576 vertonte Zeichen). Vorlagen: 205 (Werkzeuge, Hilfsfunktionen, Wortlautkarten), 160 (APR, nur Rechtsstand), 067 (Schema § 823 I, nur verwiesen), 015 (Namens-/Sichtprüfung), Katzenkönig (Stil).

**Darstellung (Vorgabe Koordinator):** Die reale Person wird nicht gezeigt und nicht karikiert; fiktive Schauspielerin Juliane Hellberg, fiktives Wochenmagazin „Funkelblatt“ (kein echter Verlag, Titelseite aus Grundformen, Brustbild = Ausschnitt der Open-Peeps-Figur Juliane). Der echte Fall nur gesprochen als „ein erfundenes Interview mit einer Prinzessin“; der Name steht nur als Fallbezeichnung auf der Fundstellen-Pille „BGH, Urt. v. 15.11.1994 · VI ZR 56/94 · BGHZ 128, 1 (Caroline von Monaco)“ und im zugehörigen Prüfpfad.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Juliane Hellberg (JU), um 35 | Schauspielerin, Betroffene | `standing/resting-1` (Oberteil Rosa `#F2A7B8`, schwarze Hose), Kopf `Long Curly` (schwarz, nicht einfärbbar), Haut `#F0C8A8`. Mimiken `Calm`, `Serious` (redet/ernst), `Concerned\|Serious` (Sorge), `Suspicious`, `Smile`, `Tired` | `julia` (Frau, jung; einzige ernste Frauenrolle – `ela_froh` dafür ungeeignet) |
| Chefredakteur Kettler (KE), um 35 | Redaktion des fiktiven Magazins | `standing/blazer-4` (Sakko Blau `#8DB3F2`, weißes Shirt), Kopf `Short 2`, Brille `Glasses 2`, Haut `#E3B08C`, kein Bart. Mimiken `Calm`, `Smile` (redet/froh), `Suspicious`, `Serious` | `niklas` (Mann, jung) |
| Anwalt Dr. Ruhnau (RU), um 60 | Anwalt von Frau Hellberg | `standing/crossed_arms-2` (schwarzes Oberteil der Pose, Hose Graublau `#6B7A8F`), Kopf `Gray Short`, Brille `Glasses 4`, Haut `#EBC29E`, kein Bart. Mimiken `Calm`, `Serious` (redet/ernst), `Smile`, `Suspicious` | `helmut` (Mann, älter) |
| Leserin (LE), um 25 | Kundin am Kiosk (heiterer Satz) | `standing/walking-3` (Kleidung der Pose), Kopf `Bun 2`, Haut `#B07552`. Mimiken `Calm`, `Cute` (redet/froh), `Awe` | `ela_froh` (Frau, jung, heiter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. A1: Leserin und Juliane blicken zum Kiosk (links); A2: Kettler blickt zum Schreibtisch (links); A3/G: Juliane (`_r`) und Ruhnau blicken einander an; Tafelszenen alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund** (auch `Concerned|Serious`); Mundzustände a/o/e nur in `JU_redet`, `KE_redet`, `RU_redet`, `LE_redet` (je links/rechts) und Lexi. 74 Figuren-PNGs in `../peeps/op_226/` (nicht im Repository, im Drive-Master).
- **Klischeeprüfung:** Kein „fieser“ Redakteur (sachliche Kleidung, freundliche bis nachdenkliche Mimik), keine Prothesen-Posen (`blazer-2` verworfen), keine Bärte; `pointing_finger-1` für den Anwalt verworfen (Oberteil nicht einfärbbar, Figur ganz schwarz). Keine Zuordnung von Herkunft oder Hautfarbe zu einer Rolle; die Leserin ist eine neutrale Nebenfigur.
- **Stimmen** nur aus dem Pool (niklas, helmut, ela_froh, julia). Vorfolge 225: william, laura_ruhig; 224: christian, hilde, lucy, stephan.
- **Namen:** Juliane, Hellberg, Kettler, Ruhnau – eindeutig deutsch, nicht in der Liste vergebener Namen, per `grep -rliw` in keiner Datei unter `youtube/` (07.10.2026; „Merle“ verworfen, in Folge 117 vergeben), in `namen_reserviert.txt` als „226: Hellberg, Juliane, Kettler, Ruhnau“ eingetragen. Gesprochen werden „Juliane Hellberg“ (Erzählerin 2×, Leserin 1×) und „Frau Hellberg“ (Erzählerin 3×); „Kettler“ und „Dr. Ruhnau“ nur auf Namensschild und Sachverhaltskarte.

**Abweichung von den letzten Folgen (223–225):** Posen `resting-1`, `blazer-4`, `crossed_arms-2`, `walking-3` – in 223 (`shirt-3`, `shirt-4`, `blazer-3`), 224 (`easing-2`, `resting-2`, `walking-1`, `blazer-1`, `robot_dance-3`, `pointing_finger-2`) und 225 (`shirt-2`, `crossed_arms-1`, `walking-2`) nicht verwendet; keine Polka Dots. Schauplätze **Kiosk mit Markise und Zeitschriftenwand**, **Redaktion mit Schreibtisch und Bildschirm**, **Kanzlei mit Bücherregal und Tür** – neu gegenüber 223 (Bank/Bürgschaft), 224 (Strafverfahren) und 225 (Staatshaftung). Die Kanzlei kehrt in G zurück, weil die Geschichte zur Mandantin zurückkehrt. Tageslicht-Cremegrund durchgehend.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Kiosk** `fall`→`erfunden` | ab 0,0 s Kiosk, Hefte, Titelblatt „Funkelblatt“ (Kopf), Leserin; Titelzeilen „Exklusiv! Juliane Hellberg spricht über ihre Trennung“ zum Wort; Pille „4 Seiten Interview“; Leserin staunt, Blase; Juliane tritt auf; Pillen „nie gesprochen“, „Jedes Wort ist erfunden.“, Stempel „erfunden“ auf dem Titel | Kiosk, Hefte aus Grundformen (`kiosk()`, `heft()`, `platzhalter()`) | `Fall · Am Kiosk: das neue Funkelblatt` (ab 0,0 s) → `· Exklusiv auf dem Titel` → `· Eine Leserin greift zu` → `· Juliane Hellberg hat nie gesprochen` | – |
| **A2 Redaktion** `redakt`→`ke1` | Schreibtisch mit Bildschirm, Textzeilen erscheinen (Tippen), Titelblatt an der Wand, Pille „Auflage: 400.000 Exemplare“; Kettler, Blase | Grundformen (`tisch()`, `feld()`), `heft()` | `Fall · In der Redaktion` → `· Auflage: 400.000 Exemplare` → `· Der Chefredakteur` | Tippen (`szene_226tippen_1`, Freesound CC0 546088) |
| **A3 Kanzlei** `kanzlei`→`bgh` | Bücherregal, Tür, Juliane und Ruhnau, Blasen; Frage, Nachbildung, Fundstelle als Pillen | `regal()`, `tuer()` | `Fall · In der Kanzlei` → `· Die Forderungen` → `Die Frage · Unterlassung, Widerruf, Geldentschädigung?` → `Die Frage · BGHZ 128, 1 (Caroline von Monaco)` | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | – |
| **C1 I. Anspruchsgrundlage** `norm`→`schema` | **Wortlautkarte § 823 Abs. 1 BGB**, Marker „sonstiges Recht“, „widerrechtlich“, „Ersatz“; Verweis Grundschema | tabler `scale`, `books` | `I. Anspruchsgrundlage · § 823 Abs. 1 BGB` → `› Wortlaut` → `› Grundschema` | – |
| **C2 Sonstiges Recht** `sonst`→`a11` | rosa Block, Haken „1954“, **Wortlautkarten Art. 2 Abs. 1 und Art. 1 Abs. 1 GG** | tabler `fingerprint`, `gavel`, `shield-check` | `› sonstiges Recht` → `› sonstiges Recht seit 1954` → `› Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG` | – |
| **C3 Rahmenrecht** `rahmen`, `abw` | gelber Block „ein Rahmenrecht“, Kreuz zum „nicht“, Haken Abwägung; Juliane und Kettler (beide Seiten) | tabler `fingerprint`, `scale` | `› ein Rahmenrecht` → `› Reichweite durch Abwägung` | – |
| **D II. Eingriff** `mund`→`eingriff` | gelber Block „Äußerungen in den Mund gelegt“, Haken Selbstbestimmung, Privatleben, grüner Block „Eingriff (+)“ | tabler `fingerprint`, `message-off`, `microphone`, `lock`, `circle-check` | `II. Eingriff · Was schützt das Persönlichkeitsrecht?` → … → `› Eingriff (+)` | – |
| **E1 III. Abwägung: Pressefreiheit** `presse`→`zitat` | **Wortlautkarte Art. 5 Abs. 1 Satz 2 GG**, Haken Unterhaltungspresse, Kreuze zum „nichts“/„nicht“; Kettler | tabler `news`, `message-off`, `quote-off` | `III. Rechtswidrigkeit · die Gegenseite: das Magazin` → … → `› unrichtiges Zitat nicht geschützt` | – |
| **E2 Abwägung und Verschulden** `vorrang`, `vors` | grüner Block „überwiegt“, Haken „rechtswidrig“, Haken „Vorsatz“; Juliane, Kettler | tabler `scale`, `writing` | `III. Rechtswidrigkeit › Persönlichkeitsrecht überwiegt` → `Verschulden · Vorsatz` | – |
| **F1 IV. Rechtsfolgen** `folgen`→`widerruf` | 1. Unterlassung (Norm zum Wort), 2. Widerruf; rechts Stopp-Hand, dann Titelblatt mit „Richtigstellung: Das Interview hat nie stattgefunden.“, Pille „Titelseite“; Ruhnau | tabler `hand-stop`, `heft()` | `IV. Rechtsfolgen · Welche Ansprüche?` → `› 1. Unterlassung` → `› 2. Widerruf` | – |
| **F2 3. Geldentschädigung** `geld`→`schutz` | Voraussetzungen, Subsumtion, Kreuz „kein Schmerzensgeld nach § 253 Abs. 2 BGB“ zum „kein“, gelber Block Schutzauftrag; Juliane | tabler `coin-euro`, `alert-triangle`, `ban`, `shield-check` | `› 3. Geldentschädigung` → … → `› 3. Schutzauftrag Art. 1, 2 GG` | – |
| **F3 3. Höhe** `hoehe`→`grenze` | Haken Genugtuung/Prävention, Block „Zwangskommerzialisierung“ zum Wort, Haken Gewinn/Hemmungseffekt, Kreuze Gewinnabschöpfung/Grenze; Kettler | tabler `coin-euro`, `heart-broken`, `chart-line`, `coins`, `hand-stop`, `scale` | `› 3. Höhe` → … → `› 3. Grenzen` | – |
| **G Ergebnis (Kanzlei)** `erg`→`echt` | Schauplatz A3; Haken Unterlassung/Widerruf, Geldentschädigung mit Gewinn, Pille BGHZ 128, 1; Juliane froh | tabler `coin-euro` | `Ergebnis · Unterlassung und Widerruf` → `› Geldentschädigung` → `› BGHZ 128, 1: Gewinn als Bemessungsfaktor` | – |
| **I Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (3 Stände) | – |
| **J Prüfschema** `sch`→`s5` | breite Karte, 8 Zeilen zum Wort | – | `Prüfschema` → je Gliederungspunkt | – |
| **K Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Markern | – | `Merksatz` | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen). **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („4 Seiten“, „400.000“, „15.11.1994“, „1954“, „§ 823 Abs. 1 BGB“, „§ 253 Abs. 2“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** ein Handlungsgeräusch (Tippen; Freesound CC0, Herkunft in `geraeusche_herkunft.json`); ein zunächst geplantes Anklopfen in A3 verworfen (Klopfen wäre nicht sichtbar).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Kiosk, Hefte, Tisch, Bildschirm, Regal, Tür programmatisch.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Das Wochenmagazin „Funkelblatt“ (Auflage 400.000) titelt: „Exklusiv! Juliane Hellberg spricht über ihre Trennung.“ Im Heft folgen 4 Seiten Interview mit der Schauspielerin über ihr Privatleben.
>
> Juliane Hellberg hat nie mit dem Magazin gesprochen; jedes Wort ist erfunden. Chefredakteur Kettler wusste das: Ihr Name auf dem Titel sollte mehr Hefte verkaufen.
>
> Frau Hellberg verlangt Unterlassung, Widerruf und eine Geldentschädigung.
>
> **Zu Recht? Und wonach richtet sich die Höhe der Geldentschädigung?**

Kein Fiktiv-Hinweis; die Nachbildung des Klassikers wird im Sprechtext genannt, beim echten Fall stehen Gericht, Datum, Aktenzeichen und Fundstelle auf der Pille.
