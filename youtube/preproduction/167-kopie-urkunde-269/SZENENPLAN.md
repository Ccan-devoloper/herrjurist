# Folge 167 · Kopie als Urkunde? Scan, PDF & § 269 StGB – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_167.py`](src/skript_167.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · StGB BT, Themenplan-Format „Streitstand“ (Thumbnail-Vorlage „Lern · STREIT“). Voraussetzungsfolge 137 (Urkundenbegriff) nur in einem Satz verwiesen, die Urkundenmerkmale werden nicht wiederholt. Fall nach dem Plan-Hook: Janosch (20) scannt sein Abiturzeugnis (2,8), ändert am Rechner die Note in 1,8 und schickt das PDF per E-Mail an Frau Hagemann (Personalabteilung); Variante: Ausdruck per Post als Kopie. Ablauf: Fall → Frage → Sachverhalt → einfache Fotokopie (BGH-Formel) → Streitstand → zwei Ausnahmen und eine Grenze (Anschein des Originals, gefälschtes Original/beglaubigte Kopie, Collage) → Datei: § 269 Abs. 1 (Wortlautkarte), hypothetischer Urkundenvergleich → Scan oder digitales Original (BGH) → PDF-Zeugnis (OLG Celle), Gegenansicht, § 270 (Wortlautkarte) → Lösung PDF → Lösung Ausdruck, Ausblick Betrug → Merktabelle Original/Kopie/Scan → Klausurtipp → Merksatz. Darstellungsmuster für Dateien und Rechner wie Folge 107 (Computerbetrug): Rechner und Datei als Requisit, keine Bildschirm-Inhalte realer Programme.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Janosch (JA), 20 | Bewerber | `standing/resting-1` (Pullover Rot `#F07A6A`, schwarze Hose, Sneaker), Kopf `Short 1`, Haar `#5A3A22`, Haut `#E8B990`; Mimiken `Calm`, `Smile` (auch redet), `Suspicious`, `Serious`, `Concerned|Serious`, `Driven`, `Solemn` | `marc` (Mann, mittel) |
| Frau Hagemann (HA), um 45 | Personalabteilung | `standing/blazer-1` (Blazer Lila `#B8A9F5`, schwarzes Oberteil, Hose Dunkelgrau `#3A3A44`; die Pose hat eine Beinprothese – bewusst bei einer Nicht-Täterin, keine Karikatur), Kopf `Long`, Haar `#3B2A20`, Brille `Glasses 2`, Haut `#D9A47E`; Mimiken `Calm`, `Smile` (redet), `Serious`, `Suspicious` | `sabrina` (Frau, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Kontaktbild (`figuren_kontaktbogen.png`): ohne Suffix gespiegelt (blickt nach links, zur Tafel), `_r` Original (blickt nach rechts; Fallszene: Janosch zu Schreibtisch und Drucker). Frau Hagemann blickt in A2 nach links zu ihrem Rechner.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `JA_redet`, `HA_redet` (je links/rechts) und Lexi. Keine Bärte. Janosch als gewöhnlicher junger Erwachsener, keine „fiese“ Täterfigur. 46 Figuren-PNGs in `../peeps/op_167/` (Drive-Master). Kein Mensch als Icon.
- **Namen** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste und per `grep -rlw` in keiner Text-/Codedatei unter `youtube/` (0 Treffer): **Janosch**, **Hagemann**. „Jannik“ verworfen (Folge 010), „Mattis“ verworfen (englische Lesart möglich). Nie im Genitiv mit -s.
- **Stimmen** nur aus dem Pool: marc (Janosch), sabrina (Frau Hagemann); william und laura_ruhig nicht eingesetzt.

**Abweichung von den letzten Folgen** (Posen 162–164 geprüft: `easing-1`, `easing-2`, `blazer-4`, `closed_legs-1`, `walking-3`, `robot_dance-2`, `shirt-3`): `resting-1` und `blazer-1` dort nicht verwendet; kein Polka-Dots-Muster. Schauplätze neu: Zimmer mit Schreibtisch, Laptop, Scanner und Drucker; Personalabteilung mit Rechner. **Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Zu Hause** `fall`→`mail` | Janosch (ab 0,0 s mit Namensschild) am Schreibtisch mit Laptop; Pillen „20 Jahre“, „Bewerbung als Sachbearbeiter“; Zeugnis-Karte „Abiturzeugnis · Note“ mit „2,8“; Scanner „eingescannt“; Note wird rot „1,8“, Pille „am Rechner geändert“; Blase Janosch; PDF-Symbol „als PDF gespeichert“; E-Mail-Umschlag fährt vom Laptop weg, Pille „per E-Mail an Frau Hagemann“ | tabler:`desk`, `scan`, `file-type-pdf`; fluent:`laptop`, `e-mail` | `Fall · Die Bewerbung` (ab 0,0 s) → `… Das Zeugnis: Note 2,8` → `… Der Scan` → `… Note am Rechner geändert` → `… PDF per E-Mail` | Scanner (`szene_167scan_1`), Tastatur beim Ändern (`szene_167tasten_1`) |
| **A2 Personalabteilung** `h1`→`frage2` | Frau Hagemann am Rechner „PDF: Note 1,8“, Blase; Variante: Trennlinie, Janosch links mit Drucker, Umschlag „Kopie“ wandert zum Schreibtisch; Frage-Pillen | tabler:`desk`; fluent:`desktop-computer`, `printer`, `envelope` | `Fall · In der Personalabteilung` → `… Variante: Ausdruck per Post` → `… Die Frage` | Drucker (`szene_167drucker_1`) |
| **B Sachverhalt** `sv` | Karte vollständig | – | `Sachverhalt` | – |
| **C Fotokopie** `begriff`→`grund2` | Verweis Urkundenbegriff, BGH-Formel (Kasten), zwei Kreuze, „nur bildlich“ | fluent:`page-facing-up`, `printer`; tabler:`copy` | `Voraussetzung › Urkundenbegriff` → `Fotokopie › Grundsatz` → `Fotokopie › keine Urkunde` | – |
| **D Streitstand** `streit`→`hm` | Gegenansicht (lila), Rechtsprechung und große Teile der Lehre (grün) | fluent:`balance-scale`, `books`; tabler:`circle-check` | `Streitstand › Fotokopie als Urkunde?` → `… › Gegenansicht: grundsätzlich Urkunde` → `… › Rechtsprechung: keine Urkunde` | – |
| **E Ausnahmen, Grenze** `aus`→`collage` | 1. Anschein des Originals; 2. gefälschtes Original, beglaubigte Kopie (Examenszeugnis); Kasten Collage | fluent:`page-with-curl`, `page-facing-up`, `graduation-cap`, `scissors`; tabler:`certificate` | `Fotokopie › Ausnahmen` → `Ausnahme 1 › …` → `Ausnahme 2 › …` → `Ausnahme 2 › beglaubigte Kopie` → `Grenze › Collage` | – |
| **F Datei, § 269** `datei`→`hyp` | Datei nicht verkörpert; **Wortlautkarte § 269 Abs. 1** (4 Marker); gelber Block hypothetischer Vergleich | tabler:`file-type-pdf`; fluent:`balance-scale`, `page-facing-up` | `Scan und PDF › Datei: nicht § 267` → `§ 269 Abs. 1 StGB › Wortlaut` → `§ 269 › hypothetischer Urkundenvergleich` | – |
| **G1 Scan oder digital** `bgh`→`digorig` | Kasten Scan (rot, (−)), Kasten digitales Original (grün, in Betracht) | tabler:`scan`, `photo-scan`; fluent:`mobile-phone` | `§ 269 › Scan oder digitales Original?` → `… Scan eines Papierdokuments: (−)` → `… digitales Original: in Betracht` | – |
| **G2 PDF-Zeugnis** `olg`→`p270` | OLG Celle (grün), Gegenansicht (lila), **Wortlautkarte § 270** | fluent:`e-mail`, `books`, `robot` | `Streit › PDF-Zeugnis: nur Reproduktion` → `Streit › Gegenansicht: Datenurkunde` → `§ 270 StGB › Datenverarbeitung` | – |
| **H1 Lösung PDF** `loes`→`l3` | Zeugnis-Karte als Kopie, Kreuze § 267/§ 269, Kasten digitales Original | tabler:`file-type-pdf`, `x`, `photo-scan`; fluent:`laptop` | `Lösung › PDF per E-Mail` → `… PDF: § 267 (−)` → `… PDF: § 269 (−)` → `… anders bei digitalem Original` | – |
| **H2 Lösung Ausdruck** `l4`→`betrug` | Kreuze, Ausblick Betrug (hellgelb) | fluent:`printer`, `envelope`, `briefcase` | `Lösung › Variante: Ausdruck als Kopie` → `… kein gefälschtes Original` → `Ausblick › Betrug, § 263 StGB` | – |
| **I Merktabelle** `tab`→`t3` | breite Karte, Zeilen Original / Kopie / Scan progressiv | fluent:`page-facing-up`, `printer`; tabler:`file-type-pdf` | `Merktabelle` → `… › Original` → `… › Kopie` → `… › Scan und PDF` | – |
| **J Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Was kommt beim Empfänger an?` → `… Gefälschtes Original dahinter?` | – |
| **K Merksatz** `merke`, `m2` | Lexi erklärt, Marker | – | `Merksatz` | – |

**Merktabelle statt Prüfschema:** Der Themenplan verlangt für dieses Streitstand-Format eine Merktabelle Original / Kopie / Scan; sie baut sich Zeile für Zeile am gesprochenen Wort auf (progressiv wie ein Schema).
**Blasen:** Stil C (`bausteine.blase`), Schwanzspitze außerhalb der Blase schräg über dem Mund (Standard `kopfziel`). **Zahlen** in Blasen, Tafeln und Pillen als Ziffern („2,8“, „1,8“, „20 Jahre“, „§ 269“).
**Übergänge:** stumme Schiebeblenden zwischen 14 Folien; innerhalb harte Schnitte und Pops; Bewegungen: E-Mail fährt vom Laptop weg (A1), Umschlag „Kopie“ wandert in die Personalabteilung (A2).
**Wortlautkarten:** § 269 Abs. 1 (vollständig, „daß“ wie amtlich; vorgelesen bis „gebraucht“) und § 270 (vollständig vorgelesen), nach gesetze-im-internet.de (Abruf 04.10.2026).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji Flat (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (**CC BY 4.0**, Namensnennung in `beschreibung.txt`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Janosch ist 20 und bewirbt sich um eine Stelle als Sachbearbeiter. In seinem Abiturzeugnis steht die Note 2,8. Er scannt das Zeugnis ein und ändert am Rechner die Note in 1,8. Er speichert die Datei als PDF und schickt sie per E-Mail an Frau Hagemann aus der Personalabteilung.
>
> Variante: Janosch druckt die bearbeitete Datei aus und schickt den Ausdruck per Post, als Kopie seines Zeugnisses.
>
> **Hat sich Janosch nach § 267 StGB oder nach § 269 StGB strafbar gemacht?**
