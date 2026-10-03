# Folge 107 · Computerbetrug § 263a: Fremde Karte am Geldautomaten – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_107.py`](src/skript_107.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · StGB BT, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Ein Mann nimmt heimlich die Bankkarte seines Mitbewohners, dessen PIN er kennt, und hebt am Automaten 500 Euro ab“): Heiko kennt die Geheimzahl seiner Mitbewohnerin Meike, nimmt heimlich ihre Bankkarte aus der Geldbörse im Flur, hebt am Geldautomaten an der Ecke 500 € ab und legt die Karte unbemerkt zurück; am nächsten Morgen sieht Meike die Abbuchung. Ablauf: Fall → Frage → Sachverhalt → Wortlautkarte § 263a I, Struktur wie Betrug → a) Tathandlung (Variante 3, richtige Daten) → drei Auslegungen von „unbefugt“ → Probe mit der gedachten Bankangestellten → b) Beeinflussung → c) Vermögensschaden (jedenfalls Bank) → subjektiver Tatbestand, Ergebnis § 263a → B. § 242 am Geld (Wortlautkarte auszugsweise, fremd, keine Wegnahme) → Streit → C. § 242 an der Karte (Zueignungsabsicht: Substanz/Sachwert) → Ergebnis, Konkurrenzen (§ 246) → Klausurtipp (berechtigter Karteninhaber, § 266b) → Prüfschema → Merksatz. Hauptfilm 6:44,7.
**Verhältnis zu Folge 065 (Betrug § 263):** Voraussetzungsfolge. Die Betrugsmerkmale werden nicht wiederholt; § 263a wird nur über die Strukturparallele (Tathandlung statt Täuschung, Beeinflussung statt Irrtum und Verfügung) angeknüpft. Zu Folge 051 (Diebstahl): Zueignungsabsicht und Gebrauchsanmaßung hier nur an der Karte; zu Folge 022 (Tankbetrug): dieselbe Logik „Geben statt Nehmen“ beim Gewahrsam, hier durch den programmierten Automaten.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Heiko, um 30 | Mitbewohner, nimmt die Karte, hebt ab | `standing/shirt-3` (Hemd Grün `#8FD694`, schwarze Hose der Pose, weiße Schuhe), Kopf `Short 2`, ohne Bart, Haut `#E3B48E`; Mimiken `Calm` (redet), `Suspicious` (denkt an die Geheimzahl), `Serious`, `Driven` (Auszahlung, Vorsatz), `Concerned|Serious`, `Smile` | `marc` (Mann, mittel) |
| Meike, um 30 | Mitbewohnerin, Kontoinhaberin | `standing/resting-2` (schwarzer Pullover der Pose, Hose Lila `#B8A9F5`), Kopf `Medium Bangs`, Haut `#F0C8A8`; Mimiken `Calm`, `Concerned|Serious` (redet erschrocken), `Fear`, `Serious`, `Suspicious` | `sabrina` (Frau, mittel) |
| gedachte Bankangestellte | Funktionsrolle der Probe (ohne Namen, spricht nicht) | `standing/blazer-3` (Blazer Blau `#8DB3F2`, Hose `#4A4A55`), Kopf `Medium 1`, Brille `Glasses 2`, Haut `#C68E62`; `Calm`, `Suspicious` | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links: Heiko im Flur zur Kommode, am Automaten zum Automaten, in den Tafelszenen zur Tafel), `_r` blickt nach rechts (Heiko in der Frage zu Meike, die Bankangestellte zu Heiko).
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimik nur als `Concerned|Serious`. Mundzustände a/o/e bei `HE_redet`, `MK_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (shirt-1/-2 wegen Prothese bewusst nicht für den Täter). 52 Figuren-PNGs in `../peeps/op_107/` (Drive-Master).
- **Klischeeprüfung:** Heiko ist ein gewöhnlicher Mitbewohner (Hemd, Jeans, ruhige oder ernste Mimik, nie „fies“), keine Herkunfts- oder Hautfarbenzuschreibung; Meike als ruhige, dann erschrockene Kontoinhaberin.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und per `grep -rlw` in keinem Skript, Szenenplan, Abnahmebogen, JSON oder CSV unter `youtube/` (03.10.2026): Heiko, Meike („Hannes“ und „Merle“ wegen früherer Folgen verworfen). Nie im Genitiv mit -s („die Bankkarte von Meike“).
- **Stimmen** nur aus dem Pool (william, sabrina, marc, laura_ruhig): marc und sabrina. Vorfolge 106 (hilde, christian) ohne Überschneidung; 105 nutzte marc und sabrina in anderen Rollen, Posen und Szenen (Pool erlaubt keine Alternative mit Männerstimme mittleren Alters außer marc).

**Abweichung von den letzten Folgen:** 104 Kneipe/Tresen (Mittäterschaft), 105 Behörde/Gericht, 106 Kanzlei und Wohnzimmer mit Laptop. Hier neu: Flur einer Wohngemeinschaft (Badezimmertür mit Dusche, Kommode mit Geldbörse), ein aus Karten und Tabler-Icons gebauter **Geldautomat ohne Bank- oder Markenlogo** (Bildschirm, Tastenfeld, Kartenschlitz, Ausgabefach), Karte und Geldschein wandern, am Morgen die Kontoumsätze auf dem Handy. Posen `shirt-3` (zuletzt 102), `resting-2` und `blazer-3` (in 104–106 nicht verwendet); kein Polka-Dots-Muster.
**Tageslicht:** durchgehend Cremegrund („Freitagabend“ und „Am nächsten Morgen“ als Pille, Sonnenaufgang-Icon; kein Nachtbild).

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Flur** `fall`→`h1` | Heiko neben der Kommode; Denkblase „Geheimzahl“, Pille „beim Einkaufen gesehen“; Dusche hinter der Tür, Geldbörse auf der Kommode; Karte wandert heimlich zu Heiko; Sprechblase „Die Karte lege ich gleich wieder zurück.“ | tabler:`door`, `wallet`, `password`; fluent:`shower`, `credit-card` | `Fall · Die Karte im Flur` (ab 0,0 s) | ≈ 9 | – |
| **A2 Geldautomat** `automat`→`geld` | Automat (Karten) mit Bildschirm „Geheimzahl“ → „500 €“ → „Auszahlung“, Tastenfeld gelb bei der Eingabe; Karte in den Schlitz, Geldschein aus dem Ausgabefach zu Heiko | tabler:`dialpad`, `password`; fluent:`credit-card`, `euro-banknote` | `Fall · Am Geldautomaten` | ≈ 9 | Karte einstecken (`szene_107karte_1`), Geldausgabe (`szene_107geld_1`) |
| **A3 Flur / Morgen / Frage** `zurueck`→`frage2` | Karte zurück in die Geldbörse („unbemerkt zurück“); Morgen: Meike mit Handy, Pille „Kontoumsatz: −500 €“, Sprechblase „500 € abgehoben? / Das war ich nicht!“; Frage-Pillen, Heiko wieder im Bild | tabler:`wallet`, `device-mobile`; fluent:`sunrise`, `credit-card` | `Fall · Die Karte zurück` → `Fall · Der nächste Morgen` → `Fall · Die Frage` | ≈ 10 | – |
| **B Sachverhalt** `sv` | Karte vollständig, 9,8 s | – | `Sachverhalt` | 1 | – |
| **C Wortlaut** `p263a`→`ersetzt` | Wortlautkarte § 263a I (vier Marker), Gegenüberstellung Betrug/Computerbetrug | tabler:`cpu`, `scale`, `arrow-narrow-right` | `A. § 263a StGB › Wortlaut` → `› dem Betrug nachgebildet` | ≈ 10 | – |
| **D Tathandlung** `t1`→`frageu` | Variante 3 (gelber Block), Haken „echt“, „richtige Daten“, Block „Entscheidend: unbefugt?“ | fluent:`credit-card`; tabler:`password` | `… › I. 1. objektiver Tatbestand › a) Tathandlung` → `… › a) unbefugte Verwendung von Daten` | ≈ 7 | – |
| **E Auslegungen** `ausl`→`arg` | subjektiv (+), computerspezifisch (−), betrugsspezifisch (Block, Rspr./h. M.), Zweck | tabler:`user-question`, `cpu`; fluent:`balance-scale` | `… › a) „unbefugt“: drei Auslegungen` → `…: betrugsspezifische Auslegung` | ≈ 9 | – |
| **F Probe** `probe`→`unbefok` | gedachte Bankangestellte und Heiko; Denkblase „berechtigt?“; Karte und Geheimzahl dazwischen; Kreuz „nicht berechtigt“, Haken „würde getäuscht“, Block „(+)“ | fluent:`credit-card`; tabler:`password` | `…: Probe mit dem Bankangestellten` → `… › a) unbefugte Verwendung (+)` | ≈ 11 | – |
| **G Beeinflussung** `dv`→`dv4` | Kette Karte/Geheimzahl → Automat → Geld, Ingangsetzen, unmittelbar, Block „(+)“ | tabler:`cpu`, `password`, `arrow-narrow-right`; fluent:`credit-card`, `euro-banknote` | `… › b) Beeinflussung des Ergebnisses eines Datenverarbeitungsvorgangs` | ≈ 12 | – |
| **H Schaden** `schad`→`jedenf` | Bank, kein Erstattungsanspruch, Konto ausgleichen, Block „jedenfalls bei der Bank“ | tabler:`building-bank` | `… › c) Vermögensschaden` → `… › c) Schaden jedenfalls bei der Bank` | ≈ 6 | – |
| **I Subjektiv, Ergebnis** `vors`→`erg1` | Vorsatz, Absicht, RW/Schuld, Block „strafbar wegen Computerbetrugs“ | tabler:`bulb`, `circle-check`; fluent:`euro-banknote` | `… › I. 2. subjektiver Tatbestand › a) Vorsatz` → `› b) Absicht …` → `… › II. Rechtswidrigkeit, III. Schuld` → `A. § 263a StGB › Ergebnis (+)` | ≈ 7 | – |
| **J § 242 am Geld** `geld242`→`gew2` | Wortlautkarte § 242 I (Auszug, zwei Marker), fremd (+), Wegnahme (−), Gewahrsam, „übergeben“ | fluent:`euro-banknote`; tabler:`dialpad` | `B. § 242 StGB am Geld` → `… › Wegnahme: Bruch fremden Gewahrsams?` | ≈ 11 | – |
| **K Streit** `streit`→`kein242` | hellroter Block (früher Diebstahl), grüner Block (BGH, Gesetzgeber), Block „(−)“ | tabler:`gavel` | `B. … › Streit` → `B. … › Diebstahl (−)` | ≈ 5 | – |
| **L § 242 an der Karte** `karte`→`kein242k` | fremd/weggenommen, Zueignungsabsicht, Substanz (−), Sachwert (−) mit Sparbuch-Vergleich, Block | fluent:`credit-card`; tabler:`arrow-back-up`, `notebook` | `C. § 242 StGB an der Karte` → `… › Zueignungsabsicht` | ≈ 12 | – |
| **M Ergebnis, Konkurrenzen** `erg`, `konk` | Ergebnisblock, § 246 tritt zurück | tabler:`circle-check` | `Ergebnis · Heiko strafbar, § 263a Abs. 1 StGB` → `D. Konkurrenzen` | 3 | – |
| **N Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Wer benutzt die Karte?` → `Klausurtipp · § 266b StGB` | ≈ 8 | – |
| **O Prüfschema** `sch`→`s4` | breite Karte A. I. 1. a)–c), 2. a)–b), II./III., B., C., D. | – | `Prüfschema` → je Punkt ein Pfadstand | 12 | – |
| **P Merksatz** `merke`→`mk3` | Lexi erklärt (redet), drei Sätze mit Marker | – | `Merksatz` | ≈ 7 | – |

