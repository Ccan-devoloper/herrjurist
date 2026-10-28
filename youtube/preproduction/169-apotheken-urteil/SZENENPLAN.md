# Folge 169 · Drei-Stufen-Theorie: Das Apotheken-Urteil zur Berufsfreiheit – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_169.py`](src/skript_169.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Klassiker-Fall · Grundrechte. Ablauf: fiktiver Einstieg (Grete, Apothekerin; „In Ihrem Stadtteil gibt es schon genug Apotheken“) → Frage → der echte Fall sachlich (Traunreut 1956, Wortlautkarte Art. 3 Abs. 1 ApothekenG, Ablehnung, Verfassungsbeschwerde) → Sachverhalt → Art. 12 Abs. 1 GG (Wortlautkarte; Berufsbegriff; Schritt in die Selbständigkeit; Wahl/Ausübung nicht trennbar, einheitliches Grundrecht, Regelungsvorbehalt für beide, je näher an der Wahl desto enger) → die drei Stufen (je eigene Farbe, gleiche Tafel: Kopf – Beispiel – Rechtfertigung; Grundsatz niedrigste Stufe; Lehre: konkretisierte Verhältnismäßigkeit) → Anwendung (Bedarf und Tragfähigkeit = objektive Voraussetzung; Volksgesundheit wichtig, aber keine Gefahr; mildere Stufen) → Ergebnis (Tenor, Leitsatz 8) → zurück zu Grete (Wortlautkarte § 2 Abs. 1 ApoG) → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 6:22,4 (5.534 vertonte Zeichen).

