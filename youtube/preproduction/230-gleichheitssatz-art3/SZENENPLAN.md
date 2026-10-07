# Folge 230 · Gleichheitssatz Art. 3 I GG: Willkürformel und Neue Formel – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_230.py`](src/skript_230.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Schema mit Fall. Aufbau nach Auftrag: Hook an der Kasse eines Freizeitbads (Preise als Ziffern: Einheimische 6 €, alle anderen 9 €) → Frage, echter Fall 2 BvR 470/08 → Sachverhalt → Wortlautkarten Art. 3 Abs. 1 und Art. 1 Abs. 3 GG (Bindung auch der Betreibergesellschaft) → Prüfung in zwei Schritten → I. Ungleichbehandlung (Vergleichsgruppen, gemeinsamer Oberbegriff, derselbe Träger) → II. Rechtfertigung: Maßstab (Willkürformel BVerfGE 1, 14 – Neue Formel BVerfGE 55, 72 – heute stufenlos, BVerfGE 88, 87; 138, 136; Kriterien für strengere Prüfung) → Wohnort als Grund (Rn. 38–40) → der echte Fall (Rn. 2–4, 24, 35 f., 42 f.) → Ergebnis → zurück zu Martha → Klausurtipp (Lexi: Vergleichsgruppe zuerst) → Prüfschema → Merksatz (Lexi). Hauptfilm 5:24,5 (4.775 vertonte Zeichen). Vorlagen: 208 (Werkzeuge, Hilfsfunktionen, Art. 3 nur verwiesen), 118 und 020 (Gleichheits- und Grundrechtsprüfung, nur verwiesen), 015 (Namens-/Sichtprüfung), Katzenkönig (Stil).

**Darstellung:** Bad und Gemeinde fiktiv und ohne Namen; der reale Beschwerdeführer und die realen Orte werden nicht genannt und nicht gezeigt (die Tafel nennt nur Gericht, Datum, Aktenzeichen). Kein Fiktiv-Hinweis.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Kühnel (KU), um 45 | Kassierer des Freizeitbads | `standing/pointing_finger-2` (zeigt nach oben zur Preistafel; schwarzes Shirt der Pose, Hose Türkis `#7FD6D0`), Kopf `Short 5`, Haut `#E3B08C`, kein Bart. Mimiken `Calm`, `Smile` (redet), `Suspicious`, `Serious` | `stephan` (Mann, mittel) |
| Frau Dittmer (DI), um 70 | Einwohnerin der Gemeinde | `standing/blazer-3` (Blazer Lila `#B8A9F5`, Hose `#5A5A66`), Kopf `Gray Medium` (Haar `#C9C9CF`), Brille `Glasses 3`, Haut `#F0C8A8`. Mimiken `Calm`, `Smile` (redet), `Cute`, `Suspicious` | `hilde` (Frau, älter) |
| Martha (MA), um 28 | wohnt im Nachbarort | `standing/walking-1` (geht zur Kasse; Oberteil Grün `#8FD694`, schwarze Hose der Pose), Kopf `Medium Bangs 2` (Haar `#7A4A2A`), Haut `#D9A47E`. Mimiken `Calm`, `Concerned\|Serious` (redet, Sorge), `Suspicious`, `Serious`, `Smile Big\|Smile` | `lucy` (Frau, jung) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. A1/H: Herr Kühnel (`_r`) blickt hinter dem Tresen nach rechts zu den Gästen; Frau Dittmer und Martha blicken nach links zur Kasse; Frau Dittmer geht nach links durch die Tür zum Becken, Martha rückt nach links zur Kasse auf. Tafelszenen alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `KU_redet`, `DI_redet`, `MA_redet` (je links/rechts) und Lexi. 56 Figuren-PNGs in `../peeps/op_230/` (nicht im Repository, im Drive-Master).
- **Stimmen** nur aus dem Pool (stephan, hilde, lucy; `christian` nicht besetzt, daher nie mit stephan in einer Szene).
- **Namen:** Martha, Kühnel, Dittmer – eindeutig deutsch („th“ in Martha wird deutsch als „t“ gesprochen), nicht in der Liste vergebener Namen, per `grep -rliw` in keinem Text unter `youtube/` und nicht in `namen_reserviert.txt` (07.10.2026; verworfen: Henrike – 106/127/146/159, Fröhlich/Gärtner – Adjektiv/Beruf, Merle – 104/117/159), eingetragen als „230: Martha, Kühnel, Dittmer“. Gesprochen werden „Martha“ (Erzählerin 2×) und „Dittmer“ (Erzählerin 1×); „Herr Kühnel“ nur auf dem Namensschild.

