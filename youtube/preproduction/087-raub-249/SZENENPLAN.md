# Folge 087 · Raub § 249 StGB: Prüfungsschema mit Gewalt, Wegnahme & Finalität – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_087.py`](src/skript_087.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis, Format „Schema“. Fall nach dem Plan-Hook (Stoß, Handtasche weg) → Frage → Sachverhalt (Grundfall, zwei Abwandlungen) → Wortlautkarte § 249 Abs. 1 und Aufbau → fremde bewegliche Sache, Wegnahme (Verweis auf Folge 051) → qualifiziertes Nötigungsmittel (Unterschied zu § 240, Gewalt gegen eine Person) → finaler Zusammenhang → Abwandlung 1 (Gewalt aus Wut, Entschluss danach) → Abgrenzung §§ 252, 255 (je ein Satz, Streit nur genannt) → Vorsatz, Zueignungsabsicht, Rechtswidrigkeit der Zueignung → Ergebnis, §§ 250, 251 (ein Satz) → Abwandlung 2 (Entreißen) → Klausurtipp (Lexi) → Klausurschema → Merksatz (Lexi). Vorlagen: 051 (Diebstahl als Schema; Wegnahme dort vertieft, hier nur verwiesen), 084 (Nötigung, Stil C), 075 (zurückhaltende Bildsprache bei Gewalt).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Margit (MG), um 55 | kommt vom Wochenmarkt, Eigentümerin der Handtasche | `standing/polka_dots` (weiß gepunktete Bluse der Pose, Hose Blau `#8DB3F2`, schwarze Schuhe), Kopf `Gray Medium` (Haar Grau `#B9B4AE`), Haut `#F0C8A8`. Mimiken `Calm`, `Smile`, `Fear` (Schreck), `Concerned|Serious` (Sorge; redet), `Serious`, `Awe` | `laura_ruhig` (Frau, mittel) |
| Hagen (HG), um 30 | Täter | `standing/robot_dance-2` (schwarzes Langarmshirt der Pose, Hose Grün `#8FD694`, weiße Turnschuhe), Kopf `Short 5`, Haut `#EDC1A0`. Mimiken `Calm`, `Suspicious` (redet), `Driven`, `Very Angry` (nur Abwandlung 1 „aus Wut“), `Serious`, `Fear`, `Solemn` | `marc` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts (Fall: Margit zu Hagen, Hagen beim Davonrennen).
- In den Tafelfolien steht Hagen links (X 1440), Margit rechts (X 1740): Hagens ausgestreckte Hand zeigt zur Tafel, nie auf Margit.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `MG_redet`, `HG_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Waffe. 50 Figuren-PNGs in `../peeps/op_087/` (Drive-Master).
- **Klischeeprüfung:** Hagen gewöhnlich gekleidet (schwarzes Langarmshirt, grüne Hose), heller Hautton ähnlich Margit, keine Herkunfts- oder Hautfarbenzuschreibung, keine „fiese“ Mimik; Margit respektvoll, erschrocken, aber nicht leidend.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und per `grep -rlw` in keinem Skript, Szenenplan, Abnahmebogen oder Themenplan unter `youtube/` (02.10.2026): Margit, Hagen („Ralf“ verworfen, Folge 007). Im Sprechtext nie im Genitiv mit -s.
- **Stimmen** nur aus dem zugeteilten Pool (marc, laura_ruhig; william und sabrina nicht gebraucht). Direkte Vorfolge 086 (lucy, stephan) und 084 (helmut, julia): keine Überschneidung; `laura_ruhig` sprach zuletzt in 085 (Frau Wiesner) – Pool-Vorgabe des Koordinators, in 087 eine andere Rolle (Margit, um 55). Lea nicht verwendet.

**Abweichung von den letzten Folgen (084 Mietwohnung/Bauamt, 085 Außenbereich/Wald, 086 Fitnessstudio):** neuer Schauplatz Weg vom Wochenmarkt zur Bushaltestelle (Marktstand mit Korb, Apfel und Möhre, Laubbaum, Haltestellenschild). Posen `polka_dots` und `robot_dance-2` in 084–086 nicht verwendet (dort `resting-2`, `blazer-3`, `robot_dance-3`, `walking-1`, `crossed_arms-1`); Polka Dots zuletzt in 081, nicht in den letzten drei Folgen.
**Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 vorher** `fall`→`stoss` | Weg vom Markt zur Haltestelle; Margit mit Handtasche ab 0,0 s, Pillen „Handtasche über der Schulter“, „Geldbörse · 80 €“; Hagen erscheint („hat sie beim Bezahlen gesehen“), Blase „Die Handtasche hole ich mir.“, „läuft auf Margit zu“ | fluent:`basket`, `red-apple`, `carrot`, `deciduous-tree`, `bus-stop`, `handbag`, `purse` | `Fall · Auf dem Weg zum Bus` (ab 0,0 s) → `Fall · Hagen hat Margit gesehen` | ≈ 9 | – |
| **A2 nachher** `stößt`→`frage2` | Schiebeblende als Zeitsprung: **kein Stoß, kein Sturz im Bild** – nur Warnsymbol mit Pillen „stößt Margit zu Boden“, „um an die Tasche zu kommen“ und die Tasche am Boden; Hagen nimmt die Tasche, rennt mit ihr nach rechts (Bewegung, dezente Bewegungslinien, Laufschritte), „will sie samt Geld behalten“; Margit steht wieder (erschrocken, „nicht verletzt“), Blase „Meine Tasche ist weg!“; Frage-Pillen | fluent:`warning`, `handbag` | `Fall · Der Stoß` → `Fall · Hagen nimmt die Handtasche` → `Fall · Margit steht wieder auf` → `Fall · Die Frage` | ≈ 13 | Laufschritte (`szene_087laufen_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10,6 s | – | `Sachverhalt` | 1 | – |
| **C Wortlaut** `p249`→`subj` | Wortlautkarte § 249 Abs. 1 (Marker gelb Nötigungsmittel, blau Sache/Wegnahme, lila Zueignung), Blöcke Aufbau, objektiv, subjektiv | fluent:`balance-scale`, `handbag`, `warning` | `A. Raub, § 249 StGB › Wortlaut` → `… › Aufbau` | ≈ 10 | – |
| **D Sache, Wegnahme** `sache`→`wegok` | Haken, Definition, Verweis auf Folge 051, Wegnahme (+) | fluent:`handbag`; tabler:`hand-grab`, `arrow-right` | `A. § 249 StGB › I. Tatbestand › 1. objektiv › a) fremde bewegliche Sache` → `… › b) Wegnahme` → `… (+)` | ≈ 11 | – |
| **E Nötigungsmittel** `nm`→`g_ja` | Vergleich § 240, zwei Karten (Gewalt / Drohung), Kreuz „Anzeige“, Gewaltdefinition, Gewalt (+) | fluent:`balance-scale`, `warning`, `leftwards-pushing-hand` (abstrakte Hand, keine Person); tabler:`file-alert` | `… › c) Nötigungsmittel` → `… › c) qualifiziertes Nötigungsmittel` → `… › c) Gewalt gegen eine Person` → `… (+)` | ≈ 12 | – |
| **F Finalität** `final`→`f_ja` | „Gewalt → um zu → Wegnahme“, Vorstellung des Täters, Finalität (+) | fluent:`link`, `handbag`; tabler:`bulb` | `… › d) finaler Zusammenhang` → `… › d) Finalität: Vorstellung des Täters` → `… (+)` | ≈ 10 | – |
| **G Abwandlung 1** `ab1`→`ab1e` | blaue Tafel; Wut (Gewitterwolke), „erst danach“ (Uhr), Finalität (−) (zerrissene Kette), Diebstahl | fluent:`cloud-with-lightning`, `broken-chain`, `handbag`; tabler:`clock` | `Abwandlung 1 › Gewalt aus Wut` → `… › Finalität (−)` → `… › Diebstahl, § 242 StGB` | ≈ 9 | – |
| **H §§ 252, 255** `p252`→`streit` | § 252, nur Flucht (−), § 255, zwei Karten BGH/Lehre; Hagen allein | fluent:`handbag`, `open-hands`, `balance-scale`; tabler:`arrow-right` | `Abgrenzung › räuberischer Diebstahl, § 252 StGB` → `… › räuberische Erpressung, § 255 StGB` | ≈ 11 | – |
| **I subjektiv** `vors`→`rwz` | Vorsatz, Aneignung/Enteignung, will behalten, kein Anspruch | tabler:`brain`; fluent:`handbag`, `purse` | `… › 2. subjektiv › a) Vorsatz` → `… › b) Zueignungsabsicht` → `… › b) Rechtswidrigkeit der Zueignung` | ≈ 11 | – |
| **J Ergebnis** `rs`→`qual` | Ergebniskarte, Qualifikationen §§ 250, 251 | tabler:`gavel` | `A. § 249 StGB › II. Rechtswidrigkeit, III. Schuld` → `Ergebnis · Hagen: Raub, § 249 StGB` → `Ausblick › Qualifikationen, §§ 250, 251 StGB` | ≈ 7 | – |
| **K Abwandlung 2** `ab2`→`ab2e` | blaue Tafel; im Vorbeilaufen, Kraft auf die Tasche, Überraschung → Diebstahl; Festhalten → Gewalt, Raub | fluent:`handbag`, `high-voltage`; tabler:`arrow-right`, `hand-grab` | `Abwandlung 2 › Entreißen im Vorbeilaufen` → `… › Überraschung: Diebstahl` → `… › Festhalten: Gewalt, Raub` | ≈ 10 | – |
| **L Klausurtipp** `tipp`→`tipp4` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Finalität sauber prüfen` → `… · bloßes Ausnutzen genügt nicht` | ≈ 9 | – |
| **M Klausurschema** `sch`→`s_iv` | breite Karte, progressiv | – | `Klausurschema › …` | ≈ 13 | – |
| **N Merksatz** `merke`→`m_3` | Lexi erklärt, Marker | – | `Merksatz` | ≈ 7 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops. Die Schiebeblende zwischen A1 und A2 ist der Zeitsprung über den Stoß: A2 beginnt beim Wort „stößt“, Hagens Satz endet vorher (kein Mund im Wisch).
**Geräusche:** ein Handlungsgeräusch (Laufschritte, als Hagen sichtbar mit der Tasche davonrennt; Freesound CC0), Herkunft in `geraeusche_herkunft.json`. Kein Stoß-, Sturz- oder Aufprallgeräusch (wäre ein Gewaltakzent), keine Geräusche bei Tafeln.
**Gewalt zurückhaltend:** Der Stoß wird nur gesprochen und als Warnsymbol/Pille gezeigt; Margit erscheint erst wieder stehend („erschrocken, nicht verletzt“); keine Verletzung, kein Blut, keine Opferperspektive mit Leid; in der Gewaltdefinition nur eine abstrakte Emoji-Hand.
**Wortlautkarte** (FOLGE-ABLAUF Abschnitt 2): § 249 Abs. 1 vollständig, wörtlich nach gesetze-im-internet.de mit Normangabe, wörtlich vorgelesen; Marker synchron.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Dienstagnachmittag auf dem Weg vom Wochenmarkt zur Bushaltestelle: Margit trägt ihre Handtasche über der Schulter, darin ihre Geldbörse mit 80 €. Hagen hat sie am Marktstand beim Bezahlen gesehen. Um an die Tasche zu kommen, stößt er Margit zu Boden, nimmt die Handtasche und rennt davon. Er will sie samt Geld behalten. Margit hat sich erschrocken, verletzt ist sie nicht.
>
> Abwandlung 1: Hagen stößt Margit nur aus Wut, weil sie ihn angerempelt hat. Erst als die Tasche am Boden liegt, beschließt er, sie mitzunehmen.
>
> Abwandlung 2: Hagen kommt von hinten und reißt Margit die locker hängende Tasche im Vorbeilaufen von der Schulter, ehe sie reagieren kann.
>
> **Hat sich Hagen nach § 249 StGB strafbar gemacht?**
