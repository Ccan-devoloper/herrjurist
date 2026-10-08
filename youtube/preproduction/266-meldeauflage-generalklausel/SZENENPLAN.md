# Folge 266 · Polizeiliche Generalklausel: Meldeauflage für Hooligans erlaubt? – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_266.py`](src/skript_266.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Polizei- und Ordnungsrecht · Schema. Beispielfall nach dem Plan-Hook: Samstag, 15 Uhr, Polizeiwache in NRW; Herr Schütte muss sich an den Samstagen der nächsten drei Auswärtsspiele seines Vereins jeweils um 15 Uhr melden (Anpfiff 15:30 Uhr, 200 km entfernt). **Darstellung ohne Klischee:** kein Vereinsname, kein Wappen, keine Vereinsfarben, kein Schal, keine Pyrotechnik, kein Gewaltbild; Herr Schütte ist ein gewöhnlicher Mann im Pullover, skeptisch und genervt, nicht „fies“. Ablauf: Fall → Frage → Sachverhalt → 1. Ermächtigungsgrundlage (Sperrwirkung, Verweis 077) → Länder im Vergleich (§ 16a NPOG, § 20 SächsPVDG, § 15a BbgPolG; NRW ohne Norm) → Wortlautkarte § 8 Abs. 1 PolG NRW → Trägt die Generalklausel? (Art. 2 Abs. 1, Art. 11 GG mit Wortlautkarte, Zitiergebot § 7 PolG NRW) → Wesentlichkeit (Zitatkarte BVerwG 6 C 39.06 Rn. 33, Grenze Vorfeld) → Abgrenzung § 10 PassG (Wortlautkarten § 10 Abs. 1 S. 2, § 7 Abs. 1 Nr. 1) → Gegenfall Auslandsspiel → 2. Tatbestand (Verweis 257, 213) → 3. Ermessen und Verhältnismäßigkeit (Gefährderansprache) → Ergebnis → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:41,2 (5.825 Zeichen Skript, 5.807 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Schütte (SC), um 35 | Fußballfan mit Meldeauflage | Pose `standing/crossed_arms-1` (Pullover Senfgelb `#E3A857`, schwarze Hose), Kopf `Short 4`, Haut `#E8B48F`, kein Bart; Mimiken `Calm`, `Suspicious` (skeptisch), `Concerned\|Serious`, `Solemn`, `Smile`, `Tired`; redet mit `Serious` | `niklas` (Mann, jung) |
| Polizistin Feddersen (FE), um 30 | Polizei auf der Wache, freundlich-sachlich | Pose `standing/blazer-2` (Jacke Dunkelblau `#2F3E6B` über hellblauem Shirt `#8DB3F2`, Hose `#2E3440`; uniformähnlich ohne Abzeichen, Wappen oder Waffe; Beinprothese der Pose – positive Rolle), Kopf `Medium Bangs 3`, Haut `#C98E6A`; `Calm`, `Serious`, `Smile`, `Suspicious`; redet mit `Smile` | `julia` (Frau, jung) |
| Wachleiter Rabe (RA), um 60 | Leiter der Wache, nennt den Anlass | Pose `standing/shirt-3` (Hemd Hellblaugrau `#C9D6E8`, schwarze Hose), Kopf `No Hair 1`, Brille `Glasses`, Haut `#EBC29E`; `Calm`, `Serious`, `Suspicious`, `Driven`, `Smile`; redet mit `Serious` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` nach rechts. Fall: Herr Schütte (links, an der Tür) blickt nach rechts zu Feddersen und Rabe; beide blicken nach links zu ihm. An den Tafeln blicken alle nach links. Gegenfall: Schütte allein, blickt nach links zu Schranke und Flugzeug.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `SC_redet`, `FE_redet`, `RA_redet` (je links/rechts) und Lexi. Keine Bärte, keine Polka Dots.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Koordinatorliste, nicht in `namen_reserviert.txt`, in keiner Datei unter `youtube/` (grep über *.py, *.md, *.csv, *.json, *.txt am 08.10.2026: Schütte, Feddersen, Rabe je 0 Treffer; „Albers“ wegen 45 Treffern, „Kruse“ wegen Nähe zu „Krause“ verworfen), vor der Vertonung als „266: Schütte, Feddersen, Rabe“ eingetragen. „Feddersen“ steht nur auf dem Namensschild (nicht gesprochen). Kein Name im Genitiv.
- **Stimmen nur aus dem Pool:** niklas, julia, helmut; `ela_froh` nicht verwendet (fröhliche Stimme passt zu keiner Rolle). Erzählerin/Lexi Carla ohne Rolle.
- Figuren-PNGs: `../peeps/op_266/` (62 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 262 (`easing-1`, `blazer-3`, `pointing_finger-2`), 263 (`easing-1`, `shirt-4`), 264 (`resting-1`, `blazer-4`, `robot_dance-2`, `crossed_arms-2`) und 257 (`shirt-4`, `easing-1`, `robot_dance-2`) – in 266 keine dieser Posen; Kleidung ohne Muster. Schauplatz neu: **Innenraum einer Polizeiwache** (Wand, Holztür, Tresen, Wanduhr auf 15 Uhr) – nicht in 077 (Stadtpark), 213 (Wohnstraße), 257 (Mehrfamilienhaus außen). Gegenfall an einer Grenzkontrolle (Flugzeug, Schranke) mit Rückkehr ins Inland (Stadion).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Polizeiwache** `fall`–`frage2` | Wache mit Tür, Tresen, Uhr; Feddersen hinter dem Tresen ab 0,0 s; Schütte tritt ein (Schreiben auf dem Tresen), Pillen Meldeauflage und Anpfiff (Stadion), Blase Feddersen, Blase Schütte, Rabe tritt hinzu, Blase Rabe, Pille Gefährderansprache, zwei Fragepillen | tabler:`clock-hour-3` (Weiß), `file-text`, `building-stadium` (Grün), `message-circle`; Wand, Tür, Tresen, Boden programmatisch | `Fall · Samstag, 15 Uhr, auf der Polizeiwache` (ab 0,0 s) → … → `Fall · Die Frage` (10 Stände) | ≈ 20 | Tür (`szene_266tuer_1`) beim Eintreten von Herrn Schütte |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s | – | `Sachverhalt` | 1 | – |
| **C Ermächtigungsgrundlage** `egl`–`spez` | Reihenfolge (Spezialbefugnis/Standardmaßnahme → Generalklausel), Sperrwirkung, Folge 077, Frage nach eigener Befugnis; Feddersen, Schütte | tabler:`book`, `list-details`, `map-2` | `1. Ermächtigungsgrundlage · …` (4) | ≈ 8 | – |
| **D Länder im Vergleich** `tni`–`tdein` | Tabelle Land/Norm/Voraussetzung/Befristung (NI, SN, BB), Sperrwirkung, NRW ohne Norm (VG Düsseldorf Rn. 15), Hinweis „In deinem Land …“, Portal-Fundstelle | – | `Länder › …` (8) | 8 | – |
| **E Generalklausel** `wl8`, `soweit` | **Wortlautkarte § 8 Abs. 1 PolG NRW** (4 Marker) | tabler:`book`, `list-details` | `1. Ermächtigungsgrundlage › …` (2) | ≈ 6 | – |
| **F Grundrechte** `trag`–`zitier` | Art. 2 Abs. 1 / Art. 11 GG (Pillen), Fundstelle Rn. 36, 45, **Wortlautkarte Art. 11 GG** (2 Marker), ✓ Zitiergebot § 7 PolG NRW | tabler:`scale`, `user-check`, `map-pin`, `book` | `… › Trägt die Generalklausel? › …` (5) | ≈ 9 | – |
| **G Wesentlichkeit** `wes`–`vorfeld` | Kritik (✗), BVerwG, **Zitatkarte BVerwG 6 C 39.06 Rn. 33**, drei Haken, roter Block Grenze Vorfeld | tabler:`message-2`, `building-bank`, `scale`, `alert-triangle` | `… › Wesentlichkeit › …` (5) | ≈ 10 | – |
| **H Abgrenzung § 10 PassG** `pass`–`zweck` | **Wortlautkarten § 10 Abs. 1 S. 2 und § 7 Abs. 1 Nr. 1 PassG** (je Marker), Ansehen, Art. 2 Abs. 1, ✓ nebeneinander, gelber Block Zweck (VG Gelsenkirchen) | tabler:`id`, `plane-departure`, `world`, `arrows-left-right`, `shield` | `Abgrenzung › § 10 PassG › …` (7) | ≈ 12 | – |
| **I Gegenfall** `ausl`–`inl` | Grenzkontrolle: Flugzeug, Schranke, Hand „Stopp“, Schreiben; ✗ über dem Flugzeug, Stadion im Inland | tabler:`plane-departure`, `barrier-block`, `hand-stop`, `file-text`, `building-stadium` | `Gegenfall · …` (3) | ≈ 5 | – |
| **J Tatbestand** `tb`–`gefja` | Folge 257, ✓ Körperverletzungen (Folge 213), Tatsachen (2 Haken), Fanszene/Verfahren (VG Minden), ✓ Verhaltensstörer, grüner Block | tabler:`alert-triangle`, `first-aid-kit`, `list-check`, `users-group`, `user-exclamation`, `shield` | `2. Tatbestand …` (6) | ≈ 13 | – |
| **K Verhältnismäßigkeit** `vh`–`erg` | geeignet, erforderlich (Gefährderansprache, OVG NRW Rn. 26), angemessen, andere Dienststelle, grüner Ergebnisblock | tabler:`scale`, `clock-hour-3`, `message-circle`, `heart`, `map-pin`, `shield` | `3. … › …` (6) | ≈ 14 | – |
| **L Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (3) | ≈ 6 | – |
| **M Schema** `sch`–`s5` | breite Karte 1.–5. mit Unterzeilen | – | `Schema › …` (6) | 6 | – |
| **N Merksatz** `merke`, `m2` | Lexi erklärt (redet), vier Marker | – | `Merksatz` | ≈ 5 | – |

**Blasen:** Stil C (Standard seit 02.10.2026; Assertion gegen stillen Rückfall). **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („15 Uhr“, „15:30 Uhr“, „200 km“, „2-mal“, „3 Auswärtsspiele“, „§ 16a NPOG“, „Folge 077“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops; keine Bewegung, kein Zoom.
**Geräusch:** eine Tür, die ins Schloss fällt, wenn Herr Schütte die Wache betritt (Freesound 872998, CC0, Herkunft in `geraeusche_herkunft.json`). Kein Stadion-, Sprechchor- oder Gewaltgeräusch.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji High Contrast (MIT: Haken/Kreuz), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Wache, Tresen, Boden programmatisch. Kein Richterhammer (Gericht als `building-bank`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Nordrhein-Westfalen: Herr Schütte wurde 2-mal wegen Körperverletzung bei Auswärtsspielen seines Fußballvereins verurteilt. Im Sommer warnte ihn die Polizei in einer Gefährderansprache. Seine Gruppe hat sich für die nächsten Auswärtsspiele zu Schlägereien mit gegnerischen Fans verabredet.
>
> Nach Anhörung verpflichtet ihn die Polizei: An den Samstagen der nächsten 3 Auswärtsspiele muss er sich jeweils um 15 Uhr auf seiner Polizeiwache melden; Anpfiff ist um 15:30 Uhr, 200 km entfernt. Bei Verhinderung darf er sich nach Absprache bei einer anderen Dienststelle melden.
>
> **Ist die Meldeauflage rechtmäßig? Worauf kann die Polizei sie stützen?**

Kein Fiktiv-Hinweis auf Karte, Tafeln oder im Sprechtext.

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen (Zahl als Ziffer: „2-mal“). Kleine graue Fundstellenzeilen (26 px) sind Belege, kein Sprechtext. Die Wortlautkarten (§ 8 Abs. 1 PolG NRW, Art. 11 GG, § 10 Abs. 1 S. 2 und § 7 Abs. 1 Nr. 1 PassG) und die Zitatkarte (BVerwG 6 C 39.06 Rn. 33) sind als Zitat gekennzeichnet; § 8 Abs. 1 wird wörtlich vorgelesen, die übrigen werden sinngemäß gesprochen und stehen lange genug zum Mitlesen. Die Ländertabelle gibt die Voraussetzungen der drei Normen gekürzt wieder.
