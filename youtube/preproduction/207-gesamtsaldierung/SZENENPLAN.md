# Folge 207 · Gesamtsaldierung: Der Vermögensschaden beim Betrug § 263 erklärt – Szenenplan

**Stand:** 06.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_207.py`](src/skript_207.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · StGB BT, Themenplan-Format „Schema“. Aufbau nach Auftrag: Hook mit Zahlen als Ziffern (Garagenverkauf, „Designer-Sessel“ 300 €, Nachbau, Gutachten genau 300 €) → Frage → Sachverhalt → § 263 Abs. 1 (Wortlautkarte), Merkmal „Vermögen beschädigt“, Täuschung/Irrtum/Verfügung nur kurz (Verweis Folge 065), Vermögensbegriff in einem Satz → Gesamtsaldierung (vor/nach der Verfügung, Gegenleistung gleicht aus) → Waage 300 € − 300 € = 0 € → kein Schaden trotz Täuschung (BGHSt 16, 321; BGH 2 StR 283/25, wie Folge 204) → Korrekturen: individueller Schadenseinschlag (Kriterien a–c), Eingehungs- und Gefährdungsschaden je ein Satz → Gegenfall 120 € → 180 € → Versuch § 263 Abs. 2 in einem Satz → Klausurtipp mit Lexi (Schaden immer beziffern; ein Satz Verweis auf Folge 204) → Prüfschema → Merksatz (Lexi). Hauptfilm 5:08,5, 4.426 Sprechzeichen (Regelumfang). Vorlagen: 065 (Betrugsschema, nur Verweis), 204 (Darstellungsmangel Schaden, ein Satz Verweis), 203 (Hilfsfunktionen, Renderer), 015 (Namens- und Sichtprüfung), Katzenkönig (Tafel-/Figurenstil).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Gundula (GU), um 60 | Käuferin | `standing/blazer-3` (Blazer Lila `#B8A9F5`, Hose Dunkelgrau `#5A5A6A`), Kopf `Gray Medium` (Haar Grau `#B5B5B5`), Brille `Glasses 3`, Haut `#F0C8A8`. Mimiken `Calm` (redet), `Smile`, `Suspicious`, `Serious`, `Concerned|Serious` | `hilde` (Frau, älter) |
| Alwin (AL), um 45 | Verkäufer beim Garagenverkauf | `standing/walking-1` (T-Shirt Grün `#8FD694`, schwarze Hose der Pose), Kopf `Short 3`, Haut `#EDC3A0`, ohne Bart. Mimiken `Calm`, `Smile` (redet), `Suspicious` (denkt an den Nachbau), `Serious`, `Concerned|Serious` | `stephan` (Mann, mittel) |
| Ulla (UL), um 30 | Gutachterin | `standing/shirt-4` (dunkles Hemd der Pose, Hose Türkis `#7FD6D0`), Kopf `Long`, Haut `#B9805A`. Mimiken `Calm` (redet), `Suspicious`, `Serious` | `lucy` (Frau, jung) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Garagenverkauf: Alwin (`_r`) und Gundula blicken einander an; Leseecke: Gundula (`_r`) blickt zu Ulla; Tafelfolien: alle zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `GU_redet`, `AL_redet`, `UL_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (blazer-1/-2 und shirt-1/-2 bewusst nicht), keine Karikatur. 58 Figuren-PNGs in `../peeps/op_207/` (Drive-Master).
- **Klischeeprüfung:** Alwin ist ein gewöhnlicher Privatverkäufer (T-Shirt, Hose), ruhige oder freundliche Mimik, nie „fies“, keine Herkunfts- oder Hautfarbenzuschreibung (heller Hautton). Gundula als aufmerksame ältere Käuferin, nicht naiv. Ulla als sachliche Fachfrau.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Auftragsliste, nicht in `namen_reserviert.txt` (dort für 207 eingetragen) und per Volltextsuche in keinem Skript, Szenenplan oder Abnahmebogen unter `preproduction/`: Gundula, Alwin, Ulla. Verworfen: Hannes (005, 104 …), Helmut (Stimmenname), Lothar/Edmund/Ortwin (früher verwendet). Nie im Genitiv.
- **Stimmen** nur aus dem Pool (stephan, hilde, lucy; christian nicht eingesetzt, daher kein stephan/christian-Dialog). Folge 204 nutzte dasselbe Trio (Pool-Vorgabe des Koordinators) – hier andere Rollen (204: stephan Angeklagter, lucy Anwältin, hilde Käuferin; 207: hilde Käuferin, stephan Verkäufer ohne Strafbarkeit, lucy Gutachterin), Posen und Schauplätze.

**Abweichung von den letzten Folgen (204 Kanzlei/Oldtimer, 205 Büro/Suchmaschine, 206 Vertretung):** neue Schauplätze **Garagenverkauf** (Phosphor-Garage, Sessel, Preisschild, Geldschein wandert) und **Leseecke** (Stehlampe, Regal mit Büchern, Pflanze, Lupe der Gutachterin). Neu ist die **Balkenwaage** aus Tuschelinien (im Gleichgewicht bzw. geneigt). Posen `blazer-3`, `walking-1`, `shirt-4` kommen in 204–206 nicht vor (dort `shirt-3`, `crossed_arms-2`, `easing-1/-2`, `resting-1/-2`, `pointing_finger-1`, `robot_dance-2`); kein Polka-Dots-Muster. Flohmarktszenen früherer Folgen (161, 179) liegen weit zurück und zeigen anderes Personal.
**Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Garagenverkauf** `fall`→`mit` | ab 0,0 s Garage, Boden, Pillen „Samstagvormittag“, „Garagenverkauf“; Gundula tritt auf („sucht einen bequemen Sessel“, „für ihre Leseecke“); Alwin und der Sessel mit „„Designer-Sessel““ und „300 €“; Denkblase Alwin „kein Original – ein Nachbau“; „Alwin hält 300 € für den richtigen Preis“; Blasen Gundula „Ist das wirklich ein Original?“, Alwin „Ja, ein echtes Designerstück.“; Geldschein wandert zu Alwin („Gundula zahlt 300 € bar“); Sessel steht bei Gundula („und nimmt den Sessel mit“) | ph:`garage`; tabler:`armchair`; fluent-hc:`euro-banknote` | `Fall · Samstagvormittag: ein Garagenverkauf` (ab 0,0 s) → … → `Fall · Gundula nimmt den Sessel mit` | Geldscheine (`szene_207geld_1`) beim Bezahlen |
| **A2 Leseecke** `leseecke`→`frage2` | Stehlampe, Sessel, Regal mit Büchern, Pflanze; Ulla tritt auf, Lupe am Sessel; Blase Ulla „Ein Nachbau, aber gut gemacht. Er ist genau 300 € wert.“, Pille „Wert: 300 €“; Fragen „Gundula wurde getäuscht.“, „Aber ist ihr Vermögen beschädigt?“, „Antwort: die Gesamtsaldierung“ | ph:`lamp`; fluent-hc:`books`, `potted-plant`, `magnifying-glass-tilted-left`; tabler:`armchair` | `Fall · Der Sessel in der Leseecke` → … → `Fall · Die Antwort: die Gesamtsaldierung` | Sessel wird abgestellt (`szene_207sessel_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,7 s | – | `Sachverhalt` | – |
| **C1 § 263 Abs. 1** `p263`→`v065` | Wortlautkarte (vollständig, Marker „Vermögen eines anderen“, „beschädigt“), Haken Täuschung/Irrtum/Verfügung, Pille Verweis Folge 065; Gundula, Alwin | fluent-hc:`balance-scale`, `white-question-mark`, `euro-banknote` | `§ 263 Abs. 1 StGB › Wortlaut` → `› Merkmal: Vermögen beschädigt` → … | – |
| **C2 Vermögen** `heute`, `vbegr` | Pille „nur noch offen …“, Block Vermögensbegriff (Rspr.), Reihe Vermögensgegenstände (Geld, Sessel, Haus, Karte) | ph:`wallet`; fluent-hc:`money-bag`, `house`, `euro-banknote`; tabler:`armchair`, `credit-card` | `§ 263 Abs. 1 StGB › Vermögensschaden: …` | – |
| **D Gesamtsaldierung** `saldo`→`minder` | Blöcke vorher/nachher mit Pfeil, Haken Gegenleistung, Block Minderung | fluent-hc:`balance-scale`, `euro-banknote`; tabler:`armchair`, `calculator` | `… › Gesamtsaldierung` → `› vorher …` → `› nachher …` → `› Gegenleistung gleicht aus` → `› Schaden = verbleibende Minderung` | – |
| **E Waage** `rech`→`null` | Balkenwaage im Gleichgewicht, links Geld „vorher: 300 € Geld“, rechts Sessel „nachher: Sessel, 300 € wert“, Rechnung „300 € − 300 € = 0 €“, Kreuz „ein Schaden bleibt nicht“ | Waage (Bausteine), fluent-hc:`euro-banknote`, `balance-scale`; tabler:`armchair`, `calculator` | `… › im Fall: die Waage` → … → `§ 263 Abs. 1 StGB › Vermögensschaden (−)` | – |
| **F Kein Schaden trotz Täuschung** `folge`→`kein` | Zeile, Block „§ 263 schützt das Vermögen …“, Melkmaschinen-Fall, Block Nachbau statt Original, Kreuz „vollendeter Betrug von Alwin“ | fluent-hc:`white-question-mark`, `balance-scale`, `cow-face`; tabler:`armchair` | `… › kein Schaden trotz Täuschung` → … → `Ergebnis · kein vollendeter Betrug von Alwin` | – |
| **G1 Individueller Schadenseinschlag** `indiv`→`i4` | „1. Korrektur“, Kriterien a)–c) zum Wort, Block „Hier nicht …“, Kreuz | tabler:`armchair`, `credit-card`; ph:`wallet`; fluent-hc:`books`, `white-question-mark` | `… › Korrektur: individueller Schadenseinschlag › a) … › im Fall (−)` | – |
| **G2 Weitere Korrekturen** `eing`→`gef2` | Blöcke „2. Eingehungsschaden“, „3. Gefährdungsschaden“, Haken „beziffert“ | fluent-hc:`handshake`, `warning`; tabler:`calculator` | `… › Eingehungsschaden` → `› Gefährdungsschaden` → `› … beziffern` | – |
| **H Gegenfall** `gegen`→`gerg` | Waage leer im Gleichgewicht; Ulla: „Dieser Nachbau ist nur 120 € wert.“; Waage geneigt (Geld schwerer): „gegeben: 300 €“, „erhalten: 120 €“, „300 € − 120 € = 180 €“, Haken „mit Vorsatz und Bereicherungsabsicht: Betrugstatbestand (+)“ | Waage, fluent-hc:`euro-banknote`; tabler:`armchair` | `Gegenfall › …` | – |
| **I Versuch** `versuch` | Wortlautkarte § 263 Abs. 2, Kreuz, Zeilen, § 22; Denkblase Alwin „300 € sind der richtige Preis“ | – | `Versuch, § 263 Abs. 2 StGB › im Ausgangsfall (−)` | – |
| **J Klausurtipp** `tipp`→`tipp4` | hellgelbe Tafel, Lexi warnt: beziffern, Rechnung, BVerfG, Verweis Folge 204, „nichts übrig …“ | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | – |
| **K Prüfschema** `sch`→`s4` | breite Karte, 1.–4., a)–c) zum Wort | fluent-hc:`balance-scale`; tabler:`calculator` | `Prüfschema Vermögensschaden › …` | – |
| **L Merksatz** `merke`, `mk2` | Lexi erklärt, Marker „kein Schaden“, „vor und nach“, „Zahl in Euro“ | – | `Merksatz` | – |

