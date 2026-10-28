# Folge 083 · Gutgläubiger Erwerb §§ 932 ff. BGB: Eigentum vom Nichteigentümer? – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_083.py`](src/skript_083.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Sachenrecht, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Dein Freund verkauft dein geliehenes Rad an jemanden, der fest glaubt, es gehöre ihm“): Erika leiht ihrem Freund Benno ihr Fahrrad für eine Woche. Benno ist knapp bei Kasse, gibt das Rad als seines aus und verkauft es für 200 € an Selma, die keinen Grund zu zweifeln hat. Am Sonntag sieht Erika ihr Rad bei Selma.

Ablauf: Fall (Leihe, Verkauf, Sonntag) → Frage → Sachverhalt → § 985 als Ausgangspunkt, Wortlautkarte § 932 Abs. 1 S. 1 → sechs Prüfungspunkte → I. Verkehrsgeschäft → II. Einigung und Übergabe (Verweis 080) → III. Nichtberechtigung → IV. Rechtsschein/Besitzverschaffungsmacht → V. guter Glaube (Wortlautkarte § 932 Abs. 2, grobe Fahrlässigkeit, keine Nachforschungspflicht, Zeitpunkt) → Beweislast („es sei denn“) → VI. kein Abhandenkommen (Wortlautkarte § 935 Abs. 1 S. 1, Leihe freiwillig) → Ergebnis → Abwandlung gestohlenes Rad, § 935 Abs. 2 → §§ 933, 934, 936 → § 816 Abs. 1 S. 1 (Verweis 073) → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:30,2 (5.473 Zeichen vertont); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Erika (EK), um 60 | Eigentümerin, verleiht ihr Rad | `standing/easing-1` (lila Hemdjacke und Oberteil `#B8A9F5`, schwarze Hose), Kopf `Gray Bun`, Haut `#F3D3B8`; Mimiken `Calm`, `Smile` (redet), `Serious` (empört, redet), `Smile Big|Smile`, `Suspicious`, `Concerned|Serious` | `hilde` (Frau, älter) |
| Benno (BE), um 40 | Freund und Entleiher, verkauft das Rad als seines | `standing/resting-1` (grüner Pullover `#8FD694`, schwarze Hose), Kopf `Short 4`, Haut `#EDC09A`; `Calm`, `Smile` (redet), `Smile Big|Smile`, `Suspicious`, `Concerned|Serious` | `christian` (Mann, mittel) |
| Selma (SE), um 25 | Käuferin | `standing/blazer-4` (roter Blazer `#F07A6A`, weißes Oberteil, schwarze Hose), Kopf `Long Curly`, Haut `#A8714A`; `Calm`, `Serious` (redet), `Smile Big|Smile`, `Suspicious`, `Concerned|Serious`; `sitting/bike` (gleiche Kleidung, Rahmen Blau) beim Heranfahren am Sonntag | `lucy` (Frau, jung) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge als Figur vergeben (geprüft per `grep -rlw` im ganzen `youtube/`-Ordner einschließlich der laufenden Folgen 081/082 und gegen die Koordinatorliste; „Greta“ und „Nora“ wegen früherer Nutzung verworfen): Erika, Benno, Selma. Kein Genitiv eines Namens im Sprechtext („aus der Garage von Erika“).
- **Stimmen nur aus dem Pool:** `hilde`, `christian`, `lucy`; `stephan` nicht eingesetzt (stephan und christian klingen ähnlich). Dialogpaare: Erika–Benno (hilde/christian), Benno–Selma (christian/lucy), Erika–Selma (hilde/lucy). Gegenüber 080 (lucy, stephan) nur `lucy` wiederholt (Pool aus vier Stimmen, drei Rollen).
- Präfix `EK_` statt `ER_`, weil `bausteine.peep_voll` Namen mit `ER_` in den Ordner `op_we` umleitet.
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. In den Fallszenen steht die linke Figur nach rechts blickend, die rechte nach links; in den Tafelszenen blicken beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `EK_redet`, `EK_empoert`, `BE_redet`, `SE_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur. Der Dieb der Abwandlung wird nicht gezeigt (nur Garage und Pille „gestohlen“), kein Mensch als Icon.
- Figuren-PNGs: `../peeps/op_083/` (66 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 080 (Hof am Abend, Nachtbühne, Morgen), 076 (Handy/Parkplatz/Notar), 027 (WG-Keller, Fahrradladen – ebenfalls ein geliehenes Fahrrad, dort Besitzschutz; hier Leihe vor einer **Garage**, Verkauf im **Park**, Begegnung am **Sonntag** auf der Straße). Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Leihe** `fall`–`be1` | vor der Garage von Erika: Erika, Rad, Benno ab 0,0 s; Kalender „für 1 Woche“; Blase Erika „Hier, bis Sonntag. Pass gut darauf auf!“, das Rad wandert zu Benno; Blase Benno „Danke! Am Sonntag hast du es zurück.“ | ph:`garage` (Gelb), ph:`bicycle` (Weiß), tabler:`calendar-event` | `Fall · Die Leihe` (ab 0,0 s) | – |
| **A2 Verkauf** `knapp`–`gibt` | Park: Benno mit Rad, Geldbörse „knapp bei Kasse“, Selma kommt; „als seines ausgegeben“; Blase Benno „Das ist mein Rad. Für 200 € gehört es dir.“; „kein Grund zu zweifeln“; Geldscheine wandern zu Benno, „200 € bezahlt“; Rad wandert zu Selma, „übergeben und einig“ | ph:`tree`, tabler:`trees` (Grün), ph:`wallet`, tabler:`cash-banknote` (Grün), ph:`bicycle` | `Fall · Der Verkauf` → `Fall · Zahlung und Übergabe` | `szene_083geld_1` bei der Zahlung |
| **A3 Sonntag** `sonntag`–`frage2` | Straße: Erika; Selma fährt auf dem Rad heran, steht dann neben dem Rad; Blasen Erika „Das ist mein Fahrrad! Gib es mir zurück.“ und Selma „Nein, ich habe es gekauft. Es gehört mir.“; Frage-Pillen, „Erika?“, „Selma?“, „Eigentum vom Nichteigentümer?“ | ph:`tree`, tabler:`sun` (Gelb), ph:`bicycle` | `Fall · Am Sonntag` → `Fall · Die Frage` | `szene_083klingel_1` beim Heranfahren |
| **B Sachverhalt** `sv` | Karte vollständig (38 px), ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C § 985 / § 932 I 1** `p985`–`w932` | Tafel § 985, ✗ „Benno durfte nicht übereignen“, Wortlautkarte § 932 Abs. 1 S. 1 (4 Marker) | ph:`bicycle`; tabler:`key-off`, `shield-check` | `Ausgangspunkt · § 985 BGB` → `Gutgläubiger Erwerb · § 932 Abs. 1 S. 1 BGB` | – |
| **D 6 Punkte** `sechs`–`v6` | I.–VI. zum Wort | tabler:`list-check` | `Gutgläubiger Erwerb › 6 Prüfungspunkte` | – |
| **E I. Verkehrsgeschäft** `rg`, `rg2` | Definition, BGH IV ZR 161/14 Rn. 12, ✓ Benno und Selma | ph:`handshake`; tabler:`arrows-exchange` | `› I. Verkehrsgeschäft` | – |
| **F II. Einigung und Übergabe** `eu`, `eu2` | § 929 S. 1, Verweis Folge 080, ✓ einig, ✓ Übergabe | ph:`handshake`, `bicycle` | `› II. Einigung und Übergabe` | – |
| **G III. Nichtberechtigung** `nb`, `luecke` | Benno nicht berechtigt, Eigentümerin Erika, keine Erlaubnis; Block „Guter Glaube schließt nur diese Lücke“ | tabler:`key-off`, `shield-check` | `› III. Nichtberechtigung` | – |
| **H IV. Rechtsschein** `rs`–`rs2` | Grundlage Besitz (vgl. V ZR 8/19 Rn. 9), Besitzverschaffungsmacht, ✓ Benno hatte das Rad | tabler:`hand-grab`; ph:`bicycle` | `› IV. Rechtsschein des Besitzes` | – |
| **I V. guter Glaube** `gg`–`zeit` | Wortlautkarte § 932 Abs. 2 (2 Marker), grobe Fahrlässigkeit (Rn. 28), ✗ keine allgemeine Nachforschungspflicht (Rn. 29), Zeitpunkt | tabler:`shield-check`, `alert-triangle`, `calendar-event`; ph:`eye` | `› V. guter Glaube` → `› grobe Fahrlässigkeit` → `› Zeitpunkt` | – |
| **J Beweislast** `bew`–`selma2` | „es sei denn“, ✗ Selma muss nicht beweisen, ✓ Erika muss beweisen, BGH V ZR 148/21 Rn. 14, Block „Selma ist in gutem Glauben“ | ph:`scales`; tabler:`shield-check` | `V. guter Glaube › Beweislast` | – |
| **K VI. kein Abhandenkommen** `ab`–`leihe` | Wortlautkarte § 935 Abs. 1 S. 1 (3 Marker), unfreiwilliger Besitzverlust (Rn. 9), ✓ freiwillig verliehen, ✓ freiwillig weggegeben, Block „Kein Abhandenkommen“ | tabler:`lock-open`; ph:`bicycle` | `› VI. kein Abhandenkommen` → `› Leihe` | – |
| **L Ergebnis** `erg`, `erg2` | Block „Selma ist Eigentümerin geworden“, §§ 929 S. 1, 932, ✗ kein Herausgabeanspruch gegen Selma | ph:`bicycle` | `Ergebnis · Selma ist Eigentümerin` | – |
| **M Abwandlung** `abw`–`p935b` | gestohlen aus der Garage, abhandengekommen, ✗ Selma nicht Eigentümerin; § 935 Abs. 2 (Geld, öffentliche Versteigerung) | ph:`garage`, `bicycle`; tabler:`cash-banknote`, `gavel` | `Abwandlung · gestohlenes Rad` → `› § 935 Abs. 2 BGB` | – |
| **N §§ 933, 934, 936** `p933`–`p936` | je eine Zeile bzw. ein Satz | ph:`handshake`; tabler:`file-certificate`, `link-off` | `Übergabeersatz · § 933 BGB` → `· § 934 BGB` → `Rechte Dritter · § 936 BGB` | – |
| **O § 816** `p816` | Herausgabe des Erlangten, ✓ Erlös 200 €, vgl. V ZR 108/12 Rn. 4, Verweis Folge 073 | ph:`scales`; tabler:`cash-banknote` | `Erika gegen Benno · § 816 Abs. 1 S. 1 BGB` | – |
| **P Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Abhandenkommen immer prüfen` | – |
| **Q Klausurschema** `sch`–`k6` | breite Karte, I.–VI. Zeile für Zeile | – | `Klausurschema` → `› III. …` → `› V. …` → `› VI. …` | – |
| **R Merksatz** `merke`, `m2` | Lexi erklärt, drei Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 20 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur, wo Rad und Geld die Hand wechseln und Selma heranfährt.
**Blasen:** Stil C (`bausteine.blase`), wortgleich mit dem Gesprochenen, Zahl als Ziffer („200 €“). Zahlen auf Tafeln, Pillen und Karte als Ziffern.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Erika leiht ihrem Freund Benno ihr Fahrrad für eine Woche, bis Sonntag. Benno ist knapp bei Kasse. Er bietet das Rad Selma für 200 Euro an und gibt es als sein eigenes aus.
>
> Selma hat keinen Grund zu zweifeln. Sie zahlt, Benno übergibt ihr das Rad, und beide sind sich einig, dass es Selma gehören soll. Erika hat den Verkauf nicht erlaubt.
>
> Am Sonntag sieht Erika ihr Rad bei Selma und verlangt es zurück.
>
> **Ist Selma Eigentümerin geworden?**
