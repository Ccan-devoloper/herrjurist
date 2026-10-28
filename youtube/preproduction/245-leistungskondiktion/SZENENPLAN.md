# Folge 245 · Leistungskondiktion § 812 I 1 Alt. 1 BGB – Prüfungsschema – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_245.py`](src/skript_245.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Bereicherungsrecht · Schema. Aufbau nach Auftrag: Hook am nichtigen Klavierkauf (Zahlen als Ziffern: 2.400 €, 4.200 €) → Rückblick (Angebot, Zusage, Barzahlung, Einzahlung) → Frage → Sachverhalt → I. Anspruchsgrundlage (Wortlautkarte § 812 Abs. 1 Satz 1 BGB, condictio indebiti, Schema mit vier Punkten) → II. 1. etwas erlangt (vermögenswerter Vorteil; Eigentum/Besitz an den Scheinen; Gutschrift) → 2. durch Leistung (bewusst und zweckgerichtet, Empfängerhorizont) → 3. ohne rechtlichen Grund (Erklärungsirrtum, Anfechtung, § 142 Abs. 1) → 4. kein Ausschluss (Wortlautkarten § 814, § 817 Satz 2) → III. Rechtsfolge (Wortlautkarte § 818 Abs. 1, 2; Abs. 3 ein Satz) → IV. Saldotheorie (Zug um Zug) → Abgrenzung condictio ob rem → Ergebnis → Klausurtipp (Lexi, Vorrang) → Prüfungsschema → Merksatz (Lexi). Hauptfilm 5:50,7 (5.051 vertonte Zeichen). Vorlagen: 229 (Werkzeuge, Hilfsfunktionen, Wortlautkarten), 073 (Überblick, nur verwiesen), 015 (Namens-/Sichtprüfung), Katzenkönig (Stil).

