# Folge 015 · Strafrecht AT Überblick: Welches Prüfungsschema wann? – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_015.py`](src/skript_015.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Klausurpraxis (Fr), Themenplan-Format „Schema“. Ein frei erfundener Alltagsfall („Gartenfest-Fall“) mit fünf Personen trägt den Überblick: Jede Person steht für ein Grundschema des Allgemeinen Teils. Ausgangspunkt ist der Grundfall (allein, vorsätzlich, aktives Tun, vollendet), dann vier Weichen in fester Reihenfolge: 1. allein oder mit anderen? (Ina, Beihilfe § 27) → 2. vollendet oder versucht? (Rudolf, §§ 242, 22, 23) → 3. Vorsatz oder Fahrlässigkeit? (Bernd, §§ 15, 229) → 4. Tun oder Unterlassen? (Gerda, §§ 223, 13). Danach Klausurtipp (Weichen kombinieren), Entscheidungsbaum als Klausurschema, Merksatz. Die Schemata sind ausdrücklich als Klausurkonvention gekennzeichnet.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Otto (OT), um 65 | Kleingärtner, Geschädigter (Topf, Mäher, Brandblase, Biss) | `standing/crossed_arms-1` (Reihe -1: lila Oberteil `#B8A9F5`, schwarze Hose), Kopf `No Hair 2`, Brille `Glasses 3`, Haut `#EBC4A0`; Mimiken `Calm`, `Suspicious` (Streit), `Concerned|Serious` (redet), `Fear` (Schreck), `Very Angry`, `Serious` | `helmut` (Mann, älter) |
| Konrad (KO), um 45 | Nachbar, zerschlägt den Topf (Grundfall, Täter) | `standing/robot_dance-2` (Reihe -2: schwarzes Oberteil, blaue Hose `#8DB3F2`), Kopf `Short 1`, Haut `#E8B98F`; Mimiken `Calm`, `Driven` (redet), `Very Angry`, `Smile`, `Serious`, `Concerned|Serious` | `stephan` (Mann, mittel) |
| Ina (IN), um 25 | Nachbarin, reicht den Hammer (Gehilfin) | `standing/resting-2` (schwarzes Oberteil, rote Hose `#F07A6A`), Kopf `Medium 2`, Haut `#B07552`; Mimiken `Calm`, `Cheeky|Smile`, `Serious`, `Concerned|Serious` | – (spricht nicht) |
| Rudolf (RU), um 50 | Gast, will den Mäher mitnehmen (Versuch) | `standing/walking-2` (schwarzes Oberteil, gelbe Hose `#F9D56E`), Kopf `Short 3`, Haut `#F0C8A8`; Mimiken `Calm`, `Cheeky|Smile`, `Driven` (zieht), `Fear`, `Concerned|Serious`, `Serious` | – (spricht nicht) |
| Bernd (BE), um 35 | Grillmeister, Spiritus in die Glut (Fahrlässigkeit) | `standing/easing-2` (orange Jacke `#F9A66C`, schwarzes Oberteil, graue Hose `#5A5A6A`), Kopf `Flat Top`, Haut `#8D5A3B`; Mimiken `Calm`, `Smile`, `Fear`, `Concerned|Serious`, `Serious` | – (spricht nicht) |
| Gerda (GE), um 70 | Hundehalterin, ruft den Hund nicht zurück (Unterlassen) | `sitting/closed_legs-1` (grüne Jacke `#8FD694`) auf einer Picknickdecke, Kopf `Gray Bun`, Brille `Glasses 2`, Haut `#E8B894`; auf 310 px statt 480 px skaliert (Kopf gleich groß wie stehend); Mimiken `Calm`, `Suspicious`, `Contempt` (redet, böse), `Serious`, `Concerned|Serious` | `elinor` (Frau, älter, „ruppige Tante“) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Stimmenpool laut Koordinator:** ela_warm, stephan, elinor, helmut. Drei Figuren sprechen (Konrad, Otto, Gerda); `ela_warm` wird nicht gebraucht (Ina spricht nicht). Keine Lea.
**Namen:** eindeutig deutsch ausgesprochen (Vorgabe vom 01.10.2026): Otto, Konrad, Ina, Rudolf, Bernd, Gerda. Rudolf hieß im Entwurf „Lothar“ (wegen des „th“ vor der Vertonung ersetzt). Ergebnis der Namensprüfung in `ABNAHME.md`.
**Alle Grundbilder mit geschlossenem Mund** (`Augen|Mund` bei Concerned und Cheeky); Mundzustände a/o/e nur bei `KO_redet`, `OT_redet`, `GE_redet` (je links/rechts) und Lexi. Grundansicht gespiegelt = blickt nach links, `_r` = blickt nach rechts. Keine Prothesen-Posen; Rudolf ohne Bart (der zuerst gewählte große Schnurrbart wirkte wie eine Schurkenkarikatur). Figuren-PNGs: `../peeps/op_015/` (92 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 013 Luftsicherheitsgesetz (Flugzeug, Ministerium), 012 Zivilprozess, 011 Uferweg mit Radfahrer, 009 Werkstatt/Fahrradladen/Straßenecke. Hier: Kleingartenanlage bei Tag (Wiesenstreifen, Zaunfelder, Bäume, Grill, Picknickdecke), sechs neue Figuren mit neuen Posen (`crossed_arms-1`, `robot_dance-2`, `resting-2`, `walking-2`, `easing-2`, `sitting/closed_legs-1`). Kein Fahrrad, kein Laden, keine Flucht wie in 009/011.

## Szenen

Alle Szenen auf Cremegrund (Tageslicht). 18 Folien, 17 stumme Schiebeblenden.

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Gartenfest** `fall`→`schlag` | Wiese, Otto links (blickt nach rechts), Blumentopf, Konrad spricht Ina an, Hammer wandert von Ina zu Konrad, Konrad geht zum Topf und zerschlägt ihn | ph:`tree` (Grün), tabler:`sun` (Gelb), tabler:`fence` (Weiß), ph:`potted-plant` (Orange/Grün, zerschlagen gekippt), tabler:`hammer` (Grau/Orange) | `Fall · Sommerfest im Kleingarten` (ab 0,0 s) | Garten mit Otto · Otto streng, „Streit um die Hecke“ · Konrad · Konrad redet (Blase) · Ina · Hammer bei Ina · Hammer wandert · Ina cool, „reicht den Hammer“ · Konrad geht zum Topf · Topf gekippt, „Topf zerschlagen“, Otto erschrocken | Topf zerbricht (`schlag`) |
| **B Am Zaun** `rudolf`→`kette` | Rudolf links, Ottos Rasenmäher, Pfosten; Rudolf zieht, Kette am Pfosten | tabler:`lawn-mower` (Rot/Weiß), fluent-emoji-high-contrast:`chains` (gedreht), Pfeil | `Fall · Am Zaun: Ottos Rasenmäher` | Rudolf ruhig · „will ihn mitnehmen und behalten“ · Rudolf am Griff · Pfeil „zieht los“ · Kette, Ring, „angekettet“ · „kein Werkzeug“, Rudolf ertappt | – |
| **C Am Grill** `grill`→`blase` | Bernd mit Spiritusflasche, Grill, Otto rechts | tabler:`grill` (Grau), tabler:`bottle` (Blau), tabler:`flame` (Orange) | `Fall · Am Grill` | Bernd froh · Flasche, „Brennspiritus“ · Pfeil in die Glut · „damit es schneller geht“ · Stichflamme, beide erschrocken · Ring an Ottos Hand, „Brandblase an der Hand“, Bernd ertappt | Stichflamme (`flamme`) |
| **D Gerdas Hund** `hund`→`biss` | Gerda sitzt auf der Picknickdecke, Hund neben ihr, Otto rechts; Hund läuft zu Otto | fluent-emoji-high-contrast:`dog` (Orange) | `Fall · Gerdas Hund` | Hund, „knurrt“, Otto erschrocken · Otto redet (Blase) · Gerda redet (Blase) · „Gerda bleibt sitzen“ · Hund an Ottos Wade, Ring, „Biss in die Wade“ | Hund knurrt (`hund`) |
| **E Fallfrage** `frage`→`fuenf` | Tafel links, fünf Personen rechts (klein) | – | `Fallfrage · Welches Schema für wen?` | Bearbeitervermerk · „5 Personen“ · „jede braucht ein anderes Prüfungsschema“, alle denken | – |
| **F Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **G Grundfall und Weichen** `weichen`→`konv` | Tafel links, rechts Gleisbild: Grundfall oben, vier rote Abzweige | – | `Überblick › Grundfall` → `› vier Weichen` → `› Klausurkonvention, kein Gesetz` | Grundfall · vier Weichen zeilenweise mit Abzweig · Pille „Klausurkonvention, kein Gesetz“ · „Schemata ordnen …“ | – |
| **H A. Konrad** `konrad`→`schuld` | Tafel, Konrad rechts mit Hammer und zerschlagenem Topf | ph:`potted-plant` (gekippt), tabler:`hammer` | `A. Konrad › Grundfall` → `A. Konrad, § 303 I StGB` → `› I. Tatbestand` → `› II. Rechtswidrigkeit` → `› III. Schuld` | § 303 I mit Normtext · objektiv ✓ · subjektiv ✓ · II · III · beide ✓ | – |
| **I B. Ina** `ina`→`mitt` | Tafel, Konrad (1) und Ina (2) rechts, Hammer mit Pfeil zu Konrad | tabler:`hammer` | `B. Ina › 1. Weiche: allein oder mit anderen?` → `› Täter vor Teilnehmer` → `› Beihilfe, § 27 I StGB` → `› keine Mittäterin` | Weiche · „erst der Täter, dann der Teilnehmer“, Ziffern 1/2 · § 27 I wörtlich · drei ✓ · ✗ Mittäterin · (+) Beihilfe | – |
| **J1 C. Rudolf: Vorprüfung** `rudolf2`→`p242` | Tafel, Rudolf, Mäher mit Kette | tabler:`lawn-mower`, fluent:`chains` | `C. Rudolf › 2. Weiche: vollendet oder versucht?` → `› 0. Vorprüfung` → `› Vorprüfung › Strafbarkeit, § 242 II StGB` | Weiche · „noch da“ · nicht vollendet ✓ · § 242 II ✓ | – |
| **J2 C. Rudolf: Tatbestand, Rücktritt** `entschl`→`ruecktr` | wie J1, Ring um die Kette | wie J1 | `› I. 1. Tatentschluss` → `› I. 2. unmittelbares Ansetzen, § 22 StGB` → `› IV. Rücktritt, § 24 StGB` | Tatentschluss ✓ · § 22 wörtlich · gezogen ✓ · II/III · IV · ✗ fehlgeschlagen · (+) versuchter Diebstahl | – |
| **K1 D. Bernd: Weiche** `bernd`→`p229` | Tafel, Bernd, Grill mit Flamme | tabler:`grill`, `flame` | `D. Bernd › 3. Weiche: Vorsatz oder Fahrlässigkeit?` → `› § 15 StGB` → `› fahrlässige Körperverletzung, § 229 StGB` | ✗ Vorsatz · § 15 wörtlich · ✓ § 229 mit Normtext | – |
| **K2 D. Bernd: Tatbestand** `erfolg`→`subj` | wie K1, Ring um die Flamme, „Brandblase“ | wie K1 | `D. Bernd, § 229 StGB › I. Tatbestand` → `› objektive Sorgfaltspflichtverletzung` → `› Gefahr verwirklicht` → `› kein subjektiver Tatbestand` | Erfolg/Handlung/Kausalität ✓ · Sorgfaltsblock · Spiritus ✓ · Gefahr verwirklicht ✓ · ✗ subjektiver TB · Schuld-Zeile | – |
| **L1 E. Gerda: Weiche** `gerda`→`p13` | Tafel, Gerda sitzend, Hund | fluent:`dog` | `E. Gerda › 4. Weiche: Tun oder Unterlassen?` → `› § 13 I StGB` | Weiche · „nichts getan“ · § 13 I wörtlich · „rechtlich einstehen?“ | – |
| **L2 E. Gerda: Tatbestand** `biss2`→`gvors` | wie L1, Ring um den Hund, „Halterin“ | fluent:`dog` | `E. Gerda, §§ 223 I, 13 I StGB › I. Tatbestand › Erfolg` → `› Handlung möglich` → `› Hund hätte gehorcht` → `› Garantenstellung` → `› Entsprechung` → `› Vorsatz` | sechs ✓ zum Wort · (+) KV durch Unterlassen | – |
| **M Klausurtipp** `tipp`→`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Weichen kombinieren` | zeilenweise, Block §§ 229, 13 I | – |
| **N Klausurschema** `sch`→`e5` | breite Karte, Entscheidungsbaum: Frage links (Pink), „ja“-Pfeil zur Antwort rechts, „nein“-Pfeil zur nächsten Frage | – | `Klausurschema · Entscheidungsbaum` | Titel · je Weiche Frage, dann Antwort zum Wort „Dann“ · Grundschema | – |
| **O Merksatz** `merke`→`m2` | Lexi erklärt (redet), zwei Zeilenblöcke mit Marker | – | `Merksatz` | Marker zu Tatbestand, Rechtswidrigkeit, Schuld, Tatbestand | – |

**Geräusche:** drei Handlungsgeräusche, Freesound CC0, `sfx3/szene_015topf_1.wav`, `szene_015flamme_1.wav`, `szene_015hund_1.wav`; Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Gewalt zurückhaltend:** Schlag und Biss werden nicht ausgespielt (Topf gekippt mit Pille, Hund an der Wade mit Ring und Pille), keine Wunden.

## Sachverhaltskarte (Szene F, erscheint vollständig)

> Sommerfest in der Kleingartenanlage. Konrad liegt mit Otto im Streit um die Hecke. Er bittet Ina um ihren Hammer, um Ottos Blumentopf zu zerschlagen; Ina weiß das, hat selbst kein Interesse daran und reicht ihm den Hammer. Konrad zerschlägt den Topf. Rudolf will Ottos Rasenmäher mitnehmen und behalten, packt den Griff und zieht. Der Mäher ist angekettet, was Rudolf übersehen hat; Werkzeug hat er nicht. Er lässt den Mäher stehen.
>
> Bernd gießt Brennspiritus in die Grillglut, damit es schneller geht, und vertraut darauf, dass nichts passiert. Eine Stichflamme verursacht bei Otto eine Brandblase an der Hand. Gerdas Hund knurrt Otto an; Gerda sieht, dass er gleich zubeißt. Ein Ruf würde genügen, der Hund gehorcht ihr zuverlässig. Gerda bleibt sitzen, weil sie den Biss will. Der Hund beißt Otto in die Wade. Otto stellt gegen alle Strafantrag. (Frei erfundener Übungsfall.)
>
> **Wer hat sich wie strafbar gemacht?**
