# Folge 051 · Diebstahl § 242 Schema: Wegnahme & Zueignungsabsicht – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_051.py`](src/skript_051.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis, Themenplan-Format „Schema“. Der Hook des Themenplans trägt den Film: Matthias nimmt im Lesesaal der Unibibliothek das Ladekabel von Antje vom Nachbartisch mit nach Hause, während Antje kurz in der Cafeteria ist. Frage → Sachverhalt (Grundfall, drei Varianten) → Wortlautkarte § 242 I und Aufbau → fremde bewegliche Sache → Wegnahme/Gewahrsam → gelockerter Gewahrsam (Gegenfall Handy auf der Straße) → Bruch und neuer Gewahrsam (Gewahrsamsenklave) → Vorsatz (Variante 1, § 16) → Zueignungsabsicht (Aneignung/Enteignung) → Gebrauchsanmaßung (Variante 2) → Rechtswidrigkeit der Zueignung (Variante 3) → Ergebnis, § 248a → Ausblick § 243 → Klausurtipp (Lexi) → Klausurschema → Merksatz (Lexi).
**Verhältnis zu Folge 047 (Vermögensdelikte Überblick):** Dort steht § 242 nur als Feld der Landkarte (Wortlaut, Wegnahmedefinition, eine Variante). Hier wird das Prüfungsschema vertieft: Gewahrsamsbegriff, gelockerter Gewahrsam, Gewahrsamsenklave, Vorsatz, beide Komponenten der Zueignungsabsicht, Gebrauchsanmaßung, Rechtswidrigkeit der Zueignung, § 248a, § 243. Keine Wiederholung der Abgrenzungen zu Betrug, Raub, Erpressung.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Antje (AN), Anfang 20 | Studentin, Eigentümerin des Ladekabels | `standing/easing-2` (offenes Hemd Grün `#8FD694` über schwarzem Top, Hose Blau `#8DB3F2`), Kopf `Long Curly`, Haut `#F0C8A8`. Mimiken `Serious` (lernt/denkt), `Calm`, `Concerned|Serious` (redet), `Smile`, `Fear`, `Suspicious`, `Awe` | `lucy` (Frau, jung) |
| Matthias (MA), Anfang 20 | Student am Nachbartisch, nimmt das Kabel | `standing/walking-2` (schwarzes T-Shirt der Pose, Hose Lila `#B8A9F5`; geht, Hand in der Tasche), Kopf `Short 2`, Haut `#D9A27A`. Mimiken `Calm`, `Suspicious`, `Cheeky|Smile` (redet), `Smile` (redet ehrlich; froh), `Driven`, `Serious`, `Fear`, `Concerned|Serious`, `Awe` | `christian` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links: Matthias zum Kabel am Nachbartisch, beide in den Tafelszenen zur Tafel), `_r` blickt nach rechts (Matthias auf dem Heimweg zum rechten Bildrand; Antje in Variante 3 zu Matthias).
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimiken nur als `Concerned|Serious`, `Cheeky|Smile`. Mundzustände a/o/e bei `AN_redet`, `MA_redet`, `MA_ehrlich` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen. 60 Figuren-PNGs in `../peeps/op_051/` (Drive-Master).
- **Klischeeprüfung:** Matthias ist ein gewöhnlicher Student (schwarzes T-Shirt, lila Hose), keine Karikatur, keine Herkunfts- oder Hautfarbenzuschreibung, keine Waffe.
- **Namen** mit eindeutig deutscher Aussprache, in keiner Vorfolge vergeben (Liste des Auftrags; zusätzlich gegen alle Skripte und Dokumente in `preproduction/` geprüft): Antje, Matthias. Im Sprechtext nie im Genitiv mit -s („das Kabel von Antje“), weil Genitivformen in 015 und 047 von der Spracherkennung verschluckt wurden.
- **Stimmen** nur aus dem zugeteilten Pool (christian, lucy; marc und elinor nicht gebraucht). Vorfolgen 047 (stephan, sabrina) und 048/049: keine Überschneidung mit 047; Lea nicht verwendet.

