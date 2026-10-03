# Folge 120 · Gesamtschuld §§ 421, 426 BGB: Einer zahlt für alle – und dann? – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_120.py`](src/skript_120.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Zivilrecht/Schuldrecht AT, Themenplan-Format „Schema“. Fall nach dem Plan-Hook („Drei Mitbewohner haften für die Stromrechnung – der Versorger holt sich alles von einem“): Insa, Lars und Rieke wohnen in einer WG; alle drei haben den Stromvertrag unterschrieben. Rieke zieht aus und ist zahlungsunfähig. Die Jahresabrechnung ergibt 900 € Nachzahlung; der Versorger verlangt alles von Insa, sie zahlt. Insa verlangt 450 € von Lars, Lars will nur 300 € zahlen.

Ablauf: Fall (WG-Küche, Telefonat mit dem Versorger, Insa und Lars) → Frage → Sachverhalt → zwei Ebenen → I. Außenverhältnis: 1. Entstehen (Wortlautkarte § 421 S. 1; § 427, § 840 Abs. 1, Gleichstufigkeit; im Fall) → 2. Erfüllung § 422 Abs. 1, Einzelwirkung § 425 → II. Innenverhältnis: 1. Ausgleich (Wortlautkarte § 426 Abs. 1 S. 1, Abrede als Variante) → 2. Ausfall (Wortlautkarte § 426 Abs. 1 S. 2) → 3. Legalzession (Wortlautkarte § 426 Abs. 2 S. 1, §§ 412, 401) → Verhältnis Abs. 1/Abs. 2 → Rechnung → Ergebnis → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Verhältnis zu Folge 089 (Abtretung):** Voraussetzungsfolge; die Legalzession wird nur über §§ 412, 401 („wie bei der Abtretung“) angeknüpft, die Abtretungsvoraussetzungen werden nicht wiederholt. **Zu Folge 099:** Der Schuldbeitritt als Entstehungsgrund wird nicht erneut erklärt; hier steht die Wirkung der Gesamtschuld im Mittelpunkt.
**Länge:** Hauptfilm 6:10,5 (Sprachspur 370,5 s, 5.275 Zeichen Skript); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Insa (IN), um 25 | Mitbewohnerin, zahlt die 900 €, verlangt Ausgleich | `standing/pointing_finger-1` (schwarzes Langarmoberteil, schwarze Hose und Stiefel der Pose; zeigt mit dem Finger), Kopf `Medium 2`, Haut `#F0C8A8`; `Calm`, `Serious` (redet), `Smile`, `Concerned|Serious`, `Suspicious`, `Awe` | `ela_froh` (Frau, jung) |
| Lars (LA), um 26 | Mitbewohner, soll ausgleichen | `standing/crossed_arms-1` (Pullover Blau `#8DB3F2`, schwarze Hose, verschränkte Arme), Kopf `Short 3`, Haar `#6B4A32`, Haut `#E3B48E`; `Calm`, `Serious` (redet), `Smile`, `Suspicious`, `Concerned|Serious` | `niklas` (Mann, jung) |
| Rieke (RI), um 24 | ausgezogene, zahlungsunfähige Mitbewohnerin (spricht nicht) | `standing/walking-2` (schwarzes T-Shirt, Hose Lila `#B8A9F5`, Schrittpose), Kopf `Medium Straight`, Haut `#F2D3B8`; `Calm`, `Concerned|Serious`, `Tired` | – |
| Sachbearbeiter des Stromversorgers (SB), um 60 | Gläubigerseite, Funktionsrolle ohne Namen, Namensschild „Stromversorger“ | `standing/blazer-4` (Blazer Grün `#8FD694`, weißes Oberteil, schwarze Hose), Kopf `Gray Short`, Brille `Glasses 3`, Haut `#D9A47E`; `Serious` (redet), `Calm`, `Smile` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Koordinatorliste und per `grep -rliw` in keinem Skript, Szenenplan, Abnahmebogen, JSON, CSV oder TXT unter `youtube/` (03.10.2026, ohne die Altordner 15/17/19): Insa, Lars, Rieke („Greta“, „Jonas“, „Lina“ wegen früherer Folgen verworfen). Kein Genitiv eines Namens im Sprechtext („die Hälfte des Ausfalls von Rieke“). Im Sprechtext „Wohngemeinschaft“ statt „WG“ (Aussprache), auf Tafeln „WG“.
- **Stimmen nur aus dem Pool** (niklas, helmut, ela_froh, julia): `ela_froh`, `niklas`, `helmut`; `julia` (in 109, 112, 114 besetzt) nicht eingesetzt, Rieke spricht nicht. Vorfolge 119 ohne diese Besetzung.
- Präfixe `IN_`/`LA_`/`RI_`/`SB_` (nie `ER_`). Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Küche: alle blicken nach links (Insa zum Kühlschrank/Telefon, Rieke an der Tür); Telefonat: Sachbearbeiter nach rechts zu Insa, Insa nach links; Insa und Lars: Insa nach rechts zu Lars, Lars nach links zu ihr; Ergebnis ebenso; Tafelszenen nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimik nur als `Concerned|Serious`. Mundzustände a/o/e nur bei `IN_redet`, `LA_redet`, `SB_redet` (je links/rechts) und Lexi. Keine weiteren Menschen im Bild.
- **Kein Klischee:** Rieke (zahlungsunfähig) wird neutral gezeigt, keine Schuldzuweisung; der Versorger ist sachlich (keine „fiese“ Gläubigerfigur, kein reales Logo, kein Firmenname). Keine Bärte, keine Prothesen-Posen, keine Karikatur.
- **Abwechslung:** Posen nicht aus 117 (`shirt-4`, `pointing_finger-2`), 118 (`robot_dance-3`, `resting-1`, `crossed_arms-2`), 119 (`easing-2`, `blazer-3`) und nicht aus der WG-Folge 107 (`shirt-3`, `resting-2`, `blazer-3`); keine Polka Dots. Kontaktbögen 116, 117, 119 verglichen (`out/vergleich_*.png`).
- Figuren-PNGs: `../peeps/op_120/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 117 (Klausurrückgabe, Schreibtisch), 118 (Stadthalle/Gericht), 119 (Reichsgericht/Bundesgerichtshof-Kärtchen). Hier neu: WG-Küche mit Kühlschrank, Glühbirne, Stromvertrag mit drei Unterschriften, Umzugskarton und Tür; Telefonat mit dem Versorger (Schreibtisch, Blitz-Symbol); Diagramm der zwei Ebenen; Rechentafel. Die WG aus Folge 107 (Flur, Geldautomat) wird nicht wiederholt: anderer Raum, andere Figuren und Kleidung. Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 WG-Küche** `fall`–`anruf` | ab 0,0 s: Insa, Lars, Rieke mit Namensschildern, Kühlschrank, Glühbirne; Stromvertrag mit Unterschriften Insa/Lars/Rieke zum Wort; Rieke an der Tür mit Karton („zieht aus“), „zahlungsunfähig“; Jahresabrechnung „Nachzahlung: 900 €“; Telefon klingelt bei Insa, „Der Versorger ruft an“ | tabler:`fridge`, `door-exit`; fluent:`light-bulb`, `high-voltage`, `package`, `receipt`, `telephone-receiver` | `Fall · Die Wohngemeinschaft` → `Fall · Rieke zieht aus` → `Fall · Die Jahresabrechnung` | `szene_120tuer_1` beim Auszug, `szene_120telefon_1` bei „Der Versorger meldet sich“ |
| **A2 Telefonat** `sb1`–`zahlt` | Sachbearbeiter am Schreibtisch, Blase „Die 900 € verlangen wir / vollständig von Ihnen.“; Insa mit Telefon, Blase „Von mir allein? / Wir waren doch zu dritt!“; Geldschein, Pfeil zum Versorger, „Insa zahlt 900 €“ | fluent:`high-voltage`, `telephone-receiver`, `euro-banknote`; tabler:`desk`, `phone` | `Fall · Der Versorger verlangt alles` → `Fall · Insa zahlt` | – |
| **A3 Insa und Lars, Frage** `lars`–`frage2` | Blase Insa „Du schuldest mir die Hälfte, / 450 Euro.“; Blase Lars „Wir waren drei. Ich zahle / dir 300, mehr nicht.“ (Geldschein); Fragepillen | tabler:`fridge`; fluent:`euro-banknote` | `Fall · Insa verlangt Ausgleich` → `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig (36 px), ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Zwei Ebenen** `eben`–`innen` | Diagramm Versorger (Gläubiger) → Insa/Lars/Rieke; Außen-Pfeile, Innen-Pfeile rot | tabler:`hierarchy-2`, `arrows-right-left`; fluent:`high-voltage` | `Gesamtschuld · Zwei Ebenen` → `› I. Außenverhältnis` → `› II. Innenverhältnis` | – |
| **D1 § 421** `w421`, `m1`–`m4` | Wortlautkarte § 421 S. 1 (4 Marker zum Merkmal), drei Zeilen zum Wort | tabler:`users`, `circle-check`, `hand-finger`; fluent:`euro-banknote` | `I. Außenverhältnis › 1. Entstehen, § 421 BGB` | – |
| **D2 Entstehungsgründe** `p427`–`gleich` | Vertrag § 427, Gesetz § 840 Abs. 1, Gleichstufigkeit (VII ZR 7/11 Rn. 18) | tabler:`file-text`, `scale`, `equal` | `I. 1. Entstehen › gemeinsamer Vertrag, § 427 BGB` → `› Gesetz, § 840 Abs. 1 BGB` → `› Gleichstufigkeit` | – |
| **D3 Im Fall** `sub1`, `sub2` | Vertragskarte, ✓ alle 3 unterschrieben, ✓ teilbar, Block „Gesamtschuldner …“ | tabler:`signature`; fluent:`high-voltage` | `I. 1. Entstehen › im Fall` → `› Gesamtschuld (+)` | – |
| **E § 422, § 425** `p422`–`p425` | Gesamtwirkung der Erfüllung, Block „Lars und Rieke sind frei“, Einzelwirkung | fluent:`euro-banknote`; tabler:`user-check`, `user` | `I. Außenverhältnis › 2. Erfüllung, § 422 Abs. 1 BGB` → `I. 2. Erfüllung › andere Tatsachen, § 425 BGB` | – |
| **F § 426 Abs. 1 S. 1** `w426`–`abrede` | Wortlautkarte (3 Marker), „900 € : 3“, je 300 €, Variante Abrede (XII ZR 53/08 Rn. 9) | tabler:`arrows-right-left`, `coins`, `users`, `chart-pie`, `home` | `II. Innenverhältnis › 1. Ausgleich, § 426 Abs. 1 S. 1 BGB` → `II. 1. Ausgleich › anderweitige Bestimmung` | – |
| **G § 426 Abs. 1 S. 2** `w426s2`–`halb` | Wortlautkarte (2 Marker), ✗ Rieke nicht zu erlangen, je + 150 € | tabler:`user-x`, `chart-pie`; fluent:`package` | `II. Innenverhältnis › 2. Ausfall, § 426 Abs. 1 S. 2 BGB` | – |
| **H § 426 Abs. 2 S. 1** `w426b`–`sich` | Wortlautkarte (3 Marker), „Versorger gegen Lars“ → „Insa gegen Lars“, §§ 412, 401 | tabler:`transfer`, `file-text`, `shield` | `II. Innenverhältnis › 3. Legalzession, § 426 Abs. 2 BGB` → `II. 3. Legalzession › Sicherheiten, §§ 412, 401 BGB` | – |
| **I Verhältnis** `neben`, `neben2` | zwei Blöcke Abs. 1 / Abs. 2, „selbständig nebeneinander“ (IX ZR 216/20 Rn. 19, XI ZR 234/11 Rn. 20) | tabler:`arrows-split-2`, `equal` | `II. Innenverhältnis › Verhältnis von Abs. 1 und Abs. 2` | – |
| **J Rechnung** `rech`–`r5` | Zeile für Zeile 900 / 300 / 300 + 150, Block „Lars an Insa: 450 €“, Insa trägt 450 € | tabler:`calculator`; fluent:`euro-banknote`, `money-bag` | `Rechnung · Wer zahlt wem wie viel?` → `Rechnung · Lars schuldet 450 €` | – |
| **K Ergebnis** `erg`–`la2` | Bühne: Ergebnisblock, Zeile § 426 Abs. 1 und 2, Pillen Abs. 1/Abs. 2 zum Wort, ✗ „300 € reichen nicht“, Blase Lars „Na gut, dann 450.“, Geldschein | tabler:`fridge`; fluent:`euro-banknote` | `Ergebnis · Lars schuldet Insa 450 €` | – |
| **L Klausurtipp** `tipp`–`tipp4` | hellgelbe Tafel, Lexi warnt; IX ZR 216/20 Rn. 19, VI ZR 200/15 Rn. 11 | Warnsymbol (Streamline Freehand) | `Klausurtipp · Regress auf beiden Wegen` | – |
| **M Klausurschema** `sch`–`k2c` | breite Karte, I. 1.–2., II. 1.–3. Zeile für Zeile | – | `Klausurschema` → `› I. Außenverhältnis` → `› II. Innenverhältnis` | – |
| **N Merksatz** `merke`–`mk3` | Lexi erklärt, drei Sätze, drei Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; keine Bewegungsanimation.
**Blasen:** Stil C (`bausteine.blase`), wortgleich mit dem Gesprochenen, Beträge als Ziffern („900 €“, „450 Euro“, „300“).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji Flat (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (**CC BY 4.0**, Namensnennung in `beschreibung.txt`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Insa, Lars und Rieke wohnen zusammen in einer Wohngemeinschaft. Den Stromliefervertrag mit dem Versorger haben alle drei unterschrieben. Im Frühjahr zieht Rieke aus; sie ist inzwischen zahlungsunfähig.
>
> Die Jahresabrechnung ergibt eine Nachzahlung von 900 Euro. Der Versorger verlangt den ganzen Betrag von Insa, und Insa zahlt die 900 Euro.
>
> Danach verlangt Insa von Lars 450 Euro. Lars meint: „Wir waren drei. Ich zahle dir 300, mehr nicht.“
>
> **Durfte der Versorger alles von Insa verlangen, und wie viel muss Lars erstatten?**
