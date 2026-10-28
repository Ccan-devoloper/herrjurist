# Folge 129 · Mängelrechte Werkvertrag § 634 BGB: Schema und Unterschiede zum Kauf – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_129.py`](src/skript_129.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Zivilrecht/Werkvertragsrecht, Themenplan-Format „Schema“ (Leitentscheidung im Plan leer). Beispielfall nach dem Plan-Hook („Das neue Dach ist undicht – und der Dachdecker reagiert nicht auf Anrufe“): Beate lässt das Dach ihres Hauses vom Dachdecker Herrn Wenzel für 18.000 € neu eindecken, prüft es und nimmt es ab, zahlt. Zwei Monate später nach Starkregen Wasserflecken an der Decke; ein anderer Dachdecker findet den Anschluss am Schornstein undicht, Reparatur laut Angebot 2.400 €. Herr Wenzel geht nicht ans Telefon.

Ablauf: Fall (Dach, Abnahme) → Regen/Befund → keine Antwort → Frage → Sachverhalt → 1. Werkvertrag und Abnahme (Bauvertrag) → 2. Mangel (Wortlaut § 633 Abs. 2, Auszug) → 3. Rechte (Wortlaut § 634) → Nacherfüllung/Wahlrecht → Selbstvornahme (Wortlaut § 637 Abs. 1), Frist → Vorschuss (Wortlaut § 637 Abs. 3) → Rücktritt/Minderung/Schadensersatz → 4. Verjährung (Wortlaut § 634a, Auszug) → 5. Unterschiede zum Kauf (Tabelle, Zeile für Zeile) → Ergebnis → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:35,9 (5.765 vertonte Zeichen); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Beate (BE), um 35 | Hauseigentümerin, Bestellerin | `standing/pointing_finger-2` (schwarzes Langarmoberteil der Pose, Hose Lila `#B8A9F5`, schwarze Schuhe), Kopf `Long` (schwarz), Haut `#F2C9A5`; Mimiken `Calm`, `Smile`, `Smile Big|Smile`, `Concerned|Serious` (redet), `Suspicious`, `Awe`, `Rage|Serious` | `ela_froh` (Frau, jung) |
| Herr Wenzel (WE), um 60 | Dachdecker, Unternehmer | `standing/shirt-4` (schwarzes Hemd der Pose, Arbeitshose Grau `#5B5F66`, weiße Schuhe), Kopf `No Hair 3` (Glatze, weißer Haarkranz), Haut `#E0A57E`; `Calm`, `Smile` (redet), `Smile Big|Smile`, `Serious`, `Suspicious` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge vergeben (geprüft per `grep -rlw` im ganzen `youtube/`-Ordner und gegen die Koordinatorliste): Beate, Wenzel. Kein Genitiv eines Namens im Sprechtext („Beates Haus“ nur auf der Pille, gesprochen „das Dach ihres Hauses“).
- **Stimmen nur aus dem Pool** niklas, helmut, ela_froh, julia: gebraucht `ela_froh` (Bestellerin, jung) und `helmut` (Handwerker, älter); `julia` nicht verwendet (Vorgabe), `niklas` nicht gebraucht. In 126 liefen alle drei Poolstimmen außer julia; eine Wiederholung war deshalb nicht vermeidbar. Lea nicht verwendet.
- Präfixe `BE_`/`WE_` (nie `ER_`).
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Fallszene A1: Herr Wenzel (links) blickt nach rechts zu Beate, Beate nach links; A2/A3: Beate nach links zum Haus; Tafelszenen: beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `BE_redet`, `WE_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (`shirt-1/-2` deshalb verworfen), keine Karikatur. Der zweite Dachdecker und andere Menschen erscheinen nicht im Bild (Befund nur als Ring und Pille).
- **Abwechslung:** Posen nicht aus 126 (`blazer-1`, `shirt-3`, `walking-1`, `blazer-4`), 127 (`blazer-2`, `crossed_arms-2`), 128 (`easing-1`, `resting-2`); keine Polka Dots. Kopf `hat-beanie` verworfen (Mütze liegt in der Hautfläche und würde hautfarben).
- Figuren-PNGs: `../peeps/op_129/` (46 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 126 (Gerichtssaal), 127 (EuGH/Strom), 128 (Wohnung/Krankenzimmer). Hier neu: Einfamilienhaus im Aufriss mit Ziegeldach (programmatisch aus Palettenflächen: Wand, Fenster, Tür, Dachfläche mit Ziegelreihen, Schornstein), altes graues Dach → neues rotes Dach, Regenwolken, Wasserflecken an der Decke, roter Ring am Schornstein; Telefon-Symbole. 095 (Abnahme) spielte im Bad, 063 (Käuferrechte) im Laden/der Küche. Cremegrund durchgehend, Tageslicht (Regen nur als Wolken-Icon).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Das neue Dach** `fall`–`bez` | Haus ab 0,0 s (altes graues Dach, Herr Wenzel und Beate mit Namensschild, Pille „Beates Haus“); bei „neu“ das rote Ziegeldach und Pille „neu eindecken“; „18.000 €“; „nach 3 Wochen: fertig“; Blase Wenzel „Fertig! Das Dach hält / jetzt viele Jahre.“; Lupe bei „genau“; Haken und Pille „abgenommen“ bei „nimmt“; Beleg und „Rechnung bezahlt“ | Haus programmatisch; tabler:`zoom-check`, `receipt-euro` | `Fall · Das neue Dach` (ab 0,0 s) → `Fall · Die Abnahme` | – |
| **A2 Zwei Monate später** `regen`–`kost` | Pille „2 Monate später“; zwei Regenwolken bei „regnet“; Wasserflecken an der Decke + Pille; roter Ring am Schornsteinanschluss, Pille „Anschluss am Schornstein undicht“; Angebot und Pille „Reparatur laut Angebot: 2.400 €“; Beate ruhig → Sorge → denkt → staunt | tabler:`cloud-rain` (Blau), `file-invoice` | `Fall · Zwei Monate später` → `Fall · Der undichte Anschluss` | `szene_129regen_1` bei „regnet“ |
| **A3 Keine Antwort** `anruf`–`frage2` | Telefon mit Rufzeichen bei „ruft“, bei „Niemand“ durchgestrichenes Telefon und Pille „Herr Wenzel geht nicht ran“; Blase Beate „Herr Wenzel, mein Dach / ist undicht! Bitte rufen / Sie mich zurück.“; Pille „3 weitere Anrufe: keine Antwort“, Beate ärgerlich; Fragen | tabler:`phone-calling`, `phone-x` (Rot) | `Fall · Keine Antwort` → `Fall · Die Frage` | `szene_129telefon_1` (Freizeichen) bei „ruft“ |
| **B Sachverhalt** `sv` | Karte vollständig (38 px), ≈ 9,7 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C 1. Werkvertrag und Abnahme** `p1`–`bau` | Erfolg geschuldet, ✓ Werkvertrag § 631, Pille Verweis Dienstvertrag, Mängelrechte erst nach Abnahme (VII ZR 301/13 LS 1), ✓ abgenommen, Pille Verweis Abnahme, ✓ Bauvertrag § 650a, Block „gelten nur ergänzend“ | tabler:`home` (Ziegelrot), `checklist`, `building` | `1. Werkvertrag und Abnahme` → `1. › Abnahme als Zäsur` → `1. › Bauvertrag, § 650a BGB` | – |
| **D 2. Mangel** `m1`–`m6` | Wortlautkarte § 633 Abs. 2 S. 1, 2 (Auszug, 4 Marker), ✓ Sachmangel, ✓ Zeitpunkt Abnahme (VII ZR 301/13 Rn. 32), gelber Block | tabler:`home`, `droplet` (Blau), `checklist` | `2. Mangel, § 633 Abs. 2 BGB` → `› das undichte Dach` → `› Zeitpunkt der Abnahme` | – |
| **E1 3. Rechte** `r1`–`r5` | Wortlautkarte § 634 vollständig, Marker zu den vier Rechten | tabler:`list-numbers`, `tools` | `3. Rechte aus § 634 BGB` | – |
| **E2 Nacherfüllung** `nach`–`kauf1` | ✓ Vorrang § 635; Zweispalter Kauf (hellblau) / Werkvertrag (hellgelb): erst „der Unternehmer“ (Sprechreihenfolge), dann „der Käufer“; VII ARZ 1/20 Rn. 27 | tabler:`tools`, `shopping-cart` | `3. › Nacherfüllung, § 635 BGB` → `› anders beim Kauf, § 439 Abs. 1 BGB` | – |
| **F Selbstvornahme** `s1`–`s6` | Wortlautkarte § 637 Abs. 1 (5 Marker, vorgelesen), Entbehrlichkeit § 637 Abs. 2/§ 323 Abs. 2 Nr. 1, VIII ZR 215/10 Rn. 24, ✗ „nicht ans Telefon gehen“, gelber Block „Frist setzen, am besten schriftlich“ | tabler:`tools`, `hourglass`, `phone-x`, `writing-sign` | `3. › Selbstvornahme, § 637 Abs. 1 BGB` → `› Frist entbehrlich?` → `› Beate setzt eine Frist` | – |
| **G Vorschuss** `v1`–`kauf2` | Wortlautkarte § 637 Abs. 3, ✓ keine Vorfinanzierung (VII ARZ 1/20 Rn. 67), ✓ verwenden, ✓ abrechnen (VII ZR 92/20 Rn. 28), hellblaue Karte ✗ „Kauf: keine Selbstvornahme, kein Vorschuss dafür“ | tabler:`cash-banknote` (Grün), `file-invoice`, `shopping-cart` | `3. › Selbstvornahme › Vorschuss, § 637 Abs. 3 BGB` → `› Vorschuss › anders beim Kauf` | – |
| **H Rücktritt, Minderung, Schadensersatz** `rm1`–`se1` | ✓ erfolglose Frist, ✗ kein Rücktritt bei unerheblichem Mangel, ✓ Minderung trotzdem, ✓ Schadensersatz mit vermutetem Vertretenmüssen; Fundstellenzeilen | tabler:`arrow-back-up`, `coins` | `3. › Rücktritt und Minderung, §§ 636, 323, 638 BGB` → `3. › Schadensersatz, §§ 636, 280, 281 BGB` | – |
| **I 4. Verjährung** `vj1`–`vj5` | Wortlautkarte § 634a Abs. 1 Nr. 1, 2, Abs. 2 (Auszug, 3 Marker), Bauwerk-Maßstab (VII ZR 348/13 Rn. 19), ✓ 5 Jahre, ✓ Beginn Abnahme | tabler:`hourglass`, `building`, `calendar-time` | `4. Verjährung, § 634a BGB` → `› Bauwerk` → `› Beginn mit der Abnahme` | – |
| **J 5. Unterschiede zum Kauf** `u1`–`u5` | Tabelle Merkmal / Kauf, § 437 / Werkvertrag, § 634; vier Zeilen nacheinander, Zellen zum Wort (Wahlrecht, Selbstvornahme und Vorschuss dafür, maßgeblicher Zeitpunkt, Verjährungsbeginn) | tabler:`arrows-exchange`, `tools`, `calendar-time` | `5. Unterschiede zum Kauf` | – |
| **K Ergebnis** `erg`–`erg4` | ✓ Frist (schriftlich, etwa 2 Wochen), ✓ anderer Dachdecker § 637 Abs. 1, grüner Block „Vorschuss … 2.400 €“, ✓ nichts verjährt | tabler:`writing-sign`, `tools`, `cash-banknote` | `Ergebnis` | – |
| **L Klausurtipp** `tipp`, `tipp2` | hellgelbe Tafel, Lexi warnt; ✗ Kosten nach § 637 nicht ersetzt; ✓ Frist? ✓ entbehrlich? | Warnsymbol (Streamline Freehand), tabler:`hourglass` | `Klausurtipp · Erst die Frist prüfen` | – |
| **M Klausurschema** `sch`–`k7` | breite Karte „Schema: Aufwendungsersatz und Vorschuss, §§ 634 Nr. 2, 637 BGB“, I.–VII. Zeile für Zeile | – | `Schema: §§ 634 Nr. 2, 637 BGB` → `Schema › I. …` bis `Schema › VII. keine Verjährung` | – |
| **N Merksatz** `merke`–`mk3` | Lexi erklärt, drei Zeilen mit Markern (wählt der Unternehmer, Frist, Vorschuss) | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; keine Bewegung, kein Zoom.
**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), wortgleich mit dem Gesprochenen. Zahlen auf Tafeln, Pillen und Karte als Ziffern.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Beate lässt das Dach ihres Hauses vom Dachdecker Herrn Wenzel für 18.000 Euro neu eindecken. Nach drei Wochen ist er fertig. Beate sieht sich alles genau an, nimmt das Dach ab und zahlt die Rechnung.
>
> Zwei Monate später regnet es stark. Im Dachgeschoss zeigen sich Wasserflecken an der Decke. Ein anderer Dachdecker stellt fest: Herr Wenzel hat den Anschluss am Schornstein undicht ausgeführt. Die Reparatur kostet laut seinem Angebot 2.400 Euro.
>
> Beate ruft Herrn Wenzel an und bittet um Rückruf. Auch auf drei weitere Anrufe kommt keine Antwort.
>
> **Was kann Beate verlangen? Was ist anders als beim Kauf?**
