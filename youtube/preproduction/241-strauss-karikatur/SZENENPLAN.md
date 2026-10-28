# Folge 241 · Strauß-Karikatur: Darf man Politiker als Tiere zeichnen? – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_241.py`](src/skript_241.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Öffentliches Recht/Grundrechte, Klassiker-Fall. Ablauf laut Auftrag: 1. Hook (Redaktion → Büro der Ministerpräsidentin → Amtsgericht) → Frage → Sachverhalt → 2. Art. 5 Abs. 3 Satz 1 GG (Wortlautkarte), Karikatur als Kunst mit Beleg <377>, Verweis Folge 160 (Kunstbegriffe), keine Niveaukontrolle, Abgrenzung Art. 5 Abs. 1 GG (spezielle Norm, Verweis Folge 238), Eingriff → 3. vorbehaltlos, kollidierendes Verfassungsrecht: Persönlichkeitsrecht mit Kern Art. 1 Abs. 1 GG (Wortlautkarte), § 185 StGB → echter Fall → 4. Deutung: Aussagekern und Einkleidung (Zitatkarte <378>), Kern/Einkleidung im echten Fall, Entwertung als Person (Zitatkarte <380>), Menschenwürde ohne Güterausgleich (Zitatkarte <380>) → 5. Ergebnis → Lösung des fiktiven Falls → 6. Gegenfall Fuchs (Tiergestalt allein, <379>) → 7. Klausurtipp (Lexi), Prüfschema, Merksatz (Lexi).
**Länge:** Hauptfilm 6:02,0 bei 5.138 vertonten Zeichen (unter 7:00/6.200); Begründung in [`ABNAHME.md`](ABNAHME.md).