**Neutralität:** Der reale Beschwerdeführer wird weder benannt noch gezeigt; im echten Fall (B1, B2) keine Figuren, nur Tafel und neutrale Icons. Apotheken nur mit Tabler-Icons (`pill`, `pills`, `first-aid-kit`) und einer Ladenfassade aus Grundformen mit dem Wort „Apotheke“ – kein Apotheken-A, keine Kette, kein Logo. Herr Dannemann ist sachlich (keine bösen Mimiken).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Grete (GR), um 30 | fiktive Apothekerin, will im Stadtteil eine eigene Apotheke eröffnen | `standing/doctor-nurse-02` (weißer Kittel, Oberteil Hellblau `#9FD8E5`, Hose Blau `#8FA7DF` – Originalfarben, die drei Flächen heißen in Figma gleich „Clothes“), Kopf `Medium Bangs 2` (Haar `#8A5A33`), Haut `#F1C9A5`, ohne Brille. Mimiken `Calm`, `Serious` (redet), `Suspicious` (denkt), `Smile` (froh), `Concerned\|Serious` (Sorge) | `ela_froh` (Frau, jung) |
| Herr Dannemann (DA), um 60 | fiktiver Sachbearbeiter der Erlaubnisbehörde | `standing/shirt-4` (schwarzes Hemd der Pose, Hose Grau `#6B6B78`), Kopf `Gray Short`, Brille `Glasses 4`, Haut `#E0AC88`, ohne Bart. Mimiken `Calm`, `Serious` (redet), `Suspicious` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. A1/G1: Grete blickt zuerst nach links zum leeren Laden, ab der Rede von Herrn Dannemann nach rechts zu ihm (`_r`); Herr Dannemann rechts blickt nach links zu ihr. Tafelszenen: alle nach links zur Tafel. Kontaktbild `out/besetzung_169.png`.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `GR_redet`, `DA_redet` (je links/rechts) und Lexi.
- **Stimmen** nur aus dem Pool (niklas, helmut, ela_froh, julia). Grete `ela_froh`: heitere, junge Frauenstimme, passt zur hoffnungsvollen Gründerin; ihre Sätze sind keine ernste Rolle (Frage, Einwand) – neue Hauptstimme gegenüber 164/165 (dort niklas und helmut). Herr Dannemann `helmut` (älterer Mann; im Pool die einzige ältere Stimme, sachliche Nebenrolle mit einem Satz). julia nicht verwendet.
- **Namen:** Grete (gesprochen), Dannemann (nur Namensschild) – eindeutig deutsch, nicht in der Liste vergebener Namen und in keinem Szenenplan/Skript/Abnahmebogen unter `youtube/preproduction` (Volltextsuche 04.10.2026; „Merle“, „Henrike“, „Greta“ verworfen, weil schon verwendet).
- Figuren-PNGs: `../peeps/op_169/` (36 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 164 (`shirt-3`, `blazer-4`), 165 (`walking-1`, `crossed_arms-2`), 166 (`resting-2`, `pointing_finger-2`, `blazer-3`, `walking-1`), 167 (`resting-1`, `blazer-1`) – hier `doctor-nurse-02` und `shirt-4`; keine Polka Dots, keine Prothesen-Posen, keine Bärte. Schauplatz **Straße im Stadtteil mit zwei Ladenfassaden** (bestehende Apotheke, leerer Laden) – neu gegenüber 164–167 (Feuerwache/Personalamt, Tretboot, Versteigerung, Personalabteilung). Rückkehr zum Schauplatz in G1, weil die Geschichte zum Einstieg zurückkehrt.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Stadtteil** `fall`→`o1` | Straße: bestehende Apotheke (Fassade, Schild „Apotheke“), leerer Laden; Grete davor (Zertifikat, „Apothekerin mit Approbation“); „eigene Apotheke“ (Pille im Schaufenster); Antrag; Herr Dannemann kommt hinzu (1,5 s), redet (Blase), Kreuz und „Erlaubnis versagt“, „schon genug Apotheken“; Grete redet (Blase) | tabler `pills`, `first-aid-kit`, `pill`, `certificate`, `file-text`; Haken/Kreuz Fluent | `Fall · Grete will eine Apotheke eröffnen` (ab 0,0 s) → `· Die Erlaubnis wird versagt` → `· Darf der Staat das?` | Schritte (`szene_169schritte_1`, Freesound CC0 868548) |
| **A2 Die Frage** `frage0`, `klassiker` | Tafel, beide Figuren | tabler `pills`, `scale` | `Die Frage · Bedarf als Grenze?` → `· Das Apotheken-Urteil` | – |
| **B1 Der echte Fall** `bf`→`wirt` | Tafel: angestellter Apotheker, Antrag 1956, Traunreut; **Wortlautkarte Art. 3 Abs. 1 ApothekenG** (nach <380>), Marker zum Wort; ohne Figuren | tabler `certificate`, `map-pin`, `book`, `pills`, `coin`, `building-store` | `Der echte Fall · Traunreut 1956` → `· Art. 3 Abs. 1 ApothekenG` → `… › wirtschaftliche Grundlage` | – |
| **B2 Ablehnung** `abl`→`frage` | Tafel mit Kreuzen, Verfassungsbeschwerde, Frage; ohne Figuren | tabler `building`, `pill`, `trending-down`, `building-bank`, `scale` | `Der echte Fall · Die Behörde lehnt ab` → `· Verfassungsbeschwerde` → `· Die Frage` | – |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s | – | `Sachverhalt` | – |
| **D1 Art. 12 Abs. 1 GG** `a12`→`selbst` | **Wortlautkarte Art. 12 Abs. 1 GG**, vier Marker; Berufsbegriff, Schritt in die Selbständigkeit; Grete | tabler `book`, `briefcase`, `building-store` | `Berufsfreiheit, Art. 12 Abs. 1 GG · Wortlaut` → `› Berufsbegriff` → `› Schritt in die Selbständigkeit` | – |
| **D2 Wahl und Ausübung** `wahl`→`intens` | Pille Wortlaut, zwei Blöcke Wahl/Ausübung, gelber Block einheitliches Grundrecht, rote Pillen; beide Figuren | tabler `book`, `layers-intersect`, `shield-check`, `lock` | `… › Wahl und Ausübung` → `› einheitliches Grundrecht` → `› je näher an der Wahl, desto enger` | – |
| **E0 Mehrere Stufen** `stufen` | Treppe (Blau/Lila/Rot) auf der Tafel, Pille „Lehre: Drei-Stufen-Theorie“ | Treppe aus Grundformen | `Die drei Stufen › Drei-Stufen-Theorie` | – |
| **E1–E3 Stufe 1–3** `s1`→`konk` | **gleiche Tafelstruktur**: farbiger Kopf (Was?), Beispiel, Rechtfertigung (Formel wörtlich, wächst mit dem Wort), Fundstelle; rechts Mini-Treppe mit aktiver Stufe und eine Figur (Herr Dannemann bei Stufe 1, Grete bei 2 und 3). Stufe 3: Beispiel folgt in F1 (Sprechreihenfolge), Zusatz „Bloßer Konkurrenzschutz reicht nie.“ | Treppe | `Die drei Stufen › Stufe 1: Berufsausübung` → `› Stufe 1 › Rechtfertigung` usw. | – |
| **E4 Grundsatz** `gr`→`vh` | Tafel: niedrigste Stufe, nächste Stufe erst …; Pille „Lehre: konkretisierte Verhältnismäßigkeit“, Verweis auf eigene Folge; rechts große Treppe mit Pfeil | Treppe, `pfeil`, tabler `scale` | `… › niedrigste Stufe zuerst` → `› nächste Stufe nur, wenn die vorige nicht reicht` → `› konkretisierte Verhältnismäßigkeit` | – |
| **F1 Anwendung** `einord`, `obj` | Beispiel Bedarf/Tragfähigkeit, Kreuz „nicht in der Hand des Bewerbers“, roter Kopf Stufe 3, Haken „schärfste Stufe“; Mini-Treppe Stufe 3; Grete | Treppe | `Anwendung › das bayerische Gesetz` → `› objektive Zulassungsvoraussetzung (Stufe 3)` | – |
| **F2 Gefahr?** `volk`→`milder` | Haken Volksgesundheit, Kreuz keine Gefahr, Schweiz, grüner Block mildere Stufen; beide Figuren | tabler `heartbeat`, `search`, `world`, `gavel` | `Anwendung › Volksgesundheit` → `› keine Gefahr belegt (−)` → `› mildere Stufen genügen` | – |
| **F3 Ergebnis** `erg`→`nl` | Tafel: Bescheide aufgehoben, roter Block nichtig, grüner Block Niederlassungsfreiheit; Grete | tabler `building-bank`, `file-x`, `lock-open` | `Ergebnis · Art. 12 Abs. 1 GG verletzt` → `· Art. 3 Abs. 1 ApothekenG nichtig` → `· allein die Niederlassungsfreiheit` | – |
| **G1 Zurück zum Fall** `o2` | Schauplatz A1; Grete redet (Blase) | wie A1 | `Zurück zum Fall · Grete` | – |
| **G2 § 2 ApoG heute** `heute`→`gr2` | **Wortlautkarte § 2 Abs. 1 ApoG** (Auszug), Kreuz Bedarf, Haken objektive Schranke, grüne Pille; beide Figuren | tabler `book`, `certificate`, `map-pins`, `building-store` | `Zurück zum Fall · § 2 Abs. 1 ApoG heute` → `· kein Bedarf als Voraussetzung` → `· Grete bekommt die Erlaubnis` | – |
| **H Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · erst die Stufe, dann der Maßstab` → `· Wirkung nahe der Berufswahl` | – |
| **I Prüfschema** `sch`→`k5` | breite Karte, 7 Zeilen zum Wort | – | `Prüfschema` → je Gliederungspunkt | – |
| **J Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („1956“, „6.000“, „40 %“, „11.6.1958“, „§ 2 Abs. 1 ApoG“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 20 Folien; innerhalb harte Schnitte und Pops; Bewegung nur: Herr Dannemann geht auf Grete zu (1,5 s).
**Geräusche:** ein Handlungsgeräusch (Freesound CC0, Herkunft in `geraeusche_herkunft.json`).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Ladenfassaden und Treppe programmatisch (`laden()`, `treppe()` in `folien_169.py`).

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Ein seit 1940 approbierter Apotheker arbeitet als Angestellter in einer Apotheke in Traunstein. Im Juli 1956 beantragt er bei der Regierung von Oberbayern die Erlaubnis, in Traunreut eine eigene Apotheke zu eröffnen.
>
> Nach Art. 3 Abs. 1 des bayerischen Apothekengesetzes darf die Erlaubnis für eine neue Apotheke nur erteilt werden, wenn ihre Errichtung zur Sicherung der Arzneimittelversorgung im öffentlichen Interesse liegt und wenn ihre wirtschaftliche Grundlage gesichert ist, ohne die der benachbarten Apotheken so weit zu beeinträchtigen, dass ein ordnungsgemäßer Apothekenbetrieb nicht mehr gewährleistet ist.
>
> Die Behörde lehnt am 29. November 1956 ab: Für die rund 6.000 Menschen, die von Traunreut aus zu versorgen sind, genüge die eine vorhandene Apotheke völlig; deren Umsatz würde um 40 % sinken. Der Apotheker erhebt Verfassungsbeschwerde.
>
> **Verletzt die Regelung ihn in seinem Grundrecht aus Art. 12 Abs. 1 GG?**

Kein Fiktiv-Hinweis; die Quelle des echten Falls (BVerfG, Datum, Aktenzeichen) steht auf den Tafeln.
