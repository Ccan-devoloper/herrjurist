# Folge 251 · Preisfehler Onlineshop: Muss der Händler liefern? (§ 119 BGB) – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_251.py`](src/skript_251.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · BGB AT · Alltagsfall. Aufbau nach Auftrag: Hook (49 € statt 499 €, Zahlen als Ziffern) → Lager bei Frau Wetzel (Softwarefehler) → Telefonat (Anfechtung, „zwei Bestätigungen“) → Frage → Sachverhalt → Anspruch § 433 Abs. 1 Satz 1, zwei Stufen → I. Vertragsschluss (Shopseite = Einladung, Verweis Folge 014; Bestellung = Angebot; Wortlautkarte § 312i Abs. 1 Satz 1 Nr. 3: Eingangsbestätigung in der Regel Wissenserklärung, Auslegung im Einzelfall; zweite Mail = Annahme, BGH) → II. Anfechtung (Wortlautkarte § 119 Abs. 1; Vertippen = Erklärungsirrtum; Wortlautkarte § 120 und BGH VIII ZR 79/04 zum Softwarefehler; Fortwirken in der Annahme; Abgrenzung Kalkulationsirrtum; § 121 unverzüglich; § 142 Abs. 1) → Folge § 122 (Wortlautkarte, Vertrauensschaden, Abs. 2) → Ergebnis → Klausurtipp (Lexi) → Prüfungsschema → Merksatz (Lexi). Hauptfilm 6:10,2 (5.457 vertonte Zeichen). Vorlagen: 245 (Werkzeuge, Hilfsfunktionen, Wortlautkarten), 014 (invitatio, nur verwiesen), 023 (Anfechtungsschema, Formulierungen abgeglichen), 015 (Namens-/Sichtprüfung), Katzenkönig (Stil).

