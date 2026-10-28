# Folge 044 · Verwaltungsakt § 35 VwVfG: Alle Merkmale in sechs Minuten – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_044.py`](src/skript_044.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen, Themenplan-Format „Schema“. Ein Übungsfall nach dem Hook des Themenplans trägt die sechs Merkmale: Frau Wiegand (Kaffeewagen auf dem Marktplatz) erhält einen ablehnenden Bescheid, hört eine Unwetterwarnung und eine Räumungsanordnung der Polizei und findet am Montag ein neues Haltverbotsschild vor ihrer Ladezone. Ablauf: Fall → Frage → Sachverhalt → Wortlaut § 35 Satz 1 → 1. hoheitliche Maßnahme (Vertrag § 54) → 2. Behörde (§ 1 IV; Gericht) → 3. öffentliches Recht (Garage nach BGB) → 4. Regelung (Ablehnung; Warnung, Auskunft, Realakt; Räumungsgebot) → 5. Einzelfall (Satzung als Rechtsnorm) → Wortlaut § 35 Satz 2 (drei Formen) → Verkehrszeichen (BVerwG) → 6. Außenwirkung (Umsetzung im Rathaus, Organisationsakt) → Ergebnis → Bedeutung (§ 42 I VwGO, Frist, Vollstreckung) → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:36,2 (5.409 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Wiegand (WI), um 62 | betreibt einen Kaffeewagen auf dem Marktplatz | Pose `standing/polka_dots` (gepunkteter Pullover, rosa Hose), Kopf `Gray Bun` (graues Haar), Haut `#F0C8A8`; Mimiken `Smile` (ruhig), `Concerned|Serious` (redet, Sorge), `Suspicious` (denkt), `Driven` (entschlossen), `Cute` (froh) | `hilde` (Frau, älter) |
| Herr Lorenz (LO), um 48 | Ordnungsamt, Beamter | Pose `standing/blazer-3` (blaues Jackett), Kopf `Short 1`, Brille `Glasses`, Haut `#E6B48F`; Mimiken `Serious` (ruhig/redet), `Solemn` (denkt) | `christian` (Mann, mittel) |
| Polizist Göbel (GO), um 28 | Polizei | Pose `standing/walking-1` (dunkelblaues Shirt `#3D4A7A` wie eine Uniform), Kopf `Short 4`, Haut `#D9A07A`; Megafon (Phosphor) neben ihm; Mimiken `Serious`, `Driven` (redet), `Suspicious` (denkt) | `niklas` (Mann, jung) |
| Frau Kessler (KE), um 38 | Amtsleiterin im Ordnungsamt | Pose `standing/crossed_arms-2` (verschränkte Arme), Kopf `Medium Bangs 3`, Haut `#F1C6A5`; Mimiken `Smile` (ruhig), `Serious` (redet) | `julia` (Frau, jung) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szene A: Frau Wiegand blickt nach rechts zu Lorenz bzw. Göbel, die nach links zu ihr blicken; Szene B: Wiegand blickt nach links zum Schild; im Rathaus blickt Kessler nach rechts zu Lorenz, Lorenz nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `WI_redet`, `LO_redet`, `GO_redet`, `KE_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (shirt-1/-2, blazer-1/-2 bewusst nicht verwendet).
- **Stimmen nur aus dem Pool** niklas, julia, christian, hilde; Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Wiegand, Lorenz, Göbel (Umlaut), Kessler; nicht in der Liste früherer Namen. Genitiv vermieden („der Antrag von Frau Wiegand“).
- Figuren-PNGs: `../peeps/op_044/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 041 Garten am Stadtrand und Instanzenweg (Bienen), 032 Altstadt und Farbengeschäft. Hier: Marktplatz mit Rathaus, Kaffeewagen und Sonnenschirm, Unwetter (Wolke, Gewitterwolke, Blitz), Ladezone mit Haltverbotsschild, Rathausbüro. Posen `polka_dots`, `blazer-3`, `walking-1`, `crossed_arms-2` in 040–043 nicht verwendet.

