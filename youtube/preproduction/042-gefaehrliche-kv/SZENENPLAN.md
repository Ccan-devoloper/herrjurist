# Folge 042 · Gefährliche Körperverletzung Schema: § 224 StGB mit allen 5 Varianten – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_042.py`](src/skript_042.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis, Themenplan-Format „Schema“. Ein Dorffest-Fall trägt den Film: Tobias stößt beim Tanzen Reinhards Bierglas um; Reinhard stößt ihn zu Boden und tritt ihm mit dem schweren Arbeitsstiefel gegen den Kopf. Frage → Sachverhalt (Grundfall und fünf Varianten) → Wortlautkarte § 224 I, II → Aufbau (Grundtatbestand, Qualifikation) → Grundfall: § 223 kurz, Nr. 2 (Definition, Schuh am Fuß) → Nr. 1 (Variante 1, Schlafmittel) → Nr. 3 (Variante 2, Handschlag als Falle; Gegenstück Angriff von hinten) → Nr. 4 (Variante 3, Anja versperrt den Weg) → Nr. 5 (Variante 4, Würgen) → Vorsatz → Versuch (Variante 5) → Ergebnis und Strafantrag → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
**Verhältnis zu den Folgen 035 und 038:** In 035 steht § 224 nur als Wortlautkarte mit Nr. 4 am Treppenhausfall; 038 behandelt § 223 und erwähnt § 224 nur im Klausurtipp (Schere). Hier wird § 223 nur kurz vorausgesetzt; Schwerpunkt sind alle fünf Nummern mit BGH-Definitionen, der Schuh als Werkzeug, der Vorsatz bezüglich der Qualifikation, der Versuch und das Fehlen des Strafantragserfordernisses.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Reinhard (RE), Mitte 50 | Täter in Grundfall und allen Varianten | `standing/pointing_finger-2` (erhobener Zeigefinger; schwarze Stiefel der Originalpose = „schwerer Arbeitsstiefel“), Kopf `No Hair 3` (Glatze mit grauem Haarkranz), schwarzes Oberteil der Pose, Hose Grün `#8FD694`, Haut `#E8B894`. Mimiken `Calm`, `Very Angry`, `Rage|Serious` (redet drohend), `Smile` (redet lächelnd, Variante 2), `Driven`, `Serious`, `Contempt`, `Fear` (ertappt), `Suspicious` | `helmut` (Mann, älter) |
| Tobias (TO/TOS), Mitte 20 | Festbesucher, Opfer | `standing/walking-2` (tanzt, steht) und nach dem Stoß `sitting/hands_back-1` (am Boden); beide mit schwarzem T-Shirt der Pose und Hose Blau `#8DB3F2`, Kopf `Short 1`, Haut `#D9A27A`. Mimiken `Smile`, `Calm`, `Fear`, `Concerned|Serious` (redet; Schmerz), `Serious`, `Suspicious`, `Awe`, `Eyes Closed` (bricht zusammen) | `timo` (Mann, jung) |
| Anja (AN), Ende 20 | Reinhards Tochter, versperrt in Variante 3 den Weg | `standing/easing-2`, Kopf `Medium Bangs 2`, Jacke Lila `#B8A9F5`, Hose dunkel `#4A4A5E`, Haut `#F0C8A8`. Mimiken `Calm`, `Driven` (redet; streng), `Serious` | `ela_warm` (Frau, jung) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links: Reinhard zu Tobias im Fall, alle Figuren rechts zur Tafel), `_r` blickt nach rechts (Tobias im Fall zu Reinhard; Reinhard in Variante 2 und 3 zu Tobias).
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimiken nur als `Concerned|Serious` bzw. `Rage|Serious`. Mundzustände a/o/e bei `RE_redet`, `RE_laechelt`, `TOS_redet`, `AN_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen. 82 Figuren-PNGs in `../peeps/op_042/` (Drive-Master).
- **Zwei Posen für Tobias** (stehend/am Boden) sind durch den Sachverhalt bedingt (Stoß zu Boden); Outfit identisch (schwarzes T-Shirt, blaue Hose, Kopf, Haut).
- **Namen** mit eindeutig deutscher Aussprache, in keiner Vorfolge vergeben (Liste des Auftrags; zusätzlich gegen alle Skripte und Dokumente 001–041 geprüft): Reinhard, Tobias, Anja.
- **Stimmen** nur aus dem zugeteilten Pool (helmut, timo, ela_warm; `lucy` nicht gebraucht – sie sprach in 038 Katrin). Vorfolge 038 (lucy, hilde, william): keine Überschneidung. Lea nicht verwendet.

**Abweichung von den letzten Folgen:** 038 (Wohngemeinschaft, Hautarztpraxis), 035 (Unibibliothek), 033 (Stadtbibliothek), 039–041 (Parallelfolgen, Büro/Behörde). Hier neu: Festwiese eines Dorffests (Festzelt, Biertisch mit Bierkrug, Sonne) bei Tageslicht. Neue Posen (`pointing_finger-2`, `walking-2`, `sitting/hands_back-1`, `easing-2`), Tafelszenen mit Figurenpaar bzw. -trio rechts und wechselnden Requisiten-Symbolen je Nummer.
**Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Dorffest** `fall`→`frage2` | Festwiese; Tobias tanzt (Noten, Pille „tanzt“), Bierkrug kippt („aus Versehen“), Reinhard erscheint, „außer sich“, Blase „Das wirst du bereuen!“, Tobias am Boden („zu Boden gestoßen“), Stiefel-Symbol mit „schwerer Arbeitsstiefel“, „Tritt gegen den Kopf“, „dicke Beule“; Blase Tobias; Frage-Pillen | tabler:`tent`, `sun`, `picnic-table`, `music`; ph:`beer-stein-thin` (gekippt um −60°, nicht umgezeichnet), `boot-thin` | `Fall · Das Dorffest` (ab 0,0 s) → `Fall · Die Frage` | ≈ 18 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10,8 s, Schrift 33 px | – | `Sachverhalt` | 1 | – |
| **C Wortlaut** `p224`→`abs2` | Wortlautkarte § 224 I, II vollständig ab Folienbeginn, Marker je Nummer; Symbolreihe Nr. 1–5 | tabler:`pill`, `users`, `heartbeat`; ph:`boot-thin`, `handshake-thin` | `§ 224 StGB › Wortlaut: fünf Begehungsweisen` | ≈ 11 | – |
| **D Aufbau** `aufbau`→`dann` | „§ 224 = Qualifikation“, zwei Blöcke mit Pfeil | tabler:`arrow-down` | `§ 224 StGB › Aufbau: Grundtatbestand und Qualifikation` | 4 | – |
| **E1 Grundfall** `gf`→`werh` | § 223 kurz (Haken), Block Nr. 2, BGH-Definition zeilenweise; Tobias am Boden, Stiefel, „Beule“ | ph:`boot-thin` | `Grundfall › I. 1. objektiv › a) Körperverletzung, § 223 StGB` → `… › b) Qualifikation: Nr. 2 gefährliches Werkzeug` | ≈ 11 | – |
| **E2 Schuh** `schuh`→`nr5gf` | drei Kriterien, Block Kopf-Regel, Haken; Turnschuh-Symbol → Arbeitsstiefel | ph:`sneaker-thin`, `boot-thin` | `… › b) Nr. 2: der Schuh am Fuß` | ≈ 10 | – |
| **F Nr. 1** `nr1`→`nr1_ok` | Variante 1; Tobias steht, bricht dann zusammen (am Boden, Augen zu); Block BGHSt 51, 18 | tabler:`glass-full`, `pills`, `ambulance` | `Variante 1 › Nr. 1: Gift oder gesundheitsschädliche Stoffe` | ≈ 9 | – |
| **G Nr. 3** `nr3`→`hinten_no` | Reinhard und Tobias einander zugewandt, Handschlag-Symbol, Blase „Komm, vertragen wir uns wieder.“, „schlägt unvermittelt zu“; Definition, Haken; Gegenstück mit Kreuz | ph:`handshake-thin` | `Variante 2 › Nr. 3: hinterlistiger Überfall` | ≈ 13 | – |
| **H Nr. 4** `nr4`→`nr4_ok` | Trio Reinhard – Tobias – Anja; Blase Anja „Hier kommst du nicht vorbei!“; „versperrt den Weg“, „kein Ausweg“, „Gehilfin“ | – | `Variante 3 › Nr. 4: mit einem anderen Beteiligten gemeinschaftlich` | ≈ 12 | – |
| **I Nr. 5** `nr5`→`nr5_ok` | Variante 4 nur als Text/Pille, Herzschlag-Symbol; Block „abstrakt geeignet“; Kreuz „nicht jeder Griff“, Haken | tabler:`heartbeat` | `Variante 4 › Nr. 5: das Leben gefährdende Behandlung` | ≈ 9 | – |
| **J Vorsatz** `vz`→`bezw` | zwei Haken, Block, Grundfall-Zeile, Kreuz „bezwecken: nicht nötig“; Denkblase Reinhard „Stiefel, Kopf“ | ph:`boot-thin` | `Grundfall › I. 2. subjektiv: Vorsatz` | ≈ 7 | – |
| **K Versuch** `vers`→`vers_ok` | Reinhard holt aus (Stiefel, „ausgeholt“), Tobias rollt weg (neue Position, „weggerollt“); zwei Haken, Block | ph:`boot-thin` | `Variante 5 › Versuch, §§ 224 Abs. 2, 22 StGB` | ≈ 9 | – |
| **L Ergebnis** `erg`→`antrag` | Ergebnisblock mit Haken, Waage „strafbar“, § 230; Unterschrift „kein Antrag nötig“ | tabler:`scale`, `signature` | `Grundfall › II. Rechtswidrigkeit, III. Schuld` → `Grundfall › Ergebnis: §§ 223, 224 Abs. 1 Nr. 2 StGB` → `Grundfall › kein Strafantrag nötig, § 230 StGB` | ≈ 7 | – |
| **M Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand), ph:`boot-thin` | `Klausurtipp · §§ 223, 224 zusammen prüfen` | ≈ 7 | – |
| **N Klausurschema** `sch`→`k_v` | breite Karte, progressiv (Nr. 1–5 einzeln zum Wort) | – | `Klausurschema` | 14 | – |
| **O Merksatz** `merke`→`m3` | Lexi erklärt, drei Marker | – | `Merksatz` | ≈ 6 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Handlung als Zustandswechsel (Bierkrug steht → gekippt; Tobias tanzt → am Boden; Reinhard am Tisch → bei Tobias; Tobias steht → bricht zusammen; Tobias rollt weg).
**Geräusche:** keine (siehe `geraeusche_herkunft.json`: Freesound gesperrt, in `sfx3/` kein Glas- oder Festgeräusch; Gewalthandlungen bewusst ohne Ton).
**Gewalt zurückhaltend:** kein Blut, keine Verletzung im Bild, kein Tritt, Schlag oder Würgen als Bewegung; nur Pillen und neutrale Symbole (Stiefel, Glas, Hand, Herzschlag). Der Täter ist keine Karikatur und trägt keine Waffe.
**Wortlautkarte** (FOLGE-ABLAUF Abschnitt 2): § 224 I, II vollständig, wörtlich nach gesetze-im-internet.de mit Normangabe; die Erzählerin liest die fünf Nummern wörtlich und den Strafrahmen verkürzt; Marker synchron.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Samstagnachmittag auf dem Dorffest: Tobias tanzt vor dem Festzelt und stößt dabei aus Versehen das Bierglas von Reinhard (Mitte 50) um. Reinhard stößt Tobias zu Boden und tritt ihm mit seinem schweren Arbeitsstiefel gegen den Kopf. Tobias bekommt eine dicke Beule.
>
> Variante 1: Reinhard mischt Tobias heimlich eine hohe Dosis eines starken Schlafmittels ins Glas; Tobias bricht zusammen und muss im Krankenhaus behandelt werden. Variante 2: Reinhard geht lächelnd auf Tobias zu, reicht ihm die Hand („Komm, vertragen wir uns wieder.“) und schlägt dann unvermittelt zu. Gegenstück: Reinhard greift Tobias nur überraschend von hinten an. Variante 3: Reinhards Tochter Anja stellt sich Tobias in den Weg, damit er nicht ausweichen kann, während Reinhard zuschlägt; selbst schlägt sie nicht. Variante 4: Reinhard drückt Tobias kräftig und lange den Hals zu; in Lebensgefahr gerät Tobias nicht. Variante 5: Reinhard holt mit dem Stiefel zum Tritt gegen Tobias’ Kopf aus, doch Tobias rollt sich weg.
>
> **Wie hat sich Reinhard strafbar gemacht?**
