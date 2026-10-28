# Folge 073 · Bereicherungsrecht Überblick: Welche Kondiktion wann? (§ 812 BGB) – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_073.py`](src/skript_073.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/Bereicherungsrecht, Themenplan-Format „Schema“ (Leitentscheidung im Plan leer). Beispielfall nach dem Plan-Hook („Du überweist versehentlich 500 Euro an eine völlig fremde Person“): Ursula will ihrem Maler 500 € überweisen und vertauscht beim Eintippen der IBAN zwei Ziffern. Das Geld landet bei dem fremden Rüdiger. Er weiß, dass es nicht für ihn ist, behält es und gibt es am selben Tag für ein Wochenende am See aus. Auf Ursulas Anruf: „Tut mir leid, das Geld ist schon weg.“ Ablauf: Fall → Frage → Sachverhalt → Wortlautkarte § 812 I (vorgelesen) → zwei Grundtypen → Leistungsbegriff (BGH) → **Entscheidungsbaum progressiv** (Weiche „durch Leistung?“, Vorrang, vier Leistungskondiktionen je ein Satz, Ausschlüsse §§ 814, 817 S. 2, Eingriffskondiktion mit Beispiel, § 816, Rückgriffs-/Verwendungskondiktion) → Lösung des Falls (condictio indebiti, BGH IX ZR 164/14) → Ausblick Bankdreieck → Rechtsfolge § 818 I, II → § 818 III, §§ 819 I, 818 IV, § 822 → Ergebnis → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
**Länge:** Hauptfilm 6:37,8 (5.778 Zeichen). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Ursula (UR), um 70 | Überweisende, Anspruchstellerin | nur `standing/polka_dots` (Oberteil mit Punkten, Hose lila `#B8A9F5`), Kopf `Gray Bun`, Brille `Glasses 4`, Haut `#F2D0B5`, kein Bart; Mimiken `Calm`, `Fear` (bemerkt den Fehler), `Concerned|Serious` (redet, Sorge), `Suspicious`, `Smile`, `Serious` | `hilde` (Frau, älter) |
| Rüdiger (RD), um 45 | Empfänger, Anspruchsgegner | nur `standing/shirt-4` (schwarzes Hemd, Hose hellblau `#8DB3F2`), Kopf `Short 5`, Haut `#D9A27A`, kein Bart; Mimiken `Calm`, `Smile Big|Smile` (grinst, redet: „die behalte ich“), `Smile`, `Serious` (redet), `Suspicious`, `Concerned|Serious`, `Fear` (ertappt) | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |
| Maler | nur erwähnt (Rechnung) | keine Figur | – |

