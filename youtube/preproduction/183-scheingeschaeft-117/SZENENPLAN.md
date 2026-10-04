# Folge 183 · Scheingeschäft § 117 BGB: Schwarzgeld beim Hauskauf – welcher Preis? – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_183.py`](src/skript_183.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · Klassiker-Fall (BGB AT). Fall nach dem Plan-Hook: Markus kauft von Frau Meinhardt ein Haus; vereinbart sind 350.000 €, beurkundet werden auf ihren Vorschlag nur 300.000 €, 50.000 € bekommt sie vorher bar im Umschlag. Im selben Termin wird die Auflassung erklärt, Wochen später wird Markus eingetragen.

Ablauf: Fall (Absprache, Übergabe, Notar, Eintragung) → Frage → Sachverhalt → Aufbau (vier Schritte) → 1. beurkundeter Vertrag (Wortlautkarte § 117 Abs. 1) → 2. verdeckter Vertrag (Wortlautkarte § 117 Abs. 2) → 3. Form (Wortlautkarte § 311b Abs. 1 S. 1, Umfang) → Folge des Mangels (Wortlautkarte § 125 S. 1, Verweis 050) → 4. Heilung (Wortlautkarte § 311b Abs. 1 S. 2, Verweis 145) → Heilung: Inhalt und Grenzen (BGH V ZR 115/22) → Folgen vor/nach der Eintragung (mit Figurenrede) → Hinweise Steuer und § 16a GwG → Abgrenzung §§ 118, 116 (Wortlautkarten) → Klausurtipp (Lexi) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 5:55,68 (5.084 Zeichen); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Markus, um 40 | Käufer | `standing/shirt-3` (Hemd Blau `#8DB3F2`, schwarze Hose), Kopf `Short 2` (Haar Dunkelbraun), Haut `#E8B896`, kein Bart; Mimiken `Calm`, `Smile` (redet), `Serious` (redet ernst), `Smile Big|Smile`, `Suspicious`, `Awe`, `Concerned|Serious` | `stephan` (Mann, mittel) |
| Frau Meinhardt, um 65 | Verkäuferin, Eigentümerin | `standing/robot_dance-3` (Oberteil Rot `#F07A6A`, Hose Dunkelblau `#4A5A85`), Kopf `Gray Bun`, Brille `Glasses 4`, Haut `#F1C9A8`; Mimiken `Old`, `Smile` (redet), `Serious` (redet streng), `Suspicious`, `Awe`, `Concerned|Serious` | `hilde` (Frau, älter) |
| Notar, um 55 | beurkundet (ohne Namen, ohne Rede, neutral; Namensschild „Notar“) | `standing/blazer-4` (Sakko Grau `#9A9AA8`, Hemd Weiß, schwarze Hose), Kopf `No Hair 1`, Brille `Glasses 2`, Haut `#B5835F`; Mimiken `Calm`, `Smile`, `Serious` | – |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge vergeben (`grep -rlw` über alle `.py/.md/.json` in `youtube/` ohne Themenplanung: Markus 0, Meinhardt 0 Treffer; „Ralf“ und „Jonas“ wegen Treffern verworfen) und nicht in der Koordinatorliste. Kein Genitiv eines Namens im Sprechtext („Auf Vorschlag von Frau Meinhardt“ nur auf der Karte). Die Figuren nennen keine Namen.
- **Stimmen nur aus dem Pool** stephan, hilde (christian und lucy nicht benötigt; stephan und christian daher nie in einer Szene). Vorfolgen 181 (christian, lucy) und 182 (william, laura_ruhig) ohne Überschneidung. Erzählerin/Lexi Carla ohne Rolle. Der Notar spricht nicht.
- Präfixe `MA_`/`MH_`/`NT_` (nie `ER_`). Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts. Fallszenen: Frau Meinhardt (links) blickt nach rechts zu Markus, Markus nach links; Notar blickt nach vorn bzw. bei der Unterschrift zu Markus. Tafelszenen: beide blicken zur Tafel; in der Folgenszene blickt Frau Meinhardt bei Markus’ Satz und bei ihrem eigenen Satz zu ihm (`_r`).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `MA_redet`, `MA_ernst`, `MH_redet`, `MH_streng` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Karikatur, keine „fiese“ Verkäuferin. **Keine weiteren Menschen im Bild.**
- **Abwechslung:** Posen nicht aus 180 (`easing-1`, `crossed_arms-1`, `resting-2`, `shirt-4`), 181 (`easing-2`, `resting-2`), 182 (`blazer-3`, `pointing_finger-2`, `resting-1`); keine Polka Dots. Kontaktbild `besetzung_183.png` im Master.
- Figuren-PNGs: `../peeps/op_183/` (70 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 180 (Strafverfahren), 181 (Warenverkehr/Reinheitsgebot), 182 (Fahrlässigkeit). 145 hatte den Notartermin als Hauptschauplatz mit Dialog über die Bedingung; hier ist der Notartermin nur eine kurze Station (stummer Notar, Tisch, Vertrag mit „Kaufpreis: 300.000 €“), Hauptschauplätze sind die Absprache vor dem Haus und die Tafelszenen mit der Gegenüberstellung „beurkundet 300.000 € / vereinbart 350.000 €“. Leitmotive: **weißer Umschlag** (Phosphor `envelope`) mit Pille „50.000 € bar“ als einziges Schwarzgeld-Symbol, **Vertrag** (Tabler `contract`) für 300.000 €, **Handschlag** (Phosphor `handshake`, grün) für 350.000 €, gelbes Haus und blaues Grundbuch wie in 145 (Rückbezug auf die Hauskauf-Folge). Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Die Absprache** `fall`–`ma1` | ab 0,0 s Haus links, Markus rechts mit Namensschild, Pille „Markus kauft ein Haus“; Frau Meinhardt bei „gehört“ mit Pille „Es gehört Frau Meinhardt“; Handschlag und „vereinbart: 350.000 €“ bei „einigen“/„dreihundertfünfzigtausend“; „vor dem Notartermin“; Blase Frau Meinhardt („In den Vertrag schreiben wir nur 300.000. Den Rest geben Sie mir bar.“), Blase Markus („Gut. Die 50.000 bekommen Sie vorher im Umschlag.“), Umschlag mit „50.000 € bar“ bei „Umschlag“ | ph:`house` (Gelb), `handshake` (Grün), `envelope` (Weiß) | `Fall · Der Hauskauf` → `Fall · Die Absprache` | – |
| **A2 Beim Notar** `umschl`–`eintr` | „So geschieht es: 50.000 € im Umschlag“ (Umschlag über Frau Meinhardt); Notar hinter dem Tisch bei „Notar“, Vertrag auf dem Tisch, „Kaufpreis: 300.000 €“; Stift-Symbol und „Beide unterschreiben“; Handschlag und „Auflassung im selben Termin“; „Wochen später“, Grundbuch und „Grundbuch: Markus ist Eigentümer“ | tabler:`contract`, `writing-sign`, `book-2` (Blau); ph:`envelope`, `handshake`; Tisch programmatisch (Gelb) | `Fall · Die Übergabe` → `Fall · Beim Notar` → `Fall · Wochen später` | `szene_183unterschrift_1` bei „unterschreiben“ |
| **A3 Die Frage** `frage`/`f2` | links „beurkundet: 300.000 €“ (Vertrag) und „vereinbart: 350.000 €“ (Handschlag), Fragezeichen bei „zu welchem Preis“; rechts Frau Meinhardt, Markus | tabler:`contract`, `question-mark`; ph:`handshake` | `Fall · Die Frage` | – |
| **B Sachverhalt** `sv` | Karte vollständig (42 px), ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Aufbau** `plan`–`s4` | 1. beurkundeter Vertrag (300.000 €) / 2. verdeckter Vertrag (350.000 €) / 3. Form / 4. Heilung zum Wort | ph:`house`, `handshake`; tabler:`contract`, `writing-sign`, `book-2` | `Scheingeschäft › Aufbau` | – |
| **D 1. beurkundeter Vertrag** `k1`–`nicht1` | Wortlautkarte § 117 Abs. 1 (3 Marker), Definition (V ZR 221/10 Rn. 6), ✓ „Keiner will 300.000 € als Preis.“, ✗ „beurkundeter Vertrag: nichtig“ | tabler:`contract`, `masks-theater`, `ban` | `1. Beurkundeter Vertrag › § 117 Abs. 1 BGB` → `› nichtig` | – |
| **E 2. verdeckter Vertrag** `k2`–`regeln` | Wortlautkarte § 117 Abs. 2 (3 Marker), ✓ „wirklich gewollt: Kauf zu 350.000 €“, „Wirksam? Erst, wenn er nach seinen eigenen Regeln besteht.“ | ph:`handshake`; tabler:`eye-off`, `checklist` | `2. Verdeckter Vertrag › § 117 Abs. 2 BGB` | – |
| **F 3. Form** `k3`–`nurs` | Wortlautkarte § 311b Abs. 1 S. 1 (2 Marker), Umfang der Beurkundungspflicht (V ZR 122/10 Rn. 6), ✗ „beurkundet: nur der Scheinpreis (300.000 €)“ | tabler:`writing-sign`, `checklist`, `contract` | `3. Form › § 311b Abs. 1 S. 1 BGB` → `› nur der Scheinpreis beurkundet` | – |
| **G Folge des Mangels** `w125`–`verw050` | Wortlautkarte § 125 S. 1 (2 Marker), ✗ „wahrer Kauf (350.000 €): zunächst formnichtig“ (V ZR 115/22 Rn. 8), Verweis „Kündigung per WhatsApp“ (Folge 050) | tabler:`file-x`, `ban`, `writing-sign` | `3. Form › § 125 S. 1 BGB` | – |
| **H 4. Heilung** `k4`/`verw145` | Wortlautkarte § 311b Abs. 1 S. 2 (3 Marker), ✓ „im Fall: Auflassung erklärt, Markus eingetragen“, Verweis „Hauskauf in drei Schritten“ (Folge 145) | tabler:`file-check`, `book-2`; ph:`handshake`, `house` | `4. Heilung › § 311b Abs. 1 S. 2 BGB` | – |
| **I Heilung: Inhalt und Grenzen** `ganz`–`nurf` | ✓ ganzer Inhalt mit dem wahren Preis; BGH 2024 (V ZR 115/22 Rn. 8); ✓ nur für die Zukunft (V ZR 122/10 Rn. 6); ✓ Einigung muss bei der Auflassung noch bestehen (V ZR 265/14 Rn. 29); ✗ andere Nichtigkeitsgründe (V ZR 115/22 Rn. 10) | ph:`handshake`; tabler:`gavel`, `clock`, `file-x` | `4. Heilung › ganzer Inhalt` → `› Grenzen` | – |
| **J Folgen** `vor`–`geb` | rote Box „Vor der Eintragung: Vertrag unwirksam“; Blase Markus („Dann will ich meine 50.000 zurück.“); ✗ keine Übereignungspflicht, ✓ Geld grundsätzlich zurück, § 812 (vgl. V ZR 122/10 Rn. 15); grüne Box „Nach der Eintragung: Vertrag geheilt“; Blase Frau Meinhardt („Der Vertrag war doch nichtig. Ich will mein Haus zurück!“); ✗ ohne Erfolg, ✓ gilt mit 350.000 €, ✓ beide gebunden, Markus Eigentümer | tabler:`arrow-back-up`, `book-2`; ph:`house` | `Folgen › vor der Eintragung` → `› nach der Eintragung` | – |
| **K Hinweise** `steuer`–`offen` | Steuer (ein Satz, § 370 AO, V ZR 115/22 Rn. 13); § 16a GwG: kein Bargeld, ✗ tilgt den Preis nicht, ✓ herausverlangen; BGH offengelassen (Rn. 12) | tabler:`receipt-tax`, `cash-banknote`, `question-mark`; ph:`envelope` | `Hinweis › Steuer` → `Hinweis › Barzahlungsverbot, § 16a GwG` | – |
| **L Abgrenzung** `abgr`–`beide` | Wortlautkarten § 118 (2 Marker) und § 116 (3 Marker), grüne Box „§ 117: Beide sind einig, das Erklärte soll nicht gelten.“ | tabler:`mood-wink`, `eye-off`, `masks-theater` | `Abgrenzung › § 118 BGB` → `› § 116 BGB` → `› § 117 BGB` | – |
| **M Klausurtipp** `tipp`–`t5` | hellgelbe Tafel, Lexi warnt; Reihenfolge 1.–4. zum Wort; „Geheilt wird nur der verdeckte Vertrag. Der Scheinvertrag bleibt nichtig.“ | Warnsymbol (Streamline Freehand) | `Klausurtipp · Reihenfolge` → `Klausurtipp · Was geheilt wird` | – |
| **N Klausurschema** `sch`–`kIII` | breite Karte, I. Scheingeschäft, II. verdecktes Geschäft (1. Form, 2. Formnichtigkeit, 3. Heilung), III. Ergebnis | – | `Klausurschema` → `› I. Scheingeschäft` → `› II. verdecktes Geschäft` → `› II. 1. Form` → `› II. 2. Formnichtigkeit` → `› II. 3. Heilung` → `› III. Ergebnis` | – |
| **O Merksatz** `merke`–`mk3` | Lexi erklärt, drei Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; keine Bewegungsanimation, kein Zoom.
**Blasen:** Stil C (`bausteine.blase`, stiller Rückfall per Assertion ausgeschlossen), wortgleich mit dem Gesprochenen, Zahlen in Ziffern.
**Darstellung Schwarzgeld:** nur Umschlag-Symbol mit Pille „50.000 € bar“, keine Geldscheine/Bündel, keine positive Wertung; der Notar ist neutral und weiß von nichts; Steuer nur ein Satz.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Markus kauft von Frau Meinhardt ein Haus. Die beiden einigen sich auf einen Kaufpreis von 350.000 €. Auf Vorschlag von Frau Meinhardt soll im Vertrag nur ein Preis von 300.000 € stehen; die restlichen 50.000 € gibt Markus ihr vorher bar im Umschlag.
>
> Beim Notar wird der Kaufvertrag mit einem Kaufpreis von 300.000 € beurkundet. Beide unterschreiben und erklären im selben Termin die Auflassung. Wochen später wird Markus als Eigentümer ins Grundbuch eingetragen.
>
> **Welcher Vertrag gilt, und zu welchem Preis?**
