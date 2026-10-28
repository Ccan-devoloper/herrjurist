# Folge 268 · Reparatur oder neues Gerät? Nacherfüllung § 439 BGB – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_268.py`](src/skript_268.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Kaufrecht · Alltagsfall. Fall: Undine kauft im August 2026 im Handyladen von Herrn Stelzer ein neues Smartphone für 600 €. 3 Wochen später schaltet es sich immer wieder von selbst aus. Auf ihren Wunsch repariert Herr Stelzer zweimal (Akku getauscht, Software neu aufgespielt), ohne Erfolg; die Ursache findet er nicht. Er bietet eine dritte Reparatur an, Undine will ein neues Handy; ein neues kostet ihn 450 €, eine Reparatur 60 €. Ablauf (Plan): Hook → Ausgangslage (Verbrauchsgüterkauf, Mangel, § 477; Verweis 063) → 1. Wahlrecht § 439 Abs. 1 (Wortlautkarte; Wechsel zur Lieferung, BGH VIII ZR 66/17) → 2. Ort der Nacherfüllung (§ 269; BGH VIII ZR 220/10) → 3. Verweigerung § 439 Abs. 4 (Wortlautkarte; relativ/absolut; Verweis 219) → 4. Fehlschlagen § 440 S. 2 (Wortlautkarte) → beim Verbraucher § 475d Abs. 1 Nr. 2 (Wortlautkarte), § 475 Abs. 4 in einem Satz → Ergebnis → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:30,2 (5.716 vertonte Zeichen, Grenze 6.200). Mehr als fünf Minuten wegen vier Wortlautkarten (§ 439 Abs. 1 und § 440 S. 2 vorgelesen, § 439 Abs. 4 und § 475d als Auszug), der im Plan verlangten vier Prüfungsstationen (Wahlrecht mit Wechsel, Ort, Verweigerung mit zwei Arten der Unverhältnismäßigkeit, Fehlschlagen) und der Abgrenzung zum Verbrauchsgüterkauf (§ 475d statt § 440, § 475 Abs. 4).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Undine (UN), um 35 | Käuferin, Verbraucherin | Pose `standing/crossed_arms-2` (schwarzes Oberteil der Pose, Hose Blau `#8DB3F2`), Kopf `Long`, Haut `#F2C9A0`; Mimiken `Calm`, `Smile`, `Smile Big|Smile`, `Suspicious`, `Concerned|Serious`, `Serious`, `Awe`, `Very Angry`, `Tired`; redet `Serious` (u1) und `Very Angry` (u2) – alle mit geschlossenem Mund | `sabrina` (Frau, mittel) |
| Herr Stelzer (ST), um 45 | Inhaber des Handyladens, Unternehmer | Pose `standing/blazer-3` (Blazer Lila `#B8A9F5`, schwarzes Shirt, Hose `#2E2E3A`), Kopf `Short 4`, Brille `Glasses 2`, Haut `#E3A47E`, kein Bart; Mimiken `Calm`, `Smile`, `Suspicious`, `Serious`, `Concerned|Serious`, `Awe`; redet `Smile` (s1) und `Serious` (s2) | `marc` (Mann, mittel) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `UN_redet`, `UN_redet2`, `ST_redet`, `ST_redet2` (je links/rechts) und Lexi. Stimmen nur aus dem Pool; `william` und `laura_ruhig` nicht besetzt (Vorfolge 267: `stephan`, `lucy`, `hilde`, `christian` – keine Überschneidung). Namen Undine und Stelzer: eindeutig deutsch, nicht in der Koordinatorliste, nicht in `namen_reserviert.txt`, unter `youtube/` (`rg -w`, .py/.md/.txt/.json/.csv) 0 Treffer; verworfen: Birte (Verwechslung mit „bitte“, wie 123/258), Dorit/Margret/Uta/Gretel (zu nah an Doris/Margit/Ute/Grete), Henrike (zu nah an Henrik/Henriette). Vor der Vertonung eingetragen als „268: Undine, Stelzer“. Kein Genitiv eines Namens (Assertion). Figuren-PNGs: `../peeps/op_268/` (70 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** Posen `crossed_arms-2` und `blazer-3` weder in 265–267 (`resting-2`, `shirt-1`, `walking-2`, `blazer-2`, `crossed_arms-1`, `shirt-3`, `easing-2`, `polka_dots`, `robot_dance-3`, `walking-3`) noch in den parallelen 269–271 (`blazer-1`, `pointing_finger-1`, `resting-2`, `blazer-4`, `resting-1`, `robot_dance-2`, `easing-1`); keine Polka Dots, keine Bärte. Schauplätze neu: Handyladen mit Theke und Wandregal, Wohnzimmer mit Sofa und Beistelltisch; 063 (Elektrogeschäft/Küche) und 219 (Fliesenhandel/Bad) zeigen andere Räume; bewusste Rückkehr in den Laden (Undine reklamiert dort).

**Darstellung:** keine echten Handymarken (Tabler `device-mobile` ohne Logo, ausgeschaltet `device-mobile-off`), fiktiver Laden „Handyladen Stelzer“. Keine Richterhämmer (Abwägung/Einzelfall als Waage `ph:scales`). Kein Streit mit Gewalt; Undine ist verärgert, Herr Stelzer freundlich-sachlich.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Laden** `fall`, `kauf` | Schild, Wandregal, Theke; Undine links, Herr Stelzer rechts | tabler:`device-mobile`, `credit-card` | `Fall · Undine kauft ein neues Smartphone` (ab 0,0 s) → `Fall · bezahlt und mitgenommen` | Undine · Herr Stelzer · Handy + „neues Smartphone“ · „600 €“ · Kartenterminal „bezahlt“ · Handy wandert zu Undine | Kartenterminal (`szene_268kasse_1`) |
| **B Zu Hause** `aus1`, `zurueck` | Fenster, Sofa, Lampe, Beistelltisch mit Handy | ph:`couch`, tabler:`lamp`, `device-mobile(-off)`, ph:`storefront` | `Fall · 3 Wochen später: Das Handy geht immer wieder aus` → `Fall · zurück in den Laden` | „3 Wochen später“ · Pille · Handy aus · „zurück in den Laden“ | – |
| **C Laden: Reparaturen, Streit, Frage** `u1`→`frage2` | wie A; Reparaturzähler oben links | tabler:`battery-2`, `tools`, `device-mobile-cog`, `device-mobile-off` | `Fall · Undine: „Bitte reparieren Sie es.“` → `… 1. Reparatur: Akku getauscht` → `… 1 Woche später: wieder aus` → `… 2. Reparatur: Software neu aufgespielt` → `… wieder aus` → Blasen → `Die Frage · …` | Blase Undine · Akku + Werkzeug · Zähler 1 · ✗ · Software · Zähler 2 · ✗ · Blase Stelzer · Blase Undine · Blase Stelzer · 2 Frage-Pillen | Schraubendreher (`szene_268schrauben_1`) |
| **D Sachverhalt** `sv` | Karte vollständig, ≈ 10 s, ohne Fiktiv-Zusatz | – | `Sachverhalt` | 1 | – |
| **E Ausgangslage** `lage`→`v063` | Tafel, beide | ph:`storefront`, tabler:`device-mobile-off`, `calendar` | `Ausgangslage · Verbrauchsgüterkauf` → `… › Sachmangel` → `… › Vermutung, § 477 Abs. 1 BGB` → `… › Folge …` | Zeilen §§ 13, 14 · ✓ § 474 · ✓ Mangel · Vermutung · Verweis 063 | – |
| **F 1. Wahlrecht** `p439`→`neu` | **Wortlautkarte § 439 Abs. 1**, Undine | tabler:`arrows-exchange`, `tools`, `device-mobile-off`, `device-mobile-check` | `A. Nacherfüllung › 1. Wahlrecht, § 439 Abs. 1 BGB` → … → `… › 1. neues Handy (+)` | Karte · 3 Marker · ✓ Wahl · zuerst Reparatur · ✗ gebunden · Treu und Glauben · Wechsel · (+) | – |
| **G 2. Ort** `ort`→`kost` | Tafel, beide | tabler:`map-pin`, ph:`storefront`, tabler:`coin-euro` | `… › 2. Ort der Nacherfüllung` → `… › 2. Ort: § 269 Abs. 1 BGB` → `… › 2. Kauf im Laden: beim Verkäufer` → `… › 2. Handy in den Laden bringen` → `… › 2. Kosten: Verkäufer, § 439 Abs. 2 BGB` | § 269 · Feld „Kauf im Laden“ · ✓ Laden · Kosten | – |
| **H 3. § 439 Abs. 4** `p4`→`abs` | **Wortlautkarte § 439 Abs. 4 S. 1, 2**, beide | tabler:`hand-stop`, ph:`scales` | `… › 3. Verweigerung, § 439 Abs. 4 BGB` → `… › 3. Abwägung …` → `… › 3. relative …` → `… › 3. absolute Unverhältnismäßigkeit` | Karte · 5 Marker · Feld relativ (Zeilen zum Wort) · Feld absolut · Fundstelle | – |
| **I 3. im Fall** `rsub`→`v219` | Tafel, Herr Stelzer | tabler:`calculator`, `tools`, `device-mobile`, `device-mobile-check` | `… › 3. relativ: 450 € gegen 60 €` → … → `… › 3. Verweigerung (−)` → `… › 3. Folge …` | Zeile · Block BGH · ✗ 2 Reparaturen · absolut · (−) · Verweis 219 | – |
| **J 4. § 440** `ruek`→`regel` | Tafel, **Wortlautkarte § 440 S. 2**, beide | tabler:`arrow-back-up`, `hourglass`, `tools` | `B. Rücktritt oder Minderung · ohne weitere Frist?` → … → `… › Regel, keine feste Grenze` | Frist · ✓ § 440 S. 1 · Karte · 3 Marker · Block „Regel“ | – |
| **K Verbraucher** `vgk`→`info` | Tafel, **Wortlautkarte § 475d Abs. 1 Nr. 2**, Undine | tabler:`user`, ph:`scales`, tabler:`info-circle` | `… › Verbraucher: § 475d statt § 440 BGB` → … → `… › Information vor der Nacherfüllung, § 475 Abs. 4 BGB` | Zeile · Karte · 2 Marker · Einzelfall · ✓ · Infoblock zeilenweise | – |
| **L Ergebnis** `erg`→`erg3` | Tafel, beide | tabler:`device-mobile-check`, `arrow-back-up`, `discount` | `C. Ergebnis · neues Handy (+)` → `… › oder Rücktritt ohne weitere Frist` → `… › oder Minderung` | (+) · Rücktritt · ✓ erheblich · Zug um Zug · Minderung | – |
| **M Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | Ebene 1 zeilenweise · Linie · Ebene 2 · § 475d | – |
| **N Schema** `sch`→`k6` | breite Karte, Punkt für Punkt | – | `Prüfungsschema …` | Titel · Anspruch · I.–V. · Alternative | – |
| **O Merksatz** `merke`, `merk2` | Lexi erklärt, Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; Bewegung nur bei sichtbarer Handlung (Handy wandert von der Theke zu Undine).
**Wortlautkarten:** § 439 Abs. 1, § 439 Abs. 4 S. 1, 2 (Satz 3 als „…“), § 440 S. 2, § 475d Abs. 1 Nr. 2 (Auszug mit „…“) wörtlich nach gesetze-im-internet.de (Abruf 08.10.2026) mit Fundstelle; Marker synchron zum gesprochenen Merkmal.
**Ziffern:** Auf Blasen, Tafeln und Pillen Zahlen als Ziffern („600 €“, „450 €“, „3 Wochen später“, „31.7.2026“, „§ 439 Abs. 4 BGB“), im Sprechtext als Wörter.

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Undine kauft im August 2026 für sich privat im Handyladen von Herrn Stelzer ein neues Smartphone für 600 €. 3 Wochen später schaltet es sich immer wieder von selbst aus. Undine bringt es in den Laden und bittet um eine Reparatur. Herr Stelzer tauscht den Akku; eine Woche später geht das Handy wieder aus. Bei der zweiten Reparatur spielt er die Software neu auf; wieder schaltet es sich ab. Die Ursache hat er nicht gefunden.
>
> Herr Stelzer bietet eine dritte Reparatur an. Undine will jetzt ein neues Handy. Ein neues kostet Herrn Stelzer 450 €, eine Reparatur 60 €. Mangelfrei ist das Handy 600 € wert.
>
> **Muss Herr Stelzer ein neues Handy liefern? Kann Undine gleich zurücktreten?**
