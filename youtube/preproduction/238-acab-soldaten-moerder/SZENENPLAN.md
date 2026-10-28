# Folge 238 · Soldaten sind Mörder und ACAB: Wie deutet man Äußerungen? – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_238.py`](src/skript_238.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Öffentliches Recht/Grundrechte, Klassiker-Fall. Fiktiver Rahmen nach BVerfG (K), Beschl. v. 17.5.2016 – 1 BvR 2150/14 (Buchstaben im Fanblock) und 1 BvR 257/14. Ablauf laut Auftrag: 1. Hook → Frage → Sachverhalt → 2. Art. 5 Abs. 1 S. 1 GG (Wortlautkarte), Meinung, Verweis Folge 025 → 3. Deutungsregeln (BVerfGE 93, 266 <295 f.>), „Soldaten sind Mörder“ → 4. Kollektivbeleidigung (Skala) → 5. ACAB-Kammerbeschlüsse → 6. Schranken Art. 5 Abs. 2 GG (Wortlautkarte), § 185 StGB (Wortlautkarte), Wechselwirkung (Verweis Folge 146), § 193 StGB ein Satz → 7. Ergebnis, Gegenfall → 8. Klausurtipp (Lexi), Prüfschema, Merksatz (Lexi).
**Länge:** Hauptfilm 6:46,6 bei 5.883 Zeichen (Grenze 7:00/6.200); Begründung in [`ABNAHME.md`](ABNAHME.md).

**Darstellung (Vorgabe Auftrag):** Das Kürzel ACAB steht nur auf dem Banner (schwarze Schrift auf Weiß) und als Fallbezeichnung auf Tafeln; die Bedeutung wird einmal sachlich auf Deutsch erklärt (Sprechtext „Es steht für eine englische Parole, auf Deutsch: …“, Pille und Sachverhaltskarte in normaler Schreibung), nie in Großschrift. Fans und Polizisten ohne Klischees: freundliche bis ernste Mimik, keine Vermummung, keine Helme, Schlagstöcke oder Waffen, keine Gewalt. Keine echten Vereinsfarben oder Logos (einfarbige Oberteile aus der Palette, kein Schal, keine Fahne). Reale Personen aus den Verfahren werden nicht gezeigt; „Soldaten sind Mörder“ nur als Tafel mit Fundstelle.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Hannes (HA), um 30 | Fan im Fanblock | `standing/walking-1` (T-Shirt Orange `#F2A65A`, schwarze Hose der Pose), Kopf `Short 2`, Haut `#E9BC98`, kein Bart; Mimiken `Smile`, `Calm`, `Serious`, `Awe`, `Solemn`, `Driven` (entschlossen), `Concerned\|Serious` | `marc` (Mann, mittel) |
| Polizistin Roth (RO), um 40 | Polizistin im Einsatz, stellt Strafantrag | `standing/robot_dance-3` (Uniformhemd Blau `#4A6FA5`, Hose Dunkelblau `#2B3550`), Kopf `Bun`, Haut `#E8B896`; Mimiken `Calm`, `Serious` (redet), `Suspicious`, `Solemn`, `Smile` | `laura_ruhig` (Frau, mittel) |
| Polizist (KO) | Kollege, spricht nicht | `standing/resting-1` (Hemd Blau `#4A6FA5`, schwarze Hose), Kopf `Short 1`, Haut `#D9A47E`; `Calm`, `Serious` | – |
| Freundin (F1), Freund (F2) | Freunde von Hannes, sprechen nicht | `robot_dance-2` (schwarzes Oberteil, Hose Hellblau), Kopf `Bangs 2`, Haut `#C68E6A`; `crossed_arms-1` (Oberteil Grün), Kopf `Short 4`, Haut `#F0C8A8`; `Smile`, `Calm` | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, weder auf der Koordinatorliste noch in `namen_reserviert.txt` (vor der Vertonung als „238: Hannes, Roth“ eingetragen), per Volltextsuche in den Skripten früherer Folgen ohne Treffer. Keine Genitivformen.
- **Stimmen nur aus dem Pool** (william, sabrina, marc, laura_ruhig): gebraucht `marc` und `laura_ruhig`; `william` (älter) und `sabrina` nicht benötigt.
- **Blickrichtung:** Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. Szene A/L: Fans im Block links blicken nach rechts zum Spielfeld, Polizisten rechts blicken nach links zum Fanblock. Szene M: Hannes kommt von links (blickt nach rechts), die Polizisten blicken ihm entgegen. Tafelfolien: alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `HA_redet`, `RO_redet` (je links/rechts) und Lexi. Keine Prothesen-Posen, keine Bärte, keine Polka Dots. 60 Figuren-PNGs in `../peeps/op_238/` (Drive-Master).

