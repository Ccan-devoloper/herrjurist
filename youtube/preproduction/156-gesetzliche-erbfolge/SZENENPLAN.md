# Folge 156 · Gesetzliche Erbfolge §§ 1924 ff. BGB: Wer erbt ohne Testament? – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_156.py`](src/skript_156.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Zivilrecht/Erbrecht, Format Schema. Beispielfall nach dem Plan-Hook („Der Vater stirbt ohne Testament – zurück bleiben Ehefrau, eine Tochter und ein Enkel vom verstorbenen Sohn“): Kurt stirbt mit 78 ohne Testament; Ehefrau Christa (Zugewinngemeinschaft), Tochter Verena mit Tochter Mathilda, Enkel Severin (Sohn des vorverstorbenen Andreas), Bruder Egbert. Ablauf: Fall → Frage → Sachverhalt → Stammbaum (baut sich mit dem Sprechtext auf) → § 1922 Abs. 1 (Wortlaut, Universalsukzession, Verweis Folge 040) → Ordnungen (Wortlaut § 1924 Abs. 1, Stufen §§ 1925, 1926) → § 1930 (Wortlaut, Egbert ausgeschlossen) → § 1924 Abs. 2 (Wortlaut, Repräsentation) → § 1924 Abs. 3, 4 (Wortlaut, Eintritt, Stämme) → § 1931 Abs. 1 S. 1 (Wortlaut) → § 1931 Abs. 3, § 1371 Abs. 1 (Wortlaut) → Ergebnis als Bruch-Diagramm mit Gegenprobe → Variante Gütertrennung § 1931 Abs. 4 (Wortlaut) → Klausurtipp (Lexi, § 2032) → Prüfschema I.–V. → Merksatz.
**Länge:** Hauptfilm 5:38,6 bei 4.713 Skriptzeichen (Grenze 7:00/6.200); Begründung in [`ABNAHME.md`](ABNAHME.md).

## Takt beim Todesfall (Auftrag, Vorbild Folge 128)

