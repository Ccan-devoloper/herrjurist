# Folge 065 · Betrug § 263 Schema: Täuschung, Irrtum, Verfügung, Schaden – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_065.py`](src/skript_065.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · StGB BT, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Ein Mann verkauft online ein angeblich neues Smartphone und verschickt ein Gerät mit gesprungenem Display“): Detlef stellt eine Kleinanzeige ins Netz (Smartphone „neu und originalverpackt“, 400 €, Foto eines heilen Geräts, „Top-Handy, ein echtes Schnäppchen!“), obwohl das Display des Geräts, das er verschicken will, gesprungen ist; Waltraud fragt am Telefon nach, überweist per Vorkasse, packt das Gerät aus (Wert 150 €). Ablauf: Fall → Frage → Sachverhalt → Wortlautkarte § 263 I und Kette → 1. Täuschung (Tatsachen, ausdrücklich, konkludent) → Abgrenzung Anpreisung → 2. Irrtum → 3. Vermögensverfügung (Abgrenzung Trickdiebstahl) → 4. Schaden (Gesamtsaldierung, Eingehungs-/Erfüllungsschaden) → Rechnung und Bezifferung (BVerfG), Kette steht → subjektiver Tatbestand (Vorsatz, Absicht, Rechtswidrigkeit, Stoffgleichheit) → Rechtswidrigkeit, Schuld, Ergebnis → Ausblick (§ 263 II, III, § 263a) → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 6:45,6.
**Verhältnis zu Folge 047 (Vermögensdelikte Überblick):** Dort steht § 263 nur als Säule der Landkarte (Wortlaut, Sachbetrug, Abgrenzung Trickdiebstahl). Hier wird das Schema vertieft; die Abgrenzung zum Trickdiebstahl kommt nur in einem Satz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Detlef, um 45 | Privatverkäufer | `standing/shirt-4` (dunkles Hemd der Pose, Hose Blau `#8DB3F2`, weiße Schuhe), Kopf `Short 4`, ohne Bart, Haut `#E8B48C`; Mimiken `Calm`, `Smile` (redet), `Suspicious` (denkt ans Display), `Serious`, `Concerned|Serious`, `Driven` | `christian` (Mann, mittel) |
| Waltraud, um 65 | Käuferin | `standing/polka_dots` (gepunktete Bluse, Hose Grün `#8FD694`), Kopf `Gray Bun`, Brille `Glasses 2`, Haut `#F0C8A8`; Mimiken `Calm` (redet, fragt), `Concerned|Serious` (redet entsetzt), `Smile`, `Suspicious`, `Serious`, `Fear` | `hilde` (Frau, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Beide Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links: Waltraud im Fall zu Detlef, beide in den Tafelszenen zur Tafel), `_r` blickt nach rechts (Detlef im Fall zu Waltraud).
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimik nur als `Concerned|Serious`. Mundzustände a/o/e bei `DE_redet`, `WA_redet`, `WA_entsetzt` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen. 56 Figuren-PNGs in `../peeps/op_065/` (Drive-Master).
- **Klischeeprüfung:** Detlef ist ein gewöhnlicher Privatverkäufer (Hemd, Jeans), keine Karikatur, keine „fiese“ Mimik, keine Herkunfts- oder Hautfarbenzuschreibung; Waltraud als ruhige, aufmerksame ältere Käuferin, nicht als naive Witzfigur.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keinem Skript oder Dokument unter `preproduction/` (Volltextsuche): Detlef, Waltraud. Nie im Genitiv mit -s („aus dem Vermögen von Waltraud“).
- **Stimmen** nur aus dem Pool; nur eine Männerstimme (christian), stephan nicht eingesetzt (keine Verwechslungsgefahr), lucy nicht gebraucht. Vorfolgen 062 (lucy, stephan) und 063 (lucy, hilde, christian, stephan): christian und hilde in anderen Rollen, Posen und Szenen.

