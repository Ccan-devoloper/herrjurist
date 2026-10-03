# Folge 109 · Regelverjährung in 5 Minuten: Drei Jahre und der Silvester-Trick – Szenenplan

**Stand:** 03.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_109.py`](src/skript_109.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/BGB AT, Themenplan-Format „Schema“. Beispielfall nach dem Plan-Hook („Du schuldest einem Freund seit 2022 Geld – ab wann darfst du dich auf Verjährung berufen?“): Im März 2022 leiht Finn seiner guten Freundin Pia 2.000 € für die Kaution ihrer ersten Wohnung; Rückzahlung fest am 1. Juli 2022. Pia zahlt nicht, Finn fragt nicht nach. Im Oktober 2026 treffen sich beide im Park. Variante: Abschlag von 200 € am 15. Mai 2024.

Ablauf: Fall (Café, Übergabe des Geldes, Rückzahlungstag) → 1. Juli 2022 (Pia zahlt nicht) → Park, Oktober 2026, Wortwechsel → Frage → Sachverhalt → Rechenweg in 6 Schritten → I. Anspruch (§ 194 Abs. 1, Wortlaut) → II. Frist (§ 195, Wortlaut) → III. Beginn (§ 199 Abs. 1, Wortlaut; Fall) → Silvester-Trick am Zeitstrahl (progressiv) → IV. Höchstfristen (§ 199 Abs. 4, Wortlaut) → V. Hemmung (§§ 203, 204, 209) → V. Neubeginn (§ 212 Abs. 1 Nr. 1, Wortlaut auszugsweise) mit Variante am Zeitstrahl → VI. Rechtsfolge (§ 214 Abs. 1, Wortlaut) → Ergebnis → Klausurtipp (Lexi) → Rechenschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 5:28,9 (4.573 vertonte Zeichen).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Pia, um 28 | Darlehensnehmerin, Schuldnerin | `standing/easing-2` (offenes Hemd Koralle `#F07A6A` über schwarzem Shirt, Hose Gelb `#F9D56E`, Turnschuhe), Kopf `Long Bangs`, Haut `#F1C9A5`; Mimiken `Calm`, `Smile` (redet), `Cheeky|Smile` (frech, redet), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious`, `Awe` | `julia` (Frau, jung) |
| Finn, um 28 | guter Freund, Darlehensgeber, Gläubiger | `standing/walking-3` (schwarzes T-Shirt, schwarze Hose, weiße Turnschuhe; Pose ohne einfärbbare Kleidung), Kopf `Short 3`, Haut `#D8A47F`; Mimiken `Calm`, `Smile` (redet), `Serious` (fordert), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious` | `niklas` (Mann, jung) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache (gleich in deutscher und englischer Lesart), in keiner früheren Folge vergeben (geprüft per `grep -rlw` über alle Text-/Codedateien in `youtube/` und gegen die Koordinatorliste; „Finn“ kommt nur in Testdaten des Instagram-Bots `src/`, `test/` vor, nicht in einer Folge): Pia, Finn. Kein Genitiv eines Namens im Sprechtext („Der Anspruch von Finn“).
- **Stimmen nur aus dem Pool** niklas, helmut, ela_froh, julia: gebraucht `julia` (Pia) und `niklas` (Finn); beide jung, passend zu zwei Freunden um 28. `helmut` (älter) passt nicht zur Rolle, `ela_froh` nicht für die nachdenklich-freche Schuldnerin. Vorfolgen 105–107: marc, sabrina, laura_ruhig, hilde, christian – keine Überschneidung (julia/niklas zuletzt in 104).
- Präfixe `PI_`/`FI_` (nie `ER_`).
- Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Im Café und im Park steht Finn links und blickt nach rechts zu Pia, Pia rechts blickt nach links zu ihm; in den Tafelszenen blicken beide nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `PI_redet`, `PI_frech`, `FI_redet`, `FI_fordert` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur. Keine weiteren Menschen im Bild.
- **Abwechslung:** Posen, Kleidung und Muster nicht aus 105 (`resting-1`, `walking-2`, `blazer-2`), 106 (`blazer-4`, `crossed_arms-2`), 107 (`shirt-3`, `resting-2`, `blazer-3`); keine Polka Dots. Figurenrezepte und Kontaktbögen verglichen.
- Figuren-PNGs: `../peeps/op_109/` (58 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 105 (Verwaltungsgericht), 106 (Laptop, Online-Handel), 107 (Geldautomat), 103 (Tischlerwerkstatt, Wohnzimmer, Treppe als Leitmotiv). Hier neu: ein Café mit lila Bistrotisch und zwei Kaffeetassen, links das Motiv „Kaution für die erste Wohnung“ (Haus, Schlüssel); ein Park im Herbst (zwei Bäume in Orange/Gelb, Bank, Laub), durch den Finn hereinläuft. Leitmotiv statt der Treppe von 103: die **Rechenleiste I–VI** oben rechts auf jeder Schritt-Tafel (aktiver Schritt gelb) und zwei progressive **Zeitstrahlen** mit Silvester-Konfetti an den Jahreswechseln. Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Im Café** `fall`–`still` | ab 0,0 s: Pille „März 2022“, Bistrotisch mit 2 Tassen, Haus und Schlüssel, beide Figuren mit Namensschild; Pille „Kaution für die erste Wohnung“ bei „Kaution“; bei „leiht“ wandern Geldscheine von Finns Hand zu Pia, Pille „2.000 € geliehen“, Pia froh; Blase Finn „Aber bis zum 1. Juli / will ich es zurück.“, Kalender + Pille „zurück am 1.7.2022“ bei „Juli“; Blase Pia „Versprochen. Am 1. Juli / hast du es.“; Pille wechselt auf „1. Juli 2022“, „Pia zahlt nicht“ (rot), „Finn fragt nicht nach“ | tabler:`coffee`, `home` (Gelb), `key`, `cash-banknote` (Grün), `calendar-event`; Tisch programmatisch | `Fall · Im Café` → `Fall · 1. Juli 2022` | `szene_109geld_1` bei „leiht“ |
| **A2 Im Park** `okt`–`frage2` | Pille „Oktober 2026“, Bäume, Bank, Laub; Pia steht rechts, Finn läuft von links durch das Laub herein (1,7 s, Namensschild läuft mit); Blase Finn „Pia, ich hätte gern endlich / meine 2.000 € zurück!“; Blase Pia (frech) „Das ist über 4 Jahre her. Ist / das nicht längst verjährt?“; Pillen „Seit wann darf sich Pia auf die Verjährung berufen?“, „Und was, wenn sie etwas zurückgezahlt hätte?“ | ph:`tree` (Orange, Gelb), tabler:`leaf`; Bank (`ostil.bank`) | `Fall · Oktober 2026` → `Fall · Die Frage` | `szene_109laub_1`, während Finn durch das Laub geht |
| **B Sachverhalt** `sv` | Karte vollständig (35 px), ≈ 9,8 s, ohne Fiktiv-Hinweis, mit Variante | – | `Sachverhalt` | – |
| **C Rechenweg** `plan`–`s6` | Tafel „Regelverjährung in 6 Schritten“, Schritte I.–VI. mit Farbkästchen nacheinander zum Wort | tabler:`list-numbers`, `calendar-event`, `clock-pause` | `Regelverjährung › Rechenweg` | – |
| **D I. Anspruch** `a194`–`a488` | Rechenleiste (I), Wortlautkarte § 194 Abs. 1 (Marker „(Anspruch)“, „unterliegt der Verjährung“), „Hier: Anspruch auf Rückzahlung des Darlehens“, § 488 Abs. 1 Satz 2, blauer Block „Finn gegen Pia: 2.000 € zurück“ | tabler:`file-text`, `cash-banknote` | `I. Anspruch › § 194 Abs. 1 BGB` → `› Rückzahlung des Darlehens` | – |
| **E II. Frist** `f195`–`fdarl` | Rechenleiste (II), Wortlautkarte § 195 (Marker „drei Jahre“), gelber Block „3 Jahre“, „gilt auch für die Rückzahlung von Darlehen“ (BGH IX ZR 129/17 Rn. 6) | tabler:`hourglass`, `cash-banknote` | `II. Frist › § 195 BGB` → `› auch beim Darlehen` | – |
| **F III. Beginn** `b199`–`bfall2` | Rechenleiste (III), Wortlautkarte § 199 Abs. 1 (Marker „mit dem Schluss des Jahres“, „der Anspruch entstanden ist“, „Kenntnis erlangt“, „ohne grobe Fahrlässigkeit“), Fundstelle XII ZB 104/22 Rn. 16; ✓ „1. fällig am 1.7.2022“, ✓ „2. Kenntnis: Finn kennt Pia und alle Umstände“ | tabler:`calendar-event`, `receipt-euro`, `eye` | `III. Beginn › § 199 Abs. 1 BGB` → `› der Fall` | – |
| **G Silvester-Trick** `silv`–`sneu` | Rechenleiste (III), Zeitstrahl 2022–2026; Punkte und Pillen „Januar“/„Dezember“ zum Wort, Pfeil und Konfetti am Jahresende; roter Ring „Beginn: 31.12.2022, 24 Uhr“; Blöcke „1./2./3. Jahr“ zu den gesprochenen Jahreszahlen; Ring und Konfetti 31.12.2025 „Ablauf 31.12.2025: verjährt“; grüner Block „Seit 1.1.2026: Pia darf die Zahlung verweigern“ | tabler:`confetti` (Diagramm und Requisit), `clock-hour-12`, `hourglass`, `hourglass-empty`, `hand-stop` | `III. Beginn › der Silvester-Trick` → `› Ende der Frist` → `Ergebnis der Rechnung › ab 1.1.2026` | – |
| **H IV. Höchstfristen** `hoech`–`h23` | Rechenleiste (IV), „Ohne Kenntnis: Höchstfrist“, Wortlautkarte § 199 Abs. 4 (Marker „ohne Rücksicht auf die Kenntnis“, „in zehn Jahren von ihrer Entstehung an“), Block „10 Jahre ab Entstehung“, „Schadensersatz: § 199 Abs. 2 und 3 BGB“ | tabler:`eye-off`, `calendar-time`, `scale` | `IV. Höchstfristen › § 199 Abs. 4 BGB` → `› Schadensersatz` | – |
| **I V. Hemmung** `hemm`–`hnein` | Rechenleiste (V), „Die Hemmung hält die Uhr an.“, § 209, §§ 203, 204 Abs. 1 Nr. 1, Nr. 3 zum Wort; ✗ keine Verhandlungen / keine Klage / kein Mahnbescheid; lila Block „Hier nichts davon: keine Hemmung“ | tabler:`clock-pause`, `message-circle-question`, `gavel`, `mail`, `x` | `V. Hemmung › die Uhr hält an` → `› §§ 203, 204 BGB` → `› der Fall` | – |
| **J V. Neubeginn** `neu`–`vrest` | Rechenleiste (V), „Der Neubeginn stellt die Uhr auf null.“, Wortlautkarte § 212 Abs. 1 Nr. 1 auszugsweise (Marker „beginnt erneut“, „Abschlagszahlung“); Zeitstrahl 2022–2027: Punkt und Münze 15.5.2024, Pille „15.5.2024: Abschlag 200 €“, gelber Balken „neue 3 Jahre, taggenau“, „ab 16.5.2024, ohne Silvester-Trick“ (XII ZR 86/11 Rn. 33), Ring „Ablauf 15.5.2027“, hellroter Block „Pia müsste die restlichen 1.800 € noch zahlen“ | tabler:`refresh`, `coin-euro`, `calendar-event`, `cash-banknote` | `V. Neubeginn › § 212 Abs. 1 Nr. 1 BGB` → `› Variante: Abschlag` → `› Variante: Ergebnis` | – |
| **K VI. Rechtsfolge** `r214` | Rechenleiste (VI), Wortlautkarte § 214 Abs. 1 (Marker „Nach Eintritt der Verjährung“, „die Leistung zu verweigern“), „Der Anspruch erlischt nicht.“, gelber Block „Pia muss sich darauf berufen“ | tabler:`file-text`, `hand-stop` | `VI. Rechtsfolge › § 214 Abs. 1 BGB` | – |
| **L Ergebnis** `erg`–`erg3` | „Anspruch von Finn:“ ✗ „verjährt mit Ablauf des 31.12.2025“; gelber Block „Beruft sich Pia darauf: Sie muss nicht zahlen“ (Pia frech); „Variante mit Abschlag:“ hellroter Block „Rest bis Mai 2027 durchsetzbar“ | tabler:`hourglass-empty`, `hand-stop`, `coin-euro` | `Ergebnis` | – |
| **M Klausurtipp** `tipp`–`tipp2` | hellgelbe Tafel, Lexi warnt; „Prüfe zuerst die Fälligkeit!“, „Kein Rückzahlungstag vereinbart:“, „Fälligkeit hängt von einer Kündigung ab,“, Fundstelle § 488 Abs. 3 Satz 1, IX ZR 129/17 Rn. 6, „erst dann kann die Frist beginnen.“; „Ein Abschlag wirkt nur, während die Frist läuft.“ mit IX ZR 129/17 Rn. 8 und XI ZR 265/13 Rn. 40 | Warnsymbol (Streamline Freehand) | `Klausurtipp · zuerst die Fälligkeit` → `· Abschlag nur in laufender Frist` | – |
| **N Rechenschema** `sch`–`k6` | breite Karte „Rechenschema: Regelverjährung“, Zeilen I.–VI. mit Farbkästchen und Norm, III. mit „1. Entstehung · 2. Kenntnis · 3. Jahresschluss“ zum Wort | – | `Rechenschema` → `› I. Anspruch` … `› VI. Rechtsfolge` | – |
| **O Merksatz** `merke`–`mk3` | Lexi erklärt; Marker „Drei Jahre,“, „hält die Uhr an,“, „stellt sie auf null.“ | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; Bewegung nur bei der Geldübergabe und Finns Weg durch den Park.
**Blasen:** Stil C (`bausteine.blase`), wortgleich mit dem Gesprochenen, Zahlen als Ziffern („1. Juli“, „2.000 €“, „4 Jahre“). Zahlen auf Tafeln, Pillen und Karte als Ziffern; Normwortlaut wörtlich („drei Jahre“, „zehn Jahren“).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Im März 2022 leiht Finn seiner guten Freundin Pia 2.000 Euro für die Kaution ihrer ersten Wohnung. Beide vereinbaren, dass Pia das Geld am 1. Juli 2022 zurückzahlt. Pia zahlt nicht. Finn fragt nicht nach, verhandelt nicht mit ihr, klagt nicht und beantragt keinen Mahnbescheid.
>
> Im Oktober 2026 verlangt Finn die 2.000 Euro zurück. Pia meint, das sei längst verjährt.
>
> Variante: Pia hat Finn am 15. Mai 2024 einen Abschlag von 200 Euro gezahlt.
>
> **Seit wann darf sich Pia auf die Verjährung berufen – und was ändert der Abschlag?**
