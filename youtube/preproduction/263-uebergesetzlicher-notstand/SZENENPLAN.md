# Folge 263 · Leben gegen Leben: Übergesetzlicher entschuldigender Notstand – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_263.py`](src/skript_263.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · StGB AT, Format **Streitstand**. Plan-Hook: Eine Stellwerksmitarbeiterin lenkt einen führerlosen Güterzug auf ein Nebengleis, wo ein einzelner Arbeiter steht. Ausgestaltung: Montag, 6:40 Uhr; Anruf aus dem Nachbarstellwerk; Bautrupp mit 5 Arbeitern auf Gleis 1, über Funk nicht erreichbar; Weiche 7 auf das Nebengleis.
Ablauf (laut Auftrag): 1. Hook (Stellwerk → Nachbarstellwerk → Schienenplan → Fragen) → Sachverhalt → Tatbestand § 212 → 2. § 34 (Wortlautkarte), „wesentlich überwiegt“ – Leben nicht abwägbar (h. M.; BVerfGE 115, 118 Rn. 85, 124; Art. 1 Abs. 1 GG) → rechtswidrig → 3. § 35 (Wortlautkarte), Personenkreis (−) → 4. übergesetzlicher entschuldigender Notstand: Herkunft (Ärzteverfahren der Nachkriegszeit, nur Text), Voraussetzungen, Ansichten (Entschuldigungsgrund / persönlicher Strafausschließungsgrund / Gegenansicht beim Umlenken), Gefahrengemeinschaft vs. Weichenstellerfall → 5. Ergebnis je Ansicht, Blase Frau Seefeld → 6. Klausurtipp (Lexi), Schema, Merksatz (Lexi).
**Abgrenzung zu den Referenzfolgen:** 189 (§ 34-Schema, Berghütte) und 013 (Luftsicherheitsgesetz, BVerfGE 115, 118) werden nicht wiederholt, sondern je in einem Satz verwiesen; aus 013 nur Rn. 85/124/130 als Begründung der Unabwägbarkeit.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Seefeld (SE), Ende 20 | Stellwerksmitarbeiterin, stellt die Weiche um | `standing/easing-1` (offene Jacke Orange `#F9A66C` wie eine Warnjacke, Oberteil Weiß, schwarze Hose der Pose), Kopf `Medium Bangs 2` (Haar Braun `#8A5A3C`), Haut `#EDC3A0`; Mimiken `Calm`, `Serious`, `Concerned\|Serious`, `Fear`, `Tired`, `Driven`, `Solemn`, `Eyes Closed`, `Suspicious`; redet: `Concerned\|Serious`, redet2: `Solemn` | `julia` (Frau, jung) |
| Herr Nordmann (NO), um 60 | Fahrdienstleiter im Nachbarstellwerk, meldet den Zug | `standing/shirt-4` (schwarzes Hemd der Pose, Hose Blau `#8DB3F2`), Kopf `No Hair 3` (Haarkranz Grau `#B4B4B4`), Haut `#E3B48C`; redet: `Concerned\|Serious` | `helmut` (Mann, älter) |
| Gleisarbeiter (GA), namenlos | 5 auf Gleis 1, 1 auf dem Nebengleis | graue Silhouetten aus `walking-2`, `walking-3`, `shirt-4`, `easing-1`, `walking-1` mit `hat-hip`, Höhe 130 px, mit Abstand im Schienenplan; kein Gesicht, kein Opferbild | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen, nicht in `namen_reserviert.txt` (eingetragen „263: Seefeld, Nordmann“) und in keiner Text-/Code-Datei unter `youtube/` (Volltextsuche 08.10.2026).
- **Stimmen** nur aus dem Pool (niklas, helmut, ela_froh, julia); `niklas` und `ela_froh` nicht gebraucht. Vorfolgen: 262 (sabrina, marc, william), 261 (lucy, christian, hilde), 260 (helmut, niklas) – `helmut` auch in 260, im Pool aber die einzige ältere Männerstimme.
- **Posen** nicht aus 259–261 (blazer-4, bike, resting-1, crossed_arms-1, robot_dance-3, one_leg_up-2, resting-2, shirt-3, easing-2); keine Polka Dots, keine Prothesen-Posen, keine Bärte, keine Karikatur. Alle Grundmimiken mit geschlossenem Mund; Mundzustände a/o/e für `SE_redet`, `SE_redet2`, `NO_redet` (je links/rechts) und Lexi. 66 Figuren-PNGs in `../peeps/op_263/`.
- **Blickrichtung:** Grundansicht blickt nach links (zum Schienenplan bzw. zur Tafel).