**Abweichung von den letzten Folgen:** 062 Tattoostudio, 063 Elektrogeschäft/Küche mit Kühlschranklieferung und Telefonat, 064 Straße vor einer Apotheke. Hier neu: zwei Privatwohnungen nebeneinander (getrennt durch eine graue Linie) mit Detlef am Schreibtisch mit Laptop, eine **Kleinanzeige als Karte** in der Bildmitte, Telefonhörer an beiden Seiten, ein Geldschein wandert zu Detlef, ein Paket wandert zu Waltraud, das gesprungene Smartphone (Streamline-Icon). Die Posen `shirt-4` (zuletzt 058) und `polka_dots` (zuletzt 059) kommen in 060–064 nicht vor.
**Tageslicht:** durchgehend Cremegrund (Sonntagabend nur als Zeitangabe, kein Nachtbild).

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Die Kleinanzeige** `fall`→`frage2` | links Detlef am Schreibtisch, rechts später Waltraud; Anzeige-Karte (Foto, Text, Preis, Anpreisung), Denkblase „Display gesprungen“, Telefonat mit zwei Blasen, 400 € wandern zu Detlef, Paket wandert zu Waltraud, Auspacken, Blase „Das Display ist ja gesprungen!“, Wertpille, Fragepillen | tabler:`desk` (Holz), `device-mobile`; fluent:`laptop`, `telephone-receiver`, `euro-banknote`, `package`; streamline-freehand:`broken-smartphone-1` | `Fall · Die Kleinanzeige` (ab 0,0 s) → `Fall · Der Anruf` → `Fall · Vorkasse und Paket` → `Fall · Das Display` → `Fall · Die Frage` | ≈ 25 | Paket kommt an (`szene_065paket_1`), Auspacken (`szene_065auspacken_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **C Wortlaut und Kette** `p263`→`subj0` | Wortlautkarte § 263 I mit vier Markern, Kettenleiste baut sich am Wort auf, Zeilen Verfügung/Glied, Block subjektiv | fluent:`chains` | `§ 263 Abs. 1 StGB › Wortlaut` → `› Kette: …` → `› subjektiver Tatbestand` | ≈ 12 | – |
| **D Täuschung** `t1`→`konkl2` | Kettenleiste (Täuschung gelb), Tatsachen, prüfbar, ausdrücklich, konkludent, Foto | tabler:`device-mobile`, `photo` | `I. Tatbestand › 1. objektiv › a) Täuschung über Tatsachen` → `… › a) Täuschung: ausdrücklich und konkludent` | ≈ 10 | – |
| **E Abgrenzung Anpreisung** `anpreis`, `tok` | Zitatpille, Kreuz, Werturteil, Ergebnisblock | fluent:`sparkles`; tabler:`circle-check` | `… › a) Täuschung: keine bloße Anpreisung` → `… › a) Täuschung (+)` | ≈ 5 | – |
| **F Irrtum** `irr`→`irr3` | Kettenleiste (Irrtum gelb), Definition, zwei Haken, Block; Denkblase Waltraud mit heilem Handy | tabler:`device-mobile` | `… › b) Irrtum` | ≈ 6 | – |
| **G Vermögensverfügung** `vf`→`trick` | Definition, drei Haken, Kasten Trickdiebstahl | fluent:`euro-banknote`; tabler:`hand-grab` | `… › c) Vermögensverfügung` → `… › c) Abgrenzung: Trickdiebstahl, § 242 StGB` | ≈ 9 | – |
| **H Schaden** `schad`→`erf` | Gesamtsaldierung, Eingehungs-/Erfüllungsschaden | fluent:`balance-scale`, `euro-banknote`; tabler:`file-text` | `… › d) Vermögensschaden` → `… › d) Schaden: Eingehungs- und Erfüllungsschaden` | ≈ 8 | – |
| **I Rechnung, Bezifferung** `rech`→`kette2` | Rechnung 400 − 150 = 250 €, BVerfG, Kette grün, Block | tabler:`calculator`, `report-money`; fluent:`chains` | `… › d) Schaden: 250 €` → `… › d) Schaden der Höhe nach beziffern` → `I. Tatbestand › 1. objektiver Tatbestand (+)` | ≈ 14 | – |
| **J Subjektiv** `vors`→`stoff2` | Vorsatz, Absicht, rechtswidrig, stoffgleich; Geldschein wandert von Waltraud zu Detlef | tabler:`bulb`, `target-arrow`; fluent:`euro-banknote` | `I. Tatbestand › 2. subjektiv › a) Vorsatz` → `… › b) Absicht rechtswidriger Bereicherung` → `… › b) Stoffgleichheit` | ≈ 12 | – |
| **K Ergebnis** `rw`→`erg` | Haken RW, Schuld, Ergebnisblock | tabler:`circle-check` | `II. Rechtswidrigkeit, III. Schuld` → `Ergebnis · Detlef strafbar, § 263 Abs. 1 StGB` | ≈ 4 | – |
| **L Ausblick** `versuch`→`p263a` | hell-lila Tafel: Versuch, § 263 III, § 263a | tabler:`hand-stop`, `repeat`, `cpu` | `Ausblick › Versuch, § 263 Abs. 2 StGB` → `› besonders schwerer Fall, § 263 Abs. 3 StGB` → `› Computerbetrug, § 263a StGB` | ≈ 9 | – |
| **M Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand), tabler:`arrow-narrow-right` | `Klausurtipp · Kette sauber verknüpfen` → `Klausurtipp · Schaden konkret berechnen` | ≈ 8 | – |
| **N Prüfschema** `sch`→`k4` | breite Karte, I. 1. a)–e), 2. a)–b), II., III., IV. | – | `Prüfschema` → je Unterpunkt ein Pfadstand | 14 | – |
| **O Merksatz** `merke`→`m3` | Lexi erklärt (redet), drei Sätze mit Marker | – | `Merksatz` | ≈ 4 | – |

**Kettenleiste:** Auf den Merkmalstafeln D–H steht oben die Kette „Täuschung → Irrtum → Vermögensverfügung → Schaden“ (Pfeile Tabler `arrow-narrow-right`): geprüfte Glieder grün, das aktuelle gelb, folgende weiß. In C und I baut sie sich am gesprochenen Wort auf („Daraus folgt eine Kette …“, „Damit steht die Kette …“).
**Blasen:** Sprechblasen Stil C (Standard seit 02.10.2026), Schwanzspitze außerhalb der Blase am Mund; zwei Denkblasen (Detlef: Display gesprungen; Waltraud: heiles Handy). **Zahlen** auf Blasen, Tafeln und Pillen in Ziffern („400 €“, „150 €“, „2 Tage später“, „§ 263 Abs. 1 StGB“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; Bewegungen: Geldschein zu Detlef (A, J), Paket zu Waltraud (A).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_065paket_1` aus 465451, `szene_065auspacken_1` aus 452566), Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji Flat (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol und gesprungenes Smartphone Streamline Freehand (**CC BY 4.0**, Namensnennung in `beschreibung.txt`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> An einem Sonntagabend stellt Detlef eine Kleinanzeige ins Netz: ein Smartphone, „neu und originalverpackt“, für 400 €. Das Foto zeigt ein unbeschädigtes Gerät. Detlef weiß, dass das Display des Geräts, das er verschicken will, gesprungen ist. Dazu schreibt er: „Top-Handy, ein echtes Schnäppchen!“
>
> Waltraud ruft an und fragt, ob das Handy wirklich neu ist. Detlef antwortet: „Ja, ganz neu, noch nie benutzt.“ Waltraud überweist die 400 € per Vorkasse. Zwei Tage später packt sie das Gerät aus: Das Display ist gesprungen. So ist das Gerät nur noch 150 € wert.
>
> **Hat sich Detlef wegen Betrugs nach § 263 StGB strafbar gemacht?**
