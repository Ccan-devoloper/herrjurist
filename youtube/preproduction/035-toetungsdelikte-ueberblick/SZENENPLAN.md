# Folge 035 · Tötungsdelikte Überblick: §§ 211–229 StGB inkl. Körperverletzung – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_035.py`](src/skript_035.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen, Themenplan-Format „Schema“, Überblicksfolge als **Landkarte**. Lernsituation: Britta und Florian lernen in der Unibibliothek; ihr Übungsfall steht auf dem Whiteboard (Fritz stößt seinen Nachbarn Henning im Treppenhaus) und wird nur mit Personen-Symbolen gezeigt. Frage → Sachverhalt mit sechs Varianten → Landkarte (zwei Säulen, fünf Ebenen) → § 212 (Wortlaut) → § 211 (drei Gruppen) → Streit Rspr./Lehre mit § 28 → §§ 213, 216 → § 222 → § 223 (Wortlaut) → § 224 (Wortlaut, Nr. 4 am Fall) → § 226 → § 227 → § 229, § 230 → Prüfreihenfolge (Konvention) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Britta (BR), Anfang 20 | Jurastudentin in der Lerngruppe | `standing/crossed_arms-2`, Kopf `Long Bangs`, Oberteil der Pose (Tusche), Hose Lila `#B8A9F5`, Haut `#F0C8A8`. Mimiken `Calm`, `Concerned|Serious` (redet; „sorge“), `Serious`, `Suspicious`, `Smile`, `Awe` | `julia` (Frau, jung) |
| Florian (FL), Mitte 20 | Jurastudent in der Lerngruppe | `standing/shirt-1` (Originalpose mit Beinprothese), Kopf `Short 3`, Hemd Grün `#8FD694`, Haut `#D9A27A`. Mimiken `Calm`, `Smile` (redet), `Suspicious` (fragt), `Serious`, `Awe`, `Tired` | `marc` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |
| Fritz, Henning, ein Freund | nur Fallbeteiligte auf dem Whiteboard bzw. der Mini-Treppe | **keine Figuren**, nur Tabler `user` in Blau/Grün/Grau mit Namenspille | – |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts (Florian spricht im Fall zu Britta).
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimiken nur als `Concerned|Serious`. Mundzustände a/o/e bei `BR_redet`, `FL_redet`, `FL_fragt` (je links/rechts) und Lexi. Keine Bärte. 54 Figuren-PNGs in `../peeps/op_035/` (Drive-Master).
- Die Beinprothese gehört zur Originalpose `shirt-1`; Florian ist Lernfigur, kein Täter (FOLGE-ABLAUF: Prothesen nicht reflexhaft für Täter).
- **Namen** mit eindeutig deutscher Aussprache, in keiner Vorfolge vergeben (Liste des Auftrags; zusätzlich gegen 030–034 geprüft, dort u. a. Ulrike, Torsten, Kluge, Fuchs, Ziegler): Britta, Florian, Fritz, Henning.
- **Stimmen** nur aus dem zugeteilten Pool (julia, marc; william, elinor nicht gebraucht). Vorfolge 034 (stephan, lisa), 033 (laura_klar, niklas, helmut): keine Überschneidung.

