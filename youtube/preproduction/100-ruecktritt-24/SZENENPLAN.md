# Folge 100 · Rücktritt vom Versuch § 24 StGB: Das Schema Schritt für Schritt – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_100.py`](src/skript_100.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall, Themenplan-Format „Schema“. Der Plan-Hook trägt den Film: Ein Einbrecher setzt schon den Hebel am Fenster an, bekommt Gewissensbisse und geht nach Hause. Frage → Sachverhalt → Wortlautkarte § 24 Abs. 1 S. 1 und 2 → Versuch in zwei Sätzen (Verweis auf Folge 097) → IV. 1. kein fehlgeschlagener Versuch (Abgrenzung zu 097 in einem Satz) → IV. 2. unbeendet/beendet (Rücktrittshorizont, Korrektur) → IV. 3. Rücktrittshandlung (S. 1 Alt. 1, Alt. 2, S. 2) → IV. 4. Freiwilligkeit (autonom/heteronom, kein sittlich billigenswertes Motiv nötig) → § 24 Abs. 2 (ein Satz) → Ergebnis → Klausurtipp (Lexi: persönlicher Strafaufhebungsgrund, vollendete Sachbeschädigung bleibt) → Klausurschema → Merksatz (Lexi).
**Verhältnis zu 097 (Versuchsschema):** Die Versuchsprüfung wird nicht wiederholt; 097 endete mit dem fehlgeschlagenen Versuch, hier geht es an genau dieser Stelle (Punkt IV.) weiter.
**Länge:** 4.553 Zeichen, Hauptfilm 5:16,8 – Regelrahmen.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Heiner (HN), Mitte 40 | Täter, tritt zurück | `standing/robot_dance-3` (Oberteil Salbeigrün `#A7C4A0`, Hose Schiefergrau `#5A6275`, weiße Turnschuhe), Kopf `Short 3`, Haar `#6B4A2E`, Haut `#E8B892`. Mimiken `Calm`, `Suspicious`, `Driven` (setzt den Hebel an), `Concerned|Serious` (redet), `Solemn` (Gewissensbisse), `Tired`, `Serious`, `Awe` | `marc` (Mann, mittel) |
| Annegret (AN), um 50 | Wohnungsinhaberin | `standing/crossed_arms-1` (Oberteil Koralle `#F28C6B`, schwarze Hose der Pose), Kopf `Medium Bangs`, Haar `#5A3A28`, Haut `#B98260`. Mimiken `Calm`, `Concerned|Serious` (redet), `Serious`, `Suspicious` | `sabrina` (Frau, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links: Annegret zum Küchenfenster, beide in den Tafelszenen zur Tafel; Heiner auf dem Heimweg), `_r` blickt nach rechts (Heiner am Fenster).
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimik nur als `Concerned|Serious`. Mundzustände a/o/e bei `HN_redet`, `AN_redet` (je links/rechts) und Lexi. Kein Bart, keine Prothesen-Pose. 50 Figuren-PNGs in `../peeps/op_100/` (Drive-Master).
- **Klischeeprüfung:** Heiner ist ein gewöhnlicher Mann in salbeigrünem Pullover, kein schwarzes „Einbrecher-Outfit“, keine Maske, keine Herkunfts- oder Hautfarbenzuschreibung, keine Karikatur. Der Hebel ist ein stilisierter Baustein (blaue Stange mit Klaue).
- **Namen** mit eindeutig deutscher Aussprache, in keiner Vorfolge vergeben (Auftragsliste und alle Skripte/Dokumente in `preproduction/` geprüft): Heiner, Annegret. Nie im Genitiv mit -s gesprochen („die Erdgeschosswohnung von Annegret“).
- **Stimmen** nur aus dem Pool (marc, sabrina; william und laura_ruhig nicht gebraucht). In 097 sprach marc das Opfer Gregor, jetzt den Täter; william (097: Täter) nicht verwendet. Lea nicht verwendet.
- **Abwechslung:** Annegret zuerst als `crossed_arms-2` (schwarzes Oberteil, blaue Hose) gebaut; beim Vergleich mit den Kontaktbögen von 099 (Jochen: schwarzes Oberteil, blaue Hose) verworfen und auf `crossed_arms-1` mit korallfarbenem Oberteil umgestellt (zuletzt in 096). Posen nicht aus 097–099 (pointing_finger-2, walking-1, blazer-3, resting-2, shirt-4, blazer-1, walking-3), keine Polka Dots. Hinweis: Heiners Pose `robot_dance-3` gehört zur selben Reihe wie Lexis `robot_dance-1`; die beiden stehen nie gleichzeitig im Bild, Outfit und Farben sind verschieden.

