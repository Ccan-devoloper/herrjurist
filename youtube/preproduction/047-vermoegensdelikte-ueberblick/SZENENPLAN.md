# Folge 047 · Vermögensdelikte Überblick: Diebstahl, Betrug, Raub, Erpressung – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_047.py`](src/skript_047.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen, Themenplan-Format „Schema“, Überblicksfolge als **Landkarte** mit sieben kurzen, gewaltarmen Mini-Fällen an einem Fall: Klaus will die alte Spiegelreflexkamera aus Dagmars Kameraladen, ohne zu bezahlen. Frage → Sachverhalt (Grundfall, sieben Varianten) → Landkarte (Eigentums- und Vermögensdelikte) → § 242 (Wortlaut, Variante 1) → § 246 (Variante 2) → § 249 (Wortlaut, Variante 3) → § 263 (Wortlaut, Variante 4) → Sachbetrug/Trickdiebstahl (Variante 5) → §§ 253, 255 (Variante 6) → Streit Raub/räuberische Erpressung (Variante 7) → § 266 kurz → Klausurtipp (Lexi) → Entscheidungsbaum → Merksatz (Lexi).
**Verhältnis zu Folge 022 (Tankbetrug):** Dort trägt die Abgrenzung Diebstahl/Betrug ein Klassiker-Fall mit Zahlungsunwillen; hier dient sie als ein Feld der Landkarte und wird am Trickdiebstahl (Gewahrsamslockerung, BGH 1 StR 402/16) geschärft.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Dagmar (DA), um 50 | Inhaberin des Kameraladens, Opfer in allen Varianten | `standing/blazer-1` (Originalpose mit Beinprothese), Kopf `Medium Bangs 3`, Blazer Lila `#B8A9F5`, Hose Blau `#8DB3F2`, Haut `#C99470`. Mimiken `Calm`, `Smile` (redet), `Fear`, `Concerned|Serious`, `Serious`, `Suspicious`, `Awe` | `sabrina` (Frau, mittel) |
| Klaus (KL), um 40 | Kunde, Täter in allen Varianten | `standing/shirt-3`, Kopf `Short 4`, Hemd Grün `#8FD694`, schwarze Hose der Pose, Haut `#EDB98A`. Mimiken `Calm`, `Cheeky|Smile` (redet), `Rage|Serious` (droht), `Smile` (bittet), `Suspicious`, `Driven`, `Serious`, `Fear`, `Contempt` | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links zur Tafel bzw. im Fall Klaus zum Regal), `_r` blickt nach rechts (Dagmar zu Klaus in den Varianten 2–7; Klaus zur Ladentür in Variante 5).
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimiken nur als `Concerned|Serious`, `Cheeky|Smile`, `Rage|Serious`. Mundzustände a/o/e bei `DA_redet`, `KL_redet`, `KL_droht`, `KL_bittet` (je links/rechts) und Lexi. Keine Bärte. 68 Figuren-PNGs in `../peeps/op_047/` (Drive-Master).
- Die Beinprothese gehört zur Originalpose `blazer-1` und zur Ladeninhaberin, nicht zum Täter (FOLGE-ABLAUF). **Kein Herkunfts- oder Hautfarbenklischee:** Der Täter ist ein gewöhnlicher Kunde im grünen Hemd mit hellem Hautton, keine Karikatur, ohne Waffe. Vor der Festlegung verworfen: `robot_dance-3` für Klaus (gleiche Silhouette wie Lexi).
- **Namen** mit eindeutig deutscher Aussprache, in keiner Vorfolge vergeben (Liste des Auftrags; zusätzlich gegen alle Skripte und Dokumente 001–046 geprüft – „Ralf“ wurde verworfen, weil in 007 vergeben): Dagmar, Klaus.
- **Stimmen** nur aus dem zugeteilten Pool (stephan, sabrina; helmut und lucy nicht gebraucht). Vorfolge 046 (hilde, timo): keine Überschneidung. Lea nicht verwendet.

