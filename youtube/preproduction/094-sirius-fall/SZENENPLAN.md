# Folge 094 · Sirius-Fall: Zur Selbsttötung überredet – mittelbare Täterschaft? – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_094.py`](src/skript_094.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Strafrecht/StGB AT, Themenplan-Format „Klassiker-Fall“. Ein **fiktiver Fall** nach dem Vorbild von BGHSt 32, 38 (Sirius-Fall), abgewandelt; der echte Fall wird nur kurz eingeordnet (Stern Sirius, neuer Körper, Lebensversicherung, überlebt, versuchter Mord aus Habgier bestätigt), ohne Methode, ohne Namen, ohne Figuren. **Höchste Zurückhaltung (Thema Suizid):** keine Methode in Bild, Ton, Tafeln, Sachverhaltskarte oder Beschreibung (kein Sprung, keine Badewanne, kein Föhn), keine Verletzung, keine Musik, keine Verspottung der Getäuschten (ruhige Mimiken, kein „leichtgläubig“, kein Kristallball, keine Esoterik-Karikatur). Wilma bleibt unverletzt. Am Ende eine ruhige Tafel mit dem Hilfsangebot der TelefonSeelsorge (Nummern verifiziert). Ablauf: Fall → Frage → Sachverhalt → echter Fall → Ausgangspunkt (Straflosigkeit, Akzessorietät, § 217 nichtig, Verweis 058) → Wortlautkarte § 25 Abs. 1, Werkzeug gegen sich selbst → Streit um den Maßstab (Exkulpations-/Einwilligungslösung, BGH) → Täuschung über den Tod (Art und Tragweite, Verweis 091) → Subsumtion → Versuch → Ergebnis (versuchter Totschlag in mittelbarer Täterschaft, Mordmerkmal offen) → Klausurtipp → Klausurschema → Merksatz → Hilfsangebot. Hauptfilm 6:08,1.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Hartwig (HW), um 55 | nennt sich spiritueller Lehrer; Hintermann | `standing/robot_dance-2` (schwarzer Pullover, Hose Lila `#B8A9F5`), Kopf `Gray Short`, Brille `Glasses 2`, Haut `#E2B08C`, ohne Bart. Mimiken `Calm`, `Smile` (redet freundlich), `Serious` (weiß es besser), `Solemn` | `helmut` (Mann, älter) |
| Wilma (WI), Mitte 30 | Getäuschte, Werkzeug gegen sich selbst | `standing/polka_dots` (Oberteil mit Punkten, Hose Grün `#8FD694`), Kopf `Long Curly`, Haut `#F0C8A8`. Mimiken `Calm` (auch redet), `Smile` (vertraut), `Serious`, `Solemn` | `ela_froh` (Frau, jung) |
| Benedikt (BE), um 30 | ihr Bruder, hält sie auf, holt Hilfe | `standing/blazer-3` (Jacke Blau `#8DB3F2`, Hose `#3B3B4F`), Kopf `Short 3`, Haut `#B07552`. Mimiken `Calm`, `Concerned\|Serious` (Sorge, redet) | `niklas` (Mann, jung) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Stimmen** nur aus dem zugeteilten Pool (niklas, helmut, ela_froh, julia); `julia` nicht gebraucht (drei Sprechrollen). Vorfolgen: 092 lucy/christian, 091 sabrina/marc/william, 090 julia/helmut/niklas. `helmut` ist die einzige ältere Männerstimme im Pool.
- **Namen** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste und in keiner versionierten Datei unter `youtube/` (`git grep -lw`): Wilma, Hartwig, Benedikt („Greta“ verworfen: Folge 003). Kein Genitiv eines Namens.
- **Blickrichtung:** Alle Posen blicken im Original nach rechts (`_r`); gespiegelt (ohne Suffix) nach links. A1: Hartwig links blickt nach rechts zu Wilma, Wilma rechts blickt nach links zu ihm. A2: Benedikt kommt links durch die Tür und blickt nach rechts zu Wilma; Wilma blickt nach links zu ihm; bei der Frage steht Hartwig rechts und blickt nach links. Tafelszenen: alle zur Tafel nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimik nur als `Concerned|Serious`. Mundzustände a/o/e nur bei `HW_redet`, `WI_redet`, `BE_redet` (je beide Blickrichtungen) und Lexi. `Awe` für Wilma verworfen (wirkt naiv, Gefahr der Verspottung). 50 Figuren-PNGs in `../peeps/op_094/` (nicht im Repository, im Drive-Master). Keine Bärte. Keine Prothesen-Pose.

