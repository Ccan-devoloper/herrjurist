# Folge 037 · Firmenwagen geschrottet: Arbeitnehmerhaftung – wer zahlt den Schaden? – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_037.py`](src/skript_037.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker-Fall laut Themenplan). Die Leitentscheidung BAG GS 1994 ist ein Vorlagebeschluss ohne erzählbaren Einzelfall; erzählt wird ein Übungsfall entlang des Hooks aus dem Themenplan (Firmenwagen, Auffahren auf einen Lastwagen). Ablauf: Fall (Dienstfahrt, Auffahren) → Büro (Forderung) → Frage → Sachverhalt → Wortlaut § 280 I → Prüfung I., II., Schaden → III. Vertretenmüssen mit Wortlaut § 619a (Beweislast) → Innerbetrieblicher Schadensausgleich (BAG GS) → 1. betrieblich veranlasst (Gegenbeispiel Privatfahrt) → 2. Grad des Verschuldens (vier Stufen) → Subsumtion und 3. Abwägung → Vollkasko und Ergebnis → Gegenfall grobe Fahrlässigkeit/Vorsatz → Abgrenzung § 105 SGB VII → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm ≈ 6:07 (5.236 Zeichen, Grenze 6.200). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Imke (IM), um 30 | Außendienstmitarbeiterin, Fahrerin des Firmenwagens | `standing/easing-1` (offene Jacke Blau `#7FB2F0`, weißes Oberteil, schwarze Hose), Kopf `Medium Straight`, Haut `#E9BE98`; Mimiken `Smile`, `Fear` (Schreck, redet), `Concerned|Serious` (Sorge, redet), `Serious`, `Suspicious`, `Smile Big|Smile`, `Calm` | `julia` (Frau, jung) |
| Herr Schäfer (SC), um 55 | Inhaber des Werkzeughandels, Arbeitgeber („Chef“) | `standing/blazer-3` (dunkler Anzug `#3D3D58`), Kopf `Short 4_2` mit grauem Haar, Brille `Glasses 2`, **kein Bart**, Haut `#D9A07A`; Mimiken `Serious` (streng, redet), `Calm`, `Suspicious`, `Concerned|Serious` | `christian` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht aus früheren Folgen: Imke, Schäfer. Genitiv „Imkes“ im Sprechtext vermieden (Lehre aus 015 „Gerdas“).
- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts (Fallszenen: Imke zum Wagen bzw. zu Herrn Schäfer).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `IM_schreck`, `IM_redet`, `SC_redet` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool** marc, julia, ela_froh, christian; gebraucht: julia, christian. Keine Überschneidung mit 036 (sabrina, niklas, laura_ruhig, helmut).
- Figuren-PNGs: `../peeps/op_037/` (56 Dateien, nicht im Repository, im Drive-Master). Kontaktbild `out/besetzung_037.png`.
- Unfall zurückhaltend: Blechschaden (Tabler `car-crash`), niemand verletzt, keine Verletzten im Bild; § 105 SGB VII nur als gedachter Fall (Symbol `users`).

**Abweichung von den letzten Folgen:** 036 (Verfahrensarten BVerfG; dort `blazer-3` mit blauem Sakko für Herrn Pohl – hier dunkler Anzug, grauer Kopf `Short 4_2`, andere Hautfarbe), 035 (Tötungsdelikte, Lerngruppe), 034 (Schwarzarbeit), 031 (Selbstbedienungsladen). Hier neu: Landstraße mit Stau (Firmenwagen, Lastwagen) und das Büro des Inhabers.

## Szenen

