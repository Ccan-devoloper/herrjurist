# Folge 222 · Aktenauszug Assessorklausur: Die ersten 20 Minuten mit der Akte – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_222.py`](src/skript_222.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · Klausurtechnik, Format Schema, **ohne Fallprüfung**. Beispielfall nach dem Hook des Themenplans: Zweites Examen, Zivilrechtsklausur, fünf Stunden, 30 Seiten Akte und ein Bearbeitervermerk, der drei Teile erlässt (Rubrum, Streitwertfestsetzung, Rechtsbehelfsbelehrung). In der Akte: Herr Rehberg verlangt von Frau Pohlmann die Mietkaution (1.500 €) zurück, sie behält sie wegen Kratzern im Parkett.
Ablauf (Schritte mit Zeitachse, Minuten als Empfehlung): Fall → Frage → Sachverhalt → Überblick (Aktenauszug statt Sachverhalt, Zeitachse 0–5–15–20) → **1. Bearbeitervermerk, Min. 0–5** (zuerst lesen, Arbeitsauftrag, Rolle und Entwurf; erlassen, Stichtag) → **2. Erster Durchgang, Min. 5–15** (Beteiligte, Anträge; Chronologie und Daten) → Blick nach Klausurtyp (Zivilurteil § 313 Abs. 2 ZPO mit Wortlautkarte, unstreitig/streitig, Verweis Folge 18; Verwaltungsurteil § 117 Abs. 2 VwGO mit Wortlautkarte, § 74 VwGO; Anklage § 200 Abs. 1 StPO mit Wortlautkarte, Verweis Folge 39) → **3. Arbeitsblatt, Min. 15–20** (Muster als Tafel, Zeitplan mit Verweis Folge 45) → drei Fallen (Hinweise im Vermerk, Anlagen, Daten: Eingang/Zustellung) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
**Länge:** Hauptfilm 6:54,7 (5.593 gesprochene Zeichen). Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Hermine (HE), Ende 20 | Referendarin im zweiten Examen, durchgehende Figur | Pose `standing/easing-1` (lila offene Jacke, weißes Oberteil, schwarze Hose), Kopf `Long Curly`, Haut `#EDBF96`; Mimiken `Calm` (ruhig), `Serious` (liest), `Driven` (schreibt), `Suspicious` (denkt), `Smile` (froh), `Concerned|Serious` (redet: „Drei Teile erlassen …“) | `sabrina` (Frau, mittel) |
| Aufsicht (AU), um 60, ohne Namen | Klausuraufsicht | Pose `standing/resting-1` (graublauer Pullover), Kopf `No Hair 1`, Brille `Glasses 4`, Haut `#F0C8A8`; `Calm`, `Serious` (redet) | `william` (Mann, älter) |
| Herr Rehberg (RB), Mitte 30 | Kläger in der Akte (früherer Mieter) | Pose `standing/robot_dance-2` (schwarzer Pullover, dunkelblaue Hose `#3D4A6B`), Kopf `Flat Top`, ohne Bart, Haut `#D9A47E`; `Calm`, `Serious` (redet / ernst) | `marc` (Mann, mittel) |
| Frau Pohlmann (PO), um 60 | Beklagte in der Akte (frühere Vermieterin) | Pose `standing/crossed_arms-2` (schwarzes Oberteil, ockerfarbene Hose `#C9A66B`), Kopf `Gray Bun` (Haar `#C8C8C8`), Brille `Glasses 3`, Haut `#E8B48E`; `Calm`, `Suspicious` (redet / skeptisch) | `laura_ruhig` (Frau, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Klausurraum: Hermine am Tisch, die Aufsicht rechts blickt zu ihr; „In der Akte“: Herr Rehberg links blickt nach rechts zu Frau Pohlmann, sie nach links zu ihm; in allen Tafelfolien blicken die Figuren nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `HE_redet`, `HE_frohredet`, `AU_redet`, `RB_redet`, `PO_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots.
- **Stimmen nur aus dem Pool** (sabrina, william, marc, laura_ruhig); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Hermine, Rehberg, Pohlmann – nicht in der Koordinatorliste, in keiner früheren Folge (Suche im ganzen `youtube/`-Baum), in `namen_reserviert.txt` eingetragen („Hilgers“ verworfen: schon in ecA7). Die Aufsicht bleibt ohne Namen. Kein Genitiv eines Namens im Sprechtext.
- Figuren-PNGs: `../peeps/op_222/` (64 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 219 Fliesenhandel/Bad, 218 Chat/Wohnung, 217 Schule, 216 Gericht; 045 hatte zwei Kandidaten im Klausursaal mit Wanduhr. Hier ein Klausurraum mit **einer** Referendarin am Tisch, Akte als Ordner, Vermerk-Karte, danach eine eigene Szene „In der Akte“ (Wohnung als Symbol, Parkett mit Kratzern). Posen `easing-1`, `resting-1`, `robot_dance-2`, `crossed_arms-2` kommen in 216–219 nicht vor. Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Klausurraum** `fall`→`h1` | Boden, Tisch mit Akte, Wanduhr 9 Uhr, Aufsicht rechts | tabler:`desk` (Holz), `folder`→`folder-open` (Gelb), `clock-hour-9` | `Fall · Zweites Examen, 9 Uhr` → `Fall · Der Bearbeitervermerk` | ab 0,0 s vollständig · „30 Seiten Akte“ · Blase Aufsicht · „ganz hinten“ · Vermerk-Karte · „ist zu entwerfen“ · drei Kreuze (Rubrum, Streitwertfestsetzung, Rechtsbehelfsbelehrung) zum Wort · Blase Hermine | – |
| **A2 In der Akte / Frage** `vorn`→`frage2` | Akte vorn; Herr Rehberg und Frau Pohlmann, Wohnung, Parkett | tabler:`folder-open`, `home`; Parkett programmatisch (Kratzer bei „zerkratzt“) | `Fall · In der Akte` → `Fall · Die Frage` | Ordner · Herr Rehberg · Wohnung · Frau Pohlmann · „Mietkaution: 1.500 €“ · Blase Rehberg · Blase Pohlmann · Kratzer · Frage in zwei Teilen | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Überblick** `auszug`→`z3` | Tafel, Hermine | tabler:`folders`, `clock` | `Überblick · Aktenauszug statt Sachverhalt` → `Überblick › die ersten 20 Minuten` | Zeilen · Schriftsätze/Anlagen/Protokolle · „ordnen“ · Empfehlung · Zeitachse 5 / 10 / 5 Min. in drei Stufen | – |
| **D1 1. Bearbeitervermerk** `s1`→`her1` | Tafel, Hermine | tabler:`file-description`, `users`, `gavel` | `1. Bearbeitervermerk › zuerst lesen` → `› Rolle und Entwurf` | zuerst lesen · Arbeitsauftrag · Rollen nacheinander · Entwürfe nacheinander · Ring „Gericht“ | – |
| **D2 1. Bearbeitervermerk** `erlassen`→`stich` | Tafel, Hermine | tabler:`file-x`, `list-check`, `calendar-event` | `› was ist erlassen?` → `› Stichtag` | erlassen · alles andere · Tenor/Tatbestand/Entscheidungsgründe mit Haken · Stichtag · 30.9.2026 · Fristen | – |
| **E1 2. Erster Durchgang** `s2`→`ab` | Tafel, Herr Rehberg und Frau Pohlmann | tabler:`writing` | `2. Erster Durchgang › Beteiligte` → `› Anträge` | Stift · Kläger · Beklagte · Antrag Kläger · Antrag Beklagte | – |
| **E2 Chronologie** `chron`→`d4` | Tafel mit Zeitstrahl (nicht maßstäblich), Hermine | tabler:`calendar`, `inbox`, `send` | `2. Erster Durchgang › Chronologie und Daten` | Strahl · vier Daten nacheinander | – |
| **F1 Zivilurteil** `typ`→`rel` | Tafel, Wortlautkarte § 313 Abs. 2 S. 1 ZPO mit vier Markern, drei Spalten | tabler:`gavel`, `scale` | `Klausurtyp · Zivilurteil` → `Zivilurteil › Tatbestand, § 313 Abs. 2 ZPO` → `› unstreitig und streitig` | Karte · Marker · Spalten · Inhalte · Verweis Folge 18 | – |
| **F2 Verwaltungsurteil** `vwgo`→`frist` | Wortlautkarte § 117 Abs. 2 VwGO (gekürzt) | tabler:`building-bank`, `calendar-time` | `Verwaltungsurteil › § 117 Abs. 2 VwGO` → `› Zustellungen und Klagefrist` | Karte · zwei Marker · abgleichen · Bescheid/Widerspruch/Zustellungen · Monatsfrist | – |
| **F3 Anklage** `stpo`→`ankl` | Wortlautkarte § 200 Abs. 1 S. 1 StPO | tabler:`file-certificate`, `notes` | `Anklage › § 200 Abs. 1 StPO` → `› für jede Tat: wer, wann, wo` | Karte · fünf Marker · wer?/wann?/wo? · Verweis Folge 39 | – |
| **G 3. Arbeitsblatt** `s3`→`f45` | Tafel als Muster-Arbeitsblatt | tabler:`clipboard-list`, `hourglass` | `3. Arbeitsblatt › Muster` → `› Zeitplan` | Blatt · Auftrag · erlassen · Beteiligte/Anträge · Zeitstrahl · drei Spalten · weiter füllen · 4 Std. 40 Min. · Folge 45 | – |
| **H1 Fallen 1 und 2** `fallen`→`f2c` | Tafel, Hermine | tabler:`alert-triangle`, `file-description`, `paperclip` | `Fallen › 1. Hinweise im Vermerk` → `› 2. Anlagen` | Hinweis · unterstellen · erlassen/Denken · Anlagen nacheinander · mitlesen · 1.650 € | – |
| **H2 Falle 3** `f3`→`p167` | Tafel, Hermine | tabler:`inbox`, `send`, `coin-euro`, `hourglass` | `Fallen › 3. Daten: Eingang und Zustellung` → `› Verjährung, § 167 ZPO` | Eingang · Zustellung · rechtshängig · Prozesszinsen · Ring + Haken 20.1. · § 167 | – |
| **I Klausurtipp** `tipp` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand), tabler:`eye` | `Klausurtipp · den Vermerk noch einmal lesen` | Zeilen nacheinander | – |
| **J Schema** `sch`→`k3a` | breite Karte, I.–III. mit Unterpunkten und Zeitachse | – | `Schema · die ersten 20 Minuten` → `› I.` → `› II.` → `› III.` | Titel · sieben Zeilen · drei Zeitachsenstücke | – |
| **K Merksatz** `merke`, `m2` | Lexi erklärt (redet), vier Marker | – | `Merksatz` | Satz 1 · 2 Marker · Satz 2 · 2 Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** keine. Die einzige sichtbare Handlung (Blättern in der Akte) gehört zu den ausgeschlossenen Blättergeräuschen; Ablegen, Gehen oder Schreiben ist nicht zu sehen. Lieber kein Geräusch als ein unpassendes (Auftrag); `geraeusche_herkunft.json` dokumentiert das.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Zweites Examen, Klausur im Zivilrecht, 5 Stunden. Vor Hermine liegt eine Akte mit 30 Seiten. Ganz hinten steht der Bearbeitervermerk: „Die Entscheidung des Gerichts ist zu entwerfen. Rubrum, Streitwertfestsetzung und Rechtsbehelfsbelehrung sind erlassen.“ Hermine: „Drei Teile erlassen. Was genau muss ich also schreiben?“
>
> In der Akte verlangt Herr Rehberg von seiner früheren Vermieterin, Frau Pohlmann, die Mietkaution zurück: „Ich will meine Kaution zurück, 1.500 €.“ Frau Pohlmann: „Das Parkett ist zerkratzt. Die Kaution behalte ich.“
>
> **Was tust du in den ersten 20 Minuten mit der Akte?**