**Abweichung von den letzten Folgen:** 090 (Posen `easing-1/-2`, `shirt-3`, `walking-2`), 091 Wohnung mit Kerzentisch und Blumenladen (`robot_dance-3`, `shirt-4`, `walking-1`), 092 (`resting-1/-2`, `crossed_arms-1`). 094: **Gesprächsraum** (Sessel, Pflanze, Stehlampe) und **Wilmas Wohnung am Abend** (Fenster mit Mond, Tür, Schreibtischlampe) – neue Schauplätze; Posen `robot_dance-2`, `polka_dots`, `blazer-3` in 090–092 nicht verwendet; Polka Dots zuletzt in 087. Der Abend nur als Mond im Fenster auf Cremegrund (keine Nachtfläche nötig).

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Gesprächsabend** `fall`→`plan` | Bodenlinie; links Hartwig, rechts Wilma, Sessel in der Mitte, Namensschilder ab 0,0 s | tabler: `plant-2` (Grün), `armchair` (Lila), `lamp` (Gelb), `stars` (Gelb), `sparkles` (Gelb), `calendar-event` (Weiß) | `Fall · Wilma und Hartwig` (ab 0,0 s) → `· Der ferne Stern` → `· Weiterleben?` → `· Hartwig weiß es besser` | Grundbild · „Mitte 30“ · „Gesprächsabende“ · „spiritueller Lehrer“ · „vertraut ihm blind“ · Sterne · „auserwählte Menschen“ · Hartwig redet · „höherer Körper“-Funkeln · Wilma redet · „Er weiß: Sie wäre tot.“ · „und genau das will er“ · Kalender | – |
| **A2 Wilmas Wohnung** `abend`→`frage2` | Fenster mit Mond, Lampe; Wilma; Tür links, Benedikt kommt herein, redet, Telefon „holt Hilfe“; Herz „Wilma bleibt unverletzt.“; bei der Frage steht Hartwig rechts. **Keine Methode, kein Gegenstand dazu** | tabler: `window` (Hellblau), `moon` (Gelb), `lamp-2` (Gelb), `door` (Weiß), `phone-call` (Grün), `heart` (Grün) | `Fall · Der verabredete Abend` → `· Wilma bleibt unverletzt` → `· Die Frage` | Abend · „beginnt, den Plan umzusetzen“ · Tür/Benedikt · „ihr Bruder, unerwartet“ · Benedikt redet · Telefon · Herz · Frage-Pillen | Tür beim Erscheinen der Tür, als Benedikt kommt (`szene_094tuer_1`, Freesound CC0 440645) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Der echte Fall** `echt`→`abgew` | Tafel; rechts nur Symbole (keine Figuren: reale Beteiligte werden nicht dargestellt) | tabler: `stars`, `file-certificate`, `heart`, `gavel` | `Der echte Fall · Sirius-Fall, BGHSt 32, 38` → `› Verurteilung bestätigt` | Zeile für Zeile, Haken, gelber Block | – |
| **D Ausgangspunkt** `aus`→`f058` | Tafel; Hartwig und Wilma | – | `Ausgangspunkt · Selbsttötung straflos` → `› Teilnahme mangels Haupttat straflos` → `› § 217 StGB nichtig` → `› vgl. Folge 058` | Zeilen, Kreuz, gelber Block | – |
| **E § 25 Abs. 1** `hand`→`unfrei` | **Wortlautkarte § 25 Abs. 1** (Marker „durch einen anderen“); Hartwig und Wilma | – | `A. Hartwig › Täter durch einen anderen?` → `› § 25 Abs. 1 Alt. 2 StGB` → `› Werkzeug gegen sich selbst` → `› Opfer handelt unfrei?` | Kreuz, Karte, Zeilen, gelber Block | – |
| **F Maßstab** `streit`→`mangel` | Tafel mit lila (Exkulpationslösung), hellblauem (Einwilligungslösung) und grünem Kasten (BGH), gelber Block; Wilma | tabler: `help-circle`, `masks-theater` | `A. Hartwig › Unfrei? › der Maßstab / Exkulpationslösung / Einwilligungslösung / BGH: Freiverantwortlichkeit / Täuschung` | Kästen nacheinander, Block | – |
| **G Täuschung** `art`→`f091` | Tafel; Hartwig und Wilma | tabler: `bulb` | `A. Hartwig › Täuschung über den Tod` → `› Täter kraft überlegenen Wissens` → `› vgl. Folge 091 (Katzenkönig)` | Zeilen, Haken, grüner Block | – |
| **H Subsumtion** `subs`→`unglaub` | Tafel; Hartwig und Wilma | – | `A. Hartwig › Subsumtion › Irrtum über den Tod` → `› beide Ansichten: unfrei` → `› Tatherrschaft` | Haken, Block, Zeilen | – |
| **I Versuch** `versuch`→`rt` | Tafel; Hartwig | tabler: `heart`, `hand-stop` | `A. Hartwig › Versuch` → `› Tatentschluss` → `› unmittelbares Ansetzen` → `› Rücktritt` | Haken, Kreuz | – |
| **J Ergebnis** `erg`, `mord` | Tafel, grüner und hellblauer Block; Hartwig und Wilma | tabler: `gavel` | `Ergebnis · versuchter Totschlag in mittelbarer Täterschaft` → `› Mordmerkmal?` | 2 | – |
| **K Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (2 Stände) | Zeile für Zeile | – |
| **L Klausurschema** `sch`→`s5` | breite Karte: Vorprüfung, 1. Tatentschluss (Opfer unfrei? Streit, Täuschung), 2.–4., Rücktritt | – | `Klausurschema` → je Gliederungspunkt ein Pfadstand | 10 Aufbaustufen | – |
| **M Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |
| **N Hilfsangebot** `hilfe`, `nummern` | ruhige hellblaue Tafel, keine Figur | tabler: `phone-call` (Grün) | `Hilfsangebot` | 2 | – |

