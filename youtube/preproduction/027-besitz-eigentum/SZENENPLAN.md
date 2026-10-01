# Folge 027 · Besitz und Eigentum: Der Unterschied einfach erklärt (§§ 854 ff. BGB) – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_027.py`](src/skript_027.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Zivilrecht/Sachenrecht, Themenplan-Format „Abgrenzung“. Frei erfundener Fall nach dem Plan-Hook („Dein Mitbewohner hat dein Fahrrad im Keller – er besitzt es, aber es gehört dir“): Anke leiht ihrem Mitbewohner Jürgen ihr Rad bis Ende September; er schließt es in sein Kellerabteil. Jürgen jobbt im Fahrradladen von Frau Kunze (Besitzdiener). Ein Unbekannter schiebt das Rad aus dem Keller davon, Jürgen verfolgt ihn und nimmt es ihm wieder ab. Ablauf: Fall → Frage → Sachverhalt → Eigentum (§ 903) → Besitz (§ 854 I) → mittelbarer Besitz (§ 868) → Eigen-/Fremdbesitz (§ 872) → Besitzdiener (§ 855), Erbenbesitz (§ 857) → verbotene Eigenmacht (§ 858) → Selbsthilfe (§ 859 II), Ergebnis → Gegenfall: Anke nimmt ihr Rad eigenmächtig zurück (§§ 858, 861, 863; Gegenprobe §§ 985, 986) → Ausblick §§ 929 S. 1, 930, 931 → Klausurtipp → Schema § 861 → Merksatz.
**Länge:** Hauptfilm 6:43,7 (5.695 Zeichen, Grenze 6.200). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Anke (AN), um 28 | Eigentümerin des Rades, Verleiherin; im Gegenfall Täterin der verbotenen Eigenmacht | Reihe „-1“ (Oberteil Grün `#8FD694`, schwarze Hose): `standing/resting-1` (ruhig, redet, froh), `crossed_arms-1` (trotzig, Ärger, denkt, zufrieden), `walking-1` (geht, nimmt das Rad); Kopf `Medium Straight`, Haar `#7A4B2E`, Haut `#E8B98F` | `laura_klar` (Frau, mittel) |
| Jürgen (JU), um 25 | Mitbewohner, Entleiher und unmittelbarer Besitzer; Aushilfe im Fahrradladen (Besitzdiener) | `standing/robot_dance-3` (offene Hand), Kopf `Short 4`, Oberteil Blau `#8DB3F2`, Hose Gelb `#F9D56E`, Haut `#C99470`; Mimiken `Calm`, `Smile` (redet), `Serious` (ruft, ernst), `Smile Big|Smile` (froh), `Fear` (Schreck), `Suspicious`, `Contempt` | `marc` (Mann, mittel) |
| Frau Kunze (KU), um 60 | Inhaberin des Fahrradladens, Besitzherrin | `standing/blazer-3` (Blazer Orange `#F9A66C`, Hose Blau), Kopf `Gray Short`, Brille `Glasses 2`, Haut `#F0C8A8`; `Calm`, `Smile` (redet/froh) | `lisa` (Frau, älter) |
| Ein Unbekannter (DI) | Dieb, ohne Text | `standing/walking-2` (schwarzes Oberteil, Hose Grau `#9C9CA6`), Kopf `hat-beanie`, Haut `#D9A07A`; `Suspicious` (geht), `Fear` (ertappt) | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel bzw. zum Gegenüber), `_r` blickt nach rechts (Anke zu Jürgen in Szene A, Jürgen zu Frau Kunze, Jürgen zum Dieb, Jürgen zu Anke im Gegenfall).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `AN_redet`, `AN_trotzig`, `JU_redet`, `JU_ruft`, `KU_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (`blazer-1/-2`, `shirt-1/-2` nicht gewählt).
- **Stimmen nur aus dem Pool** lisa, marc, laura_klar (otto, Status „unsicher“, nicht benötigt); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache:** Anke, Jürgen (Umlaut), Kunze; in früheren Folgen nicht vergeben (geprüft gegen alle `skript_*.py`; „Kessler“ aus 010 vermieden). Genitivformen im Sprechtext vermieden („das Eigentum von Anke“).
- **Namensschild** jeder Figur ab ihrem ersten Auftritt und durchgehend, auch allein neben der Tafel und bei Lexi; bei Bewegung wandert das Schild mit.
- Figuren-PNGs: `../peeps/op_027/` (80 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 026 (Kausalität, Strafrecht), 025 (Auschwitzlüge), 023 (Buchladen/Großhändler), 021 (Handyladen), 005 (Bäckerei/Haustür). Hier neu: WG mit Lattenverschlag-Kellerabteil, Fahrradladen mit Schaufenster, Straßenecke am Abend, Haus und Garage der Eltern. Erstes Thema mit fünf Wortlautkarten (§§ 903, 854 I, 868, 872, 855).

## Szenen

Alle Szenen auf Cremegrund (Tageslicht; Szene C „Am Abend“ nur mit Mond-Requisit, kein Nachtverlauf).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Das geliehene Rad** `fall`–`j1` | WG: Anke, Jürgen, Rad; rechts das Kellerabteil (Lattenverschlag aus `karte`/`linienzug`) | tabler:`bike` (Rosa, Ankes Rad), `calendar`, `lock` (Gelb) | `Fall · Das geliehene Rad` (ab 0,0 s) | Grundbild · Juni · „geliehen bis Ende September“ · Anke redet · Jürgen redet · Rad wandert ins Abteil · Schloss | – |
| **B Im Fahrradladen** `laden`–`ku1` | Laden, Schaufenster, zwei Laderäder, Frau Kunze weist an, Jürgen stellt die Räder ins Fenster | tabler:`building-store` (Gelb), `bike` (Blau, Rot) | `Fall · Im Fahrradladen` | Laden · Jürgen kommt · Kunze redet · Räder wandern ins Fenster, „Schaufenster“ | – |
| **C Der Dieb** `dieb`–`frage` | Kellerabteil am Abend; Unbekannter bricht auf, schiebt das Rad davon; Jürgen rennt hinterher, ruft, nimmt es ihm ab | tabler:`moon`, `lock`/`lock-open` (Rot), `bike` | `Fall · Der Dieb` → `Fall · Die Frage` | Abteil · Unbekannter · Schloss offen · wegschieben · Jürgen kommt · Jürgen ruft · „an der nächsten Ecke“ · Rad zurück, Dieb ertappt · Frage-Pillen | Schloss bricht auf (`szene_027schloss_1`), Freilauf (`szene_027freilauf_1`) |
| **D Sachverhalt** `sv` | Karte vollständig, ≈ 10 s, ohne Fiktiv-Hinweis (Vorgabe 01.10.2026) | – | `Sachverhalt` | 1 | – |
| **E Eigentum** `eig`–`anke` | Tafel, Wortlautkarte § 903 S. 1, Anke | tabler:`certificate` | `Eigentum, § 903 BGB` | Titel · Definition · Karte · Marker (3) · Block „Eigentümerin: Anke“ | – |
| **F Besitz** `besitz`–`jb` | Tafel, Wortlautkarte § 854 I (vorgelesen), Jürgen mit Rad und Schloss | tabler:`bike`, `lock` | `Besitz, § 854 I BGB` → `Besitz › Jürgen: unmittelbarer Besitz` | Definition · Karte · Marker · Besitzwille · Verkehrsanschauung + V ZR 70/16 · ✓ Kellerabteil · Block | – |
| **G Mittelbarer Besitz** `mittel`–`mb` | Wortlautkarte § 868, Anke und Jürgen | tabler:`bike` | `Mittelbarer Besitz, § 868 BGB` → `… › Leihe als Besitzmittlungsverhältnis` | Karte · Marker (5) · Leihe · Rückgabe · V ZR 92/25 · Block | – |
| **H Eigen-/Fremdbesitz** `p872`–`fremd` | Wortlautkarte § 872 | tabler:`bike` | `Eigen- und Fremdbesitz, § 872 BGB` | Karte · Marker · ✓ Anke · ✓ Jürgen · fremde Sache | – |
| **I Besitzdiener** `diener`–`p857` | Wortlautkarte § 855, Frau Kunze und Jürgen; Laderäder → Ankes Rad | tabler:`bike` | `Besitzdiener, § 855 BGB` → `Sonderfall · Erbenbesitz, § 857 BGB` | Karte · Marker (5) · ✓ Besitzdiener · Besitzerin · V ZR 63/13 · ✗ kein Weisungsverhältnis · Block § 857 | – |
| **J Verbotene Eigenmacht** `eigenm`–`fehler` | Tafel, Unbekannter und Jürgen | tabler:`bike` | `Verbotene Eigenmacht, § 858 BGB` → `… › fehlerhafter Besitz, § 858 II BGB` | § 858 I · ✓ verbotene Eigenmacht · unmittelbarer Besitzer · V ZR 70/16 Rn. 9 · fehlerhaft · ✗ kein Eigentum | – |
| **K Selbsthilfe** `p859`–`erg` | Tafel | tabler:`bike` | `Selbsthilfe, § 859 II BGB` → `Ergebnis` | § 859 II (2 Zeilen) · ✓ frische Tat · Ergebnisblock | – |
| **L Gegenfall** `gegen`–`a2` | Haus, Jürgen stellt Rad ab; Anke nimmt es, bringt es zur Garage der Eltern; Streit | ph:`house`, ph:`garage`, tabler:`bike` | `Gegenfall · Anke holt ihr Rad` | Im Juli · Anke kommt · „ohne zu fragen“ · Rad wandert · Garage · Jürgen redet · Anke redet | – |
| **M § 861/§ 863** `p861`–`posses` | Tafel, Anke und Jürgen | – | `Gegenfall › verbotene Eigenmacht, § 858 I BGB` → `› § 861 I BGB` → `› Einwendungen, § 863 BGB` | ✓ Eigenmacht · ohne Willen · kein Gesetz · § 861 · ✗ Eigentum · § 863 (2 Zeilen) · possessorisch | – |
| **N Gegenprobe** `p985`–`p986` | Tafel | tabler:`certificate`, `bike` | `Gegenprobe · § 985 BGB?` → `› Recht zum Besitz, § 986 BGB` | § 985? · ✗ Nein · petitorisch · Recht zum Besitz · § 986 | – |
| **O Ausblick** `ausblick`–`p931` | Tafel | tabler:`arrows-exchange`, `home`, `writing-sign` | `Ausblick · Übereignung` → `› Übergabe, § 929 S. 1` → `› Besitzkonstitut, § 930` → `› Abtretung, § 931` | Satz · § 929 · § 930 (2) · § 931 (2) | – |
| **P Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Besitz je Person` → `Klausurtipp · § 861 ohne Eigentum` | 4 Zeilen · § 861-Satz · ✗ Zitat | – |
| **Q Klausurschema** `sch`–`k6` | breite Karte, Aufbau Punkt für Punkt | – | `Klausurschema` | Titel · I.–III. (+) · IV. (2) · V. · Ergebnis | – |
| **R Merksatz** `merke`–`m2` | Lexi erklärt, Merksatz mit Markern | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur, wo das Rad den Ort wechselt (Keller, Schaufenster, Wegschieben, Zurücknehmen, Garage) und beim Hinterherrennen.
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0, Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** wortgleich mit dem Gesprochenen.

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Anke leiht ihrem Mitbewohner Jürgen im Juni ihr Fahrrad, bis Ende September. Jürgen schließt es in sein Kellerabteil. Tagsüber jobbt er im Fahrradladen von Frau Kunze und stellt dort auf ihre Anweisung die neuen Räder des Ladens ins Schaufenster.
>
> An einem Abend bricht ein Unbekannter das Kellerabteil auf und schiebt das Rad davon. Jürgen sieht ihn, rennt sofort hinterher und nimmt dem Mann das Rad an der nächsten Ecke wieder ab.
>
> **Wem gehört das Rad, wer besitzt es – und durfte Jürgen es sich zurückholen?**
