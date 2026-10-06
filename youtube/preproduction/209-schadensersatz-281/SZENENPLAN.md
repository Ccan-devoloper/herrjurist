# Folge 209 · Schadensersatz statt der Leistung §§ 280, 281 BGB – Schema – Szenenplan

**Stand:** 06.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_209.py`](src/skript_209.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Schuldrecht AT · Schema. Hook nach Plan („Der Händler liefert die bezahlten Felgen nicht – du kaufst woanders teurer ein.“). Fiktiver Fall: Jörn kauft am 1.9.2026 im Reifenhandel von Ingolf vier Felgen für 1.200 € und zahlt sofort; Lieferung bis 8.9. zugesagt; nichts kommt; E-Mail am 10.9. „Bitte liefern Sie die Felgen umgehend.“; Ingolf vertröstet; drei Wochen später kauft Jörn bei Herta gleichwertige Felgen für 1.450 € und verlangt von Ingolf sein Geld zurück und die 250 € Mehrkosten; Ingolf will „nächste Woche“ doch noch liefern.
Ablauf: Fall (Kauf, Warten/E-Mail, Antwort, Deckungskauf, Forderung/Einwand) → Frage → Sachverhalt → A. Anspruchsgrundlage (Verweis 046) → § 280 Abs. 1, 3 (Wortlautkarten) → § 281 Abs. 1 Satz 1 (Wortlautkarte) → B. Schema: 1. Schuldverhältnis → 2. Pflichtverletzung (fällig, durchsetzbar) → 3. Frist („umgehend“ genügt, VIII ZR 49/15 Rn. 25; Zeitstrahl) → 4. Entbehrlichkeit § 281 Abs. 2 (Wortlautkarte, VIII ZR 226/14 Rn. 33) → 5. Vertretenmüssen → 6. Schaden (Rechenweg 1.450 € − 1.200 € = 250 €, VIII ZR 169/12) → C. Folge § 281 Abs. 4 (Wortlautkarte) → D. Abgrenzung Verzögerungsschaden (Verweis 112), Rücktritt (Verweis 116), § 325 → Ergebnis → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:44,4 (5.746 vertonte Zeichen); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Jörn (JO), um 30 | Käufer, Verbraucher, Gläubiger | `standing/easing-2` (offenes Hemd Rot `#F07A6A` über schwarzem Shirt der Pose, Hose Blau `#8DB3F2`, Turnschuhe), Kopf `Short 1`, Haut `#F2D0B4`, kein Bart; Mimiken `Calm`, `Smile`, `Serious` (redet, fordert), `Suspicious`, `Concerned\|Serious`, `Tired`, `Smile Big\|Smile` | `niklas` (Mann, jung) |
| Ingolf (IN), um 60 | Inhaber des Reifenhandels, Verkäufer, Unternehmer, Schuldner; vertröstet, kein Bösewicht | `standing/shirt-3` (Hemd Gelb `#F9D56E`, schwarze Hose der Pose), Kopf `No Hair 3` (Haarkranz), Brille `Glasses 4`, Haut `#EBC3A2`, kein Bart; Mimiken `Calm`, `Smile` (redet), `Concerned\|Serious` (klagt), `Fear`, `Suspicious`, `Solemn`, `Awe` | `helmut` (Mann, älter) |
| Herta (HE), um 35 | Inhaberin eines anderen Reifenhandels (ein freundlicher Satz) | `standing/pointing_finger-2` (schwarzes Oberteil der Pose, Hose Grün `#8FD694`, zeigt auf das Regal), Kopf `Medium Straight`, Haut `#C99572`; Mimiken `Calm`, `Smile`, `Smile Big\|Smile` (redet) | `ela_froh` (Frau, jung) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Stimmen:** nur aus dem Pool (niklas, helmut, ela_froh; `julia` gemieden). `ela_froh` spricht nur den freundlichen Verkaufssatz von Herta („Die habe ich da, für 1.450 €.“) – keine ernste Rolle. Vorfolge 206 nutzte denselben Pool (Pool vorgegeben); 207/208 andere Stimmen.
**Namen** mit eindeutig deutscher Aussprache, nicht in der Namensliste des Auftrags, nicht in der Reservierungsliste der parallelen Folgen (202–208) und in keinem `.py/.md/.json/.txt` unter `youtube/preproduction/` (Volltextsuche 06.10.2026; verworfen: Timo (Stimmenname im Ensemble, 203), Lothar (015, 199), Gerhard (160, 177 u. a.), Hubert (089, 112, 177), Gunther (zu nah an „Günter“)). Reserviert als „209: Jörn, Ingolf, Herta“. Nie im Genitiv (Skript-Assertion). Namensschilder Jörn Blau, Ingolf Grün, Herta Gelb.
**Blickrichtung:** Grundansicht gespiegelt (blickt nach links), `_r` nach rechts. A1: Ingolf blickt nach rechts zu Jörn, Jörn nach links. A2: Jörn nach links zum Laptop. A3: Ingolf nach links zum Laptop. A4: Herta zeigt nach links aufs Regal, Jörn blickt nach links zu ihr. A5 (geteiltes Bild): Jörn nach rechts zur Trennlinie, Ingolf nach links. N: wie A1. Tafelszenen: beide nach links zur Tafel. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `JO_redet`, `JO_fordert`, `IN_redet`, `IN_klagt`, `HE_redet` (je links/rechts) und Lexi. Keine weiteren Menschen im Bild. Figuren-PNGs `../peeps/op_209/` (80 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- Posen der letzten drei Folgen nicht verwendet (206: pointing_finger-1, robot_dance-2, resting-1; 207: blazer-3, walking-1, shirt-4; 208: robot_dance-3, walking-2, blazer-4); robot_dance-1 bleibt Lexi; Prothesen-Posen (blazer-1, blazer-2, shirt-1/2) verworfen; keine Polka Dots, keine Bärte, keine Karikatur. Kleidung neu: rotes offenes Hemd mit blauer Hose (Jörn), gelbes Hemd (Ingolf), schwarz-grün (Herta); 206 schwarz/braun/rosa, 207 lila/grün/türkis, 208 orange/blau/rosa.
- **Schauplätze neu:** Reifenhandel von innen (Rückwand, Wandregal mit Felgen; bei Ingolf später leer, bei Herta in Hellgrün voll), Carport bei Jörn mit Auto und Tisch mit Laptop, geteiltes Bild Jörn/Ingolf (Auto links, Laden-Symbol rechts). Grundformen aus `laden()`, `carport()`, `tisch()`, Requisiten aus Tabler. Gegenüber 206 (Garage, Motorradhändler), 207 und 208 (parallel) neu.
- Leitmotiv: **Zeitstrahl 10.9. → 1.10.** für die Frist („Jörn wartet 3 Wochen“). Cremegrund durchgehend, Tageslicht.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Der Kauf** `fall`–`in1` | ab 0,0 s Laden mit Regal und vier Felgen; Hook-Pillen zum Wort („liefert“, „teurer“); Jörn bei seinem Namen; Ingolf bei „Ingolf“; „1. September“, „4 Felgen: 1.200 €“; Geldschein „sofort bezahlt“; Blase Ingolf „Die Felgen liefere ich Ihnen / bis zum 8. September.“ | tabler:`wheel` (Weiß), `cash-banknote` (Grün) | `Fall · Die Felgen` → `… Der Kauf im Reifenhandel` → `… Jörn zahlt sofort` → `… Lieferung bis 8. September` | – |
| **A2 Das Warten / Die E-Mail** `warten`–`jo1` | Carport, Auto, Tisch mit Laptop; „8. September“, Paket durchgestrichen „nichts kommt“; „10. September“, E-Mail-Symbol und „E-Mail an Ingolf“; Blase Jörn „Bitte liefern Sie die / Felgen umgehend.“ | tabler:`car` (Blau), `device-laptop`, `package-off`, `mail` | `Fall · Das Warten` → `… Die E-Mail` → `… Jörn: „umgehend“` | `szene_209tippen_1` beim Wort „E-Mail“ |
| **A3 Ingolf antwortet** `antw`, `in2` | Laden mit leerem Regal, Tisch mit Laptop, „Antwort an Jörn“; Blase Ingolf „Die Felgen kommen / bald, versprochen.“ | tabler:`device-laptop`, `mail` | `Fall · Ingolf antwortet` | – |
| **A4 Bei Herta** `drei`–`kauft` | „3 Wochen später: immer noch nichts da“, „1. Oktober“; Laden von Herta (Hellgrün, acht Felgen); Herta zeigt aufs Regal; „gleichwertige Felgen?“; Blase Herta „Die habe ich da, / für 1.450 €.“; Kassenbon „1.450 € bezahlt“; E-Mail-Symbol bei „schreibt“ | tabler:`wheel`, `receipt-euro`, `mail` | `Fall · Drei Wochen später` → `… Bei Herta` → `… Jörn kauft bei Herta` | `szene_209kasse_1` beim Wort „kauft“ |
| **A5 Forderung und Einwand / Frage** `jo2`–`frage2` | geteiltes Bild (Trennlinie): links Jörn mit Auto, rechts Ingolf mit Laden-Symbol, E-Mail-Symbole; Blase Jörn (3 Zeilen) „Ihre Felgen will ich nicht mehr. / Ich will mein Geld zurück, und die / 250 € Mehrkosten zahlen Sie auch!“; Blase Ingolf „Aber die Felgen kommen / doch nächste Woche!“; Pillen „Kann Jörn die Mehrkosten verlangen?“, „War „umgehend“ überhaupt eine Frist?“ | tabler:`car`, `building-store`, `mail` | `Fall · Jörn: Geld zurück und Mehrkosten` → `… Ingolf will noch liefern` → `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig (35 px), ≈ 9,7 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Anspruchsgrundlage** `agl`–`sys` | „Jörn verlangt die Mehrkosten als / Schadensersatz statt der Leistung“, Block „§§ 280 Abs. 1, 3, 281 BGB“, Verweis Video 046 | tabler:`coin-euro`, `scale` | `A. Anspruchsgrundlage › …` | – |
| **D § 280** `w280`, `w3` | **Wortlautkarten § 280 Abs. 1** (Marker Pflicht, Schadens, vertreten) und **§ 280 Abs. 3** (Marker zusätzlichen Voraussetzungen, § 281) | tabler:`scale`, `hourglass` | `A. Anspruchsgrundlage › § 280 Abs. 1 BGB` → `… § 280 Abs. 3 BGB: zusätzlich § 281 BGB` | – |
| **E § 281 Abs. 1** `w281`–`plan` | **Wortlautkarte § 281 Abs. 1 Satz 1** (Marker fällige Leistung nicht, erfolglos, angemessene Frist), zwei Punkte, Block „Das Schema in 6 Schritten“ | tabler:`hourglass`, `package-off`, `mail`, `list-numbers` | `… § 281 Abs. 1 Satz 1 BGB › …` → `B. Schema · 6 Schritte` | – |
| **F 1. Schuldverhältnis** `s1`, `s1b` | ✓ Kaufvertrag zwischen Jörn und Ingolf, § 433 BGB | tabler:`file-text`, `arrows-exchange` | `B. Schema › 1. Schuldverhältnis …` | – |
| **G 2. Pflichtverletzung** `p1`–`p3` | „fällige, durchsetzbare Leistung nicht erbracht“; ✓ fällig (§ 271 Abs. 2); ✓ durchsetzbar (§ 320 Abs. 1) | tabler:`package-off`, `calendar-event`, `cash-banknote` | `B. Schema › 2. Pflichtverletzung › fällig` → `› durchsetzbar` | – |
| **H 3. Frist** `f1`–`f7` | Zitat der E-Mail; ✓ „„umgehend“ genügt …“ (VIII ZR 49/15 Rn. 25); Punkt „kein bestimmter Endtermin nötig“ (VIII ZR 254/08 Rn. 10 f.); Punkt zu kurze Frist (Verweis 116); Zeitstrahl 10.9.–1.10. mit „Jörn wartet 3 Wochen“; ✓ „Frist erfolglos abgelaufen“ | tabler:`hourglass`, `mail`, `circle-check`, `calendar-event`, `hourglass-low` | `B. Schema › 3. Frist › …` | – |
| **I 4. Entbehrlichkeit** `e1`–`e7` | **Wortlautkarte § 281 Abs. 2** (Marker ernsthaft und endgültig, besondere Umstände); Block strenge Anforderungen (VIII ZR 226/14 Rn. 33); ✗ „Ingolf vertröstet nur, er will ja liefern“; ✓ „Frist also nötig, und Jörn hat sie gesetzt“ | tabler:`hourglass-off`, `hand-stop`, `scale`, `mail`, `circle-check` | `B. Schema › 4. Entbehrlichkeit, § 281 Abs. 2 BGB › …` | – |
| **J 5. Vertretenmüssen** `v1`–`v3` | Block „vermutet: § 280 Abs. 1 Satz 2 BGB“; Punkte „Ingolf müsste sich entlasten“, „er nennt keinen Grund für die Verzögerung“ | tabler:`user-question`, `scale`, `message-off` | `B. Schema › 5. Vertretenmüssen › …` | – |
| **K 6. Schaden** `d1`–`d6` | Rechenweg: „so stellen, als hätte Ingolf ordnungsgemäß geliefert“ (§ 249 Abs. 1); 1.200 € / 1.450 €; Strich; „Differenz: 1.450 € – 1.200 € = 250 €“; Block „Schaden: 250 € Mehrkosten“; Block BGH Deckungskauf (VIII ZR 169/12 LS, Rn. 27) | tabler:`calculator`, `wheel`, `coin-euro` | `B. Schema › 6. Schaden › …` | – |
| **L Folge § 281 Abs. 4** `r1`–`r4` | Punkt „Ingolf will nächste Woche doch noch liefern“; **Wortlautkarte § 281 Abs. 4** (Marker ausgeschlossen, verlangt); ✓ „Jörn hat es mit seiner E-Mail verlangt“; Block „Nicht beides …“ (VIII ZR 169/12 Rn. 29) | tabler:`truck-delivery`, `ban`, `mail` | `C. Folge › …` | – |
| **M Abgrenzung** `ab1`–`ab4` | Block Verzögerungsschaden, Beispiel Montagetermin, „Verzug nötig: § 280 Abs. 2 mit § 286 BGB“ (Verweis 112); Block „bezahlte 1.200 € zurück: Rücktritt, § 323 BGB“ (Verweis 116); Punkt § 325 BGB | tabler:`arrows-split`, `clock`, `arrow-back-up`, `plus` | `D. Abgrenzung › …` | – |
| **N Ergebnis** `erg` | Laden von Ingolf, Jörn und Ingolf, Pillen „Ergebnis: 250 € Schadensersatz statt der Leistung“, „§§ 280 Abs. 1, 3, 281 BGB“, Geldschein „250 €“ | tabler:`cash-banknote` | `Ergebnis · Jörn bekommt 250 €` | – |
| **O Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | – |
| **P Klausurschema** `sch`–`k7` | breite Karte, Anspruchsgrundlage, 1.–6., Folge § 281 Abs. 4, jede Zeile zum Wort | – | `Klausurschema › …` | – |
| **Q Merksatz** `merke`, `mk2` | Lexi erklärt (redet), zwei Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund der Sprecherfigur, wortgleich mit dem Gesprochenen, Zahlen in Ziffern („8. September“, „1.450 €“, „250 €“).
**Bewertungszeichen:** Haken/Kreuz nur bei gesprochener Bejahung/Verneinung; Rechtsfolgen und Hinweise als neutrale Aufzählungspunkte.
**Übergänge:** stumme Schiebeblenden nur zwischen den 21 Folien; innerhalb harte Schnitte und Pops; kein Zoom.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Laden, Regal, Carport, Tisch aus Grundformen (`folien_209.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Jörn kauft am 1. September 2026 für sich privat im Reifenhandel von Ingolf vier Felgen für 1.200 € und zahlt sofort. Ingolf sagt die Lieferung bis zum 8. September zu.
>
> Bis dahin kommt nichts. Am 10. September schreibt Jörn per E-Mail: „Bitte liefern Sie die Felgen umgehend.“ Ingolf antwortet: „Die Felgen kommen bald, versprochen.“ Einen Grund für die Verzögerung nennt er nicht.
>
> Drei Wochen später ist immer noch nichts geliefert. Am 1. Oktober kauft Jörn gleichwertige Felgen bei Herta für 1.450 €. Dann schreibt er Ingolf: „Ihre Felgen will ich nicht mehr. Ich will mein Geld zurück, und die 250 € Mehrkosten zahlen Sie auch!“ Ingolf antwortet: „Aber die Felgen kommen doch nächste Woche!“
>
> **Kann Jörn die 250 € Mehrkosten verlangen?**
