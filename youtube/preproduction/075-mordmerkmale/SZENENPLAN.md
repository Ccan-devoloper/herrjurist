# Folge 075 · Mordmerkmale § 211 StGB: Mord oder Totschlag? Alle Gruppen – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_075.py`](src/skript_075.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis, Themenplan-Format „Schema“. Zwei Übungsfälle nach dem Plan-Hook (gleiche Tathandlung, einmal spontane Wut, einmal Erbschaft) → Frage → Sachverhalt → §§ 212/211 (Wortlaut § 212, Streit, § 28, lebenslang) → Wortlautkarte § 211 Abs. 2 mit drei Gruppen progressiv → 1. Gruppe (Mordlust, Geschlechtstrieb, Habgier am Erbschaftsfall; niedrige Beweggründe am Wut-Fall) → 2. Gruppe (Heimtücke mit Arg-/Wehrlosigkeit, Ausnutzungsbewusstsein, feindlicher Willensrichtung, Fall Horst; grausam; gemeingefährliche Mittel) → 3. Gruppe (Ermöglichung, Verdeckung) → Ergebnis beider Fälle → Klausurtipp (Lexi) → Klausurschema → Merksatz (Lexi). Vorlagen: 035 (Tötungsdelikte, Mordmerkmale hier vertieft statt wiederholt), 068 (zurückhaltende Bildsprache, Blasen Stil C), 029.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Norbert (NO), um 50 | Fall 1, tötet in spontaner Wut | `standing/crossed_arms-1` (verschränkte Arme, keine Gewaltpose), Kopf `Short 2`, Pullover Blau `#8DB3F2`, schwarze Hose, Haut `#E8B894`. Mimiken `Calm`, `Suspicious` (Ärger), `Very Angry` (redet, Mund zu), `Serious`, `Solemn`, `Tired` | `marc` (Mann, mittel) |
| Horst (HO), um 55 | Fall 1, Nachbar und Opfer; spricht nicht | `standing/resting-1`, Kopf `Short 4`, Pullover Rot `#F07A6A`, schwarze Hose, Haut `#D9A27A`. Mimiken `Calm`, `Concerned|Serious` (rechnet mit Angriff), `Serious` | – |
| Dietmar (DI), um 75 | Fall 2, Onkel und Opfer | `standing/shirt-3`, Kopf `Short 4_2` (graues Haar), Hemd Lila `#B8A9F5`, schwarze Hose, Haut `#EDC1A0`. Mimiken `Smile` (redet, froh), `Calm`, `Serious` | `william` (Mann, älter) |
| Friederike (FR), um 30 | Fall 2, Nichte und Alleinerbin, tötet aus Habgier | `standing/easing-2`, Kopf `Long` (dunkelbraun), Jacke Grün `#8FD694`, schwarzes Oberteil, schwarze Hose, Haut `#F0C8A8`. Mimiken `Smile`, `Calm`, `Suspicious` (denkt), `Serious` (redet), `Solemn` | `sabrina` (Frau, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts (Fallszenen: Norbert zu Horst, Friederike zu Dietmar).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e bei `NO_wut`, `DI_redet`, `FR_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikaturen; Täter und Opfer neutral gekleidet, keine Klischees. 64 Figuren-PNGs in `../peeps/op_075/` (Drive-Master).
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keinem Skript, Szenenplan oder Abnahmebogen unter `youtube/` (Volltextsuche 02.10.2026): Norbert, Horst, Dietmar, Friederike.
- **Stimmen** nur aus dem zugeteilten Pool (marc, william, sabrina; laura_ruhig nicht gebraucht). Vorfolge 074 (ela_froh, helmut, julia) und 073 (hilde, stephan): keine Überschneidung; marc und william zuletzt in 072, sabrina in 069 (Pool-Vorgabe des Koordinators).

**Abweichung von den letzten Folgen:** 074 (Ermessensfehler), 073 (Bereicherungsrecht), 068 (Waldrand mit Hochsitz in der Dämmerung). Hier neu: Hofeinfahrt zwischen zwei Häusern (Fall 1) und Wohnzimmer mit Sofa (Fall 2), danach eine **Gegenüberstellung** beider Täter (Frage), Wortlautkarte § 211 Abs. 2 mit **dreifarbiger** Gruppenmarkierung (gelb/blau/lila), die in den Gruppenfolien als Pillenfarbe wiederkehrt. Neue Posen gegenüber 068–074 (`crossed_arms-1`, `resting-1`, `shirt-3`, `easing-2`).
**Tageslicht:** durchgehend Cremegrund (Fall 1 spielt abends; nur Mondsymbol, kein Nachtverlauf nötig).

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Fall 1** `fall`→`wut` | „Zwei Fälle, zwei Tote“ (zwei kleine Grablichter), Häuser links/rechts, graue Hofeinfahrt; Norbert und Horst; Streit seit Monaten; Abend (Mond); Horst „rechnet mit einem Angriff“ (besorgt); Norbert: „Jetzt reicht es mir endgültig!“; Gewitterwolke über Norbert; **nach** „mit Tötungsvorsatz“ steht Horst nicht mehr da, an seiner Stelle ein kleines Grablicht; die Tat selbst ist nie im Bild | fluent:`house`, `automobile`, `candle`, `cloud-with-lightning`; tabler:`moon-stars` | `Fall 1 · Streit an der Hofeinfahrt` (ab 0,0 s) → `Fall 1 · Wieder ein Streit` → `Fall 1 · Spontane Wut` | ≈ 12 | – |
| **A2 Fall 2** `dietmar`→`tat2` | Wohnzimmer: Friederike links, Dietmar rechts; Testament (Schriftrolle), „einzige Erbin“; Dietmar: „Mein Haus und mein Geld bekommst du einmal, Friederike.“ (Haus, Münze); Dietmar geht; Friederike allein: „Ich will das Erbe nicht erst in 20 Jahren.“; „um früher an sein Vermögen zu kommen“, Grablicht an Dietmars Platz | fluent:`couch-and-lamp`, `framed-picture`, `potted-plant`, `scroll`, `house-with-garden`, `coin`, `candle` | `Fall 2 · Die Erbschaft` → `Fall 2 · Später, allein` → `Fall 2 · Um früher zu erben` | ≈ 10 | – |
| **A3 Frage** `frage`→`frage2` | Norbert (Gewitterwolke) und Friederike (Testament) gegenüber; „2 × dieselbe Tathandlung“, „Beides Mord?“, „Oder einmal nur Totschlag?“ | fluent:`cloud-with-lightning`, `scroll` | `Fall · Die Frage` | 3 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,7 s | – | `Sachverhalt` | 1 | – |
| **C §§ 212, 211** `p212`→`lebensl` | Wortlautkarte § 212 Abs. 1, Haken „vorsätzlich getötet“, Mord = zusätzlich Mordmerkmal, Streit Lehre/BGH (zwei Kästen), § 28, lebenslang; Norbert und Friederike | tabler:`users`, `scale`, `gavel` | `A. Totschlag, § 212 StGB` → … → `A. Mord › Rechtsfolge, § 211 Abs. 1 StGB` | ≈ 13 | – |
| **D § 211 Abs. 2** `wl`→`g3` | Wortlautkarte § 211 Abs. 2, Gruppen farbig zum gesprochenen Gruppennamen, drei Gruppenbalken | fluent:`balance-scale`; tabler:`brain`, `route`, `target` | `B. Mordmerkmale, § 211 Abs. 2 StGB` → `› 1./2./3. Gruppe` | ≈ 6 | – |
| **E 1. Gruppe** `mlust`→`hab_ja` | Mordlust, Geschlechtstrieb, Habgier; Friederike; Habgier (+) | fluent:`money-bag`, `scroll`, `house-with-garden` | `B. 1. Gruppe › …` → `Fall 2 › Habgier (+)` | ≈ 11 | – |
| **F niedrige Beweggründe** `niedrig`→`nb_nein` | Definition, Gesamtwürdigung, Wut/Zorn, Norbert; niedriger Beweggrund (−) | tabler:`scale`; fluent:`cloud-with-lightning` | `B. 1. Gruppe › sonstige niedrige Beweggründe` → `Fall 1 › niedrige Beweggründe (−)` | ≈ 9 | – |
| **G Heimtücke** `heim`→`wehrlos` | Definition, arglos, wehrlos; Horst | tabler:`user-question`, `hand-stop` | `B. 2. Gruppe › heimtückisch` → `… arglos` → `… wehrlos` | ≈ 8 | – |
| **H Heimtücke Fall 1** `ausnutz`→`horst` | Ausnutzungsbewusstsein, feindliche Willensrichtung (ein Satz), Horst rechnete mit Angriff: Heimtücke (−); Norbert und Horst | tabler:`eye`, `alert-triangle` | `B. 2. Gruppe › heimtückisch: bewusst ausgenutzt` → `Fall 1 › Horst nicht arglos: Heimtücke (−)` | ≈ 7 | – |
| **I grausam, gemeingefährlich** `grausam`→`gemein` | zwei Definitionen; keine Figuren, nur abstrakte Symbole | tabler:`alert-triangle`, `users-group` | `B. 2. Gruppe › grausam` → `… mit gemeingefährlichen Mitteln` | ≈ 8 | – |
| **J 3. Gruppe** `g3a`→`keins` | Ermöglichung, Verdeckung, „in beiden Fällen keine Rolle“; Norbert und Friederike | tabler:`target`, `eraser` | `B. 3. Gruppe › …` → `Fall 1 und 2 › 3. Gruppe (−)` | ≈ 7 | – |
| **K Ergebnis** `erg`→`erg2` | zwei Ergebniskarten, Gerichtssymbol | tabler:`gavel`; fluent:`cloud-with-lightning`, `scroll` | `Ergebnis · …` | ≈ 7 | – |
| **L Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | ≈ 7 | – |
| **M Klausurschema** `sch`→`k4` | breite Karte, progressiv | – | `Klausurschema › …` | 8 | – |
| **N Merksatz** `merke`→`m3` | Lexi erklärt, Marker | – | `Merksatz` | ≈ 6 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** keine. Die einzigen Handlungen (Streit, Tat) sind bewusst nicht gezeigt; ein Tat- oder Sturzgeräusch wäre ein Gewaltakzent, und Dietmars Abgang ist kein sichtbarer Vorgang mit Tür. „Lieber kein Geräusch als ein unpassendes.“
**Gewalt zurückhaltend:** kein Messer, kein Stich, kein Blut, keine Leiche, keine Gewaltpose; nach der Tat fehlt das Opfer, ein kleines Grablicht (fluent `candle`, 70 px) steht an seinem Platz; Wut als Gewitterwolke, Erbschaft als Schriftrolle/Haus/Münze, Ergebnis als Richterhammer (Gerichtssymbol).
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 212 Abs. 1 (Anfang wörtlich gesprochen) und § 211 Abs. 2 (Merkmale nach Gruppen hervorgehoben), wörtlich nach gesetze-im-internet.de mit Normangabe.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Fall 1: Norbert und sein Nachbar Horst streiten seit Monaten um die gemeinsame Hofeinfahrt. An einem Abend geraten sie wieder aneinander; Horst rechnet damit, dass Norbert gleich auf ihn losgeht. In spontaner Wut tötet Norbert Horst mit Tötungsvorsatz.
>
> Fall 2: Friederike ist die einzige Erbin ihres Onkels Dietmar. Um früher an sein Vermögen zu kommen, tötet sie ihn auf die gleiche Weise wie Norbert.
>
> Weitere Umstände der beiden Taten sind nicht bekannt.
>
> **Wie haben sich Norbert und Friederike strafbar gemacht?**
