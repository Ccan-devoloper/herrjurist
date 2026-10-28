# Folge 228 · Sekundäre Darlegungslast § 138 ZPO: Wenn nur der Gegner es weiß – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_228.py`](src/skript_228.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · ZPO, Themenplan-Format „Sonderlage“. Hook nach Plan: Ein Rechteinhaber verklagt den Anschlussinhaber wegen Filesharings, obwohl vier Personen im Haushalt denselben Router nutzen. Beispielfall: Familie Mehnert (Herr und Frau Mehnert, Sohn 24, Tochter 21) nutzt einen Anschluss; eine Filmfirma verklagt Herrn Mehnert auf 1.000 € Schadensersatz. Ablauf: 1. Grundsatz (Verweis 141) → 2. § 138 Abs. 1, 2 und Abs. 3 ZPO (Wortlautkarten) → 3. tatsächliche Vermutung, Voraussetzungen und Inhalt der sekundären Darlegungslast, keine Umkehr der Beweislast → 4. Fall und Gegenfall (pauschales Bestreiten, § 138 Abs. 3; Name des geständigen Kindes) → Klausurtipp Relation (Lexi) → Schema → Merksatz (Lexi).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Mehnert (HM), um 52 | Anschlussinhaber, Beklagter | `standing/robot_dance-2` (schwarzer Pullover, offene Hand), Kopf `Short 1`, Brille `Glasses`; Hose Blau `#8DB3F2`, Haut `#E8B48E`; Mimiken `Calm`, `Serious`, `Smile`, `Suspicious`, `Concerned\|Serious`, `Awe`, `Fear`; spricht mit `Serious` | `marc` (Mann, mittel) |
| Frau Mehnert (FM), um 50 | Ehefrau, Mitnutzerin | `standing/polka_dots` (Oberteil mit Punkten), Kopf `Bangs 2` (Haar `#4A3222`); Hose Grün `#8FD694`, Haut `#C68E6A`; spricht mit `Calm` | `sabrina` (Frau, mittel) |
| Sohn (SO), 24, ohne Namen und Text | Mitnutzer | `sitting/crossed_legs` (sitzt auf dem Sofa), Kopf `Medium 1`; Pullover Gelb `#F9D56E`, schwarze Hose, Haut `#D9A47E` | – |
| Tochter (TO), 21, ohne Namen und Text | Mitnutzerin | `sitting/closed_legs-1` (sitzt auf einem Sitzkissen), Kopf `Buns`; Jacke Lila `#B8A9F5` über Ringelshirt, Haut `#D9A47E` | – |
| Anwältin der Filmfirma (AW), um 40, ohne Namen | Prozessvertreterin der Klägerin | `standing/blazer-2` (dunkelblauer Blazer `#3A4A6B`, weißes Shirt, Beinprothese – beiläufig, sachliche Rolle), Kopf `Medium Bangs 3`, Haut `#F2D3BD`; spricht mit `Serious` | `laura_ruhig` (Frau, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Sitzende Figuren über `hoehe` im gleichen Maßstab wie die stehenden (Sohn 372 px, Tochter 352 px bei 470 px stehend). **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e (Explaining / Concerned Fear / Hectic, Schnitt bei 60 %) nur in `HM_redet`, `FM_redet`, `AW_redet` (je links/rechts) und Lexi. Keine Bärte, keine Karikatur, keine Täterfigur: Die Familie bleibt sympathisch, offen bleibt, wer den Film angeboten hat. Figuren-PNGs: `../peeps/op_228/` (78 Dateien, nicht im Repository, im Drive-Master).

**Stimmen:** nur aus dem Pool (william, sabrina, marc, laura_ruhig). `william` nicht verwendet, weil Folge 225 ihn für die Hauptfigur nutzte; `laura_ruhig` (auch 225) für die Anwältin, weil drei Sprechrollen aus vier Poolstimmen zu besetzen waren. Die parallel laufenden Folgen 226/227 nutzen andere Stimmen.

**Namen:** Mehnert – eindeutig deutsch (Meh-nert), nicht auf der Koordinatorliste, nicht in `namen_reserviert.txt`, per Volltextsuche unter `youtube/` (`*.py`, `*.md`, `*.csv`, `*.json`) ohne Treffer; vor der Vertonung als „228: Mehnert“ eingetragen. Verworfen: Bruno (009/011/015), Greta (003). Sohn, Tochter und Anwältin bleiben namenlos (weniger Ausspracherisiko).

**Abweichung von den letzten Folgen:**
- Posen der Folgen 223–225 und der parallel laufenden 226/227 (blazer-1/-3/-4, shirt-2/-3/-4, easing-1/-2, pointing_finger-1/-2, resting-1/-2, robot_dance-1 [nur Lexi]/-3, walking-1/-2/-3, crossed_arms-1/-2) nicht verwendet; erstmals seit Langem zwei sitzende Posen. Polka Dots zuletzt in keiner der Folgen 223–227.
- Schauplatz neu: Wohnzimmer einer Familie (Sideboard mit Router, Sofa, Sitzkissen); 225 Straße mit Baustelle, 224 Wohnung/Polizei/Gericht, 223 Werkstatt/Bank. Die Klage als freie Bühne mit Klageschrift statt Gerichtssaal.
- Cremegrund durchgehend, Tageslicht (die Tatzeit 21:47 Uhr wird nur genannt, kein Nachtverlauf).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Wohnzimmer** `fall`–`fm1` | Sideboard mit Router links, Sohn auf dem Sofa, Tochter auf dem Kissen (beide blicken nach rechts), Frau Mehnert (blickt nach rechts), Herr Mehnert rechts (blickt nach links) | tabler:`router` (Weiß), `wifi`, `device-laptop`, `device-tablet` (Weiß), `mail-opened` (Weiß), `movie` (Lila); Sideboard, Sofa (Türkis), Kissen (Orange) programmatisch | `Fall · 4 Menschen, 1 Router` → `· Familie Mehnert` → `· Post von einer Filmfirma` → `· Der Vorwurf` → `· Herr Mehnert` → `· Frau Mehnert` | Raum ab 0,0 s mit allen vier Figuren und Namensschildern · WLAN · je Nennung lächelt die Person · Geräte bei „surfen“ · Brief · Film, „Spielfilm in einer Tauschbörse“ · „12. Mai um 21:47 Uhr“ · Herr Mehnert redet · Frau Mehnert redet | Brief wird geöffnet (`szene_228brief_1`) |
| **A2 Die Klage** `klage`–`frage2` | freie Bühne: Anwältin links (blickt nach rechts), Herr Mehnert rechts | tabler:`file-text`, `home-question` (Gelb) | `Fall · Die Klage` → `· Das Argument der Anwältin` → `· Die Frage` | Klageschrift, „Klage: 1.000 € Schadensersatz“ · Anwältin redet („IP-Adresse“) · „weiß nur die Familie“ · Frage | – |
| **B Sachverhalt** `sv` | Sachverhaltskarte vollständig, 5,0 s Lesepause | – | `Sachverhalt` | 1 | – |
| **C Aufbau** `plan`–`p5` | Tafel, Anwältin und Herr Mehnert rechts | tabler:`scale`, `book`, `home-question`, `users`, `list-numbers` | `Aufbau · 5 Schritte` | fünf Schritte nacheinander | – |
| **D 1. Grundsatz** `g1`–`g3` | Tafel | tabler:`movie`, `scale` | `1. Grundsatz · § 97 Abs. 2 UrhG` → `› Darlegungs- und Beweislast` → `› anspruchsbegründende Tatsache` | Anspruch · Block Beweislast · BearShare Rn. 14 · Haken · Verweis Video „Beweislast ZPO“ | – |
| **E § 138 Abs. 1, 2** `e1`–`w2` | Tafel mit zwei Wortlautkarten | tabler:`book`, `messages` | `2. § 138 ZPO` → `› Abs. 1: Wahrheitspflicht` → `› Abs. 2: Erklärungspflicht` | Karten mit Markern „vollständig“, „der Wahrheit gemäß“, „Jede Partei“, „zu erklären“ | – |
| **F § 138 Abs. 3** `w3`–`w5` | Tafel mit Wortlautkarte | tabler:`file-certificate`, `hand-stop`, `question-mark` | `› Geständnisfiktion` → `› ausdrückliches Bestreiten` | Marker „nicht ausdrücklich bestritten“, „zugestanden anzusehen“ · Haken „bestreitet ausdrücklich“ · „Reicht das?“ | – |
| **G Vermutung, Wissensgefälle** `v1`–`v3` | Tafel, zwei Blöcke | tabler:`router`, `home-question`, `home`, `world-www` | `3. Sekundäre Darlegungslast` → `› tatsächliche Vermutung` → `› nur die Familie weiß es` | Frage · Vermutung mit Fundstelle · Block Familie · Block Filmfirma | – |
| **H Voraussetzungen** `v4`, `v5` | Tafel | tabler:`eye-off`, `message-circle-question` | `3. › Voraussetzungen` → `› sekundäre Darlegungslast des Gegners` | drei Haken nacheinander · BearShare Rn. 17 · Block „Dann in der Regel“ | – |
| **I Inhalt** `i1`–`i4` | Tafel mit Zitatkarte BearShare Rn. 18, Frau und Herr Mehnert rechts | tabler:`message-circle-question`, `users`, `search`, `device-laptop` | `3. › Was muss er vortragen?` → `› Nachforschung` → `› Grenzen` | Zitat mit Markern „andere Personen“, „selbständigen Zugang“, „als Täter“ · Haken Nachforschung · zwei Kreuze „nicht nötig“ · Afterlife | – |
| **J Keine Umkehr** `u1`, `u2` | Tafel | tabler:`scale`, `book` | `3. › keine Umkehr der Beweislast` → `› Grenze: § 138 Abs. 1, 2 ZPO` | Block „Beweislast bleibt“ · Grenze · Kreuz „keine Pflicht, alles zu liefern“ | – |
| **K 4. Fall im Wohnzimmer** `f1`–`f2` | Rückkehr ins Wohnzimmer (Herr Mehnert berichtet, was er zu Hause erfragt hat) | wie A1, zusätzlich tabler:`key` (Gelb) | `4. Der Fall · Herr Mehnert hat alle gefragt` → `› Vortrag` → `› niemand hat etwas zugegeben` | Familie · Herr Mehnert redet · je Nennung lächelt die Person · Geräte · Schlüssel bei „WLAN“ · „alle zu Hause“ · „Zugegeben hat es niemand“ | – |
| **L 4. Ergebnis** `f3`–`f5` | Tafel | tabler:`circle-check`, `scale`, `file-x` | `4. Der Fall › …` | Haken · Kreuz „keine Vermutung“ · Block Beweislast Filmfirma · „Klage abgewiesen“ | – |
| **M Gegenfall** `gf`–`gf3` | Tafel, Herr Mehnert allein mit Blase | tabler:`question-mark`, `clock` | `4. Der Gegenfall` → `› pauschales Bestreiten` → `› nachvollziehbarer Vortrag` | „sagt nur“ · Herr Mehnert redet · Kreuz · Kriterien einzeln zum Wort | – |
| **N Folge des Gegenfalls** `gf4`–`loud` | Tafel | tabler:`file-certificate`, `gavel`, `id` | `› § 138 Abs. 3 ZPO` → `› Haftung als Täter` → `› Name nennen` | Kreuz · § 138 Abs. 3 · Block Haftung · Block Name nennen | – |
| **O Klausurtipp** `tipp`–`t3` | hellgelbe Tafel, Lexi rechts | Streamline Freehand: Warnsymbol | `Klausurtipp · Relation` → `› Erheblichkeit` → `› Beweisstation` | Stationen nacheinander, Beklagtenstation gelb · Erheblichkeit · Kreuz pauschal · Haken genug vorgetragen | – |
| **P Klausurschema** `sch`–`k4` | breite Schema-Karte (x ≤ 1820) | – | `Klausurschema › I.` … `› IV. Ergebnis` | I. bis IV. nacheinander, II. und IV. zweizeilig | – |
| **Q Merksatz** `merke`, `mk2` | Merkkarte, Lexi rechts | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

## Sachverhaltskarte (Szene B)

Herr und Frau Mehnert leben mit ihrem 24-jährigen Sohn und ihrer 21-jährigen Tochter zusammen. Alle vier nutzen mit eigenen Geräten denselben Internetanschluss; das WLAN ist mit einem Passwort geschützt, das alle kennen. Anschlussinhaber ist Herr Mehnert. Eine Filmfirma, Inhaberin der ausschließlichen Nutzungsrechte an einem Spielfilm, lässt ermitteln: Am 12. Mai 2026 um 21:47 Uhr wurde der Film über diesen Anschluss in einer Tauschbörse zum Herunterladen angeboten. Sie verklagt Herrn Mehnert auf 1.000 € Schadensersatz. Herr Mehnert bestreitet, den Film angeboten zu haben. Er hat alle im Haushalt gefragt; niemand hat etwas eingeräumt. An dem Abend waren alle vier zu Hause. — Frage: Was muss Herr Mehnert vortragen – und wer muss was beweisen?

## Ton

Erzählerin und Lexi: Carla Blum. Figurenrede: Herr Mehnert (`me1`, `me2`, `me3`), Frau Mehnert (`fm1`), Anwältin (`aw1`). Ein Handlungsgeräusch (Brief), Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json). Schiebeblenden stumm.
