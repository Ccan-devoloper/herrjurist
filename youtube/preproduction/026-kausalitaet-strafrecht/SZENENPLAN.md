# Folge 026 · Kausalität im Strafrecht: Conditio-sine-qua-non einfach erklärt – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_026.py`](src/skript_026.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen, Themenplan-Format „Schema“. Der Hook des Themenplans trägt den Film: Kioskbesitzer Egon verkauft Bodo ein Feuerzeug, Bodo zündet nachts die Scheune der Landwirtin Maren an. Frage → Sachverhalt → Erfolgsdelikte (Wortlaut §§ 212 I, 222, 306 I Nr. 1) → Bedingungstheorie/csqn-Formel, Äquivalenztheorie (Lehre) → Wegdenken am Fall (Bodo, Egon, sogar der Hersteller: „zu weit“) → Ersatzursache → keine Unterbrechung durch Bodos Vorsatztat → Kausalität nur die erste Hürde (objektive Zurechnung, Vorsatz) → Abwandlung 1 überholende Kausalität (Blitz, nur Versuch) → Abwandlung 2 alternative Kausalität (BGHSt 39, 195) → Abwandlung 3 kumulative Kausalität → Ausblick Unterlassen (Quasi-Kausalität) → Klausurtipp → Schema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Egon (EG), Mitte 60 | Kioskbesitzer, verkauft das Feuerzeug | `standing/blazer-1`, Kopf `No Hair 2`, Brille `Glasses 2`, Jacke Grün `#8FD694`, Hose `#5A5A6E`, Haut `#F0C8A8` (Pose mit Unterschenkelprothese; Egon ist kein Täter). Mimiken `Calm`, `Smile` (redet, froh), `Serious`, `Concerned|Serious` | `helmut` (Mann, älter) |
| Bodo (BO), um 40 | Käufer, Brandstifter | `standing/easing-2`, Kopf `Short 3`, Jacke Rot `#F07A6A`, Hose `#3B3B4F`, Haut `#D9A27A`. Mimiken `Calm` (redet), `Cheeky|Smile` (redet, Einwand), `Suspicious` (schleicht), `Driven` (zündet), `Fear`, `Serious`, `Concerned|Serious` | `stephan` (Mann, mittel) |
| Maren (MA), um 30 | Landwirtin, Eigentümerin der Scheune | `standing/polka_dots`, Kopf `Medium Bangs 2`, Oberteil Blau `#8DB3F2`, Hose Gelb `#F9D56E`, Haut `#E8B894`. Mimiken `Fear` (redet), `Tired`, `Calm`, `Serious` | `ela_warm` (Frau, jung) |
| Silke (SI) | Abwandlungen 2 und 3, ohne Sprechrolle | `standing/crossed_arms-2`, Kopf `Long Curly`, Hose Lila `#B8A9F5`, Haut `#C68A62`. Mimiken `Calm`, `Suspicious`, `Concerned|Serious` | – |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links, zur Tafel bzw. zum Kiosk/zur Scheune), `_r` blickt nach rechts (Egon im Kiosk zu Bodo; Bodo in den Abwandlungen 2/3 links der Scheune zur Scheune).
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimiken nur als `Cheeky|Smile`, `Concerned|Serious`. Mundzustände a/o/e nur bei `EG_redet`, `BO_redet`, `BO_frech`, `MA_redet` (je links/rechts) und Lexi. Keine Bärte. 72 Figuren-PNGs in `../peeps/op_026/` (Drive-Master).
- **Namen** mit eindeutig deutscher Aussprache, nicht vergeben (auch nicht in 024/025: Köhler, Vogel, Möller, Svenja): Egon, Bodo, Maren, Silke. „Heinz“ wurde vor der Vertonung verworfen (englisch lesbar).
- **Stimmen** nur aus dem Pool (helmut, stephan, ela_warm; `lucy` nicht gebraucht, Silke spricht nicht). Vorfolge 025 nutzte william/julia, 024 laura_ruhig/marc/hilde/timo – keine Überschneidung. Lea nicht verwendet.

