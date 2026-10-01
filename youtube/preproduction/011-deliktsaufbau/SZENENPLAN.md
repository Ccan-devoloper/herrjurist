# Folge 011 · Deliktsaufbau Strafrecht: Tatbestand, Rechtswidrigkeit, Schuld – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_011.py`](src/skript_011.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Examenswissen (Mi), Themenplan-Format „Schema“. Ein frei erfundener Alltagsfall trägt den ganzen dreistufigen Aufbau des vorsätzlichen vollendeten Begehungsdelikts: Am Uferweg rast der Radfahrer Holger knapp an der Joggerin Nele vorbei; dreißig Meter weiter steht er abgestiegen und trinkt, Nele stößt ihn um, er schürft sich den Ellenbogen auf. Prüfung § 223 I StGB: I. Tatbestand (objektiv: Handlung, Erfolg, Kausalität, objektive Zurechnung [Lehre]; subjektiv: § 15, Vorsatz, § 16-Abwandlung) → II. Rechtswidrigkeit (Indiz [Lehre], § 32 scheitert an der Gegenwärtigkeit) → III. Schuld (§§ 19, 20, 35, 17) → Ergebnis, § 230 → Gegenfall (Hook des Themenplans: Holger will sie anfahren → Notwehr, Prüfung endet bei II.) → Klausurtipp → Schema → Merksatz. Vorab „Warum drei Stufen?“ mit §§ 32 I, 20, 29 StGB (Kernfrage des Plans).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Nele (NE), Mitte 50 | Joggerin, Täterin im Hauptfall, Verteidigerin im Gegenfall | `standing/walking-1` (läuft) und `standing/resting-1` (steht), beide Reihe -1: Laufshirt Orange `#F9A66C`, schwarze Hose; Kopf `Gray Medium` (Haar `#C3C6CF`), Haut `#E8B894`. Mimiken `Calm`, `Fear` (Schreck/Angst), `Very Angry` (Wut, redet), `Serious` (denkt), `Concerned|Serious` (ertappt), `Smile` (erleichtert) | `lisa` (Frau, älter) |
| Holger (HO), um 40 | Radfahrer | `sitting/bike` (fährt; Jacke Blau `#8DB3F2`, Oberteil Weiß, Rahmen Blau) und `standing/blazer-4` (steht; gleiche Jacke, gleiches Oberteil); nach dem Sturz `sitting/hands_back-2` (kniet am Boden; diese Pose hat keine Jacke, Oberteil daher im Jackenblau – **Abweichung** vom gleichen Outfit, wie in 010); Kopf `Short 2`, Haut `#C68A62`. Maßstab über die gemessene Kopfbreite angeglichen (Rad 1,10 × FH, Boden 0,66 × FH). Mimiken `Driven` (fährt, redet), `Very Angry` (Gegenfall), `Calm`, `Smile` (trinkt), `Concerned|Serious` und `Tired` (am Boden) | `marc` (Mann, mittel) |
| Herr Albrecht (AL), um 70 | Angler am Ufer, Zeuge | `standing/shirt-3`, Hemd Grün `#8FD694`; Kopf `Gray Short`, Schnurrbart `Moustache 6` (Mund bleibt sichtbar, Lippenbilder geprüft), Brille `Glasses 4`, Haut `#F0C8A8`. Mimiken `Calm`, `Suspicious` (schaut), `Serious` (redet) | `william` (Mann, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links, `_r` nach rechts (Nele und Albrecht links in den Fallszenen blicken nach rechts zu Holger; Holger rechts blickt nach links). Keine Prothesen-Posen. `pointing_finger-1` (Arm erhoben, für „Dehnen“) wurde verworfen, weil das Oberteil dort nicht einfärbbar ist und die Statur abweicht. **Alle Grundmimiken mit geschlossenem Mund** (`Concerned` nur als `Concerned|Serious`); Mundzustände a/o/e nur in `NE_redet`, `HO_rad_redet`, `AL_redet` (je links/rechts) und Lexi. Figuren-PNGs: `../peeps/op_011/` (66 Dateien, nicht im Repository, im Drive-Master).

**Namen und Stimmen:** Nach der Vorgabe des Kanalinhabers (einheitliche Aussprache) Namen mit eindeutig deutscher Aussprache: Nele, Holger, Albrecht (der Radfahrer hieß im ersten Entwurf „Tim“, vor der Vertonung umbenannt). Stimmen ausschließlich aus dem zugeteilten Pool (laura_klar, marc, lisa, william); `laura_klar` nicht gebraucht. `marc` sprach in 003 und 007, im Pool nicht vermeidbar; keine Stimme aus 010 (laura_ruhig, timo, stephan). Lea nicht verwendet.

**Abweichung von den letzten Folgen:**
- 010: Einrichtungshaus (Zivilrecht); 009: Werkstatt/Fahrradladen/Straßenecke (Klausuraufbau, Stoß bei der Flucht); 008: Stadtpark; 007: Wohnhaus bei Nacht.
- Hier: Uferweg am Fluss bei Tag (Flussband, Angler mit Rute, Bäume), ein Radfahrer statt Ladenszene; drei neue Figuren, neue Posen (`walking-1`, `resting-1`, `sitting/bike`, `blazer-4` mit neuem Kopf, `hands_back-2`, `shirt-3` mit neuem Kopf/Bart/Brille).
- Der Themenplan-Hook (Joggerin, Park) wird zum Gegenfall; der Park wird wegen Folge 008 nicht wiederholt.

## Szenen

Alle Szenen bei Tag auf Cremegrund.

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Am Uferweg** `fall`→`sprung` | Flussband, Wegkante, Albrecht angelt links (blickt nach rechts), Nele joggt (blickt nach rechts), Holger fährt von rechts heran (blickt nach links) | tabler:`tree`, `ripple` (Blau), `fish-hook`; Angelrute/Schnur als Linienzug | `Fall · Am Uferweg` (ab 0,0 s) | 1 Ufer mit Albrecht · 2 Nele joggt · 3 „joggt ihre Runde“ · 4 Holger fährt heran · 5 „viel zu schnell, zu knapp“ · 6 Holger redet, Blase „Platz da!“, Nele erschrickt · 7 Nele springt zur Seite (Pfeil) | fahrendes Rad (`szene_011rad_1`) |
| **B Dreißig Meter weiter** `halt`→`lernst` | Holger steht neben dem Rad und trinkt, Nele kommt wütend, läuft hin, Stoß, Holger am Boden, umgestürztes Rad; Albrecht als Zeuge | ph:`bicycle` (Weiß; gestürzt um 180° gedreht), tabler:`bottle`, `bandage` (Rot) | `Fall · Dreißig Meter weiter` → `Fall · Die Frage` | 1 Holger steht · 2 trinkt (Flasche) · 3 „steigt ab, trinkt in Ruhe“ · 4 Nele läuft hin (Bewegung) · 5 „Stoß mit beiden Händen“ · 6 Holger am Boden, Rad umgestürzt · 7 Pflaster · 8 „Schürfwunde am Ellenbogen“ · 9 Nele redet, Blase „Das war für eben!“ · 10 Albrecht redet, Blase „Der stand doch längst!“ · 11 Frage-Pille · 12–14 I./II./III. zum Wort | Sturz des Rads (`szene_011sturz_1`) |
| **C Sachverhalt** `sv` | Sachverhaltskarte vollständig, ≈ 9,7 s (5 s Lesepause) | – | `Sachverhalt` | 1 | – |
| **D Warum drei Stufen?** `drei`→`ssch` | Tafel, Nele denkt | tabler:`book`, `shield`, `user-exclamation` | `Warum drei Stufen?` › `I. Tatbestand` › `II. Rechtswidrigkeit` › `III. Schuld` | drei Farbblöcke zum Wort, Icon wechselt | – |
| **E Das Gesetz trennt** `gesetz`→`g29` | Tafel, Nele ruhig | tabler:`shield`, `brain`, `users-group` | `… › Das Gesetz trennt` › `§ 20 StGB` › `§ 29 StGB` | § 32 I · „nicht rechtswidrig“ · § 20 · „ohne Schuld“ · § 29 · „jeder nach eigener Schuld“ | – |
| **F I. 1. objektiv: Handlung, Erfolg** `tb`→`wunde` | Tafel; rechts Holger am Boden | tabler:`hand-stop` (Orange), `mood-sad`, `bandage` | `A. Nele, § 223 I StGB › I. Tatbestand › 1. objektiv` › `Tathandlung` › `Erfolg` | Titel · a) Tathandlung (✓) · Definition Misshandlung zeilenweise · Sturz mit Schürfwunde (✓) · Gesundheitsschädigung (✓) | – |
| **G Kausalität, Zurechnung** `kausal`→`zurech` | Tafel; rechts Kausalkette Stoß → Sturz → Schürfwunde, Ring „Gefahr verwirklicht“ | `hand-stop`, ph:`bicycle` (gedreht), `bandage` | `… › Kausalität` → `… › objektive Zurechnung` | Formel · ohne Stoß kein Sturz (✓) · Kette · objektive Zurechnung (Lehre) · Ring · obj. Tatbestand erfüllt (✓) | – |
| **H I. 2. subjektiv** `subj`→`vorsatz` | Tafel; Nele, Denkblase „umstoßen!“ | tabler:`book` | `… › 2. subjektiv, § 15 StGB` → `› Vorsatz` | § 15 zeilenweise · Vorsatz · zwei Haken · Denkblase | – |
| **I Abwandlung § 16** `p16`→`tb_erg` | Tafel; Nele dehnt sich (blickt nach links), hinter ihr Albrecht als „jemand“, Pfeil Armschwung | – | `… › Tatumstandsirrtum, § 16 StGB` → `… › I. Tatbestand › erfüllt` | Abwandlung · „weiß sie nicht“ · § 16 · § 229 · Block „Tatbestand erfüllt“, Nele im Fall | – |
| **J II. Rechtswidrigkeit** `rw`→`rw_erg` | Tafel; Nele und Holger, Zeitleiste Raserei → Stoß „vorbei“, Holger trinkt | tabler:`bottle` | `A. Nele … › II. Rechtswidrigkeit` › `Notwehr, § 32 StGB` › `gegenwärtiger Angriff?` → `› II. rechtswidrig` | Indiz (Lehre) · Rechtfertigungsgrund · § 32 · Zeitleiste · Kreuz „kein Angriff mehr“ · Block „rechtswidrig“ | – |
| **K III. Schuld** `schuld`→`schuld_erg` | Tafel; Nele | tabler:`mood-kid` (Gelb), `brain` (Lila) | `… › III. Schuld` › `Schuldfähigkeit, §§ 19, 20 StGB` › `Entschuldigungsgründe` › `Unrechtsbewusstsein, § 17 StGB` → `› III. schuldhaft` | § 19 · § 20 · Nele erwachsen (✓) · § 35 · § 17 · Block „schuldhaft“ | – |
| **L Ergebnis** `ergebnis`→`antrag` | Tafel; Nele (ertappt) und Holger | tabler:`file-text` | `Ergebnis` → `Ergebnis › Strafantrag, § 230 StGB` | Ergebnisblock · § 230 · „Strafantrag?“ | – |
| **M Gegenfall (Szene)** `gegen` | Uferweg; Holger lenkt absichtlich auf Nele zu, sie stößt ihn vom Rad | ph:`bicycle` (gedreht) | `Gegenfall · Holger will Nele anfahren` | Nele joggt · Holger fährt zu · „absichtlich auf Nele zu“, Nele erschrickt · Holger am Boden, „Stoß vom Rad“ | fahrendes Rad, Sturz |
| **N Gegenfall (Prüfung)** `gegen2`→`ende` | Tafel; rechts Stufenleiter I. ✓ / II. ✗ / III. grau „nicht mehr geprüft“, Nele | Fluent Emoji High Contrast Haken/Kreuz | `Gegenfall › II. Rechtswidrigkeit › Notwehr, § 32 StGB` → `› gerechtfertigt` → `› Prüfung endet bei II.` | vier Haken zum Wort · Tatbestand bleibt erfüllt · Block „gerechtfertigt“ · Stufenleiter | – |
| **O Klausurtipp** `tipp`→`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Schwerpunkt setzen` → `Klausurtipp · Unproblematisches kurz` | zeilenweise | – |
| **P Klausurschema** `sch`→`k4` | Schema baut sich Punkt für Punkt auf | – | `Klausurschema` | I · 1. · 2. · II · III · Unrechtsbewusstsein · Strafantrag | – |
| **Q Merksatz** `merke`→`m4` | Lexi erklärt (redet), vier Zeilen mit Marker | – | `Merksatz` | vier Zeilen zum Wort | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb der Folien harte Schnitte und Pops; Bewegungen: Holger fährt heran (A, M), Nele läuft zu Holger (B).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_011rad_1`, `szene_011sturz_1`), je zweimal eingesetzt (Hauptfall und Gegenfall), Herkunft in `geraeusche_herkunft.json`.
**Gewalt zurückhaltend:** Der Stoß selbst wird nicht gezeigt (Pille „Stoß mit beiden Händen“, danach Holger am Boden); keine Verletzungsdarstellung außer Pflaster-Icon.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Sonntagmorgen am Uferweg: Der Radfahrer Holger rast viel zu schnell und zu knapp an der Joggerin Nele (Mitte 50) vorbei und ruft „Platz da!“. Nele springt zur Seite. Dreißig Meter weiter hält Holger an, steigt ab und trinkt in Ruhe. Nele läuft zu ihm und stößt ihn mit beiden Händen um; dass er sich dabei verletzt, nimmt sie in Kauf. Holger stürzt über sein Rad und schürft sich den Ellenbogen auf. Nele: „Das war für eben!“ Der Angler Herr Albrecht: „Der stand doch längst!“
>
> Annahme: Nele ist erwachsen, nüchtern und gesund.
>
> **Hat Nele sich strafbar gemacht?**
