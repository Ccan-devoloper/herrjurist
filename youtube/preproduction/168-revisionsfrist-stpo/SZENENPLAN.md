# Folge 168 · Revisionsfrist StPO: Einlegung, Begründung, Wiedereinsetzung – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_168.py`](src/skript_168.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · StPO-Praxis, Format Schema. Beispielfall nach dem Plan-Hook („Das Urteil wurde an einem Montag verkündet, zugestellt wird es erst sieben Wochen später“): Die Strafkammer verurteilt Herrn Tiedemann am Montag, 18.5.2026, in seiner Anwesenheit; Rechtsanwältin Sternberg legt am Dienstag nach Pfingsten (26.5.) elektronisch Revision ein; Zustellung am 6.7.; die Kanzlei notiert die Begründungsfrist für den 6.9. statt 6.8.; am 10.8. fällt der Fehler auf, am 12.8. folgt der Wiedereinsetzungsantrag. Ablauf: Fall (Sitzungssaal → Kanzlei) → Sachverhalt → Aufbau (§ 333, Verweis 066) → Einlegung § 341 (Wortlaut) → Form § 32d S. 2 (Wortlaut, seit 1.1.2022, Fax unwirksam) → § 43 (Wortlaut) → Kalender Mai 2026 (Pfingstmontag) → § 345 Abs. 1 (Wortlaut) mit Zeitstrahl → § 345 Abs. 2 (Wortlaut), § 344, § 335 → Telefonat → §§ 44, 45 (Wortlaut) → Verteidigerverschulden und Lösung → die Grenze (Verfahrensrügen) → Merktabelle → Klausurtipp (Lexi) → Prüfschema I.–V. → Merksatz (Lexi).
**Länge:** Hauptfilm 6:53,7 bei 5.877 gesprochenen Zeichen (Grenze 7:00/6.200); Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Tiedemann (TI), um 60 | Angeklagter, Revisionsführer | `standing/crossed_arms-1` (Pullover Sand `#C9B38C`, schwarze Hose, weiße Schuhe), Kopf `Gray Short`, Brille `Glasses 3`, kein Bart, Haut `#EDC3A0`; Mimiken `Calm`, `Serious` (redet), `Concerned\|Serious` (redet2, Sorge), `Fear`, `Suspicious`, `Tired`, `Smile` | `william` (Mann, älter) |
| Rechtsanwältin Sternberg (SB), um 40 | Verteidigerin | `standing/blazer-4` (Sakko Anthrazit `#2B2B35` wie eine Robe, weißes Shirt, schwarze Hose), Kopf `Medium Straight` (schwarz), Haut `#E2B190`; Mimiken `Calm` (redet2), `Serious` (redet), `Smile`, `Suspicious`, `Fear`, `Solemn` | `laura_ruhig` (Frau, mittel) |
| Vorsitzende Richterin (RI), um 55, Funktionsrolle ohne Namen, spricht nicht | verkündet das Urteil | `standing/pointing_finger-1` (ganz in Schwarz wie eine Robe, erhobener Zeigefinger), Kopf `Medium 3`, Brille `Glasses 2`, Haut `#F0CDB4`; Mimiken `Calm`, `Serious` | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, nicht in der Liste vergebener Namen und als Figurenname in keiner bisherigen Folge (Volltextsuche über `youtube/` am 04.10.2026: nur Literaturzitate „LK/Tiedemann“ in 144 und „Sternberg-Lieben“ in 157). Keine Genitivformen.
- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Sitzungssaal: Richterin (`_r`) blickt zu Angeklagtem und Verteidigerin, beide blicken zu ihr; bei seiner Rede wendet sich Herr Tiedemann (`_r`) seiner Verteidigerin zu. Telefonat: Sternberg links (`_r`), Tiedemann rechts (links blickend) – einander zugewandt über die Trennlinie. Tafelfolien: alle blicken zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `TI_redet`, `TI_redet2`, `SB_redet`, `SB_redet2` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool** (william, sabrina, marc, laura_ruhig); gebraucht: william, laura_ruhig – nicht die Stimmen der Vorfolge 167 (marc, sabrina).
- Figuren-PNGs: `../peeps/op_168/` (70 Dateien, nicht im Repository, im Drive-Master). Kontaktbild `out/besetzung_168.png`.
- Keine Prothesen-Posen, keine Bärte, keine Polka Dots, keine Karikatur; der Angeklagte in Alltagskleidung ohne Herkunfts- oder Hautfarben-Klischee; keine realen Personen.