- **Namen** mit eindeutig deutscher Aussprache, nicht in früheren Folgen vergeben (geprüft per `grep -w` im Repository und gegen die Koordinatorliste): Ursula, Rüdiger. Kein Genitiv eines Namens („Konto von Rüdiger“). Die Figuren nennen keine Namen; alle Nennungen spricht die Erzählerin.
- **Stimmen nur aus dem Pool** stephan, hilde, christian, lucy; gebraucht hilde und stephan (christian nicht, stephan/christian also nie gemeinsam). Vorfolge 067: julia/niklas/helmut – keine Überschneidung.
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. In A1/A2 blickt Ursula (links) nach rechts, Rüdiger (rechts) nach links; in den Tafelszenen beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `UR_redet`, `RD_grinst`, `RD_redet` (je links/rechts) und Lexi. Keine Prothesen-Posen, keine Bärte, keine Karikatur, Rüdiger ohne Klischee (Alltagskleidung).
- Figuren-PNGs: `../peeps/op_073/` (54 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 067 (Gehweg vor der Bäckerei, Radfahrer), 063 (Elektrogeschäft, Küche), 070/071 (Produkthaftung/Unterlassen). Hier neu: Fernhandlung per Handy – zwei Personen ohne gemeinsamen Ort auf einer Bühne, fliegender Geldschein (Fluent Emoji `money-with-wings`) als Bild der Überweisung, Strandschirm für den Ausflug, Anruf. Tafelteil mit neuem Element **Entscheidungsbaum** (breite Karte, progressiv) und **Bankdreieck-Skizze** (Linien und Pillen, keine echte Bank, keine echte IBAN – nur „…74 statt …47“).

## Szenen

Alle Szenen auf Cremegrund (Tag).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Fehlüberweisung** `fall`–`rd2` | Ursula links mit Handy, Rechnung 500 €, Pille „IBAN: …74 statt …47“; Geld fliegt nach rechts (Bewegung) zu Rüdiger („Konto von Rüdiger“); Blase Rüdiger (grinst); Strandschirm „Wochenende am See“; „2 Tage später“, Anruf (Telefon-Symbole), Blasen Ursula und Rüdiger | tabler:`device-mobile`, `phone-call`, `file-invoice`, `beach` (Gelb); fluent-emoji-flat:`money-with-wings` | `Fall · Die Fehlüberweisung` (ab 0,0 s) → `Fall · Rüdiger behält das Geld` → `Fall · Der Anruf` | Grundbild · Rechnung · IBAN · Geld fliegt · Konto · 500 € · Blase Rüdiger · See · Anruf · Handy Rüdiger · Blase Ursula · Blase Rüdiger | `szene_073tippen_1` bei `ziff`, `szene_073vibration_1` bei „ruft“ |
| **A2 Frage** `frage`, `frage2` | beide, Geldschein, zwei Fragepillen | tabler:`cash-banknote` (Grün) | `Fall · Die Frage` | | – |
| **B Sachverhalt** `sv` | Karte vollständig, ohne Fiktiv-Hinweis | – | `Sachverhalt` | 1 | – |
| **C § 812 I** `norm`–`nlk` | Wortlautkarte (vorgelesen, 6 Marker), Blöcke Leistungs-/Nichtleistungskondiktion | tabler:`scale`, `arrows-split` | `Anspruchsgrundlage · § 812 Abs. 1 BGB › Wortlaut` → `§ 812 Abs. 1 BGB › zwei Grundtypen` | | – |
| **D Leistungsbegriff** `lb`–`ehz` | Definition mit Fundstelle, Empfängerhorizont | tabler:`arrows-split`, `target-arrow`, `eye` | `Leistungsbegriff` → `› Sicht des Empfängers` | | – |
| **E Entscheidungsbaum** `baum`–`rv` | breite Karte ohne Figuren: Wurzel „Erlangt durch eine Leistung?“, Äste Ja/Nein, Vorrang-Pille; links vier Leistungskondiktionen (je: Fall, dann Norm · Name) und Ausschluss mit Kreuz; rechts Eingriffskondiktion, Bildbeispiel, § 816, Rückgriff/Verwendung | Linien, Blöcke | `Entscheidungsbaum` → `› Erlangt durch Leistung?` → `› Vorrang der Leistungskondiktion` → `Leistungskondiktionen` → `› condictio indebiti …` → `› condictio ob causam finitam …` → `› condictio ob rem …` → `› § 817 Satz 1 BGB` → `› Ausschluss …` → `Nichtleistungskondiktionen › Eingriffskondiktion …` → `› § 816 BGB` → `› Rückgriff, Verwendung` | | – |
| **F Lösung** `fl`–`ci2` | Prüfung 1.–4. mit Haken, grüner Block „condictio indebiti greift“ | tabler:`building-bank`, `device-mobile`, `scale`, `file-invoice`, `cash-banknote` | `Fall · § 812 I 1 Alt. 1 BGB` → `› 1. etwas erlangt` → `› 2. durch Leistung von Ursula` → `› 3. ohne rechtlichen Grund` → `› 4. kein Ausschluss, § 814 BGB` → `› condictio indebiti` | | – |
| **G Bankdreieck** `dreieck`–`direkt` | Dreieck Kontoinhaber–Bank–Empfänger, Kreuz am Auftrag, grüner Pfeil Bank → Empfänger; Ursula allein | tabler:`building-bank`, `ban` (Rot), `arrow-back-up` | `Ausblick · Bankdreieck` → `› ohne wirksamen Auftrag: keine Leistung` → `› Nichtleistungskondiktion der Bank` | | – |
| **H1 Rechtsfolge** `rf`–`rf2` | § 818 I, II mit Bildbeispiel | tabler:`receipt-refund`, `arrow-back-up`, `photo` | `Rechtsfolge · §§ 818 ff. BGB` → `› Herausgabe, § 818 Abs. 1 BGB` → `› Wert, § 818 Abs. 2 BGB` | | – |
| **H2 Geld weg** `rf3`–`erg` | § 818 III, Kenntnis, §§ 819 I, 818 IV (Kreuz an § 818 III), § 822, grüner Ergebnisblock | tabler:`beach`, `eye`, `scale`, `gift`, `cash-banknote` | `Rechtsfolge › nicht mehr bereichert, § 818 Abs. 3 BGB` → `› Kenntnis, §§ 819 Abs. 1, 818 Abs. 4 BGB` → `› Dritter, § 822 BGB` → `Ergebnis` | | – |
| **I Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Leistungskondiktion zuerst` | | – |
| **J Klausurschema** `sch`–`k3` | breite Karte, Aufbau I.–III. | – | `Klausurschema` → `› Nichtleistungskondiktion` → `› Rechtsfolge` | | – |
| **K Merksatz** `merke`, `m2` | Lexi erklärt, zwei Marker | – | `Merksatz` | | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 13 Folien; innerhalb harte Schnitte und Pops; Bewegung nur beim fliegenden Geld.
**Blasen:** Stil C (`bausteine.blase`), wortgleich mit dem Gesprochenen, Zahlen als Ziffern („500 €“). Zahlen auf Tafeln, Pillen und Karte als Ziffern („500 €“, „2 Tage später“, „§ 812 I 1 Alt. 1“).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Ursula will ihrem Maler 500 Euro für seine Rechnung überweisen. Beim Eintippen der IBAN vertauscht sie zwei Ziffern. Das Geld landet auf dem Konto von Rüdiger, einem völlig Fremden.
>
> Rüdiger weiß, dass das Geld nicht für ihn ist, behält es aber und gibt es noch am selben Tag für ein Wochenende am See aus. Zwei Tage später bemerkt Ursula den Fehler, ruft Rüdiger an und bittet um Rückzahlung. Rüdiger: „Tut mir leid, das Geld ist schon weg.“
>
> **Kann Ursula die 500 Euro zurückverlangen, und woraus?**
