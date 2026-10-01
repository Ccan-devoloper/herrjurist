# Folge 016 · Volkszählungsurteil: Die Geburtsstunde des Datenschutzes (Art. 2 I GG) – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_016.py`](src/skript_016.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker-Fall). Der echte Fall wird sachlich nacherzählt (Volkszählungsgesetz 1983, zahlreiche Verfassungsbeschwerden, Urteil vom 15.12.1983 – 1 BvR 209/83 u. a., BVerfGE 65, 1). Der Kern wird an fiktiven Figuren gezeigt: Frau Hartmann soll den Fragebogen ausfüllen, der ehrenamtliche Zähler Herr Lehmann (Behördenfigur) bringt ihn, Nachbar Herr Sommer fürchtet um seine Bürgerinitiative. Ablauf: Fall → Frage → Sachverhalt → A. Zulässigkeit (ausnahmsweise direkt gegen das Gesetz) → B. I. Schutzbereich (informationelle Selbstbestimmung, kein belangloses Datum, wer was wann weiß) → II. Eingriff → III. Rechtfertigung (Allgemeininteresse, gesetzliche Grundlage/Normenklarheit, Verhältnismäßigkeit, Schutzvorkehrungen, Zweckbindung/Abschottung) → Erhebungsprogramm (zulässig, Umschlag, Nachbesserung) → Melderegisterabgleich § 9 I (verfassungswidrig) → Übermittlung § 9 II–IV → Ergebnis → Rechtslage heute (DSGVO, GRCh) → Klausurtipp → Schema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Hartmann (HA), um 65 | soll den Fragebogen ausfüllen; fragt, wer ihre Angaben sieht | Pose `standing/polka_dots` (gepunktete Bluse), Kopf `Gray Medium` (Haar grau `#C9C9CF`), Brille `Glasses 3`; Hose Lila `#B8A9F5`, Haut `#EBC4A0`; Mimiken `Calm`, `Serious` (liest), `Concerned|Serious` (redet/Sorge), `Suspicious` (denkt), `Smile` (froh), `Fear` (Schreck) | `lisa` (Frau, älter) |
| Herr Lehmann (LE), um 25 | ehrenamtlicher Zähler (§ 6 VZG 1983), Behördenfigur | Pose `standing/shirt-4` (schwarzes Hemd), Kopf `Short 2`; Hose Blau `#8DB3F2`, Haut `#C58E64`; Mimiken `Calm`, `Serious` (redet), `Smile`; Klemmbrett tabler:`clipboard-list` | `niklas` (Mann, jung) |
| Herr Sommer (SO), um 70 | Nachbar, aktiv in einer Bürgerinitiative | Pose `standing/pointing_finger-1`, Kopf `No Hair 3`, Brille `Glasses 4`; Oberteil Grün `#8FD694`, Haut `#F0C8A8`; Mimiken `Calm`, `Concerned|Serious` (redet), `Fear` (Sorge), `Serious` (denkt) | `william` (Mann, älter) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Keine realen Personen:** Beschwerdeführer, Richter und Politiker treten nicht auf; das Gericht erscheint nur als Gebäude-Icon, die Beschwerden nur als Dokument-Icons.
- Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt (blickt nach links zur Tafel bzw. zum Gegenüber), `_r` blickt nach rechts (Lehmann zu Frau Hartmann, Frau Hartmann zu Herrn Sommer).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `HA_redet`, `LE_redet`, `SO_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Stimmen nur aus dem Pool** lisa, niklas, william (hilde nicht benötigt); keine Überschneidung mit 015 (helmut, stephan, elinor) und 013 (helmut, lucy, stephan).
- **Namen mit eindeutig deutscher Aussprache:** Hartmann, Lehmann, Sommer (alle nur von der Erzählerin gesprochen).
- Figuren-PNGs: `../peeps/op_016/` (56 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 013: Luftraum, Lagezentrum, Flughafen; 014: Vertragsschluss; 015: Kleingarten.
- Hier: Wohnzimmer 1983 mit Fragebogen, Haustür mit Klingel, Datenfluss-Skizze, Nachbarhaus mit Bürgerinitiative, Briefkasten; erstmals Persönlichkeitsrecht/Datenschutz.
- Drei neue Figuren, drei neue Posen gegenüber 013/015 (`polka_dots`, `shirt-4`, `pointing_finger-1`).

## Szenen

Alle Szenen auf Cremegrund (Tageslicht).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Der Fragebogen** `fall`→`fragen` | Wohnzimmer: Tisch mit Lampe, Frau Hartmann rechts, Fragebogen-Karte links | tabler:`table` (Orange), `lamp` (Gelb), `briefcase`, `building`, `bus`, `home`, `coins`, `building-church`; Pillen „Frühjahr 1983“, „Volkszählung 1983“ | `Fall · Der Fragebogen` (ab 0,0 s) | Grundbild · Frühjahr · Volkszählung · Bogen · sechs Fragezeilen zum Wort | – |
| **B Der Zähler** `zaehler`→`h1` | Haustür; Lehmann (links, blickt nach rechts) mit Klemmbrett, Frau Hartmann rechts | tabler:`door` (Orange), `bell` (Gelb), `clipboard-list`, `coins`; Pillen „ehrenamtlicher Zähler“, „Bußgeld“ | `Fall · Der Zähler` | Tür+Klingel+Lehmann · Namen · Lehmann redet (Blase) · Bußgeld · Frau Hartmann redet (Blase) | Türklingel `szene_016klingel_1` |
| **C Was mit den Daten geschieht** `melde`→`weiter` | Datenfluss: Fragebogen → Melderegister, Behörden, Gemeinden | tabler:`forms`, `address-book` (Gelb), `building-bank` (Grau), `building-community` (Grün), Pfeile | `Fall · Was mit den Daten geschieht` | Bogen · Melderegister · vergleichen · berichtigen · Einzelangaben · Behörden · Gemeinden | – |
| **D Der Nachbar** `sommer`→`s1` | Nachbarhaus, Bürgerinitiative; Frau Hartmann hört zu, Herr Sommer redet | tabler:`building-cottage`, `users-group` (Orange), `database`, `link`, Kreuz | `Fall · Der Nachbar` | Haus · Sommer · Bürgerinitiative · Blase · speichern · verknüpfen · Kreuz „lieber nicht mehr hin“ | – |
| **E Die Frage** `frage` | Dokumente (Verfassungsbeschwerden) → Gesetz | tabler:`file-text`, `file-certificate` (Blau) | `Fall · Die Frage` | Dokumente · Pille · Gesetz · zwei Fragen | – |
| **F Sachverhalt** `sv` | Sachverhaltskarte vollständig (≈ 10 s) | – | `Sachverhalt` | 1 | – |
| **G Zulässigkeit** `zul`/`eile` | Tafel, Frau Hartmann | `calendar`, `hourglass` | `A. Zulässigkeit › Verfassungsbeschwerde direkt gegen das Gesetz` | ≈ 7 | – |
| **H Schutzbereich** `sb`→`ris2` | Tafel, Frau Hartmann | `user-shield`, `forms` | `B. Begründetheit › I. Schutzbereich: Art. 2 I i. V. m. Art. 1 I GG` → `… informationelle Selbstbestimmung` | ≈ 9 | – |
| **I Kein belangloses Datum** `edv`→`wofuer` | Tafel, Frau Hartmann | `device-desktop`, `database`, `clock`, `puzzle`, `file-text`, `link` | `… › automatische Datenverarbeitung` → `… › kein belangloses Datum` | ≈ 9 | – |
| **J Wer was wann weiß** `wer`→`gemein` | Tafel, Herr Sommer | `users-group`, `eye` | `… › wer was wann weiß` | ≈ 7 | – |
| **K Eingriff, Rechtfertigung** `ein`→`vork` | Tafel, Frau Hartmann | `coins`, `users`, `book`, `scale`, `shield-lock` | `B. Begründetheit › II. Eingriff: Auskunftspflicht` → `B. › III. Rechtfertigung › …` (Allgemeininteresse, gesetzliche Grundlage/Normenklarheit, Verhältnismäßigkeit, Schutzvorkehrungen) | ≈ 10 | – |
| **L Zweckbindung** `zweck`→`abschott` | Tafel, Frau Hartmann | `building-bank`, `chart-bar`, `lock`, `eye-off` | `… › Zweckbindung` → `… bei der Statistik` → `… › Abschottung der Statistik` | ≈ 7 | – |
| **M Erhebungsprogramm** `fragenok`/`stich` | Tafel, Frau Hartmann | `forms`, `chart-pie`, `id` | `B. › III. Erhebungsprogramm, §§ 2–5 VZG 1983` | ≈ 7 | – |
| **N Umschlag, Nachbesserung** `umschlag`→`nach3` | Tafel; Frau Hartmann steckt den Umschlag in den Briefkasten (Bewegung) | `mailbox`, `mail` (bewegt), `info-circle`, `trash`, `home` + Kreuz | `… › verschlossener Umschlag` → `B. › III. Erhebung › Schutzvorkehrungen` | ≈ 9 | Umschlag `szene_016umschlag_1` |
| **O Melderegisterabgleich** `abgl`→`nachteil` | Tafel, Frau Hartmann | `chart-bar` → `address-book`, `arrows-shuffle`, `question-mark` | `B. › III. Melderegisterabgleich, § 9 I VZG 1983` | ≈ 8 | – |
| **P Übermittlung, Ergebnis** `uebermit`→`nichtig` | Tafel, Frau Hartmann | `building-bank`, `building-community` + Kreuz, `microscope` + Haken, fluent-hc:`classical-building`, `gavel` | `B. › III. Übermittlung, § 9 II–IV VZG 1983` → `Ergebnis · Urteil vom 15.12.1983` | ≈ 9 | – |
| **Q Rechtslage heute** `heute`/`charta` | Tafel, Frau Hartmann | `flag` (Blau), classical-building | `Rechtslage heute · DSGVO und Grundrechtecharta` | ≈ 6 | – |
| **R Klausurtipp** `tipp`→`tipp2` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Verwendung und Verknüpfung prüfen` | 5 | – |
| **S Klausurschema** `sch`→`k8` | Schema baut sich auf | – | `Klausurschema` | 9 | – |
| **T Merksatz** `merke`/`m2` | Lexi erklärt, Merksatz mit Marker | – | `Merksatz` | 5 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 20 Folien; innerhalb harte Schnitte und Pops; eine Bewegung (Umschlag wandert aus Frau Hartmanns Hand zum Briefkasten).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_016klingel_1`, `szene_016umschlag_1`), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene F, erscheint vollständig)

> Frühjahr 1983: Nach dem Volkszählungsgesetz 1983 sollen alle Auskunftspflichtigen einen Fragebogen ausfüllen, unter anderem zu Beruf, Arbeitsstätte, Weg zur Arbeit, Wohnung, Miete und Religion. Wer nicht antwortet, dem droht ein Bußgeld. Frau Hartmann fragt den ehrenamtlichen Zähler Herrn Lehmann, wer ihre Angaben zu sehen bekommt. Das Gesetz erlaubt, die Angaben mit dem Melderegister zu vergleichen und es zu berichtigen (§ 9 Abs. 1 VZG 1983); Einzelangaben dürfen an Behörden und Gemeinden gehen (§ 9 Abs. 2, 3). Ihr Nachbar Herr Sommer, aktiv in einer Bürgerinitiative, fürchtet, dass seine Daten gespeichert und verknüpft werden. Viele Bürger erheben Verfassungsbeschwerde unmittelbar gegen das Gesetz.
>
> *(Nach BVerfGE 65, 1 – 1 BvR 209/83 u. a.; Frau Hartmann, Herr Lehmann und Herr Sommer sind erfunden.)*
>
> **Sind die Verfassungsbeschwerden zulässig und begründet?**

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen. Tafeln schreiben Jahreszahlen und Normen in Ziffern („1983“, „§ 9 I–III“), gesprochen als Wörter. Kleine graue Fundstellenzeilen (z. B. „BVerfGE 65, 1 (43) · Rn. 154“) sind Belege, kein Sprechtext.