**Darstellung:** Personen fiktiv; keine echte Instrumentenmarke (Klavier aus Grundformen, ohne Schriftzug); Nachricht auf einem gezeichneten Smartphone ohne App- oder Herstellerkennzeichen; kein Fiktiv-Hinweis.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Mila (MI), um 25 | Käuferin, Anspruchstellerin | `standing/shirt-4` (schwarzes Hemd der Pose, Hose Türkis `#7FD6D0`), Kopf `Medium 2`, Haut `#E8B48C`, keine Brille, kein Bart. Mimiken `Calm`, `Serious` (redet/ernst), `Concerned\|Serious` (sorgt/sorge), `Smile`, `Awe`, `Suspicious`, `Smile Big\|Smile` | `lucy` (Frau, jung) |
| Frau Heidkamp (HK), um 70 | Verkäuferin, ficht an | `standing/shirt-3` (Bluse Lila `#B8A9F5`, Hose Dunkelgrau `#4A4A55`), Kopf `Gray Bun`, Brille `Glasses 2`, Haut `#EFC6A4`. Mimiken `Calm`, `Concerned\|Serious` (redet, entschuldigend), `Serious` (fest/ernst), `Smile`, `Suspicious`, `Driven` (tippt) | `hilde` (Frau, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem Pool (stephan, hilde, christian, lucy): besetzt `lucy` und `hilde`; `stephan` und `christian` nicht besetzt (also nie zusammen in einer Szene).
- **Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. A1/A3/Ergebnis: Mila (links, `_r`) und Frau Heidkamp (an der Tür rechts, Grundansicht) blicken einander an; zu Beginn blickt Mila zum Klavier (links). A2: Frau Heidkamp (`_r`) zum Handy bzw. zu Mila, Mila (Grundansicht) zu ihr. Tafelszenen alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund** (auch `Concerned|Serious`, `Smile Big|Smile`); Mundzustände a/o/e nur in `MI_redet`, `MI_sorgt`, `HK_redet`, `HK_fest` (je links/rechts) und Lexi. 66 Figuren-PNGs in `../peeps/op_245/` (nicht im Repository, im Drive-Master).
- **Klischeeprüfung:** Frau Heidkamp sachlich-freundlich (keine „geizige Alte“), Mila ohne Übertreibung; keine Prothesen-Posen (`shirt-2` verworfen), keine Polka Dots, keine Bärte; keine Zuordnung von Herkunft oder Hautfarbe zu einer Rolle.
- **Namen:** Mila, Heidkamp – eindeutig deutsche Aussprache (Mila gleich in beiden Sprachen; Heidkamp mit stimmlosem d vor k), nicht in der Liste vergebener Namen, per `grep -rliw` in keiner `*.py/*.md/*.json/*.csv/*.txt` unter `youtube/` (verworfen: Greta – Folge 003, Lotta – in 173 genannt, Henrike – mehrfach im Repo), in `namen_reserviert.txt` als „245: Mila, Heidkamp“ eingetragen. Gesprochen nur von der Erzählerin: „Mila“ 11×, „Frau Heidkamp“ 9×.

**Abweichung von den letzten drei Folgen (242–244):** Posen `shirt-4`, `shirt-3` – in 242 (`walking-2`, `blazer-3`, `pointing_finger-2`), 243 (`blazer-3`, `walking-2`, `blazer-2`, `pointing_finger-1`, `walking-3`, `robot_dance-2`, `shirt-1`) und 244 (`robot_dance-3`, `crossed_arms-1`, `resting-1`, `robot_dance-2`, `polka_dots`, `walking-3`) nicht verwendet; keine Polka Dots. Schauplätze **Wohnzimmer bei Mila** (Fenster, Sessel, Klavier, Tür) und **Wohnstube bei Frau Heidkamp** (Klavier, Bild, Pflanze, Smartphone-Nachricht) – neu gegenüber 242 (Notar, Straße), 243, 244; Folge 012 hatte zuletzt ein Klavier (Rollen beim Abholen), hier ein anderer Raum und Fall. Das Wohnzimmer kehrt in A3 und im Ergebnis zurück, weil die Geschichte dorthin zurückkehrt. Tageslicht-Cremegrund durchgehend.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Wohnzimmer** `fall`→`m1` | ab 0,0 s Fenster, Sessel, Klavier, Tür, Mila mit Namensschild; Pille „seit einer Woche“ zu `klavier`; Frau Heidkamp an der Tür, Klingelsymbol zu „klingelt“; Blasen Heidkamp, Mila | Klavier, Fenster, Tür aus Grundformen (`klavier()`, `fenster()`, `tuer()`); tabler `armchair`, `bell-ringing` | `Fall · Bei Mila im Wohnzimmer` → `· Frau Heidkamp klingelt` → `· „Vertippt: 4.200 € statt 2.400 €“` → `· Mila hat schon bezahlt` | Türklingel (`szene_245klingel_1`, Freesound CC0 157250) |
| **A2 Rückblick bei Frau Heidkamp** `rueck`→`konto` | Frau Heidkamp mit Handy in der Hand, Smartphone-Karte „Sie können das Klavier für 2.400 € haben.“, Haken „Mila sagt sofort zu“, Mila tritt auf, Geldscheine + „2.400 € bar“ zum Wort „bar“, Einzahlung: Scheine → Bank, „auf ihr Konto eingezahlt“ | Klavier (Grundformen), Smartphone (Grundformen); tabler `photo`, `plant-2`, `device-mobile`, `cash-banknote`, `building-bank` | `Rückblick · Zwei Wochen vorher bei Frau Heidkamp` → `· Das Angebot: 2.400 €` → `· Mila sagt sofort zu` → `· Mila zahlt bar` → `· Die Scheine kommen aufs Konto` | Geldscheine (`szene_245scheine_1`, Freesound CC0 447458) |
| **A3 Wohnzimmer** `mi2`→`frage2` | Blasen Mila („Dann will ich meine 2.400 € zurück.“), Heidkamp („… wenn ich mein Klavier wiederbekomme.“); Pillen Frage | wie A1 | `Fall · Mila will ihr Geld zurück` → `· Frau Heidkamp will ihr Klavier` → `Die Frage · Geld zurück trotz nichtigem Kauf?` → `Die Frage · Und das Klavier?` | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,3 s | – | `Sachverhalt` | – |
| **C I. Anspruchsgrundlage** `norm`→`schema` | Zeile „§ 812 Abs. 1 Satz 1 Alt. 1 BGB: Leistungskondiktion“, „genauer: condictio indebiti“ + Fundstelle zum Wort, **Wortlautkarte § 812 Abs. 1 Satz 1** (Marker „durch die Leistung eines anderen“, „etwas“, „ohne rechtlichen Grund“, „erlangt“), Schema-Block mit vier Punkten zum Wort; Mila, Heidkamp | tabler `scale`, `list-check` | `I. Anspruchsgrundlage · § 812 Abs. 1 Satz 1 Alt. 1 BGB` → `› Wortlaut` → `› Schema: vier Prüfungspunkte` | – |
| **D 1. Etwas erlangt** `erl`→`gutschr` | Haken „jeder vermögenswerte Vorteil“, „Eigentum und Besitz an den Scheinen“, Blöcke Übereignung nicht angefochten, Gutschrift; Heidkamp | tabler `help-circle`, `cash-banknote`, `building-bank` | `II. Voraussetzungen › 1. …` (5 Stände) | – |
| **E 2. Durch Leistung** `leist`→`horiz` | Block Leistungsbegriff, Fundstellen, Haken bewusst/zweckgerichtet (§ 433 Abs. 2), Block Empfängersicht, „hier: Zweck eindeutig“; Mila | tabler `cash-banknote-move`, `target-arrow`, `eye` | `› 2. …` (5 Stände) | – |
| **F 3. Ohne rechtlichen Grund** `org`→`alt1` | Kaufvertrag, Erklärungsirrtum („vertippt, 2.400 € statt 4.200 €“), Anfechtung §§ 121, 143, roter Block § 142 Abs. 1, grüner Block „Rückwirkung: Satz 1, 1. Alternative“ + BGH; Heidkamp | tabler `file-text`, `keyboard`, `file-x` | `› 3. …` (6 Stände) | – |
| **G1 4. Kein Ausschluss: § 814** `aus`→`k814` | **Wortlautkarte § 814** (Marker „gewusst hat“, „nicht verpflichtet“), „positive Kenntnis der Rechtslage“, Kreuz „Mila wusste … nichts“ zum Wort; Mila | tabler `ban`, `help-circle` | `› 4. …` (3 Stände) | – |
| **G2 4. Kein Ausschluss: § 817 Satz 2** `w817`→`tbm` | **Wortlautkarte § 817 Satz 2** (Marker „Rückforderung ist ausgeschlossen“, „dem Leistenden“, „Verstoß“), Erläuterung, Kreuz Klavierkauf, grüner Block 1.–4. (+); Mila | tabler `ban`, `circle-check` | `› 4. § 817 Satz 2 BGB` → `› 4. kein Gesetzes- oder Sittenverstoß` → `› Voraussetzungen (+)` | – |
| **H III. Rechtsfolge** `rf`→`entr` | „Herausgabe des Erlangten“, **Wortlautkarte § 818 Abs. 1, 2** (Marker „Nutzungen“, „außerstande“, „Wert“), Kreuz „Scheine: nicht mehr da“, Block „Wertersatz: 2.400 €“, Haken keine Entreicherung + BGH; Heidkamp | tabler `arrow-back-up`, `building-bank`, `coin-euro` | `III. Rechtsfolge · Herausgabe` → … (6 Stände) | – |
| **I IV. Saldotheorie** `gegen`→`saldo` | Haken „auch Mila hat erlangt: das Klavier …“, Block Saldotheorie, Mini-Klavier ⇄ Geldscheine, grüner Block Zug um Zug + BGH; Mila, Heidkamp | Klavier (Grundformen); tabler `arrows-exchange`, `cash-banknote`, `piano`, `scale` | `IV. Saldotheorie · …` (3 Stände) | – |
| **J Abgrenzung** `orem`, `orem2` | § 812 Abs. 1 Satz 2 Alt. 2, Block Zweckeinigung + BGH, Kreuz „hier nicht: Mila zahlte auf eine Kaufpreisschuld“; Mila | tabler `target`, `file-text` | `Abgrenzung · condictio ob rem, …` → `› hier nicht` | – |
| **K Ergebnis (Wohnzimmer)** `erg`, `erg2` | Schauplatz A1; Haken „2.400 € an Mila, § 812 …“, „Zug um Zug gegen Rückgabe und Rückübereignung des Klaviers“; Geldscheine und Tauschpfeile zwischen den Figuren; beide froh | tabler `cash-banknote`, `arrows-exchange` | `Ergebnis · 2.400 € für Mila` → `› Zug um Zug gegen das Klavier` | – |
| **L Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (2 Stände) | – |
| **M Prüfungsschema** `sch`→`s5` | breite Karte, 10 Zeilen zum Wort | – | `Prüfungsschema` → je Gliederungspunkt | – |
| **N Merksatz** `merke`, `merk2` | Lexi erklärt (redet), zwei Sätze mit Markern | – | `Merksatz` | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen). **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern.
**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** zwei Handlungsgeräusche (Türklingel, Geldscheine); Freesound-API am 07.10.2026 gesperrt (HTTP 403), deshalb bitgleiche Kopien vorhandener CC0-Dateien aus `sfx3` unter eigenem Namen, Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Klavier, Fenster, Tür, Smartphone programmatisch.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Frau Heidkamp schreibt Mila: „Sie können das Klavier für 2.400 € haben.“ Gemeint hatte sie 4.200 €; sie hat sich vertippt. Mila sagt sofort zu.
>
> Beim Abholen zahlt Mila 2.400 € bar. Frau Heidkamp zahlt die Scheine noch am selben Tag auf ihr Konto ein. Von dem Tippfehler weiß Mila nichts.
>
> Eine Woche später bemerkt Frau Heidkamp den Fehler und ficht ihre Erklärung sofort gegenüber Mila an. Mila verlangt ihre 2.400 € zurück; Frau Heidkamp will dafür ihr Klavier wiederhaben.
>
> **Kann Mila ihr Geld zurückverlangen, und muss sie dafür das Klavier hergeben?**
