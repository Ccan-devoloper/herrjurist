# Folge 039 · Anklageklausur Aufbau: Gutachten, Prozessuales, Abschlussverfügung – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_039.py`](src/skript_039.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · StPO-Praxis, Themenplan-Format „Schema“. Beispielfall (kleiner Ermittlungsfall statt der Einbruchsserie des Plans): Herr Rösch steckt im Elektronikmarkt Kopfhörer für 249 € ein, legt die leere Packung zurück und zahlt nur eine Cola; Ladendetektiv Brehm stellt ihn, Einlassung „Bezahlen vergessen“. Drei Tage später „Du Idiot!“ vor dem Markt, Brehm stellt keinen Strafantrag. Im August liegt die Akte bei der Staatsanwältin. Ablauf: Fall → Frage → Sachverhalt → Aufbau (drei Teile, Länderunterschiede) → Maßstab § 170 I StPO (hinreichender Tatverdacht) → A. materiell-rechtliches Gutachten (Diebstahl, Beweiswürdigung aus der Akte, Beleidigung offen) → B. prozessuales Gutachten (Strafantrag und Frist, Zuständigkeit, prozessuale Tat § 264 StPO) → C. Abschlussverfügung (Einstellung § 170 II, Abgrenzung §§ 153/154, Vermerk § 169a, Anklage) → Anklageschrift § 200 → Klausurtipp → Schema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Rösch (RO), 24 | Beschuldigter (Diebstahl, Beleidigung) | Pose `standing/easing-1` (offenes blaues Hemd `#8DB3F2` über weißem Shirt, schwarze Hose), Kopf `Short 5`, ohne Bart, Haut `#F0C8A8`; Mimiken `Calm`, `Cheeky\|Smile` (cool), `Concerned\|Serious` (redet, ertappt), `Very Angry` (redet, schimpft), `Fear`, `Suspicious` | `niklas` (Mann, jung) |
| Herr Brehm (BR), um 50 | Ladendetektiv, Zeuge, Verletzter der Beleidigung | Pose `standing/crossed_arms-2` (verschränkte Arme, schwarzer Pullover, Hose `#5A5A6A`), Kopf `No Hair 2`, Brille `Glasses 3`, ohne Bart, Haut `#D9A47E`; Mimiken `Calm`, `Serious` (redet), `Contempt` (beleidigt), `Suspicious`, `Tired` (kein Strafantrag) | `stephan` (Mann, mittel) |
| Staatsanwältin (SA), um 45, ohne Namen | Abschlussverfügung | Pose `standing/blazer-4` (lila Blazer `#B8A9F5`, weißes Oberteil, schwarze Hose), Kopf `Long`, ohne Brille, Haut `#C68E6A`; Mimiken `Calm`, `Driven` (redet), `Serious`, `Smile`, `Suspicious` | `laura_klar` (Frau, mittel; „Sharp and Professional“) |
| Lexi | Moderatorin: Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links (zur Tafel bzw. zum Regal und zur Kasse), `_r` blickt nach rechts (Rösch zum Detektiv). Keine Prothesen-Posen (`blazer-1/-2`, `shirt-1/-2`), keine Bärte. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in den sprechenden Ansichten `RO_redet`, `RO_wut`, `BR_redet`, `SA_redet` (je links/rechts) und Lexi. Täterrolle ohne Herkunfts- oder Hautfarben-Klischee (heller Hautton, Alltagskleidung). Stimmen ausschließlich aus dem zugeteilten Pool (`sabrina` nicht gebraucht). **Namen mit eindeutig deutscher Aussprache**, nicht in der Liste vergebener Namen und in keiner früheren Folge verwendet: Rösch, Brehm (Lorenz und Brandt waren schon in 013/004 vergeben und wurden deshalb verworfen); die Staatsanwältin bleibt ohne Namen. Figuren-PNGs: `../peeps/op_039/` (64 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 038 (Körperverletzung), 037 (Arbeitnehmerhaftung), 030 (Treppenhaus, Schreibtisch mit Laptop, Sitzungssaal), 009 (Fahrradladen, Werkstatt, Straßenecke). 039: Elektronikmarkt mit Regal, Kamera und Kasse; Gehweg vor dem Markt; Schreibtisch mit Aktenstapel bei der Staatsanwaltschaft (kein Laptop, kein Sitzungssaal). Neue Posen (`easing-1`, `crossed_arms-2`, `blazer-4`), andere Stimmen als in 030 (lea, william, laura_ruhig). Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Im Elektronikmarkt** `fall`→`r1` | Regal links, Kamera, Kasse in der Mitte; Rösch erst am Regal (blickt zum Regal), dann rechts der Kasse; Brehm rechts | tabler:`headphones` (Blau/Gelb/Lila/Grün), `package` (leere Packung), `device-cctv`, `cash-register`, `bottle` (Rot), `coins` (Gelb); Regal und Theke als `karte`/`fl_block` | `Fall · Im Elektronikmarkt` → `Fall · Der Ladendetektiv` | Laden ab 0,0 s · Anfang März · Rösch am Regal · 249 € · Ring um die Packung · Kopfhörer wandern in die Jacke · leere Packung zurück · Kasse, Cola, Münzen · Detektiv · Brehm redet (Blase) · Fund · Rösch redet (Blase) | Münzen auf der Theke (`szene_039muenzen_1`) |
| **B Vor dem Markt** `drei`→`kein` | Markt links, Rösch blickt nach rechts zu Brehm | tabler:`building-store` (Gelb), `calendar-event`, `file-text` | `Fall · Drei Tage später` → `Fall · Kein Strafantrag` | drei Tage später · Rösch, Brehm · Rösch schimpft (Blase), Brehm verärgert · Polizei · kein Strafantrag (Kreuz), Brehm müde | – |
| **C Bei der Staatsanwaltschaft** `akte`→`frage2` | Schreibtisch, Akte fällt darauf; Staatsanwältin rechts | tabler:`desk` (Holz), `folders` (Gelb) | `Fall · Bei der Staatsanwaltschaft` → `Fall · Die Frage` | Akte fällt · August · Staatsanwältin redet (Blase) · Diebstahl · Beleidigung · Frage · „Vom Gutachten …“ | Akte auf dem Tisch (`szene_039akte_1`) |
| **D Sachverhalt** `sv` | Karte vollständig, ≈ 9,7 s | – | `Sachverhalt` | 1 | – |
| **E Aufbau** `aufbau`→`vermerk` | Tafel, Staatsanwältin allein | tabler:`folders`, `map-pin` (Rot), `file-description` | `Aufbau · drei Teile` → `› von Land zu Land verschieden` → `› Bearbeitervermerk` | A · B · C · Konvention · Strafantrag wo? · Bearbeitervermerk | – |
| **F Maßstab** `p170`→`wahr` | Tafel, Rösch und Staatsanwältin | tabler:`file-text`, `scale` (Gelb) | `Maßstab › § 170 Abs. 1 StPO` → `› hinreichender Tatverdacht` → `› Verurteilung wahrscheinlich` | Wortlautkarte § 170 I mit zwei Markern · „= hinreichender Tatverdacht“ (BVerfG) · Wortlautkarte BGH StB 58/25 Rn. 5 mit zwei Markern | – |
| **G1 A. Diebstahl** `mat`→`einl` | Tafel, Rösch und Brehm | tabler:`headphones` | `A. Materiell-rechtliches Gutachten` → `› Tat 1: Diebstahl, § 242 Abs. 1 StGB` → `› Tat 1: Einlassung` | Strafbar? · Nachweisbar? · Tat 1 · Wegnahme (Haken) · Einlassung · kein Vorsatz | – |
| **G2 A. Beweiswürdigung** `bw`→`bw3` | Tafel | tabler:`device-cctv`, `bottle`, `scale` | `› Tat 1: Beweiswürdigung` → `› Tat 1: hinreichender Tatverdacht` | Video · Cola · Einlassung (Kreuz) · wahrscheinlich (Haken) · hinreichender Tatverdacht, Rösch erschrickt | – |
| **G3 A. Beleidigung** `bel`→`scheit` | Tafel | tabler:`calendar-event` | `› Tat 2: Beleidigung, § 185 StGB` → `› Tat 2: kann offenbleiben` | „Du Idiot!“ · offen · Zeuge · scheitert woran? | – |
| **H1 B. Strafantrag** `proz`→`diebst` | Tafel, Brehm und Staatsanwältin | tabler:`signature`, `hourglass-empty`, `calendar-x` (Rot), `headphones` | `B. Prozessuales Gutachten` → `› Prozessvoraussetzungen` → `› Tat 2: Strafantrag, § 194 Abs. 1 StGB` → `› Tat 2: Antragsfrist, § 77b StGB` → `› Tat 2: Verfahrenshindernis` → `› Tat 1: kein Strafantrag nötig` | Wortlautkarte § 194 I 1 · Frist · Juni (Kreuz) · Verfahrenshindernis · Diebstahl verfolgbar (Haken) | – |
| **H2 B. Zuständigkeit** `zust`→`strafr` | Tafel, Staatsanwältin allein | tabler:`map-pin`, `building-bank` (Grün), `gavel` (Holz) | `› Zuständigkeit` → `› örtlich: § 7 Abs. 1 StPO` → `› sachlich: § 24 Abs. 1 GVG` → `› Strafrichter, § 25 Nr. 2 GVG` | örtlich · sachlich · Strafrichter · Anklage zum AG | – |
| **H3 B. Prozessuale Tat** `tat`→`jede` | Tafel, Rösch und Staatsanwältin | tabler:`folders`, `calendar-event` | `› prozessuale Tat, § 264 StPO` → `› zwei prozessuale Taten` → `› je Tat eine Entscheidung` | Wortlautkarte BGH GSSt 1/23 Rn. 25 mit drei Markern · Tat 1 · Tat 2 · je Tat eine Entscheidung | – |
| **I C. Abschlussverfügung** `verf`→`ankl` | Tafel, Rösch und Staatsanwältin | tabler:`file-x` (Rot), `mail`, `file-check` (Grün) | `C. Abschlussverfügung` → `› Tat 2: Einstellung, § 170 Abs. 2 StPO` → `› Mitteilung an den Beschuldigten` → `› Abgrenzung: §§ 153, 154 StPO` → `› Tat 1: Vermerk, § 169a StPO` → `› Tat 1: Anklage zum Strafrichter` | Wortlautkarte § 170 II 1 · Mitteilung · §§ 153/154 · Vermerk · Anklage (Haken) | – |
| **J Anklageschrift** `p200`→`rist` | Tafel links, Entwurf der Anklageschrift als Karte, Staatsanwältin | – | `› Anklageschrift, § 200 Abs. 1 StPO` → `› Anklageschrift: Anklagesatz` → `› Anklageschrift: Beweismittel, Gericht` → `› Anklageschrift, § 200 Abs. 2 StPO` | Wortlautkarte § 200 I mit acht Markern, synchron dazu die Zeilen des Entwurfs · Abs. 2 · Nr. 112 RiStBV | – |
| **K Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · erst die prozessualen Taten` → `Klausurtipp · Anklagesatz ohne Beweiswürdigung` | Zeile für Zeile, Kreuz bei „Beweiswürdigung“ | – |
| **L Klausurschema** `sch`→`sC2` | Schema baut sich auf | – | `Klausurschema` | A · B · C · I. · II. mit Unterzeilen | – |
| **M Merksatz** `merke`, `mz` | Lexi erklärt (redet), Merksatz mit Marker | – | `Merksatz` | Satz 1 · drei Marker · Satz 2 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; zwei Bewegungen (Kopfhörer in die Jacke, Münzen auf die Theke) und die fallende Akte. Das erste Bild nach dem Intro zeigt ab 0,0 s den Markt (Regal, Kamera, Kasse, Titel, Prüfpfad); Rösch erscheint mit seinem Namen.
**Geräusche:** zwei Handlungsgeräusche, vorhandene Freesound-CC0-Dateien unter eigenem Namen kopiert (Freesound-API über den Proxy gesperrt), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Herr Rösch (24, nicht vorbestraft) öffnet am 2. März 2026 in einem Elektronikmarkt eine Packung Kopfhörer für 249 Euro, steckt die Kopfhörer ein und legt die leere Packung zurück. An der Kasse bezahlt er nur eine Cola. Ladendetektiv Brehm findet die Kopfhörer; ein Video zeigt den Ablauf. Als Beschuldigter vernommen, sagt Herr Rösch, er habe das Bezahlen vergessen.
>
> Am 5. März 2026 ruft er Herrn Brehm vor dem Markt „Du Idiot!“ zu. Herr Brehm schildert das am selben Tag der Polizei, stellt aber keinen Strafantrag.
>
> Im August 2026 liegt die Akte der Staatsanwältin vor. Herr Rösch hat keinen Verteidiger. Bearbeitervermerk: Gutachten und Abschlussverfügung entwerfen, keinen Strafbefehl.
>
> **Was verfügt die Staatsanwältin?**
