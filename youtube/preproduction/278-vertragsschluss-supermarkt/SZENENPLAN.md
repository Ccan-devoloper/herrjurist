# Folge 278 · Vertragsschluss Supermarkt: Wann kaufst du die Milch? – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_278.py`](src/skript_278.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · BGB AT · Streitstand. Aufbau nach Auftrag: Hook (Glasflasche rutscht im Gang aus der Hand) → Dialog Filialleiterin/Kunde → Frage → Sachverhalt → Anspruch § 433 Abs. 2 (Wortlautkarte), Anknüpfung an Folge 276 → **Streitstand** nach BGHZ 66, 51, Gründe V. 1: Ansicht 1 (Auslage = Angebot, Annahme durch Vorlegen) und Ansicht 2 (Auslage = Einladung, Angebot durch Vorlegen, Annahme durch Registrieren) nebeneinander, je ein Argument (§ 9 JuSchG) → Folge für die Flasche: nach beiden Ansichten erst an der Kasse, Streit offen, kein Kaufpreis → § 311 Abs. 2 Nr. 2 und § 241 Abs. 2 (Wortlautkarten), § 280 Abs. 1 (Wortlautkarte, vermutetes Vertretenmüssen), Fahrlässigkeit → § 823 Abs. 1 und Beweislast (Gemüseblatt-Fall, Gründe IV.) → Gegenrichtung: Schutzpflicht des Ladens (Gemüseblatt-Fall, Verweis 031) → Ergebnis → Klausurtipp (Lexi) → Prüfungsschema → Merksatz (Lexi). Hauptfilm 5:56,5 (5.347 vertonte Zeichen). Vorlagen: 276 (Werkzeuge, Hilfsfunktionen, Wortlautkarten; Voraussetzung, nicht wiederholt), 010/014/031 (nur verwiesen), 015 (Namens-/Sichtprüfung), Katzenkönig (Stil).

**Darstellung:** Supermarkt fiktiv, ohne Namen, Logo oder Marke (Schild nur „Milch“); Milchflaschen als Tabler-Icons; Scherben nur als Symbol (weiße Pfütze und kleines Kollisionszeichen), niemand verletzt; kein Fiktiv-Hinweis.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Erhard (EH), um 40 | Kunde, lässt die Flasche fallen | `standing/walking-1` (T-Shirt Grün `#8FD694`, Hose schwarz der Pose), Kopf `Short 5`, Haut `#E3B08C`, keine Brille, kein Bart. Mimiken `Calm`, `Concerned\|Serious` (redet/Sorge), `Smile`, `Fear` (Schreck), `Awe`, `Suspicious`, `Serious`, `Solemn`, `Smile Big\|Smile` (erleichtert) | `stephan` (Mann, mittel) |
| Frau Kesting (KE), um 30 | Filialleiterin | `standing/blazer-3` (Blazer Lila `#B8A9F5`, Oberteil schwarz der Pose, Hose Grau `#5A5F6E`), Kopf `Medium Bangs`, Haut `#C99470`, keine Brille. Mimiken `Calm`, `Serious` (redet/ernst), `Smile`, `Suspicious`, `Concerned\|Serious`, `Awe` | `lucy` (Frau, jung) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem Pool (stephan, hilde, christian, lucy): besetzt `stephan` und `lucy`; `hilde` und `christian` (Vorfolge 276) nicht besetzt, stephan und christian also nie gemeinsam.
- **Blickrichtung:** Beide Posen blicken im Original nach rechts (Gesicht); Grundansicht gespiegelt (nach links), `_r` nach rechts. Im Gang blickt Erhard zunächst zum Kühlregal (links), ab Frau Kestings Auftritt zu ihr (rechts); Frau Kesting blickt nach links zu ihm. Tafelszenen alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund** (auch `Concerned|Serious`, `Smile Big|Smile`); Mundzustände a/o/e nur in `EH_redet`, `KE_redet` (je links/rechts) und Lexi. 54 Figuren-PNGs in `../peeps/op_278/` (nicht im Repository, im Drive-Master).
- **Klischeeprüfung:** Filialleiterin sachlich (Blazer, keine Häme), Kunde freundlich-alltäglich; keine Prothesen-Posen, keine Polka Dots, keine Bärte; Frau Kesting ohne Dutt (Abgrenzung zu Lexi).
- **Namen:** Erhard, Kesting – eindeutig deutsche Aussprache, nicht in der Liste vergebener Namen; `grep -rliw` über `youtube/` (`*.py/*.md/*.json/*.csv/*.txt`): „Kesting“ ohne Treffer, „Erhard“ nur als verworfener Kandidat in 206 (nie verwendet). Eingetragen in `namen_reserviert.txt` („278: Erhard, Kesting“). Kein Genitiv eines Namens (Skript-Assertion). Gesprochen nur von der Erzählerin.