**Setting (neu):** Stellwerksraum (Wand, Fenster mit zwei Gleisen, Stellpult mit Bildschirm und Telefon), Nachbarstellwerk (grünliche Wand, Zug-Icon im Fenster), Schienenplan auf Cremegrund (Gleis 1, Weiche 7, Nebengleis mit Schwellen; Weichenlage als gelbe Markierung). Gegenüber 260 (Wohnung bei Nacht), 261 (Prüfungsamt/Gericht), 262 (Autohandel) neu. Cremegrund durchgehend, Tageslicht.
**Darstellung:** Kein Zusammenstoß, kein Opfer im Bild. Zug als Tabler-Icon `train`, der nie bis zu den Silhouetten fährt; beim Satz „kommt ums Leben“ verschwinden Zug und Silhouette vom Nebengleis, nur eine graue Pille bleibt. Ärzteverfahren der Nachkriegszeit nur als Tafeltext, ohne Bilder und ohne Figur.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Stellwerk** `fall`→`anruf` | Raum, Stellpult; Frau Seefeld erscheint bei „Frau Seefeld“; Telefon klingelt | tabler:`phone-ringing`; Pillen „Montag, 6:40 Uhr“, „Stellwerk“, „Ende 20, im Dienst“, „Anruf: Nachbarstellwerk“ | `Fall · Stellwerk, Montag 6:40 Uhr` (ab 0,0 s) → `Fall · Anruf aus dem Nachbarstellwerk` | Telefon (`szene_263telefon_1`, bei `anruf`) |
| **A2 Nachbarstellwerk** `no1` | Herr Nordmann warnt (Blase) | tabler:`phone`, `train` | `Fall · Warnung: Güterzug führerlos` | – |
| **A3 Schienenplan** `gleis1`→`se2` | Gleis 1 mit 5 Silhouetten, Funk, Blase Seefeld, Zug-Icon links, „Anhalten: unmöglich“, Weiche 7 mit Pfeil, Silhouette auf dem Nebengleis, Weiche umgestellt (Hebel), Zug auf dem Nebengleis, „5 Arbeiter unverletzt“, „1 Arbeiter kommt ums Leben“ (ohne Silhouette, ohne Zug), Blase Seefeld | tabler:`radio`, `train`, `toggle-right` | `Fall · Gleis 1: Bautrupp, 5 Arbeiter` → `· Funk: keine Antwort` → `· Anhalten unmöglich` → `· Weiche 7 auf das Nebengleis?` → `· Weiche 7 umgestellt` → `· 5 gerettet, 1 Arbeiter tot` | Weichenhebel (`szene_263weiche_1`, bei `stellt`) |
| **A4 Fragen** `frage`, `frage2` | Stellwerk, Frau Seefeld still; zwei Fragepillen | tabler:`scale` | `Fall · Strafbar wegen Totschlags?` → `Fall · 1 Leben opfern, um 5 zu retten?` | – |
| **B Sachverhalt** `sv` | Karte vollständig (≈ 9,6 s), kein Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Tatbestand** `tb`→`rw` | Haken „einen Menschen getötet“, „Vorsatz“; Block II. Rechtswidrigkeit | tabler:`train`, `eye`, `scale` | `A. Frau Seefeld, § 212 StGB › I. Tatbestand …` → `› II. Rechtswidrigkeit` | – |
| **D § 34** `p34`→`v189` | Wortlautkarte S. 1, 2, Marker „gegenwärtigen“, „Leben“, „nicht anders abwendbaren“, „das geschützte Interesse“, „wesentlich überwiegt“; Haken Notstandslage, Notstandshandlung; Frage Interessenabwägung; Verweis 189 | tabler:`alert-triangle`, `heartbeat`, `git-fork`, `scale` | `A. Frau Seefeld › II. Rechtswidrigkeit › § 34 StGB · Wortlaut` → `› Notstandslage (+)` → `› einziges Mittel (+)` → `› Interessenabwägung` | – |
| **E1 Leben gegen Leben** `zahl`→`nicht` | Blöcke „Leben von 5 Arbeitern“/„Leben von 1 Arbeiter“, Kreuz „herrschende Meinung: nein“ | tabler:`scale`, `ban` | `… › Interessenabwägung: Leben gegen Leben` → `› Leben nicht abwägbar (h. M.)` | – |
| **E2 BVerfGE 115, 118** `bverfg`→`v013` | Zitatkarte Rn. 85, Rn. 124, Art. 1 Abs. 1 GG, „Das Gericht sprach über den Staat“, Strafrechtslehre, Block „§ 34 (−): rechtswidrig“, Verweis 013 | tabler:`building-bank`, `user-x`, `shield`, `book`, `ban` | `… › BVerfGE 115, 118` → `› Tötung als bloßes Mittel` → `› übertragen auf § 34 StGB` → `… § 34 StGB (−) › rechtswidrig` | – |
| **F § 35** `p35`→`nein35` | Wortlautkarte Abs. 1 S. 1, Marker; Kreuz „kennt sie nicht“; Block „§ 35 StGB (−)“ | tabler:`heartbeat`, `users` | `A. Frau Seefeld › III. Schuld › § 35 StGB · Wortlaut` → `› Personenkreis` → `› Personenkreis (−)` → `(−)` | – |
| **G Herkunft** `ueber`→`offen` | Tafel ohne Figur: ungeschrieben, Nachkriegsverfahren gegen Ärzte, Listen, OGHSt 1, 321; Block BVerfGE 115, 118 Rn. 130 | tabler:`help`, `book-off`, `archive`, `building-bank` | `A. Frau Seefeld › III. Schuld › übergesetzlicher entschuldigender Notstand` → `› Herkunft` → `› BVerfG lässt offen` | – |
| **H Voraussetzungen** `vor`→`v3` | drei Blöcke 1.–3. | tabler:`list-details`, `alert-triangle`, `git-fork`, `heart-handshake` | `… › Voraussetzungen` | – |
| **I Ansichten** `ans`→`a2b` | Block 1 Entschuldigungsgrund (wohl h. L.), Block 2 persönlicher Strafausschließungsgrund (OGH BrZ) | tabler:`help`, `shield-check`, `scale` | `… › Streit: Wie wirkt er?` → `› 1. Entschuldigungsgrund` → `› 2. persönlicher Strafausschließungsgrund` | – |
| **J Gefahrengemeinschaft / Weichensteller** `gg`→`a4` | Zeilen Gefahrengemeinschaft, Weichenstellerfall; Block 3. Gegenansicht, Block „andere“ | tabler:`users-group`, `git-fork`, `user-x`, `help` | `… › Gefahrengemeinschaft` → `› Weichenstellerfall` → `› 3. Gegenansicht: keine Entschuldigung` → `› andere: auch beim Umlenken` | – |
| **K Ergebnis** `lsg`→`l4` | Block straflos, Block Totschlag § 212, Zeile § 213, „Begründung entscheidet“ | tabler:`scale`, `shield-check`, `ban`, `file-text` | `Ergebnis je Ansicht` → … | – |
| **L Stellwerk** `se3` | Frau Seefeld, Blase „Dann hängt alles an diesem Streit.“ | – | `Ergebnis · Frau Seefeld` | – |
| **M Klausurtipp** `tipp`→`k5` | hellgelbe Tafel, vier Blöcke, zwei Zeilen; Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Reihenfolge` → … | – |
| **N Klausurschema** `sch`→`s6` | breite Karte, sechs Zeilen progressiv (I.–IV.) | – | `Klausurschema › …` | – |
| **O Merksatz** `merke`→`m3` | Lexi erklärt, drei Marker | – | `Merksatz` | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 19 Folien; innerhalb harte Schnitte und Pops; Handlung als Zustandswechsel im Schienenplan (Zug links → Weiche umgestellt → Zug auf dem Nebengleis → Nebengleis leer).
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 34 S. 1, 2 vollständig; § 35 Abs. 1 S. 1 vollständig; Zitatkarte BVerfGE 115, 118 Rn. 85 wörtlich (auch gesprochen). Marker synchron zum gesprochenen Merkmal.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Montag, 6:40 Uhr: Frau Seefeld (Ende 20) hat Dienst im Stellwerk. Herr Nordmann aus dem Nachbarstellwerk meldet, dass ein Güterzug führerlos auf ihren Bereich zurollt; die Bremsen greifen nicht.
>
> Auf Gleis 1 arbeitet ein Bautrupp mit 5 Arbeitern, über Funk nicht zu erreichen. Anhalten kann Frau Seefeld den Zug nicht. Sie kann nur Weiche 7 auf das Nebengleis umstellen. Dort steht ein einzelner Arbeiter, auch er ist nicht zu erreichen. Keinen der Arbeiter kennt sie persönlich.
>
> Sie sieht den Arbeiter und weiß, dass der Zug ihn erfassen wird. Sie stellt die Weiche um. Die 5 Arbeiter bleiben unverletzt, der Arbeiter auf dem Nebengleis kommt ums Leben.
>
> **Hat sich Frau Seefeld wegen Totschlags (§ 212 StGB) strafbar gemacht?**
