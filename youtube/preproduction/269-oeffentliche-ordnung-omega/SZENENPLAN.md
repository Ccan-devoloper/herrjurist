# Folge 269 · Öffentliche Ordnung: Zwergenweitwurf und Laserdrome (Omega) – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_269.py`](src/skript_269.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Polizei- und Ordnungsrecht · Klassiker-Fall. Beispielfall nach dem Plan-Hook: Freitagnachmittag vor einer Diskothek in NRW; Frau Bredemeier wirbt für Samstag mit einem „Zwergenweitwurf“, der kleinwüchsige Artist Herr Mehring macht freiwillig und gegen Bezahlung mit; Frau Leuschner (Ordnungsamt) untersagt die Veranstaltung wegen einer Gefahr für die öffentliche Ordnung. Ablauf: Fall → Frage → Sachverhalt → 1. Begriff (Zitatkarte BVerfGE 69, 315 [352]; Abgrenzung öffentliche Sicherheit, Verweis 213; Sachsen § 4 Nr. 2) → Bestimmtheit und Länder (Kritik/BVerfG; Schleswig-Holstein 1992 gestrichen; NRW, NI, SN, BB) → 2. Klassiker Zwergenweitwurf (VG Neustadt, Gewerberecht; Wortlautkarte Art. 1 Abs. 1 GG; Argumente beider Seiten; Übertragung; UN-Ausschuss) → 3. Klassiker Laserdrome (Wortlautkarte § 14 Abs. 1 OBG NRW; BVerwG) → Unionsrecht (Wortlautkarten Art. 56 Abs. 1, Art. 52 Abs. 1 AEUV) → EuGH Omega (Rn. 30, 34–39, 41) → Gegenfall feste Ziele → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:06,1 (5.499 Zeichen Skript, 5.481 gesprochene Zeichen); Begründung in ABNAHME.md.

## Darstellung (besonders wichtig)

