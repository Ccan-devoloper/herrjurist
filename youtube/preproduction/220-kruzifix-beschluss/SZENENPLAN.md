# Folge 220 · Kruzifix-Beschluss: Muss das Kreuz aus dem Klassenzimmer? – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_220.py`](src/skript_220.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Grundrechte, Klassiker-Fall. Fiktiver Fall nach dem Muster von BVerfGE 93, 1. Ablauf laut Auftrag: 1. Hook (Bayern, Anfang der 1990er; Kreuz über der Tafel; Eltern bitten um Abhängen) → Frage → Sachverhalt → 2. Art. 4 Abs. 1 GG (Wortlautkarte), positive/negative Glaubensfreiheit, Elternrecht → 3. Eingriff (Schulpflicht, „unter dem Kreuz“, Glaubenssymbol statt bloßer Kultur) → 4. Rechtfertigung (vorbehaltlos, Art. 7 Abs. 1 GG als Wortlautkarte, praktische Konkordanz, positive Glaubensfreiheit, kein Mehrheitsprinzip) → 5. Ergebnis mit abweichender Meinung in einem Satz, Ergebnis im Fall → 6. Folgen in Bayern (Art. 7 Abs. 3 BayEUG 1995 als Wortlautkarte, BVerwG 6 C 18.98, Kreuzerlass/BVerwG 10 C 5.22) → 7. Klausurtipp und Merksatz mit Lexi. Hauptfilm 5:23,2.

**Darstellung (Vorgabe Koordinator):** respektvoll gegenüber allen Bekenntnissen. Das Kreuz ist ein schlichtes, holzfarbenes lateinisches Kreuz (Tabler-Icon `cross`, ohne Korpus), über der Tafel bzw. als Requisit; keine Karikatur von Gläubigen oder Nichtgläubigen, keine weiteren religiösen Symbole. Eltern höflich und besorgt (nie aggressiv), Schulleiter sachlich-freundlich, auch beim Nachgeben ohne Triumph der einen oder Niederlage der anderen Seite. Eltern, Schule, Schulleiter fiktiv; reale Beschwerdeführer weder gezeigt noch benannt; der Sohn als Open-Peeps-Kind.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Rohde (RO), um 38 | Vater | `standing/robot_dance-2` (offene Handgeste; schwarzes Oberteil der Pose, Hose Sand `#D9B38C`), Kopf `Short 3` (Haar `#6B4A2E`), Haut `#EBC3A0`; Mimiken `Smile` (ruhig), `Concerned|Serious` (Sorge), `Serious` (redet), `Calm` (froh), `Tired` (nachdenklich) | `niklas` (Mann, jung) |
| Frau Rohde (FR), um 36 | Mutter; spricht nicht | `standing/walking-3` (schwarze Kleidung der Pose, nicht einfärbbar), Kopf `Long` (Haar `#3A2A20`), Haut `#D9A884`; `Smile`, `Concerned|Serious`, `Calm` | – |
| Herr Kampe (KA), um 60 | Schulleiter | `standing/blazer-4` (Sakko Blau `#8DB3F2`, Hemd Weiß, schwarze Hose), Kopf `Gray Short`, Brille `Glasses 4`, Haut `#F0CDB2`; `Smile`, `Calm` (redet ka1), `Serious`, `Tired` (nachdenklich), `Smile` (redet ka2) | `helmut` (Mann, älter) |
| Sohn der Rohdes (SO), 7 | Schüler der 2a; spricht nicht, ohne Namen (Schild „Sohn der Rohdes“) | `standing/resting-1` (Pullover Grün `#8FD694`), Kopf `Short 2`, Haut `#EBC3A0`; Höhe 58 % (Fallszene 255 px, Tafelszene 278 px); `Calm`, `Cute`, `Concerned|Serious` | – |
| Mitschüler K1, K2, 7 | Kinder der 2a; sprechen nicht, ohne Namen | K1 `standing/pointing_finger-1` (Kopf `Bun 2`, Haut `#B07552`), K2 `standing/crossed_arms-2` (Kopf `Bangs`, Hose Blau); Höhe 58 %; `Smile`/`Cute`/`Calm` | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Grundansicht gespiegelt (nach links), `_r` nach rechts. Büro: Familie (`_r`) blickt zum Schulleiter rechts, Kampe nach links zu ihr. Schlussszene im Klassenzimmer: Kampe (`_r`) blickt zur Familie, die Familie nach links zu ihm und zur Tafel. Klassenzimmer: Kinder blicken nach links zur Tafel. Tafelszenen: alle nach links zur Tafel.
- **Grundmimiken alle mit geschlossenem Mund**; Mundzustände a/o/e nur in `RO_redet`, `KA_redet`, `KA_redet2` (je links/rechts) und Lexi. 66 Figuren-PNGs in `../peeps/op_220/` (Drive-Master); Kontaktbild `out/figuren_bogen.png`, Köpfe `out/koepfe.png`.
- **Namen:** Rohde, Kampe – eindeutig deutsch, nicht auf der Koordinatorliste, nicht in `namen_reserviert.txt`, per Volltextsuche über `*.py/*.md/*.csv/*.json` unter `youtube/` ohne Treffer (verworfen: Albers wegen 006, Hannes wegen 005, Karl wegen 002/041, Bruno wegen 011/015, Ole wegen 150, Wolff wegen 101); vor der Vertonung als „220: Rohde, Kampe“ eingetragen. Der Sohn bleibt namenlos.
- **Stimmen** nur aus dem Pool (niklas, helmut); ela_froh und julia nicht eingesetzt.

