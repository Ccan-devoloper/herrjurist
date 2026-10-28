# Folge 204 · Sachrüge StPO: Wenn die Feststellungen das Urteil nicht tragen – Szenenplan

**Stand:** 06.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_204.py`](src/skript_204.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · StPO-Praxis, Format Schema (Revisionsbegründung). Beispielfall nach dem Plan-Hook („Das Urteil verurteilt wegen Betrugs, sagt aber kein Wort dazu, worin der Vermögensschaden liegen soll“): Die Strafkammer verurteilt Herrn Wichmann wegen Betrugs zu 2 Jahren und 6 Monaten. Laut den Feststellungen verkaufte er Frau Danner einen Oldtimer für 85.000 € als „unfallfrei“, obwohl er den schweren Unfallschaden kannte; sie zahlte. Den Wert des Wagens mit Unfallschaden stellt das Urteil nicht fest; strafschärfend nennt es einen „hohen Schaden“. Ablauf: Fall (Kanzlei → Rückblick Oldtimer-Halle → Kanzlei) → Sachverhalt → § 337 (Wortlaut) → allgemeine Sachrüge (§ 344 Abs. 2 S. 1 Wortlaut, „Ich rüge die Verletzung materiellen Rechts.“) → Grundlage nur die Urteilsurkunde (Rekonstruktionsverbot, urteilsfremd, Verweis Verfahrensrüge) → vier Stufen a) Subsumtion, b) Darstellungsmangel (§ 267 Abs. 1 S. 1 Wortlaut), c) Beweiswürdigung, d) Strafzumessung → Fall: Vermögensschaden (Waage 85.000 € gegen „Wert: ?“) → Ergebnis (Beruhen, §§ 353, 354 Abs. 2) → Klausurtipp (Lexi) → Prüfschema I.–V. → Merksatz (Lexi).
**Länge:** Hauptfilm 5:55,3 bei 5.064 gesprochenen Zeichen; Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Wichmann (WI), um 50 | Angeklagter, Mandant | `standing/shirt-3` (Hemd Graublau `#A9C4D9`, schwarze Hose, weiße Schuhe), Kopf `Short 4`, kein Bart, keine Brille, Haut `#E5B48C`; Mimiken `Calm`, `Serious`, `Concerned\|Serious` (Sorge, redet2), `Suspicious`, `Smile` (redet beim Verkauf) | `stephan` (Mann, mittel) |
| Rechtsanwältin Hellmers (HE), um 35 | Verteidigerin | `standing/crossed_arms-2` (schwarzer Pullover, verschränkte Arme, Hose Lila `#B8A9F5`), Kopf `Medium Bangs` (dunkelbraun `#4A3426`), Haut `#F2CDB0`; Mimiken `Calm`, `Serious` (redet), `Suspicious`, `Smile`, `Solemn` | `lucy` (Frau, jung) |
| Frau Danner (DA), um 65 | Käuferin des Oldtimers (nur im Rückblick) | `standing/easing-2` (offene Jacke Grün `#8FD694` über schwarzem Shirt, Hose Anthrazit `#5A5A6A`), Kopf `Gray Bun`, Brille `Glasses 2`, Haut `#EFC9A9`; Mimiken `Calm`, `Smile` (redet, froh), `Concerned\|Serious` | `hilde` (Frau, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen, nicht in `namen_reserviert.txt` der Parallelfolgen (dort „204: Wichmann, Hellmers, Danner“ eingetragen) und als Figurenname in keiner bisherigen Folge (Volltextsuche über `youtube/` in `*.py/*.md/*.json/*.csv` am 06.10.2026: keine Treffer). „Albers“ verworfen (in 007/041/057 vergeben).
- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Kanzlei: Hellmers (`_r`) und Wichmann (links blickend) einander zugewandt; Halle: Wichmann (`_r`) und Danner (links blickend) einander zugewandt über den Wagen; Tafelfolien: alle blicken zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `WI_redet`, `WI_redet2`, `HE_redet`, `DA_redet` (je links/rechts) und Lexi. Ansicht `WI_schreck` (`Fear`) nach dem Kontaktbild verworfen (wirkte wie eine Brille) und gelöscht.
- **Stimmen nur aus dem Pool** (stephan, hilde, christian, lucy): stephan, lucy, hilde; christian nicht gebraucht (stephan und christian nie in derselben Szene).
- Keine Prothesen-Posen, keine Bärte, keine Polka Dots, keine Karikatur; der Angeklagte in Alltagskleidung ohne Herkunfts- oder Hautfarben-Klischee; keine realen Personen. Hellmers zuerst in `resting-1` erprobt: wirkte im Kontaktbild wie eine Schwangerschaftssilhouette → `crossed_arms-2`.
- Figuren-PNGs: `../peeps/op_204/` (66 Dateien, nicht im Repository, im Drive-Master). Kontaktbild `out/besetzung_204.png`.

**Abweichung von den letzten Folgen:** 201 (`pointing_finger-2`, `blazer-4`), 202 (`robot_dance-3`, `blazer-3`, `shirt-4`), 203 (`crossed_arms-1`, `pointing_finger-2`) – Posen `shirt-3`, `crossed_arms-2`, `easing-2` in keiner der drei Vorfolgen; Farben Graublau/Lila/Grün-Anthrazit, keine Muster. Schauplätze: Kanzlei mit Aktenregal und vergrößerter Urteilsurkunde (die Kanzlei in 066/168 sah anders aus: Schreibtisch, Fristenkalender), Oldtimer-Halle mit Rolltor (neu). Kein Sitzungssaal, weil die Geschichte beim schriftlichen Urteil beginnt.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Kanzlei** `fall`→`liest` | Aktenregal; Hellmers und Wichmann ab 0,0 s mit Namensschildern | Grundformen `regal()`, `urkunde()` (Fenster nach der Sichtprüfung entfernt) | `Fall · In der Kanzlei` (ab 0,0 s) → `· Das Urteil des Landgerichts` → `· Die Urteilsgründe` | Grundbild · Pille Betrug · Pille 2 Jahre 6 Monate, Wichmann besorgt · Urkunde erscheint, Hellmers liest | – |
| **A2 Rückblick: Oldtimer-Halle** `rueck`→`zahlt` | Halle mit Rolltor, Wagen in der Mitte; Wichmann links, Danner rechts | tabler:`car` (Rot), `car-crash`, `cash-banknote` (Grün) | `Fall · Rückblick: der Verkauf` → `· „unfallfrei“` → `· Der Unfallschaden` → `· Die Zahlung` | Grundbild · Preis 85.000 € · Blase Wichmann · Blase Danner · Unfall-Icon und Pille · „wusste das“ · Geld, Danner froh | Geldscheine (`szene_204geld_1`) |
| **A3 Kanzlei** `h1`→`frage2` | wie A1 (Rückkehr nach dem Rückblick); Urkunde mit Prüfliste | wie A1 | `Fall · Was steht im Urteil?` → `· Und der Schaden?` → `· „das Geld wert“` → `· Die Fragen` | Haken Täuschung/Irrtum/Zahlung zum Wort · „Schaden: ?“ · „kein Wort“ · Blase Wichmann · zwei Fragepillen | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,7 s | – | `Sachverhalt` | 1 | – |
| **C § 337** `p337`→`beruh` | Wortlautkarte Abs. 1 und 2, beide Figuren | tabler:`scale`, `file-x`, `link-off` | `Revision · nur Rechtsfehler, § 337 StPO` → `› Gesetzesverletzung, § 337 Abs. 2` → `› zwei Prüfpunkte` → `› Beruhen, § 337 Abs. 1` | Karte + 4 Marker · Zeile · zwei Blöcke | – |
| **D allgemeine Sachrüge** `sach`→`umf` | Wortlautkarte § 344 Abs. 2 S. 1, Satz als Block, Hellmers | tabler:`file-text`, `writing-sign`, `search` | `Sachrüge · Fehler im materiellen Recht` → `› § 344 Abs. 2 S. 1 StPO` → `› allgemeine Sachrüge: 1 Satz` → `› umfassende Prüfung` | Zeile · Karte + 2 Marker · Satz · ✓ + BGH | – |
| **E Grundlage** `grund`→`verf` | Tafel, Wichmann | tabler:`file-text`, `folder-off`, `message-off`, `gavel` | `Sachrüge › Grundlage: nur die Urteilsurkunde` → `› Feststellungen, Beweiswürdigung, Strafzumessung` → `› keine Akte, keine Rekonstruktion` → `› urteilsfremd: unbeachtlich` → `Verfahrensfehler: Verfahrensrüge` | Zeile + BGH · 3 Blöcke zum Wort · ✗ Akte · ✗ Rekonstruktion · ✗ urteilsfremd · Block Verfahrensrüge · Verweis | – |
| **F a) Subsumtion** `stufen`→`sa2` | Tafel mit Stufenleiste a)–d), beide Figuren | tabler:`list-numbers`, `scale`, `file-check` | `Prüfungsstufen · vier Stufen` → `› a) Subsumtionsfehler` → `› a) hier: Tatsache (+)` | Leiste · a) · Erklärung · ✓ Tatsache + BGH · ✓ Täuschung | – |
| **G b) Darstellungsmangel** `sb`→`sb2` | Wortlautkarte § 267 Abs. 1 S. 1 | tabler:`file-alert`, `list-check`, `puzzle-off` | `› b) Darstellungsmangel` → `› b) § 267 Abs. 1 S. 1 StPO` → `› b) Tatsachen für jedes Merkmal` | Karte + 2 Marker · Block · ✗ + BGH | – |
| **H c) Beweiswürdigung** `sc`→`sc3` | Tafel, Hellmers | tabler:`zoom-question`, `file-certificate` | `› c) Beweiswürdigung` → `› c) nur Rechtsfehler` → `› c) hier: schlüssig (+)` | Zeile · 5 Fehlerarten zum Wort · BGH · ✓ schlüssig | – |
| **I d) Strafzumessung** `sd`→`sd3` | Tafel, Wichmann | tabler:`scale`, `zoom-question` | `› d) Strafzumessung` → `› d) nur Rechtsfehler` → `› d) „hoher Schaden“ – unbeziffert` | Zeilen zum Wort · BGH · Urteilszitat · „nirgends beziffert“ | – |
| **K Fall: Vermögensschaden** `schaden`→`traegt` | Tafel mit Waage 85.000 € gegen „Wert des Wagens: ?“, beide Figuren | tabler:`scale`, `cash-banknote`, `car`, `puzzle-off`, `file-x` | `Fall › b) Darstellungsmangel: der Schaden` → `› Gesamtsaldierung` → `› Kauf: Sache den Preis nicht wert?` → `› 85.000 € gezahlt` → `› Wert des Wagens?` → `› Wert nicht festgestellt` → `› Schuldspruch hält nicht stand (-)` | Saldo + BGH · Kauf + BGH · linke Schale · rechte Schale · „nicht festgestellt“ · Block · Schuldspruch (-), Figuren froh | – |
| **L Ergebnis** `beruhen`→`zur` | Tafel, beide Figuren | tabler:`link-off`, `hand-stop`, `file-x`, `arrow-back-up` | `Ergebnis › Beruhen, § 337 Abs. 1 StPO` → `› die Strafe fällt mit` → `› keine eigene Sachentscheidung` → `› Aufhebung, § 353 StPO` → `› Zurückverweisung, § 354 Abs. 2 StPO` | ✓ Beruhen + BGH · Strafe · ✗ selbst entscheiden · Block § 353 · Block § 354 | – |
| **M Klausurtipp** `tipp`→`k4` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | 1. Satz · 2. Reihenfolge · 3. Formulierung · Block | – |
| **N Prüfschema** `sch`→`s5` | breite Karte, Aufbau Punkt für Punkt | – | `Prüfschema › I. …` bis `› V. Beruhen, Aufhebung` | 10 Stufen | – |
| **O Merksatz** `merke`, `m2` | Lexi erklärt (redet), Marker | – | `Merksatz` | 2 Sätze, 3 Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; keine Figurenbewegung, kein Zoom.
**Geräusche:** ein Handlungsgeräusch aus Freesound CC0 (Geldscheine, als Frau Danner zahlt), Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** Stil C, wortgleich mit dem Gesprochenen. Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 06.10.2026), Auslassungen mit „…“, amtlich „daß“/„muß“.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Regal, Urkunde und Halle programmatisch.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Die Strafkammer des Landgerichts verurteilt Herrn Wichmann wegen Betrugs zu einer Freiheitsstrafe von 2 Jahren und 6 Monaten. Nach den Urteilsgründen verkaufte er Frau Danner einen Oldtimer für 85.000 € und versicherte, der Wagen sei unfallfrei. Tatsächlich hatte der Wagen, wie Herr Wichmann wusste, einen schweren Unfallschaden. Frau Danner glaubte ihm und zahlte.
>
> Den Unfallschaden stützt die Kammer schlüssig auf ein Sachverständigengutachten. Was der Wagen mit diesem Schaden wert war, teilt das Urteil nicht mit. Strafschärfend wertet es den „hohen Schaden“.
>
> Rechtsanwältin Hellmers hat rechtzeitig Revision eingelegt. Herr Wichmann meint, der Wagen sei das Geld wert gewesen.
>
> **Was prüft das Revisionsgericht auf die Sachrüge – und hält der Schuldspruch?**