**Darstellung (Vorgabe Auftrag):** Die Original-Karikaturen werden **nicht** nachgezeichnet; keine sexuelle Darstellung. Tiere nur als neutrales Icon allein auf einem leeren Zeichenblatt (Tabler `pig` in Rosa; im Gegenfall Fluent Emoji High Contrast `fox` in Orange), auf dem Schreibtisch der Ministerpräsidentin als kleines Icon auf der Zeitschrift – ohne Figur, Pose oder Gesicht eines Menschen. Die reale Person ist **keine Figur**; „Strauß“ steht nur in der Fallbezeichnung (Pille, Tafeltitel, Prüfpfad). Echter Fall nur mit neutralen Icons (Kalender, Zeitschrift, Bleistift, Richterhammer, Waage). „in einer sexuell herabwürdigenden Pose“ einmal sachlich (Hook) und auf der Sachverhaltskarte.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Meinrad (ME), um 45 | Karikaturist | `standing/easing-2` (offene Jacke Lila `#B8A9F5` über schwarzem Shirt, Hose Grau `#6B6B78`), Kopf `Short 4`, Haut `#E2B48E`, kein Bart, keine Brille; Mimiken `Smile` (ruhig), `Serious` (redet/ernst), `Driven` (zeichnet), `Cute` (froh), `Concerned\|Serious` (Sorge), `Suspicious` (denkt) | `christian` (Mann, mittel) |
| Henriette (HE), um 30 | Redakteurin des Satiremagazins | `standing/crossed_arms-2` (schwarzes Oberteil, Hose Grün `#8FD694`), Kopf `Long Curly`, Haut `#F0C8A8`; `Smile` (ruhig/redet), `Cute`, `Suspicious`, `Serious` | `lucy` (Frau, jung) |
| Ministerpräsidentin Achenbach (AC), um 60 | fiktive Ministerpräsidentin, stellt Strafantrag | `standing/blazer-4` (Blazer Blau `#8DB3F2`, Oberteil Weiß, schwarze Hose), Kopf `Gray Bun`, Brille `Glasses 3`, Haut `#EDC3A3`; `Calm`, `Serious` (redet), `Rage\|Serious` (Ärger), `Solemn` (ernst), `Suspicious`, `Smile` | `hilde` (Frau, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Koordinatorliste, nicht in `namen_reserviert.txt` (dort vor der Vertonung als „241: Meinrad, Henriette, Achenbach“ eingetragen) und per `grep -rlw` über `youtube/` (`*.py/*.md/*.json/*.csv/*.txt`) ohne Treffer (07.10.2026). Verworfen: Ortwin (170, 215, 231), Lothar (015), Jette (159: englische Lesart), Mechthild (239: „ch-th“), Adalbert (53 Treffer), Jana (27 Treffer). Kein Genitiv eines Namens (Skript-Assertion). Gesprochen: „Meinrad“ (Erzählerin, 5×), „Achenbach“ (Erzählerin, 1×); Henriette nur auf dem Namensschild. Fallbezeichnung „Strauß-Karikatur“ (1× gesprochen), „Mephisto-Beschluss“ (Verweis, 1×).
- **Stimmen** nur aus dem Pool: `christian`, `lucy`, `hilde`; `stephan` nicht besetzt (also nie stephan/christian zusammen). Abweichung zu 160 (gleiches Grundrecht: lucy, stephan, hilde) durch `christian` statt `stephan`; 238 hatte marc/laura_ruhig.
- **Blickrichtung:** Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. Szene A1/I: Meinrad links blickt nach rechts zum Zeichenbrett, Henriette rechts blickt nach links. A2: Achenbach blickt nach links zum Schreibtisch. A3/H: beide blicken nach links zur Richterbank. Tafelszenen: alle nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `ME_redet`, `HE_redet`, `AC_redet` (je links/rechts) und Lexi. 62 Figuren-PNGs in `../peeps/op_241/` (Drive-Master).
- **Namensschilder** ab dem ersten Auftritt, solange die Figur im Bild ist; in A1 zusätzlich Rollenpillen „Karikaturist“, „Redakteurin“. Das lange Schild „Ministerpräsidentin Achenbach“ wird bei Bedarf so verschoben, dass es vollständig im Bild bleibt (`ns()`); deshalb steht die Ministerpräsidentin in Tafelszenen nur allein (FX), nie im Paar.

**Abweichung von den letzten Folgen:** 238 (`walking-1`, `robot_dance-3`, `resting-1`, `robot_dance-2`, `crossed_arms-1`), 239 (`easing-1`, `resting-2`, `shirt-4`), 240 (`easing-1`, `shirt-3`, `walking-1`): keine dieser Posen. Keine Prothesen-Posen (shirt-1/-2, blazer-1/-2 geprüft und verworfen), keine Polka Dots, keine Bärte. Schauplätze **Redaktion** (Zeichenbrett, Pinnwand), **Büro** (Fenster, Schreibtisch, Zeitschrift) und **Amtsgericht** (Richterbank, Richterhammer) – neu gegenüber 238–240 (Stadion, Garage/Werkstatt, Laden). Rückkehr ins Amtsgericht (H) und in die Redaktion (I), weil die Geschichte zum Ausgangsfall bzw. zum Zeichenbrett zurückkehrt. Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Redaktion** `fall`→`he1` | Meinrad am Zeichenbrett, Henriette; Blatt zeigt das Schwein-Icon; Pillen Karikatur/Pose/Botschaft; Henriette redet (Blase) | tabler:`pig`; Zeichenbrett, Pinnwand programmatisch | `Fall · In der Redaktion eines Satiremagazins` (ab 0,0 s) → `· Die Karikatur` → `· Die Botschaft` → `· Satire darf alles?` | leeres Blatt · Pille Karikatur · Schwein-Icon · Pose · Botschaft · Henriette redet | Stift (`szene_241stift_1`) |
| **A2 Büro** `heft`, `ac1` | Zeitschrift auf dem Schreibtisch; Achenbach sieht sie, ärgert sich, redet (Blase), Pille Strafantrag | ph:`newspaper`, tabler:`pig` (klein); Fenster, Tisch | `Fall · Das Heft erscheint` → `· Der Strafantrag` | Heft · denkt · Ärger · redet · Strafantrag | – |
| **A3 Amtsgericht** `urteil`→`klassiker` | Richterbank, Hammer; Meinrad redet (Blase); Achenbach daneben; Fragen; Fallbezeichnung | tabler:`gavel` | `Fall · Das Amtsgericht verurteilt` → `· Meinrad: Das ist Kunst` → `Die Frage · Darf man Politiker als Tiere zeichnen?` → `Die Frage · Beschluss zur Strauß-Karikatur` | Bank · Hammer/Urteil · redet · Frage · Frage 2 · Strauß-Karikatur | Richterhammer (`szene_241hammer_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **C1 Schutzbereich** `a53`→`v160` | Wortlautkarte Art. 5 Abs. 3 Satz 1 GG, Frage, Zitatblock <377>, (+), Verweis 160; Meinrad | tabler:`palette`, `pencil`, `brush`, `book` | `I. Schutzbereich · Art. 5 Abs. 3 Satz 1 GG` → `› Ist eine Karikatur Kunst?` → `› Karikatur ist Kunst (+)` → `› Kunstbegriffe: Folge zum Mephisto-Beschluss` | Karte · 2 Marker · Frage · Zitat + (+) · Verweis | – |
| **C2 Kunst und Meinung** `niveau`→`eingriff` | Niveaukontrolle ✗, Meinung, ✓ schließen sich nicht aus, Block spezielle Norm, Verweis 238, Eingriff (+); Meinrad, Henriette | tabler:`brush`, `message-circle`, `palette`, `gavel` | `I. Schutzbereich › keine Niveaukontrolle` → `› zugleich eine Meinung` → `› Art. 5 Abs. 3 GG als spezielle Norm` → `› Abgrenzung zu Art. 5 Abs. 1 GG` → `II. Eingriff · Verurteilung wegen Beleidigung (+)` | 8 | – |
| **D Schranken** `vorb`→`licht` | ✗ Gesetzesvorbehalt, ✓ kollidierendes Verfassungsrecht, Block APR, Wortlautkarte Art. 1 Abs. 1 GG, ✓ § 185 StGB, Licht der Kunstfreiheit; Achenbach | tabler:`shield-check`, `fingerprint`, `gavel` | `III. Rechtfertigung · kein Gesetzesvorbehalt` → `› kollidierendes Verfassungsrecht` → `› allgemeines Persönlichkeitsrecht` → `› Kern: Art. 1 Abs. 1 GG` → `› § 185 StGB schützt die Ehre` → `› Auslegung im Licht der Kunstfreiheit` | 9 | – |
| **E Der echte Fall** `echt`→`vb` | ohne Figuren; Pillen zum Wort, Icons auf der Bodenlinie | tabler:`calendar-event`, ph:`newspaper`, tabler:`pencil`, `gavel`, `scale` | `Strauß-Karikatur · der echte Fall` → `› die Karikaturen` → `› Schuldspruch` → `› Verfassungsbeschwerde` | 7 | – |
| **F Deutung** `deut`→`milde` | Übertreibung, Gewand, Blöcke Kern/Einkleidung, Zitatkarte <378> mit Markern, Block milderer Maßstab; Meinrad, Henriette | tabler:`zoom-question`, `search`, `masks-theater`, `scale` | `Deutung · Wie prüft man Satire?` → `› Übertreibung und Verfremdung` → `› Aussagekern` → `› Einkleidung` → `› gesondert prüfen` → `› Einkleidung: weniger strenger Maßstab` | 9 | – |
| **G1 Kern/Einkleidung im echten Fall** `kern1`→`oeff` | Blöcke, Zitatkarte <380> mit Markern, ✓ personale Würde; Achenbach | tabler:`search`, `masks-theater`, `shield-check`, `podium` | `Strauß-Karikatur › Aussagekern` → `› Einkleidung` → `› Entwertung als Person` → `› Politiker: personale Würde bleibt` | 6 | – |
| **G2 Menschenwürde, Ergebnis** `abw`→`zurueck` | Abwägung als Regel, Zitatkarte <380> mit Markern, Ergebnisblöcke; Meinrad | tabler:`scale`, `shield-check`, `gavel` | `Strauß-Karikatur › sonst: Abwägung` → `› Menschenwürde: absolute Schranke` → `Strauß-Karikatur · Ergebnis: Verurteilung verfassungsgemäß` | 8 | – |
| **H Zurück zu Meinrad** `zur`→`zv` | Amtsgericht wie A3; ✓ Kern, ✗ Einkleidung, Pillen Menschenwürde und Ergebnis; Mimikwechsel | wie A3 | `Zurück zu Meinrad · die Lösung` → `› Aussagekern: zulässige Kritik` → `› Einkleidung: Entwertung als Person` → `› Menschenwürde` → `› Verurteilung hält` | 7 | – |
| **I Gegenfall** `gegen`→`abw2` | Redaktion wie A1, leeres Blatt; Meinrad redet (Blase), zeichnet; Fuchs-Icon; Pillen | fluent-emoji-high-contrast:`fox` | `Gegenfall · Nie als Tiere zeichnen?` → `· Meinrad zeichnet einen Fuchs` → `› übliche Karikatur` → `› Abwägung, milderer Maßstab` | 6 | Stift (`szene_241stift_1`) |
| **J Klausurtipp** `tipp`→`t3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Art. 5 Abs. 3 statt Abs. 1 GG` → `· Kern und Einkleidung trennen` → `· Menschenwürde nicht vorschnell` | 7 | – |
| **K Prüfschema** `sch`→`k3c` | breite Karte, Zeile für Zeile | – | `Prüfschema` → `› I. Schutzbereich` … `› III. 3. Abwägung` | 7 | – |
| **L Merksatz** `merke`, `m2` | Lexi erklärt (redet), Marker | – | `Merksatz` | 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; kein Zoom.
**Geräusche:** zwei Handlungsgeräusche, drei Einsätze (Stift beim Zeichnen in A1 und I, Richterhammer beim Urteil in A3). Freesound-API am 07.10.2026 über den Proxy gesperrt (HTTP 403); daher Kopien vorhandener sfx3-Dateien unter eigenem Namen, Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** Stil C, wortgleich mit dem Gesprochenen. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („3.6.1987“, „§ 185 StGB“, „3 Fällen“, „Art. 5 Abs. 3 Satz 1 GG“).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Phosphor (MIT), Haken/Kreuz und Fuchs Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Der Karikaturist Meinrad zeichnet für ein Satiremagazin die Ministerpräsidentin Achenbach als Schwein, in einer sexuell herabwürdigenden Pose. Seine Botschaft: Sie mache Politik für Bauinvestoren. Die Redakteurin Henriette druckt die Karikatur: „Satire darf alles.“
>
> Die Ministerpräsidentin stellt Strafantrag. Das Amtsgericht verurteilt Meinrad wegen Beleidigung (§ 185 StGB).
>
> Meinrad beruft sich auf die Kunstfreiheit: Seine Zeichnung sei Kunst und kritisiere ihre Politik.
>
> **Verletzt die Verurteilung Meinrad in seinem Grundrecht aus Art. 5 Abs. 3 Satz 1 GG?**

Kein Fiktiv-Hinweis; beim echten Fall stehen Gericht, Datum, Aktenzeichen und Fundstelle auf der Pille.
