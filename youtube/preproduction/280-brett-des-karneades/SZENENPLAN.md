# Folge 280 · Entschuldigender Notstand § 35: Das Brett des Karneades – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_280.py`](src/skript_280.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · StGB AT, Format **Klassiker-Fall**. Plan-Hook: Nach einem Bootsunglück stößt ein Schiffbrüchiger einen anderen von einer Planke, die nur einen tragen kann. Ausgestaltung: Herr Tamm, Fahrgast eines im Sturm gesunkenen Ausflugsboots, sagt im Hafenbüro der Wasserschutzpolizei bei Kommissarin Petzold aus.
Ablauf (laut Auftrag): 1. Hook (Hafenbüro → Symbolbild See → Hafenbüro, Frage, Brett des Karneades als antikes Gedankenexperiment) → Sachverhalt → 2. Tatbestand § 212 und Rechtswidrigkeit (§ 34 in einem Satz, Verweis 263) → 3. § 35 Abs. 1 S. 1 (Wortlautkarte): Gefahr für Leben, gegenwärtig, nicht anders abwendbar, eigene Person, Rettungswille → 4. § 35 Abs. 1 S. 2 (Wortlautkarte): Hinnahmepflicht – Gefahr selbst verursacht, besonderes Rechtsverhältnis; Abwandlung 1 Kapitän → keine Entschuldigung → 5. § 35 Abs. 2 (Wortlautkarte): Abwandlung 2 Irrtum, Vermeidbarkeit (BGHSt 48, 255 Rn. 35; Verweis 007) → 6. Ergebnis, Blase Petzold → 7. Klausurtipp (Lexi), Schema, Merksatz (Lexi).
**Abgrenzung zu den Referenzfolgen:** 263 (§ 34 scheitert bei Leben gegen Leben, § 35-Personenkreis, übergesetzlicher Notstand) und 189 (§ 34-Schema) werden nicht wiederholt; § 34 steht in einem Satz mit Verweis auf 263. 007 (Haustyrann) nur als Quelle der Vermeidbarkeitsformel und Verweis.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Tamm (TA), Mitte 40 | Fahrgast, Überlebender, Täter im Ausgangsfall | `standing/resting-1` (Pullover Orange `#F9A66C`, schwarze Hose der Pose), Kopf `Short 3` (dunkles Haar), Haut `#E8B994`; Mimiken `Calm`, `Serious`, `Concerned\|Serious`, `Fear`, `Tired`, `Solemn`, `Eyes Closed`, `Suspicious`, `Smile`; redet: `Concerned\|Serious`, redet2: `Tired` | `marc` (Mann, mittel) |
| Kommissarin Petzold (PE), um 35 | Wasserschutzpolizei, nimmt die Aussage auf | `standing/shirt-3` (hellblaues Hemd `#8DB3F2` ohne Abzeichen, schwarze Hose der Pose), Kopf `Medium Straight` (schwarzes Haar), Haut `#EBC2A0`; Mimiken `Calm`, `Serious`, `Suspicious`, `Smile`; redet: `Serious`; blickt im Hafenbüro nach rechts zu Herrn Tamm | `sabrina` (Frau, mittel) |
| Kapitän (KA), um 60, namenlos | nur Abwandlung 1, steht neben der Tafel, spricht nicht | `standing/resting-2` (schwarzes Oberteil der Pose, Hose Marine `#3E4A6B`), Kopf `Gray Short`, Haut `#D9A57E`, kein Bart; Mimiken `Serious`, `Solemn`, `Suspicious`, `Tired` | – |
| Der andere Schiffbrüchige, der Fahrgast der Abwandlung | – | **nicht dargestellt** (nur im Text) | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen, nicht in `namen_reserviert.txt` (eingetragen „280: Tamm, Petzold“ vor der Vertonung) und in keiner versionierten Datei unter `youtube/` (`git grep -w`, 08.10.2026).
- **Stimmen** nur aus dem Pool (william, sabrina, marc, laura_ruhig); `william` und `laura_ruhig` nicht gebraucht (der Kapitän spricht nicht).
- **Posen** nicht aus 277–279 (blazer-2, easing-1, walking-1, blazer-3, robot_dance-3, sitting/mid-2, blazer-4); keine Polka Dots, keine Prothesen-Posen, keine Bärte, keine Karikatur. Alle Grundmimiken mit geschlossenem Mund; Mundzustände a/o/e für `TA_redet`, `TA_redet2`, `PE_redet` (je links/rechts) und Lexi. 66 Figuren-PNGs in `../peeps/op_280/`.
- **Blickrichtung:** Herr Tamm und der Kapitän blicken nach links (zu Petzold bzw. zur Tafel), Petzold im Hafenbüro nach rechts zu Herrn Tamm.