**Blasen:** Stil C (`bausteine.blase`), Schwanzspitze außerhalb der Blase am Mund; wortgleich mit dem Gesprochenen. **Zahlen** auf Tafeln, Pillen und Karte als Ziffern („Mitte 30“, „5.7.1983“, „§ 217“, „0800 111 0 111“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; keine Bewegung.
**Geräusche:** ein Handlungsgeräusch (Tür), Freesound CC0, Herkunft in `geraeusche_herkunft.json`. Keine Musik.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Wilma (Mitte 30) vertraut seit Jahren Hartwig, der sich spiritueller Lehrer nennt. Er erzählt ihr, er stamme von einem fernen Stern, und redet ihr ein: Lasse sie ihren Körper hinter sich, wache sie sofort in einem höheren Körper auf und lebe weiter. Sterben will Wilma nicht; sie glaubt ihm.
>
> Hartwig weiß, dass sie sterben würde, und will genau das. Er legt alles fest, auch den Abend. Am verabredeten Abend beginnt Wilma, den Plan umzusetzen. Ihr Bruder Benedikt kommt unerwartet dazu, hält sie auf und holt Hilfe. Wilma bleibt unverletzt.
>
> Vorbild: BGHSt 32, 38 (Sirius-Fall), abgewandelt.
>
> **Wie hat sich Hartwig strafbar gemacht?**