**Abweichung von den letzten Folgen:** Posen der Haupt- und Nebenfiguren nicht aus 217–219 (blazer-3, shirt-4, crossed_arms-1, resting-2, walking-1, easing-1, shirt-3, pointing_finger-2, sitting/one_leg_up-1, easing-2, robot_dance-3, walking-2); keine Polka Dots, keine Bärte, keine Prothesen-Posen. Blaues Sakko, sandfarbene Hose, grüner Kinderpullover neu gegenüber 217–219. Schauplätze **Klassenzimmer der 2a mit Kreuz über der Tafel** und **Büro der Schulleitung** – das Klassenzimmer gab es in 217 (Gymnasium, Mathematik); hier bewusst wieder, weil das Kreuz über der Tafel der Fall selbst ist. Unterschiede: Grundschule (2a, Rechnung „3 + 4 = 7“), Kreuz über der Tafel, kleinere Kinder, Pultfront breiter, Büro ohne Fenster und Glocke. Rückkehr ins Klassenzimmer (F2), weil die Geschichte mit dem Ergebnis dorthin zurückkehrt. Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Klassenzimmer** `fall`, `kreuz` | Schultafel („Klasse 2a“, Kreide „3 + 4 = 7“ beim Wort „Grundschule“), Kreuz darüber, drei Kinder hinter der Pultfront; Pillen „Bayern, Anfang der 1990er · staatliche Grundschule“ (ab 0,0 s), Volksschulordnung im Wortlaut mit Fundstelle | tabler:`cross` (Holz) | `Fall · Bayern, Anfang der 1990er Jahre` → `· Das Kreuz über der Tafel` | 4 | Kreide (`szene_220kreide_1`) |
| **A2 Büro** `eltern`→`ka1` | Tür, Tisch; Familie Rohde links, Schulleiter Kampe rechts (erscheint bei `gespr`); Pillen zur Familie; Blasen ro1, ka1 | – | `Fall · Familie Rohde` → `· Gespräch mit Schulleiter Kampe` → `· Die Bitte der Eltern` → `· Die Antwort der Schule` | 6 | – |
| **A3 Die Frage** `frage`, `echt` | Tafel mit der Frage, gelber Block BVerfGE 93, 1; Rohde, Kampe | tabler:`cross`, `building-bank` | `Die Frage · …` | 2 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s, ohne Fiktiv-Zusatz | – | `Sachverhalt` | 1 | – |
| **C1 Art. 4 Abs. 1 GG** `art4`, `wl4` | Wortlautkarte mit Markern „Glaubens“, „Bekenntnisses“ | `book`, `heart` | `Art. 4 Abs. 1 GG · Maßstab` → `· Wortlaut` | 4 | – |
| **C2 I. Schutzbereich** `pos`→`a6` | positiv/negativ, Kreuz „kein Schutz … im Alltag“, Haken „vom Staat geschaffene Lage“, Block Elternrecht | `heart`, `eye-off`, `road`, `school`, `home` | `I. Schutzbereich › …` | 7 | – |
| **D1 II. Eingriff** `eingr`→`korpus` | Haken „Eingriff: ja“, Schulpflicht, gelber Block „unter dem Kreuz“, Straßenbild, mit und ohne Korpus; Sohn und K1 | `cross`, `school`, `road` | `II. Eingriff › …` | 7 | – |
| **D2 Was bedeutet das Kreuz?** `kultur`→`appell` | Kreuz „nur Kultur: nein“, Block „Glaubenssymbol … schlechthin“, Haken appellativ; Kampe nachdenklich | `building-community`, `cross`, `school` | `II. Eingriff › …` | 5 | – |
| **E1 III. Rechtfertigung** `vorb`→`auftrag` | Kreuz „Gesetzesvorbehalt: keiner“, Wortlautkarte Art. 7 Abs. 1 (Marker „Aufsicht“), Block Erziehungsauftrag | `book`, `building-bank`, `school` | `III. Rechtfertigung › …` | 6 | – |
| **E2 Praktische Konkordanz** `konk`→`grenze` | gelber Block, Haken religiöse Bezüge, Minimum an Zwang, Kreuz „Grenze überschritten“; Rohde, Kampe | `scale`, `book`, `hand-stop`, `cross` | `III. Rechtfertigung › …` | 5 | – |
| **E3 Glaubensfreiheit der anderen** `posit`→`wand` | allen zu, Kreuz Mehrheitsprinzip, Block Minderheitenschutz, Haken Freiwilligkeit, Kreuz „kein Ausweichen“; K1, K2 | `heart`, `scale`, `book`, `cross` | `III. Rechtfertigung › …` | 7 | – |
| **F1 Ergebnis** `erg`→`abw` | roter Block Leitsatz 1, „§ 13 Abs. 1 S. 3 VSO: nichtig“, grauer Block abweichende Meinung | `building-bank`, `circle-x`, `message-circle` | `Ergebnis · …` | 3 | – |
| **F2 Ergebnis im Fall** `ka2` | zurück in der 2a; Kampe sagt zu, das Kreuz abzunehmen; das Kreuz verschwindet bei „Rohde“ | tabler:`cross` (bis „Rohde“) | `Ergebnis im Fall · Das Kreuz kommt ab` | 2 | – |
| **G1 Bayern** `bayern`→`wid` | Gesetz 23.12.1995, heute Abs. 4; „Das Kreuz hängt weiter“; Wortlautkarte Art. 7 Abs. 3 S. 3 BayEUG (Marker „einsehbaren“, „Einigung“) | `map-2`, `cross`, `message-circle` | `Folgen in Bayern · …` | 5 | – |
| **G2 Folgefälle** `bverwg`→`flucht` | BVerwG 1999 (Haken, Widersprechender setzt sich durch), Kreuzerlass 2018, Kreuz „Pflicht zur Entfernung: nein“, Kläger, flüchtig | `building-bank`, `building`, `door-enter` | `Folgen in Bayern › …` | 7 | – |
| **H Klausurtipp** `tipp`→`fehler` | I.–III., Block Kopftuch/Kreuz (Verweis Folge 217), Kreuz „nie mit der Mehrheit“; Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp › …` | 9 | – |
| **I Merksatz** `merke`, `m2` | Marker „zwingen“, „Ausweichen“, „Mehrheit“; Lexi erklärt | – | `Merksatz` | 5 | – |

**Bildhalte:** laut Manifest (siehe ABNAHME.md), Soll bei 5:23 ≈ 9 je Minute, also ≥ 49. Mundzustände getrennt.
**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte/Pops; kein Zoom.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Bayern, Anfang der 1990er Jahre: Nach § 13 Abs. 1 S. 3 der bayerischen Volksschulordnung (VSO) gilt: „In jedem Klassenzimmer ist ein Kreuz anzubringen.“ Im Klassenzimmer der 2a einer staatlichen Grundschule hängt deshalb über der Tafel ein Kreuz. Die Grundschule ist keine Bekenntnisschule.
>
> Herr und Frau Rohde gehören keiner Kirche an und erziehen ihren schulpflichtigen Sohn, der die 2a besucht, ohne religiöses Bekenntnis. Sie bitten Schulleiter Kampe, das Kreuz abzuhängen. Er lehnt ab: Die Schulordnung schreibe das Kreuz vor, und es stehe für die abendländische Kultur.
>
> **Verletzt das Kreuz die Rohdes und ihren Sohn in Art. 4 Abs. 1 GG?**