**Setting (neu):** Hafenbüro der Wasserschutzpolizei (graublaue Wand, Fenster mit Blick auf das Hafenbecken, Stehpult mit Klemmbrett und Stift) und ein Symbolbild der See (Wasserfläche mit Wellenlinien, Sturmwolke, Holzplanke, Kutter-Icon) ohne Menschen. Gegenüber 277 (Bauamt/Innenbereich), 278 (Supermarkt), 279 (E-Examen) neu. Cremegrund durchgehend, Tageslicht.
**Darstellung (Auftrag):** kein Ertrinken, kein Stoß, keine Leiche im Bild. Der Vorgang steht nur als Text auf Pillen („Herr Tamm stößt den anderen weg.“, „Der andere kommt ums Leben.“); die Planke wird beim Untergehen tiefer und blasser ins Wasser gesetzt. Figuren nur an Land.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Hafenbüro** `fall`→`ta1` | Raum mit Fenster und Stehpult (ab 0,0 s), Petzold erscheint bei „Kommissarin“, Klemmbrett und Stift bei „Aussage“, Tamm bei „Vor ihr“, Pillen „Mitte 40“, „überlebte ein Bootsunglück“; Blasen Petzold, Tamm | tabler:`clipboard-text`, `pencil`; Pillen „Dienstagmorgen“, „Hafenbüro · Wasserschutzpolizei“ | `Fall · Hafenbüro der Wasserschutzpolizei` → `· Aussage von Herrn Tamm` → `· Was ist auf dem Wasser passiert?` → `· Boot im Sturm gesunken` | Stift (`szene_280stift_1`, bei „Aussage“) |
| **A2 Symbolbild See** `planke`→`rettung` | Planke auf den Wellen, Sturmwolke; Pillen in Erzählreihenfolge; Planke tiefer/blasser bei „Unter beiden“; Kutter-Icon bei „Stunden später“ | tabler:`cloud-storm`, `ship`; programmatisch: See, Planke | `Fall · Symbolbild: Planke trägt nur 1 Menschen` → `… 2 Schiffbrüchige an der Planke` → `… Planke geht unter` → `… Herr Tamm stößt den anderen weg` → `… der andere kommt ums Leben` → `… Rettung durch einen Fischkutter` | – |
| **A3 Hafenbüro** `ta2`→`antik` | Blase Tamm; Pillen „Totschlag, § 212 StGB?“, „Klassiker: das Brett des Karneades“, „antikes Gedankenexperiment, zurückgeführt / auf den griechischen Philosophen Karneades“ | tabler:`book` | `Fall · Herr Tamm: sonst beide ertrunken` → `· Strafbar wegen Totschlags?` → `· Klassiker: Brett des Karneades` | – |
| **B Sachverhalt** `sv` | Karte vollständig (≈ 9,9 s), kein Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Tatbestand/Rechtswidrigkeit** `tb`→`v263` | Haken § 212, Vorsatz; Block II.; Kreuz § 34; Verweis 263 | tabler:`lifebuoy`, `eye`, `scale`, `ban` | `A. Herr Tamm, § 212 StGB › I. Tatbestand …` → `› II. Rechtswidrigkeit: § 34 (−)` | – |
| **D § 35 Abs. 1 S. 1** `p35`→`rettw` | Wortlautkarte (gesprochen), Marker „handelt“, „ohne Schuld.“ beim Vorlesen, dann „Leben,“, „gegenwärtigen,“, „nicht anders abwendbaren“, „von sich,“, „um die Gefahr“ zur Subsumtion; fünf Haken | tabler:`book`, `heartbeat`, `lifebuoy`, `shield-check` | `A. Herr Tamm › III. Schuld › § 35 Abs. 1 S. 1 · Wortlaut` → `› Gefahr für Leben` → `› gegenwärtig (+)` → `› nicht anders abwendbar (+)` → `› eigene Person (+)` → `› Rettungswille (+)` | – |
| **E § 35 Abs. 1 S. 2: selbst verursacht** `satz2`→`gast` | Wortlautkarte S. 2, Marker „zugemutet … hinzunehmen;“, „die Gefahr selbst verursacht hat“; Zeilen, Kreuz „nur Fahrgast“ | tabler:`alert-triangle`, `cloud-storm`, `ship` | `… § 35 Abs. 1 S. 2: Hinnahmepflicht? · Wortlaut` → `› 1. Gefahr selbst verursacht?` → `› 1. selbst verursacht (−)` | – |
| **F besonderes Rechtsverhältnis** `rv`→`entsch` | Karte S. 2 erneut, Marker „in einem besonderen / Rechtsverhältnis stand,“; Beispiele; Kreuz; Block „§ 35 (+): entschuldigt“ | tabler:`id-badge-2`, `firetruck`, `ship`, `shield-check` | `… › 2. besonderes Rechtsverhältnis?` → `› 2. etwa Feuerwehr, Polizei, Soldaten` → `› 2. besonderes Rechtsverhältnis (−)` → `A. Herr Tamm › III. Schuld › § 35 (+): entschuldigt` | – |
| **G Abwandlung 1: Kapitän** `abw1`→`kap6` | Kapitän neben der Tafel; Haken Sicherheit/Schutzpflicht, Block „besonderes Rechtsverhältnis (+)“, „zwar … sicheren Tod“ (verbreitete Ansicht), „aber: Gefahr auf den Geschützten abgewälzt“, Block § 212, „keine Strafmilderung“ | tabler:`steering-wheel`, `lifebuoy`, `ban`, `scale` | `Abwandlung 1: Kapitän stößt Fahrgast weg` → `Abwandlung 1: Kapitän › § 35 Abs. 1 S. 2 › …` → `› nicht entschuldigt, § 212` → `› keine Milderung nach S. 2` | – |
| **H Abwandlung 2: Irrtum** `abw2`→`w2` | Zeilen Rettungsboot, Kreuz „objektiv anders abwendbar“, Wortlautkarte § 35 Abs. 2, Marker „irrig Umstände an,“, „wenn er den Irrtum vermeiden konnte.“ | tabler:`speedboat`, `eye-off`, `book` | `Abwandlung 2: Rettungsboot übersehen` → `· objektiv anders abwendbar` → `Abwandlung 2: Irrtum › § 35 Abs. 2 · Wortlaut` | – |
| **I Vermeidbarkeit** `bgh`→`v007` | BGHSt 48, 255 Rn. 35: gewissenhaft geprüft, strenge Anforderungen, Zeit; Block unvermeidbar/straflos, Block vermeidbar/gemildert; Verweis 007 | tabler:`file-search`, `stopwatch`, `shield-check`, `scale` | `… › Irrtum vermeidbar? · BGHSt 48, 255` → … → `› unvermeidbar: straflos` → `› vermeidbar: Strafe zwingend gemildert` | – |
| **J Ergebnis** `erg`→`erg3` | Haken rechtswidrig, Block entschuldigt/straflos, Block Kapitän strafbar | tabler:`scale`, `shield-check`, `steering-wheel` | `Ergebnis` → … | – |
| **K Hafenbüro** `pe2` | Blase Petzold „Ihre Aussage geht jetzt an die Staatsanwaltschaft.“ | tabler:`clipboard-text` | `Ergebnis · Hafenbüro` | – |
| **L Klausurtipp** `tipp`→`t3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · § 35 in der Schuld` → … | – |
| **M Klausurschema** `sch`→`s8` | breite Karte, neun Zeilen progressiv (I.–IV., 1.–4.) | – | `Klausurschema › …` | – |
| **N Merksatz** `merke`, `m2` | Lexi erklärt, zwei Marker | – | `Merksatz` | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 35 Abs. 1 S. 1 (vollständig, auch gesprochen), § 35 Abs. 1 S. 2 (vollständig, zweimal), § 35 Abs. 2 (vollständig). Marker synchron zum gesprochenen Merkmal.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Herr Tamm (Mitte 40) ist Fahrgast auf einem Ausflugsboot. Im Sturm sinkt das Boot. Im Wasser treibt nur eine einzige Planke, die einen Menschen tragen kann. Rettung ist nicht in Sicht.
>
> Ein zweiter Schiffbrüchiger, den Herr Tamm nicht kennt, hält sich ebenfalls an der Planke fest. Unter beiden geht sie unter. Um nicht zu ertrinken, stößt Herr Tamm den anderen weg; er weiß, dass dieser dann ertrinken wird. Der andere kommt ums Leben.
>
> Stunden später zieht ein Fischkutter Herrn Tamm aus dem Wasser. Den Untergang des Bootes hat er nicht verursacht.
>
> **Hat sich Herr Tamm wegen Totschlags (§ 212 StGB) strafbar gemacht?**