**Abweichung von den letzten Folgen:** 097 (Wohnstraße mit zwei Satteldachhäusern, Garage, Auto), 098 und 099 (andere Gebiete). Neu: Seitenstraße mit einem Mehrfamilienhaus mit Flachdach (rote Dachkante), Erdgeschoss-Küchenfenster direkt am Gehweg, gelbe Haustür; in den Tafelszenen kleine Requisiten rechts (Haus, Zielscheibe, Waage, Fenster, Auge, Hand, Herz, Absperrung, Personen, Hammer). Kein früherer Schauplatz.
**Tageslicht:** durchgehend Cremegrund (Dienstagnachmittag; „Am Abend“ als Zeitpille, kein Nachtverlauf nötig).
**Gewalt:** keine Gewalt gegen Personen; der Hebel nur stilisiert, kein Splittern, kein Eindringen. Die Delle als roter Ring am Rahmen.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Seitenstraße** `fall`→`frage2` | Mehrfamilienhaus (Flachdach, Küchenfenster im Erdgeschoss am Gehweg, Haustür), Heiner am Fenster; „Mitte 40“, „braucht dringend Geld“ (Geldschein); Ring um das Erdgeschoss, „Erdgeschosswohnung von Annegret“, „Spätschicht: niemand zu Hause“ (Uhr); Ring um das Küchenfenster; „will einbrechen und stehlen“, Hebel an der Hand, Ring „tiefe Delle“; Blase Heiner „Was mache ich hier eigentlich? Das ist nicht richtig.“; „Gewissensbisse“ (Herz), „niemand hat ihn bemerkt“, „Fenster fast offen“; Hebel weg, Heiner auf dem Heimweg mit Haus und Pfeil; „Am Abend“: Annegret mit Schlüssel, Blase „Was ist denn mit meinem Fensterrahmen passiert?“, Ring an der Delle; Frage-Pillen | tabler:`cash-banknote`, `clock`, `heart`; ph:`house`, `key`; Haus und Hebel als Bausteine | `Fall · Die Seitenstraße` (ab 0,0 s) → `Fall · Der Hebel` → `Fall · Die Gewissensbisse` → `Fall · Am Abend` → `Fall · Die Frage` | ≈ 27 | Holz knarzt (`szene_100hebel_1`), Schlüsselbund (`szene_100schluessel_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Wortlaut** `p24`→`p24s2` | Wortlautkarte § 24 Abs. 1 S. 1 und 2 mit vier Markern, Pillen „Satz 1“/„Satz 2“ | tabler:`arrow-back-up`, `hand-stop` | `Rücktritt › Wortlaut § 24 Abs. 1 StGB` | ≈ 7 | – |
| **D Versuch** `vers`→`vers2` | Haken Tatentschluss, unmittelbares Ansetzen (BGH Rn. 8), rechtswidrig und schuldhaft; Block versuchter Wohnungseinbruchdiebstahl | ph:`house`; tabler:`target`, `scale` | `Versuchter Wohnungseinbruchdiebstahl › I.–III. Versuch (wie Folge 097)` | ≈ 7 | – |
| **E IV. 1.** `rt`→`rt1c` | Fehlschlag-Definition (BGH Rn. 5), Folge 097, Haken „Fenster gleich aufgehebelt“, Block „nicht fehlgeschlagen“ | tabler:`arrow-back-up`, `circle-x`; Fenster-Baustein | `… › IV. Rücktritt` → `… › 1. kein fehlgeschlagener Versuch` | ≈ 9 | – |
| **F IV. 2.** `rt2`→`unb2` | Rücktrittshorizont, Blöcke unbeendet/beendet, Korrektur, Haken, Block „unbeendeter Versuch“; Denkblase Heiner mit geschlossenem Fenster | tabler:`eye`; Fenster-Baustein | `… › 2. unbeendet oder beendet` → `… › 2. Korrektur des Rücktrittshorizonts` → `… › 2. unbeendeter Versuch` | ≈ 9 | – |
| **G IV. 3.** `rh`→`rh4` | Blöcke Aufgeben/Verhindern mit Normstellen, S. 2, Haken, Block „Tat aufgegeben“ | tabler:`hand-stop`; ph:`house` | `… › 3. Rücktrittshandlung` | ≈ 10 | – |
| **H IV. 4.** `fw`→`fw5` | Formel (BGH Rn. 8), Blöcke autonom/heteronom, Motiv (Rn. 9), Haken, Block „freiwillig zurückgetreten“ | tabler:`brain`, `heart`, `barrier-block` | `… › 4. Freiwilligkeit` | ≈ 10 | – |
| **I Abs. 2, Ergebnis** `zwei`→`erg2` | § 24 Abs. 2 S. 1, Ergebnisblöcke straflos/strafbar wegen der Delle | tabler:`users`, `gavel`; Fenster-Baustein mit Ring | `§ 24 Abs. 2 StGB · mehrere Beteiligte` → `Ergebnis` | ≈ 4 | – |
| **J Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Rücktritt erfasst nur den Versuch` | ≈ 8 | – |
| **K Klausurschema** `sch`→`s44` | breite Karte, progressiv | – | `Klausurschema` | ≈ 9 | – |
| **L Merksatz** `merke`→`m3` | Lexi erklärt, drei Marker | – | `Merksatz` | ≈ 6 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 12 Folien; innerhalb harte Schnitte und Pops.
**Wortlautkarte** (FOLGE-ABLAUF Abschnitt 2): § 24 Abs. 1 S. 1 und 2 vollständig, wörtlich nach gesetze-im-internet.de mit Normangabe, wörtlich vorgelesen; Marker synchron.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Heiner (Mitte 40) braucht dringend Geld. An einem Dienstagnachmittag will er in die Erdgeschosswohnung von Annegret einbrechen und dort stehlen. Er weiß, dass Annegret dort wohnt und gerade in der Spätschicht arbeitet. Das Küchenfenster liegt direkt am Gehweg.
>
> Heiner setzt einen Hebel am Fensterrahmen an und drückt. Das Holz gibt nach, im Rahmen bleibt eine tiefe Delle. Das Fenster hätte er gleich aufgehebelt.
>
> Da bekommt Heiner Gewissensbisse. Niemand hat ihn bemerkt. Trotzdem steckt er den Hebel ein und geht nach Hause. Am Abend entdeckt Annegret die Delle.
>
> **Ist Heiner strafbar?**
