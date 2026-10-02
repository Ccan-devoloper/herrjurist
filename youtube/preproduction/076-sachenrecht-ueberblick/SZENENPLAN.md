# Folge 076 · Sachenrecht Überblick: Eigentum an Sachen und Grundstücken – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_076.py`](src/skript_076.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/Sachenrecht, Themenplan-Format „Schema“ (Leitentscheidung im Plan leer). Ein durchgehender, frei erfundener Beispielfall nach dem Plan-Hook („Handy, Auto, Haus – wie Eigentum übergeht, wann guter Glaube hilft und was die Grundbucheintragung bewirkt“) mit drei Stationen:
1. **Handy:** Arne verkauft Nina für 150 € sein altes Handy – es gehört aber seiner Schwester, die es ihm nur geliehen hat (§ 929 S. 1, § 932, § 1006, § 935: gutgläubiger Erwerb gelingt).
2. **Auto:** Herr Kuhnert verkauft Nina auf einem Parkplatz für 6.000 € den Gebrauchtwagen seines Schwagers; die Zulassungsbescheinigung will er „nächste Woche“ schicken (§ 932 II, BGH V ZR 8/19 Rn. 29: grob fahrlässig, kein Erwerb).
3. **Haus:** Frau Lohse steht im Grundbuch, das Haus gehört aber noch ihrem Bruder (§§ 873 I, 925, § 892: Erwerb mit Eintragung; Widerspruch und Vormerkung je ein Satz).

