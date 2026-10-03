# Folge 106 · Laptop für Kanzlei und Netflix: Der Verbraucherbegriff (§ 13 BGB) – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_106.py`](src/skript_106.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/Schuldrecht AT, Themenplan-Format „Abgrenzung“. Fiktiver Fall nach dem Plan-Hook („Die Anwältin kauft einen Laptop – für die Kanzlei und abends für Netflix“): Rechtsanwältin Ricarda (eigene Kanzlei) bestellt im Mai online bei Herrn Kortmann (Elektronikhandel im Internet) einen Laptop für 1.200 € über ihr privates Kundenkonto, Rechnung an die Wohnung, Lieferung an die Kanzlei. Nutzung 40 % Kanzlei, 60 % privat. Eine Woche nach der Lieferung widerruft sie per E-Mail; Herr Kortmann lehnt ab.

Ablauf: Fall (Bestellung, Lieferung/Nutzung, Widerruf) → Frage → Sachverhalt → Rechtsfolge, an der es hängt (Widerrufsrecht § 312g Abs. 1, § 355 BGB) → § 13 BGB (Wortlautkarte, Merkmale) → § 14 Abs. 1 BGB (Wortlautkarte; Anwältin: freier Beruf, aber selbständig beruflich) → Dual Use (Waage: „überwiegend“ seit 13.6.2014, Gegenfall 60 % Kanzlei) → strengere EuGH-Linie Gruber → objektiver Zweck und erkennbare Umstände (BGH) → Lampenfall und Ricarda (Zweispalter) → Ergebnis → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 5:06,9 (4.402 Zeichen Sprechtext); innerhalb der Regel von rund fünf Minuten.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Ricarda (RI), um 55 | Rechtsanwältin mit eigener Kanzlei, Käuferin | `standing/blazer-4` (lila Blazer `#B8A9F5`, weißes Oberteil, schwarze Hose, weiße Schuhe), Kopf `Gray Medium` (Haar `#BDBDC6`), Brille `Glasses 3`, Haut `#EBC2A0`; Mimiken `Calm`, `Serious` (redet), `Smile Big\|Smile`, `Concerned\|Serious`, `Suspicious`, `Awe` (staunt über die Ablehnung) | `hilde` (Frau, älter) |
| Herr Kortmann (KO), um 40 | betreibt einen Elektronikhandel im Internet, Unternehmer | `standing/crossed_arms-2` (schwarzer Pullover, verschränkte Arme, braune Hose `#9A7B5B`), Kopf `Short 4`, Haut `#E3AE88`; `Calm`, `Serious` (redet), `Smile Big\|Smile`, `Concerned\|Serious`, `Suspicious` | `christian` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit deutscher Aussprache, in keiner früheren Folge als Figur vergeben (geprüft per `grep -rlw` im ganzen `youtube/`-Ordner und gegen die Koordinatorliste): Ricarda, Kortmann. „Henrike“ verworfen (zu nah an „Henrik“). Kein Genitiv eines Namens im Sprechtext.
- **Stimmen nur aus dem Pool:** `hilde` (Ricarda), `christian` (Herr Kortmann); `stephan` nicht eingesetzt (klingt wie `christian`), `lucy` nicht gebraucht. Vorfolgen 103 (lucy/stephan), 104 (helmut/niklas/julia), 105 (sabrina/marc/laura_ruhig): keine Überschneidung.
- Präfixe `RI_`/`KO_` (nie `ER_`).
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Bestellung: Ricarda (rechts) blickt zum Bildschirm links. Lieferung/Nutzung: Ricarda in der Mitte blickt zur Kanzlei (links), bei „privat“ zum Wohnzimmer (rechts). Widerruf: Ricarda (links) blickt nach rechts zu Herrn Kortmann, er nach links zu ihr. Tafelszenen: beide blicken nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `RI_redet`, `KO_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur. Keine weiteren Menschen im Bild (die Rechtsanwältin des Lampenfalls nur als Tafeltext, nicht als Figur).
- **Abwechslung:** Posen, Kleidung und Muster nicht aus 103 (`easing-1`, `pointing_finger-2`), 104 (bisher nur Skript, keine Figuren) und 105 (`resting-1`, `walking-2`, `blazer-2`); keine Polka Dots.
- Figuren-PNGs: `../peeps/op_106/` (42 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 103 (Tischlerei/Rechnung), 104 (Mittäterschaft), 105 (Gebührenbescheid/Verwaltungsgericht). Hier neu: Bildschirm eines Online-Shops, Kanzlei mit Schreibtisch und Aktentasche neben einem Wohnzimmer mit Sessel, Lager mit Paketen; Balkenwaage für die Dual-Use-Abgrenzung; Zweispalter Lampenfall/Ricarda. Cremegrund durchgehend, Tageslicht. **Kein Streaming-Logo:** „Netflix“ nur einmal im Sprechtext (Hook), im Bild nur das neutrale Film-Icon `tabler:movie`.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Bestellung** `fall`–`konto` | ab 0,0 s Pille „Ricarda kauft einen Laptop“, Laptop, Ricarda; Aktentasche „Kanzlei“, Film-Icon „abends“, Kalender „Mai“; Bildschirm „Online-Shop Kortmann · Elektronik“ mit „Jetzt bestellen“ (Klick bei „bestellt“), „Laptop · 1.200 €“, „Kundenkonto: privat“, „Rechnung an: Wohnung“ | tabler:`device-laptop` (Blau), `briefcase` (Gelb), `movie` (Lila), `calendar-event`, `pointer`, `user` (Lila), `home` (Gelb) | `Fall · Die Bestellung` (ab 0,0 s) | `szene_106klick_1` bei „bestellt“ |
| **A2 Lieferung/Nutzung** `liefer`–`privat` | Kanzlei links (Schreibtisch, Aktentasche, Schild „Kanzlei“), Paket auf dem Tisch, „tagsüber dort“; dann Laptop auf dem Tisch, „40 % Kanzlei“; Wohnzimmer rechts: Sessel, „60 % privat“, Film-, Foto-, Flugzeug-Icon zu „Filme, Fotos, Urlaubsplanung“ | tabler:`desk` (Gelb), `briefcase`, `package` (Gelb), `sun`, `device-laptop`, `armchair` (Lila), `movie`, `photo`, `plane` | `Fall · Die Lieferung` → `Fall · Die Nutzung` | `szene_106paket_1` bei „Kanzlei“ |
| **A3 Widerruf/Frage** `woche`–`frage2` | „1 Woche nach der Lieferung“, Laptop am Schreibtisch „Display gefällt nicht mehr“, E-Mail; Herr Kortmann im Lager (Pakete); Blasen Ricarda „Ich widerrufe den Kaufvertrag.“, Kortmann „Sie sind Anwältin, und geliefert wurde / an Ihre Kanzlei. Für Unternehmer / gibt es kein Widerrufsrecht.“, Ricarda „Ich nutze den Laptop aber / überwiegend privat.“; Pillen „Ist Ricarda Verbraucherin?“, „Daran hängt ihr Widerrufsrecht.“ | tabler:`desk`, `device-laptop`, `mail`, `packages` (Gelb) | `Fall · Der Widerruf` → `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig (36 px), ohne Fiktiv-Hinweis, ≈ 9,5 s | – | `Sachverhalt` | – |
| **C Widerrufsrecht** `wr`–`offen` | § 312g Abs. 1, § 312c; ✓ online bestellt, ✓ Kortmann Unternehmer; Frist 14 Tage ab Erhalt; ✓ rechtzeitig; Block „Offen: Ist Ricarda Verbraucherin?“ | tabler:`arrow-back-up`, `calendar-event`, `question-mark` | `Rechtsfolge · Widerrufsrecht, § 312g Abs. 1 BGB` → `Rechtsfolge · hängt an § 13 BGB` | – |
| **D § 13 BGB** `w13`–`mz` | Wortlautkarte § 13 (5 Marker), ✓ natürliche Person, ✓ Rechtsgeschäft, Block „3. Entscheidend ist der Zweck“ | tabler:`user`, `user-check`, `receipt`, `question-mark` | `Abgrenzung › Verbraucher, § 13 BGB` | – |
| **E § 14 Abs. 1 BGB** `w14`–`rolle` | Wortlautkarte § 14 Abs. 1 (5 Marker), ✗ kein Gewerbe (§ 2 BRAO), ✓ selbständig beruflich, Block „Nicht der Beruf entscheidet, sondern der Zweck des Geschäfts“ | tabler:`building-store`, `briefcase`, `id-badge`, `question-mark` | `Abgrenzung › Unternehmer, § 14 Abs. 1 BGB` → `Unternehmer › Anwältin: freier Beruf` | – |
| **F Dual Use** `dual`–`gegen` | Waage im Gleichgewicht (Kanzlei/privat) → kippt zu „privat 60 %“ → Gegenfall kippt zu „Kanzlei 60 %“; „seit 13.6.2014 … „überwiegend““, BT-Drs. 17/13951, ErwG 17; ✓ Ricarda 60 % privat; Gegenfall | gezeichnete Waage (`waage()`), tabler:`scale`, `user-check`, `briefcase` | `Abgrenzung › Dual Use: überwiegender Zweck` → `Dual Use › Gegenfall: 60 % Kanzlei` | – |
| **G Gruber** `gruber`, `nat` | Urteil Gruber (C-464/01, Rn. 39, 41, 54), ✗ Überwiegen genügt nicht, ganz untergeordnet; Block „§ 13 BGB: Es zählt das Überwiegen“ | tabler:`gavel`, `scale` | `Dual Use › strengere EuGH-Linie (Gruber)` → `Dual Use › § 13 BGB: das Überwiegen zählt` | – |
| **H Erkennbare Umstände** `erk`–`eind` | objektiver Zweck (VIII ZR 191/19 Rn. 16), im Zweifel Verbraucher (VIII ZR 7/09 Rn. 10 f.), Block „Anders nur bei eindeutigen …“ (VIII ZR 49/19 Rn. 84) | tabler:`question-mark`, `user-check`, `eye` | `Abgrenzung › erkennbare Umstände` | – |
| **I Lampenfall/Ricarda** `lampe`–`bew` | Zweispalter: Lampenfall (Rechtsanwältin, Lampen für die Wohnung, Lieferung an die Kanzlei, ✓ Verbraucherin) │ Ricarda (Lieferadresse Kanzlei, Kundenkonto privat, Rechnung Wohnung, ✗ nicht eindeutig); Beweislast (Rn. 11) | tabler:`lamp`, `user-check`, `truck-delivery`, `scale` | `Erkennbare Umstände › Lampenfall, BGH VIII ZR 7/09` → `Erkennbare Umstände › Ricarda` | – |
| **J Ergebnis** `erg`–`erg3` | Block „Ricarda ist Verbraucherin, ihr Widerruf ist wirksam“, Rückgewähr 14 Tage, ✓ Laptop, ✓ 1.200 € | tabler:`user-check`, `package`, `cash` | `Ergebnis · Ricarda ist Verbraucherin` | – |
| **K Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Kanzleiadresse allein reicht nicht` | – |
| **L Klausurschema** `sch`–`k5` | breite Karte, I.–IV. Zeile für Zeile mit Untermerkmalen, dann „Scheitert die Verbrauchereigenschaft: Unternehmer nach § 14 BGB prüfen“ | – | `Klausurschema` → `› III. Zweck` → `› IV. erkennbare Umstände` → `› sonst Unternehmer, § 14 BGB` | – |
| **M Merksatz** `merke`, `mz2` | Lexi erklärt, zwei Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; keine Bewegung, kein Zoom.
**Blasen:** Stil C (`bausteine.blase`), wortgleich mit dem Gesprochenen. Zahlen auf Tafeln, Pillen und Karte als Ziffern.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Rechtsanwältin Ricarda hat eine eigene Kanzlei. Im Mai 2026 bestellt sie online bei Herrn Kortmann, der einen Elektronikhandel im Internet betreibt, einen Laptop für 1.200 Euro: über ihr privates Kundenkonto, Rechnung an ihre Wohnung, Lieferung an die Kanzlei, weil sie tagsüber dort ist.
>
> Ricarda nutzt den Laptop zu 40 % für die Kanzlei und zu 60 % privat (Filme, Fotos, Urlaubsplanung).
>
> Eine Woche nach der Lieferung widerruft sie den Kaufvertrag per E-Mail. Herr Kortmann lehnt ab: Sie sei Anwältin, geliefert worden sei an die Kanzlei, und für Unternehmer gebe es kein Widerrufsrecht.
>
> **Ist Ricarda Verbraucherin und kann sie widerrufen?**
