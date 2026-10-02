# Folge 049 · Rücknahme § 48 VwVfG: Muss das Café die Förderung zurückzahlen? – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_049.py`](src/skript_049.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker-Fall, Übungsfall nach dem Hook des Themenplans). Frau Hofmann erhält für ihr Café 20.000 Euro Förderung des Landes; die Förderstelle hat sich verrechnet, ihre Angaben waren richtig, das Geld ist für Miete, Löhne und Lieferanten ausgegeben. Zwei Jahre später entdeckt Prüferin Ebert den Fehler, Herr Wagner hört Frau Hofmann an und nimmt den Bescheid zurück. Ablauf: Fall → Frage → Sachverhalt → A. Rechtsgrundlage (§ 48 statt § 49, Landesrecht) → B. formell (Zuständigkeit, Anhörung § 28) → C. 1. Wortlaut § 48 I 1 (rechtswidrig) → 2. Wortlaut § 48 I 2 (begünstigend) → 3. Wortlaut § 48 II 1–2 (Vertrauen, Verbrauch) → Wortlaut § 48 II 3 (Ausschluss Nr. 1–3) → Abwägung und Ergebnis → Gegenfall (falsche Angaben, Nr. 2, Rücknahme für die Vergangenheit) → 4. Wortlaut § 48 IV 1 (Jahresfrist, BVerwG) → 5. Ermessen (kein intendiertes Ermessen) → Wortlaut § 49a I, Zinsen § 49a III → Ausblick EU-Beihilfen → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:34,6 (5.647 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Hofmann (HO), um 32 | betreibt ein kleines Café in der Altstadt | Pose `standing/robot_dance-3` (rotes Oberteil `#F07A6A`, gelbe Hose), Kopf `Long`, Haut `#F2C9A9`; Mimiken `Smile` (ruhig), `Smile Big|Smile` (froh, redet froh), `Concerned|Serious` (Sorge, redet), `Suspicious` (denkt), `Driven` (entschlossen), `Cute` (zufrieden) | `ela_warm` (Frau, jung) |
| Herr Wagner (WA), um 60 | Sachbearbeiter der Förderstelle des Landes | Pose `standing/resting-1` (lila Pullover `#B8A9F5`), Kopf `Gray Short`, Brille `Glasses 2`, Haut `#E6B48F`; Mimiken `Serious` (ruhig/redet), `Solemn` (denkt) | `william` (Mann, älter) |
| Frau Ebert (EB), um 38 | Prüferin der Förderstelle | Pose `standing/crossed_arms-1` (grünes Oberteil `#8FD694`, verschränkte Arme), Kopf `Medium Bangs 3`, Haut `#C68C66`; Mimiken `Serious` (ruhig/redet), `Suspicious` (denkt) | `julia` (Frau, jung) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szenen A und C: Frau Hofmann blickt nach rechts zu Antrag, Bescheid und Ausgaben; Szene B: Ebert blickt nach rechts zu Wagner, Wagner nach links zu ihr; Frage und Tafeln: alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `HO_redfroh`, `HO_redet`, `WA_redet`, `EB_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Stimmen nur aus dem Pool** ela_warm, niklas, julia, william (niklas nicht gebraucht); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Hofmann, Wagner, Ebert (nicht in der Liste früherer Namen). Genitive vermieden („Bei Frau Hofmann ist der Umsatz …“).
- Figuren-PNGs: `../peeps/op_049/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 044 Marktplatz mit Rathaus, Kaffeewagen, Unwetter; 048/043 Gericht bzw. Geschäftsräume. Hier: Café mit Ladenfront und Theke in der Altstadt, Büro der Förderstelle mit Schreibtisch, Lampe, Rechner und Umschlag. Posen: `robot_dance-3` in 040–048 nicht verwendet; `resting-1` zuletzt 046, `crossed_arms-1` zuletzt 041 (jeweils andere Köpfe, Farben, Rollen). Kein Kaffeewagen und kein Marktplatz trotz Café-Bezug (anderer Fall, anderer Ort).

