# Folge 080 · § 929 S. 1 BGB: Einigung und Übergabe – Übereignung Schema – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_080.py`](src/skript_080.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Sachenrecht, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Du verkaufst dein Fahrrad, der Käufer holt es erst morgen ab – wem gehört es heute Nacht?“): Annika verkauft Herrn Brunner am Abend ihr Fahrrad für 300 €, er zahlt bar, holt es aber erst am nächsten Morgen ab.

Ablauf: Fall (Abend, Nacht) → Frage → Sachverhalt → Kaufvertrag und Übereignung (§ 433) → Wortlautkarte § 929 S. 1 mit vier Prüfungspunkten → I. Einigung (§§ 145 ff., Bestimmtheit, Abstraktion mit Verweis auf 005, „kann offenbleiben“) → II. Übergabe mit Wortlautkarte § 854 I (Besitzerwerb; h. M.: vollständiger Besitzverlust, Veranlassung; Geheißperson ein Satz) → Hof bei Nacht (Übergabe fehlt) → III. Einigsein (Widerruf als h. M.) → IV. Berechtigung (§ 185; gutgläubiger Erwerb nur Verweis auf 076) → Lösung heute Nacht (und Geld) → § 930 als Variante, § 446 ein Satz → der nächste Morgen (Übergabe) → Abwandlung § 449 → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 5:23,0 (4.570 Zeichen vertont), im Regelrahmen.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Annika (AN), um 25 | verkauft ihr Fahrrad | Reihe „-2“ (schwarzes Oberteil, Hose Blau `#8DB3F2`, Schuhe weiß): `standing/robot_dance-2` (offene Hand: ruhig, redet, froh), `crossed_arms-2` (denkt, Sorge); Kopf `Medium Straight`, Haut `#F0C8A8`; Mimiken `Calm`, `Smile` (redet), `Smile Big|Smile`, `Suspicious`, `Concerned|Serious` | `lucy` (Frau, jung) |
| Herr Brunner (BR), um 45 | kauft das Rad | `standing/shirt-4` (schwarzes Hemd, Hose Grau `#9C9CA6`), Kopf `Short 2`, `Glasses 2`, Haut `#B98055`; `Calm`, `Smile` (redet), `Smile Big|Smile`, `Suspicious`, `Serious`; `sitting/bike` (fährt am Morgen mit dem Rad davon; Jacke/Oberteil schwarz, Rahmen Rot) | `stephan` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in früheren Folgen nicht als Figur vergeben (geprüft per `grep -rlw` im ganzen `youtube/`-Ordner einschließlich der laufenden Folgen 078/079 und gegen die Koordinatorliste): Annika, Brunner („Annika“ steht nur als Name einer nicht eingesetzten ElevenLabs-Kandidatenstimme in `figurenstimmen-kandidaten.txt`). Kein Genitiv eines Namens im Sprechtext („im Hof von Annika“).
- **Stimmen nur aus dem Pool:** `lucy` (Annika) und `stephan` (Herr Brunner); `christian` und `hilde` nicht eingesetzt (nur zwei Fallfiguren; stephan und christian klingen ähnlich). Erzählerin/Lexi Carla ohne Rolle. Andere Stimmen als in 076 (julia, niklas, helmut, ela_froh).
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. In den Fallszenen steht Annika links und blickt nach rechts zu Herrn Brunner, er steht rechts und blickt nach links; in den Tafelszenen blicken beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `AN_redet`, `BR_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur.
- Figuren-PNGs: `../peeps/op_080/` (42 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 076 (Handy/Parkplatz/Notar), 027 (WG-Keller, Fahrradladen – ebenfalls ein Fahrrad, dort geliehen; hier ein Verkauf im **Hof** vor Annikas Haus, kein Keller, kein Laden), 005 (Bäckerei, Plattenspieler). Neu: Hof am Abend, **geteilte Nachtbühne** (Hof von Annika mit Rad links, Herr Brunner zu Hause rechts, Mond), Morgenszene mit Übergabe und Losfahren auf dem Rad. Die Nachtbühne kehrt in Szene G für die Subsumtion „Übergabe fehlt“ bewusst zurück. Cremegrund durchgehend (die Nacht wird durch Mond und Pille „heute Nacht“ gezeigt, kein Nachtverlauf).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Verkauf** `fall`–`an1` | Hof: Haus, Rad, Annika ab 0,0 s; Herr Brunner kommt, Blase „Ich nehme es. Hier sind 300 €.“, Geldscheine wandern zu Annika; Pillen „300 €, bar“, „zu Fuß gekommen“, „Abholung: morgen“; Blase Annika | tabler:`building-cottage` (Gelb), `fence`, `cash-banknote` (Grün), `calendar-event`; ph:`bicycle` (Weiß) | `Fall · Der Fahrradverkauf` (ab 0,0 s) → `Fall · Bar bezahlt` → `Fall · Abholung erst morgen` | `szene_080geld_1` beim Zahlen |
| **A2 Nacht** `nacht`–`frage2` | geteilte Bühne: Hof von Annika (Rad, Annika), Herr Brunner zu Hause; Mond; Frage-Pille, „Annika?“, „Herr Brunner?“ | tabler:`moon-stars` (Gelb), `home`; ph:`bicycle` | `Fall · Die Nacht` → `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig (38 px), ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Kaufvertrag** `kv`, `eigen` | Tafel § 433 I 1, ✗ „überträgt selbst kein Eigentum“, Block „eigene Übereignung“ | tabler:`receipt`; ph:`bicycle` | `Kaufvertrag · § 433 Abs. 1 S. 1 BGB` → `Kaufvertrag und Übereignung` | – |
| **D § 929 S. 1** `p929`–`v4` | Wortlautkarte (3 Marker), vier Prüfungspunkte I.–IV. zum Wort | ph:`bicycle`; tabler:`list-check` | `Übereignung · § 929 S. 1 BGB` → `§ 929 S. 1 BGB › vier Prüfungspunkte` | – |
| **E I. Einigung** `einig`–`offen` | dinglicher Vertrag, §§ 145 ff. (BGH V ZR 240/14 Rn. 9), Bestimmtheit (V ZR 174/21 Rn. 10), Abstraktion + Verweis, Block „kann offenbleiben“ | ph:`handshake`, `bicycle`; tabler:`link-off`, `question-mark` | `› I. Einigung` → `› bestimmte Sache` → `› Abstraktion` | – |
| **F II. Übergabe** `ueberg`–`geheiss` | 1. Besitzerwerb, Wortlautkarte § 854 I (2 Marker), V ZR 240/14 Rn. 21; „nach herrschender Meinung außerdem“: 2. Besitzverlust, 3. Veranlassung; Geheißperson | tabler:`arrows-exchange`, `hand-grab`, `hand-off`, `hand-finger`, `truck-delivery` | `› II. Übergabe` → `› Besitzerwerb, § 854 Abs. 1 BGB` → `› Besitzverlust und Veranlassung` → `› Geheißperson` | – |
| **G Hof bei Nacht** `hof`–`fehlt` | Nachtbühne wie A2; ✓ „tatsächliche Gewalt: Annika“, ✗ „Herr Brunner: kein Besitz“, „Die Übergabe fehlt“ | wie A2 | `II. Übergabe › heute Nacht?` → `› fehlt` | – |
| **H III. Einigsein** `einigsein`–`bindet` | „im Zeitpunkt der Übergabe noch einig“, „h. M.: … widerruflich“, Konjunktiv-Zeilen, ✗ kein Eigentumsübergang, Block § 433 | ph:`handshake`; tabler:`arrow-back-up`, `receipt` | `› III. Einigsein` → `› Widerruf bis zur Übergabe` | – |
| **I IV. Berechtigung** `berecht`–`gutgl` | Eigentümer, § 185 I, ✓ Annika, Verweis gutgläubiger Erwerb/076 | tabler:`key`, `shield-check`; ph:`bicycle` | `› IV. Berechtigung` → `› gutgläubiger Erwerb` | – |
| **J Lösung** `loes`–`geld` | ✗ Übergabe fehlt, Block „Annika bleibt Eigentümerin“, nur Anspruch § 433, ✓ Geld | ph:`bicycle`; tabler:`receipt`, `cash-banknote` | `Lösung · heute Nacht` → `Lösung › das Geld` | – |
| **K § 930, § 446** `p930`–`p446` | Variante Verwahrung/§ 930, Trennlinie, § 446 S. 1, Block „Kaufrecht, nicht Sachenrecht“ | ph:`handshake`; tabler:`lock`, `cloud-storm` | `Übergabeersatz · § 930 BGB` → `Gefahrübergang · § 446 S. 1 BGB` | – |
| **L Morgen** `morgen`–`faehrt` | Hof mit Sonne; Blasen Herr Brunner und Annika; Rad wechselt zu Herrn Brunner; „Einigung und Übergabe“; er sitzt auf dem Rad (`sitting/bike`), „Eigentümer: Herr Brunner“ | tabler:`sun`, `building-cottage`, `fence`; ph:`bicycle` | `Fall · Am nächsten Morgen` → `Fall · Die Übergabe` → `Ergebnis · Herr Brunner ist Eigentümer` | `szene_080klingel_1` beim Losfahren |
| **M Abwandlung** `abw`–`raten` | sofort mitgenommen, Raten, Vorbehalt, § 449 I, § 158 I, Block „Eigentum erst mit vollständiger Zahlung“ | ph:`bicycle`; tabler:`calendar-dollar`, `lock`, `cash-banknote` | `Abwandlung · Eigentumsvorbehalt` → `› § 449 Abs. 1 BGB` | – |
| **N Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Einigung und Übergabe getrennt` | – |
| **O Klausurschema** `sch`–`k4b` | breite Karte, I.–IV. mit Untermerkmalen, Zeile für Zeile | – | `Klausurschema` → `› II. Übergabe` → `› III. Einigsein` → `› IV. Berechtigung` | – |
| **P Merksatz** `merke`, `m2` | Lexi erklärt, drei Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur, wo Geld und Rad die Hand wechseln.
**Blasen:** Stil C (`bausteine.blase`), wortgleich mit dem Gesprochenen, Zahl als Ziffer („300 €“). Zahlen auf Tafeln, Pillen und Karte als Ziffern.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Annika verkauft ihr Fahrrad. Am Abend sieht sich Herr Brunner das Rad in ihrem Hof an und kauft es für 300 Euro. Er zahlt sofort bar.
>
> Weil er zu Fuß gekommen ist, will er das Rad erst am nächsten Morgen abholen. Annika ist einverstanden. Das Rad bleibt über Nacht in ihrem Hof. Weitere Vereinbarungen treffen die beiden nicht.
>
> **Wem gehört das Fahrrad in der Nacht?**
