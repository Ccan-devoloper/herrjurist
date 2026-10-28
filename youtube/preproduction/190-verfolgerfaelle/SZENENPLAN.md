# Folge 190 · Kontrolleur stürzt bei Verfolgung: Die Verfolgerfälle (§ 823 I BGB) – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_190.py`](src/skript_190.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/Deliktsrecht, Klassiker-Fall. Hook nach Plan: „Ein Schwarzfahrer flüchtet, der Kontrolleur stürzt bei der Verfolgung die Treppe hinunter.“ Fiktiver Fall nach dem Vorbild des Verfolgerfalls (BGHZ 57, 25): Kontrolleur Wendelin trifft im U-Bahnhof den Fahrgast Anselm ohne gültigen Fahrschein und bittet um den Ausweis; Anselm läuft zur Treppe am Ausgang, Wendelin rennt hinterher (2 Stufen auf einmal) und stürzt; Arm gebrochen, 6 Wochen Armschlinge. Ablauf: Fall → Frage, Klassiker → Sachverhalt → Problem (psychisch vermittelte Kausalität) → § 823 Abs. 1 BGB (Wortlautkarte) → Äquivalenz und wertende Zurechnung → Herausforderungsformel → Im Fall → Verschulden → Gegenbeispiele → § 254 Abs. 1 BGB (Wortlautkarte) → Ergebnis → Ausblick (Retter, Strafrecht, § 265a StGB je ein Satz) → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 5:45,2.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Wendelin (WD, mit Armschlinge WS), um 55 | Fahrkartenkontrolleur, verlangt Ersatz | `standing/resting-1` (Oberteil Dunkelblau `#3B5B92` als Dienstkleidung ohne Logo, schwarze Hose, weiße Schuhe), Kopf `No Hair 1`, Brille `Glasses 4`, Haut `#E6B897`, kein Bart; ab dem Sturz mit **Armschlinge** (weißes Dreieckstuch unter dem angewinkelten Unterarm, Gurt zum Hals; Grundform mit Tuschekontur über der fertigen Figur, die Open-Peeps-Teile bleiben unverändert). Mimiken `Calm`, `Serious`, `Fear`, `Suspicious`, `Tired`, `Smile`, `Solemn`, `Concerned\|Serious`; redet mit `Serious` (vor dem Sturz) bzw. `Calm` (danach, ruhig) | `helmut` (Mann, älter) |
| Anselm (AS, beim Weglaufen AL), um 22 | Fahrgast ohne gültigen Fahrschein | `standing/resting-2` (schwarzes Oberteil, Hose Grün `#8FD694`, schwarze Schuhe), beim Weglaufen `standing/walking-2` (gleicher Farbaufbau der Reihe -2), Kopf `Short 4`, Haut `#F2C9A8`, keine Brille, kein Bart; freundlich, ohne Täterklischee. Mimiken `Calm`, `Serious`, `Suspicious`, `Concerned\|Serious` (redet), `Fear`, `Tired`, `Solemn`, `Smile` | `niklas` (Mann, jung) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Stimmen:** nur aus dem Pool; ela_froh (nicht für ernste Rollen) und julia (möglichst meiden) nicht gebraucht. helmut und niklas sprachen auch in Folge 187 (Pool erlaubt keine andere Männerbesetzung); Rollen, Namen und Figuren sind neu. Deshalb ist der Fahrgast ein junger Mann (Thumbnail-Plan „Schwarzfahrerin“ angepasst).
**Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und in keinem Skript, Szenenplan, Rechtsstand oder Abnahmebogen unter `youtube/preproduction/` (Volltextsuche 04.10.2026): Wendelin, Anselm – nie im Genitiv („der Arm von Wendelin“). Namensschilder Wendelin Blau, Anselm Grün.
**Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links, zur Tafel), `_r` nach rechts. A1: Wendelin blickt nach rechts zu Anselm, Anselm nach links zu Wendelin; bei der Flucht blicken beide nach rechts zur Treppe. A3: Wendelin (links) blickt nach rechts, Anselm nach links. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `WD_redet`, `WS_redet`, `AS_redet` (je links/rechts) und Lexi. Figuren-PNGs: `../peeps/op_190/` (72 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- Posen der letzten drei Folgen (187: `easing-1`, `pointing_finger-1`; 188: `pointing_finger-2`, `crossed_arms-1`; 189: `blazer-4`, `crossed_arms-2`) nicht verwendet; Prothesen-Posen (`shirt-1`, `shirt-2`, `blazer-1`, `blazer-2`) nicht verwendet; keine Polka Dots, keine Bärte, keine Karikatur.
- Schauplatz neu: **U-Bahnhof in Seitenansicht** (Bahnsteig mit gelber Sicherheitslinie und Fliesenfugen, Deckenkante mit Lampen, Zug als Tabler `train`, Treppe als Tabler `stairs-down` mit Pille „Ausgang“). 187 hatte eine Baustelle, 188 ein Bauamt. Kein Name, kein Logo, kein reales Verkehrsunternehmen.
- **Sturz nicht gezeigt:** eigene Folie nur mit großem Treppen-Icon und Pille „Wendelin stürzt auf den Stufen“; danach Wendelin ruhig mit Armschlinge. Kein Geräusch beim Sturz.
- Fahrgast neutral als „Fahrgast ohne gültigen Fahrschein“ (kein „Schwarzfahrer“ im Bild oder Ton).
- Cremegrund durchgehend, Tageslicht (U-Bahnhof hell beleuchtet, keine Nacht).

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Bahnsteig** `fall`–`verfolg` | Zug links, Treppe zum Ausgang rechts; Wendelin kontrolliert, Anselm ohne Fahrschein; Wendelin redet; Anselm läuft zur Treppe (Laufpose), Wendelin rennt hinterher | tabler:`train` (Blau), `stairs-down`, `arrow-down`, `ticket` (Gelb), `ticket-off` (Hellrot); Bahnsteig, Decke programmatisch | `Fall · Im U-Bahnhof` (ab 0,0 s) → `Fahrscheinkontrolle` → `Wendelin bittet um den Ausweis` → `Anselm läuft zur Treppe` → `Wendelin rennt hinterher` | Zug ab 0,0 s · Wendelin · Fahrschein · Anselm · kein Fahrschein · Blase · Flucht · Verfolgung | `szene_190zug_1` (Freesound CC0 661169) ab 0,0 s, `szene_190schritte_1` (Freesound CC0 682771) bei der Flucht |
| **A2 Treppe** `sturz`, `arm` | großes Treppen-Icon, Pille „stürzt“; dann Wendelin mit Armschlinge | tabler:`stairs-down` (Hellgrau), `bandage` | `Fall · Der Sturz` → `Fall · Arm gebrochen` | Treppe · stürzt · Wendelin mit Schlinge · Arm gebrochen · 6 Wochen | – |
| **A3 Danach** `w2`–`klass` | Bahnsteig, Treppe links; Wendelin (Schlinge) und Anselm einander zugewandt | tabler:`stairs-down` | `Fall · Wendelin verlangt Ersatz` → `Die Frage` → `Ein Klassiker` | Wendelin redet · Anselm redet · Frage · Klassiker mit Fundstelle | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **C Problem** `problem`–`psych` | Kreuz „weder gestoßen noch berührt“, eigener Entschluss, Block „psychisch vermittelte Kausalität“ | tabler:`hand-off`, `route`, `brain` | `Das Problem · …` (3 Stände) | Zeile für Zeile | – |
| **D § 823 Abs. 1 BGB** `norm`–`schema` | Wortlautkarte, Marker „Körper“ und „verletzt“ zum Wort, Haken Körper verletzt, Block Kausalität, Verweis | tabler:`book`, `bandage`, `link` | `Die Norm: § 823 Abs. 1 BGB › …` | Karte + 2 Marker + 3 Zeilen | – |
| **E Kausalität** `aequ`–`wert2` | Haken Äquivalenz, Kreuz „genügt allein nicht“, Block wertende Zurechnung | tabler:`link`, `route`, `scale` | `Haftungsbegründende Kausalität › …` | Zeile für Zeile | – |
| **F Herausforderungsformel** `formel`–`h5` | Formel mit drei Merkmalen, Fundstellen | tabler:`book`, `arrows-split`, `heart-handshake`, `scale`, `alert-triangle` | `Herausforderungsformel › …` (6 Stände) | Zeile für Zeile | – |
| **G Im Fall** `mot`–`zur` | drei Merkmale mit Haken, grüner Block | tabler:`id`, `scale`, `stairs-down`, `check` | `Im Fall › …` (6 Stände) | Zeile für Zeile | – |
| **H Verschulden** `versch`, `versch2` | zwei Haken, grüner Block | tabler:`zoom-question`, `alert-triangle` | `Verschulden · …` | 4 | – |
| **I Gegenbeispiele** `gegen`–`gg3` | Block, Kreuz Lebensrisiko, Beispiel Umknicken, Kreuz Sprung aus großer Höhe | tabler:`shoe`, `clock`, `road`, `arrow-big-down-lines` | `Gegenbeispiele › …` | Zeile für Zeile | – |
| **J § 254 Abs. 1 BGB** `mit`–`orig` | Wortlautkarte (vorgelesen), Marker zum Wort, 2 Stufen, abwägen, Originalfall 2/3 | tabler:`book`, `stairs-down`, `scale`, `chart-pie-2` | `Mitverschulden, § 254 Abs. 1 BGB › …` | Karte + 3 Marker + 4 Zeilen | – |
| **K Ergebnis** `erg` | grüner Block, Norm, Kürzung | tabler:`gavel` | `Ergebnis · Wendelin gegen Anselm` | 3 | – |
| **L Ausblick** `retter`–`fahrt` | Retter, Strafrecht, § 265a StGB je eine Zeile | tabler:`lifebuoy`, `gavel`, `ticket-off` | `Ausblick › …` | Zeile für Zeile | – |
| **M Klausurtipp** `tipp`–`tp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | Zeile für Zeile | – |
| **N Prüfschema** `sch`–`c4` | breite Karte, I.–III. mit Untermerkmalen | – | `Prüfschema › …` | 5 Aufbaustufen | – |
| **O Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Markern | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Sprechblasen Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („2 Stufen“, „6 Wochen“, „2/3“, „§ 823 Abs. 1 BGB“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; kein Zoom.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Bahnsteig, Deckenkante und Armschlinge aus Grundformen (`bahnsteig()`, `deckenband()` in `folien_190.py`, `schlinge()` in `figuren_190.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Kontrolleur Wendelin prüft in einem U-Bahnhof die Fahrscheine. Der Fahrgast Anselm hat keinen gültigen Fahrschein dabei. Wendelin bittet ihn um seinen Ausweis, um die Personalien festzustellen.
>
> Anselm läuft los, zur Treppe am Ausgang. Wendelin rennt hinterher, die steile Treppe hinunter, 2 Stufen auf einmal. Auf den Stufen stürzt er. Anselm hat ihn dabei weder gestoßen noch berührt. Der Arm von Wendelin ist gebrochen; 6 Wochen trägt er eine Armschlinge.
>
> Wendelin sagt zu Anselm: „Für meinen gebrochenen Arm müssen Sie aufkommen.“ Anselm antwortet: „Ich habe Sie doch gar nicht berührt. Sie sind selbst gestürzt!“
>
> **Kann Wendelin von Anselm Schadensersatz aus § 823 Abs. 1 BGB verlangen?**
