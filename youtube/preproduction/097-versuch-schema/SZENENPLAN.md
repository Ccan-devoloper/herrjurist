# Folge 097 · Versuch Schema: Vorprüfung, Tatentschluss, unmittelbares Ansetzen – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_097.py`](src/skript_097.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall, Themenplan-Format „Schema“. Der Plan-Hook trägt den Film: Herbert schießt nach einem Streit um das Auto vor seiner Garage auf seinen Nachbarn Gregor und verfehlt ihn um Zentimeter. Frage → Sachverhalt → Wortlautkarten § 22 und § 23 Abs. 1, Aufbau, Mordmerkmale (ein Satz) → 0. Vorprüfung → I. 1. Tatentschluss → I. 2. unmittelbares Ansetzen (Formel, Gefährdung, Abgrenzung Vorbereitung) → II. Rechtswidrigkeit, III. Schuld → IV. Rücktritt (fehlgeschlagener Versuch) → Ergebnis, § 23 Abs. 2, Konkurrenz → Klausurtipp (Lexi) → Klausurschema → Merksatz (Lexi).
**Verhältnis zu 011 (Deliktsaufbau) und 029 (Vorsatzformen):** Der dreistufige Aufbau und die Vorsatzformen werden nicht wiederholt; hier nur, was beim Versuch anders ist (Vorprüfung, Tatentschluss vor dem Ansetzen, Rücktritt als vierter Punkt).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herbert (HE), Anfang 60 | Täter | `standing/pointing_finger-2` (schwarzer Pullover der Pose, Hose Graublau `#6E7F9E`), Kopf `No Hair 3` (grauer Haarkranz), Brille `Glasses 3`, Haut `#EDC3A0`. Mimiken `Calm`, `Very Angry`, `Rage|Serious` (redet im Streit), `Driven` (zielt), `Concerned|Serious` (redet bestürzt), `Tired`, `Serious`, `Suspicious` | `william` (Mann, älter) |
| Gregor (GR), um 45 | Nachbar, Opfer des Versuchs (unverletzt) | `standing/walking-1` (T-Shirt Grün `#8FD694`, schwarze Hose), Kopf `Short 4`, Haut `#C98F66`. Mimiken `Calm`, `Suspicious`, `Concerned Fear|Serious` (redet erschrocken), `Fear`, `Awe`, `Smile`, `Serious` | `marc` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links: Gregor im Fall zu Herbert, beide in den Tafelszenen zur Tafel), `_r` blickt nach rechts (Herbert im Fall zu Gregor, Gregor auf dem Weg zur Haustür).
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimiken nur als `Rage|Serious`, `Concerned|Serious`, `Concerned Fear|Serious`. Mundzustände a/o/e bei `HE_redet`, `HE_bestuerzt`, `GR_redet` (je links/rechts) und Lexi. Kein Bart, keine Prothesen-Pose (die `shirt-`/`blazer-`Posen mit Prothese wurden für den Täter bewusst nicht genommen). 56 Figuren-PNGs in `../peeps/op_097/` (Drive-Master).
- **Klischeeprüfung:** Herbert ist ein gewöhnlicher älterer Nachbar (Pullover, Brille), keine Karikatur, keine Herkunfts- oder Hautfarbenzuschreibung; die Pistole erscheint nur als weiß gefülltes Linien-Icon an seiner Hand.
- **Namen** mit eindeutig deutscher Aussprache, in keiner Vorfolge vergeben (Auftragsliste und alle Skripte/Dokumente in `preproduction/` geprüft; auch nicht 094/096: Hartwig, Wilma, Benedikt, Wendland, Vollmer): Herbert, Gregor. Nie im Genitiv mit -s gesprochen („die Garage von Herbert“).
- **Stimmen** nur aus dem Pool (william, marc; sabrina, laura_ruhig nicht gebraucht). In 091 sprach william den Vordermann Ulrich, marc den Wolfram; in 095 marc den Fliesenleger: jetzt anders besetzt (william = Täter, marc = Opfer). Lea nicht verwendet.
- **Abwechslung:** Posen nicht aus 094–096 (robot_dance-2, polka_dots, blazer-3, easing-1/-2, shirt-3, resting-1, blazer-4, crossed_arms-1), keine Polka Dots.