**Abweichung von den letzten Folgen (225–228; parallel 229):** Posen `pointing_finger-2`, `blazer-3`, `walking-1` – in 225 (`shirt-2`, `crossed_arms-1`, `walking-2`), 226 (`resting-1`, `blazer-4`, `crossed_arms-2`, `walking-3`), 227 (`blazer-4`, `pointing_finger-1`, `easing-1`, `resting-1`) und 228 (`robot_dance-2`, `polka_dots`, `sitting/crossed_legs`, `sitting/closed_legs-1`, `blazer-2`) nicht verwendet; keine Polka Dots, keine Bärte, keine Prothesen-Posen (`blazer-1` und `shirt-1` wegen Prothese verworfen). Schauplatz **Eingangshalle eines Freizeitbads mit Kasse, Preistafel und Tür zum Becken** – neu gegenüber 225–228. Rückkehr in H, weil die Geschichte zum Ausgangsfall zurückkehrt. Tageslicht-Cremegrund durchgehend.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Kasse** `fall`→`ma1` | ab 0,0 s Fassade „Freizeitbad“ (Fenster, Tür zum Becken), Preistafel „Eintritt“ (Preise zum Wort: „wer im Ort wohnt: 6 €“, „alle anderen: 9 €“), Tresen mit Kasse, Herr Kühnel, Pille „Freizeitbad einer kleinen Gemeinde“; Pillen Betreiberin und Urlauber/Gewinn; Herr Kühnel (Blase); Frau Dittmer zeigt den Ausweis (Blase), Ring um „6 €“; Kasse druckt die Karte; Frau Dittmer geht zum Becken (1,4 s, Schritte); Martha rückt auf, Ring um „9 €“, Martha (Blase) | tabler `pool`, `cash-register`, `building-bank`, `luggage`, `trending-up`, `id`, `ticket`; Fassade, Tresen, Preistafel, Tür programmatisch | `Fall · An der Kasse des Freizeitbads` (ab 0,0 s) → `· Betreiberin: Gesellschaft der Gemeinde` → `· Einwohner 6 €, alle anderen 9 €` → `· Frau Dittmer wohnt im Ort` → `· Martha wohnt im Nachbarort` → `· Ist das gerecht?` | Kassendrucker (`szene_230kasse_1`, Freesound CC0 476011), Schritte (`szene_230schritte_1`, Freesound CC0 595078) |
| **A2 Die Frage** `frage`→`drittel` | Tafel: Frage, gelber Block BVerfG 2 BvR 470/08, Block Rabatt rund ein Drittel; Martha, Frau Dittmer | – | `Die Frage · …` (3 Stände) | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,6 s | – | `Sachverhalt` | – |
| **C Gleichheitssatz und Bindung** `a3`→`gbind` | **Wortlautkarten Art. 3 Abs. 1 GG** (Marker „gleich“) und **Art. 1 Abs. 3 GG** (Marker Gesetzgebung/vollziehende/Rechtsprechung), grüner Block öffentliches Unternehmen; Martha | tabler `scale`, `building-bank`, `pool` | `Vorfrage · Maßstab: Art. 3 Abs. 1 GG` → `· Bindung: Art. 1 Abs. 3 GG` → `· auch die Betreibergesellschaft` | – |
| **D1 Zwei Schritte** `zwei`→`s2` | blaue Stufe I., Pfeil, gelbe Stufe II.; Frau Dittmer, Martha | Pfeil | `Prüfung · zwei Schritte` → `· I. Ungleichbehandlung` → `· II. Rechtfertigung` | – |
| **D2 I. Ungleichbehandlung** `vgl`→`ungl` | Vergleichsgruppen, blauer Block Oberbegriff, derselbe Träger, roter Block „6 € gegen 9 €“ mit Haken; über den Figuren „einheimisch“/„auswärtig“, „dasselbe Bad“, dann „6 €“/„9 €“ | tabler `pool` | `I. Ungleichbehandlung › …` (4 Stände) | – |
| **E1 Willkürformel** `mass`, `willk` | Zitatkarte BVerfGE 1, 14 <52> mit drei Markern; Herr Kühnel | tabler `scale`, `gavel` | `II. Rechtfertigung · Wie streng?` → `› Willkürformel, BVerfGE 1, 14` | – |
| **E2 Neue Formel** `neu`, `nf2` | Zitatkarte BVerfGE 55, 72 <88> mit vier Markern; Frau Dittmer | tabler `calendar`, `scale` | `› Neue Formel, BVerfGE 55, 72` → `› Neue Formel: Art und Gewicht der Unterschiede` | – |
| **E3 stufenlos** `heute`→`str3` | Farbband Grün–Gelb–Rot (Regler), Endbeschriftungen zum Wort, Zeiger wandert mit jedem Kriterium nach rechts; drei Haken-Zeilen; Martha | tabler `adjustments-horizontal`, `user`, `scale`, `lock-open`; Band und Zeiger programmatisch | `› heute: stufenloser Maßstab` → … → `› strenger: Freiheitsrechte betroffen` (5 Stände) | – |
| **F Wohnort** `wohn`→`ziele` | Haken „nicht von vornherein verwehrt“, „aber: Sachgründe nötig“, Kreuz „Wohnsitz allein: kein Grund“, gelber Block untrennbarer Sachgrund, vier Beispielzeilen zum Wort; Frau Dittmer | tabler `map-pin`, `home`, `link`, `wallet`, `scale`, `users`, `heart-handshake` | `› Wohnort als Grund?` → … → `› mögliche Sachgründe` (6 Stände) | – |
| **G1 Der echte Fall** `real`→`haush` | Klage, Instanzen, lila Block Grundrechtsbindung verkannt, drei Kreuze (Ziel, Ausgleich, Haushaltsmittel) zum „nicht“; Martha | tabler `luggage`, `building-bank`, `link`, `trending-up`, `users`, `pig-money` | `Der echte Fall · …` (5 Stände) | – |
| **G2 Ergebnis** `erg`, `aufh` | roter Block „Art. 3 Abs. 1 GG verletzt – nach den bisherigen Feststellungen“, Haken aufgehoben/zurückverwiesen; Martha | tabler `scale`, `building-bank` | `Ergebnis · …` (2 Stände) | – |
| **H Zurück zu Martha** `martha`, `anders` | Schauplatz A1; Kreuz an „9 €“ zum „nicht“, Martha froh; Pillen | wie A1 | `Zurück zu Martha · Mehrpreis nicht gerechtfertigt` → `· anders mit echtem Sachgrund` | – |
| **I Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (3 Stände) | – |
| **J Prüfschema** `sch`→`k6` | breite Karte, neun Zeilen zum Wort | – | `Prüfschema › …` | – |
| **K Merksatz** `merke`→`m3` | Lexi erklärt (redet), drei Sätze mit Markern | – | `Merksatz` | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen). **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („6 €“, „9 €“, „3 €“, „19.7.2016“, „7.10.1980“, „1980“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegung nur in A1 (Frau Dittmer geht zum Becken, Martha rückt auf).
**Geräusche:** zwei Handlungsgeräusche (Kassendrucker, Schritte; Freesound CC0, Herkunft in `geraeusche_herkunft.json`).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Fassade, Tresen, Preistafel, Tür, Farbband und Zeiger programmatisch.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Eine kleine Gemeinde lässt ihr Freizeitbad von einer Gesellschaft betreiben, die ganz der Gemeinde gehört. Das Bad wirbt um Urlauber aus der ganzen Region und soll Gewinn bringen.
>
> An der Kasse gilt: Wer im Ort wohnt, zahlt 6 €, alle anderen zahlen 9 €. Frau Dittmer wohnt im Ort und zahlt mit Ausweis 6 €. Martha wohnt im Nachbarort und soll für dasselbe Becken 9 € zahlen.
>
> Einen Ausgleich für besondere Lasten der Einwohner gibt es nicht, ebenso keinen Zuschuss aus dem Gemeindehaushalt. Einen anderen Grund als den Wohnort nennt die Gemeinde nicht.
>
> **Verletzt der Einheimischenpreis Martha in Art. 3 Abs. 1 GG?**
