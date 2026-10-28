# Folge 040 · Berliner Testament: Die Falle nach dem ersten Todesfall (§ 2271 BGB) – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_040.py`](src/skript_040.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/Erbrecht, Themenplan-Format „Klassiker-Fall“. Übungsfall nach dem Plan-Hook („Nach dem Tod ihres Mannes will die Witwe den Sohn statt der Tochter als Schlusserben einsetzen“), Muster BGH IV ZR 72/11 und OLG Köln 2 W 169/25. Ablauf: Fall (Testament am Küchentisch, drei Jahre später, neues Testament, Streit) → Frage → Sachverhalt → I. Wirksamkeit (§§ 2265, 2267; § 10 Abs. 4 LPartG) → II. Inhalt (Wortlaut § 2269 Abs. 1, Einheitslösung, Abgrenzung Trennungslösung) → III. Wechselbezüglichkeit (Wortlaut § 2270 Abs. 1, erst Auslegung, Vermutung Abs. 2, Abs. 3) → IV. Bindung (zu Lebzeiten § 2271 Abs. 1/§ 2296; Wortlaut § 2271 Abs. 2 Satz 1; Ausweg Ausschlagung, §§ 1943, 1944) → V. Ergebnis → Gestaltungstipp Änderungsklausel → Ausblick § 2287 analog und Pflichtteil → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:33,2 (5.540 Zeichen, Grenze 6.200; Segment 15 nachvertont, 311 Zeichen). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Günter (GU), um 75 | Ehemann, schreibt das Testament, verstirbt (nur in Szenen zu seinen Lebzeiten) | `standing/shirt-4` (schwarzes Hemd, Hose Blau `#8DB3F2`), Kopf `No Hair 3` (graue Seiten), Brille `Glasses`, Haut `#EBC1A0`; Mimiken `Calm`, `Smile`, `Smile` (redet), `Serious` | `helmut` (Mann, älter) |
| Ingrid (IN), um 72 | Ehefrau, Überlebende, Vollerbin | `standing/easing-1` (Jacke Grün `#8FD694`, Oberteil Weiß, schwarze Hose), Kopf `Gray Medium` (Haar grau `#DCD7D7`), Brille `Glasses 4`, Haut `#F0C8A8`; `Calm`, `Smile`, `Smile`/`Driven` (redet), `Concerned|Serious`, `Serious`, `Suspicious`, `Solemn`, `Tired` | `hilde` (Frau, älter) |
| Petra (PE), um 45 | Tochter, Schlusserbin | `standing/shirt-3` (Hemd Rosa `#F6A5C0`), Kopf `Medium Bangs 2` (Haar braun), Haut `#E2B08C`; `Calm`, `Driven` (redet), `Concerned|Serious`, `Smile`, `Serious` | `lisa` (Frau, älter) |
| Uwe (UW), um 42 | Sohn, Schlusserbe, ohne Text | `standing/resting-2` (Hose Grau `#9C9CA6`), Kopf `Short 2`, Haut `#E2B08C`; `Calm`, `Smile`, `Suspicious` | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen nur aus dem Pool** helmut, hilde, lisa (timo nicht gebraucht, Uwe spricht nicht). Vorfolge 039: niklas, stephan, laura_klar – keine Überschneidung.
- **Namen** Günter, Ingrid, Petra, Uwe: eindeutig deutsche Aussprache, in keinem früheren `skript_*.py` vergeben (geprüft). Prüfung je Nennung in ABNAHME.md.
- **Tod zurückhaltend:** kein Sterbebett, kein Friedhof. Nach „Drei Jahre später stirbt Günter“ zeigen ein Wandkalender und Günters leerer blauer Sessel den Verlust; Günter erscheint danach nur noch in Tafelszenen, die die Zeit des gemeinsamen Testierens erklären (I., II. Wortlaut, III., IV. zu Lebzeiten, Gestaltungstipp). In „IV. Bindung nach Günters Tod“ steht Ingrid allein neben dem leeren Sessel.
- Grundansicht gespiegelt (blickt nach links zur Tafel bzw. zu Günter), `_r` blickt nach rechts (Günter zu Ingrid in Szene A, Ingrid zu Petra und Uwe in Szene B).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `GU_redet`, `IN_redet`, `IN_entschl`, `PE_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- Figuren-PNGs: `../peeps/op_040/` (74 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 039 (Anklageklausur, Elektronikmarkt), 038 (Körperverletzung), 034 (Einfahrt im Querschnitt). Hier neu: Küchentisch mit Testamentsblatt, Wohnzimmer mit leerem Sessel und Wandkalender; erstes Erbrechtsthema. Neue Posen gegenüber 037–039 (`shirt-4`, `easing-1` mit Jacke Grün, `shirt-3`, `resting-2`). Drei Wortlautkarten (§ 2269 Abs. 1, § 2270 Abs. 1, § 2271 Abs. 2 Satz 1), erstmals mit automatischem Zeilenumbruch (`wortlaut_auto()`); erste Folge mit Flussdiagramm (Einheitslösung).

## Szenen

Alle Szenen auf Cremegrund (Tag).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Am Küchentisch** `fall`–`i1` | Küche: Tisch (aus `karte`/`linienzug`), Günter links (blickt nach rechts), Ingrid rechts; Testament, Stift, Unterschrift | tabler: `heart` (Rosa), `file-text` (Weiß), `pencil` (Gelb), `signature` | `Fall · Das gemeinsame Testament` (ab 0,0 s) | Grundbild · verheiratet · Testament/Stift · „mit der Hand“ · Blase Günter · Unterschrift · Blase Ingrid | – |
| **B Drei Jahre später** `tod`–`frage2` | Wohnzimmer: Kalender, leerer Sessel, Ingrid; Petra und Uwe kommen dazu; neues Testament | tabler: `calendar`, `armchair` (Blau), `home` (Gelb), `heart-broken` (Rot), `file-pencil` | `Fall · Drei Jahre später` → `· Das neue Testament` → `· Die Frage` | Kalender/Sessel · erbt alles · Petra · zerstritten · Uwe · hilft · Blase Ingrid · neues Testament · Blase Petra · zwei Frage-Pillen | – |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 10 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | 1 | – |
| **D I. Wirksamkeit** `gt`–`formok` | Tafel, Günter und Ingrid | tabler: `heart`, `signature` | `I. Wirksamkeit …` → `› nur Ehegatten, § 2265 BGB` → `› Form, § 2267 BGB` | ✓ Ehegatten · LPartG · ✗ Paar · Form · 2 Zeilen · ✓ · Block | – |
| **E1 II. Inhalt** `inhalt`–`w2269b` | Wortlautkarte § 2269 Abs. 1 mit 6 Markern | tabler: `file-text` | `II. Inhalt durch Auslegung` → `› Auslegungsregel, § 2269 Abs. 1 BGB` | Titel · Karte · Marker | – |
| **E2 Einheitslösung** `einheit`–`trenn` | Flussdiagramm Günter → Ingrid (Vollerbin) → Petra · Uwe (Schlusserben); Ingrid und Petra | tabler: `home` | `II. Inhalt › Einheitslösung` → `› Abgrenzung: Trennungslösung` | Günter · Ingrid · Vollerbin · Petra/Uwe · Schlusserben · nach Ingrid · alles · Trennungslösung | – |
| **F1 III. Wechselbezüglichkeit** `p2270`–`w2270b` | Wortlautkarte § 2270 Abs. 1 (5 Marker) | tabler: `link` | `III. Wechselbezüglichkeit, § 2270 Abs. 1 BGB` | Karte · Marker · Pillen | – |
| **F2 Auslegung, Vermutung** `ausl`–`abs3` | Tafel, Günter und Ingrid | tabler: `gift`, `users` (Rosa), `link` | `III. › erst Auslegung` → `› Vermutung, § 2270 Abs. 2 BGB` → `› § 2270 Abs. 3 BGB` | 1. · 2. · ✓ Zuwendung · ✓ Kinder · Block · Abs. 3 | – |
| **G1 IV. Bindung zu Lebzeiten** `leb`–`allein` | Tafel, Günter und Ingrid | tabler: `file-certificate`, `file-x` | `IV. Bindung › zu Lebzeiten beider, § 2271 Abs. 1 BGB` | ✓ Widerruf · notariell · gegenüber · ✗ neues Testament | – |
| **G2 IV. Bindung nach Günters Tod** `tod2`–`gebunden` | Wortlautkarte § 2271 Abs. 2 Satz 1; Ingrid allein neben dem leeren Sessel | tabler: `armchair`, `lock` | `IV. Bindung › nach dem ersten Todesfall, § 2271 Abs. 2 BGB` | Karte · 4 Marker · ✓ gebunden · Erbvertrag | – |
| **H Ausschlagung** `aus`–`sonder` | Tafel, Ingrid und Petra | tabler: `hourglass`, `lock` (Rot) | `IV. Bindung › Ausweg Ausschlagung?` | Ausschlagung · Preis · Frist · Annahme · ✗ versperrt · Sonderfälle | – |
| **I V. Ergebnis** `erg`–`e2` | Tafel, Petra und Uwe | tabler: `file-x` | `V. Ergebnis` | ✗ unwirksam · soweit · Block je zur Hälfte | – |
| **J Gestaltungstipp** `klausel`–`kl4` | Tafel mit Musterklausel, Günter und Ingrid | tabler: `file-pencil` | `Gestaltungstipp · Änderungsvorbehalt` | Frage · Klausel · ✓ Umfang · ✓ ein Kind alles | – |
| **K1 Ausblick Schenkung** `schenk`–`bgh` | Tafel; das Haus wandert von Ingrid zu Uwe | tabler: `home` (bewegt) | `Ausblick · lebzeitige Schenkung, § 2287 BGB analog` | ✓ frei · Schenkung · Interesse · Petra · Block § 2287 | – |
| **K2 Pflichtteil** `pfl`, `pfl2` | Tafel, Petra und Uwe | tabler: `cash-banknote` (Grün) | `Ausblick · Pflichtteil beim ersten Erbfall, § 2303 BGB` | ✗ leer aus · ✓ Pflichtteil | – |
| **L Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Wechselbezüglichkeit je Verfügung` → `· erst Auslegung` | 6 Halte | – |
| **M Klausurschema** `sch`–`s9` | breite Karte, Aufbau Punkt für Punkt | – | `Klausurschema` | Titel · I. · II. · III. · Auslegung/Vermutung · IV. · 1.–3. · V. | – |
| **N Merksatz** `merke`, `mk2` | Lexi erklärt, Merksatz mit Markern | – | `Merksatz` | 4 Halte | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; Bewegung nur beim Haus (Schenkung an Uwe).
**Geräusche:** keine. Freesound-API über den Proxy gesperrt (HTTP 403); unter den vorhandenen CC0-Dateien in `sfx3` gibt es kein Stift-auf-Papier-Geräusch für das Schreiben des Testaments – nach der Vorgabe „lieber kein Geräusch als ein unpassendes“ bleibt die Folge ohne Handlungsgeräusch.
**Blasen:** wortgleich mit dem Gesprochenen.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Günter und Ingrid sind seit über 40 Jahren verheiratet. Günter schreibt mit der Hand und unterschreibt: „Wir setzen uns gegenseitig als Alleinerben ein. Nach dem Tod des Letzten von uns erben Petra und Uwe zu gleichen Teilen.“ Ingrid unterschreibt mit. Weitere Bestimmungen enthält das Testament nicht.
>
> Drei Jahre später stirbt Günter. Ingrid nimmt die Erbschaft an. Mit ihrer Tochter Petra hat sie sich inzwischen zerstritten, ihr Sohn Uwe hilft ihr im Alltag. Ingrid will ein neues Testament schreiben: Uwe soll alles bekommen.
>
> **Kann Ingrid ihr Testament noch wirksam ändern?**
