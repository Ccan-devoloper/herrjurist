# Folge 119 · Abgrenzung Täter Teilnehmer: Tatherrschaft vs. subjektive Theorie – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_119.py`](src/skript_119.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen, Format „Streitstand“. Fall: die beiden Klassiker als Akten (Badewannen-Fall, RGSt 74, 84; Staschinski-Fall, BGHSt 18, 87), gelesen von zwei Referendaren in der Bibliothek → Frage → Sachverhalt → 1. Problem (Wortlautkarten § 25 Abs. 1 und § 27 Abs. 1; § 26; Strafrahmen § 27 Abs. 2 Satz 2, § 49 Abs. 1) → 2. subjektive Theorie des Reichsgerichts (animus auctoris/socii, Badewannen-Fall), BGH 1956 (BGHSt 8, 393) und Staschinski 1962 → 3. Kritik und Wende (§ 25 Abs. 1 Alt. 1 seit 1975, BGH 3 StR 35/92) → 4. Tatherrschaftslehre (Zentralgestalt; Handlungs-, Willens-, funktionale Tatherrschaft) → 5. Streitstand als **progressiver Zweispalter** (Rechtsprechung: RG → wertende Gesamtbetrachtung des BGH; Lehre: Tatherrschaft; Verweis Folge 104) → 6. Streitentscheid und Dahinstehen → Ergebnis nach heutigem Recht → Klausurtipp (Lexi) → Klausurschema → Merksatz (Lexi). Vorlagen: 104 (Mittäterschaft; Kioskfall nicht wiederholt, nur verwiesen), 091/094 (mittelbare Täterschaft, nur verwiesen: Katzenkönig), 015 (Namens- und Sichtprüfung).

## Darstellung sensibel (Auftrag)

- **Badewannen-Fall:** kein Kind, kein Säugling, keine Badewanne, keine Tathandlung im Bild – nur die Akte (Kartonkarte mit Reiter), das Gerichtsgebäude (Fluent `classical-building`), die Jahreszahl „1940“, die Fundstelle „RGSt 74, 84“ und sachliche Textzeilen. Die Tathandlung wird nur in einem Satz und ohne Methode genannt („tötet die Schwester das Neugeborene“); das Wort „Badewanne“ fällt nur als Fallname.
- **Staschinski-Fall:** keine Waffe, kein Gift im Bild oder im Sprechtext; nur Akte, Stadtsilhouette (Fluent `cityscape`) mit „München“, die Jahreszahl „1962“, „BGHSt 18, 87“. Keine Namen der Opfer und Auftraggeber.
- **Keine Beteiligten der echten Fälle als Figuren** (FOLGE-ABLAUF Abschnitt 1). Figuren sind nur die beiden fiktiven Referendare und Lexi. Ruhiger, sachlicher Ton; die Referendare zu Beginn mit ernster Mimik (`Solemn`, `Serious`), nicht lächelnd.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Luise (LU), um 28 | Referendarin, liest die Akten, fragt nach dem Badewannen-Fall | `standing/easing-2` (offenes Hemd Grün `#8FD694` über schwarzem Shirt, Hose Gelb `#F9D56E`), Kopf `Long Bangs`, Haut `#E3A982`. Mimiken `Solemn`, `Serious` (auch redet), `Calm`, `Smile`, `Suspicious` | `sabrina` (Frau, mittel) |
| Oskar (OS), um 32 | Referendar, fragt nach dem Staschinski-Fall | `standing/blazer-3` (Blazer Blau `#8DB3F2` über schwarzem Shirt, Hose Grau `#5B5F66`), Kopf `Short 1`, Haut `#F2D3B8`. Mimiken wie Luise | `marc` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Je Person eine Pose, Outfit im ganzen Video gleich; Namensschilder Luise Grün, Oskar Blau ab 0,0 s und durchgehend. In den Tafelfolien stehen beide immer rechts (Luise x 1440, Oskar x 1740) und blicken zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `LU_redet`, `OS_redet` und Lexi. `Awe` (`*_staunt`) erzeugt, aber nicht verwendet (wirkt wie eine Brille). `pointing_finger-1` für Oskar verworfen (Oberteil nicht einfärbbar, Figur ganz schwarz). Keine Bärte, keine Prothesen-Posen, keine Brillen.
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und per `grep -rlw` in keinem Skript, Szenenplan, Abnahmebogen oder Themenplan unter `youtube/` (03.10.2026): Luise, Oskar. Sie werden im Sprechtext nie genannt (nur Namensschilder). Gesprochen wird als Name nur der Fallname „Staschinski“ (3 Nennungen).
- **Stimmen** nur aus dem zugeteilten Pool (sabrina, marc; william und laura_ruhig nicht nötig). Vorfolge 104 (helmut, niklas, julia): keine Überschneidung.

