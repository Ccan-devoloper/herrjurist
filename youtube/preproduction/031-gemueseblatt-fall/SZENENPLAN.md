# Folge 031 · Gemüseblatt-Fall: Vertrag mit Schutzwirkung für Dritte erklärt – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_031.py`](src/skript_031.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker-Fall). Der echte Fall BGH, Urt. v. 28.1.1976 – VIII ZR 246/74 = BGHZ 66, 51 wird sachlich nacherzählt; die Beteiligten sind namenlose Funktionsfiguren. Ablauf: Fall (Laden 1963) → Klage 1970 und Verjährungseinrede → Frage → Sachverhalt → Warum Vertrag? (Verjährung, § 278 statt § 831, Beweislast) → Die Mutter: culpa in contrahendo (Wortlaut § 311 II, § 241 II) → Die Tochter selbst (keine eigene c.i.c.) → Vertrag mit Schutzwirkung → vier Voraussetzungen mit Subsumtion → schon vor Vertragsschluss (Gesetzesbegründung) → Streitstand Herleitung → Prüfung I.–IV., Ergebnis → Heute → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:52 (5.841 Zeichen, Grenze 6.200). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Die Mutter (MU), um 40 | Kundin, Vertragspartnerin in spe | `standing/shirt-3` (Hemd Lila `#B8A9F5`, schwarze Hose), Kopf `Medium Bangs 2` (Haar `#6B4226`), Haut `#E8BE9A`; Mimiken `Calm`, `Smile`, `Concerned|Serious` (redet, Sorge), `Fear` (Schreck), `Serious` | `lucy` (Frau, jung) |
| Die Tochter (TO/TS), 14 | Klägerin, begleitet die Mutter; spricht nicht | `standing/walking-3` (schwarzes Oberteil und Hose), nach dem Sturz `sitting/mid-1` mit schwarz gefärbter Hose (gleiches Outfit), Kopf `Long`, Haut `#E8BE9A`; stehend 430 px (Erwachsene 480 px); Mimiken `Calm`, `Smile`, `Serious`, `Suspicious`, `Smile Big|Smile`, am Boden `Fear`, `Concerned|Serious`, `Tired` | – |
| Der Betreiber des Ladens (BE), um 50 | Beklagter | `standing/pointing_finger-2` (schwarzes Oberteil, Hose Blau `#8DB3F2`), Kopf `Short 3`, Brille `Glasses 2`, kein Bart, Haut `#D9A47A`; Mimiken `Contempt` (redet, abwehrend), `Calm`, `Serious`, `Suspicious`, `Concerned|Serious` (ertappt); `crossed_arms-2` wegen anderer Statur verworfen | `marc` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Keine realen Personen als Porträt, keine Namen:** Schilder „Mutter“, „Tochter, 14“ bzw. „Tochter“ (1970), „Betreiber des Ladens“/„Betreiber“. Verletzung zurückhaltend (sitzend am Boden, Pflaster-Symbol, „am Knie verletzt“).
- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts (Mutter zur Kasse und Tochter, Tochter in Laufrichtung und zum Betreiber).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `MU_redet`, `BE_redet` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool** lucy, marc, hilde, timo; hilde und timo nicht gebraucht (keine Mädchenstimme im Pool → die Tochter spricht nicht). Keine Überschneidung mit 030 (lea, william, laura_ruhig).
- **Namen:** keine Figurennamen im Sprechtext (nur „die Mutter“, „die Tochter“, „der Betreiber“); damit entfällt das Risiko wechselnder Aussprache. Geprüft wurden stattdessen Fachwörter (culpa in contrahendo, Gemüseblatt, Salatblattfall, Gläubigernähe).
- Figuren-PNGs: `../peeps/op_031/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 030 (Schlüssigkeitsprüfung, Gericht), 029 (Vorsatzformen), 027 (WG/Fahrradladen), 010 (Einrichtungshaus, culpa in contrahendo: dort die erfundene Teppichrollen-Variante des Linoleumrollen-Falls). Hier neu: Selbstbedienungsladen 1963 mit Regal, Kasse und Packablage, die Tochter geht hinter der Kasse herum; Klageszene 1970 vor dem Laden. Neue Posen gegenüber 029/030 (`shirt-3` ist in 029 vergeben, hier andere Farbe/Kopf; `walking-3`, `sitting/mid-1`, `pointing_finger-2` neu). Zweite Folge mit Wortlautkarten (§ 311 II, § 241 II).

## Szenen

Alle Szenen auf Cremegrund (Tag).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Im Selbstbedienungsladen** `fall`–`knie` | Regal links, Kasse (Theke), Packablage rechts; Mutter an der Kasse, Tochter geht hinter der Kasse herum zur Packablage, rutscht auf dem Gemüseblatt aus, sitzt am Boden | tabler: `carrot` (Orange), `apple` (Rot), `leaf` (Grün), `basket` (Gelb), `shopping-bag` (Blau), `cash-register` (Weiß), `leaf` liegend als Gemüseblatt (um 70° gedreht), `bandage`; Regal/Theke/Packablage aus `karte`/`linienzug` | `Fall · Im Selbstbedienungsladen` (ab 0,0 s) | Laden · Mutter · Tochter · Kasse + Waren · Weg zur Packablage · Gemüseblatt · Sturz · Blase Mutter · „am Knie verletzt“ · „länger behandelt“ | Sturz `szene_031sturz_1` beim Wort „stürzt“ |
| **B Die Klage** `klage`–`frage` | Tochter (1970) links mit Klageschrift, Betreiber rechts vor dem Laden; Verjährungseinrede | tabler: `building-store` (Gelb), `file-text`, `hourglass` (Gelb) | `Fall · Die Klage` → `Fall · Die Frage` | Tochter · Klageschrift · Betreiber · Pille Klage · Blase · Sanduhr · Frage-Pillen | – |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 10 s, mit Quelle (BGH, Az., BGHZ) | – | `Sachverhalt` | 1 | – |
| **D Warum Vertrag?** `delikt`–`vbew` | Tafel, Tochter und Betreiber | tabler: `hourglass`, `link`, `scale` | `Vorfrage · Delikt oder Vertrag?` → `· Verjährung damals` → `· Vorteile der vertraglichen Haftung` | § 823 · ✗ Verjährung · ✓ 30 Jahre · Vorteile · ✓ § 278 · keine Entlastung · ✓ Beweislast | – |
| **E Die Mutter** `mutter2`–`p241` | Wortlautkarten § 311 II und § 241 II mit Markern; Mutter, Laden-Symbol | tabler: `building-store` | `Die Mutter · culpa in contrahendo` → `· § 311 Abs. 2 Nr. 2 BGB: Anbahnung` → `· Rücksichtspflichten, § 241 Abs. 2 BGB` | Titel · Karte § 311 II · Marker (3) · Laden · Karte § 241 II · Marker (2) | – |
| **F Die Tochter selbst** `kind`–`kind5` | Tafel, Tochter | tabler: `shopping-cart-off`, `umbrella` (Blau), `walk` | `Die Tochter · eigenes Schuldverhältnis?` | Frage · nur begleitet · möglicher Kunde · ✗ Wetter · ✗ Durchgang · Block | – |
| **G Schutzwirkung** `vsd`–`vsd4` | Tafel, Mutter und Tochter, Laden und Schutzschild | tabler: `building-store`, `shield-check` (Grün) | `Vertrag mit Schutzwirkung für Dritte` | Titel · Schutzbereich · ✗ Leistung · ✓ Schutz · ✓ Schadensersatz · Block | – |
| **H Vier Voraussetzungen** `ln`–`sb2` | Karte mit vier Punkten, je Subsumtion mit Haken; Symbol wechselt | tabler: `cash-register`, `heart` (Rot), `eye`, `shield-check` | `Schutzwirkung › 1. Leistungsnähe` → `› 2. Einbeziehungsinteresse (Gläubigernähe)` → `› 3. Erkennbarkeit und Zumutbarkeit` → `› 4. Schutzbedürfnis` | je Punkt: Titel, (Definition,) Haken + Symbol (≈ 9 Halte) | – |
| **I Vor Vertragsschluss** `vor`–`begr2` | Tafel, Mutter und Tochter | tabler: `cash-register`, `book` | `Schutzwirkung › schon vor dem Vertragsschluss` | Satz · ✓ vor wie nach · Gesetzesbegründung · „Salatblattfall“ · Block | – |
| **J Streitstand** `streit`–`st5` | Tafel, Waage | tabler: `scale`, `book` (Grün, Blau) | `Streitstand · Woraus folgt die Schutzwirkung?` | Titel · Rspr. § 157 · a. A. · offen gelassen · § 328 analog · § 311 III · offen | – |
| **K Prüfung I.–II.** `a`–`p2b` | Tafel, Tochter und Betreiber, Gemüseblatt | tabler: `leaf` liegend | `A. Tochter gegen Betreiber › …` (I., II.) | Normkette · I. · ✓ · II. · Boden · ✓ Gemüseblatt | – |
| **L Prüfung III.–IV.** `p3`–`erg` | Tafel, Tochter und Betreiber | tabler: `link` | `A. Tochter gegen Betreiber › III. …` → `› IV. Schaden` → `› Ergebnis` | III. · vermutet · ✓ · § 278 · IV. · ✓ Aufwendungen · Mitverschulden · Ergebnis | – |
| **M Heute** `heute`–`h3` | Tafel, Tochter, drei Symbole | tabler: `hourglass`, `coin-euro`, `link` | `Heute · was vom Vorteil bleibt` | ✗ Verjährung · § 195 · ✓ § 253 II · ✓ § 278 | – |
| **N Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · erst das eigene Schuldverhältnis` → `· nicht § 328 BGB verwechseln` | 6 Halte | – |
| **O Klausurschema** `sch`–`s9` | breite Karte, Aufbau Punkt für Punkt | – | `Klausurschema` | Titel · Anspruch · I. · 1.–5. · II. · III. · IV. | – |
| **P Merksatz** `merke`, `m2` | Lexi erklärt, Merksatz mit Markern | – | `Merksatz` | 4 Halte | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegung nur beim Gang der Tochter zur Packablage (hinter der Kasse entlang).
**Geräusche:** ein Handlungsgeräusch (Sturz), Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json); ein Kassengeräusch war geplant, Freesound war über den Proxy gesperrt.
**Blasen:** wortgleich mit dem Gesprochenen.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Im November 1963 begleitet eine 14-jährige Tochter ihre Mutter zum Einkauf in einen kleinen Selbstbedienungsladen. Die Mutter hat ihre Waren ausgesucht und steht noch an der Kasse. Die Tochter geht um die Kasse herum zur Packablage, um beim Einpacken zu helfen. Dort rutscht sie auf einem Gemüseblatt aus und verletzt sich am Knie; sie muss länger ärztlich behandelt werden.
>
> 1970 verklagt die Tochter den Betreiber des Ladens auf Ersatz ihres Schadens. Er beruft sich unter anderem auf Verjährung.
>
> BGH, Urt. v. 28.1.1976 – VIII ZR 246/74, BGHZ 66, 51 (Gemüseblatt-Fall)
>
> **Hat die Tochter einen vertraglichen Anspruch gegen den Betreiber?**
