# Folge 079 · Lederspray-Fall: Garantenstellung & Kausalität im Vorstand – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_079.py`](src/skript_079.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Strafrecht/StGB AT, Themenplan-Format „Klassiker-Fall“. Erfundener Ausgangsfall nach dem Plan-Hook („Die Geschäftsführung eines Herstellers erfährt, dass ihr Schuhpflegespray Atemnot auslöst, und beschließt einstimmig, es im Handel zu lassen“), danach der echte Fall korrekt eingeordnet (BGH, Urt. v. 6.7.1990 – 2 StR 549/89, BGHSt 37, 106). **Zurückhaltend:** keine erkrankten Menschen, kein Röcheln; Atemnot nur als Symbol (Tabler `lungs`, `alert-triangle`, `building-hospital`), Sitzungstisch, Spraydose (Tabler `spray`) ohne Marke, kein reales Unternehmen. Ablauf: Fall → Frage → Sachverhalt → echter Fall → Vorab Tun/Unterlassen → Wortlautkarte § 13 Abs. 1 → 1. Erfolg und Ursächlichkeit → 2. Garantenstellung (Ingerenz) → Rückrufpflicht → Handlungspflicht des Einzelnen → 3. Quasikausalität und Einwand → Wortlautkarte § 25 Abs. 2 (Mittäterschaft) → Fahrlässigkeit: Teilbeitrag → 4. Vorsatz/Fahrlässigkeit → Wortlautkarte § 224 Abs. 1 → Ergebnis → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 6:52,5.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Eberhard, um 60 | Geschäftsführer, dominant („Ein Rückruf kostet uns ein Vermögen.“) | `standing/pointing_finger-2` (schwarzer Pullover, Hose Marine `#4A5A85`), Kopf `No Hair 3`, Brille `Glasses 2`, Haut `#E2B08C`, ohne Bart. Mimiken `Calm`, `Serious` (redet, ernst), `Suspicious`, `Solemn` | `helmut` (Mann, älter) |
| Almut, um 50 | Geschäftsführerin („Dann bleibt das Spray im Handel …“) | `standing/blazer-3` (Blazer Lila `#B8A9F5`, Hose `#3B3B4F`), Kopf `Medium Bangs 3`, Haut `#F0C8A8`. Mimiken `Calm` (ruhig, redet), `Serious`, `Solemn`, `Concerned\|Serious` | `julia` (Frau, jung; ruhige, sachliche Stimme) |
| Hauke, um 35 | Geschäftsführer, Einwand „Meine Stimme hätte nichts geändert.“ | `standing/blazer-4` (Blazer Blau `#8DB3F2`, Oberteil Weiß), Kopf `Short 2`, Haut `#E8BE9A`. Mimiken `Calm`, `Concerned\|Serious` (Sorge, redet), `Serious`, `Solemn`, `Suspicious` (Zweifel) | `niklas` (Mann, jung) |
| Laborleiterin, um 40 | berichtet in der Sondersitzung (ohne Namen, Namensschild „Laborleiterin“) | `standing/doctor-nurse-02` (Laborkittel), Kopf `Long`, Haut `#C68A62`. Mimik `Serious` | `ela_froh` (Frau, jung) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |
| Beteiligte des echten Falls | Geschäftsführer, Kunden | **keine Figuren**, nur Symbole (Fabrik, Kalender, Hammer) und Tafelzeilen | – |

- **Keine Prothesen-Posen für die Täterrollen** (`blazer-1/-2`, `shirt-1/-2` deshalb verworfen). Sachlich, keine Dämonisierung: keine bösen Mimiken.
- **Blickrichtung:** Alle Posen blicken im Original nach rechts (Kontaktbild `figuren_kontaktbogen.png`); Grundansicht gespiegelt (blickt nach links: am Sitzungstisch zur Laborleiterin und Meldungstafel, in den Tafelszenen zur Tafel), `_r` nach rechts (nicht benötigt).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `EB_redet`, `AL_redet`, `HA_redet`, `LL_redet` (je beide Blickrichtungen) und Lexi. 70 Figuren-PNGs in `../peeps/op_079/` (nicht im Repository, im Drive-Master).
- **Stimmen** nur aus dem zugeteilten Pool (niklas, helmut, ela_froh, julia – alle vier verwendet, je eine Figur). 077 sprach stephan/lucy/hilde, 078 eine andere Besetzung; 076 nutzte denselben Pool (unvermeidbar, Pool vorgegeben).
- **Namen** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste und in keiner Datei unter `youtube/` (Volltextsuche `grep -rlw`): Eberhard, Almut, Hauke. Kein Genitiv eines Namens („der Einwand von Hauke“).