## Szenen

Alle Szenen auf Cremegrund (Tageslicht; das Unwetter nur durch Wolken-Icons, kein Nachtgrund).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Marktplatz** `fall`–`go2` | Rathaus, Kaffeewagen, Schirm, Kundschaft; Lorenz bringt den Bescheid; mittags Wind, Göbel mit Megafon, Warnung, Gewitter, Räumung | fluent-hc:`classical-building`, tabler:`caravan`+`coffee`, `umbrella`, `sun`, `users`, `file-text`, `cloud`, fluent-hc:`wind-face`, ph:`megaphone`, tabler:`cloud-storm`, `bolt` | `Fall · Samstag auf dem Marktplatz` (ab 0,0 s) → `Fall · Ein Brief vom Amt` → `Fall · Durchsagen der Polizei` | Marktplatz · Lorenz · Brief · Blase Lorenz · Wiegand Sorge · Blase Wiegand · Mittags · Wind · Göbel · Megafon · Blase Warnung · Gewitter · Blitz · Blase Räumung | Donner (`szene_044donner_1`) |
| **B Montag** `montag`/`wi2` | Ladezone, Kaffeewagen, neues Haltverbotsschild | `building-community`, Ladezone (Karte), Haltverbotsschild (Baustein) | `Fall · Montag: ein neues Schild` | Straße · Ladezone · Schild · Pille · Wiegand denkt · Blase | – |
| **C Die Frage** `frage`/`frage2` | vier Maßnahmen nebeneinander | `file-text`, ph:`megaphone` ×2, Haltverbotsschild | `Fall · Was davon ist ein Verwaltungsakt?` | Bescheid · zwei Durchsagen · Schild · Frage · 6 Merkmale · wehren | – |
| **D Sachverhalt** `sv` | Karte vollständig, Bearbeitervermerk, ≈ 9,7 s | – | `Sachverhalt` | 1 | – |
| **E Wortlaut § 35 S. 1** `wl35`–`land` | Wortlautkarte, vorgelesen, acht Marker zum Wort | `book` | `Norm · § 35 Satz 1 VwVfG` | Karte · Marker · 6 Merkmale · Länder | – |
| **F 1. hoheitliche Maßnahme** `m1`–`vertrag` | Tafel; Wiegand | `file-text`, ph:`handshake` | `Verwaltungsakt › 1. hoheitliche Maßnahme` | Zeilen zum Wort, ✗ Vertrag | – |
| **G 2. Behörde** `beh0`–`gericht` | Tafel; Göbel | `building`, ph:`megaphone`, `gavel` | `› 2. Behörde, § 1 IV VwVfG` | Definition · ✓ Ordnungsamt · ✓ Polizei · ✗ Urteil | – |
| **H 3. öffentliches Recht** `m3`/`garage` | Tafel; Wiegand | `file-text`, ph:`garage` | `› 3. auf dem Gebiet des öffentlichen Rechts` | Befugnis · ✓ Standplatz · Garage · ✗ Privatrecht | – |
| **I 4. Regelung** `m4`/`abl` | Tafel; Lorenz | `file-text` | `› 4. Regelung` | Definition · fünf Pillen · ✓ Ablehnung · Block | – |
| **J 4. Regelung: Abgrenzung** `hinw`–`gebot` | Tafel; Göbel | ph:`megaphone`, tabler:`device-landline-phone`, ph:`broom`, `umbrella` | `› 4. Regelung › Hinweis, Auskunft, Realakt` → `› Gebot` | ✗ Warnung · ✗ Auskunft · ✗ Realakt · ✓ Gebot · Block | – |
| **K 5. Einzelfall** `m5`/`norm` | Tafel; Wiegand | `user`, `book` | `› 5. Einzelfall` | ✓ Antrag · Satzung · ✗ Rechtsnorm | – |
| **L Wortlaut § 35 S. 2** `wl352`–`av3` | Wortlautkarte, Merkmale markiert, drei Formen; Göbel | ph:`megaphone`, `road`, `barrier-block` | `› 5. Einzelfall › Allgemeinverfügung, § 35 Satz 2` | Karte · Marker · a) · b) · c) | – |
| **M Verkehrszeichen** `vz`/`halt` | Tafel, Haltverbotsschild; Wiegand | Haltverbotsschild | `› 5. Einzelfall › Verkehrszeichen` | BVerwG · ✓ Haltverbot | – |
| **N 6. Außenwirkung** `m6`–`aussen` | Tafel; im Rathaus Kessler und Lorenz, Blase Kessler | `file-text` | `› 6. unmittelbare Außenwirkung` → `› innerdienstliche Weisung` → `› Bescheid an Frau Wiegand` | Definition · Rathaus · Blase · Umsetzung ✗ · Organisationsakt ✗ · Bescheid ✓ | – |
| **O Ergebnis** `erg`–`erg3` | vier Maßnahmen wie in C, Haken/Kreuz | wie C | `Ergebnis` | ✓ Bescheid · ✓✓ Allgemeinverfügungen · ✗ Warnung | – |
| **P Klageart** `warum`–`unst` | Tafel; Wiegand | Haltverbotsschild, `caravan` | `Bedeutung › Klageart, § 42 I VwGO` | Anfechtung · Verpflichtung · ✗ unstatthaft | – |
| **Q Frist und Vollstreckung** `frist`/`vollstr` | Tafel; Wiegand | `calendar`, `file-text` | `Bedeutung › Frist` → `› Vollstreckung` | 1 Monat · 1 Jahr · Verwaltungszwang | – |
| **R Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Verwaltungsakt prüfen` | drei Hinweise | – |
| **S Klausurschema** `sch`–`q7` | Schema baut sich auf | – | `Klausurschema` | Titel · Oberbegriff · 6 Merkmale + Allgemeinverfügung · Folge | – |
| **T Merksatz** `merke`/`m2` | Lexi erklärt, Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 20 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** ein Handlungsgeräusch (Donner, wenn die Gewitterwolke erscheint), CC0 aus dem Bestand (Freesound gesperrt), Herkunft in `geraeusche_herkunft.json`.
**Haltverbotsschild:** als Baustein gezeichnet (blaue Scheibe, roter Ring, rotes Kreuz in Palettenfarben, Tuschekontur), weil keine Iconbibliothek ein Haltverbotszeichen enthält; Zeichen 283 StVO nachempfunden, kein Icon umgezeichnet.

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Frau Wiegand verkauft Kaffee aus einem kleinen Wagen auf dem Marktplatz. Herr Lorenz vom Ordnungsamt übergibt ihr einen Bescheid: Ihr Antrag auf eine Erlaubnis für einen festen Standplatz wird abgelehnt. Mittags warnt Polizist Göbel per Megafon vor einem Unwetter. Als es kurz darauf donnert, ordnet er an: Alle verlassen sofort den Marktplatz. Am Montag steht vor ihrer Ladezone ein neues Haltverbotsschild. Im Rathaus teilt Amtsleiterin Kessler dem Beamten Lorenz mit, dass er ab Montag im Bürgerbüro arbeitet.
>
> Bearbeitervermerk: Die Standplatzerlaubnis richtet sich nach öffentlichem Recht.
>
> **Welche dieser Maßnahmen sind Verwaltungsakte?**

Kein Fiktiv-Hinweis auf Karte, Tafeln oder im Sprechtext.

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen. Tafeln schreiben Normen in Ziffern („§ 35 Satz 1 VwVfG“, „§ 42 I VwGO“), gesprochen als Wörter. Kleine graue Fundstellenzeilen sind Belege, kein Sprechtext. Die Wortlautkarte § 35 Satz 1 wird vorgelesen; die Karte § 35 Satz 2 ist als Zitat gekennzeichnet, ihre Merkmale werden genannt und markiert.