**Abweichung von den letzten Folgen:** 047 (Kameraladen), 046 (Elektrohändler), 045 (Klausursaal). Der Hook verlangt eine Bibliothek; die Unibibliothek von 035 (Whiteboard-Szene) und die Stadtbibliothek von 033 werden **nicht** wiederverwendet: neu gezeichnet als Lesesaal mit zwei Arbeitstischen, Leselampen, Steckdose an der Tischfront, Handy am Ladekabel und Rucksack; in den Tafelszenen kleine Requisitenbilder (Traktor auf dem Feld, Straße bei Nacht, Rucksack mit Ring, Denkblase mit zwei gleichen Kabeln). Neue Posen (`easing-2`, `walking-2`) gegenüber 047.
**Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Lesesaal** `fall`→`frage2` | zwei Arbeitstische; Antje lernt, Handy lädt am Kabel in der Steckdose, sie geht in die Cafeteria (Kabel bleibt), Matthias am Nachbartisch (Akku fast leer), Blase „Das nehme ich mir einfach mit.“, er zieht das Kabel heraus, steckt es in den Rucksack, geht heim; Antje kommt zurück, Blase „Wo ist denn mein Ladekabel?“; Frage-Pillen | tabler:`lamp`, `books`, `book`, `device-mobile-charging`, `plug`, `coffee`, `battery-1`, `backpack`, `home`; Steckdose als Karte | `Fall · Der Lesesaal` (ab 0,0 s) → `Fall · Die Frage` | ≈ 20 | Stecker aus der Steckdose (`szene_051stecker_1`), Reißverschluss (`szene_051reissv_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Wortlaut** `p242`→`subj` | Wortlautkarte § 242 I mit drei Markern, Blöcke objektiver/subjektiver Tatbestand | tabler:`plug` | `§ 242 StGB › Wortlaut und Aufbau` | ≈ 6 | – |
| **D Sache** `sache`→`fremd` | drei Haken (Sache, beweglich, fremd), Block | tabler:`plug` | `I. Tatbestand › 1. objektiv › a) fremde bewegliche Sache` | ≈ 6 | – |
| **E Wegnahme** `wegn`→`verkehr` | Definition, Gewahrsamsblock | tabler:`hand-grab`, `plug` | `… › b) Wegnahme` → `… › b) Wegnahme › Gewahrsam` | ≈ 6 | – |
| **F Gelockerter Gewahrsam** `weg`→`fund` | leerer Platz (Bücher, Kabel, Steckdose, „Platz besetzt“), Antje mit Kaffee; Traktor auf dem Feld; Gegenfall Handy auf der Straße bei Nacht | tabler:`books`, `plug`, `coffee`, `tractor`, `moon`, `device-mobile` | `… › b) Wegnahme › gelockerter Gewahrsam` | ≈ 9 | – |
| **G Bruch, Enklave** `bruch`→`wegok` | Matthias, Kabel wandert in den Rucksack, Ring = Gewahrsamsenklave | tabler:`backpack`, `plug`, `books` | `… › b) Wegnahme › Bruch und neuer Gewahrsam` | ≈ 8 | – |
| **H Vorsatz** `vors`→`v1ok` | Denkblase mit zwei gleichen Kabeln (Variante 1), Kreuz § 16 | tabler:`plug` | `I. Tatbestand › 2. subjektiv › a) Vorsatz` → `… › Variante 1` | ≈ 7 | – |
| **I Zueignungsabsicht** `zueig`→`zueigok` | zwei Spalten Aneignung/Enteignung, Ergebnisblock | tabler:`home`, `plug` | `… › b) Zueignungsabsicht` | ≈ 9 | – |
| **J Gebrauchsanmaßung** `v2`→`v2ok` | Blase Matthias „Morgen früh lege ich es zurück.“, Mond → Kabel zurück | tabler:`moon`, `plug` | `… › b) Zueignungsabsicht › Variante 2` | ≈ 7 | – |
| **K Rechtswidrigkeit** `rwz`→`v3ok` | Anspruch gerade auf diese Sache; Kaufvertrag, bezahlt | tabler:`receipt`, `cash` | `… › Rechtswidrigkeit der Zueignung` → `… › Variante 3` | ≈ 9 | – |
| **L Ergebnis, § 248a** `erg`→`oeff` | Haken, Ergebnisblock, Strafantrag | tabler:`coin`, `signature` | `Grundfall › II. Rechtswidrigkeit, III. Schuld › Ergebnis` → `Grundfall › Strafantrag, § 248a StGB` | ≈ 7 | – |
| **M Ausblick § 243** `p243`→`p243c` | Regelbeispiele, Block Strafzumessungsregeln, Kreuz § 243 II | tabler:`building`, `briefcase` | `Ausblick › besonders schwerer Fall, § 243 StGB` | ≈ 5 | – |
| **N Klausurtipp** `tipp`→`tipp4` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand), tabler:`plug` | `Klausurtipp · Zueignung gehört in den subjektiven Tatbestand` | ≈ 5 | – |
| **O Klausurschema** `sch`→`s_v` | breite Karte, progressiv | – | `Klausurschema` | ≈ 10 | – |
| **P Merksatz** `merke`→`m_3` | Lexi erklärt, drei Marker | – | `Merksatz` | ≈ 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Handlung als Zustandswechsel (Antje am Platz → in der Cafeteria → zurück; Kabel in der Steckdose → im Rucksack; Matthias am Nachbartisch → zwischen den Tischen → blickt zum Ausgang).
**Geräusche:** nur die zwei sichtbaren Handgriffe im Fall (Stecker aus der Steckdose, Reißverschluss beim Einstecken in den Rucksack), Freesound CC0, siehe `geraeusche_herkunft.json`.
**Wortlautkarte** (FOLGE-ABLAUF Abschnitt 2): § 242 I vollständig, wörtlich nach gesetze-im-internet.de mit Normangabe, wörtlich vorgelesen; Marker synchron.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Donnerstagnachmittag im Lesesaal der Unibibliothek: Antje lädt ihr Handy an einem weißen Ladekabel (Wert 15 Euro), das in der Steckdose an ihrem Tisch steckt. Sie geht kurz in die Cafeteria und nimmt das Handy mit; Kabel, Jacke und Bücher bleiben am Platz. Matthias vom Nachbartisch, dessen Akku fast leer ist, zieht das Kabel aus der Steckdose, steckt es in seinen Rucksack und nimmt es mit nach Hause, um es zu behalten.
>
> Variante 1: Matthias besitzt ein gleiches weißes Kabel und glaubt, er habe es am Morgen dort vergessen. Er hält das Kabel von Antje für seines. Variante 2: Matthias will das Kabel nur über Nacht benutzen und am nächsten Morgen an Antjes Platz zurücklegen. Variante 3: Antje hat Matthias genau dieses Kabel gestern verkauft. Er hat bezahlt, und sie hat zugesagt, es ihm heute zu übergeben.
>
> **Hat sich Matthias nach § 242 StGB strafbar gemacht?**