**Abweichung von den letzten Folgen:** 071 Garten mit Teich, 077 Polizeirecht, 070 Küche/Mineralbrunnen. 079: **Sitzungsraum einer Firma** (Sitzungstisch mit Namensschildern, Meldungstafel) – neuer Schauplatz; Posen `pointing_finger-2`, `blazer-3`, `doctor-nurse-02` in 070–077 nicht verwendet, `blazer-4` (074, 076) mit neuem Kopf und neuen Farben. Tageslicht auf Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Sondersitzung** `fall`→`frage2` | Bodenlinie; rechts Sitzungstisch (Grundformen `karte`) mit Eberhard, Almut, Hauke und Namensschildern ab 0,0 s; links zuerst Schuh, Spray, Telefon, Lunge/Warnzeichen, Klinik; ab „Sondersitzung“ Meldungstafel und Laborleiterin | tabler: `shoe` (Holz), `spray` (Blau), `phone-call`, `lungs` (Hellrot), `alert-triangle` (Gelb), `building-hospital`, `coins` (Gelb), `thumb-up` (Gelb), `building-store` | `Fall · Die Schuhpflege-Firma` (ab 0,0 s) → `· Meldungen: Atemnot` → `· Die Sondersitzung` → `· Kein Rückruf` → `· Weitere Kunden erkranken` → `· Der Einwand von Hauke` → `· Die Frage` | Grundbild · Spray · Telefon · Atemnot · Klinik · Meldungstafel + Laborleiterin · „Geschäftsführung“ · Laborleiterin redet · Eberhard redet · Münzen · Almut redet · Daumen hoch, „einstimmig: kein Rückruf“ · „in Kauf genommen“ · Hauke besorgt, „weitere Kunden“, Laden · Hauke redet · Fragen | Sprühstoß (`szene_079spray_1`, Freesound CC0 738895), Telefon klingelt (`szene_079telefon_1`, CC0 509742) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **C Der echte Fall** `bgh`→`bgh4` | Tafel, rechts nur Symbole | tabler: `building-factory-2`, `calendar`, `gavel` | `Der echte Fall · Lederspray, BGHSt 37, 106` → `› Verurteilungen bestätigt` | Zeile für Zeile, Haken, grüner Block | – |
| **D Tun/Unterlassen** `tun`→`unterl2` | Tafel, blauer/lila Kasten, gelber Block; Eberhard und Almut | tabler: `shopping-cart`, `truck-return` | `Vorab · Tun oder Unterlassen?` → `› Verkauf nach der Sitzung: Tun` → `› Dosen im Laden: unterlassener Rückruf` → `A. Gefährliche Körperverletzung durch Unterlassen` | 6 | – |
| **E § 13 Abs. 1** `p13`→`entspr2` | **Wortlautkarte § 13 Abs. 1** (Marker „einen Erfolg abzuwenden“, „rechtlich dafür einzustehen hat“, „durch ein Tun entspricht“); Hauke | tabler: `shield`, `scale` | `A. … › § 13 Abs. 1 StGB` → `› § 13: Garantenstellung` → `› § 13: Entsprechung` | Karte, Marker, Zeilen, Haken | – |
| **F 1. Erfolg/Ursächlichkeit** `erfolg`→`kaus3` | Tafel, gelber Block; Laborleiterin | tabler: `lungs`, `flask`, `microscope` | `› 1. Erfolg, § 223 StGB` → `› 1. Ursächlichkeit des Sprays` → `› 1. andere Ursachen ausgeschlossen` | Zeilen, Haken, Block | – |
| **G 2. Garantenstellung** `garant`→`zivil` | Tafel, lila Kasten „offen gelassen“; Eberhard | tabler: `spray` | `› 2. Garantenstellung: Ingerenz` → `› 2. objektiv pflichtwidrig` → `› 2. offen: Produktbeobachtung` | Zeilen, Haken, Kasten | – |
| **H Rückrufpflicht** `rueck`→`gesamt` | Tafel, grüner Kasten Krise; Eberhard und Hauke | tabler: `truck-return`, `alert-triangle`, `coins`, `users-group` | `› 2. Pflicht zum Rückruf` → `› 2. Kosten treten zurück` → `› 2. Krise: jeder Geschäftsführer` | Haken/Kreuz am Wort | – |
| **I Einzelner** `einzel`→`keiner` | Tafel, gelber Block; Almut | tabler: `hand-stop`, `truck-return` | `› 2. Was schuldet der Einzelne?` → `› 2. alles Mögliche und Zumutbare` | Kreuz, Block, Kreuz | – |
| **J 3. Quasikausalität** `quasi`→`mitt` | Tafel, gelber und grüner Block; Hauke (zweifelnd) | tabler: `truck-return`, `hand-stop`, `users-group` | `› 3. Quasikausalität` → `› 3. Einwand: meine Stimme` → `› 3. Lösung: Mittäterschaft` | Zeilen, Haken, Block | – |
| **K § 25 Abs. 2** `p25`→`zurech` | **Wortlautkarte § 25 Abs. 2** (Marker „gemeinschaftlich“, „jeder als Täter“); alle drei Geschäftsführer | – | `› 3. Mittäterschaft, § 25 Abs. 2 StGB` → `› 3. Mittäterschaft beim Unterlassen` → `› 3. Zurechnung: Unterlassen aller` | Karte, Zeilen, Haken | – |
| **L Fahrlässigkeit** `fahr`, `frei` | hell-lila Tafel; Almut und Hauke | tabler: `users-group` | `› 3. bei Fahrlässigkeit: Teilbeitrag` → `› 3. Entlastung nur bei vollem Einsatz` | Zeilen, Block | – |
| **M 4. Vorsatz** `vorsatz`, `vorher` | Tafel mit rotem (ab der Sitzung) und blauem Kasten (davor); Eberhard | tabler: `calendar` | `› 4. Vorsatz ab der Sitzung` → `Vor der Sitzung › fahrlässige Körperverletzung, § 229 StGB` | Kästen, Zeile | – |
| **N § 224 Abs. 1** `p224`→`rw` | **Wortlautkarte § 224 Abs. 1** (Nr. 1 und Nr. 5, Rest „…“; Marker Nr. 5 bei „mittels“, Nr. 1 bei „Beibringung“); Almut | tabler: `lungs`, `scale` | `› Qualifikation: § 224 Abs. 1 Nr. 5 StGB` → `› nach dem Wortlaut auch Nr. 1` → `› Rechtswidrigkeit und Schuld` | Karte, Marker, Haken | – |
| **O Ergebnis** `erg`, `erg2` | Tafel, grüner Block; alle drei | tabler: `gavel` | `Ergebnis · gefährliche Körperverletzung durch Unterlassen in Mittäterschaft` → `Ergebnis › Verkauf nach der Sitzung: Tun` | Block, Zeile | – |
| **P Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (2 Stände) | Zeile für Zeile | – |
| **Q Prüfschema** `sch`→`s3` | breite Karte: Vorab; I. 1. a)–f), 2.; II.; III. | – | `Prüfschema` → je Gliederungspunkt ein Pfadstand | 12 Aufbaustufen | – |
| **R Merksatz** `merke`→`m3` | Lexi erklärt (redet), drei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Stil C (`bausteine.blase`), Schwanzspitze außerhalb der Blase am Mund; wortgleich mit dem Gesprochenen. **Zahlen** auf Tafeln, Pillen und Karte als Ziffern („6.7.1990“, „Mai 1981“, „2 Jahre“, „3 Geschäftsführer“, „§ 224 Abs. 1 Nr. 5“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; keine Bewegung.
**Geräusche:** zwei Handlungsgeräusche (Sprühstoß beim Erscheinen der Spraydose, Telefonklingeln beim Erscheinen des klingelnden Telefons), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Tisch und Meldungstafel aus Grundformen (`karte`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Eine Firma stellt Pflegemittel für Schuhe her. Seit dem Herbst melden Kunden, dass sie nach dem Sprühen des Imprägniersprays Atemnot bekommen; einige kommen ins Krankenhaus, manche auf die Intensivstation. Schon vor der Sondersitzung erkranken nach den ersten Meldungen weitere Kunden; die Gefahr hätte die Geschäftsführung da bereits erkennen können.
>
> In der Sitzung berichtet die Laborleiterin: Einen Giftstoff findet das Labor nicht, andere Ursachen scheiden aus. Die 3 Geschäftsführer Eberhard, Almut und Hauke beschließen einstimmig, das Spray im Handel zu lassen und nur einen Warnhinweis aufzudrucken. Weitere Erkrankungen halten sie für möglich und nehmen sie in Kauf. Ein sofortiger Rückruf hätte die Läden rechtzeitig erreicht. In den folgenden Monaten bekommen weitere Kunden Atemnot, mit Dosen, die schon vor der Sitzung in den Läden standen. Hauke meint, seine Stimme hätte nichts geändert.
>
> **Haben sich Eberhard, Almut und Hauke strafbar gemacht?**
