# Folge 022 · Tankbetrug: Tanken ohne zu zahlen – Diebstahl oder Betrug? – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_022.py`](src/skript_022.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker-Fall). Fiktiver Fall an einer Selbstbedienungstankstelle → Frage → Sachverhalt → A. Jens: I. Diebstahl (Wortlaut § 242 I, Einverständnis: Geben statt Nehmen) → II. Betrug (Wortlaut § 263 I, Merkmale, Subsumtion) → Abwandlung: Personal bemerkt nichts (Wortlaut § 22, versuchter Betrug, BGH 2012, Subsidiarität mit Wortlaut § 246 I) → B. Gegenfall Renate: Entschluss erst nach dem Tanken (§ 263/§ 242 −, § 246 und Streit um den Eigentumsübergang) → Klausurtipp → Schema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Jens (JE), Mitte 20 | tankt mit vorgefasstem Zahlungsunwillen | `standing/easing-1`, Kopf `Short 5`, Hemd Türkis `#7FD6D0`, Shirt `#2E2E3A`, Haut `#E8B98F`; Mimiken `Calm`, `Suspicious` (redet), `Cheeky|Smile`, `Fear`, `Serious`, `Tired` | `timo` (Mann, jung) |
| Birgit (BI), um 40 | Kassiererin | `standing/pointing_finger-2`, Kopf `Long Bangs`, Brille `Glasses 4`, Hose Lila `#B8A9F5`, Haut `#C99470`; `Calm`, `Rage|Serious` (redet), `Smile`, `Suspicious`, `Serious` | `laura_klar` (Frau, mittel) |
| Renate (RE), um 70 | Gegenfall: Entschluss erst nach dem Tanken | `standing/resting-1`, Kopf `Gray Medium` (Haar grau `#E2E2E2`), Brille `Glasses`, Pullover Orange `#F9A66C`, Haut `#F1C7A5`; `Calm`, `Contempt` (redet), `Serious`, `Smile` | `hilde` (Frau, älter) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimiken nur als `Rage|Serious`, `Cheeky|Smile`. Mundzustände a/o/e nur bei `JE_redet`, `BI_redet`, `RE_redet` (je links/rechts) und Lexi.
- Grundansicht blickt nach links (Tafelszenen; Jens zur Säule), `_r` nach rechts (Birgit blickt aus dem Shop zur Säule). Am Kontaktbild geprüft.
- Keine Bärte, keine Prothesen-Posen, keine Karikaturen.
- **Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben:** Jens, Birgit, Renate. Stimmen nur aus dem Pool (timo, laura_klar, hilde; `otto` nicht gebraucht). Vorfolge 021 nutzte ela_froh, helmut, julia – keine Überschneidung.
- Figuren-PNGs: `../peeps/op_022/` (60 Dateien, im Drive-Master).