**Abweichung von den letzten Folgen (116 Rücktritt § 323, 117 Klausurfehler, 118 Stadthalle; 104 Kiosk):** neuer Schauplatz Bibliothek mit Aktendeckeln (Karton mit Reiter, Bücherstapel); Posen `easing-2` und `blazer-3` in 116–118 und 104 nicht verwendet (dort `easing-1`, `robot_dance-2/-3`, `shirt-4`, `pointing_finger-2`, `resting-1`, `crossed_arms-2`, `blazer-4`, `walking-1`); kein Polka-Dots-Muster.
**Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A Bibliothek** `fall`→`frage2` | Akte „Reichsgericht · 1940“ ab 0,0 s, Zeilen zum Wort (verheimlicht, Geburt heimlich mit Hilfe der Schwester, auf Drängen der Mutter, Schwester tötet das Neugeborene), Block „Reichsgericht: nur Gehilfin“, „Täterin: die Mutter“; Blase Luise; ab `bw` kompakte Akte „Badewannen-Fall“, zweite Akte „Bundesgerichtshof · 1962“ (Agent, 2 ukrainische Exilpolitiker, im Auftrag, „BGH: nur Beihilfe zum Mord“, „Staschinski-Fall · BGHSt 18, 87“); Blase Oskar; Frage-Pillen | fluent:`classical-building`, `cityscape`, `books` | `Fall · Badewannen-Fall, Reichsgericht 1940` (ab 0,0 s) → `… Warum nur Gehilfin?` → `… Staschinski-Fall, Bundesgerichtshof 1962` → `… Wer selbst tötet …` → `… Die Frage` | – |
| **B Sachverhalt** `sv` | Karte mit beiden Fällen, ≈ 9,6 s | – | `Sachverhalt` | – |
| **C Problem** `prob`→`p26` | Wortlautkarten § 25 Abs. 1 (Marker Täter/selbst/durch einen anderen) und § 27 Abs. 1 (Marker Gehilfe/Hilfe geleistet), Block § 26 | fluent:`balance-scale` | `1. Problem: Täter oder Teilnehmer? › Täter, § 25 Abs. 1 StGB` → `… › Gehilfe, § 27 Abs. 1 StGB` → `… › Anstifter, § 26 StGB` | – |
| **D Strafrahmen** `straf`→`mord` | Anstifter gleich Täter; Gehilfe zwingend gemildert; Mord: statt lebenslang nicht unter 3 Jahren | fluent:`balance-scale` | `… › Strafrahmen` | – |
| **E Reichsgericht** `rg1`→`rgbw` | innerer Wille; Karten animus auctoris / animus socii; Badewannen-Fall: „also nur Gehilfin“ | fluent:`brain`, `classical-building` | `2. Subjektive Theorie des Reichsgerichts › …` | – |
| **F BGH 1956 / 1962** `bgh56`→`st3` | Zitatkarte BGHSt 8, 393 mit Markern; Staschinski: Wille, widerwillig, kein Interesse (Kreuz), Auftraggeber beherrschten Ob und Wie (Haken) | fluent:`classical-building`, `cityscape` | `… › BGH 1956: BGHSt 8, 393` → `… › Staschinski-Fall, BGHSt 18, 87` | – |
| **G Kritik und Wende** `krit`→`stets` | zwei Kreuze (kaum greifbar, löst sich vom Tatbestand), Wortlaut § 25 Abs. 1 Alt. 1 (Marker „selbst“), BGH 3 StR 35/92, „Lehre: stets Täter“ | fluent:`spiral-calendar`, `classical-building` | `3. Kritik und Wende › …` | – |
| **H Tatherrschaftslehre** `thl`→`fh` | Zentralgestalt/Randfigur, drei Formen als Blöcke | fluent:`bullseye`, `puzzle-piece` | `4. Tatherrschaftslehre (h. L.) › …` | – |
| **I Streitstand (Zweispalter)** `zw`→`v104` | links Rechtsprechung (RG: Täterwille; BGH heute: wertende Gesamtbetrachtung, drei Kriterien, Tatherrschaft nur ein Kriterium), rechts Lehre (Tatherrschaft, Zentralgestalt), Verweis Folge 104 | fluent:`balance-scale`, `bullseye` | `5. Streitstand › Rechtsprechung` → `… › Lehre` → `… › Mittäter: Folge 104` | – |
| **J Streitentscheid** `ents`→`dahin2` | Tatherrschaftslehre; Haken (Begehen), Kreuz (keine Rangfolge); Klausur: gleich → dahinstehen, verschieden → entscheiden | fluent:`balance-scale`, `memo` | `6. Streitentscheid › …` | – |
| **K Ergebnis** `erg`→`erg3` | Badewannen-Fall: Täterin (§ 25 Abs. 1 Alt. 1); Staschinski: Täter (Lehre ohnehin, BGH wohl ebenso); Auftraggeber: Täter hinter dem Täter? (Katzenkönig) | fluent:`classical-building`, `cityscape` | `Ergebnis nach heutigem Recht` → `Ergebnis · …` | – |
| **L Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | – |
| **M Klausurschema** `sch`→`s_iv` | breite Karte, progressiv I.–IV. | – | `Klausurschema › …` | – |
| **N Merksatz** `merke`→`m_3` | Lexi erklärt, Marker | – | `Merksatz` | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops. Keine Bewegung, **kein Geräusch**: Die Folge zeigt keine Handlung, die ein Handlungsgeräusch tragen könnte (Akten, Tafeln); „lieber kein Geräusch als ein unpassendes“ (`geraeusche_herkunft.json`).
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 25 Abs. 1 und § 27 Abs. 1 vollständig, § 25 Abs. 1 Alt. 1 mit Auslassung „…“, wörtlich nach gesetze-im-internet.de mit Normangabe, vorgelesen; Marker synchron. Zitatkarte BGHSt 8, 393 wörtlich nach Hefendehl KK 683, vorgelesen.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Badewannen-Fall (Reichsgericht 1940, RGSt 74, 84): Eine junge Frau verheimlicht aus Angst vor ihrem Vater ihre Schwangerschaft und bringt das Kind mit Hilfe ihrer Schwester heimlich zur Welt. Auf Drängen der Mutter tötet die Schwester das Neugeborene unmittelbar nach der Geburt. Das Reichsgericht sieht in ihr nur eine Gehilfin; Täterin sei die Mutter, die die Tat als eigene gewollt habe.
>
> Staschinski-Fall (Bundesgerichtshof 1962, BGHSt 18, 87): Ein Agent des sowjetischen Geheimdienstes tötet in München zwei ukrainische Exilpolitiker, im Auftrag seiner Vorgesetzten. Der Bundesgerichtshof verurteilt ihn nur wegen Beihilfe zum Mord.
>
> **Wann ist jemand Täter, wann nur Anstifter oder Gehilfe?**