- Der Tod von Kurt und Andreas erscheint **nur als Text** (graue Pillen „Kurt ist mit 78 Jahren gestorben.“, „Andreas, Vater von Severin: vor 3 Jahren gestorben“; im Stammbaum „Erblasser“, „vorverstorben“, „verstorben“).
- **Kurt und Andreas sind keine Figuren**, nur Namen im Stammbaum mit **grauem Rahmen** und grauer Fläche. Die Eltern von Kurt ebenso.
- Kein Sterbebett, kein Sarg, kein Grab, **kein Kreuz und kein †**; die Bleistift-Kreuze stehen nur bei „erbt nicht“ (Egbert, Mathilda) und nie an einem Verstorbenen.
- Ruhige Gestaltung: Esszimmer mit Kommode, gerahmtes Familienfoto (nur das Familien-Symbol tabler `users-group`, keine Person), eine Blume. Ruhige Mimiken (`Solemn`, `Tired`, `Calm`, `Concerned|Serious`); `Smile` nur einmal kurz bei Verena und Severin, als ihr Erbteil feststeht. Ein leises Handlungsgeräusch (Schritte), keine Musik.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Christa (CH), um 75 | Ehefrau des Erblassers, Witwe; spricht nicht | `standing/easing-2` (Jacke Dunkelblau `#2E3550`, schwarzes Oberteil, Hose Grau `#8A8A96`), Kopf `Gray Bun` (Haar `#DCD7D7`), Brille `Glasses 4`, Haut `#F0C8A8`; `Solemn`, `Tired`, `Calm`, `Serious` | – |
| Verena (VE), um 45 | Tochter; spricht nicht | `standing/shirt-3` (Hemdbluse Blau `#8DB3F2`, schwarze Hose), Kopf `Long`, Haut `#E8B48F`; `Solemn`, `Concerned\|Serious`, `Serious`, `Calm`, `Smile` | – |
| Mathilda (MA), um 6 | Tochter von Verena (Enkelin); spricht nicht | `standing/walking-2` (schwarzes T-Shirt, Hose Rot `#F07A6A`), Kopf `Buns` (zwei Haarknoten), Haut `#E8B48F`; **Kind: 58 % der Erwachsenenhöhe** über `hoehe`; `Calm`, `Cute` | – |
| Severin (SE), um 20 | Enkel, Sohn des vorverstorbenen Andreas | `standing/robot_dance-2` (schwarzer Pullover, Hose Grün `#8FD694`, offene Hand), Kopf `Short 4`, Haut `#D9A47E`; `Solemn`, `Concerned\|Serious` (auch redet), `Calm`, `Serious`, `Smile` | `niklas` (Mann, jung) |
| Egbert (EG), um 75 | Bruder von Kurt (zweite Ordnung) | `standing/pointing_finger-2` (schwarzer Pullover, Hose Beige `#D6B48A`, erhobener Zeigefinger), Kopf `No Hair 2`, Brille `Glasses 3`, Haut `#EBC3A0`, kein Bart; `Calm`, `Suspicious` (auch redet), `Tired` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und per `grep -rlw` in keiner Datei unter `youtube/` (04.10.2026): Kurt, Christa, Verena, Mathilda, Andreas, Severin, Egbert. Verworfen: Walter (005), Hannes (005/104), Greta (003), Heinz (englisch lesbar, 026), Lasse (094), Ole (150), Jannik/Lina (vergeben). Nie im Genitiv mit -s („der Bruder von Kurt“, „die Tochter von Verena“).
- **Stimmen nur aus dem Pool** (niklas, helmut, ela_froh, julia): gebraucht niklas (Severin, jung) und helmut (Egbert, älter). ela_froh (fröhlich) passt nicht zur Trauersituation, julia vermieden; Christa, Verena und Mathilda sprechen deshalb nicht. Nicht die Stimmen der Vorfolgen 154/155 (lucy, christian, marc, sabrina).
- **Blickrichtung:** Grundansicht gespiegelt (blickt nach links), Suffix `_r` blickt nach rechts. Fall: Christa, Verena, Mathilda links (`_r`) blicken zu Severin und Egbert, diese blicken nach links zu ihnen. Tafelfolien: alle blicken nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `SE_redet`, `EG_redet` (je beide Blickrichtungen) und Lexi. 66 Figuren-PNGs in `../peeps/op_156/` (nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 152 (`walking-1`, `shirt-4`; Gewächshaus), 153 (`easing-1`, `resting-2`, `resting-1`; Konditorei/Wohnung), 154 (`crossed_arms-2`, `blazer-3`), 155 (`blazer-4`, `walking-3`, `sitting/hands_back-1`). 156: Posen `easing-2`, `shirt-3`, `walking-2`, `robot_dance-2`, `pointing_finger-2` in keiner dieser Folgen; keine lila Jacke (153/155), keine Polka Dots, keine Prothesen-Posen, keine Bärte. Schauplatz Esszimmer mit Kommode und Familienfoto (neu; 128 und 153 hatten ein Wohnzimmer mit Sofa, 040 eine Küche); Stammbaum und Bruch-Diagramm als neue Bildformen. Erbrechtlicher Vorgänger 040 (Berliner Testament) nur als Verweis.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Esszimmer** `fall`→`frage2` | ab 0,0 s Boden, Kommode mit Familienfoto, Christa, Verena, Mathilda, Severin mit Namensschildern, Pille „Kurt ist mit 78 Jahren gestorben.“; „Kein Testament“; Rollen-Pillen über den Köpfen bei Nennung; „Andreas, Vater von Severin: vor 3 Jahren gestorben“; Egbert kommt von rechts (120 px) mit Pille „Egbert, Bruder von Kurt“; Blasen Severin, Egbert; Fragen | tabler:`users-group` (im Rahmen), `flower` (Rot), `file-off`, `chart-pie` | `Fall · Ohne Testament` → `· Die Familie` → `· Wer bekommt etwas?` → `· Die Frage` | Grundbild · kein Testament · Ehefrau · Tochter · Tochter von Verena · Enkel · Andreas · Egbert · Bruder · Severin redet · Egbert redet · Frage 1 · Frage 2 | Schritte (`szene_156schritte_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **C Stammbaum** `baum`→`beg` | Knoten erscheinen beim Namen: Kurt (grau), Christa + Doppellinie, Pille „Zugewinngemeinschaft“, Verena, Andreas (grau), Mathilda, Severin, Egbert, Eltern (grau); Christa und Severin rechts | tabler:`sitemap`, `heart` (Lila), `users`, `users-group`, `user` (Orange) | `Stammbaum` → `› Erblasser: Kurt` → `› Ehefrau: Christa` → `› Kinder …` → `› Enkel …` → `› Bruder: Egbert` | 10 Aufbaustufen | – |
| **D § 1922** `p1922`→`v040` | Wortlautkarte mit Markern, Block Universalsukzession, Haken „Kein Testament: gesetzliche Erbfolge“, Verweis 040; Verena, Christa | tabler:`book`, `box` (Gelb), `file-off`, `file-text` | `Erbfall › § 1922 Abs. 1 BGB` → `› Universalsukzession` → `› kein Testament: gesetzliche Erbfolge` | Karte · 4 Marker · Block · Haken · Verweis | – |
| **E Ordnungen** `ord`→`o3` | Wortlautkarte § 1924 Abs. 1, drei Stufen (Gelb/Blau/Lila) mit §§ 1924/1925/1926, Pillen „Kinder, Enkel, Urenkel“, „Egbert“ | tabler:`stairs`, `users-group`, `users` | `Ordnungen` → `› 1. Ordnung, § 1924 Abs. 1 BGB` → `› 2. Ordnung, § 1925 BGB` → `› 3. Ordnung, § 1926 BGB` | Karte · Marker · Stufe 1 · Abkömmlinge · Stufe 2 · Egbert · Stufe 3 | – |
| **F § 1930** `p1930`→`egb3` | Wortlautkarte, Stammbaum (voll), Verena/Severin grün umrahmt („1. Ordnung“), Egbert blass mit Kreuz („2. Ordnung“); Egbert allein | tabler:`stairs`, `user-x` (Orange) | `Ordnungen › Ausschluss, § 1930 BGB` → `› Kurt hat Abkömmlinge` → `› Egbert erbt nicht (−)` | Karte · Marker · 1. Ordnung · Egbert raus | – |
| **G1 § 1924 Abs. 2** `inn`→`repr2` | Wortlautkarte, Stammbaum (erste Ordnung), „Repräsentationsprinzip“, Verena grün „lebt“, Mathilda blass mit Kreuz; Verena und Mathilda (Kind) rechts | tabler:`users-group`, `user-check`, `user-x` | `Erste Ordnung › Wer erbt?` → `› Repräsentation, § 1924 Abs. 2 BGB` → `› Mathilda erbt nicht (−)` | Baum · 4 Marker · Prinzip · lebt · Mathilda raus | – |
| **G2 § 1924 Abs. 3, 4** `p3`→`gleich` | Wortlautkarte, Zitatzeile Abs. 4, Stammbaum, Pfeil Severin → Platz von Andreas, Stämme als farbige Flächen mit Pillen, „gleich viel“; Verena, Severin | tabler:`replace`, `arrow-big-up`, `scale`, `hierarchy` | `Erste Ordnung › Eintrittsrecht, § 1924 Abs. 3 BGB` → `› Severin statt Andreas (+)` → `› gleiche Teile, § 1924 Abs. 4 BGB` → `› Erbfolge nach Stämmen` | Marker · Pfeil · Abs. 4 · Stämme · Pillen · gleich viel | – |
| **H1 § 1931 Abs. 1 S. 1** `ehe`→`viertel` | Wortlautkarte (vorgelesen), Block „Christa: zunächst 1/4“, Kreis mit 1/4; Christa allein | tabler:`heart`, `chart-pie` | `Ehegatte` → `› § 1931 Abs. 1 S. 1 BGB` → `› neben 1. Ordnung: 1/4` | Karte · 3 Marker · Block · Kreis | – |
| **H2 § 1931 Abs. 3, § 1371 Abs. 1** `abs3`→`halb` | Zitatzeile § 1931 Abs. 3, Wortlautkarte § 1371 Abs. 1, Kreis 1/4 + 1/4, Block „1/4 + 1/4 = 1/2“; Christa, Verena | tabler:`book`, `plus`, `chart-pie-2` | `Ehegatte › § 1931 Abs. 3 BGB` → `› § 1371 Abs. 1 BGB: plus 1/4` → `› Christa: 1/2` | Zeile · Karte · 4 Marker · Viertel · Viertel · Block | – |
| **I Ergebnis** `erg`→`e_nicht` | Bruch-Diagramm (Kreis): 1/2 Lila, Rest grau, 1/4 Blau, 1/4 Grün; Pillen mit Ziffern, Gegenprobe-Block, Kreuz „Mathilda, Egbert: nichts“; Christa, Verena, Severin | tabler:`chart-pie`, `equal` | `Ergebnis` → `› Rest nach Stämmen` → `› Gegenprobe: Summe 1` → `› Mathilda, Egbert: nichts` | 1/2 · Rest · 1/4 · 1/4 · Probe · nichts | – |
| **J Variante** `guet`/`drittel` | Wortlautkarte § 1931 Abs. 4, Kreis in Dritteln, Pillen „je 1/3“; Christa, Severin | tabler:`arrows-split`, `chart-pie` | `Variante › Gütertrennung, § 1931 Abs. 4 BGB` → `› je 1/3` | Karte · 4 Marker · Drittel | – |
| **K Klausurtipp** `tipp`→`t4` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Ehegattenquote zuerst` → `· Rest nach Stämmen` → `· Erbengemeinschaft, § 2032 BGB` | 5 Zeilen nacheinander | – |
| **L Prüfschema** `sch`→`s5` | breite Karte, I.–V. Punkt für Punkt | – | `Prüfschema` → `› I. Erbfall` … `› V. Gegenprobe` | 9 Aufbaustufen | – |
| **M Merksatz** `merke`/`m2` | Lexi erklärt (redet), Marker | – | `Merksatz` | 2 Marker | – |

**Prüfpfad und Reihenfolge:** Das Video erklärt in der Reihenfolge des Auftrags (Ordnungen → innerhalb der Ordnung → Ehegatte → Ergebnis). Die Klausurreihenfolge (Ehegattenquote vor der Verteilung nach Stämmen) nennt Lexi ausdrücklich; das Schema verwendet sie mit I.–V. und denselben Bezeichnungen.
**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; Bewegung nur: Egbert kommt 120 px von rechts herein.
**Blasen:** Stil C, wortgleich mit dem Gesprochenen. Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026). **Brüche als Ziffern** (1/2, 1/4, 1/3), Zahlen in Ziffern („78 Jahren“, „3 Jahren“).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Kurt ist im Alter von 78 Jahren gestorben. Ein Testament oder einen Erbvertrag hat er nicht hinterlassen. Er war mit Christa verheiratet; die beiden lebten im gesetzlichen Güterstand der Zugewinngemeinschaft.
>
> Ihre gemeinsamen Kinder sind Verena und Andreas. Andreas ist drei Jahre vor Kurt gestorben; sein einziges Kind ist Severin. Verena hat eine Tochter, Mathilda.
>
> Die Eltern von Kurt sind schon lange verstorben. Sein Bruder Egbert lebt.
>
> **Wer wird gesetzlicher Erbe von Kurt, und zu welchen Teilen?**
