# Folge 116 · Rücktritt § 323 BGB: Das Prüfungsschema mit Fristsetzung – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_116.py`](src/skript_116.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Schuldrecht AT, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Der Online-Shop liefert die bezahlte Spielkonsole einfach nicht.“): Leni bestellt am 1. Juli 2026 privat im Online-Shop von Ottmar eine Spielkonsole für 499 € und zahlt per Vorkasse; Lieferung versprochen bis 8. Juli. Kein Paket. Am 15. Juli setzt sie per E-Mail eine Frist „bis morgen“; Ottmar bittet um Geduld (Lieferant). Am 30. Juli erklärt Leni den Rücktritt und verlangt die 499 € zurück.

Ablauf: Fall (Bestellung, Warten/Frist, Lager von Ottmar, Rücktritt) → Frage → Sachverhalt → Aufbau (drei Ebenen) → I. § 323 Abs. 1 (Wortlautkarte) → 1. gegenseitiger Vertrag → 2. fällige, durchsetzbare Leistung (§§ 271, 475 Abs. 1; Verweis 103) → 3. angemessene Frist, erfolglos (Zeitstrahl Juli, progressiv; zu kurze Frist) → 4. Entbehrlichkeit § 323 Abs. 2 Nr. 1–3 → 5. kein Ausschluss § 323 Abs. 5, 6 → typischer Klausurfehler Vertretenmüssen (Abgrenzung § 281; kein Verzug, Verweis 112) → II. § 349 (Wortlautkarte) → III. § 346 Abs. 1 → Abgrenzung § 326 Abs. 5 / § 437 Nr. 2 → Ergebnis → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:42,9 (5.595 vertonte Zeichen); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Leni, um 35 | Käuferin, Verbraucherin, Gläubigerin | `standing/easing-1` (offene Jacke Grün `#8FD694`, weißes Oberteil, schwarze Hose, Turnschuhe), Kopf `Long Curly` (schwarz), Haut `#D9A47E`; Mimiken `Calm`, `Smile` (redet), `Serious` (bestimmt, redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious`, `Tired` | `laura_ruhig` (Frau, mittel) |
| Ottmar, um 60 | Inhaber des Online-Shops, Verkäufer, Unternehmer, Schuldner | `standing/robot_dance-2` (schwarzes Oberteil, Hose Blau `#8DB3F2`; geöffnete Hand zur Bitte um Geduld), Kopf `No Hair 2` (Halbglatze), Brille `Glasses 3`, Haut `#F0CDB0`, kein Bart; Mimiken `Calm`, `Concerned|Serious` (redet), `Suspicious`, `Awe`, `Smile Big|Smile` | `william` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge vergeben (geprüft per `grep -rlw` über alle `.py/.md/.json` in `youtube/preproduction`: 0 Treffer, und gegen die Koordinatorliste): Leni, Ottmar. Verworfen: Greta, Wolfgang (beide schon in 003/115 verwendet). Kein Genitiv eines Namens im Sprechtext („die E-Mail von Leni an Ottmar“, „Wer an der Verzögerung schuld ist“).
- **Stimmen nur aus dem Pool** william, sabrina, marc, laura_ruhig: `laura_ruhig` (Leni, ruhig-bestimmt) und `william` (Ottmar, älter, beschwichtigend). `sabrina` und `marc` waren in 113 besetzt (Vorfolge-Regel), daher nicht verwendet.
- Präfixe `LE_`/`OT_` (nie `ER_`). Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts (nicht benötigt). In den Fallszenen steht die Figur rechts und blickt nach links zu Laptop bzw. Lager; in den Tafelszenen blicken beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `LE_redet`, `LE_bestimmt`, `OT_redet` und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur. **Keine weiteren Menschen im Bild** (der Lieferant erscheint nur im Satz von Ottmar).
- **Abwechslung:** Posen, Kleidung und Muster nicht aus 113 (`resting-1`, `shirt-1`), 114 (`crossed_arms-1`, `walking-2`, `blazer-4`), 115 (`shirt-3`, `sitting/crossed_legs`, `resting-2`, `blazer-3`) und nicht aus 112 (`pointing_finger-2`, `walking-1`); keine Polka Dots. Figurenrezepte verglichen.
- Figuren-PNGs: `../peeps/op_116/` (52 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 115 (Kneipe, Parkbank, Nacht), 114 (Terrasse/Staatsanwaltschaft), 113 (Nachbargrundstück, Anbau), 112 (Fahrradwerkstatt, Briefkasten). Hier neu: Lenis Wohnzimmer mit Schreibtisch, Laptop und Sessel (Warenkorb, E-Mail-Icons erscheinen über dem Laptop), Ottmars Lager (Lagerhaus-Icon, leerer Karton). Leitmotiv: **Zeitstrahl Juli 2026** für die Frist (15.7. Frist bis morgen → zu kurz → angemessene Frist läuft → 2 Wochen → 30.7. erfolglos). Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Die Bestellung** `fall`–`le1` | ab 0,0 s: Sessel, Schreibtisch, Laptop, Leni mit Namensschild; Warenkorb über dem Laptop bei „bestellt“, „1. Juli 2026“, „Online-Shop“, „Spielkonsole: 499 €“, „Vorkasse: sofort bezahlt“, „Lieferung bis 8. Juli“ zum Wort; Blase Leni „Bezahlt. In einer / Woche ist sie da.“ | tabler:`armchair` (Lila), `device-laptop`, `shopping-cart`, `device-gamepad-2` (Lila), `credit-card`, `truck-delivery`; Tisch programmatisch | `Fall · Die Bestellung` | `szene_116tippen_1` bei „bestellt“ |
| **A2 Warten/Frist** `warten`–`le2` | „8. Juli 2026“, „kein Paket“ (rot, Paket durchgestrichen); „15. Juli 2026“, Brief über dem Laptop bei „E-Mail“, „E-Mail an den Shop“; Blase Leni „Liefern Sie die Konsole / bitte bis morgen.“, „Frist: bis morgen“ | tabler:`package-off`, `mail` | `Fall · Das Warten` → `Fall · Die Frist` | `szene_116tippen_1` bei „E-Mail“ |
| **A3 Im Lager von Ottmar** `ott`–`ot1` | Lagerhaus, „Online-Shop von Ottmar“; leerer Karton und „Regal leer“ bei „leer“; Blase Ottmar (4 Zeilen) „Mein Lieferant hat mich / im Stich gelassen. Die Konsole / kommt bald, bitte haben Sie / noch etwas Geduld.“ | tabler:`building-warehouse` (Gelb), `package` | `Fall · Im Lager von Ottmar` | `szene_116karton_1` bei „leer“ |
| **A4 Der Rücktritt / Frage** `still`–`frage2` | „Zwei Wochen später“ → „30. Juli 2026“, „immer noch nichts da“; Brief bei „schreibt“, „Rücktritt“, „499 € zurück“; Blase Leni „Ich trete vom Kaufvertrag zurück. / Bitte überweisen Sie mir / die 499 € zurück.“; Pillen „Kann Leni wirksam zurücktreten?“, „War ihre Frist bis morgen nicht viel zu kurz?“ | tabler:`package-off`, `mail` | `Fall · Der Rücktritt` → `Fall · Die Frage` | `szene_116tippen_1` bei „schreibt“ |
| **B Sachverhalt** `sv` | Karte vollständig (34 px), ≈ 9,7 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Aufbau** `plan`–`p3` | Tafel „Rücktritt: drei Ebenen“: I. Rücktrittsrecht, § 323 BGB / II. Rücktrittserklärung / III. Rechtsfolge, je Farbkästchen zum Wort | tabler:`list-numbers`, `scale`, `mail`, `arrow-back-up` | `Rücktritt, § 323 BGB › Aufbau` | – |
| **D § 323 Abs. 1** `w1` | Wortlautkarte vollständig, Marker „gegenseitigen Vertrag“, „eine fällige Leistung nicht“, „erfolglos“, „angemessene Frist zur Leistung“, „vom Vertrag zurücktreten“; Block „Rücktrittsrecht nach erfolgloser Frist“ | tabler:`scale`, `hourglass` | `I. Rücktrittsrecht › § 323 Abs. 1 BGB` | – |
| **E 1. Gegenseitiger Vertrag** `g1`–`g2` | ✓ Kaufvertrag; „Ottmar schuldet die Konsole, / Leni den Kaufpreis: 499 €“; § 433 Abs. 1, 2 | tabler:`arrows-exchange`, `device-gamepad-2`, `coin-euro` | `I. 1. Gegenseitiger Vertrag` | – |
| **F 2. Fällige Leistung** `f1`–`f103` | ✓ „vereinbart: Lieferung bis 8.7.2026“, ✓ „dann fällig, die Lieferung bleibt aus“ (§ 271 Abs. 2), „ohne Termin: sofort fällig, § 271 Abs. 1“, „Verbrauchsgüterkauf: nur unverzüglich, § 475 Abs. 1“, ✓ „durchsetzbar: Leni hat bezahlt, keine Einrede“ (V ZR 11/18 Rn. 38), Block „Mehr dazu: Video „Einwendung und Einrede““ | tabler:`package-off`, `calendar-event`, `clock`, `hand-stop` | `I. 2. Fällige Leistung nicht erbracht` → `› ohne Termin` → `› durchsetzbar` | – |
| **G 3. Frist (Zeitstrahl)** `fr1`–`fr7` | Achse Juli 2026; Punkt + Brief „15.7.: Frist bis morgen“; rote Strecke 15.–16.7. + „zu kurz“; grüner Balken „angemessene Frist läuft“; „Zu kurze Frist setzt eine angemessene in Gang“ (VIII ZR 318/19 Rn. 28), „außer: Es kommt gerade auf die Kürze an“ (VIII ZR 351/19 Rn. 28, 43); Klammer 15.–30.7. „Leni wartet 2 Wochen“; Kreuz am 30.7.; ✓ „Frist erfolglos abgelaufen“ | tabler:`hourglass`, `hourglass-high`, `truck-delivery`, `package-off`, `mail` (Diagramm), Kreuz Fluent Emoji HC | `I. 3. Frist › angemessen, erfolglos` → `› zu kurz` → `› abgelaufen` | – |
| **H 4. Entbehrlichkeit** `e1`–`e5` | „§ 323 Abs. 2 BGB“; Nr. 1 Verweigerung (strenge Anforderungen, VIII ZR 226/14 Rn. 33), ✗ „Ottmar bittet nur um Geduld“; Nr. 2 Termin wesentlich, „etwa vor Vertragsschluss mitgeteilt“, ✗ „bloßer Liefertermin genügt nicht“; Nr. 3 nur bei nicht vertragsgemäßer Leistung, ✗ „hier bleibt die Lieferung aus“; Block „Frist nötig, und Leni hat sie gesetzt“ | tabler:`hourglass`, `hand-stop`, `calendar-event`, `alert-triangle` | `I. 4. Entbehrlichkeit › § 323 Abs. 2 BGB` → `› der Fall` | – |
| **I 5. Kein Ausschluss** `a1`–`a4` | Abs. 5 Satz 1, Satz 2, Abs. 6 je zum Wort; ✗ „Ottmar hat gar nichts geliefert“, ✗ „Leni trifft keine Verantwortung“; Block „kein Ausschluss“ | tabler:`ban`, `package`, `user-exclamation`, `check` | `I. 5. Kein Ausschluss › § 323 Abs. 5, 6 BGB` | – |
| **J Klausurfehler** `vm1`–`vm5` | Block „Vertretenmüssen prüfen“; ✗ „§ 323 BGB verlangt es nicht“ (BT-Drucks. 14/6040 S. 93, 184); „Vertretenmüssen gehört zum Schadensersatz statt der Leistung: §§ 281, 280 Abs. 1 BGB“; ✗ „auch kein Verzug nötig“, Block „Mehr dazu: Video „Schuldnerverzug““; ✓ „Wer schuld ist, spielt keine Rolle“ | tabler:`alert-triangle` (Rot), `scale`, `user-question` | `I. Rücktrittsrecht › kein Vertretenmüssen` | – |
| **K II. § 349** `r1`–`r2` | Wortlautkarte § 349, Marker „durch Erklärung“, „dem anderen Teil“; ✓ „E-Mail von Leni an Ottmar, 30.7.2026“, Block „Erklärung wirksam“ | tabler:`mail` | `II. Rücktrittserklärung › § 349 BGB` → `› der Fall` | – |
| **L III. Rechtsfolge** `rf1`–`rf3` | „§ 346 Abs. 1 BGB: empfangene Leistungen zurückgewähren“; ✓ „Ottmar: 499 € zurückzahlen“, ✓ „Leni: hat nichts erhalten, gibt nichts zurück“ | tabler:`arrow-back-up`, `coin-euro`, `package-off` | `III. Rechtsfolge › § 346 Abs. 1 BGB` | – |
| **M Abgrenzung** `ab1`–`ab2` | „Leistung unmöglich: § 326 Abs. 5 BGB“, „etwa: bestimmte gebrauchte Konsole verbrannt“, ✓ „Rücktritt nach § 323 BGB, ohne Fristsetzung“; „mangelhafte Konsole: § 437 Nr. 2 BGB“, ✓ „§ 323 BGB mit Frist zur Nacherfüllung“ | tabler:`device-gamepad-2`, `flame` (Rot), `tool` | `Abgrenzung › Unmöglichkeit, § 326 Abs. 5 BGB` → `› Mangel, § 437 Nr. 2 BGB` | – |
| **N Ergebnis** `erg`–`erg2` | ✓ „Leni ist wirksam zurückgetreten“, ✓ „Ottmar muss die 499 € zurückzahlen“ (§§ 323 Abs. 1, 349, 346 Abs. 1) | tabler:`scale`, `coin-euro` | `Ergebnis` | – |
| **O Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt: „Frist in drei Schritten prüfen: 1. gesetzt? 2. angemessen? 3. erfolglos abgelaufen?“; „Frist zu kurz? Mit der angemessenen Frist weiterrechnen, statt den Rücktritt abzulehnen.“ (VIII ZR 318/19 Rn. 28) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Frist in drei Schritten` → `· zu kurze Frist` | – |
| **P Klausurschema** `sch`–`k3` | breite Karte: I. Rücktrittsrecht (§ 323 Abs. 1) 1.–5., II. Rücktrittserklärung (§ 349), III. Rückgewähr (§ 346 Abs. 1), jede Zeile zum Wort | – | `Klausurschema` → `› I. Rücktrittsrecht` → `› II. Erklärung` → `› III. Rückgewähr` | – |
| **Q Merksatz** `merke`–`mk3` | Lexi erklärt; Marker „wer schuld ist.“, „Leistung, die ausbleibt,“, „und eine Frist, die erfolglos abläuft,“ | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 20 Folien; innerhalb harte Schnitte und Pops; keine Bewegungsanimation.
**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), wortgleich mit dem Gesprochenen, Zahlen als Ziffern („499 €“). Zahlen auf Tafeln, Pillen und Karte als Ziffern; Normwortlaut wörtlich.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Leni bestellt am 1. Juli 2026 für sich privat im Online-Shop von Ottmar, der den Shop gewerblich betreibt, eine Spielkonsole für 499 Euro. Sie zahlt sofort per Vorkasse. Versprochen ist die Lieferung bis zum 8. Juli.
>
> Bis zum 8. Juli kommt kein Paket. Am 15. Juli schreibt Leni per E-Mail: „Liefern Sie die Konsole bitte bis morgen.“ Ottmar antwortet, sein Lieferant habe ihn im Stich gelassen; die Konsole komme bald, Leni möge noch etwas Geduld haben.
>
> Am 30. Juli ist immer noch nichts geliefert. Leni erklärt Ottmar per E-Mail den Rücktritt vom Kaufvertrag und verlangt die 499 Euro zurück.
>
> **Kann Leni wirksam zurücktreten – und war ihre Frist „bis morgen“ zu kurz?**