Alle Szenen auf Cremegrund (Tag).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Die Dienstfahrt** `fall`–`kasko0` | Landstraße; Imke neben dem Firmenwagen, steigt ein; Wagen fährt zum Stau; Lastwagen am Stauende; Wagen rollt zu nah heran, Aufprall; Imke steigt aus, spricht | tabler: `car` (Blau), `tools` (Gelb), `map-pin` (Rot), `truck` (Gelb), `car-crash` (Blau), `shield-check` (Grün), `receipt`, `shield-off`; Straße aus `linienzug` | `Fall · Die Dienstfahrt` (ab 0,0 s) | Imke am Wagen · Einsteigen · Fahrt · Firmenwagen · Kunde · Stau · Abstand · Aufprall · Blase · niemand verletzt · Haftpflicht · mitversichert · 12.000 € · keine Vollkasko | Einsteigen `szene_037tuer_1`, Anfahren `szene_037anfahren_1`, Aufprall `szene_037aufprall_1` |
| **B Im Büro** `buero`–`frage2` | Büro, Schreibtisch mit Rechnung; Herr Schäfer verlangt das Geld, Imke widerspricht | tabler: `receipt`, `scale`; Tisch aus `karte` | `Fall · Im Büro` → `Fall · Die Frage` | Büro · Rechnung · Blase Schäfer · Blase Imke · Frage · Verschuldensgrad | – |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **D Wortlaut § 280 I** `agl`–`w280b` | Wortlautkarte mit Markern; Imke und Schäfer | tabler: `car-crash` | `Anspruch · § 280 Abs. 1 BGB` | Titel · Karte · Marker (4) | – |
| **E Prüfung I./II./Schaden** `sv1`–`schad` | Tafel, Symbol wechselt | tabler: `file-text`, `car`, `receipt` | `A. Schäfer gegen Imke, § 280 Abs. 1 BGB › I. …` → `› II. …` → `› Schaden` | 5 | – |
| **F § 619a** `w619`–`bew3` | Wortlautkarte § 619a, darunter Beweislast | tabler: `scale` | `A. Schäfer gegen Imke › III. Vertretenmüssen, § 619a BGB` → `· Beweislast` | Karte · Marker (3) · Entlastung · Beweislast · fahrlässig | – |
| **G Innerbetrieblicher Schadensausgleich** `ibs`–`risk` | Tafel BAG GS | tabler: `building-store` | `… › Haftung beschränkt?` → `Innerbetrieblicher Schadensausgleich · BAG GS 1994` | 6 | – |
| **H 1. Betrieblich veranlasst** `bv`–`bv4` | Tafel, Imke; Dienstfahrt vs. Wochenende | tabler: `map-pin`, `car`, `beach` | `Haftungsbeschränkung › 1. betrieblich veranlasste Tätigkeit` | 5 | – |
| **I 2. Grad des Verschuldens** `stufen`–`st4` | vier Farbstufen | tabler: `circle-half`, `alert-triangle` | `Haftungsbeschränkung › 2. Grad des Verschuldens` | 5 | – |
| **J Abwägung** `mittel`–`abw3` | Subsumtion, Abwägungsliste | tabler: `scale` | `… › 2. Grad des Verschuldens: Imke` → `… › 3. Abwägung aller Umstände` | 7 | – |
| **K Vollkasko, Ergebnis** `kasko`–`erg2` | Tafel, Ergebnisblock | tabler: `shield-off`, `chart-pie` | `… › 3. Abwägung · Vollkasko` → `A. Schäfer gegen Imke › Ergebnis` | 5 | – |
| **L Gegenfall** `grob`–`vors` | Handy am Steuer (Annahme), Erleichterung, keine Obergrenze, Vorsatz | tabler: `device-mobile-message` | `Gegenfall · grobe Fahrlässigkeit` → `Gegenfall · Vorsatz` | 7 | – |
| **M Abgrenzung § 105 SGB VII** `pers`, `pers2` | gedachter Personenschaden eines Kollegen | tabler: `users` | `Abgrenzung · Personenschaden, § 105 SGB VII` | 3 | – |
| **N Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (2 Stände) | 5 | – |
| **O Klausurschema** `sch`–`sc8` | breite Karte, Aufbau Punkt für Punkt | – | `Klausurschema` | 10 | – |
| **P Merksatz** `merke`, `m2` | Lexi erklärt, Merksatz mit Markern | – | `Merksatz` | 5 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegung nur bei der Fahrt und beim Auffahren.
**Blasen:** wortgleich mit dem Gesprochenen.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Imke arbeitet im Außendienst eines Werkzeughandels und verdient 3.000 Euro brutto im Monat. Auf einer Dienstfahrt zu einem Kunden ist sie im Stau einen Moment unaufmerksam, hält zu wenig Abstand und fährt auf einen Lastwagen auf. Ein grober Verstoß liegt nicht vor. Niemand wird verletzt.
>
> Den Schaden am Lastwagen zahlt die Haftpflichtversicherung des Firmenwagens. Die Reparatur des Firmenwagens kostet 12.000 Euro; eine Vollkaskoversicherung besteht nicht. Ihr Chef, der Inhaber Herr Schäfer, verlangt den vollen Betrag von ihr.
>
> **Muss Imke die 12.000 Euro ersetzen?**
