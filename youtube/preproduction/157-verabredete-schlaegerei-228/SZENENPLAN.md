# Folge 157 · Verabredete Schlägerei: Einwilligung? Sittenwidrigkeit § 228 StGB – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_157.py`](src/skript_157.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Klassiker-Fall · StGB AT. Ablauf: fiktiver Einstieg nach dem Plan-Hook (Verabredung per Chat zu einem „Match“ auf der Wiese, 10 gegen 10, keine Waffen, zwei Schiedsrichter) → Frage → der echte Fall BGHSt 58, 140 sachlich (zwei Gruppen, faktische Übereinkunft, LG Stuttgart, BGH) → Sachverhalt → I. Einwilligung (Verweis Folge 062 in einem Satz) und **Wortlautkarte § 228**, Prüfungsort → II. Maßstab der guten Sitten (Gewicht und Gefahr, Sicht vor der Tat, konkrete Todesgefahr, Zweck) → III. Kern BGHSt 58, 140 (Gesamtumstände, Eskalationsgefahr, fehlende Absprachen und Sicherungen) und **Wortlautkarte § 231** → IV. Abgrenzung Boxkampf → V. Absprachen und Schiedsrichter (Rn. 23; BGHSt 60, 166) → Lösung des Falls → Ergebnis → Klausurtipp → Prüfschema → Merksatz. Hauptfilm 6:27,6 (5.746 vertonte Zeichen).
**Verhältnis zu den Vorfolgen:** 062 (Einwilligung, Wortlaut § 228, Maßstab BGHSt 49, 166) wird nur verwiesen; vertieft werden Gruppen, Eskalation und § 231. 155 (§§ 226, 227) war bei Produktionsbeginn noch in Arbeit und wurde nur gelesen, nicht angefasst. 146 als Klassiker-Muster (fiktiver Einstieg, echter Fall ohne Figuren, Rückkehr zum Einstieg).

