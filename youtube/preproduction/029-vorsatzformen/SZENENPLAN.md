# Folge 029 · Vorsatzformen: Absicht, direkter Vorsatz, Eventualvorsatz erklärt – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_029.py`](src/skript_029.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen, Themenplan-Format „Schema“. Der Hauptteil läuft an einem ruhigen fiktiven Fall: Volker reißt seine alte Gartenmauer ab, sie kippt auf den neuen Holzzaun der Nachbarin Heike. Frage → Sachverhalt → Sachbeschädigung (Wortlaut § 303 I) und § 15 (Wortlaut; keine fahrlässige Sachbeschädigung) → Wissen und Wollen → Variante 1 Absicht → Variante 2 direkter Vorsatz → Lehrbuchbeispiel Thomas-Fall (Bremerhaven 1875, nur Icons) → Variante 3 Eventualvorsatz (BGH-Formel, Berliner Raser) → Variante 4 bewusste Fahrlässigkeit (Seil) → Abgrenzung durch Gesamtschau → Gegenstück Tatumstandsirrtum (Wortlaut § 16 I) → Klausurtipp (§ 226 II, Hemmschwelle) → Schema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Volker (VO), Anfang 60 | Hausbesitzer, reißt die Mauer ab | `standing/shirt-3`, Kopf `Gray Short`, Brille `Glasses 3`, Hemd Blau `#8DB3F2`, Hose dunkel, Haut `#F0C8A8`. Mimiken `Calm` (redet), `Driven` (arbeitet; redet grimmig in Variante 1), `Concerned|Serious` (redet bedauernd in Variante 2; ertappt), `Contempt` (redet gleichgültig in Variante 3), `Smile` (redet zuversichtlich in Variante 4; froh), `Fear`, `Serious` | `helmut` (Mann, älter) |
| Heike (HE), um 45 | Nachbarin, Eigentümerin des Zauns | `standing/resting-1`, Kopf `Medium Straight`, Oberteil Lila `#B8A9F5`, Haut `#D9A27A`. Mimiken `Calm`, `Concerned|Serious` (redet), `Fear` (ruft), `Suspicious`, `Tired` | `sabrina` (Frau, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links: Volker zur Mauer und zur Tafel), `_r` blickt nach rechts (Heike links im Bild zu ihrem Zaun und zu Volker).
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimiken nur als `Concerned|Serious`. Mundzustände a/o/e bei `VO_redet`, `VO_grimmig`, `VO_bedauert`, `VO_egal`, `VO_zuversicht`, `HE_redet`, `HE_ruft` (je links/rechts) und Lexi. Keine Bärte. 82 Figuren-PNGs in `../peeps/op_029/` (Drive-Master).
- Für Heike war zunächst `pointing_finger-1` vorgesehen; deren Oberteil lässt sich nicht einfärben (rendert schwarz) → `resting-1`.
- **Namen** mit eindeutig deutscher Aussprache, in keiner Vorfolge vergeben (auch nicht in 027/028: Anke, Jürgen, Kunze, Böhm, Elke): Volker, Heike. „Thomas“ ist nur Fallname („Thomas-Fall“), keine Figur.
- **Stimmen** nur aus dem Pool (helmut, sabrina; `niklas`, `ela_froh` nicht gebraucht). Vorfolgen 028 (christian, hilde), 027 (laura_klar, marc, lisa), 026 (helmut, stephan, ela_warm): `helmut` war zuletzt in 026 (Egon) – zwei Folgen Abstand, passend für „Mann, älter“ aus dem zugeteilten Pool. Lea nicht verwendet.
- **Thomas-Fall:** Täter nicht als Figur, keine Opfer, keine Explosion; nur Schiff, Wellenlinie, Fass, Uhr, Urkunde, Münzen als Icons.

