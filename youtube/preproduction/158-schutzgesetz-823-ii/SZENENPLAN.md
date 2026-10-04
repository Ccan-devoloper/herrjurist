# Folge 158 · § 823 II BGB: Schutzgesetzverletzung – das Prüfungsschema – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_158.py`](src/skript_158.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Deliktsrecht, Themenplan-Format „Schema“. Hook nach Plan: „Der Nachbar fährt ohne Führerschein und beschädigt beim Rangieren dein Auto.“ Beispielfall: Hiltrud hat ihr Auto am Straßenrand einer Wohnstraße geparkt; ihr Nachbar Burkhard (keine Fahrerlaubnis, Halter seines Autos) setzt rückwärts aus seiner Einfahrt auf die Straße, verschätzt sich und streift ihr Auto (Kratzer am hinteren Kotflügel, 900 €). Ablauf: Fall → Fahrerlaubnis/Führerschein → Frage → Sachverhalt → § 823 Abs. 2 S. 1, 2 BGB (Wortlautkarte) → Aufbau in sechs Schritten → I. Schutzgesetz (Wortlautkarte Art. 2 EGBGB, BGH-Formel als Zitatkarte, Allgemeinheit/Reflex) → Klassiker §§ 223, 263 StGB, Parallele Schutznormtheorie → § 21 StVG (Wortlautkarten § 21 Abs. 1 Nr. 1 und § 2 Abs. 1 S. 1 StVG) → II. Schutzbereich persönlich/sachlich → III. Verstoß, IV. Rechtswidrigkeit → V. Verschulden (Satz 2) → VI. Schaden, Kausalität, §§ 249 ff. → Vorteil von Abs. 2 (reiner Vermögensschaden) → Lösung (daneben Abs. 1 und § 7 StVG) → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 6:33,0.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Hiltrud (HI), um 45 | Geschädigte, ihr Auto parkt am Straßenrand | `standing/shirt-4` (schwarze Bluse mit Knöpfen, Hose Rot `#F07A6A`, weiße Schuhe), Kopf `Bangs` (Haar Kastanienbraun `#8A5A34`), Haut `#F2C9A6`; Mimiken `Calm`, `Fear` (beim Streifen), `Rage\|Serious` (redet), `Serious`, `Suspicious`, `Concerned\|Serious`, `Smile`, `Solemn` | `laura_ruhig` (Frau, mittel) |
| Burkhard (BU), um 60 | Nachbar ohne Fahrerlaubnis, Halter und Fahrer | `standing/easing-1` (offenes Hemd Beige `#D6B48A` über weißem Shirt, schwarze Hose), Kopf `Gray Medium` (Haar Grau `#C9C9C9`), Brille `Glasses 2`, Haut `#E3B08C`, kein Bart; Mimiken `Calm`, `Suspicious`, `Fear` (nach dem Aussteigen), `Concerned\|Serious` (redet, kleinlaut), `Serious`, `Tired`, `Solemn` | `william` (Mann, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links, zur Tafel), `_r` nach rechts. In der Straßenszene steht Hiltrud links vor ihrem Haus und blickt nach rechts zur Straße und zu Burkhard; Burkhard steht rechts und blickt nach links. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e (Explaining / Concerned Fear / Hectic, Schnitt bei 60 %) nur in `HI_redet`, `BU_redet` (je links/rechts) und Lexi. **Stimmen** nur aus dem Pool (laura_ruhig, william; sabrina und marc nicht gebraucht – beide in 149 und 155 eingesetzt, Vorfolge 157 nutzt stephan/lucy). **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keinem Skript, Szenenplan, Rechtsstand oder Abnahmebogen unter `youtube/preproduction/` (Volltextsuche 04.10.2026): Hiltrud, Burkhard – nie im Genitiv („das Auto von Hiltrud“). Namensschildfarben wie die Autos (Hiltrud Gelb, Burkhard Blau). Figuren-PNGs: `../peeps/op_158/` (52 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- Posen der letzten drei Folgen (155: `blazer-4`, `walking-3`, `sitting/hands_back-1`; 156: `easing-2`, `shirt-3`, `walking-2`, `robot_dance-2`, `pointing_finger-2`; 157 lag beim Start ohne Figurenrezept vor) nicht verwendet. Zuerst erwogen: `robot_dance-3` für Hiltrud – verworfen, weil fast gleich wie Lexi (`robot_dance-1`). Keine Polka Dots, keine Prothesen-Posen, keine Bärte, keine Karikatur.
- Schauplatz neu: **Wohnstraße am Tag** in Seitenansicht (graue Straße mit Bordsteinkante, rechts gepflasterte Einfahrt, zwei Wohnhäuser als Tabler-Icons, ein Baum). 149 hatte einen Supermarktparkplatz, 147 eine Stadtstraße, 124 eine Dorfstraße.
- **Kein Aufprallbild:** Burkhards Auto rollt langsam rückwärts, bis sein Heck das Heck von Hiltruds Auto streift; danach ein feiner Kratzerstrich am hinteren Kotflügel. Leises Schaben statt Aufprallgeräusch.
- Cremegrund durchgehend, Tageslicht.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Wohnstraße** `fall`–`frage` | Straße, Einfahrt rechts; Hiltruds gelbes Auto parkt (blickt nach links), Burkhards blaues Auto steht in der Einfahrt (blickt nach rechts) | tabler:`home` (Gelb, Blau), `tree` (Grün), `car` (Gelb gespiegelt, Blau), `license-off` (Hellrot), `receipt-euro`; Pfeil, Kratzer programmatisch | `Fall · In der Wohnstraße` (ab 0,0 s) → `Fall · Burkhard ohne Fahrerlaubnis` → `Fall · Rangieren aus der Einfahrt` → `Fall · Der Kratzer` → `Fall · Fahrerlaubnis` → `Fall · Die Frage` | Straße ab 0,0 s · Hiltrud vor ihrem Haus · Burkhard neben seinem Auto · „keine Fahrerlaubnis“ · Burkhard steigt ein, Auto rollt rückwärts · „verschätzt sich“ · streift · Kratzer · Burkhard steigt aus · Hiltrud redet · Burkhard redet · Fahrerlaubnis/Führerschein · 900 € · Frage | `szene_158kratzer_1` (Freesound CC0 482599) beim Streifen, `szene_158tuer_1` (Freesound CC0 778419) beim Aussteigen |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C § 823 Abs. 2 BGB** `norm`–`gleich` | **Wortlautkarte** (wörtlich vorgelesen), Marker „gleiche Verpflichtung“, „Schutz eines anderen“, „verstößt“, „ohne Verschulden“, „Falle des Verschuldens“; Rechtsfolgezeile, Verweis 067 | tabler:`book`, `alert-triangle`, `scale` | `Die Norm: § 823 Abs. 2 BGB › S. 1: Schutzgesetz` → `› S. 2: Verschulden` → `› Rechtsfolge wie Abs. 1` | Karte + 5 Marker, 2 Zeilen | – |
| **D Aufbau** `aufbau`–`a6` | sechs Farbblöcke I.–VI. | tabler:`list-check`, `book`, `license-off`, `alert-triangle`, `receipt-euro` | `Aufbau · sechs Schritte` → je Schritt | Block für Block | – |
| **E I. Schutzgesetz** `sg`–`reflex` | **Wortlautkarte Art. 2 EGBGB**, Zeile Verordnung, **Zitatkarte BGH-Formel** (VIa ZR 335/21 Rn. 20) mit Markern „zumindest auch“, „den Einzelnen“; Haken „Allgemeinheit schadet nicht“, Kreuz „bloßer Reflex“ | tabler:`book`, `file-text`, `user-check`, `users-group`, `users` | `I. Schutzgesetz` → `› jede Rechtsnorm, Art. 2 EGBGB` → `› zumindest auch Schutz des Einzelnen` → `› Allgemeinheit in erster Linie: unschädlich` → `› bloßer Reflex: kein Schutzgesetz` | Karte, Zeile, Karte + Marker, Haken, Kreuz | – |
| **F Klassiker** `klass`, `snt` | zwei Karten §§ 223, 263 StGB, Fundstellen; Block Schutznormtheorie, Verweis 110 | tabler:`gavel`, `building` | `I. Schutzgesetz › Klassiker: Strafgesetze` → `Abgrenzung · Schutznormtheorie (Öffentliches Recht)` | Karte für Karte | – |
| **G § 21 StVG** `p21`–`sgja` | **Wortlautkarten § 21 Abs. 1 Nr. 1 StVG** (Auszug) und **§ 2 Abs. 1 S. 1 StVG**, Zeilen Befähigung/Schutzzweck, grüner Block | tabler:`license-off`, `road`, `certificate`, `users-group`, `shield-check` | `I. Schutzgesetz › § 21 StVG` → `› § 2 StVG: öffentliche Straßen` → `› Befähigung geprüft` → `› Schutzzweck` → `› Schutzgesetz (+)` | Karten + Marker, Zeilen, Block | – |
| **H II. Schutzbereich** `sb`–`offen` | Karten „persönlich“ / „sachlich“ mit Haken, Fundstellen, Block zur offenen Schutzzweckfrage | tabler:`target`, `user-check`, `car`, `bulb` | `II. Schutzbereich` → `› persönlich` → `› sachlich` → `› Schutzzweck` | Zeile für Zeile | – |
| **I III./IV.** `verst`–`rw` | drei Haken Verstoß, Haken Indikation, Kreuz Rechtfertigung | tabler:`license-off`, `road`, `scale` | `III. Verstoß gegen § 21 StVG` → `IV. Rechtswidrigkeit` | Zeile für Zeile | – |
| **J V. Verschulden** `vs`–`vs5` | gelber Block Bezugspunkt, Zeilen, Haken Vorsatz, roter Block Satz 2 | tabler:`alert-triangle`, `gavel`, `bulb`, `book` | `V. Verschulden` → `› Bezugspunkt: der Verstoß` → `› subjektiver Tatbestand des Strafgesetzes` → `› Vorsatz (+)` → `› § 823 Abs. 2 S. 2 BGB` | Zeile für Zeile | – |
| **K VI. Schaden** `sd`, `rf` | Haken Schaden, Kausalität; Rechtsfolge, Block 900 € | tabler:`car`, `link`, `receipt-euro` | `VI. Schaden und Kausalität` → `VI. Schaden › Rechtsfolge, §§ 249 ff. BGB` | Zeile für Zeile | – |
| **L Vorteil** `vort`–`vt2` | zwei Karten Abs. 1 / Abs. 2, Block Betrug | tabler:`bulb`, `home`, `wallet` | `Vorteil · Warum Abs. 2?` → `› Abs. 1: kein Vermögensschutz als solcher` → `› Abs. 2: auch reiner Vermögensschaden` | Zeile für Zeile | – |
| **M Lösung** `loes`–`l3` | grüner Block 900 €, Haken § 823 Abs. 1, § 7 StVG, Verweis 149 | tabler:`gavel`, `coin-euro`, `home`, `car` | `Lösung · Hiltrud gegen Burkhard` → `› daneben § 823 Abs. 1 BGB` → `› daneben § 7 StVG` | Zeile für Zeile | – |
| **N Klausurtipp** `tipp`–`tp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · konkretes Schutzgesetz zitieren` → `· Schutzgesetz inzident prüfen` → `· öffentliche Straße?` | Zeile für Zeile | – |
| **O Prüfschema** `sch`–`c6` | breite Karte, I.–VI. mit Untermerkmalen | – | `Prüfschema` → je Gliederungspunkt | 7 Aufbaustufen | – |
| **P Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Sprechblasen Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („900 €“, „§ 823 Abs. 2 BGB“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegung: Burkhards Auto rollt rückwärts (≈ 4 s) bis zum Streifen.
**Geräusche:** zwei Handlungsgeräusche (leises Schaben, Autotür), Freesound CC0, Herkunft in `geraeusche_herkunft.json`. Kein Aufprallgeräusch.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Straße, Einfahrt, Pfeil und Kratzer aus Grundformen (`strasse()`, `kratzer()` in `folien_158.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> An einem Samstagmittag hat Hiltrud ihr Auto ordnungsgemäß am Straßenrand einer öffentlichen Wohnstraße vor ihrem Haus geparkt. Ihr Nachbar Burkhard will sein eigenes Auto umparken. Eine Fahrerlaubnis hat er nicht; die Prüfung hat er nie gemacht.
>
> Burkhard setzt rückwärts aus seiner Einfahrt auf die Straße, verschätzt sich beim Rangieren und streift das Auto von Hiltrud. Am hinteren Kotflügel bleibt ein langer Kratzer. Hiltrud ruft: „Burkhard, du hast doch gar keinen Führerschein!“ Burkhard antwortet: „Ich wollte doch nur kurz umparken.“
>
> Die Reparatur kostet 900 €. Hiltrud verlangt das Geld von Burkhard.
>
> **Hat Hiltrud einen Anspruch aus § 823 Abs. 2 BGB?**