**Darstellung (Vorgabe Koordinator):** keine Prügelszene, keine Schläge, kein Blut, keine Verletzten im Bild; keine echten Vereinsfarben, Fan-Schals oder Vereinslogos, keine Hooligan-Klischees. Die Gruppen erscheinen nur als neutrale farbige Gruppen-Icons (Tabler `users-group`) mit Pillen „Gruppe A“ (Blau) / „Gruppe B“ (Lila), im echten Fall „eine Gruppe“ (Gelb) / „andere Gruppe“ (Grün); die Verabredung über Chat- und Handy-Icons; die Wiese als Landschafts-Icon (Tabler `trees`, Phosphor `plant`). Sönke und Inken stehen ruhig in Alltagskleidung. „Verletzt“ steht nur als Text in Pillen. Im echten Fall keine Figuren.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Sönke, um 35 | verabredet das Match für Gruppe A, protestiert später („Regeln und Schiedsrichter!“) | `standing/resting-2` (schwarzes Oberteil, Hose Blau `#8DB3F2`, schwarze Schuhe), Kopf `Short 4`, Haut `#E2B088`, kein Bart, keine Brille. Mimiken `Calm` (ruhig), `Serious` (redet), `Driven` (Protest, redet), `Suspicious` (denkt), `Concerned\|Serious` (Sorge), `Solemn` (ernst) | `stephan` (Mann, mittel) |
| Inken, um 30 | antwortet für Gruppe B | `standing/walking-1` (Oberteil Lila `#B8A9F5`, schwarze Hose, weiße Schuhe), Kopf `Long Curly`, Haut `#F2CDB0`, keine Brille. Mimiken `Calm`, `Serious` (redet), `Suspicious`, `Concerned\|Serious`, `Smile`, `Solemn` | `lucy` (Frau, jung) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. Fallszene A und Lösung J: Sönke links blickt nach rechts zu Inken (`_r`), Inken rechts blickt nach links zu ihm. Tafelszenen: beide nach links zur Tafel. Kontaktbild `out/besetzung_157.png`.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `SO_redet`, `SO_protest`, `IN_redet` (je links/rechts) und Lexi.
- **Stimmen** nur aus dem Pool: stephan und lucy; christian und hilde nicht verwendet (keine Paarung stephan/christian). Erzählerin/Lexi Carla ohne Rolle.
- **Namen:** Sönke, Inken – eindeutig deutsch (norddeutsch), nicht in der Liste vergebener Namen und in keiner Datei unter `youtube/` (Volltextsuche 04.10.2026). Verworfen: „Hendrik“ (realer YouTuber „Herr Anwalt“, Tim Hendrik Walter, in `themenplanung/recherche_youtube.md`), „Birte“ (Verwechslung mit „bitte“, so schon 123), „Timo“ (Name einer Ensemble-Stimme).
- Figuren-PNGs: `../peeps/op_157/` (50 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 154 (`crossed_arms-2`, `blazer-3`), 155 (`blazer-4`, `walking-3`, `sitting/hands_back-1`), 156 (`easing-2`, `shirt-3`, `walking-2`, `robot_dance-2`, `pointing_finger-2`) – hier `resting-2` und `walking-1` (zuletzt 153 bzw. früher); keine Polka Dots, keine Prothesen-Posen, keine Bärte. Schauplatz **Wiese am Waldrand mit Gruppen-Icons** und **Stationen des echten Falls** – neu gegenüber 154–156 (Seminar, Bar/Pflaster, Familie); die Wiese kehrt in J wieder, weil die Lösung zum Einstiegsfall zurückkehrt.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Verabredung, Match, Frage** `fall`→`klassiker` | Bodenlinie, Wiese (Bäume, Pflanzen), Gruppen-Icons A/B ab 0,0 s; Chat-Pille; Sönke mit Handy und Nachrichten-Icon, redet (Blase); Inken mit Handy, redet (Blase); Match nur als Pillen (Kalender, zwei Haken, „leicht verletzt“), Fragepille, „Klassiker des BGH“ | tabler `trees`, `users-group`, `messages`, `device-mobile`, `message-circle`, `calendar`; ph `plant` | `Fall · Die Verabredung per Chat` (ab 0,0 s) → `Fall · Das Match` → `Fall · Die Frage` | 14 | Handyvibration (`szene_157handy_1`, Freesound CC0 708215), als Inkens Handy mit Sönkes Nachricht erscheint |
| **B1 Der echte Fall** `echt`→`minuten` | ohne Figuren: zwei Gruppen-Icons, Handy und `users-plus` (Verstärkung), Gegenpfeile, Pillen zum Wort, Stoppuhr | tabler `users-group`, `device-mobile`, `users-plus`, `stopwatch` | `Der echte Fall · BGHSt 58, 140 · zwei Gruppen` → `· die Übereinkunft` → `· die Folgen` | 8 | – |
| **B2 LG und BGH** `lg`→`frage` | Tafel, Requisit rechts (ohne Figuren) | tabler `gavel`, `building-bank`, `help-circle` | `… · LG Stuttgart` → `· BGH, 20.2.2013` → `· die Frage` | 5 | – |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **D Einwilligung, § 228** `einw`→`ort` | Tafel, **Wortlautkarte § 228** mit drei Markern, Pille Prüfungsort; beide Figuren | tabler `writing-sign`, `scale`, `list-check` | `I. Einwilligung · Voraussetzungen (eigene Folge)` → `· in Schläge und Tritte eingewilligt` → `› Grenze: § 228 StGB` → `› Prüfungsort: Rechtswidrigkeit` | 8 | – |
| **E Maßstab** `mass`→`heil` | Tafel, Haken, roter Block, Kreuz; Inken | tabler `scale`, `clock`, `alert-triangle`, `target-arrow`, `stethoscope` | `II. Gute Sitten › Maßstab: Gewicht und Gefahr` → `› Sicht vor der Tat` → `› jedenfalls: konkrete Todesgefahr` → `› und der Zweck?` | 8 | – |
| **F Eskalationsgefahr** `gesamt`→`sitten` | Tafel, gelber Block, zwei Kreuze, roter Block; beide Figuren | tabler `users-group`, `trending-up`, `file-x`, `lock-open`, `scale` | `III. BGHSt 58, 140 › Gesamtumstände` → `› Eskalationsgefahr` → `› keine Absprachen` → `› keine effektiven Sicherungen` → `› sittenwidrig` | 7 | – |
| **G § 231** `p231`→`vorfeld` | **Wortlautkarte § 231 Abs. 1** (Auszug, Strafrahmen „…“) mit vier Markern, grüner Block; Sönke | tabler `book`, `shield-check` | `III. … › Wertung des § 231 StGB` → `› Schutz schon im Vorfeld` | 7 | – |
| **H Boxkampf** `sport`→`grob` | Tafel, zwei Haken, Kreuz; Inken | fluent-emoji-flat `boxing-glove`; tabler `book`, `alert-triangle` | `IV. Abgrenzung: Sport › der Boxkampf` → `› nach den Regeln gedeckt` → `› grober Regelverstoß` | 6 | – |
| **I1 Absprachen?** `offen`, `neigt` | Tafel, gelber Block; beide Figuren | tabler `help-circle`, `scale` | `V. Absprachen und Schiedsrichter › offen gelassen` → `› BGH neigt zur Sittenwidrigkeit` | 3 | – |
| **I2 BGHSt 60, 166** `hool`→`box2` | Tafel, roter Block, Haken; beide Figuren | tabler `flag-2`, `scale`, `alert-triangle`; fluent `boxing-glove` | `V. … › BGHSt 60, 166` → `› Wertung des § 231 StGB` → `› Gefahr schwerer Gesundheitsschäden` → `› Unterschied zum Boxen` | 8 | – |
| **J Zurück zum Fall, Lösung** `s2`→`l6` | Schauplatz A; Sönke protestiert (Blase), Prüfliste (Karte zwischen den Figuren) Zeile für Zeile mit Haken/Kreuz | wie A | `Zurück zum Fall · Sönke` → `Lösung des Falls · Tatbestand, §§ 223, 224 Abs. 1 Nr. 4` → `· Rechtswidrigkeit: Einwilligung` → `· § 228 StGB` → `· sittenwidrig` | 8 | – |
| **K Ergebnis** `erg`→`p231c` | Tafel; beide Figuren | tabler `scale`, `gavel`, `book` | `Ergebnis · Einwilligung unwirksam` → `· strafbar, §§ 223, 224 Abs. 1 Nr. 4 StGB` → `· § 231 StGB nur bei schwerer Folge` | 5 | – |
| **L Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · Prüfungsort: Rechtswidrigkeit` → `· Gruppen: Eskalationsgefahr` | 7 | – |
| **M Prüfschema** `sch`→`k3` | breite Karte, 8 Zeilen zum Wort | – | `Prüfschema` → je Gliederungspunkt | 9 | – |
| **N Merksatz** `merke`, `m2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | 4 | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („10 gegen 10“, „2 Schiedsrichter“, „20.2.2013“, „§ 228“, „4–5 Minuten“).
**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; keine Bewegung, kein Zoom.
**Geräusch:** ein Handlungsgeräusch (Freesound CC0, Herkunft in `geraeusche_herkunft.json`).
**Lizenzen der Requisiten:** Tabler Icons (MIT), Phosphor Icons (MIT), Fluent Emoji Flat (MIT, Boxhandschuh), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`).

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Zwei Gruppen junger Leute geraten aneinander. Ein Angeklagter ruft per Telefon weitere Mitglieder seiner Gruppe herbei. Dann stehen sich beide Gruppen gegenüber. Aufgrund einer faktischen Übereinkunft wollen alle die Auseinandersetzung mit Faustschlägen und Fußtritten austragen; auch erhebliche Verletzungen billigen sie. Absprachen, die den Kampf begrenzen, gibt es nicht. In vier bis fünf Minuten werden mehrere Beteiligte erheblich verletzt.
>
> Das Landgericht Stuttgart verurteilt die Angeklagten wegen gefährlicher Körperverletzung (§§ 223, 224 Abs. 1 Nr. 4 StGB). Der Bundesgerichtshof verwirft die Revisionen (Beschluss vom 20.2.2013 – 1 StR 585/12, BGHSt 58, 140).
>
> **Sind die Körperverletzungen durch die Einwilligung der Verletzten gerechtfertigt?**

Kein Fiktiv-Hinweis; die Quelle des echten Falls (Gericht, Datum, Az.) steht auf der Karte.