**Abweichung von den letzten Folgen:** 094 (Sirius-Fall), 095 (Badezimmer), 096 (Pfändung). Neu: Wohnstraße mit zwei Hausfronten, Garage mit Sektionaltor und dem blauen Auto davor; in den Tafelszenen kleine Requisiten rechts (Zielscheibe, Herz, Glühbirne, Haus → Pistole, Schild durchgestrichen, Schloss). Kein früherer Schauplatz (029 Reihenhausgärten mit Mauer/Zaun nicht übernommen).
**Tageslicht:** durchgehend Cremegrund („Samstagabend“ als Sommerabend, kein Nachtverlauf nötig).
**Gewalt zurückhaltend:** Pistole nur stilisiert (Fluent Emoji High Contrast `water-pistol` als Linien-Icon, weiß gefüllt, an der Hand), kein Mündungsfeuer, kein Knall, kein Blut; die Flugbahn ist eine gestrichelte Linie knapp über Gregors Kopf mit Einschlagpunkt in der Hauswand. Thumbnail ohne Waffe.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Wohnstraße** `fall`→`frage2` | Haus von Herbert (lila Dach), Garage, blaues Auto davor, Herbert; rechts Gregor vor seiner Hauswand (rotes Dach). Streit, Blase Herbert „Fahr endlich dein Auto weg!“; Herbert verschwindet ins Haus, Pistole und „1 einzige Patrone“ erscheinen; Herbert zurück mit Pistole, „5 m“; Blase Gregor „Herbert, leg die Pistole weg!“; Flugbahn, Einschlag mit Ring, „um wenige Zentimeter verfehlt“; Gregor an der Haustür, verschwindet, Schloss; Blase Herbert „Das war meine einzige Patrone.“; Frage-Pillen | ph:`car-profile`, `lock`; Fluent HC:`water-pistol`; Häuser, Garage, Flugbahn als Bausteine | `Fall · Die Wohnstraße` (ab 0,0 s) → `Fall · Die Pistole` → `Fall · Der Schuss` → `Fall · Die Frage` | ≈ 25 | Haustür (`szene_097tuer_1`), Schlüssel (`szene_097schloss_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Wortlaut** `p22`→`mord` | Wortlautkarten § 22 und § 23 Abs. 1 mit Markern, drei Aufbau-Blöcke, Zeile Mordmerkmale/§ 212 | tabler:`target`, `list-numbers`, `scale` | `Versuch › Wortlaut §§ 22, 23 Abs. 1 StGB` → `Versuch › Aufbau` → `Versuchter Totschlag, §§ 212, 22, 23 Abs. 1 StGB` | ≈ 8 | – |
| **D Vorprüfung** `vp`→`vp4` | Haken Nichtvollendung, Strafbarkeit über § 212/§ 12 Abs. 1, Block § 23 Abs. 1 | tabler:`checklist`, `heart`, `scale` | `… › 0. Vorprüfung` → `… › 1. Nichtvollendung` → `… › 2. Strafbarkeit des Versuchs` | ≈ 7 | – |
| **E Tatentschluss** `te`→`te3` | BGH-Definition, besondere subjektive Merkmale (Klausurstandard), Kreuz „§ 212 verlangt keine“, Haken, Block; Denkblase mit Zielscheibe | tabler:`bulb`, `target` | `… › I. Tatbestand › 1. Tatentschluss` | ≈ 8 | – |
| **F Unmittelbares Ansetzen** `ua`→`vorb` | Formel, Gefährdung, Haken „abgedrückt“, Block, Kreuz „nur Pistole holen“; rechts Haus → Pfeil „Zwischenschritte“ → Pistole | tabler:`target`; ph:`house`; Fluent HC:`water-pistol` | `… › 2. unmittelbares Ansetzen` → `… › Abgrenzung: Vorbereitung` | ≈ 10 | – |
| **G Rechtswidrigkeit, Schuld** `rw`→`schuld` | zwei Abschnitte mit Kreuz „keine Notwehr“ und Blöcken | tabler:`message-circle`, `shield-off`, `user-check` | `… › II. Rechtswidrigkeit` → `… › III. Schuld` | ≈ 7 | – |
| **H Rücktritt** `rt`→`rt5` | Prüfungspunkt nach der Schuld, Fehlschlag-Definition, Haken „nur 1 Patrone“, Block „fehlgeschlagen: kein Rücktritt“; rechts Pistole „0 Patronen übrig“ | tabler:`arrow-back-up`, `circle-x`; Fluent HC:`water-pistol` | `… › IV. Rücktritt, § 24 StGB` → `… › fehlgeschlagener Versuch` | ≈ 8 | – |
| **I Ergebnis** `erg`→`konk` | Ergebnisblock, Milderung, Konkurrenz | tabler:`gavel`, `arrow-down`, `stack-2` | `Ergebnis` → `… › Strafmilderung` → `… › Konkurrenzen` | ≈ 6 | – |
| **J Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Tatentschluss vor Ansetzen` | ≈ 5 | – |
| **K Klausurschema** `sch`→`s4b` | breite Karte, progressiv | – | `Klausurschema` | ≈ 11 | – |
| **L Merksatz** `merke`→`m3` | Lexi erklärt, drei Marker | – | `Merksatz` | ≈ 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 12 Folien; innerhalb harte Schnitte und Pops.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 22 und § 23 Abs. 1 vollständig, wörtlich nach gesetze-im-internet.de mit Normangabe, wörtlich vorgelesen; Marker synchron.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Herbert (Anfang 60) und sein Nachbar Gregor streiten seit Monaten, weil Gregor sein Auto immer wieder vor Herberts Garage parkt. An einem Samstagabend kommt es erneut zum Streit.
>
> Herbert holt aus seinem Haus eine alte Pistole, in der eine einzige Patrone steckt; weitere Munition hat er nicht. Er zielt aus 5 Metern auf Gregor, der ihm zuruft, er solle die Pistole weglegen. Herbert will Gregor töten und drückt ab. Die Kugel verfehlt Gregor um wenige Zentimeter und schlägt in die Hauswand ein.
>
> Gregor rennt in sein Haus und schließt ab. Herbert weiß, dass er keine Patrone mehr hat. Gregor bleibt unverletzt.
>
> **Hat sich Herbert wegen versuchten Totschlags strafbar gemacht?**
