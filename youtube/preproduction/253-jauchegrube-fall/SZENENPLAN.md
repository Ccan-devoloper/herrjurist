# Folge 253 · Jauchegrube-Fall: dolus generalis oder Versuch plus Fahrlässigkeit? – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_253.py`](src/skript_253.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · StGB AT · Klassiker-Fall. Fiktiver Übungsfall, dem echten Fall nachgebildet (Personen fiktiv); der echte Fall (BGHSt 14, 193) nur abstrakt auf einer Tafel. Ablauf laut Auftrag: 1. Hook (Garten, Teich) → Frage → Sachverhalt → echter Fall (abstrakt) → 2. Problem: zweiaktiges Geschehen → objektiver Tatbestand (Kausalität, Zurechnung) → 4. § 16 Abs. 1 S. 1 (Wortlautkarte), Vorsatz bei der Tathandlung, Kausalverlauf (Verweis 068) → 3. Lösungen: 1. dolus generalis (historisch, vom BGH abgelehnt), 2. BGH (unwesentliche Abweichung; bedingter Vorsatz ändert nichts) und heutige Formel (4 StR 223/15 Rn. 12), 3. Versuchslösung (Lehre), 4. vermittelnd: Tatplan → 5. Ergebnis im Fall nach BGH (und nach den Gegenansichten) → 6. Klausurtipp, Schema, Merksatz mit Lexi. Hauptfilm 6:06,7.

**Darstellung (Vorgabe Koordinator):** keine Gewaltszene, kein Würgen, keine Leiche, kein Ertrinken im Bild. Die Nachbarin ist **keine Figur** (auch keine Silhouette): Hinter dem Zaun bleibt die Szene leer, nur ihr Haus steht dort. Symbole statt Handlung: Warndreieck bei „greift … an“, Uhr bei „regungslos“ und bei „Erst im Wasser stirbt sie“, Wasserringe auf dem Teich bei „versenkt“ (verschwinden bei „stirbt“), Herzschlag-Symbol bei „nur bewusstlos“, Pillen. Brunhilde neutral (`Calm`, `Serious`, `Suspicious`, `Concerned|Serious`, `Fear`, `Tired`, `Solemn`, `Awe`; beim Streit `Very Angry` mit geschlossenem Mund), keine fiese Mimik, keine Karikatur. Kein Geräusch.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Brunhilde (BR) | Täterin im Übungsfall (um 50) | `standing/crossed_arms-1` (Oberteil Rostrot `#C0603A`, schwarze Hose der Pose), Kopf `Medium 3`, Haut `#EDB98A`; redet: `Concerned\|Serious` | `sabrina` (Frau, mittel) |
| Nachbarin | Opfer | **keine Figur**, nie im Bild, namenlos, kein Namensschild | – |
| Lexi | Klausurtipp (warnt), Schema und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Pose blickt im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts (Kontaktbild `out/besetzung_253.png`). A1: Brunhilde steht rechts und blickt nach links zum Zaun; A2: nach links zum Teich; Tafelfolien: nach links zur Tafel.
- **Grundmimiken alle mit geschlossenem Mund**; Mundzustände a/o/e nur in `BR_redet` (links/rechts) und Lexi. Kein Bart, keine Prothesen-Pose, keine Polka Dots. 34 Figuren-PNGs in `../peeps/op_253/` (Drive-Master).
- **Name:** Brunhilde – eindeutig deutsch, nicht auf der Koordinatorliste, nicht in `namen_reserviert.txt`, `git grep -iw` über `youtube/` (`*.py/*.md/*.json/*.csv`) ohne Treffer (Mechthild verworfen: in 239/241 erwähnt). Vor der Vertonung als „253: Brunhilde“ eingetragen. Die Nachbarin bleibt namenlos.
- **Stimme** aus dem Pool william, sabrina, marc, laura_ruhig: nur eine Fallfigur (Frau) → `sabrina`. Keine Männerstimme nötig (die Opferrolle hat keine Figur). Kein Lea-Einsatz.

**Abweichung von den letzten Folgen:** 250 (`shirt-4`, `crossed_arms-2`, Silhouette `walking-1`), 251 (`easing-1`, `resting-2`), 252 (`pointing_finger-2`, `blazer-3`, `walking-2`, `robot_dance-2`) – `crossed_arms-1` in keiner davon; Rostrot neu gegenüber Bordeaux/Jeansblau (250), Grün/Koralle (251), Schiefergrau/Graublau/Lila (252). Schauplätze **Garten mit Zaun** und **Teich** (Tageslicht, Cremegrund) – neu gegenüber 250 (Büro, Kanal bei Nacht), 247 (Zimmer, Schlafzimmer), 068 (Wald/Hochsitz).

## Szenen