**Abweichung von den letzten Folgen (274–276):** Posen `walking-1`, `blazer-3` – dort nicht verwendet (274 `easing-2`/`resting-2`, 275 `shirt-3`/`robot_dance-2`, 276 `easing-2`/`pointing_finger-2`); keine Polka Dots; Farben Grün/Lila statt Rot/Schwarz (276) und Senf/Rot (275). Schauplatz **Gang im Supermarkt mit Kühlregal** – neu gegenüber 274 (Werkstatt/Behörde), 275 (Werkzeugwand, Kasse eines Baumarkts) und 276 (Schaufenster, Modegeschäft). Der Gang kehrt im Ergebnis zurück, weil dort die Flasche zerbrach. Cremegrund durchgehend.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A Im Gang** `fall`→`frage3` | ab 0,0 s Kühlregal (Schild „Milch“, drei Böden mit Milchflaschen, oben eine Lücke); Pille „Musst du sie bezahlen?“; Erhard mit Namensschild ab `erh`, „Dienstagabend“; Flasche in der Hand und Handy (`griff`), Pillen „Glasflasche Milch“, „eine Hand, Blick aufs Handy“; Flasche kippt in zwei Stufen (`rutsch`), Pille „beschlagen: rutscht“; Pfütze + Kollisionszeichen zum Wort „zerbricht“, Pillen „zerbrochen“, „niemand verletzt“; Frau Kesting mit Namensschild und Pille „Filialleiterin“ (`kest`); Blasen Kesting („Die Flasche müssen Sie bezahlen, 1,49 €.“), Erhard („Wieso? Gekauft habe ich sie doch noch gar nicht. An der Kasse war ich noch nicht.“); drei Frage-Pillen | tabler `bottle`, `device-mobile`; Fluent HC `collision` | `Fall · Im Supermarkt` → … (11 Stände) | Glasflasche zerbricht (`szene_278glas_1`, Freesound CC0 212698) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s | – | `Sachverhalt` | – |
| **C Anspruch** `ansp`→`kern` | „Markt gegen Erhard: 1,49 €“, **Wortlautkarte § 433 Abs. 2** (Marker „Kaufpreis zu zahlen“), Block Kaufvertrag + §§ 145 ff., Block Schaufenster → Folge 276, Block „Selbstbedienungsladen: umstritten“; beide | tabler `bottle`, `file-text`, `building-store`, `shopping-cart` | `Anspruch · …` (5 Stände) | – |
| **D Streitstand** `streit`→`jusch` | Fundstelle BGHZ 66, 51, Gründe V. 1; **Ansicht 1 und Ansicht 2 nebeneinander**, Zeilen zum Wort; „Dafür:“ je Argument; Block „Schnaps nicht an Jugendliche“ + § 9 Abs. 1 Nr. 2 JuSchG; Frau Kesting | Fluent HC `leafy-green`; tabler `shopping-cart`, `mail-opened`; Phosphor `cash-register`, `barcode`, `beer-bottle` | `Streit · …` (7 Stände) | – |
| **E Folge für die Flasche** `beide`→`aber` | Haken „nach beiden Ansichten: Vertrag erst an der Kasse“, Kreuz „Herausnehmen … bindet noch nicht“ + VIII ZR 171/10 Rn. 14 f., Kreuze „im Gang: noch kein Kaufvertrag“, „kein Anspruch auf den Kaufpreis“, Block „Aber: Haftung für die Scherben?“; Erhard | Phosphor `cash-register`; tabler `shopping-cart`, `bottle`; Fluent HC `collision` | `Die Flasche · …` (4 Stände) | – |
| **F1 § 311** `w311`, `anb` | **Wortlautkarte § 311 Abs. 2 Nr. 2** (Auszug, Marker „Anbahnung“, „Einwirkung“), Haken „Der Markt lässt Erhard die Ware selbst in die Hand nehmen.“; Erhard | tabler `building-store`, `bottle` | `II. culpa in contrahendo · …` | – |
| **F2 § 241** `w241`→`v010` | **Wortlautkarte § 241 Abs. 2** (Marker „jeden Teil“, „Rücksicht“), Haken „auch der Kunde …“, „die Milch gehört noch dem Markt“, Block Folge 010; Frau Kesting | tabler `hand-stop`, `bottle`, `book` | (3 Stände) | – |
| **F3 § 280** `w280`→`anders` | **Wortlautkarte § 280 Abs. 1** (Marker „Pflicht“, „nicht zu“), Haken „Vertretenmüssen vermutet …“, „fahrlässig …“ + § 276 Abs. 2, Block „angerempelt? …“; Erhard | tabler `receipt`, `device-mobile`, `users`; Phosphor `scales` | (4 Stände) | – |
| **F4 Delikt** `d823`, `beweis` | Haken § 823 Abs. 1, Vergleich c. i. c./Delikt (Beweislast), Block Beweisvorteil Gemüseblatt-Fall + Gründe IV.; Frau Kesting | tabler `bottle`; Phosphor `scales` | `III. Delikt · …` | – |
| **G Gegenrichtung** `gegen`→`v031` | „Die Rücksichtspflicht gilt auch umgekehrt.“, Gemüseblatt-Fall (Kassenzone), Haken „Laden haftet aus c. i. c.“, „obwohl …“ + Gründe V. 1, V. 4, Block Folge 031; Frau Kesting | tabler `arrows-exchange`, `building-store`, `book`; Fluent HC `leafy-green` | `Gegenrichtung · …` (4 Stände) | – |
| **H Ergebnis** `erg`→`erg3` | Gang wie A mit Pfütze; Kreuz „kein Kaufpreis …“, Haken „Schadensersatz …“ + Normen, Block „nicht als Käufer, sondern als Schädiger“; beide blicken einander an | wie A | `Ergebnis · …` (3 Stände) | – |
| **I Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (3 Stände) | – |
| **L Prüfungsschema** `sch`→`s3` | breite Karte, 10 Zeilen zum Wort | – | `Prüfungsschema` → je Gliederungspunkt | – |
| **M Merksatz** `merke`, `merk2` | Lexi erklärt (redet), zwei Sätze mit Markern | – | `Merksatz` | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), jeweils über der sprechenden Figur. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern.
**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** ein Handlungsgeräusch (zerbrechende Glasflasche zum Wort „zerbricht“, wenn Pfütze und Kollisionszeichen erscheinen). Freesound-API am 08.10.2026 über den Proxy erreichbar; Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Phosphor Icons (MIT), Fluent Emoji High Contrast (MIT: collision, leafy-green, Haken/Kreuz), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Kühlregal, Pfütze und Boden programmatisch.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Erhard nimmt am Dienstagabend im Supermarkt eine kalte Glasflasche Milch aus dem Kühlregal. Er hält sie mit einer Hand und schaut dabei auf die Einkaufsliste in seinem Handy. Die beschlagene Flasche rutscht ihm durch die Finger und zerbricht auf dem Boden. Verletzt wird niemand.
>
> Frau Kesting, die Filialleiterin, verlangt für den Markt 1,49 €. Erhard meint, er habe die Milch noch gar nicht gekauft; an der Kasse sei er noch nicht gewesen.
>
> **Kann der Markt von Erhard Geld verlangen?**