**Abweichung von den letzten Folgen:** 034 (Schwarzarbeit, Baustelle/Wohnung), 033 (Notwehr), 029 (Gärten mit Mauer). Hier neu: Lernsituation in der Unibibliothek mit Whiteboard (Lampe, Bücher), danach Tafeln mit einer **kleinen Landkarte rechts oben**, die sich Delikt für Delikt füllt (aktuelles Feld gelb) – das Orientierungsmittel der Überblicksfolge. Neue Posen (`crossed_arms-2`, `shirt-1`).
**Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Übungsfall** `fall`→`frage2` | Bibliothek: Whiteboard links, Florian und Britta rechts; auf dem Whiteboard Treppe, Fritz und Henning (Symbole), Fahrrad, Pfeil „stößt“, Henning unten an der Treppe; Florian: „Klare Sache: Körperverletzung.“, Britta: „Und wenn Henning dabei stirbt?“ | tabler:`stairs`, `user`, `lamp`, `books`; ph:`bicycle` | `Fall · Der Übungsfall` (ab 0,0 s) → `Fall · Die Frage` | ≈ 17 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Landkarte** `karte`→`fahrl` | Raster zwei Säulen × fünf Ebenen, Zeilen zum gesprochenen Wort; Felder noch leer | tabler:`heart`, `bandage` | `Überblick · Landkarte §§ 211–229 StGB` | 9 | – |
| **D Totschlag** `p212`→`p212s` | Wortlautkarte § 212 I, Variante 1; Britta | Mini-Landkarte | `A. Tötungsdelikte › Grundtatbestand: Totschlag, § 212 StGB` | ≈ 8 | – |
| **E Mord** `p211`→`lebensl` | drei Gruppenblöcke; Florian | Mini-Landkarte | `A. Tötungsdelikte › Mord, § 211 StGB` | ≈ 11 | – |
| **F Streit** `streit`→`offen` | Lehre / Rechtsprechung, § 28; Florian fragt (Blase) | tabler:`scale`, `users` | `A. Tötungsdelikte › Mord und Totschlag: Streit` → `… › Teilnehmer, § 28 StGB` | ≈ 13 | – |
| **G Milder** `milder`→`s216` | §§ 213, 216; Britta | Mini-Landkarte | `A. Tötungsdelikte › milder: minder schwerer Fall, § 213 StGB` → `… › milder: Tötung auf Verlangen, § 216 StGB` | ≈ 10 | – |
| **H § 222** `p222`→`p222s` | Variante 2; Mini-Treppe mit Fritz, Fahrrad, Henning | tabler:`stairs`, `user`; ph:`bicycle` | `A. Tötungsdelikte › Fahrlässigkeit: fahrlässige Tötung, § 222 StGB` | ≈ 7 | – |
| **I § 223** `p223`→`prell` | Wortlautkarte § 223 I, Variante 3, Haken; Britta | Mini-Landkarte | `B. Körperverletzungsdelikte › Grundtatbestand: Körperverletzung, § 223 StGB` | ≈ 11 | – |
| **J § 224** `p224`→`nr5` | Wortlautkarte § 224 I mit Markern Nr. 1–5; Mini-Treppe mit Freund (grau) | tabler:`stairs`, `user` | `B. … › gefährliche Körperverletzung, § 224 StGB` → `… › § 224 Abs. 1 Nr. 4: gemeinschaftlich` | ≈ 15 | – |
| **K § 226** `p226`→`abs2` | Dauerfolgen, Variante 5, § 18, Abs. 2; Florian | tabler:`eye-off` | `B. … › schwere Körperverletzung, § 226 StGB` | ≈ 7 | – |
| **L § 227** `p227`→`t227` | Variante 6; Kausalität (Kreuz), spezifische Gefahr (Haken); Mini-Treppe, Henning unten, Pille „Tod“ | tabler:`stairs`, `user` | `B. … › Körperverletzung mit Todesfolge, § 227 StGB` | ≈ 11 | – |
| **M §§ 229, 230** `p229`→`oeff` | § 229, Variante 2; § 230 Antrag; Britta | tabler:`signature` | `B. … › fahrlässige Körperverletzung, § 229 StGB` → `B. … › Strafantrag, § 230 StGB` | ≈ 8 | – |
| **N Prüfreihenfolge** `reihe`→`konv` | nummerierte Liste; Florian und Britta | tabler:`list-numbers` | `Prüfreihenfolge · Klausurkonvention` | ≈ 8 | – |
| **O Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Mordmerkmale im Aufbau` | ≈ 7 | – |
| **P Klausurschema** `sch`→`k4` | breite Karte, progressiv | – | `Klausurschema` | 9 | – |
| **Q Merksatz** `merke`→`m3` | Lexi erklärt, Marker | – | `Merksatz` | ≈ 5 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** keine. Die einzige sichtbare Handlung (Stoß/Sturz) ist bewusst abstrakt; ein Sturz- oder Aufprallgeräusch wäre ein Gewaltakzent. Freesound ist über den Proxy gesperrt (HTTP 403); in `sfx3/` gibt es nichts Passendes („lieber kein Geräusch als ein unpassendes“).
**Gewalt zurückhaltend:** keine Leichen, kein Blut, keine Waffen, keine Verletzungsbilder; Fallbeteiligte nur als Symbole; „Tod“ als graue Pille unter dem Symbol, Dauerfolge als durchgestrichenes Auge (Icon).
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 212 I (wörtlich vorgelesen), § 223 I (amtliche Schreibung „mißhandelt“; gesprochen sinngemäß), § 224 I (Merkmale gesprochen, Marker je Nummer synchron), wörtlich nach gesetze-im-internet.de mit Normangabe.
**Mini-Landkarte:** ab Szene D rechts oben (x 1268–1872, y 58–388); Zeilen- und Spaltenbeschriftungen wie in Szene C gesprochen, Felder erscheinen beim gesprochenen Paragrafen.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Im Treppenhaus streiten Fritz und sein Nachbar Henning um ein Fahrrad. Fritz stößt Henning, Henning stürzt die Treppe hinunter. Grundfall: Fritz will Henning verletzen.
>
> Variante 1: Fritz will Henning töten; Henning stirbt. Variante 2: Fritz rempelt Henning beim Tragen des Fahrrads nur aus Unachtsamkeit an. Variante 3: Henning erleidet Prellungen. Variante 4: Ein Freund von Fritz versperrt Henning bewusst den Weg. Variante 5: Henning verliert das Sehvermögen auf einem Auge. Variante 6: Henning stirbt an den Folgen des Sturzes.
>
> **Welche Delikte kommen in Betracht?**