**Abweichung von den letzten Folgen:** 028 (Versammlung/Behörde), 027 (WG-Keller, Fahrradladen, Garage), 026 (Dorfkiosk, Scheune bei Nacht). Hier neu: Reihenhausgärten mit Mauer, Holzzaun, Baum und Haus am Samstagmorgen; für die Varianten eine kleine wiederkehrende Bühne (Zaun – Mauer – Volker) rechts neben der Tafel, die sich je Variante in einer Kleinigkeit ändert (Zielscheibe, schiefe Mauer, Fragezeichen, Seil am Baum). Neue Posen gegenüber 026 (`shirt-3`, `resting-1`).
**Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Die alte Mauer** `fall`→`frage2` | Gärten: Heike links, ihr Zaun, Volkers Mauer, Volker, Baum, Haus; Volker schlägt die Steine heraus, Mauer kippt, liegt auf dem Zaun | tabler:`sun`, `tree`, `wall` (gedreht 22°/78°), `fence`, `fence-off`, `hammer`, `brain`; ph:`house` | `Fall · Die alte Mauer` (ab 0,0 s) → `Fall · Die Frage` | ≈ 20 | Hammer (`szene_029hammer_1`), Mauer stürzt (`szene_029mauer_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 11 s | – | `Sachverhalt` | 1 | – |
| **C Sachbeschädigung** `p303`→`keinef` | Wortlautkarten § 303 I und § 15, Block „keine fahrlässige Sachbeschädigung“; Volker, kaputter Zaun | tabler:`fence-off` | `A. Sachbeschädigung, § 303 StGB › objektiver Tatbestand` → `› subjektiver Tatbestand: Vorsatz, § 15 StGB` | ≈ 10 | – |
| **D Wissen und Wollen** `ww`→`formen` | Tafel mit zwei Pegeln (Wissen/Wollen), „drei Vorsatzformen“; Volker | tabler:`brain`, `target` | `A. Sachbeschädigung › Vorsatz: Wissen und Wollen` | ≈ 8 | – |
| **E Variante 1** `var1`→`abs2` | Mini-Bühne; Zielscheibe über dem Zaun, Volker grimmig mit Sprechblase | tabler:`fence`, `wall`, `target` | `… › Vorsatz › Variante 1` → `… › Variante 1: Absicht (dolus directus 1. Grades)` | ≈ 11 | – |
| **F Variante 2** `var2`→`dir2` | Mini-Bühne; Mauer steht schief, Pfeil „nur zum Zaun hin“, Volker bedauert | tabler:`fence`, `wall` (14°) | `… › Variante 2` → `… › Variante 2: direkter Vorsatz (dolus directus 2. Grades)` | ≈ 11 | – |
| **G Thomas-Fall** `thomas`→`th_wiss` | Tafel; rechts Schiff über Wellenlinie, Fass, Uhr, Urkunde, Münzen | tabler:`ship`, `barrel`, `clock`, `file-certificate`, `coins` | `Lehrbuchbeispiel · Thomas-Fall, Bremerhaven 1875` → `… › direkter Vorsatz` | ≈ 12 | – |
| **H Variante 3** `var3`→`raser` | Mini-Bühne; Fragezeichen über der Mauer, Volker gleichgültig | tabler:`fence`, `wall`, `help-circle` | `… › Variante 3` → `… › Variante 3: Eventualvorsatz` | ≈ 11 | – |
| **I Variante 4** `var4`→`straflos` | Mini-Bühne mit Baum; Seil Mauer–Baum, Seil reißt, Mauer liegt auf dem Zaun | tabler:`fence`, `fence-off`, `wall`, `tree`; Seil als Linienzug | `… › Variante 4` → `… › Variante 4: bewusste Fahrlässigkeit` | ≈ 15 | Seil reißt (`szene_029seil_1`) |
| **J Gesamtschau** `gesamt`→`seil` | Tafel; Waage „billigen/vertrauen“, Indizien | tabler:`scale` | `… › Vorsatz › Abgrenzung: Gesamtschau` | ≈ 10 | – |
| **K Tatumstandsirrtum** `irrtum`→`p16b` | Wortlautkarte § 16 I; Karte „alter Grenzplan“, Zaun „fremd“ | tabler:`map`, `fence` | `A. Sachbeschädigung, § 303 StGB › Gegenstück: Tatumstandsirrtum, § 16 Abs. 1 StGB` | ≈ 8 | – |
| **L Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Vorsatzform nur, wenn es darauf ankommt` | ≈ 10 | – |
| **M Klausurschema** `sch`→`k3` | breite Karte, progressiv | – | `Klausurschema` | 11 | – |
| **N Merksatz** `merke`→`m4` | Lexi erklärt, Marker | – | `Merksatz` | ≈ 5 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur als Zustandswechsel (Mauer steht – kippt – liegt; Seil gespannt – gerissen).
**Geräusche:** drei Handlungsgeräusche (Freesound CC0), je einmal, Herkunft in `geraeusche_herkunft.json`.
**Gewalt zurückhaltend:** nur Sachschaden am Zaun. Der Thomas-Fall erscheint ohne Figuren, Opfer und Explosion; der Tod wird nur im Satz „Nach der Lehrbuchdeutung kam es ihm auf den Tod der Menschen an Bord nicht an“ erwähnt.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 303 I, § 15 und § 16 I vollständig, wörtlich nach gesetze-im-internet.de mit Normangabe; Marker synchron zum gesprochenen Wort.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Volker (Anfang 60) schlägt die unteren Steine seiner alten Gartenmauer heraus. Die Mauer kippt auf den neuen Holzzaun seiner Nachbarin Heike, drei Latten brechen.
>
> Variante 1: Der Zaun ärgert Volker, die Mauer soll genau dorthin fallen. Variante 2: Die Mauer kann nur zum Zaun hin fallen, Volker weiß das sicher. Variante 3: Volker hält das für möglich, Abstützen ist ihm zu mühsam. Variante 4: Volker sichert die Mauer mit einem Seil und vertraut darauf; das Seil reißt.
>
> Gegenstück: Volker hält den Zaun nach einem alten Grenzplan für seinen eigenen.
>
> **Hat Volker den Zaun vorsätzlich beschädigt?**