**Abweichung von den letzten Folgen:** 235 (`walking-3`, `blazer-4`), 236 (`crossed_arms-2`, `blazer-3`), 237 (`easing-2`, `blazer-3`), parallel 234 (`crossed_arms-2`, `shirt-3`, `blazer-3`, `easing-2`, `resting-1`): Die sprechenden Figuren nutzen keine dieser Posen (`resting-1` nur für den stummen Kollegen). Orange-T-Shirt, Uniformblau neu. Schauplätze **Fußballstadion** (Tribüne mit Stufen, Brüstung, Rasen mit Seitenlinie) und **Stadionausgang** (Mauer mit Tor, Schild „Ausgang“) – neu gegenüber 235–237; die Rückkehr ins Stadion in Szene L folgt der Geschichte („Zurück ins Stadion“). Grundrechtsvorgänger 025 (Meinung/Tatsache), 134 (§ 185) und 146 (Wechselwirkung) nur über Verweise. Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Stadion** `fall`→`echt` | Tribüne, Fans hinter der Brüstung ab 0,0 s; Banner „ACAB“ an der Brüstung; Polizei am Spielfeldrand; Roth und Hannes reden; Frage; Karte der zwei Klassiker | programmatisch (Tribüne, Brüstung, Banner, Rasen) | `Fall · Im Stadion` (ab 0,0 s) → `· Das Banner` → `· Polizei im Einsatz` → `· Der Strafantrag` → `· Die Frage` → `· Zwei Klassiker aus Karlsruhe` | Fans · Fanblock · Banner · Kürzel · Bedeutung · Polizei · Roth redet, Blase · Hannes redet, Blase · Frage · Karte Zeile 1 · Zeile 2 | Stimmengewirr (`szene_238menge_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s, Quellenzeile | – | `Sachverhalt` | 1 | – |
| **C Art. 5 Abs. 1 S. 1 GG** `a5`→`form` | Wortlautkarte, Meinung, Hannes allein | tabler:`book`, `message-circle`, `speakerphone` | `Art. 5 Abs. 1 S. 1 GG › Schutzbereich` → `› Meinung` → `› geschützt, auch polemisch` | Karte · 3 Marker · Meinung · ✓ begründet/grundlos · emotional · ✓ polemisch | – |
| **D Das Kürzel** `gleich`→`eingr` | Tafel, Hannes allein | tabler:`abc`, `message-circle`, `gavel` | `… › das Kürzel` → `› Meinung (+)` → `› Eingriff` | Kürzel · bekannt · ✓ nicht inhaltslos · Block Meinung · Verweis 025 · Block Eingriff | – |
| **E Deutung** `deut`→`kont` | Tafel, Hannes und Roth | tabler:`zoom-question`, `users`, `eye` | `Deutung › Sinn der Äußerung` → `› objektiver Sinn` → `› Wortlaut` → `› Kontext und Begleitumstände` | Voraussetzung · Block objektiv · ✗ Absicht · ✓ Publikum · Wortlaut · Kontext | – |
| **F Mehrdeutig** `mehrd`→`fern` | Verzweigung „Äußerung“ → „Deutung: strafbar“ / „Deutung: straflos“ | tabler:`arrows-split`, `gavel`, `search` | `Deutung › mehrdeutige Äußerung` → `› andere Deutungen ausschließen` → `› fernliegende Deutungen` | Äußerung · strafbar · Regel · straflos · ✗ fernliegend | – |
| **G „Soldaten sind Mörder“** `sold`→`uebers` | Fundstellenkarte, Deutung | tabler:`gavel`, `flag`, `scale` | `„Soldaten sind Mörder“ › BVerfGE 93, 266` → `› andere Deutung` → `› nicht ausgeschlossen` | Karte · verurteilt · Transparent · ✓ schlechthin · ✗ einzelne · Block | – |
| **H Kollektiv** `koll`→`umst` | Skala Einzelperson … soziale Einrichtungen, Stecknadeln „Bundeswehr“ und „alle Soldaten der Welt“ | tabler:`user`, `building`, `map-pin` ×2, `users-group`, `flag`, `search` | `Kollektivbeleidigung › wen trifft die Äußerung?` → `› je größer, desto schwächer` → `› alle Soldaten der Welt` → `› Soldaten der Bundeswehr` → `› Teilgruppe genügt nicht` | Kollektiv · je größer · Skala · Einzelperson · Einrichtungen · ✗ Welt · ✓ Bundeswehr · Teilgruppe · Umstände | – |
| **I ACAB-Beschlüsse** `acab`→`uebg` | Fundstellenkarte, Kreuze, Block personalisierte Zuordnung, Kontext | Banner klein, tabler:`user-check`, `eye`, `message-report` | `ACAB-Beschlüsse › BVerfG (Kammer) 2016` → `› Teilgruppe reicht nicht` → `› personalisierte Zuordnung` → `› Anwesenheit genügt nicht` → `› Kontext` | Karte · Az. · ✗ Teilgruppe · Block · bestimmte Beamte · ✗ Anwesenheit · Kontext · Kritik · nicht gewürdigt | – |
| **J Schranken** `schr`→`nur` | Wortlautkarten Art. 5 Abs. 2 GG und § 185 StGB, Roth allein | tabler:`book` | `Schranken › Art. 5 Abs. 2 GG` → `› § 185 StGB: allgemeines Gesetz` → `› § 185 StGB definiert die Beleidigung nicht` | Karte · 2 Marker · Karte § 185 · ✓ allgemeines Gesetz · 2 Marker · nennt nur die Strafe | – |
| **K Anwendung** `wechs`→`p193` | Wechselwirkung, Prüfort, § 193 | tabler:`arrows-left-right`, `zoom-question`, `scale` | `Schranken › Wechselwirkung` → `› Anwendung: Deutung, Personenbezug` → `› § 193 StGB: Abwägung` | Block · Lüth · Prüfort 1. · 2. · Block § 193 · Abwägung | – |
| **L Ergebnis** `erg`→`verl` | zurück im Stadion (Banner oben, Polizei am Rand) | wie A | `Ergebnis › zurück im Stadion` → `› kein Bezug auf die Beamten` → `› keine Beleidigung der Polizisten vor Ort` → `› Verurteilung verletzt Art. 5 Abs. 1 S. 1 GG` | 3 Pillen · Ergebniskarte ✗ · Verletzung | – |
| **M Gegenfall** `gegen`→`gg4` | Stadionausgang; Hannes geht mit dem Banner zu Roth und Kollegen und hält es vor ihnen hoch; Roth redet | programmatisch (Mauer, Tor), tabler:`door-exit` | `Gegenfall › nach dem Spiel` → `› gezielt zu den Beamten` → `› bewusst in ihre Nähe begeben` → `› Bezug auf diese Beamten (+)` → `› Beleidigung möglich, § 193 StGB` | Ausgang · Hannes geht · angekommen · Roth redet, Blase · konfrontieren · ✓ Bezug · Karte · Abwägung | Schritte (`szene_238schritte_1`) |
| **N Klausurtipp** `tipp`→`t3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · zuerst den Sinn ermitteln` → `· personalisierte Zuordnung` → `· Schmähkritik nicht vorschnell` | 3 Punkte | – |
| **O Prüfschema** `sch`→`k3e` | breite Karte, Aufbau Punkt für Punkt | – | `Prüfschema` → `› I. Schutzbereich` … `› III. 2. c) Abwägung, § 193 StGB` | Titel · I. · II. · III. · 1. · 2. · a) · b) · c) | – |
| **P Merksatz** `merke`/`m2` | Lexi erklärt (redet), Marker | – | `Merksatz` | Satz 1 + Marker · Satz 2 + Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegung nur: Hannes geht im Gegenfall 540 px von links mit dem Banner zu den Polizisten.
**Geräusche:** zwei Handlungsgeräusche (Freesound CC0, als Kopien vorhandener sfx3-Dateien, weil die Freesound-API am 07.10.2026 über den Proxy gesperrt war), Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** Stil C, wortgleich mit dem Gesprochenen. Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 07.10.2026), Auslassungen mit „…“.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Samstagnachmittag im Fußballstadion: In der zweiten Halbzeit halten Hannes und seine Freunde im Fanblock an der Brüstung ein Banner hoch, in Richtung Spielfeld. Darauf steht nur das Kürzel ACAB. Es steht für eine englische Parole, auf Deutsch: „Alle Polizisten sind Bastarde“.
>
> Am Rand des Spielfelds sind Polizisten im Einsatz, darunter Polizistin Roth. Sie sehen das Banner. An die Beamten wendet sich Hannes nicht. Polizistin Roth meint, das Banner gelte ihnen, und stellt Strafantrag.
>
> Hannes sagt: Das sei seine Meinung über die Polizei, gemeint sei niemand persönlich.
>
> **Beleidigt Hannes mit dem Banner die Polizisten vor Ort?** — *Nach BVerfG (Kammer), Beschl. v. 17.5.2016 – 1 BvR 2150/14 und 1 BvR 257/14; BVerfGE 93, 266 („Soldaten sind Mörder“)*