**Darstellung:** Personen fiktiv; keine echten Shops oder Marken (Shopseite nur mit „Onlineshop“ überschrieben, Bildschirm, Mails, Lager aus Grundformen und Tabler-Icons, ohne Logo, Shopname oder Herstellerkennzeichen); kein Fiktiv-Hinweis.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Kübler (KU), um 35 | Käufer, verlangt Lieferung | `standing/easing-1` (offenes Hemd Grün `#8FD694`, Shirt Weiß, schwarze Hose der Pose), Kopf `Short 1`, Haut `#C99470`, kein Bart, keine Brille. Mimiken `Calm`, `Driven` (redet), `Smile`, `Smile Big\|Smile`, `Awe`, `Suspicious`, `Serious`, `Concerned\|Serious` | `marc` (Mann, mittel) |
| Frau Wetzel (WE), um 45 | Händlerin mit kleinem Onlineshop, ficht an | `standing/resting-2` (schwarzes Oberteil der Pose, Hose Rot `#F07A6A`), Kopf `Medium Bangs 2`, Brille `Glasses 4`, Haut `#F2C9A6`. Mimiken `Calm`, `Serious` (redet/ernst), `Smile`, `Suspicious`, `Concerned\|Serious`, `Fear` (Schreck), `Driven` | `sabrina` (Frau, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem Pool (william, sabrina, marc, laura_ruhig): besetzt `marc` und `sabrina`; `william` und `laura_ruhig` nicht besetzt. Vorfolgen 249/250 nutzten `lucy`, `stephan`, `hilde` – keine Überschneidung.
- **Blickrichtung:** Beide Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. A1: Herr Kübler blickt nach links zum Bildschirm. A2: Frau Wetzel blickt nach links zum Bildschirm. A3/Ergebnis (geteiltes Bild): Frau Wetzel links (`_r`) und Herr Kübler rechts (Grundansicht) blicken zur Trennlinie, also zueinander. Tafelszenen alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund** (auch `Concerned|Serious`, `Smile Big|Smile`); Mundzustände a/o/e nur in `KU_redet`, `WE_redet` (je links/rechts) und Lexi. 52 Figuren-PNGs in `../peeps/op_251/` (nicht im Repository, im Drive-Master).
- **Klischeeprüfung:** Händlerin sachlich, kein „gieriger Händler“, Käufer ohne Häme; keine Prothesen-Posen (`blazer-1`, `shirt-1` verworfen), keine Polka Dots, keine Bärte; Frau Wetzel bewusst ohne Dutt (Verwechslung mit Lexi); keine Zuordnung von Herkunft oder Hautfarbe zu einer Rolle.
- **Namen:** Kübler, Wetzel – eindeutig deutsche Aussprache (ü; tz), nicht in der Liste vergebener Namen, per `grep -rliw` in keiner `*.py/*.md/*.json/*.csv/*.txt` unter `youtube/` (verworfen: Niklas – Stimmenname, Ruben/Leander – englisch lesbar), in `namen_reserviert.txt` als „251: Kübler, Wetzel“ eingetragen. Gesprochen nur von der Erzählerin (Figuren nennen sich nicht).

**Abweichung von den letzten drei Folgen (248–250):** Posen `easing-1`, `resting-2` – in 248 (`blazer-3`, `pointing_finger-2`, `blazer-4`, `crossed_arms-1`), 249 (`easing-2`, `blazer-2`, `shirt-3`, `resting-1`) und 250 (`shirt-4`, `crossed_arms-2`) nicht verwendet; keine Polka Dots. Schauplätze **Zuhause bei Herrn Kübler** (Schreibtisch, Bildschirm mit Shopseite und Posteingang, Fenster), **Lager von Frau Wetzel** (Regal mit Paketen, Bildschirm, Tastatur) und **Telefonat als geteiltes Bild** – neu gegenüber 248–250. Tageslicht-Cremegrund durchgehend.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Zuhause** `fall`→`mail2` | ab 0,0 s Schreibtisch, Bildschirm („Onlineshop“), Fenster, Herr Kübler mit Namensschild; Fernseher-Icon und „Fernseher“ zu `shop`, „49 €“ (rot) zum Wort, Pille „sonst 499 €“, Haken „bestellt“ + Pille „Montagabend“, Mailkarte 1 „Vielen Dank, wir haben Ihre Bestellung erhalten.“, Mailkarte 2 „Ihr Auftrag wird jetzt von unserer Versandabteilung bearbeitet.“ + Pille „Dienstagmorgen“ | Tisch, Bildschirm, Fenster aus Grundformen (`tisch()`, `monitor()`, `fenster()`, `mailkarte()`); tabler `device-tv`, `mail` | `Fall · Bei Herrn Kübler zu Hause` → `· Fernseher für 49 € im Onlineshop` → `· Herr Kübler bestellt sofort` → `· 1. Mail: Bestellung erhalten` → `· 2. Mail: Auftrag wird bearbeitet` | – |
| **A2 Lager** `lager`→`anruf` | Regal mit Paketen, Bildschirm „Bestellung: Fernseher“, „eingegeben: 499 €“, Pfeil + Käfer (Softwarefehler) zu „Software“, „im Shop: 49 €“ (rot); Frau Wetzel erschrickt; Telefon an ihrer Seite + „ruft sofort an“ | tabler `package`, `keyboard`, `bug`, `device-mobile` | `Fall · Dienstagmittag im Lager von Frau Wetzel` → `· eingegeben 499 €, im Shop 49 €` → `· Frau Wetzel ruft sofort an` | Telefonklingeln (`szene_251telefon_1`, Freesound CC0 725445) |
| **A3 Telefonat** `w1`→`frage3` | geteiltes Bild, beide mit Telefon; Blase Wetzel „Der Preis im Shop war ein Softwarefehler. Ich fechte den Kauf an und liefere nicht.“, Blase Kübler „Aber ich habe zwei Bestätigungen! Ich will den Fernseher für 49 €.“; drei Frage-Pillen | tabler `package`, `device-mobile`; Fenster | `Fall · Frau Wetzel: „Ich fechte den Kauf an“` → `· Herr Kübler: „zwei Bestätigungen“` → `Die Frage · …` (3 Stände) | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | – |
| **C Anspruch** `ansp`→`aufbau2` | Herr Kübler gegen Frau Wetzel, „Lieferung: Übergabe und Übereignung“, § 433 Abs. 1 Satz 1, Blöcke Stufe 1/Stufe 2; beide Figuren | tabler `device-tv`, `list-check` | `Anspruch · § 433 Abs. 1 Satz 1 BGB: Lieferung` → `› Stufe 1: Kaufvertrag?` → `› Stufe 2: Anfechtung?` | – |
| **D1 I. Vertragsschluss** `inv`→`best` | Kreuz „Fernseher im Shop: noch kein Angebot“, „invitatio ad offerendum“ + BGH, Block Verweis Folge „Angebot und Annahme“, Haken „Angebot: die Bestellung“; Kübler | tabler `browser`, `shopping-cart` | `I. Vertragsschluss · …` (3 Stände) | – |
| **D2 1. Mail** `w312`→`erhalten` | **Wortlautkarte § 312i Abs. 1 Satz 1 Nr. 3** (Marker „Zugang von dessen“, „unverzüglich“, „elektronischem Wege“), Block „in der Regel nur Wissenserklärung, keine Annahme“ + X ZR 37/12 Rn. 19, „Einzelfall: Auslegung aus Sicht des Empfängers“, Kreuz „Wir haben Ihre Bestellung erhalten.“: nur Eingang; Kübler | tabler `mail`, `info-circle` | `I. Vertragsschluss › 1. Mail: …` (4 Stände) | – |
| **D3 2. Mail** `ann`→`vertrag` | Mailzitat, Haken „kündigt vorbehaltlose Ausführung an“, „= Annahme“ + BGH, „vom Computer verschickt: trotzdem Erklärung von Frau Wetzel“ + Rn. 17, grüner Block „Kaufvertrag geschlossen: Fernseher für 49 €“; Kübler | tabler `mail`, `mail-check`, `device-desktop`, `file-text` | `I. Vertragsschluss › 2. Mail: …` (4 Stände) | – |
| **E II. Anfechtung § 119** `anf`→`hier` | **Wortlautkarte § 119 Abs. 1** (Marker „anfechten“, „über deren Inhalt“, „überhaupt nicht abgeben“), Haken „vertippt: Erklärungsirrtum, § 119 Abs. 1 Alt. 2 BGB“, Kreuz „Frau Wetzel hat sich nicht vertippt: den Fehler machte die Software“; Wetzel | tabler `help-circle`, `keyboard`, `bug` | `II. Anfechtung · Anfechtungsgrund` → … (4 Stände) | – |
| **F § 120** `w120`→`bereich` | **Wortlautkarte § 120** (Marker „Einrichtung“, „unrichtig übermittelt“, „angefochten“), Block BGH „kein Unterschied – selbst vertippt oder Software verfälscht das richtig Eingegebene“, Haken „auch im eigenen System: Erklärungsirrtum“; Wetzel | tabler `send`, `bug`, `device-desktop` | `II. Anfechtung › Gedanke des § 120 BGB` → … (3 Stände) | – |
| **F2 Was wird angefochten?** `fort`→`kaus` | Kasten „Shopseite: 49 € / kein Angebot“ (Kreuz) → Pfeil → Kasten „2. Mail: Annahme / angefochten“, „Fehler wirkt fort …“ + BGH, Haken Kausalität; beide | tabler `browser`, `mail-check` | `II. Anfechtung › …` (3 Stände) | – |
| **G Kalkulationsirrtum** `kalk`, `kalk2` | „verrechnet schon bei der Berechnung des Preises“, Block „= Irrtum im Beweggrund“, Kreuz „grundsätzlich keine Anfechtung, selbst wenn eine Software falsch gerechnet hat“ + BGH; Wetzel | tabler `calculator`, `ban` | `Abgrenzung · …` (2 Stände) | – |
| **H Frist und Folge** `frist`→`p142` | § 121 unverzüglich, „ohne schuldhaftes Zögern, ab Kenntnis“, Haken „am selben Mittag gegenüber Herrn Kübler“ (§ 143), roter Block § 142 Abs. 1; Wetzel | tabler `clock`, `device-mobile`, `file-x` | `II. Anfechtung › …` (3 Stände) | – |
| **I § 122** `w122`→`abs2` | **Wortlautkarte § 122 Abs. 1** (gekürzt; Marker „Schaden zu ersetzen“, „Gültigkeit der Erklärung“), Haken Vertrauensschaden + Begriff, Kreuz „nicht ersetzt: was er bei Erfüllung gehabt hätte, also nicht der günstige Fernseher“, Block § 122 Abs. 2; Kübler | tabler `coin-euro`, `device-tv`, `eye` | `Folge der Anfechtung · …` (4 Stände) | – |
| **J Ergebnis (Telefonat)** `erg`, `erg2` | Schauplatz A3 ohne Blasen; Kreuz „kein Lieferanspruch …“, Haken „Vertrag erst mit der 2. Mail – den hat sie wirksam angefochten“ + Fundstellen | wie A3 | `Ergebnis · …` (2 Stände) | – |
| **K Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (3 Stände) | – |
| **L Prüfungsschema** `sch`→`s3` | breite Karte, 8 Zeilen zum Wort | – | `Prüfungsschema` → je Gliederungspunkt | – |
| **M Merksatz** `merke`, `merk2` | Lexi erklärt (redet), zwei Sätze mit Markern | – | `Merksatz` | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), jeweils auf der Blickseite der Figur. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern.
**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** ein Handlungsgeräusch (Telefonklingeln, als Frau Wetzel anruft); Freesound-API am 08.10.2026 gesperrt (HTTP 403), deshalb bitgleiche Kopie einer vorhandenen CC0-Datei aus `sfx3` unter eigenem Namen, Herkunft in `geraeusche_herkunft.json`. Ein Tippgeräusch wurde verworfen, weil Frau Wetzel nicht an der Tastatur steht.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Tisch, Bildschirm, Regal, Mailkarten, Fenster programmatisch.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Im Onlineshop von Frau Wetzel kostet ein Fernseher plötzlich 49 € statt 499 €. Sie hatte 499 € in ihr System eingegeben; die Software hat den Preis unbemerkt falsch in den Shop übertragen.
>
> Am Montagabend bestellt Herr Kübler. Sofort kommt eine automatische E-Mail: „Vielen Dank, wir haben Ihre Bestellung erhalten.“ Am Dienstagmorgen folgt eine zweite: „Ihr Auftrag wird jetzt von unserer Versandabteilung bearbeitet.“
>
> Am Dienstagmittag bemerkt Frau Wetzel den Fehler, ruft Herrn Kübler sofort an und ficht den Kauf an. Er verlangt den Fernseher für 49 €.
>
> **Muss Frau Wetzel liefern?**
