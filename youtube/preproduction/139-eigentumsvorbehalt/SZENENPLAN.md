# Folge 139 · Eigentumsvorbehalt: Das Sofa ist da, gehört aber dem Möbelhaus – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_139.py`](src/skript_139.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/Sachenrecht, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Das auf Raten gekaufte Sofa steht in deinem Wohnzimmer – der Kaufvertrag sagt: Eigentum bleibt beim Händler.“): Sonja kauft im Möbelhaus bei Verkäufer Herrn Schuster ein Sofa für 2.400 €, 12 Monatsraten zu je 200 €, mit Eigentumsvorbehalt bis zur letzten Rate. Das Sofa wird geliefert. Nach fünf Raten (1.000 €) zahlt Sonja nicht mehr; Herr Schuster kündigt am Telefon die Abholung an. Eine Frist hat das Möbelhaus nicht gesetzt.

Ablauf: Fall (Möbelhaus, Lieferung, Anruf) → Frage → Sachverhalt → Aufbau (drei Schritte) → 1. Trennungsprinzip (Kaufvertrag § 433 unbedingt, Übereignung § 929 S. 1 aufschiebend bedingt) → Wortlautkarte § 449 Abs. 1 → Wortlautkarte § 158 Abs. 1 mit Ratenleiste (5 von 12 Raten) → 2. Anwartschaftsrecht (BGH V ZR 143/24 Rn. 16) → 3. Herausgabe: Wortlautkarte § 985, § 986 Abs. 1 (Besitzrecht aus dem Kaufvertrag, IX ZR 128/12 Rn. 11) → Wortlautkarte § 449 Abs. 2 → Rücktritt § 323 (Verweis 116), Teilzahlungsgeschäft §§ 506, 508 offen, Rückabwicklung §§ 346 ff. → Ergebnis (mit Sofa) → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm ≈ 5:55 (5.164 Zeichen); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Sonja, um 30 | Käuferin, Vorbehaltskäuferin, Besitzerin | `standing/robot_dance-3` (rotes Oberteil `#F07A6A`, schwarze Hose, weiße Turnschuhe; geöffnete Hand), Kopf `Long Bangs` (schwarz), Haut `#F2C9A5`; Mimiken `Calm`, `Smile`, `Smile Big|Smile` (redet froh), `Concerned|Serious` (redet empört, Sorge), `Suspicious`, `Awe` | `ela_froh` (Frau, jung) |
| Herr Schuster, um 60 | Verkäufer im Möbelhaus (handelt für das Möbelhaus) | `standing/pointing_finger-2` (schwarzes Oberteil, Hose Graublau `#5B6B8C`, schwarze Stiefel; erhobener Zeigefinger zur Vorbehaltsklausel), Kopf `Gray Short`, Brille `Glasses`, Haut `#EDC3A3`, kein Bart; Mimiken `Calm`, `Smile` (redet), `Serious` (redet streng, ernst), `Suspicious`, `Concerned|Serious` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge vergeben (geprüft per `grep -rlw` über alle `.py/.md/.json` in `youtube/`: 0 Treffer, und gegen die Koordinatorliste): Sonja, Schuster. Im Sprechtext kein Genitiv eines Namens („in ihrem Wohnzimmer“, „Rechtsposition von Sonja“ nur auf der Tafel).
- **Stimmen nur aus dem Pool** niklas, helmut, ela_froh, julia: `ela_froh` (Sonja) und `helmut` (Herr Schuster). julia und niklas liefen in 135 – hier nicht eingesetzt, also andere Rollenverteilung. Erzählerin/Lexi Carla ohne Rolle.
- Präfixe `SO_`/`SC_` (nie `ER_`). Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Im Möbelhaus blickt Sonja nach rechts zu Herrn Schuster, er nach links zu ihr; im Wohnzimmer blickt Sonja nach links zum Sofa; beim Anruf blickt Herr Schuster (links) nach rechts, Sonja (rechts) nach links; in den Tafelszenen blicken beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `SO_redet`, `SO_empoert`, `SC_redet`, `SC_streng` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur, kein Klischee (der Verkäufer bleibt sachlich). **Keine weiteren Menschen im Bild** (die Lieferung zeigt nur einen Lieferwagen).
- **Abwechslung:** Posen nicht aus 135 (`blazer-4`, `crossed_arms-2`), 136 (`blazer-3`, `robot_dance-2`, `pointing_finger-1`), 137 (`easing-2`, `shirt-3`, `resting-2`); keine Polka Dots. Figurenrezepte und Kontaktbögen verglichen.
- Figuren-PNGs: `../peeps/op_139/` (62 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 137 (Schule, Entschuldigungszettel), 136 (brennende Mülltonne, Nachbarschaft), 135 (Lerngruppe, EU). Hier neu: Möbelhaus mit Ausstellungssofa und Preisschild, Sonjas Wohnzimmer (blaues Sofa, Lampe, Pflanze, Bild), geteilte Bühne beim Anruf (Möbelhaus links, Wohnzimmer rechts). Leitmotiv: das **blaue Sofa** (Tabler `sofa`) in Fall, Requisiten und Ergebnis; **Ratenleiste** mit 5 von 12 grünen Feldern. 080 (Übereignung) hatte eine geteilte Nachtbühne; hier eine Tagesbühne mit Telefon. Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Im Möbelhaus** `fall`–`sc1` | ab 0,0 s Ausstellungssofa, Lampe, Sonja mit Namensschild; Preisschild und „Sofa: 2.400 €“ bei „Sofa“, „12 Monatsraten zu je 200 €“ bei „zwölf“, Herr Schuster bei „Verkäufer“, „Kaufvertrag“ bei „Satz“; Blase Schuster „Bis zur letzten Rate bleibt das Sofa / Eigentum des Möbelhauses.“ | tabler:`sofa` (Blau), `lamp` (Gelb), `tag`, `calendar-dollar`, `contract` | `Fall · Im Möbelhaus` → `Fall · Der Kaufvertrag` | – |
| **A2 Die Lieferung** `liefer`–`so1` | Wohnzimmer; Lieferwagen und „geliefert“ bei „geliefert“, „Wohnzimmer“; Blase Sonja „Endlich ein eigenes Sofa!“ | tabler:`sofa`, `lamp`, `plant-2` (Grün), `photo`, `truck-delivery` | `Fall · Die Lieferung` | – |
| **A3 Raten / Anruf / Frage** `fuenf`–`frage2` | geteilte Bühne; „5 Raten gezahlt: 1.000 €“ + Münzen, „dann: keine Zahlung mehr“ + Kalender; Möbelhaus, Herr Schuster und klingelndes Telefon bei „ruft“; Blase Schuster „Das Sofa gehört noch uns. / Wir holen es am Montag ab.“; Blase Sonja „Aber ich habe das Sofa / doch gekauft!“; Fragepillen | tabler:`coins`, `calendar-x`, `building-store` (Gelb), `phone-ringing`, `phone-call`, `sofa`, `photo` | `Fall · Die Raten` → `Fall · Der Anruf` → `Fall · Die Frage` | `szene_139telefon_1` bei „ruft“ |
| **B Sachverhalt** `sv` | Karte vollständig (38 px), ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Aufbau** `plan`–`s3` | 1. Konstruktion / 2. Rechtsposition von Sonja / 3. Herausgabe des Sofas? zum Wort | tabler:`list-numbers`, `link`, `key`, `sofa` | `Eigentumsvorbehalt › Aufbau` | – |
| **D 1. Trennungsprinzip** `tr1`–`ueb2` | „zwei verschiedene Geschäfte“; grüne Box Kaufvertrag § 433 unbedingt (✓ liefern und übereignen, ✓ zahlen); Box Übereignung § 929 S. 1 „aufschiebend bedingt“ (✓ Einigung und Übergabe mit der Lieferung, ✗ Wirkung noch nicht; IX ZR 128/12 Rn. 10) | tabler:`link`, `arrows-split-2`, `contract`, `sofa`, `lock`, `truck-delivery` | `1. Trennungsprinzip` → `› Kaufvertrag, § 433 BGB` → `› Übereignung, § 929 S. 1 BGB` | – |
| **E § 449 Abs. 1** `w449` | Wortlautkarte, 3 Marker; Block „Übereignung unter aufschiebender Bedingung“ | tabler:`contract`, `lock` | `1. Konstruktion › § 449 Abs. 1 BGB` | – |
| **F § 158 Abs. 1** `w158`–`eig1` | Wortlautkarte, 2 Marker; Ratenleiste 12 Felder, 5 grün bei „Gezahlt“; „Bedingung: vollständige Zahlung, 2.400 €“, ✗ „gezahlt: erst 1.000 €“, Block „Eigentümer: noch das Möbelhaus“ | tabler:`hourglass`, `coin-euro`, `coins`, `building-store` | `1. Konstruktion › § 158 Abs. 1 BGB` → `› Bedingung: vollständige Zahlung` | – |
| **G 2. Anwartschaftsrecht** `anw`–`anw4` | ✓ Anwartschaftsrecht; Definition (V ZR 143/24 Rn. 16); „ein dem Volleigentum wesensähnliches Recht“; ✓ „Rest gezahlt: Sonja wird Eigentümerin, ob das Möbelhaus will oder nicht“ | tabler:`key`, `shield-lock`, `sofa` | `2. Anwartschaftsrecht` | – |
| **H 3. Herausgabe** `her`–`h4` | Wortlautkarte § 985 (3 Marker); ✓ Eigentümer Möbelhaus, ✓ Besitzerin Sonja; „Recht zum Besitz? § 986 Abs. 1 BGB“; ✓ „aus dem Kaufvertrag, bis zum wirksamen Rücktritt“ (vgl. IX ZR 128/12 Rn. 11) | tabler:`hand-grab`, `building-store`, `sofa`, `shield-check`, `contract` | `3. Herausgabe › § 985 BGB` → `› Recht zum Besitz, § 986 Abs. 1 BGB` | – |
| **I § 449 Abs. 2** `w4492`–`nurev` | Wortlautkarte (3 Marker), Block „Der Vorbehalt allein genügt nicht.“ | tabler:`arrow-back-up`, `lock` (Rot) | `3. Herausgabe › § 449 Abs. 2 BGB` | – |
| **J Rücktritt** `rt1`–`rg` | § 323 Abs. 1, Frist zur Zahlung, Block „Mehr dazu: Video „Rücktritt““; „entgeltliches Teilzahlungsgeschäft? offen“, § 508; §§ 346 ff.: Sofa zurück, Wertersatz, 1.000 € zurück | tabler:`arrow-back-up`, `hourglass`, `calendar-dollar`, `arrows-exchange`, `sofa`, `coins` | `Rücktritt › § 323 Abs. 1 BGB` → `› Teilzahlungsgeschäft?` → `Rückabwicklung › §§ 346 ff. BGB` | – |
| **K Ergebnis** `erg`–`erg5` | Tafel mit Haken/Kreuzen zum Wort; rechts Sonja neben dem Sofa, Pillen „Sofa bleibt vorerst bei Sonja“ → „erst nach Rücktritt: zurück“; Block „erst nach wirksamem Rücktritt: Herausgabe, §§ 985, 346 Abs. 1 BGB“ (IX ZR 110/17 Rn. 65) | tabler:`sofa` | `Ergebnis` → `Ergebnis › nach wirksamem Rücktritt` | – |
| **L Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt; letzte Rate → Eigentum automatisch (§ 158 Abs. 1); 2 Begriffe verlängerter / erweiterter Eigentumsvorbehalt | Warnsymbol (Streamline Freehand) | `Klausurtipp · letzte Rate` → `Klausurtipp · Begriffe` | – |
| **M Klausurschema** `sch`–`k4` | breite Karte, I. Eigentum (1. bedingt, 2. nicht eingetreten/Anwartschaftsrecht), II. Besitz, III. kein Recht zum Besitz (1. Kaufvertrag, 2. endet erst mit wirksamem Rücktritt), daneben Rückgewähr § 346 Abs. 1 | – | `Klausurschema` → `› I. Eigentum` → `› II. Besitz` → `› III. kein Recht zum Besitz` → `› Rückgewähr` | – |
| **N Merksatz** `merke`–`mk3` | Lexi erklärt, vier Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; keine Bewegungsanimation, kein Zoom.
**Blasen:** Stil C (`bausteine.blase`, stiller Rückfall per Assertion ausgeschlossen), wortgleich mit dem Gesprochenen. Zahlen auf Tafeln, Pillen und Karte als Ziffern.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Sonja kauft in einem Möbelhaus beim Verkäufer Herrn Schuster ein Sofa für 2.400 Euro, zahlbar in 12 Monatsraten zu je 200 Euro. Im Kaufvertrag steht: „Bis zur letzten Rate bleibt das Sofa Eigentum des Möbelhauses.“
>
> Das Sofa wird geliefert und steht in Sonjas Wohnzimmer. Sonja zahlt fünf Raten pünktlich, zusammen 1.000 Euro. Danach zahlt sie nicht mehr.
>
> Herr Schuster ruft an: Das Sofa gehöre noch dem Möbelhaus, man werde es am Montag abholen. Eine Frist zur Zahlung hat das Möbelhaus Sonja nicht gesetzt.
>
> **Wer ist Eigentümer des Sofas – und darf das Möbelhaus es einfach abholen?**
