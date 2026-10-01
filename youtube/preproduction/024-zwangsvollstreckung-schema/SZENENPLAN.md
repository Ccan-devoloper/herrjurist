# Folge 024 · Zwangsvollstreckung Schema: Titel, Klausel, Zustellung – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_024.py`](src/skript_024.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · ZV, Themenplan-Format „Schema“. Ein frei erfundener Fall trägt das Schema: Malermeisterin Köhler hat gegen Herrn Vogel ein rechtskräftiges Urteil des Amtsgerichts über 4.800 € Werklohn; der Gerichtsvollzieher lehnt ab, weil die Vollstreckungsklausel fehlt. Prüfung: I. Antrag (§ 753 I, § 754a n. F.) → II. Vollstreckungsorgan (Gerichtsvollzieher, Vollstreckungsgericht, Grundbuchamt, Prozessgericht) → III. 1. Titel (Wortlautkarte § 704, §§ 708, 709, 794) → 2. Klausel (Wortlautkarte § 724 I, § 725, Urkundsbeamtin) mit Gegenfall Vollstreckungsbescheid (§ 796 I) → 3. Zustellung (Wortlautkarte § 750 I n. F., § 317) → IV. besondere Voraussetzungen (§§ 751, 756) → V. keine Hindernisse (§ 775) → Pfändung bei Vogel (§ 808) → Ausblick §§ 771, 767, 766 → Klausurtipp → Schema → Merksatz. Länge: Hauptfilm 6:54 (Begründung in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Köhler (KO), um 45 | Malermeisterin, Gläubigerin (Klägerin) | Pose `standing/crossed_arms-1` (verschränkte Arme, selbstbewusst), Kopf `Medium 3`; Oberteil Weiß (Malerhemd), Hose schwarz, Haut `#E8B98F`; Mimiken `Calm` (ruhig), `Driven` (redet), `Smile` (froh), `Contempt` (Ärger), `Serious` (denkt), `Concerned|Serious` (Sorge) | `laura_ruhig` (Frau, mittel) |
| Herr Vogel (VO), um 28 | Schuldner (Beklagter) | Pose `standing/walking-3` (schwarzes Shirt und Hose; Pose ohne einfärbbare Kleidung), Kopf `Short 2`, Haut `#C99470`; Mimiken `Calm`, `Suspicious` (redet), `Contempt` (trotzig), `Fear` (Schreck), `Tired` (müde) | `timo` (Mann, jung) |
| Gerichtsvollzieher (GV), um 50, ohne Namen | Vollstreckungsorgan | Pose `standing/blazer-4`, Kopf `No Hair 2`, Brille `Glasses 3`, kein Bart (Mund frei); Sakko `#3A3A48`, Hemd Weiß, Haut `#D9A07A`; Mimiken `Calm`, `Serious` (redet), `Suspicious` (denkt) | `marc` (Mann, mittel) |
| Urkundsbeamtin der Geschäftsstelle (UB), um 60, ohne Namen | erteilt die Vollstreckungsklausel | Pose `standing/polka_dots` (gepunktete Bluse), Kopf `Gray Medium` (Bibliothek: rotes Haar), Brille `Glasses 2`; Hose Lila `#B8A9F5`, Haut `#F0C8A8`; Mimiken `Calm`, `Smile` (redet) | `hilde` (Frau, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links zur Tafel, `_r` blickt nach rechts (Köhler in der Wohnung und im Büro zu Vogel bzw. zum Gerichtsvollzieher, Vogel bei der Pfändung zum Gerichtsvollzieher). Keine Prothesen-Posen, keine Bärte. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `KO_redet`, `VO_redet`, `GV_redet`, `UB_redet` (je links/rechts) und Lexi. Stimmen ausschließlich aus dem zugeteilten Pool (timo, hilde, marc, laura_ruhig). **Namen mit eindeutig deutscher Aussprache**, in früheren Folgen nicht vergeben: Köhler, Vogel; Gerichtsvollzieher und Urkundsbeamtin ohne Namen. Figuren-PNGs: `../peeps/op_024/` (64 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 023: Anfechtung (Posen `resting-2`, `robot_dance-2`, `walking-2`); 022: Tankstelle (`easing-1`, `pointing_finger-2`, `resting-1`); 012 (dieselbe Station „Zwangsvollstreckung“ im Überblick): Gerichtsvollzieher `walking-2` mit Schnurrbart, Klavier, Türklingel.
- 024: neue Schauplätze (frisch gestrichene Wohnung mit Wandfläche, Farbroller und Eimer; Büro des Gerichtsvollziehers mit Schreibtisch; Geschäftsstelle als Tafelszene mit Stempel; Vogels Wohnzimmer mit Sofa und Gemälde), neue Posen (`crossed_arms-1`, `walking-3`, `blazer-4`, `polka_dots`), anderer Gerichtsvollzieher (glatzköpfig, Brille, Sakko). Das Stimmenpool ist neu zugeteilt; laura_ruhig, marc, timo, hilde haben andere Rollen als in 010/017/019/022.
- Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Die Wohnung** `fall`→`urteil` | Bodenlinie, Wandfläche (Karte, Hellblau), Köhler links (blickt zu Vogel), Vogel rechts; Mitte: Pillen und Symbole | tabler:`paint` (Farbroller, Weiß, streicht nach oben), `bucket` (Blau), `currency-euro-off` (Rot), `building-bank` (Blau), `file-text` | `Fall · Die Wohnung von Herrn Vogel` (ab 0,0 s) → `Fall · Das Urteil` | Köhler + Wand · „Malermeisterin“ · Roller streicht · Vogel kommt · „4.800 €“ · „keine Zahlung“, Köhler Ärger, Vogel trotzig · „Klage“ · Köhler froh · Amtsgericht · Vogel müde, „Urteil: Vogel zahlt 4.800 €“ · „rechtskräftig“ | Farbroller an der Wand (`szene_024rolle_1`) |
| **B Beim Gerichtsvollzieher** `buero`→`frage` | Büro: Köhler links, Gerichtsvollzieher hinter dem Schreibtisch rechts | tabler:`file-text` (wandert auf den Tisch); Kreuz | `Fall · Beim Gerichtsvollzieher` → `Fall · Die Frage` | GV erscheint · Köhler redet, Blase, Urteil wandert · GV redet, Blase · Kreuz, „ohne Vollstreckungsklausel“ · Köhler redet, Blase · zwei Frage-Pillen, Köhler besorgt, GV denkt | – |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **D Überblick** `ueber` | Tafel links, Köhler und GV rechts | tabler:`list-numbers` | `Überblick · Prüfungsschema der Zwangsvollstreckung` | I. · II. · III. · Titel, Klausel, Zustellung · IV. · V. | – |
| **E I. Antrag** `antrag`→`versich` | Tafel | tabler:`file-text` („Auftrag“), `device-laptop` (Blau), `file-check` | `I. Antrag · Vollstreckungsauftrag, § 753 Abs. 1 ZPO` → `I. Antrag › elektronischer Auftrag, § 754a ZPO (seit 1.10.2026)` | Auftrag · § 753 · Block „Seit 1.10.2026: § 754a ZPO“ · elektronischer Auftrag · Titel und Klausel elektronisch · Versicherung, Köhler froh | – |
| **F II. Vollstreckungsorgan** `organ`→`hier` | Tafel; Symbol rechts wechselt mit der Vollstreckungsart | tabler:`sofa` (Lila), `wallet` (Gelb), `home` (Rot), `tools` | `II. Zuständiges Vollstreckungsorgan` → `II. Vollstreckungsorgan › hier: Gerichtsvollzieher, § 808 ZPO` | Einleitung · Sachen · Forderungen · Vollstreckungsgericht · Grundbuchamt · Prozessgericht · „Frau Köhler will Sachen pfänden lassen“ · Haken, Block „Zuständig: Gerichtsvollzieher“ | – |
| **G III. 1. Titel** `titel`→`titel_ok` | Tafel mit **Wortlautkarte § 704**; Köhler und Vogel | tabler:`file-text` („Urteil“ → „rechtskräftig“) | `III. Allgemeine Voraussetzungen › 1. Titel, § 704 ZPO` → `› 1. Titel › weitere Titel, § 794 ZPO` | Karte · Marker Endurteilen/rechtskräftig/vorläufig vollstreckbar · § 708 Nr. 11 · § 709 · § 794 · Prozessvergleich · notarielle Urkunde · Vollstreckungsbescheid · Haken, Köhler froh, Vogel müde | – |
| **H III. 2. Klausel** `klausel`→`p725` | Tafel mit **Wortlautkarte § 724 I**; Köhler und die Urkundsbeamtin | tabler:`file-text` („ohne Klausel“), `file-certificate` (Gelb), `rubber-stamp` (Rot, stempelt) | `III. … › 2. Klausel, § 724 ZPO` → `III. … › 2. Klausel › Wortlaut, § 725 ZPO` | „Daran ist Frau Köhler gescheitert“, „ohne Klausel“ · Karte · Marker · Erteilung · Urkundsbeamtin kommt · sie redet, Blase mit Klauselformel · Stempel auf die Ausfertigung, „vollstreckbare Ausfertigung“, Köhler froh | Stempel (`szene_024stempel_1`) |
| **I Gegenfall Vollstreckungsbescheid** `vb`→`p796` | hell-lila Tafel (Abzweig) | tabler:`file-certificate` (Lila) | `Gegenfall · Vollstreckungsbescheid, § 794 Abs. 1 Nr. 4 ZPO` → `… › Klausel? § 796 Abs. 1 ZPO` | Mahnverfahren · Titel Nr. 4 · § 796 Abs. 1 · andere Personen · im Bescheid genannt · Köhler froh | – |
| **J III. 3. Zustellung** `zust`→`zust_ok` | Tafel mit **Wortlautkarte § 750 I n. F.**; Köhler und Vogel; Brief vom Gericht zu Vogel | tabler:`building-bank`, `mail` (wandert) | `III. … › 3. Zustellung, § 750 Abs. 1 ZPO` | Pille „neu gefasst seit 1.10.2026“ · Karte · Marker namentlich bezeichnet · zugestellt · das Urteil · Brief wandert, Haken · „Auch das liegt vor“ | – |
| **K IV. besondere Voraussetzungen** `bes`→`bes_ok` | Tafel | tabler:`calendar-event`, `coins`, `arrows-exchange`, `file-check` | `IV. Besondere Vollstreckungsvoraussetzungen, §§ 751, 756 ZPO` | Kalendertag · Sicherheit · Zug um Zug · Block „nichts davon“ · rechtskräftig und unbedingt | – |
| **L V. Vollstreckungshindernisse** `hind`→`hind_ok` | Tafel; Vogel und GV | tabler:`hand-stop` (Rot), `receipt`, `receipt-off` | `V. Keine Vollstreckungshindernisse, § 775 ZPO` | § 775 · Nr. 1 · Nr. 4 · befriedigt · Haken „Herr Vogel kann nichts davon vorlegen“, Vogel müde | – |
| **M Pfändung bei Herrn Vogel** `auftrag`→`v1` | Vogels Wohnzimmer: Vogel links (blickt zum GV), Sofa, Gemälde an der Wand, GV rechts | tabler:`sofa` (Lila), `photo` (Gemälde, Gelb), `file-certificate`, `sticker` (Siegel, Rot) | `Fall · Der Auftrag` → `Fall · Pfändung bei Herrn Vogel, § 808 ZPO` | Auftrag, „vollstreckbare Ausfertigung“, „Auftrag von Frau Köhler“ · „Pfändung, § 808 ZPO“ · Vogel erschrickt, GV redet, Blase · Siegel · Vogel redet, Blase | – (Siegelgeräusch verworfen: kein passendes Klebegeräusch) |
| **N Ausblick Rechtsbehelfe** `rb`→`rb766` | Tafel; Vogel und GV | tabler:`photo` + Pille „Schwester“, `receipt`, `file-x` | `Ausblick · Rechtsbehelfe` → `Ausblick · Drittwiderspruchsklage, § 771 ZPO` → `… Vollstreckungsabwehrklage, § 767 ZPO` → `… Erinnerung, § 766 ZPO` | § 771 · hindert · § 767 · spätere Zahlung · § 766, Vogel trotzig | – |
| **O Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand), Haken/Kreuz | `Klausurtipp · Zustellung: Urteil, nicht die einfache Klausel` | Wortlaut · Haken Urteil · Kreuz einfache Klausel · Sonderfälle · Nr. 2 b | – |
| **P Klausurschema** `sch`→`s5` | breite Karte, Schema baut sich auf | – | `Klausurschema` | Titel · I. · II. · III. · 1. · 2. · 3. · IV. · V. | – |
| **Q Merksatz** `merke`→`m2` | Lexi erklärt (redet), Merksatz mit Marker | – | `Merksatz` | Satz 1 · Satz 2 · Marker · Satz 3 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; Bewegungen: Farbroller (A), Urteil auf den Schreibtisch (B), Stempel (H), Brief zu Vogel (J).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_024rolle_1`, `szene_024stempel_1`), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Malermeisterin Köhler streicht die Wohnung von Herrn Vogel für 4.800 Euro. Vogel zahlt nicht. Auf ihre Klage verurteilt ihn das Amtsgericht zur Zahlung von 4.800 Euro. Das Urteil wird beiden Parteien von Amts wegen zugestellt und ist inzwischen rechtskräftig.
>
> Frau Köhler legt dem Gerichtsvollzieher ihre Ausfertigung des Urteils vor, auf der keine Vollstreckungsklausel steht, und bittet ihn, bei Vogel zu pfänden. Der Gerichtsvollzieher lehnt ab.
>
> (Frei erfundener Übungsfall.)
>
> **Was muss vorliegen, damit der Gerichtsvollzieher vollstreckt?**