**Abweichung von den letzten Folgen:** 025 (Auschwitzlüge), 024 (Zwangsvollstreckung: Gericht/Wohnung), 022 (Tankstelle), 011 (Uferweg). Hier erstmals ein Dorfkiosk und eine Scheune bei Nacht; neue Figuren und für die Serie wenig genutzte Posen (`blazer-1`, `polka_dots`, `crossed_arms-2` mit neuen Köpfen).
**Nacht:** Szene B spielt nachts; wie in 022 nur als Pille „In der Nacht“ und Mond-Icon auf Cremegrund (die Tageszeit trägt den Fall nicht).

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Dorfkiosk** `fall`→`ahnt` | Kioskhäuschen mit Dach, Fenster, Theke; Egon hinter der Theke, Bodo kommt von rechts herein | tabler:`sunset-2`, `news`, `bottle`, `lighter`, `coin-euro` | `Fall · Am Dorfkiosk` (ab 0,0 s) | Grundbild · Egon · „Mitte 60“ · Bodo kommt · Bodo redet · Egon redet · Feuerzeug · Münze · „ahnt nichts“ | – |
| **B Scheune** `nacht`→`frage2` | Scheune (ph:`barn`) mit Stroh, Bodo schleicht heran, zündet, Flammen, Maren | ph:`barn`, tabler:`moon-stars`, `lighter`, `flame`, `building-store` | `Fall · Die Scheune brennt` → `Fall · Die Frage` | ≈ 10 | Feuerzeug (`szene_026feuerzeug_1`), Feuer (`szene_026feuer_1`) |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 9,7 s | – | `Sachverhalt` | 1 | – |
| **D Erfolgsdelikte** `erfolg`→`p306` | Tafel mit **Wortlautkarten § 212 I, § 222, § 306 I Nr. 1** (Marker „tötet“, „verursacht“, „in Brand setzt“), Maren rechts, brennende Scheune | ph:`barn`, tabler:`flame` | `Erfolgsdelikte › …` | ≈ 7 | – |
| **E Bedingungstheorie** `csqn`→`aequi` | Tafel: Formel zeilenweise, Pille „Conditio-sine-qua-non-Formel“, Äquivalenztheorie (Lehre); Egon, drei gleichwertige Bedingungen | tabler:`help-circle`, `building-store`, `lighter`, `flame` | `A. Kausalität › Bedingungstheorie (BGH)` → `› Conditio-sine-qua-non-Formel` → `› Äquivalenztheorie (Lehre)` | ≈ 10 | – |
| **F Wegdenken** `bodo_k`→`weit` | Tafel; rechts Kette Kiosk → Feuerzeug → Scheune; weggedachte Glieder werden ausgegraut, Flammen verschwinden; zuletzt Hersteller | tabler:`building-store`, `lighter`, `building-factory-2`, ph:`barn` | `A. Kausalität › Formel am Fall › Bodo: Anzünden / Egon: Verkauf / reicht sehr weit` | ≈ 15 | – |
| **G Ersatzursache** `reserve`→`res3` | Bodo (frech) mit Sprechblase, Streichholz-Icon, Kreuz „außer Betracht“ | tabler:`matchstick` | `A. Kausalität › Ersatzursache?` | ≈ 9 | – |
| **H Unterbrechung?** `dritt`→`knuepft` | Tafel mit BGH-Formel, rechts Kiosk – Kette – Feuerzeug – Flamme, Bodo | tabler:`building-store`, `lighter`, `flame`, ph:`link` | `A. Kausalität › Unterbrechung durch Bodos Tat?` | ≈ 10 | – |
| **I Erste Hürde** `huerde`→`vors` | Tafel; Egon (sorgt sich, dann froh), Treppe | tabler:`stairs-up` | `A. Kausalität › nur die erste Hürde` → `B. Nächster Schritt › …` | ≈ 8 | – |
| **J Abwandlung 1** `var1`→`versuch` | Tafel; rechts Scheune mit Kerze im Stroh, Uhr, Blitzwolke, Flammen, Bodo erschrickt | tabler:`candle`, `clock`, `flame`, ph:`cloud-lightning`, `barn` | `B. Abwandlung 1 · Kerze im Stroh` → `› überholende Kausalität (Lehre)` → `› versuchte Brandstiftung, §§ 306, 22, 23 StGB` | ≈ 12 | Donner (`szene_026donner_1`) |
| **K Abwandlung 2** `var2`→`altlehre` | Scheune mit zwei Feuern, Bodo links, Silke rechts | tabler:`flame`, ph:`barn` | `C. Abwandlung 2 · zwei Feuer` → `› Formel streng angewandt` → `› alternative Kausalität` | ≈ 14 | – |
| **L Abwandlung 3** `var3`→`kum2` | dieselbe Scheune (Rückkehr zum Ort der Abwandlung 2, nur das Stroh ist feucht), Tropfen, kleine Flammen, dann Brand | tabler:`droplet`, `flame` | `D. Abwandlung 3 · feuchtes Stroh` → `› kumulative Kausalität (Lehre)` | ≈ 10 | – |
| **M Unterlassen** `unterl`→`quasi` | Tafel; Hand-Icon „keine Handlung“, Feuerlöscher „+ gebotene Handlung“ | tabler:`hand-off`, `fire-extinguisher` | `Ausblick › Unterlassen: Quasi-Kausalität` | ≈ 7 | – |
| **N Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Kausalität knapp oder ausführlich?` | ≈ 7 | – |
| **O Klausurschema** `sch`→`k4` | breite Karte, progressiv | – | `Klausurschema` | 9 | – |
| **P Merksatz** `merke`→`m3` | Lexi erklärt, Marker | – | `Merksatz` | ≈ 5 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegungen: Bodo kommt in den Kiosk (A), Bodo schleicht zur Scheune (B).
**Geräusche:** drei Handlungsgeräusche (Freesound CC0), je einmal, Herkunft in `geraeusche_herkunft.json`.
**Gewalt zurückhaltend:** Sachschaden ohne Personenschaden („verletzt wird niemand“); der Tod erscheint nur im Normtext der Wortlautkarten §§ 212, 222 und im Satz „zwei Schüsse“ (BGH), ohne Bild.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 212 I und § 222 vollständig, § 306 I Nr. 1 mit markierten Auslassungen, wörtlich nach gesetze-im-internet.de mit Normangabe; Marker synchron zum gesprochenen Wort.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Freitagabend kauft Bodo bei Kioskbesitzer Egon (Mitte 60) ein Feuerzeug für 2 Euro. Egon ahnt nichts von Bodos Plan. In der Nacht zündet Bodo mit dem Feuerzeug das Stroh in der Scheune der Landwirtin Maren an. Die Scheune brennt nieder, verletzt wird niemand.
>
> Abwandlung 1: Bodos Kerze im Stroh soll erst in einer Stunde zünden; vorher brennt die Scheune durch einen Blitz ab.
>
> Abwandlung 2: Silke legt unabhängig am anderen Ende Feuer; jedes Feuer hätte allein gereicht. Abwandlung 3: Jedes Feuer wäre allein erloschen. (Fiktiver Fall, Personen erfunden.)
>
> **Ist der Verkauf kausal für den Brand?**
