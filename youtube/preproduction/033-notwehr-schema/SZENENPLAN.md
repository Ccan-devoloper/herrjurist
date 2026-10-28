# Folge 033 · Notwehr Schema § 32 StGB – so prüfst du die Notwehr – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_033.py`](src/skript_033.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis, Themenplan-Format „Schema“. Ein fiktiver Alltagsfall trägt das ganze Notwehrschema: Vor der Stadtbibliothek zerrt Torsten an Ulrikes Tasche; Ulrike warnt, der Passant Herr Kluge ruft die Polizei, Torsten zerrt fester, Ulrike tritt ihm gegen das Schienbein. Frage → Sachverhalt → § 223 kurz → Wortlautkarte § 32 I, II → 1. Notwehrlage (Angriff, gegenwärtig, rechtswidrig) → 2. Notwehrhandlung (gegen den Angreifer; Erforderlichkeit; mildere Mittel: Warnung, Festhalten, Polizei, Flucht; Androhung beim lebensgefährlichen Mittel; Gebotenheit im Überblick und am Fall) → 3. Verteidigungswille → Ergebnis/Rechtsfolge → Abgrenzung § 33 (Wortlautkarte) → Klausurtipp → Schema → Merksatz.
**Verhältnis zu Folge 011:** Dort scheitert Notwehr am Joggerin-Fall an der Gegenwärtigkeit, der Gegenfall wird nur in einem Satz bejaht. Hier wird das Schema vertieft: Erforderlichkeit mit konkreten milderen Mitteln, Warnung/Androhung, Gebotenheit, Verteidigungswille, Rechtsfolge und § 33. Keine Wiederholung der Gegenwärtigkeits-Problematik.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Ulrike (UL), Mitte 40 | Angegriffene, verteidigt ihre Tasche | `standing/easing-1`, Kopf `Medium Bangs`, Jacke Lila `#B8A9F5`, Oberteil Grün `#8FD694`, Haut `#E8B894`. Mimiken `Calm`, `Fear` (Schreck), `Driven` (hält fest; redet warnend), `Serious` (denkt), `Smile` (erleichtert), `Concerned|Serious` (besorgt) | `laura_klar` (Frau, mittel) |
| Torsten (TO), Mitte 20 | Angreifer | `standing/robot_dance-3` (ausgestreckter Arm greift die Tasche), Kopf `Short 4`, Oberteil Orange `#F9A66C`, Hose dunkel `#4A4A5E`, Haut `#F0C8A8`. Mimiken `Driven` (gierig), `Rage|Serious` (redet, zerrt), `Concerned|Serious` (Schmerz), `Tired` (humpelt davon), `Suspicious`, `Calm` | `niklas` (Mann, jung) |
| Herr Kluge (KL), um 70 | Passant, ruft die Polizei | `standing/shirt-4`, Kopf `No Hair 1`, Brille `Glasses 2`, Hemd schwarz (Pose), Hose Blau `#8DB3F2`, Haut `#E0B48E`. Mimiken `Calm`, `Concerned|Serious` (redet), `Fear` (erschrocken), `Serious` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links: Torsten zu Ulrike, alle Figuren rechts zur Tafel), `_r` blickt nach rechts (Herr Kluge und Ulrike in der Fallszene zu Torsten; Torsten beim Weghumpeln).
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimiken nur als `Concerned|Serious` bzw. `Rage|Serious`. Mundzustände a/o/e bei `UL_redet`, `TO_redet`, `KL_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (`blazer-1/2`, `shirt-1/2` bewusst nicht verwendet). 62 Figuren-PNGs in `../peeps/op_033/` (Drive-Master).
- Torstens Pose `robot_dance-3` ist eine Schwesterpose von Lexis `robot_dance-1`; Unterscheidung durch Kopf, orangefarbenes Oberteil, dunkle Hose und Namensschild.
- **Namen** mit eindeutig deutscher Aussprache, in keiner Vorfolge vergeben (Liste im Auftrag, dazu 030–032): Ulrike, Torsten, Kluge.
- **Stimmen** nur aus dem zugeteilten Pool (niklas, laura_klar, helmut; `sabrina` nicht gebraucht). Vorfolge 032 (christian, ela_warm, julia): keine Überschneidung. `helmut` zuletzt in 029, `laura_klar` in 027 – im Pool unvermeidbar. Lea nicht verwendet.

**Abweichung von den letzten Folgen:** 032 (Behörde/Verhältnismäßigkeit), 031 (Gemüseblatt-Fall), 030 (Zivilprozess), 029 (Reihenhausgärten), 011 (Uferweg mit Radfahrer). Hier neu: Fahrradständer vor einer Stadtbibliothek (Gebäude-Icon, Bücher, Fahrrad), drei neue Figuren mit neuen Posen (`easing-1`, `robot_dance-3`, `shirt-4`). Das Fahrrad ist nur Requisit (Ulrike schließt es auf), kein Radfahrer-Fall wie in 011.
**Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Vor der Stadtbibliothek** `fall`→`frage2` | Kluge links, Fahrrad, Ulrike (blickt nach rechts), Tasche, Torsten (blickt nach links), Bibliothek rechts; Torsten packt die Tasche, Ulrike hält fest und warnt, Kluge ruft die Polizei, Tritt (nur Pille + Schuh), Torsten humpelt davon | tabler:`building-community`, `books`, `lock-open`, `shoe`, `device-mobile`, `shield-check`; ph:`bicycle`, `handbag` | `Fall · Vor der Stadtbibliothek` (ab 0,0 s) → `Fall · Die Frage` | ≈ 30 | Fahrradschloss (`szene_033schloss_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,7 s | – | `Sachverhalt` | 1 | – |
| **C Tatbestand kurz** `tb`→`rw` | Tafel § 223, drei Haken, Block „gerechtfertigt durch Notwehr?“; Ulrike, Torsten | tabler:`shoe` | `A. Ulrike, § 223 Abs. 1 StGB › I. Tatbestand` → `› II. Rechtswidrigkeit` | ≈ 8 | – |
| **D Wortlautkarte § 32** `p32`→`aufbau` | Wortlaut § 32 I, II mit Markern; Aufbau in drei Blöcken | tabler:`shield-check` | `A. Ulrike › II. Rechtswidrigkeit › Notwehr, § 32 StGB` | ≈ 9 | – |
| **E 1. Notwehrlage** `lage`→`lage_ok` | Tafel a)–c); kleine Bühne Ulrike – Tasche – Torsten | ph:`handbag`, tabler:`clock` | `… › 1. Notwehrlage › a) Angriff / b) gegenwärtig / c) rechtswidrig` | ≈ 13 | – |
| **F 2. Notwehrhandlung** `handl`→`geeig` | Tafel a) gegen den Angreifer, b) Erforderlichkeit (BGH-Formel), geeignet | tabler:`shoe` | `… › 2. Notwehrhandlung › a) gegen den Angreifer` → `› b) erforderlich` | ≈ 9 | – |
| **G Milderes Mittel?** `milder`→`erf_ok` | Tafel mit vier Kreuzen; Icon-Spalte Warnung, Festhalten, Polizei/Uhr, Fliehen; Ulrike denkt | tabler:`speakerphone`, `hand-grab`, `clock`, `run`; ph:`siren` | `… › b) erforderlich: milderes Mittel?` | ≈ 13 | – |
| **H Androhung** `droh` | Tafel; Warnsymbol, **keine Waffe im Bild** | tabler:`alert-triangle` | `… › b) erforderlich: Androhung` | ≈ 5 | – |
| **I Gebotenheit (Überblick)** `geboten`→`fg_rf` | Tafel mit vier Fallgruppen und Fundstellen; 2×2-Icons | tabler:`mood-kid`, `scale`, `flame`, `home-heart` | `… › c) geboten` | ≈ 13 | – |
| **J Gebotenheit bei Ulrike** `geb_ok`→`geb_erg` | drei Haken, Block „geboten (+)“; Ulrike, Torsten | – | `… › c) geboten: bei Ulrike` | ≈ 7 | – |
| **K 3. Verteidigungswille** `wille`→`wille_ok` | Tafel; Flamme „Wut“, Tasche; Ulrike | tabler:`flame`, ph:`handbag` | `A. Ulrike › Notwehr, § 32 StGB › 3. Verteidigungswille` | ≈ 7 | – |
| **L Ergebnis** `ergebnis`→`duld` | Block „Notwehr: nicht rechtswidrig“, Haken, Kreuz „keine Notwehr gegen Notwehr“ | tabler:`shield-check`, `ban` | `A. Ulrike › Ergebnis` | ≈ 5 | – |
| **M Abgrenzung § 33** `p33`→`p33d` | Wortlautkarte § 33 mit Markern; drei Gesichter-Icons | tabler:`mood-nervous`, `mood-sad`, `mood-surprised` | `Abgrenzung · Notwehrexzess, § 33 StGB` | ≈ 9 | – |
| **N Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Schwerpunkt Erforderlichkeit` | ≈ 9 | – |
| **O Klausurschema** `sch`→`k4` | breite Karte, progressiv | – | `Klausurschema` | 11 | – |
| **P Merksatz** `merke`→`m3` | Lexi erklärt, drei Marker | – | `Merksatz` | ≈ 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Handlung als Zustandswechsel (Tasche an der Schulter – zwischen beiden – wieder bei Ulrike; Torsten am Platz – humpelt davon).
**Geräusche:** ein Handlungsgeräusch (Fahrradschloss), CC0, Kopie aus Folge 027 (Freesound-API gesperrt), Herkunft in `geraeusche_herkunft.json`. Kein Trittgeräusch (Gewalt zurückhaltend).
**Gewalt zurückhaltend:** kein Schlag/Tritt im Bild, kein Blut, keine Waffe; der Androhungsabschnitt zeigt nur ein Warnsymbol.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 32 I, II und § 33 vollständig, wörtlich nach gesetze-im-internet.de mit Normangabe, beide wörtlich vorgelesen; Marker synchron zum gesprochenen Wort.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Dienstagnachmittag vor der Stadtbibliothek: Torsten (Mitte 20) packt die Tasche von Ulrike (Mitte 40) und zerrt daran: „Her mit der Tasche!“ Ulrike hält sie mit beiden Händen fest und warnt: „Lass los, sonst wehre ich mich!“ Der Passant Herr Kluge ruft die Polizei; sie kann erst nach einigen Minuten da sein.
>
> Torsten zerrt nur noch fester. Ulrike tritt ihm kräftig gegen das Schienbein, um ihre Tasche zu behalten. Torsten lässt los und humpelt davon; am Schienbein bekommt er einen Bluterguss.
>
> Annahme: Torsten ist erwachsen und erkennbar bei klarem Verstand. Ulrike hat ihn vorher nicht provoziert.
>
> **Hat Ulrike sich wegen Körperverletzung strafbar gemacht?**
