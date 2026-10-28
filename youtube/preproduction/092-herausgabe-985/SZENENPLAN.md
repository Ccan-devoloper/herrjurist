# Folge 092 · § 985 BGB: Der Herausgabeanspruch – Prüfungsschema Vindikation – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_092.py`](src/skript_092.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Sachenrecht, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Dein Ex hat nach der Trennung deinen Plattenspieler behalten“): Theresa kauft sich lange vor dem Zusammenziehen einen Plattenspieler. In der gemeinsamen Wohnung erlaubt sie Clemens, ihn mitzubenutzen. Nach der Trennung zieht sie aus, der Plattenspieler bleibt bei Clemens. Sie fordert ihn zurück, er möchte ihn behalten. Respektvoll, ohne Streit und ohne Beziehungsdrama.

Ablauf: Fall (Kauf, gemeinsame Wohnung, Trennung) → Frage → Sachverhalt → Wortlautkarte § 985 mit drei Prüfungspunkten → I. Eigentum historisch (Erwerb vom Händler, kein Verlust durch Zusammenziehen, kein Erwerb Dritter, Verweis 080/083) → § 1006 (ein Satz) → II. Besitz (§ 854, § 868 je ein Satz) → III. Wortlautkarte § 986 Abs. 1 S. 1 → eigenes Besitzrecht (Leihe, Ende mit Rückforderung), abgeleitetes Besitzrecht (ein Satz) → Einwendung und Beweislast → Ergebnis und Rechtsfolge (Abholung, Holschuld) → § 604 (Konkurrenz) und Ausblick §§ 987 ff. → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 4:51,4 (4.148 Zeichen vertont), im Regelrahmen.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Theresa (TH), um 30 | Eigentümerin des Plattenspielers | `standing/resting-2` (schwarzes Oberteil, rote Hose `#F07A6A`, schwarze Schuhe), Kopf `Bun 2`, Haut `#F2CDB0`; Mimiken `Calm`, `Smile` (redet), `Serious` (bittet, redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious` | `lucy` (Frau, jung) |
| Clemens (CL), um 30 | Ex-Partner, Besitzer | `standing/resting-1` (lila Pullover `#B8A9F5`, schwarze Hose), `standing/crossed_arms-1` (denkt, gleiche Kleidung), Kopf `Short 5`, Haut `#C68E68`; `Calm` (ruhig; „meint“, redet), `Smile` (redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious` | `christian` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge als Figur vergeben (geprüft per `grep -rlw` im ganzen `youtube/`-Ordner einschließlich der laufenden Folgen 090/091 und gegen die Koordinatorliste): Theresa, Clemens. Kein Genitiv eines Namens im Sprechtext („in der Wohnung bei Clemens“).
- **Stimmen nur aus dem Pool:** `lucy` und `christian`; `stephan` nicht eingesetzt (klingt wie `christian`), `hilde` (älter) passt zu keiner Rolle. Erzählerin/Lexi Carla ohne Rolle. Die Vorfolgen 089–091 nutzten keine dieser Stimmen.
- **Abwechslung:** Posen, Kleidung und Muster nicht aus 089–091 (dort shirt-3, easing-2, walking-2, easing-1, crossed_arms-2, blazer-4, robot_dance-3, shirt-4, walking-1); keine Polka Dots. Präfixe `TH_`/`CL_` (nie `ER_`).
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. In den Fallszenen steht Theresa links und blickt nach rechts, Clemens rechts und blickt nach links; in den Tafelszenen blicken beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `TH_redet`, `TH_bittet`, `CL_redet`, `CL_meint` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur. Der Händler wird nicht gezeigt (nur der Laden), kein Mensch als Icon.
- Figuren-PNGs: `../peeps/op_092/` (56 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 083 (Garage, Park, Straße mit Fahrrad), 080 (Hof, Nachtbühne), 005 (Bäckerei mit Plattenspieler-Kauf unter Minderjährigen – dort Abstraktionsprinzip; hier ein neuer Fall: Laden, gemeinsames Wohnzimmer mit Sofa, Auszug mit Umzugskarton, Abholung an der Wohnungstür). Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Kauf** `fall`–`th1` | Laden; Theresa ab 0,0 s; der Plattenspieler wandert vom Laden zu ihr, Quittung „gekauft“, Kalender „lange vor dem Zusammenziehen“; Blase „Endlich mein eigener Plattenspieler!“ | tabler:`building-store` (Gelb), `vinyl` (Blau), `calendar-event`; ph:`receipt` | `Fall · Der Kauf` (ab 0,0 s) | – |
| **A2 Wohnung** `zusammen`–`th2` | Wohnzimmer mit Sofa; Clemens kommt dazu; Blasen Clemens „Darf ich auch mal Platten auflegen?“, Theresa „Klar, nutz ihn ruhig mit.“; Musiknoten | ph:`couch` (Grün), `music-notes`; tabler:`vinyl` | `Fall · Die gemeinsame Wohnung` | – |
| **A3 Trennung** `trennung`–`frage2` | Tür, Umzugskarton bei Theresa „Theresa zieht aus“; Plattenspieler „bleibt bei Clemens“, Haus rechts; Blasen Theresa „Clemens, ich möchte meinen Plattenspieler zurück.“ und Clemens „Wir haben ihn doch zusammen genutzt. Er kann hierbleiben.“; Frage-Pillen | tabler:`door` (Gelb), `package` (Gelb), `vinyl`; ph:`house` | `Fall · Nach der Trennung` → `Fall · Die Frage` | `szene_092karton_1` beim Auszug |
| **B Sachverhalt** `sv` | Karte vollständig (38 px), ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C § 985** `p985`–`v3` | Wortlautkarte § 985 (3 Marker), drei Prüfungspunkte zum Wort | tabler:`vinyl`, `list-check` | `Anspruchsgrundlage · § 985 BGB` → `§ 985 BGB › 3 Prüfungspunkte` | – |
| **D1 I. Eigentum** `eig`–`dritte` | 1. Kauf (✓ Händler übereignet, § 929 S. 1), 2. später verloren? (✗ Zusammenziehen, Einigung fehlt; ✗ kein Dritter, auch nicht gutgläubig), Verweis auf die Videos 080/083 | tabler:`list-numbers`; ph:`receipt`, `couch`, `handshake` | `I. Eigentum › historisch prüfen` → `› später verloren?` | – |
| **D2 § 1006** `p1006`, `eig2` | Vermutung für den Besitzer, ✗ hilft Clemens nicht, BGH V ZR 268/15 Rn. 18, 27; Block „Theresa ist Eigentümerin geblieben“ | ph:`scales`; tabler:`vinyl` | `I. Eigentum › Vermutung, § 1006 BGB` → `› Theresa ist Eigentümerin` | – |
| **E II. Besitz** `bes`–`mittel` | tatsächliche Gewalt, § 854 Abs. 1, ✓ unmittelbarer Besitzer, mittelbarer Besitzer § 868 | tabler:`hand-grab`; ph:`house`, `handshake` | `II. Besitz › § 854 Abs. 1 BGB` → `› mittelbarer Besitz, § 868 BGB` | – |
| **F III. § 986** `rzb`, `w986` | Wortlautkarte § 986 Abs. 1 S. 1 (4 Marker) | tabler:`vinyl`, `shield-check` | `III. kein Recht zum Besitz › § 986 Abs. 1 S. 1 BGB` | – |
| **G Besitzrecht** `eigen`–`abgel` | 1. eigenes Besitzrecht: Leihe (§ 598, XII ZB 243/20 Rn. 41), keine feste Zeit, ✗ endet mit Rückforderung (§ 604 Abs. 3); 2. abgeleitetes Besitzrecht (§ 986 Abs. 1 S. 1 Alt. 2) | tabler:`file-certificate`, `calendar-event`, `arrow-back-up`, `vinyl`; ph:`handshake` | `III. › eigenes Besitzrecht: Leihe` → `› Ende des Besitzrechts` → `› abgeleitetes Besitzrecht` | – |
| **H Einwendung** `einw`–`kein` | von Amts wegen (ohne Az.), Beweislast Clemens (XII ZB 243/20 Rn. 42), Block „Hier: kein Recht zum Besitz mehr“ | tabler:`gavel`, `shield-x`; ph:`scales` | `III. › Einwendung, keine Einrede` → `› Beweislast` | – |
| **I Ergebnis** `erg`, `ort` | Fallbühne: Theresa an der Wohnungstür, Plattenspieler wandert zu ihr; Pillen „Herausgabe nach § 985 BGB“, „dort, wo er steht: in seiner Wohnung“, „Theresa holt ihn ab: Holschuld“ | tabler:`door`, `vinyl`; ph:`house` | `Ergebnis · § 985 BGB` → `Rechtsfolge › Herausgabe am Ort der Sache` | `szene_092klopfen_1` an der Tür |
| **J Daneben** `p604`, `ebv` | § 604 Rückgabeanspruch aus der Leihe, ✓ nebeneinander; Ausblick §§ 987 ff. | ph:`handshake`, `scales`; tabler:`arrows-exchange` | `Daneben · § 604 BGB` → `Ausblick · §§ 987 ff. BGB` | – |
| **K Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Eigentum historisch prüfen` | – |
| **L Klausurschema** `sch`–`k4` | breite Karte, I.–IV. mit Untermerkmalen, Zeile für Zeile | – | `Klausurschema` → `› II. Besitz` → `› III. kein Recht zum Besitz` → `› IV. Rechtsfolge` | – |
| **M Merksatz** `merke`, `m2` | Lexi erklärt, zwei Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur, wo der Plattenspieler den Besitzer wechselt (Kauf, Abholung).
**Blasen:** Stil C (`bausteine.blase`), wortgleich mit dem Gesprochenen. Zahlen auf Tafeln, Pillen und Karte als Ziffern.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Theresa kauft sich einen Plattenspieler, lange bevor sie mit Clemens zusammenzieht. Der Händler übereignet ihn ihr.
>
> In der gemeinsamen Wohnung stellt sie ihn ins Wohnzimmer und erlaubt Clemens, ihn mitzubenutzen. Für wie lange, vereinbaren die beiden nicht.
>
> Nach der Trennung zieht Theresa aus. Der Plattenspieler bleibt in der Wohnung von Clemens. Theresa fordert ihn zurück; Clemens möchte ihn behalten, weil beide ihn zusammen genutzt haben.
>
> **Kann Theresa den Plattenspieler herausverlangen?**