**Abweichung von den letzten Folgen:** 046 (Elektrohändler/Waschmaschine), 045 (Klausursaal), 044 (Marktplatz), 043 (Werbeagentur/Möbelhaus), 042 (Dorffest). Hier neu: kleiner **Kameraladen in der Altstadt** (Regal mit Kameras, Ladentür, Theke mit Kasse) und danach Tafeln mit einer **kleinen Landkarte rechts oben** (Spalten Eigentum/Vermögen, aktuelles Feld gelb, behandelte weiß), die einer Sprechblase kurz weicht. Neue Posen (`blazer-1`, `shirt-3`).
**Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Kameraladen** `fall`→`frage2` | Regal mit vier Kameras (die gelbe = Spiegelreflexkamera, Pille „300 €“), Ladentür, Theke mit Kasse; Dagmar hinter der Theke (Namensschild auf der Theke), Klaus kommt herein, Blase „Die Kamera kriege ich schon, so oder so.“, Frage-Pillen | tabler:`camera`, `door`, `cash-register` | `Fall · Der Kameraladen` (ab 0,0 s) → `Fall · Die Frage` | ≈ 14 | Ladenglocke (`szene_047glocke_1`) beim Eintreten |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10,4 s | – | `Sachverhalt` | 1 | – |
| **C Landkarte** `karte`→`bruecke` | zwei Säulen, Felder zum gesprochenen Delikt; rosa Band über Raub/räub. Erpressung | – | `Überblick · Landkarte der Vermögensdelikte` | ≈ 16 | – |
| **D Diebstahl** `p242`→`v1ok` | Wortlautkarte § 242 I, Definition, Variante 1; Kamera verschwindet „unbemerkt eingesteckt“ | tabler:`camera` | `A. Eigentumsdelikte › Diebstahl, § 242 StGB` → `… › Variante 1` | ≈ 9 | – |
| **E Unterschlagung** `p246`→`anv` | Dagmar leiht (Kamera zwischen beiden), „verkauft“ mit Internet-Symbol | tabler:`camera`, `world-www` | `A. Eigentumsdelikte › Unterschlagung, § 246 StGB` → `… › Variante 2` | ≈ 10 | – |
| **F Raub** `p249`→`v5ok` | Wortlautkarte § 249 I; Blase Klaus „Keine Bewegung, sonst gibt es Schläge!“ (Landkarte weicht), Dagmar erschrickt; Kamera wandert vom kleinen Regal zu Klaus | tabler:`camera`; Regal als Linien | `A. Eigentumsdelikte › Raub, § 249 StGB` → `… › Variante 3` | ≈ 11 | – |
| **G Betrug** `p263`→`v3ok` | Wortlautkarte § 263 I (bis „unterhält, …“), sechs Merkmal-Pillen; Blase Dagmar „Ach so, dann nehmen Sie sie mit.“; Kamera geht zu Klaus | tabler:`camera` | `B. Vermögensdelikte › Betrug, § 263 StGB` → `… › Variante 4` | ≈ 13 | – |
| **H Trickdiebstahl** `trick`→`wille` | Blase Klaus „Darf ich mal kurz durchschauen?“; Klaus rennt mit der Kamera zur Ladentür; zwei Blöcke „Opfer gibt weg: Betrug“ / „Täter nimmt: Diebstahl“ | tabler:`camera`, `door-exit` | `B. Vermögensdelikte › Sachbetrug oder Trickdiebstahl? › Variante 5` | ≈ 12 | Ladenglocke beim Hinausrennen |
| **I Erpressung** `p253`→`p255` | Tatbestand § 253 zeilenweise, Variante 6 (Internet-Symbol, „Kamera für 10 €“), Block § 255 | tabler:`world-www`, `camera` | `B. Vermögensdelikte › Erpressung, § 253 StGB` → `… › Variante 6` → `B. Vermögensdelikte › räuberische Erpressung, § 255 StGB` | ≈ 13 | – |
| **J Streit** `streit`→`schl2` | zwei Spalten Rechtsprechung / Lehre, Haken „Variante 7: § 255“, Pille „es bleibt beim Raub“ | tabler:`camera` | `Streit › Raub oder räuberische Erpressung? › Variante 7` → `… › Rechtsprechung` → `… › Lehre` | ≈ 16 | – |
| **K Untreue** `p266`→`p266d` | Block Vermögensbetreuungspflicht, Beispiel, Kreuz für Klaus | tabler:`briefcase` | `B. Vermögensdelikte › Untreue, § 266 StGB` | ≈ 5 | – |
| **L Klausurtipp** `tipp`→`tipp4` | hellgelbe Tafel, Lexi warnt; Kamera mit „nur ein Wochenende“ | Warnsymbol (Streamline Freehand), tabler:`camera` | `Klausurtipp · Streit nur entscheiden, wo er sich auswirkt` | ≈ 8 | – |
| **M Entscheidungsbaum** `sch`→`e4` | vier Fragen mit Pfeil und Ergebnissen, progressiv | – | `Entscheidungsbaum` | ≈ 11 | – |
| **N Merksatz** `merke`→`m3` | Lexi erklärt, drei Marker | – | `Merksatz` | ≈ 5 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops; Handlung als Zustandswechsel (Kamera im Regal → weg; Kamera zwischen den Figuren → bei Klaus; Klaus an der Ladentür).
**Geräusche:** nur die Ladenglocke an den beiden sichtbaren Türvorgängen (siehe `geraeusche_herkunft.json`).
**Gewalt zurückhaltend:** keine Waffen, kein Blut, keine Schlagbewegung; die Drohung nur als Sprechblase, Dagmar erschrickt.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 242 I (wörtlich vorgelesen), § 249 I (Merkmale gesprochen, Marker synchron), § 263 I bis „unterhält, …“ (Merkmale gesprochen, amtliche Schreibung „daß“), wörtlich nach gesetze-im-internet.de mit Normangabe.
**Mini-Landkarte:** ab Szene D rechts oben (x 1268–1872, y 58–388); in F, G und H während der Sprechblasen ausgeblendet.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Samstagvormittag in der Altstadt: Dagmar verkauft in ihrem Laden gebrauchte Kameras, darunter eine alte Spiegelreflexkamera für 300 Euro. Klaus gefällt die Kamera, bezahlen will er sie nicht.
>
> Variante 1: Klaus steckt die Kamera unbemerkt ein und geht. Variante 2: Dagmar leiht Klaus die Kamera für ein Wochenende. Erst später beschließt er, sie zu verkaufen, und verkauft sie. Variante 3: Klaus droht Dagmar Schläge an („Keine Bewegung, sonst gibt es Schläge!“) und nimmt die Kamera selbst aus dem Regal. Variante 4: Klaus behauptet, Dagmars Bruder habe die Kamera schon bezahlt und ihn zum Abholen geschickt. Dagmar glaubt ihm und gibt sie ihm mit. Variante 5: Klaus fragt, ob er kurz durch die Kamera schauen darf. Dagmar reicht sie ihm, er rennt damit hinaus. Variante 6: Klaus droht, Dagmars Laden im Internet mit erfundenen Vorwürfen schlechtzumachen. Dagmar verkauft ihm die Kamera deshalb für 10 Euro. Variante 7: wie Variante 3, doch Dagmar reicht Klaus die Kamera.
>
> **Wie hat sich Klaus jeweils strafbar gemacht?**

Hinweis: Die Marken der Varianten im Skript heißen aus der Entstehung `v5` (= Variante 3), `v3` (= Variante 4), `v4` (= Variante 5), `v7` (= Variante 6), `v6` (= Variante 7); maßgeblich ist der gesprochene Text.