| Nr. | Cue(s) | Ort / Handlung | Figuren | Tafel / Pillen / Requisiten (Iconset:Name) | Prüfpfad | Geräusch |
|---|---|---|---|---|---|---|
| A1 | `fall`–`br1` | Garten: ab 0,0 s Baum, Haus der Nachbarin hinter dem Zaun, Zaun, Tulpen, Brunhilde mit Namensschild; Weg-Symbol bei „Weg“; Sonne bei „Nachmittags“, Sprechblasen-Symbol bei „eskaliert“; Warndreieck bei „greift … an“; Uhr bei „regungslos“; Brunhilde redet | BR ruhig → wut → ernst → angst → redet | Pillen „Brunhilde und ihre Nachbarin streiten seit Jahren über den Weg zum Teich.“, „Eines Nachmittags eskaliert der Streit am Gartenzaun.“, „Brunhilde greift die Nachbarin an.“ + „Dass sie dabei sterben kann, nimmt Brunhilde in Kauf.“, „Die Nachbarin bleibt regungslos liegen.“; Blase „Sie atmet nicht mehr. / Sie ist tot.“ (Stil C); ph:tree, house, flower-tulip, sun; tabler:route, messages, alert-triangle, clock; Zaun programmatisch | Fall · Brunhilde und ihre Nachbarin … Fall · „Sie ist tot.“ (5 Stände) | – |
| A2 | `verst`–`stirbt` | Teich (Wasserfläche, Schilf, Baum): Glühbirne bei „beschließt“; Wasserringe ab „versenkt“; Herzschlag bei „bewusstlos“; bei „Erst im Wasser stirbt sie“ Ringe und Herzschlag weg, ruhige Wasserfläche, Uhr | BR ernst → müde → ruhig | Pillen „Erst jetzt beschließt Brunhilde, die vermeintliche Leiche verschwinden zu lassen.“, „Sie versenkt die Nachbarin im Teich.“, „Doch die Nachbarin war nur bewusstlos.“, „Erst im Wasser stirbt sie.“; tabler:bulb, ripple, clock; ph:plant, tree, heartbeat | Fall · Die vermeintliche Leiche … Fall · Erst im Wasser stirbt sie (4) | – |
| A3 | `frage`, `frage2` | Tafel „Die Frage“ | BR | tabler:ripple, scale | Die Frage · … | – |
| B | `sv` | Sachverhaltskarte (≈ 10 s, Hinweis zum Anhalten, ohne Fiktiv-Hinweis) | – | Pille „Ist Brunhilde wegen vollendeten Totschlags strafbar?“ | Sachverhalt | – |
| C | `echt`–`echt3` | Tafel „Der Jauchegrube-Fall (BGH 1960)“: Fundstelle, abstrakter Sachverhalt, Block „Erst dort stirbt die Frau.“ | BR | tabler:scale, alert-triangle, ripple, clock | Der Jauchegrube-Fall, BGHSt 14, 193 · … | – |
| D1 | `zwei`–`akt2` | Tafel „Das Problem: zwei Akte“: zwei Blöcke mit Pfeil | BR | tabler:timeline, alert-triangle, ripple, arrow-right, clock | Das Problem · zweiaktiges Geschehen › … | – |
| D2 | `obj`–`zurech` | Tafel „Objektiver Tatbestand“: Haken Kausalität, eigenes späteres Handeln (BGHSt 14, 193, 194; 4 StR 223/15 Rn. 10), Lehre: Zurechnung | BR | tabler:list-check, link, arrows-join, scale | Brunhilde, § 212 StGB (Angriff) › Objektiv › … | – |
| D3 | `p16`–`f68` | Tafel „Subjektiver Tatbestand: Vorsatz“: Wortlautkarte § 16 Abs. 1 Satz 1 (Marker „bei Begehung der Tat“, „Umstand“); Zeitpunkt; Kausalverlauf (Rn. 12); Verweis Folge 068 | BR | tabler:book, clock, route | … › Vorsatz? § 16 Abs. 1 Satz 1 … | – |
| E1 | `dg`–`dg4` | Tafel „1. dolus generalis (historisch)“: Gesamtvorsatz, Folge, Kreuz „BGH 1960: abgelehnt“ bei „abgelehnt“, Zitat, „Heute nicht mehr vertreten“ | BR | tabler:history, link, scale, archive | … › Vorsatz bzgl. Kausalverlauf › 1. … | – |
| E2 | `bgh`–`bedingt` | Tafel „2. BGH: unwesentliche Abweichung“ | BR | tabler:scale, alert-triangle, route, target | … › 2. BGH: … | – |
| E3 | `formel`, `verdeck` | Tafel „Der BGH heute: die Formel“ (Rn. 12), Verdeckungshandlung | BR | tabler:eye, scale, ripple | … › 2. BGH heute / Verdeckungshandlung | – |
| E4 | `vers`–`vers4` | Tafel „3. Versuchslösung (Teil der Lehre)“: 1. Akt Versuch, 2. Akt § 222, Kritik | BR | tabler:unlink, book, clock, alert-triangle | … › 3. … | – |
| E5 | `plan`, `plan2` | Tafel „4. Vermittelnd: der Tatplan“ | BR | tabler:map-2, zoom-question | … › 4. … | – |
| F | `erg`–`e6` | Tafel „Zurück zu Brunhilde“: Haken e1–e3, Block BGH (+), Mordmerkmale offen, Block Versuchslösung, Tatplan | BR | tabler:ripple, link, eye, scale, unlink, map-2 | … › Subsumtion … Ergebnis › … | – |
| G | `tipp`–`k2` | Klausurtipp | Lexi (warnt) | Warnsymbol (Streamline Freehand) | Klausurtipp › … | – |
| H | `sch`–`s4` | Klausurschema progressiv (§ 212 durch den Angriff: I. 1. objektiv (+), 2. a) Vorsatz Tod (+), b) Kausalverlauf: Streit, BGH (+); II., III.) | Lexi (erklärt) | (+) | Klausurschema › … | – |
| I | `merke`–`m3` | Merksatz mit Markern „Generalvorsatz“, „unwesentliche Abweichung“, „vollendeter Tat“ | Lexi | – | Merksatz | – |

**Sachverhaltskarte:** wörtlich in `src/folien_253.py` (`sachverhalt_253`), Schrift 34 px, ohne Fiktiv-Hinweis und ohne Quellenzeile (Übungsfall).
**Lizenzen:** Open Peeps (CC0), Tabler Icons (MIT), Phosphor Icons (MIT: tree, house, flower-tulip, sun, plant, heartbeat), Streamline Freehand (CC BY 4.0, Warnsymbol, Namensnennung in der Beschreibung); kein Geräusch.
