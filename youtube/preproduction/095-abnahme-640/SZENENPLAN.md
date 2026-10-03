# Folge 095 · Abnahme Werkvertrag § 640 BGB: Wirkungen und fiktive Abnahme – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_095.py`](src/skript_095.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Werkvertragsrecht, Themenplan-Format „Schema“ (Leitentscheidung im Plan leer). Beispielfall nach dem Plan-Hook („Der Fliesenleger ist fertig und will sein Geld – du hast Zweifel an den Fugen“): Susanne lässt das Bad ihrer Wohnung vom Fliesenleger Herrn Fiedler sanieren (neue Fliesen an Wand und Boden, neue Wanne), Rechnung 3.800 €. Hinter der Tür ist eine Fuge etwas breiter und ungleichmäßig (Schönheitsfehler, Nachbessern 150 €). Am nächsten Tag E-Mail mit 2 Wochen Frist zur Abnahme und Hinweis auf die Folgen.

Ablauf: Fall (Bad, Rechnung, Fuge) → E-Mail → Frage → Sachverhalt → Begriff → § 640 Abs. 1 (Wortlaut, Subsumtion) → § 640 Abs. 2 S. 1 (Wortlaut, drei Merkmale) → Verbraucher § 640 Abs. 2 S. 2 (Wortlaut, Subsumtion) → Mangel genannt / endgültige Verweigerung → Vorbehalt § 640 Abs. 3 → Wirkungen 1–2 (Fälligkeit, § 650g; Gefahr) → Wirkungen 3–5 (Verjährung, Beweislast, Mängelstadium) → Ergebnis mit § 641 Abs. 3 → Klausurtipp (Lexi) → Klausurschema Werklohn (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:16,1 (5.444 vertonte Zeichen); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Susanne (SU), um 40 | Verbraucherin, Bestellerin | `standing/easing-2` (korallrote offene Jacke `#F07A6A` über schwarzem Shirt, dunkelblaue Hose `#3D4A7A`, weiße Turnschuhe), Kopf `Medium Bangs 2` (braun `#7A4B2E`), Haut `#F2C9A5`; Mimiken `Calm`, `Serious` (redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious`, `Awe` | `laura_ruhig` (Frau, mittel) |
| Herr Fiedler (FI), um 50 | Fliesenleger, Unternehmer | `standing/shirt-3` (blaues Arbeitshemd `#5B7DB8`, schwarze Hose, weiße Schuhe), Kopf `Gray Short` (grau `#BDBDBD`), Haut `#E0A57E`; `Calm`, `Smile` (redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious`, `Serious` | `marc` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge vergeben (geprüft per `grep -rlw` im ganzen `youtube/`-Ordner und gegen die Koordinatorliste): Susanne, Fiedler. Kein Genitiv eines Namens im Sprechtext („die Rechnung von Herrn Fiedler“).
- **Stimmen nur aus dem Pool** william, sabrina, marc, laura_ruhig: gebraucht `laura_ruhig` und `marc`. `marc` war zuletzt in 091 (Wolfram) – im Pool gibt es nur zwei Männerstimmen, beide in 091 eingesetzt; `marc` (mittel) passt besser zum Handwerker um 50 als `william` (älter). `laura_ruhig` in 090–093 nicht eingesetzt.
- Präfixe `SU_`/`FI_` (nie `ER_`).
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Im Bad blickt Herr Fiedler (links) nach rechts zu Susanne, Susanne nach links zu ihm und zur Wand; in der E-Mail-Szene blickt Susanne nach links zur E-Mail; in den Tafelszenen blicken beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `SU_redet`, `FI_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur. Keine weiteren Menschen im Bild.
- **Abwechslung:** Posen, Kleidung und Muster nicht aus 091 (`robot_dance-3`, `shirt-4`, `walking-1`), 092 (`resting-1/-2`, `crossed_arms-1`), 093 (`robot_dance-2`, `blazer-3`, `pointing_finger-1`); `easing-2` (nicht `easing-1` wie 090); keine Polka Dots.
- Figuren-PNGs: `../peeps/op_095/` (44 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 091 (Katzenkönig), 092 (Laden, Wohnzimmer, Auszug), 093 (Behörde/Café). Hier neu: Badezimmer im Aufriss – zuerst die alte, vergilbte Wand, bei „Neue Fliesen“ die neu geflieste Wand mit Fugenraster, Wanne, Tür, Eimer und Kelle des Fliesenlegers; die eine breitere, ungleichmäßige Fuge neben der Tür; E-Mail als Bildschirmkarte. 056 (Werkvertrag) zeigte eine gestrichene Zimmerwand – hier Fliesen, anderer Fall, andere Figuren. Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Das neue Bad** `fall`–`su1` | Bad im Aufriss ab 0,0 s (alte Wand, Tür, Eimer, Kelle, beide Figuren mit Namensschild); „Neue“: Fliesenwand, Pille „neue Fliesen an Wand und Boden“; „Wanne“: Wanne + Pille; Blase Fiedler „Fertig! Hier ist meine / Rechnung: 3.800 €.“; Rechnung wandert von seiner Hand zu Susanne; Pille „3.800 €“; Lupe, roter Ring um die Fuge, Pillen „Fuge hinter der Tür: breiter, ungleichmäßig“, „reiner Schönheitsfehler“, „Nachbessern: 150 €“; Blase Susanne | Fliesenwand und Tür programmatisch (Palettenfarben); ph:`bathtub` (Weiß), `magnifying-glass`; tabler:`bucket`, `trowel`, `receipt-euro` | `Fall · Das neue Bad` (ab 0,0 s) → `Fall · Die Fuge hinter der Tür` | `szene_095rechnung_1`, als die Rechnung übergeben wird |
| **A2 Die E-Mail** `mail`–`frage2` | Pille „Am nächsten Tag“; E-Mail-Karte (Absender, Betreff, Frist, Hinweis zeilenweise zum Wort); Susanne liest (ruhig → denkt → staunt → Sorge); Pillen „Abnehmen und zahlen?“, „Und wenn sie schweigt?“ | tabler:`mail` (Gelb/Weiß), `calendar-event`; ph:`question` (Pink) | `Fall · Die E-Mail` → `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig (35 px), ≈ 9,7 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Begriff** `begr`–`b4` | Tafel: 1. körperliche Entgegennahme, 2. Billigung (VII ZR 276/13 Rn. 21); ✓ ausdrücklich, ✓ stillschweigend, Prüfzeit (VII ZR 64/09 Rn. 21 f.) | tabler:`zoom-question`, `hand-grab`, `thumb-up` | `Abnahme › Begriff` | – |
| **D § 640 Abs. 1** `p640`–`unw` | Wortlautkarte (3 Marker), Pflicht/Verweigerung nur bei wesentlichem Mangel, ✓ Fuge optisch, ✓ Bad nutzbar, grüner Block „unwesentlich: Susanne muss abnehmen“ | tabler:`gavel`, `grid-pattern`, `checks` | `Abnahme › Pflicht, § 640 Abs. 1 BGB` → `§ 640 Abs. 1 BGB › die Fuge` | – |
| **E1 § 640 Abs. 2 S. 1** `fikt`, `w640` | Frage „Und wenn der Besteller schweigt?“, Wortlautkarte (3 Marker), Merkmale 1–3 zum Wort | tabler:`hourglass`, `calendar-event` | `Abnahme › fiktive Abnahme, § 640 Abs. 2 Satz 1 BGB` | – |
| **E2 Verbraucher** `verb`–`schw` | Wortlautkarte Satz 2 (3 Marker), ✓ Verbraucherin, ✓ Fertigstellung/Frist/Hinweis, ✓ E-Mail Textform (I ZR 202/25 Rn. 20), gelber Block „Schweigen bis Fristende: gilt als abgenommen“ | tabler:`mail`, `user-check`, `hourglass` | `fiktive Abnahme › Verbraucher, § 640 Abs. 2 Satz 2 BGB` → `fiktive Abnahme › Susanne schweigt` | – |
| **E3 Mangel genannt** `mang`–`endg` | ✗ keine fiktive Abnahme, 1 Mangel genügt (BT-Drs.), Missbrauchsgrenze, Block „aber: Abnahmepflicht bleibt“, endgültige Verweigerung → fällig (VII ZR 158/09 Rn. 5) | tabler:`grid-pattern`, `cash-banknote` | `fiktive Abnahme › Verweigerung unter Angabe eines Mangels` → `Abnahmepflicht › endgültige Verweigerung` | – |
| **F Vorbehalt** `vorb`–`se` | Block „Abnehmen, aber unter Vorbehalt“, ✗ verloren § 634 Nr. 1–3, ✓ bleibt Schadensersatz Nr. 4 | tabler:`writing`, `alert-triangle` | `Abnahme › Vorbehalt, § 640 Abs. 3 BGB` | – |
| **G1 Wirkungen 1–2** `wirk`–`w2b` | 1. Fälligkeit, Bauvertrag § 650g Abs. 4, ✓ Rechnung; 2. Gefahrübergang, Rohrbruch-Beispiel | tabler:`list-numbers`, `cash-banknote`, `receipt-euro`, `shield`, `droplet` (Blau) | `Abnahme › Wirkungen` → `Wirkungen › 1. Fälligkeit, § 641 Abs. 1 BGB` → `Wirkungen › 2. Gefahrübergang, § 644 BGB` | – |
| **G2 Wirkungen 3–5** `w3`–`w5` | 3. Verjährung (2/5 Jahre), 4. Beweislast (VII ZR 301/13 Rn. 36), 5. Ende des Erfüllungsstadiums (Leitsatz 1, Rn. 35) | tabler:`hourglass`, `tool`; ph:`scales` | `Wirkungen › 3. Verjährung, § 634a Abs. 2 BGB` → `› 4. Beweislast` → `› 5. Mängelrechte, § 634 BGB` | – |
| **H Ergebnis** `erg`–`zbr2` | ✓ Abnahme unter Vorbehalt, ✓ fällig, ✓ Mangelbeseitigung; § 641 Abs. 3; Block „2 × 150 € = 300 € zurückhalten“, grüner Block „jetzt 3.500 €, Rest nach der Nachbesserung“ | tabler:`writing`, `cash-banknote`, `coins` | `Ergebnis · Abnahme unter Vorbehalt` → `Ergebnis › § 641 Abs. 3 BGB` | – |
| **I Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt; Reihenfolge 1.–3. zum Wort | Warnsymbol (Streamline Freehand) | `Klausurtipp · Abnahme bei der Fälligkeit` | – |
| **J Klausurschema** `sch`–`k3` | breite Karte „Klausurschema: Werklohn, § 631 Abs. 1 BGB“, I.–III. mit Unterpunkten Zeile für Zeile | – | `Klausurschema` → `› II. Fälligkeit` → `› III. Durchsetzbarkeit` | – |
| **K Merksatz** `merke`–`mk3` | Lexi erklärt, drei Zeilenpaare mit Markern (Zäsur, fällig, schweigt) | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; Bewegung nur bei der Übergabe der Rechnung.
**Blasen:** Stil C (`bausteine.blase`), wortgleich mit dem Gesprochenen, Zahl als Ziffer („3.800 €“). Zahlen auf Tafeln, Pillen und Karte als Ziffern.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Susanne lässt das Bad ihrer Wohnung vom Fliesenleger Herrn Fiedler sanieren: neue Fliesen an Wand und Boden, dazu eine neue Wanne. Als er fertig ist, gibt er ihr die Rechnung über 3.800 Euro, in der alle Posten aufgelistet sind.
>
> Hinter der Tür ist eine Fuge etwas breiter und ungleichmäßig. Das ist ein reiner Schönheitsfehler, das Bad ist dicht und voll nutzbar. Nachbessern kostet 150 Euro.
>
> Am nächsten Tag schreibt Herr Fiedler ihr eine E-Mail: Sie möge das Bad innerhalb von 2 Wochen abnehmen. Dazu der Hinweis: Wer schweigt oder die Abnahme ohne Angabe eines Mangels verweigert, bei dem gilt das Bad als abgenommen.
>
> **Muss Susanne abnehmen und zahlen, und was gilt, wenn sie schweigt?**