**Abweichung von den letzten Folgen:** 021 Wohnung/Laden (Geschäftsfähigkeit), 020 Behörde/Schema, 019 Straße mit Sitzblockade. Hier erstmals eine Tankstelle (Shop mit Theke, Kasse und Bildschirm, Zapfsäule 3); neue Figuren und Posen. Autos sind dieselben Tabler-Icons wie in 001/019, aber an der Zapfsäule statt im Verkehr. Der Gegenfall kehrt bewusst an dieselbe Tankstelle zurück (gleiche Säule, anderes Auto, andere Kundin), weil er nur den Zeitpunkt des Entschlusses ändert.
**Tageszeit:** „Dienstagabend“ nur als Pille und Mond-Icon; Cremegrund (kein Nachtverlauf nötig, die Tageszeit trägt den Fall nicht).

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Säule drei / Frage** `fall`→`frage2` | Tankstelle von der Seite: Shop links (Birgit hinter der Theke), Zapfsäule 3, Auto fährt vor; Jens tankt, steigt ein, fährt weg; Birgit ruft | tabler:`gas-station`, `cash-register`, `device-desktop`, `car`, `wallet-off`, `droplet`, `moon-stars` | `Fall · Säule drei` (ab 0,0 s) → `Fall · Die Frage` | Grundbild · Selbstbedienung · Stadtrand · Auto fährt vor · Jens · Konto leer · Beschluss · Jens redet · tankt · 60 Liter · 110 € · Birgit · Bildschirm · Säule 3 läuft · lässt ihn tanken · Zapfhahn ein · Jens steigt ein · fährt davon · Birgit redet · Frage · Abwandlungsfrage | Zapfhahn (`szene_022zapf_1`), Wegfahren (`szene_022auto_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Diebstahl** `a`→`kein242` | Tafel mit **Wortlautkarte § 242 I** (Marker „wegnimmt“), Jens rechts | tabler:`gas-station`, `hand-grab`; Haken/Kreuz | `A. Jens` → `A. Jens › I. Diebstahl, § 242 StGB` → `… › Wegnahme` → `A. Jens › I. Diebstahl (-)` | ≈ 9 | – |
| **D1 Betrug: Wortlaut** `p263`→`merkm` | **Wortlautkarte § 263 I**, Marker synchron zu Täuschung, Irrtum, Schaden, Absicht; sechs Merkmal-Pillen in Sprechreihenfolge | – | `A. Jens › II. Betrug, § 263 StGB` | ≈ 8 | – |
| **D2 Subsumtion** `taeu`→`erg1` | Tafel mit 1.–5. und Ergebnisblock; Jens und Birgit rechts | tabler:`droplet`, `coin-euro` | `… › 1. Täuschung` → `2. Irrtum` → `3. Vermögensverfügung` → `4. Schaden` → `5. Vorsatz, Bereicherungsabsicht` → `A. Jens › Ergebnis` | ≈ 12 | – |
| **E1 Abwandlung** `abw`→`vers2` | Tafel; Birgit telefoniert; **Wortlautkarte § 22** (Marker „nach seiner Vorstellung“, „unmittelbar ansetzt“) | tabler:`phone-call` | `A. Abwandlung › Birgit bemerkt nichts` → `… › 2. Irrtum (-)` → `A. Abwandlung › III. versuchter Betrug, §§ 263, 22, 23 StGB` | ≈ 8 | – |
| **E2 BGH 2012, Subsidiarität** `bgh12`→`subs` | Tafel; **Wortlautkarte § 246 I** (Marker Subsidiaritätsklausel) | tabler:`gavel` | `A. Abwandlung › BGH, 10.1.2012 – 4 StR 632/11` → `A. Abwandlung › § 246 StGB tritt zurück` | ≈ 6 | – |
| **F1 Gegenfall an der Tankstelle** `gegen`→`rweg` | dieselbe Tankstelle; Renate an Säule 3 mit grünem Auto, Schlange an der Theke; Renate spricht und fährt weg | tabler:`users-group`, `users`, `car` | `B. Gegenfall: Renate` | ≈ 7 | Wegfahren (`szene_022auto_1`) |
| **F2 Renate: Prüfung** `r263`→`fremd` | Tafel: § 263/§ 242 (−), **Wortlautkarte § 246 I** (Marker „fremde“), „umstritten“ | tabler:`droplet` | `B. Renate › Betrug, Diebstahl (-)` → `… › Unterschlagung, § 246 StGB` → `… › fremde Sache?` | ≈ 7 | – |
| **F3 Streitstand** `ans1`→`offen` | zwei Ansichten als Blöcke, Fundstellen, Vermischung, BGH offen | tabler:`receipt-euro`, `coin-euro` | `B. Renate › § 246 StGB › Streit: Eigentumsübergang` → `… › BGH: offen` | ≈ 9 | – |
| **G Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand), tabler:`clock` | `Klausurtipp · Zeitpunkt des Entschlusses` | ≈ 6 | – |
| **H Klausurschema** `sch`→`k2b` | breite Karte, progressiv | – | `Klausurschema` | 9 | – |
| **I Merksatz** `merke`→`m3` | Lexi erklärt, Marker | – | `Merksatz` | ≈ 5 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 13 Folien; innerhalb harte Schnitte und Pops; Bewegung nur bei fahrenden Autos.
**Geräusche:** zwei Handlungsgeräusche (Freesound CC0), Herkunft in `geraeusche_herkunft.json`.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 242 I (bis „zuzueignen, …“), § 263 I (bis „unterhält, …“, amtliche Schreibung „daß“), § 22 und § 246 I vollständig, wörtlich nach gesetze-im-internet.de, mit Normangabe; Marker synchron zum gesprochenen Merkmal.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Dienstagabend an einer Selbstbedienungstankstelle: Jens hat kein Geld auf dem Konto und schon zu Hause beschlossen, nicht zu zahlen. Er tankt an Säule 3 sechzig Liter Super für 110 Euro. Kassiererin Birgit sieht auf ihrem Bildschirm, dass an Säule 3 ein Kunde tankt, und lässt ihn tanken. Dann fährt Jens davon, ohne zu bezahlen.
>
> Abwandlung: Birgit telefoniert und bemerkt den Tankvorgang gar nicht.
>
> Gegenfall: Renate tankt und will bezahlen. Erst als sie die lange Schlange an der Kasse sieht, beschließt sie, ohne zu zahlen wegzufahren, und fährt davon.
>
> *(Fiktiver Fall, alle Personen erfunden.)*
>
> **Wie haben sich Jens und Renate strafbar gemacht?**