**Blasen:** Sprechblasen Stil C (`bausteine.blase`), Schwanzspitze außerhalb der Blase am Mund; Denkblasen Heiko („Geheimzahl“) und Bankangestellte („berechtigt?“). **Zahlen** auf Blasen, Tafeln und Pillen in Ziffern („500 €“, „§ 263a Abs. 1 StGB“, „4 Varianten“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; Bewegungen: Karte zu Heiko (A1), Karte in den Schlitz und Geldschein zu Heiko (A2), Karte zurück in die Geldbörse (A3).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_107karte_1` aus 717370, `szene_107geld_1` aus 405302), Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji Flat (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (**CC BY 4.0**, Namensnennung in `beschreibung.txt`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Heiko und Meike wohnen in einer Wohngemeinschaft. Heiko kennt die Geheimzahl (PIN) der Bankkarte von Meike, weil er sie beim gemeinsamen Einkaufen gesehen hat. An einem Freitagabend steht Meike unter der Dusche, ihre Geldbörse liegt im Flur. Heiko nimmt heimlich die Bankkarte heraus; er will sie von Anfang an gleich wieder zurücklegen.
>
> Am Geldautomaten an der Ecke steckt er die Karte ein, tippt die Geheimzahl und hebt 500 € ab. Zu Hause legt er die Karte unbemerkt in die Geldbörse zurück. Am nächsten Morgen sieht Meike die Abbuchung.
>
> **Wie hat sich Heiko strafbar gemacht?**