## Szenen

Alle Szenen auf Cremegrund (Tageslicht).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Café** `fall`–`verbraucht` | Ladenfront, Theke; Umsatz eingebrochen, Antrag, Förderbescheid, Blase Hofmann, Ausgaben | ph:`storefront`, Theke (Karte), tabler:`coffee`, fluent-hc:`croissant`, tabler:`sun`, `file-text`, `file-euro`, `home`, `users`, `truck` | `Fall · Das Café und die Förderung` (ab 0,0 s) | Café · Umsatz · Sorge · Antrag · Zahlen richtig · Bescheid · 20.000 € · froh · Blase · Miete · Löhne · Lieferanten · ausgegeben | Papier (`szene_049brief_1`) beim Bescheid |
| **B Förderstelle** `amt`–`anh` | Büro mit Schreibtisch; Ebert prüft die Akte, Blase Ebert, Blase Wagner, Anhörung | fluent-hc:`office-building`, ph:`desk`, tabler:`lamp`, `file-search`, `calculator`, ph:`envelope` | `Fall · Zwei Jahre später: die Förderstelle` → `Fall · Die Anhörung` | Büro · Ebert · Akte · Rechner · 15 % · 30 % · Blasen · Anhörung · Umschlag · Stellungnahme | Umschlag (`szene_049umschlag_1`) |
| **C Café** `rueck`/`ho2` | zurück im Café (gleiche Ansicht wie A, erkennbar derselbe Ort), Rücknahmebescheid, Blase Hofmann | wie A, tabler:`file-euro` (rot) | `Fall · Die Rücknahme` | Bescheid · Rücknahme · 20.000 € mit Zinsen · Blase | Papier (`szene_049brief_1`) |
| **D Frage** `frage`/`frage2` | Café, Förderung, zwei Normen | ph:`storefront`, tabler:`file-euro` | `Fall · Muss das Café zurückzahlen?` | Frage · § 48 · § 49a | – |
| **E Sachverhalt** `sv` | Karte vollständig, Bearbeitervermerk, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **F A. Rechtsgrundlage** `rgl`–`land` | Tafel; Hofmann | tabler:`file-euro`, fluent-hc:`classical-building` | `Rücknahme › A. Rechtsgrundlage` → `› Abgrenzung: Widerruf, § 49` → `› Landesrecht` | Zeilen zum Wort, ✓ § 48 | – |
| **G B. formell** `formell`/`anh2` | Tafel; Wagner | fluent-hc:`office-building`, ph:`envelope` | `Rücknahme › B. formell: Zuständigkeit` → `› Anhörung, § 28 I VwVfG` | ✓ Zuständigkeit · § 28 · ✓ geschehen | – |
| **H Wortlaut § 48 I 1** `wl481`–`unanf` | Wortlautkarte vorgelesen, drei Marker; Hofmann | `file-euro`, `calculator` | `Rücknahme › C. materiell › 1. rechtswidriger Verwaltungsakt` | Karte · Marker · ✓ rechtswidrig · unanfechtbar | – |
| **I Wortlaut § 48 I 2** `beg`/`beg2` | Wortlautkarte, Marker; Hofmann | tabler:`cash-banknote` | `› 2. begünstigender Verwaltungsakt, § 48 I 2` | Karte · Marker · ✓ begünstigt | – |
| **J Wortlaut § 48 II 1–2** `wl482`–`v4` | Wortlautkarte (Zitat), sechs Marker zum Wort; Hofmann | `cash-banknote` | `› 3. Vertrauensschutz, § 48 II` | Marker · ✓ vertraut · verbraucht | – |
| **K Wortlaut § 48 II 3** `aus`–`aus3` | Wortlautkarte mit Nummern, Marker; drei ✗ | `file-euro` | `› 3. Vertrauensschutz › Ausschluss, § 48 II 3` | Marker · ✗ Nr. 1 · ✗ Nr. 2 · ✗ Nr. 3 | – |
| **L Abwägung und Ergebnis** `abw`–`erg2` | Tafel; Hofmann froh | ph:`scales`, tabler:`shield-check` | `› Abwägung` → `Ergebnis` | Interesse · ✓ Regelfall · Ergebnis · Anfechtung | – |
| **M Gegenfall** `gegen`–`verg` | Tafel (zartrot); Hofmann | `calculator` | `Gegenfall › falsche Angaben, § 48 II 3 Nr. 2` → `› Rücknahme für die Vergangenheit, § 48 II 4` | zu hoch · ✓ Nr. 2 · kein Vertrauensschutz · Vergangenheit | – |
| **N Wortlaut § 48 IV 1** `wl484`–`frist4` | Wortlautkarte vorgelesen; Wagner | tabler:`calendar` | `Gegenfall › C. materiell › 4. Jahresfrist, § 48 IV` | Marker · ✗ zwei Jahre · Beginn · Anhörung · ✓ gewahrt | – |
| **O Ermessen** `erm`–`erm3` | Tafel; Wagner | ph:`scales` | `Gegenfall › C. materiell › 5. Ermessen, § 48 I 1` | kann · ✗ intendiert · ✗ Sparsamkeit · Sphäre | – |
| **P Wortlaut § 49a I** `wl49a`–`zins` | Wortlautkarte (Zitat), Marker; Zinszeilen; Hofmann | `file-euro`, tabler:`percentage` | `Gegenfall › Erstattung, § 49a I` → `› Zinsen, § 49a III` | Marker · schriftlich · Zinsen | – |
| **Q Ausblick EU** `eu`/`eu2` | Tafel; Ebert | tabler:`stars` | `Ausblick · EU-Beihilfen` | Rückforderung · überlagert · Jahresfrist | – |
| **R Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Rücknahme prüfen` | drei Hinweise | – |
| **S Klausurschema** `sch`–`q8` | Schema baut sich auf | – | `Klausurschema` | Titel · Oberbegriff · A · B · C · 1–5 · Danach | – |
| **T Merksatz** `merke`/`m2` | Lexi erklärt, Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 20 Folien; innerhalb harte Schnitte und Pops.
**Geräusche:** zwei Handlungsgeräusche (Papier beim Erscheinen der beiden Bescheide, Umschlag auf dem Schreibtisch bei der Anhörung), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Theke:** als Baustein (`karte` in Holzfarbe), keine Iconbibliothek enthält eine Theke.

## Sachverhaltskarte (Szene E, erscheint vollständig)

> Frau Hofmann führt ein kleines Café. Sie beantragt Geld aus einem Förderprogramm des Landes, das nur bei einem Umsatzrückgang von mindestens 30 Prozent fördert, und gibt ihre Zahlen richtig an. Die Förderstelle verrechnet sich und bewilligt durch endgültigen Bescheid 20.000 Euro; der Bescheid nennt nur den Betrag. Frau Hofmann bezahlt damit Miete, Löhne und Lieferanten. Zwei Jahre später bemerkt Prüferin Ebert: Der Umsatz ist nur um 15 Prozent gesunken. Herr Wagner hört Frau Hofmann an. Einen Monat nach ihrer Stellungnahme nimmt die Förderstelle den Bescheid zurück und verlangt 20.000 Euro nebst Zinsen.
>
> Bearbeitervermerk: Die Förderstelle ist zuständig. Der Förderbescheid ist unanfechtbar.
>
> **Muss Frau Hofmann die Förderung zurückzahlen?**

Kein Fiktiv-Hinweis auf Karte, Tafeln oder im Sprechtext.

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen. Tafeln schreiben Normen und Zahlen in Ziffern („§ 48 II 3 Nr. 2“, „15 %“), gesprochen als Wörter. Kleine graue Fundstellenzeilen sind Belege, kein Sprechtext. Die Wortlautkarten § 48 I 1 und § 48 IV 1 werden vorgelesen; die Karten § 48 I 2, § 48 II 1–2, § 48 II 3 und § 49a I sind als Zitat gekennzeichnet, ihre Merkmale werden genannt und markiert.