Ablauf: Fall (drei Stationen) → Frage → Sachverhalt → drei Grundsätze (Publizität, Spezialität, Abstraktion; Verweis auf die Videos 005 und 027) → Wortlautkarte § 929 S. 1 mit Subsumtion → Übergabeersatz §§ 929 S. 2, 930, 931 (Überblick) → Wortlautkarte § 932 I 1, II → Rechtsschein des Besitzes (§ 1006) → § 935 (Ausnahme Geld ein Satz) → Auto (ZB II, grob fahrlässig) → Wortlautkarte § 873 I, § 925 → § 892, Widerspruch, Vormerkung → **Vergleichstabelle progressiv** → Ergebnis → Klausurtipp (Lexi) → Klausurschema → Merksatz (Lexi).
**Länge:** Hauptfilm 6:56,7 (5.925 Zeichen). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Nina (NI), um 30 | Käuferin in allen drei Stationen | Reihe „-1“ (Oberteil Lila `#B8A9F5`, schwarze Hose): `standing/resting-1` (ruhig, redet, froh, Schreck), `crossed_arms-1` (denkt, Sorge, zufrieden), `walking-1` (geht, nicht eingesetzt); Kopf `Long Curly`, Haut `#E8B98F`; Mimiken `Calm`, `Serious` (redet), `Smile`, `Suspicious`, `Concerned|Serious`, `Smile Big|Smile`, `Fear` | `julia` (Frau, jung) |
| Arne (AR), um 25 | Bekannter, verkauft das Handy seiner Schwester | `standing/easing-1` (offenes Hemd), Kopf `Short 3`, Haut `#B07552`; `Calm`, `Smile` (redet), `Smile Big|Smile`, `Suspicious` | `niklas` (Mann, jung) |
| Herr Kuhnert (KU), um 60 | verkauft den Gebrauchtwagen seines Schwagers | `standing/robot_dance-3` (offene Hand, reicht den Schlüssel), Oberteil Grau `#9C9CA6`, Hose Blau `#8DB3F2`, Kopf `No Hair 1`, Brille `Glasses 3`, Haut `#F0C8A8`; `Calm`, `Smile` (redet), `Suspicious`, `Serious` | `helmut` (Mann, älter) |
| Frau Lohse (LO), um 35 | im Grundbuch eingetragene Verkäuferin des Hauses | `standing/blazer-4`, Blazer Gelb `#F9D56E`, Kopf `Long Bangs`, Haut `#D9A07A`; `Calm`, `Smile` (redet), `Concerned|Serious` | `ela_froh` (Frau, jung) |
| Schwester von Arne, Schwager von Herrn Kuhnert, Bruder von Frau Lohse | nur erwähnt (Pillen) | keine Figur | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (geprüft per `grep -rlw` im ganzen `youtube/`-Ordner, inkl. der laufenden Folgen 073–075, und gegen die Koordinatorliste): Nina, Arne, Kuhnert, Lohse. Kein Genitiv eines Namens im Sprechtext („die Schwester von Arne“, „der Schwager von Herrn Kuhnert“). Die Figuren nennen keine Namen; alle Nennungen spricht die Erzählerin.
- **Stimmen nur aus dem Pool** niklas, helmut, ela_froh, julia (alle vier eingesetzt); Erzählerin/Lexi Carla ohne Rolle.
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. In den Fallszenen steht Nina links und blickt nach rechts zum Gegenüber, die Verkäufer stehen rechts und blicken nach links; in den Tafelszenen blicken alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `NI_redet`, `AR_redet`, `KU_redet`, `LO_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur der Verkäufer (Alltagskleidung).
- Figuren-PNGs: `../peeps/op_076/` (72 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 073 (Fernhandlung per Handy, Geld fliegt), 027 (WG-Keller, Fahrradladen), 005 (Bäckerei, Haustür). Hier neu: drei Kaufstationen auf einer Bühne mit wechselndem Ort – Handyübergabe Hand in Hand, Parkplatz mit Gebrauchtwagen (Auto fährt sichtbar los), Notartermin mit Unterschrift-Symbol und Grundbuch-Symbol; Tafelteil mit **Vergleichstabelle** (breite Karte, zeilenweise) und **Ergebnisbühne** mit den drei Gegenständen.

## Szenen

Alle Szenen auf Cremegrund (Tag).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Handy** `fall`–`schwester` | Nina links, drei Symbole (Handy, Auto, Haus) zum Satz „drei Dinge“; Arne kommt, Handy in seiner Hand, Blase, „150 €“; Geld wandert zu Arne, Handy zu Nina; Pillen „gehört der Schwester von Arne“, „nur geliehen“ | tabler:`device-mobile`, `car` (Blau), `cash-banknote` (Grün); ph:`house` (Gelb) | `Fall · Drei Käufe` (ab 0,0 s) → `Fall · Das Handy` → `Fall · Das Handy gehört der Schwester` | – |
| **A2 Auto** `auto`–`schwager` | Parkplatz, Gebrauchtwagen, „6.000 €“; Blase Nina (Zulassungsbescheinigung?), Blase Kuhnert, Schlüssel wandert zu Nina, Geld zu Kuhnert; Nina fährt los (Auto fährt nach links, Nina ist im Auto); Pillen Schwager | tabler:`parking`, `car`, `key` (Gelb), `cash-banknote` | `Fall · Das Auto` → `Fall · Das Auto gehört dem Schwager` | `szene_076motor_1` beim Losfahren |
| **A3 Haus** `haus`–`falsch` | Haus links, Nina, Frau Lohse; „Beim Notar“: Unterschrift-Symbol, „Kaufvertrag“, „Auflassung“; Blase Lohse; Grundbuch-Symbol „Grundbuch: Frau Lohse“, Kreuz, „gehört noch ihrem Bruder“, „Nina weiß davon nichts“ | ph:`house`; tabler:`writing-sign`, `book-2` | `Fall · Das Haus` → `Fall · Beim Notar` → `Fall · Das Grundbuch ist falsch` | `szene_076stift_1` bei „Kaufvertrag“ |
| **A4 Frage** `frage`, `frage2` | Frage-Pille, drei Gegenstände mit „Handy?“, „Auto?“, „Haus?“, Nina denkt | tabler:`device-mobile`, `car`; ph:`house` | `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig (34 px), ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Grundsätze** `grund`–`mehr` | Tafel: 1. Publizität (Besitz/Grundbuch), 2. Spezialität, 3. Abstraktion, Verweis auf die Videos; Nina | tabler:`scale`, `eye`, `hand-finger`, `link-off` | `Grundsätze des Sachenrechts` → `› Publizität` → `› Spezialität` → `› Abstraktion` | – |
| **D § 929 S. 1** `p929`–`berecht` | Wortlautkarte (3 Marker), ✓ Einigung, ✓ Übergabe, ✗ Berechtigung; Nina, Arne | tabler:`device-mobile` | `Bewegliche Sachen · § 929 S. 1 BGB` → `› Einigung` → `› Übergabe` → `› Berechtigung` | – |
| **E Übergabeersatz** `surr`–`p931` | § 929 S. 2, § 930, § 931 je zwei Zeilen; Nina | tabler:`arrows-exchange`, `hand-finger`, `home`, `file-text` | `Übergabeersatz` → `› § 929 S. 2 BGB` → `› § 930 BGB` → `› § 931 BGB` | – |
| **F § 932** `p932`, `w932`, `w932b` | Wortlautkarte Abs. 1 S. 1 und Abs. 2 (5 Marker) | tabler:`shield-check`, `eye-off` | `Gutgläubiger Erwerb · § 932 Abs. 1 S. 1 BGB` → `› guter Glaube, § 932 Abs. 2 BGB` | – |
| **G Rechtsschein** `schein`–`nina2` | § 1006, BGH-Fundstelle, ✓✓, Block „Nina ist in gutem Glauben“ | tabler:`device-mobile`, `shield-check` | `Gutgläubiger Erwerb › Rechtsschein des Besitzes` → `› guter Glaube von Nina` | – |
| **H § 935** `p935`–`nina4` | § 935 I, Ausnahme Geld, „abhandengekommen = unfreiwillig“, ✓ freiwillig verliehen, Block „Nina wird Eigentümerin des Handys“ | tabler:`lock-open` (Rot), `device-mobile` | `Ausschluss · § 935 BGB` → `› abhandengekommen?` → `Ergebnis · Handy` | – |
| **I Auto** `auto2`–`auto4` | ✓/✗/✓, „Besitz allein reicht nicht“, ZB II mit BGH-Fundstellen, ✗ grob fahrlässig, Block „Nina wird nicht Eigentümerin“; Nina, Kuhnert | tabler:`car`, `file-certificate`, `file-x` | `Das Auto · § 929 S. 1, § 932 BGB` → `› guter Glaube beim Gebrauchtwagen` → `› grob fahrlässig, § 932 Abs. 2 BGB` → `Ergebnis · Auto` | – |
| **J § 873 I, § 925** `p873`–`eintr` | Wortlautkarte § 873 I (4 Marker), Auflassung § 925, Block „Eigentum erst mit der Eintragung“; Nina, Lohse | ph:`house`; tabler:`writing-sign`, `book-2` | `Grundstücke · § 873 Abs. 1 BGB` → `› Auflassung, § 925 BGB` → `› Eintragung` | – |
| **K § 892** `p892`–`vorm` | öffentlicher Glaube, Wortlaut in Zeilen, „nur Kenntnis“, ✓, Block Ergebnis, ✗ Widerspruch, Vormerkung | tabler:`book-2`, `eye`, `ban`, `bookmark`; ph:`house` | `Grundstücke › öffentlicher Glaube, § 892 BGB` → `› nur Kenntnis schadet` → `Ergebnis · Haus` → `› Widerspruch` → `Ausblick · Vormerkung, § 883 BGB` | – |
| **L Vergleich** `vgl`–`v4` | breite Karte: Spalten bewegliche Sache / Grundstück, Zeilen Übertragung, Rechtsschein, Was schadet?, abhandengekommen – Zelle für Zelle zum Wort | Linien | `Vergleich · bewegliche Sache und Grundstück` | – |
| **M Ergebnis** `erg`–`e3` | Bühne: Handy ✓, Auto ✗, Haus ✓, Nina | tabler:`device-mobile`, `car`; ph:`house` | `Ergebnis` | – |
| **N Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Erwerb vom Nichtberechtigten` → `Klausurtipp · Grundstück: nur Kenntnis` | – |
| **O Klausurschema** `sch`–`k5` | breite Karte, I.–IV. und Block Grundstück | – | `Klausurschema` → `› Grundstück` | – |
| **P Merksatz** `merke`, `m2` | Lexi erklärt, vier Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 19 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur, wo Gegenstände die Hand wechseln (Handy, Geld, Schlüssel) und beim Losfahren des Autos.
**Blasen:** Stil C (`bausteine.blase`), wortgleich mit dem Gesprochenen, Zahlen als Ziffern („150 €“). Zahlen auf Tafeln, Pillen und Karte als Ziffern.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Nina kauft ihrem Bekannten Arne für 150 Euro sein altes Handy ab, und Arne übergibt es ihr. Das Handy gehört aber seiner Schwester, die es ihm nur geliehen hat.
>
> Auf einem Parkplatz kauft Nina von Herrn Kuhnert für 6.000 Euro einen Gebrauchtwagen. Auf ihre Frage nach der Zulassungsbescheinigung sagt er, er schicke sie nächste Woche. Nina zahlt und fährt los. Das Auto gehört dem Schwager von Herrn Kuhnert, der es ihm nur geliehen hat.
>
> Frau Lohse verkauft Nina ein kleines Haus. Beim Notar schließen beide den Kaufvertrag und erklären die Auflassung. Frau Lohse ist im Grundbuch als Eigentümerin eingetragen. Die Übertragung an sie war aber unwirksam, das Haus gehört noch ihrem Bruder. Nina weiß davon nichts; ein Widerspruch ist nicht eingetragen.
>
> **Wird Nina Eigentümerin von Handy, Auto und Haus?**
