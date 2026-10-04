# Folge 155 · Schwere Körperverletzung § 226 & Todesfolge § 227 StGB – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_155.py`](src/skript_155.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · StGB BT, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Ein Faustschlag, ein Sturz, ein verlorenes Auge – oder sogar der Tod: Was ändert die schwere Folge?“): Roswitha schlägt Ludger vor einer Bar im Streit um ein Taxi mit der Faust ins Gesicht, Ludger stürzt rückwärts auf das Pflaster. Variante A: dauerhafter Verlust des Sehvermögens auf dem linken Auge; Variante B: Tod durch den Aufprall des Kopfes. Ablauf: Fall → Varianten → Frage → Sachverhalt → Grunddelikt § 223 (Verweis 038) und Erfolgsqualifikation → Wortlautkarte § 18 → Wortlautkarte § 226 Abs. 1 (Nr. 1–3) → Variante A (Nr. 1, Nr. 2/3 (−), Fahrlässigkeit, Abs. 2) → Wortlautkarte § 227 Abs. 1, Kausalität genügt nicht → spezifischer Gefahrzusammenhang: Letalitätstheorie vs. BGH (Handlung), Wortlautargument → versuchte KV mit Todesfolge, Gubener Hetzjagd, älteres Urteil „zu restriktiv“ → Lösung Variante B, Vorhersehbarkeit, § 227 Abs. 2 → Abgrenzung §§ 212, 222 (Verweis 035) → Klausurtipp → Prüfungsschema → Merksatz. Hauptfilm 6:41,6.
**Verhältnis zu den Vorfolgen:** 038 (§ 223) und 035 (Tötungsdelikte im Überblick) werden nur verwiesen, nicht wiederholt; 124 als Muster für zurückhaltende Gewaltdarstellung (Folge nur als Text, Figur ruhig, keine Verletzungsdetails).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Roswitha, um 45 | schlägt Ludger mit der Faust ins Gesicht (Verletzungsvorsatz) | `standing/blazer-4` (Blazer Lila `#B8A9F5`, weißes Oberteil, schwarze Hose, weiße Schuhe), Kopf `Medium 3` (Haar `#4A3222`), Haut `#E0AC86`, keine Brille, kein Bart. Mimiken `Calm` (nur zu Beginn), `Serious` (redet; ernst), `Suspicious` (denkt), `Fear` (Schreck nach dem Sturz), `Solemn`, `Concerned|Serious` | `sabrina` (Frau, mittel) |
| Ludger, um 50 | Opfer | stehend `standing/walking-3` (schwarzes T-Shirt, schwarze Hose, weiße Schuhe), Kopf `Short 3` (Haar `#6B5440`), Haut `#F0C8A8`; nach dem Sturz `sitting/hands_back-1` mit gleicher Kleidung (Hose `#2B2B2B`), Mimik `Tired` (benommen) – keine Verletzungsdetails, kein Liegen. Stehend `Calm`, `Serious` (redet), `Solemn`, `Concerned|Serious` | `marc` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Blickrichtung:** Alle Posen blicken im Original nach rechts (Kontaktbild `besetzung_155.png`); Grundansicht gespiegelt (nach links, zur Tafel), `_r` nach rechts. Fallszene: Roswitha (links) blickt nach rechts zu Ludger, Ludger blickt nach links zu ihr; das Taxi hält rechts. Tafelszenen: alle Figuren rechts, blicken nach links. **Roswitha sachlich:** keine bösen Mimiken (kein Contempt, Angry, Rage), in den Tafelszenen ernst statt lächelnd. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `RO_redet`, `LU_redet` (je links/rechts) und Lexi. **Stimmen** nur aus dem Pool (sabrina, marc; william und laura_ruhig nicht benötigt); Vorfolgen 152 (laura_ruhig, william), 153 (niklas, helmut), 154 (lucy, christian): keine Überschneidung. Lea nicht verwendet. **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keinem Skript, Szenenplan oder Abnahmebogen unter `youtube/preproduction/` (Volltextsuche 04.10.2026; „Wilhelm“ verworfen, in 150 vorhanden): Roswitha, Ludger. Figuren-PNGs: `../peeps/op_155/` (46 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 150 (`shirt-3`, `blazer-3`), 151 (`easing-1`, `shirt-4`), 152 (`walking-1`, `shirt-4`), 153 (`easing-1`, `resting-2`, `resting-1`; Konditorei). 155: **Gehweg vor einer Bar am Abend** (Fassade mit Schild „Bar“, Fenster, Tür, Pflaster, Mond, Taxi) – neuer Schauplatz; Posen `blazer-4`, `walking-3`, `sitting/hands_back-1` in diesen Folgen nicht verwendet; keine Polka Dots, keine Prothesen-Posen, keine Bärte. **Abend** nur über Mond und Text, Cremegrund (kein Nachtverlauf nötig).

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Vor der Bar** `fall`→`sturz` | Fassade, Pflaster, Mond; Taxi fährt von rechts vor; Roswitha und Ludger; Blasen; Faustschlag nur als Pille; Ludger sitzt danach benommen auf dem Pflaster, Warnsymbol | tabler:`car` (Gelb) mit Taxischild, `glass-cocktail` (Pink), `alert-triangle` (Gelb); `bar()`, `pflaster()`, `taxischild()`, `mond()` programmatisch | `Fall · Vor der Bar` (ab 0,0 s) → `Fall · Das Taxi` → `Fall · Der Faustschlag` → `Fall · Der Sturz` | Bar ab 0,0 s · Taxi, beide Figuren · „beide wollen in dasselbe Taxi“ · Ludger redet · Roswitha redet · „Faustschlag ins Gesicht“ · „will verletzen, mehr nicht“ · Ludger sitzt, „stürzt rückwärts“ · Warnsymbol | Taxi fährt vor (`szene_155taxi_1`, Freesound CC0 508901) |
| **A2 Die Varianten** `va`→`frage2` | Tafel: Variante A (Pille „Sehvermögen auf einem Auge verloren“), Variante B (Pille „Ludger stirbt an dieser Kopfverletzung.“, nur Text), „nicht gerechnet“, Fragepillen; Roswitha rechts | tabler:`eye` (kein durchgestrichenes Auge), `help-circle`, `scale` | `Fall · Variante A` → `Fall · Variante B` → `Fall · Die Frage` | Zeile für Zeile | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C1 Grunddelikt** `grund`→`formel` | Tafel; Haken; gelber Block „Grunddelikt + schwere Folge“ | tabler:`alert-triangle`, `plus` | `Grunddelikt · § 223 StGB` → `Erfolgsqualifizierte Delikte · §§ 226, 227 StGB` | Zeile für Zeile | – |
| **C2 § 18** `p18`→`vf` | **Wortlautkarte § 18** (vollständig, vier Marker), zwei Blöcke | tabler:`book`, `scale` | `Erfolgsqualifikation › § 18 StGB: wenigstens Fahrlässigkeit` | Karte + Marker, Blöcke | – |
| **D § 226 Abs. 1** `p226`→`rahmen1` | **Wortlautkarte § 226 Abs. 1** (Nr. 1–3 vollständig), Marker je Nummer und Strafrahmen | tabler:`book`, `eye`, `hand-stop`, `alert-triangle`, `scale` | `Variante A › § 226 Abs. 1 StGB` → `› Nr. 1` → `› Nr. 2` → `› Nr. 3` → `› Strafrahmen` | Karte + 6 Marker, Pillen | – |
| **E Variante A** `sub_a`→`abs2` | Tafel; Haken/Kreuz; grüner Ergebnisblock; Abs. 2; Roswitha und Ludger rechts | tabler:`eye`, `bulb`, `gavel` | `Variante A › Nr. 1: Sehvermögen auf einem Auge` → `› Nr. 2 und 3 (−)` → `› Fahrlässigkeit, § 18 StGB` → `› Ergebnis: § 226 Abs. 1 Nr. 1 StGB` → `Abgrenzung · § 226 Abs. 2 StGB: absichtlich oder wissentlich` | Zeile für Zeile | – |
| **F § 227 Abs. 1** `p227`→`nurk` | **Wortlautkarte § 227 Abs. 1**, Marker; Haken Kausalität, Kreuz „reicht nicht“ | tabler:`book`, `link`, `help-circle` | `Variante B › § 227 Abs. 1 StGB` → `› Kausalität` → `› Kausalität genügt nicht` | Karte + 3 Marker, Zeilen | – |
| **G1 Gefahrzusammenhang** `spez`→`arg` | lila Formelblock; zwei Spalten Letalitätstheorie / BGH | tabler:`alert-triangle`, `arrows-split`, `scale` | `Variante B › spezifischer Gefahrzusammenhang` → `› Streit: Erfolg oder Handlung?` → `› Letalitätstheorie` → `› BGH: auch die Handlung` | Block, Spalte für Spalte | – |
| **G2 Flucht des Opfers** `guben`→`aelter` | gelber Block „versuchte KV mit Todesfolge möglich“; Gubener Hetzjagd nur als Text mit Fundstelle (keine Darstellung der Beteiligten); älteres Urteil | tabler:`book`, `link`, `calendar-event` | `› versuchte Körperverletzung mit Todesfolge` → `› Flucht des Opfers` → `› älteres Urteil: zu restriktiv` | Zeile für Zeile | – |
| **H Lösung B** `sub_b`→`msf` | Tafel; Haken; grüner Ergebnisblock; Abs. 2 | tabler:`alert-triangle`, `bulb`, `gavel`, `scale` | `Variante B › Gefahrzusammenhang im Fall` → `› Fahrlässigkeit, § 18 StGB` → `› Ergebnis: § 227 Abs. 1 StGB` → `› minder schwerer Fall, § 227 Abs. 2 StGB` | Zeile für Zeile | – |
| **I Abgrenzung** `abgr`→`v035` | zwei Blöcke §§ 212, 222; Verweis | tabler:`arrows-split` | `Abgrenzung · § 212 StGB` → `Abgrenzung · § 222 StGB` | 3 | – |
| **J Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (3 Stände) | Zeile für Zeile | – |
| **K Prüfungsschema** `sch`→`s226` | breite Karte, progressiv, grüner Kasten Gefahrzusammenhang, gelber Block § 226 | – | `Prüfungsschema` → je Gliederungspunkt | 10 Aufbaustufen | – |
| **L Merksatz** `merke`→`m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Sprechblasen Stil C (Standard seit 02.10.2026, `bausteine.blase`, stiller Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („§ 226 Abs. 1 Nr. 1 StGB“, „1 bis 10 Jahre“, „nicht unter 3 Jahren“; Wortlautkarten in amtlicher Schreibung).
**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; Bewegung nur: Taxi fährt vor (1,8 s).
**Geräusche:** ein Handlungsgeräusch (Taxi fährt vor), Freesound CC0, Herkunft in `geraeusche_herkunft.json`. Kein Schlag- oder Aufprallgeräusch.
**Darstellung (Vorgabe):** kein Schlag im Bild, kein Blut, keine Verletzungen, keine Leiche, kein Krankenhausbett; Folgen nur als Text/neutrale Icons (offenes Auge-Icon, kein durchgestrichenes Auge), Tod nur als Text, kein Kreuz/Grab; Täterin und Opfer fiktive Erwachsene in Alltagskleidung, kein Milieu-Klischee.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Fassade, Pflaster, Taxischild aus Grundformen (`bar()`, `pflaster()`, `taxischild()` in `folien_155.py`), Mond aus `ostil.mond()`.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Ein Freitagabend vor einer Bar in der Altstadt. Roswitha und Ludger wollen beide in dasselbe Taxi steigen. Ludger: „Das Taxi habe ich bestellt!“ Roswitha: „Ich war aber zuerst hier.“
>
> Roswitha schlägt Ludger mit der Faust ins Gesicht. Sie will ihn verletzen, mehr nicht. Ludger stürzt rückwärts auf das Pflaster.
>
> Variante A: Durch den Schlag verliert Ludger dauerhaft das Sehvermögen auf dem linken Auge; äußerlich ist er nicht entstellt. Variante B: Beim Sturz schlägt sein Kopf auf das Pflaster, und Ludger stirbt an dieser Kopfverletzung. Mit beidem hat Roswitha nicht gerechnet.
>
> **Wie hat sich Roswitha strafbar gemacht?**