- **Herr Mehring** ist ein selbstbewusster Erwachsener mit eigener Stimme, eigenem Namensschild („Herr Mehring, Artist“) und eigenem Argument („Über meine Würde entscheide ich selbst.“); keine Witzfigur, keine komische Mimik. Seine Körpergröße entsteht nur über die Darstellungshöhe (74 % der Erwachsenenhöhe), die Zeichnung (Erwachsenenkleidung, Kinnbart) bleibt unverändert.
- **Kein Wurf im Bild:** nur das Veranstaltungsplakat (Text „SAMSTAG – ‚Zwergenweitwurf‘ – 21 Uhr“, Stern). Das Wort „Zwerg“ nur als Name der Veranstaltung und im Zitat des Gerichts, das die Bezeichnung als herabsetzend rügt; sonst „kleinwüchsig“.
- **Laserdrome nur als Arena-Symbol** (tabler `building-arch`), Weste als `shirt`, feste Ziele als `target` – keine Spielszene, keine Waffen, kein Laserzielgerät im Bild.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Leuschner (LE), um 45 | Leiterin des Ordnungsamts | Pose `standing/blazer-1` (Blazer Dunkelgrün `#3B6B57`, Hose Anthrazit `#2E3440`; Beinprothese der Pose – positive Rolle), Kopf `Long`, Haut `#E0A882`; Mimiken `Calm`, `Serious`, `Suspicious`, `Solemn`, `Smile`; redet mit `Serious` | `julia` (Frau, jung) |
| Frau Bredemeier (BR), um 40 | Betreiberin der Diskothek | Pose `standing/pointing_finger-1` (schwarzes Outfit der Pose, zeigt auf das Plakat), Kopf `Long Curly`, Haut `#F2C9A8`; `Smile`, `Concerned\|Serious`, `Suspicious`, `Tired`, `Calm`; redet mit `Smile` | `ela_froh` (Frau, jung, fröhlich) |
| Herr Mehring (ME), um 35 | kleinwüchsiger Artist | Pose `standing/resting-2` (schwarzer Pullover der Pose, Jeans Dunkelblau `#2F3E6B`), Kopf `Short 2`, Kinnbart `Chin` (unter dem Mund), Haut `#B9805C`; `Calm`, `Driven`, `Serious`, `Solemn`, `Smile`; redet mit `Driven`; Höhe 370 px (Fall) bzw. 355 px (Tafeln) | `niklas` (Mann, jung) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` nach rechts. Fall: Mehring (links) und Bredemeier blicken nach rechts zu Leuschner, Leuschner nach links; Bredemeier zeigt beim „Plakat“ nach links auf das Plakat. An den Tafeln blicken alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `LE_redet`, `BR_redet`, `ME_redet` (je links/rechts) und Lexi.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Koordinatorliste, nicht in `namen_reserviert.txt`, in keiner Datei unter `youtube/` (grep über *.py, *.md, *.csv, *.json, *.txt am 08.10.2026: Leuschner, Bredemeier, Mehring je 0 Treffer; „Stelter“ wegen der Nähe zu „Stelze“ für einen kleinwüchsigen Menschen verworfen, „Vollrath“ wegen „Vollmer“), vor der Vertonung als „269: Leuschner, Bredemeier, Mehring“ eingetragen. Kein Name im Genitiv.
- **Stimmen nur aus dem Pool:** julia, ela_froh, niklas; `helmut` nicht verwendet (keine ältere Männerrolle). Erzählerin/Lexi Carla ohne Rolle. Gegenüber 266 (niklas, julia, helmut) neu: ela_froh; julia und niklas wegen des kleinen Pools erneut.
- Figuren-PNGs: `../peeps/op_269/` (62 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 266 (`crossed_arms-1`, `blazer-2`, `shirt-3`), 267 (`easing-2`, `robot_dance-3`, `walking-3`), 264 (`resting-1`, `blazer-4`, `robot_dance-2`, `crossed_arms-2`), 262/263 (`easing-1`, `blazer-3`, `pointing_finger-2`, `shirt-4`, `walking-1/-2`) – in 269 keine dieser Posen; keine Polka Dots. Schauplatz neu: **Fassade einer Diskothek** (Tür, Schild, Plakat) – nicht in 213 (Wohnstraße), 257 (Mehrfamilienhaus), 266 (Polizeiwache innen). Gegenfall als Arena-Symbol mit festen Zielen.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Diskothek** `fall`–`frage2` | Fassade, Tür, Schild „Diskothek“, Bredemeier ab 0,0 s; Plakat, Pille geplante Veranstaltung, Leuschner mit Verfügung, Blasen Leuschner/Bredemeier/Mehring, zwei Fragepillen | tabler:`star` (Weiß, auf dem Plakat), `file-text` (Weiß); Fassade, Tür, Boden programmatisch | `Fall · Freitagnachmittag, vor einer Diskothek` (ab 0,0 s) → … → `Fall · Die Frage` (9 Stände) | 11 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **C 1. Begriff** `begriff`–`sachsen` | **Zitatkarte BVerfGE 69, 315 (352)** (3 Marker), Abgrenzung, Pille Sachsen § 4 Nr. 2 | tabler:`book`, `users`, `shield` (Blau), `map-2` (Grün) | `1. Begriff › …` (4) | 9 | – |
| **D Bestimmtheit und Länder** `unbest`–`dein` | breite Karte: ✗ Kritik, ✓ BVerfG; ✗ Schleswig-Holstein 1992; Begründung; ✓ NRW, NI, SN, BB; gelber Block | – | `1. Begriff › Bestimmtheit … › Länder › …` (6) | 13 | – |
| **E 2. Klassiker** `zw`–`art1` | RLP 1992, VG Neustadt (Gewerberecht, gute Sitten, Fundstelle „nach Sekundärquellen“), blauer Block Wertordnung, **Wortlautkarte Art. 1 Abs. 1 GG** (2 Marker) | tabler:`file-text` (Gelb), `building-bank` (Blau), `book`, `heart` (Rot) | `2. Klassiker: Zwergenweitwurf › …` (5) | 10 | – |
| **F Würde trotz Einwilligung?** `pro`–`un` | (+) zwei Argumente für Herrn Mehring, (−) fünf Gründe des VG, grüner Ergebnisblock, UN-Ausschuss | tabler:`user-check`, `building-bank`, `heart`, `briefcase`, `shield`, `world` | `2. Klassiker: Zwergenweitwurf › …` (7) | 13 | – |
| **G 3. Klassiker Laserdrome** `ld`–`bverwg` | Bonn 1994, **Wortlautkarte § 14 Abs. 1 OBG NRW** (2 Marker), ✓ BVerwG | tabler:`building-arch` (Lila), `shirt`, `file-text`, `building-bank` | `3. Klassiker: Laserdrome (Omega) › …` (4) | 11 | – |
| **H Unionsrecht** `eu`–`art52` | britische Firma, **Wortlautkarten Art. 56 Abs. 1 und Art. 52 Abs. 1 AEUV** (je 2 Marker) | tabler:`world` (Blau), `arrows-left-right`, `scale` | `… › Unionsrecht › …` (3) | 8 | – |
| **I EuGH Omega** `eng`–`tenor` | eng (Rn. 30), ✓ Menschenwürde (Rn. 34 f.), ✓ keine gemeinsame Auffassung (Rn. 37 f.), ✓ verhältnismäßig (Rn. 39), grüner Ergebnisblock (Rn. 41) | tabler:`building-bank`, `heart`, `map-2`, `scale`, `shield` | `… › Unionsrecht › …`, `… › Ergebnis` (5) | 14 | – |
| **J Gegenfall** `gegen` | Arena-Symbol, drei feste Ziele, ✓, zwei Pillen; Bredemeier | tabler:`building-arch` (Lila), `target` (Weiß) | `Gegenfall · …` (2) | 2 | – |
| **K Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (3) | 6 | – |
| **L Schema** `sch`–`s4` | breite Karte 1.–4. mit Unterzeilen | – | `Schema › …` (5) | 9 | – |
| **M Merksatz** `merke`, `m2` | Lexi erklärt (redet), fünf Marker | – | `Merksatz` | 6 | – |

**Blasen:** Stil C (Assertion gegen stillen Rückfall). **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („1992“, „21 Uhr“, „§ 33a GewO“, „Art. 56 AEUV“, „Folge 213“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 13 Folien; innerhalb harte Schnitte und Pops; keine Bewegung, kein Zoom.
**Geräusch:** keines (kein passendes Handlungsgeräusch; Wurf- oder Spielgeräusche verboten), siehe `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji High Contrast (MIT: Haken/Kreuz), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Fassade, Tür, Plakat, Boden programmatisch. Kein Richterhammer (Gerichte als `building-bank`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Nordrhein-Westfalen: Frau Bredemeier betreibt eine Diskothek. Für Samstag wirbt sie auf einem Plakat mit einem „Zwergenweitwurf“: Gäste sollen den kleinwüchsigen Artisten Herrn Mehring möglichst weit auf eine Matte werfen. Herr Mehring macht freiwillig und gegen Bezahlung mit; es ist sein Beruf.
>
> Frau Leuschner vom Ordnungsamt untersagt die Veranstaltung. Sie stützt sich auf die Generalklausel (§ 14 Abs. 1 OBG NRW): Die Veranstaltung verletze die Menschenwürde und gefährde die öffentliche Ordnung.
>
> **Liegt trotz der Einwilligung eine Gefahr für die öffentliche Ordnung vor?**

Kein Fiktiv-Hinweis auf Karte, Tafeln oder im Sprechtext.

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen. Kleine graue Fundstellenzeilen (26 px) sind Belege, kein Sprechtext. Die Zitatkarte (BVerfGE 69, 315 [352]) wird sinngemäß gesprochen; Art. 1 Abs. 1 GG wörtlich vorgelesen; § 14 Abs. 1 OBG NRW, Art. 56 Abs. 1 und Art. 52 Abs. 1 AEUV sind als Zitat gekennzeichnet, werden sinngemäß gesprochen und stehen lange genug zum Mitlesen (Ausnahme nach FOLGE-ABLAUF.md Abschnitt 2).