**Abweichung von den letzten Folgen:** 165 (Analogieverbot; `walking-1`, `crossed_arms-2`), 166 (Weinversteigerung; `resting-2`, `pointing_finger-2`, `blazer-3`, `walking-1`), 167 (Urkunde/Kopie; `resting-1`, `blazer-1`). 168: Posen `crossed_arms-1`, `blazer-4`, `pointing_finger-1` in keiner der drei Vorfolgen; Kleidung Sand/Anthrazit/Schwarz neu gegenüber 165–167. Sitzungssaal mit Richterbank, Kanzlei mit Fristenkalender, Telefonat im geteilten Bild (Kanzlei | Zuhause), Kalender Mai 2026 und Zeitstrahl als Fristbilder. 066 (Revision, Kanzlei/Saal) und 126 (Sitzungssaal mit Tür) nur über Verweise; der Saal ist neu gestaltet (Holzvertäfelung, Richterbank, kein Zuschauerraum), weil die Geschichte bei der Urteilsverkündung beginnt.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Sitzungssaal** `fall`→`st1` | Holzvertäfelung, Richterbank; Richterin, Tiedemann, Sternberg ab 0,0 s mit Namensschildern | – (Grundformen `saal()`, `richterbank()`) | `Fall · Im Sitzungssaal` (ab 0,0 s) → `· Das Urteil` → `· anwesend bei der Verkündung` → `· Revision!` | Grundbild · Urteil-Pille · Richterin ernst/Tiedemann erschrocken · „anwesend“ · „Verteidigerin“ · Blase Tiedemann · Blase Sternberg | – |
| **A2 Kanzlei** `zust`→`frage2` | Schreibtisch, Fristenkalender an der Wand, Sternberg | tabler:`mail`, `mail-opened`, `hourglass` | `Fall · Die Zustellung` → `· Der Fristenkalender` → `· Die Fragen` | Brief kommt · Pille „7 Wochen später“ · „Revisionsbegründung“ · „Tiedemann: 6.9.2026“ · rot unterstrichen „1 Monat zu spät“ · zwei Fragen | Umschlag (`szene_168umschlag_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **C Aufbau** `aufbau`→`a4` | Tafel, beide Figuren | tabler:`building-bank`, `send`, `file-text`, `arrow-back-up` | `Aufbau · Statthaftigkeit, § 333 StPO` → `· die Fristen` → `› 1. Einlegung` → `› 2. Begründung` → `› 3. Wiedereinsetzung` | ✓ § 333 · Verweis 066 · drei Blöcke | – |
| **D § 341** `p341`→`abw` | Wortlautkarte (vorgelesen) | tabler:`send`, `building-bank`, `mail` | `Einlegung › § 341 Abs. 1 StPO: eine Woche` → `› beim Landgericht` → `› abwesend: § 341 Abs. 2 StPO` | Karte · 5 Marker · Block Landgericht · Abs. 2 | – |
| **E § 32d** `p32d`→`fax` | Wortlautkarte, Sternberg allein | tabler:`writing-sign`, `device-laptop`, `printer-off` | `Einlegung › Form: schriftlich` → `› Form: § 32d S. 2 StPO` → `› elektronisch seit 1.1.2022` → `› Fax: unwirksam` | Zeile · Karte · Marker müssen/elektronisch/Revision · ✓ seit 2022 + BGH · ✗ Fax + BGH | – |
| **F1 § 43** `frist1`, `p43` | Wortlautkarte (Abs. 1 und 2) | tabler:`calendar-event`, `calendar-week` | `Einlegung › Fristberechnung, § 43 StPO` → `› § 43 Abs. 1: Benennung oder Zahl` | Karte · Marker Wochen/Benennung, Monaten/Zahl · zwei Blöcke | – |
| **F2 Kalender Mai 2026** `mo`→`rz` | Kalender (Grundform), Sternberg | tabler:`calendar-event`, `calendar-off`, `alarm`, `calendar-check` | `Einlegung › Urteil: Mo, 18.5.2026` → `› 1 Woche: Mo, 25.5.2026?` → `› Pfingstmontag` → `› § 43 Abs. 2: nächster Werktag` → `› Ende: Di, 26.5.2026, 24 Uhr` → `› eingelegt am 26.5.2026 (+)` | 18 „Urteil“ · 25 „1 Woche“ · 25 „Feiertag“ · Abs.-2-Zeile · 26 „Ende“ + Block · ✓ | – |
| **G § 345 Abs. 1** `p345`→`sept` | Wortlautkarte (S. 1, 3) + Zeitstrahl 26.5.–6.9. | tabler:`file-text`, `mail-opened`, `alarm`, `calendar-x` | `Begründung › § 345 Abs. 1 StPO: ein Monat` → `› später zugestellt: ab Zustellung` → `› Verlängerung, § 345 Abs. 1 S. 2` → `› Zustellung: Mo, 6.7.2026` → `› Ende: Do, 6.8.2026` → `› notiert: 6.9. – versäumt (-)` | Karte · Marker · S. 2-Zeilen · Zeitstrahl 26.5./6.7. · „1 Monat“ · 6.8. · 6.9. rot · ✗ | – |
| **H § 345 Abs. 2, § 344, § 335** `p3452`→`spr` | Wortlautkarte, Tiedemann allein | tabler:`signature`, `mail`, `list-check`, `arrow-bounce` | `Begründung › Form: § 345 Abs. 2 StPO` → `› eigener Brief reicht nicht` → `› Inhalt: § 344 StPO` → `Sprungrevision, § 335 StPO` | Karte · Marker · ✗ Brief · Verfahrensrüge · Sachrüge · Block § 335 · Zeile | – |
| **I Telefonat** `entd`→`st2` | geteiltes Bild: Kanzlei (Schreibtisch, Kalender-X) \| Zuhause (Lampe, Sofa) | tabler:`calendar-x`, `sofa`, `lamp-2`, `phone-call`, `phone-ringing` | `Fall · 10. August: der Fehler` → `· Ist die Revision verloren?` → `· Wiedereinsetzung!` | Grundbild · Pille 10.8. · Telefon · Blase Tiedemann · Blase Sternberg · Tiedemann erleichtert | Telefonklingeln (`szene_168telefon_1`) |
| **K §§ 44, 45** `p44`→`nach` | zwei Wortlautkarten, beide Figuren | tabler:`arrow-back-up`, `hourglass`, `file-certificate`, `send` | `Wiedereinsetzung › § 44 S. 1 StPO: ohne Verschulden` → `› § 45 Abs. 1 StPO: eine Woche` → `› Glaubhaftmachung, § 45 Abs. 2 S. 1` → `› Nachholung, § 45 Abs. 2 S. 2` | Karte § 44 + 3 Marker · Karte § 45 + 6 Marker | – |
| **L Verschulden, Lösung** `zur`→`gew` | Tafel, beide Figuren | tabler:`scale`, `user-check`, `phone-call`, `send`, `shield-check` | `› Verschulden der Kanzlei?` → `› nicht zugerechnet` → `› kein eigenes Verschulden (+)` → `› Wochenfrist ab 10.8.2026` → `› Antrag am 12.8.2026 (+)` → `› zu gewähren (+)` | § 85 ZPO · ✓ nicht zugerechnet + BGH · ✓ Auftrag · Wochenfrist + BGH · Antrag · Block | – |
| **M Die Grenze** `grenze`→`gr3` | hellgelbe Tafel, Sternberg | tabler:`alert-triangle`, `file-x`, `ear` | `› die Grenze` → `› Verfahrensrügen nachschieben? (-)` → `› §§ 344, 345 nicht unterlaufen` → `› Ausnahme: rechtliches Gehör` | Zeilen nacheinander, BGH-Fundstellen, Block Ausnahme | – |
| **N Merktabelle** `tab`→`tb3` | breite Tabelle | – | `Merktabelle · …` | Kopf · 3 Zeilen | – |
| **O Klausurtipp** `tipp`→`k3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · der Fristen-Check` → `· Wochentag, Wochenende, Feiertag` → `· versäumt: Wiedereinsetzung` | Zeitstrahl 4 Punkte nacheinander · Wochentag · Frist versäumt? · Wiedereinsetzung | – |
| **P Prüfschema** `sch`→`s5` | breite Karte, Aufbau Punkt für Punkt | – | `Prüfschema › I. …` bis `› V. Wiedereinsetzung` | 11 Stufen | – |
| **Q Merksatz** `merke`/`m2` | Lexi erklärt (redet), Marker | – | `Merksatz` | 2 Sätze, 3 Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; keine Bewegung von Figuren, kein Zoom.
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0, Herkunft in [`geraeusche_herkunft.json`](geraeusche_herkunft.json).
**Blasen:** Stil C, wortgleich mit dem Gesprochenen. Wortlautkarten wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), Auslassungen mit „…“.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Am Montag, 18. Mai 2026, verurteilt die Strafkammer des Landgerichts Herrn Tiedemann im ersten Rechtszug wegen Betrugs zu einer Freiheitsstrafe. Er ist bei der Verkündung anwesend und wird über das Rechtsmittel belehrt.
>
> Seine Verteidigerin, Rechtsanwältin Sternberg, legt am Dienstag, 26. Mai 2026, über das besondere elektronische Anwaltspostfach Revision ein. Das schriftliche Urteil wird ihr am Montag, 6. Juli 2026, zugestellt.
>
> In ihrer Kanzlei wird die Begründungsfrist versehentlich für den 6. September 2026 notiert. Am Montag, 10. August 2026, bemerkt sie den Fehler und unterrichtet Herrn Tiedemann noch am selben Tag.
>
> **War die Einlegung rechtzeitig, bis wann war zu begründen – und was kann Herr Tiedemann jetzt tun?**