**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 263 Abs. 1 vollständig (gesprochen nur das Merkmal; die Karte steht ≈ 15 s als Zitat), § 263 Abs. 2 (wörtlich), wörtlich nach gesetze-im-internet.de.
**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; Bewegung: Geldschein von Gundula zu Alwin (A1).
**Zahlen** auf Blasen, Tafeln und Pillen in Ziffern („300 €“, „120 €“, „180 €“, „§ 263 Abs. 1 StGB“). **Kein Fiktiv-Hinweis.**
**Lizenzen der Requisiten:** Tabler Icons (MIT), Phosphor (MIT), Fluent Emoji High Contrast (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (**CC BY 4.0**, Namensnennung in `beschreibung.txt`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Samstagvormittag, Garagenverkauf: Gundula (um 60) sucht einen bequemen Sessel für ihre Leseecke. Alwin bietet vor seiner Garage einen „Designer-Sessel“ für 300 € an. Er weiß, dass es kein Original ist, sondern ein Nachbau; 300 € hält er aber für den richtigen Preis.
>
> Gundula: „Ist das wirklich ein Original?“ Alwin: „Ja, ein echtes Designerstück.“ Gundula zahlt 300 € bar und nimmt den Sessel mit.
>
> Später schätzt die Gutachterin Ulla den Sessel: ein gut gemachter Nachbau, genau 300 € wert.
>
> **Hat sich Alwin wegen Betrugs nach § 263 StGB strafbar gemacht?**
