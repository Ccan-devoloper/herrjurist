# Folge 133 · Für Freunde bürgen? Bürgschaft Schema §§ 765 ff. BGB – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_133.py`](src/skript_133.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Schema; Zivilrecht, weitere Vertragstypen. Fall nach dem Plan-Hook („Du bürgst für den Kredit deiner Schwester – plötzlich zahlt sie nicht mehr“): Hilke nimmt für eine neue Küche einen Bankkredit über 15.000 € auf (Zinsen 75 € im Monat). Herr Seibold von der Bank verlangt eine Bürgschaft, Hilke bittet ihre Schwester Marlies (netto 3.400 €). Marlies unterschreibt in der Bank eigenhändig „Ich bürge selbstschuldnerisch für den Kredit von Hilke über 15.000 Euro.“ Zwei Jahre später sind nach der Kündigung 9.000 € offen; die Bank verlangt sie von Marlies, die auf Hilke verweist.

Ablauf: Fall (Küche, Bank, Bitte, Urkunde, Zahlungsverlangen) → Frage (zahlen? zurückholen?) → Sachverhalt → Anspruch aus § 765 Abs. 1 (Wortlautkarte) und Aufbau → I. 1. Bürgschaftsvertrag, Schriftform (Wortlautkarte § 766 S. 1, 2; § 126 Abs. 1; § 350 HGB) → I. 2. keine Sittenwidrigkeit (BGH XI ZR 82/11 Rn. 9; verneint) → I. 3. Hauptschuld (Wortlautkarte § 767 Abs. 1 S. 1) und II. nicht erloschen → III. §§ 768, 770 → III. § 771 (Wortlautkarte) und Ausschluss § 773 Abs. 1 Nr. 1 (Wortlautkarte) → Ergebnis (Bühne) → IV. Rückgriff (Wortlautkarte § 774 Abs. 1 S. 1, Verweis § 426 Abs. 2, Auftrag § 670, BGH XI ZR 362/15 Rn. 20, 21) → Klausurtipp (Lexi; selbstschuldnerisch ≠ Gesamtschuld, BGH IX ZR 36/22 Rn. 17) → Klausurschema (progressiv) → Merksatz (Lexi).
**Länge:** Hauptfilm 6:22,8 (Sprachspur 382,8 s, 5.680 Zeichen Skript); Begründung für mehr als fünf Minuten in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Marlies (MA), um 45 | Bürgin, Schwester von Hilke | `standing/resting-1` (lila Pullover `#B8A9F5`, schwarze Hose, weiße Schuhe), Kopf `Medium 1` (dunkler Bob), Haut `#F2C9A5`; Mimiken `Calm`, `Serious` (redet), `Smile` (redet froh), `Smile Big|Smile`, `Concerned|Serious`, `Suspicious`, `Fear` | `sabrina` (Frau, mittel) |
| Hilke (MA-Schwester, HI), um 40 | Kreditnehmerin, Hauptschuldnerin | `standing/easing-1` (rote Jacke `#F07A6A` über gelbem Shirt `#F9D56E`, schwarze Hose), Kopf `Long Curly`, Haut `#EDBF9A`; `Calm` (auch redet), `Smile Big|Smile`, `Concerned|Serious`, `Tired` | `laura_ruhig` (Frau, mittel) |
| Herr Seibold (SE), um 55 | Mitarbeiter der Bank (Gläubigerseite) | `standing/blazer-2` (dunkelblauer Blazer `#3D4A7A`, weißes Shirt, schwarze Hose, Beinprothese), Kopf `Short 2`, Brille `Glasses 2`, Haut `#E3B48E`; `Calm`, `Serious` (redet), `Smile`, `Suspicious` | `william` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge vergeben (Koordinatorliste und `grep -rlw` über `youtube/`): Marlies, Hilke, Seibold. Verworfen: Regina (englische Lesart „Re-dschai-na“ möglich), Doris, Albers (Folge 006). Kein Genitiv eines Namens im Sprechtext („die Erklärung von Marlies“, „das Risiko von Marlies“).
- **Stimmen nur aus dem Pool** (`william`, `sabrina`, `marc`, `laura_ruhig`): `sabrina`, `laura_ruhig`, `william`; `marc` nicht nötig (nur ein Mann). `sabrina` und `laura_ruhig` liefen schon in 036 und 057 nebeneinander und sind gut unterscheidbar. Vorfolgen: 132 `niklas`, `julia`, `ela_froh`, `helmut`; 131 `hilde`, `lucy`, `christian`; 130 `marc`, `william`, `sabrina` (Überschneidung mit 130 durch den vorgegebenen Pool unvermeidbar).
- Präfixe `MA_`/`HI_`/`SE_` (nie `ER_`). Grundansicht gespiegelt (blickt nach links), `_r` blickt nach rechts.
- **Blickrichtung:** Küche: Hilke nach links zur Küche. Bank: Herr Seibold (links, hinter dem Schalter) nach rechts; Hilke nach links zu ihm, bei ihrer Frage an Marlies nach rechts; Marlies nach links zu Hilke. Zwei Jahre später: Seibold nach rechts zu Marlies, Marlies und Hilke nach links. Ergebnis: Seibold nach rechts, Marlies und Hilke nach links. Tafelszenen: beide Figuren nach links zur Tafel.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `MA_redet`, `MA_redetfroh`, `HI_redet`, `SE_redet` (je links/rechts) und Lexi. Keine weiteren Menschen im Bild.
- **Kein Klischee:** Die Bank bleibt sachlich (keine „fiese“ Gläubigerfigur, kein Logo), die Beinprothese ist selbstverständliches Merkmal des Bankmitarbeiters, keine Täterrolle. Keine Bärte, keine Karikatur.
- **Abwechslung:** Posen nicht aus 130 (`robot_dance-2`, `blazer-3`, `blazer-4`), 131 (`blazer-3`, `crossed_arms-1`, `shirt-3`), 132 (`robot_dance-3`, `easing-2`, `walking-3`, `shirt-2`, `shirt-1`) und nicht wie 099 (`shirt-4`, `walking-3`, `blazer-1`); Köpfe nicht aus 130–132; keine Polka Dots.
- Figuren-PNGs: `../peeps/op_133/` (64 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 130 (Trunkenheitsfahrt), 131 (EuGH-Klagearten), 132 (Organspende). Neu: Küche mit Kühlschrank, Herd und Mikrowelle; Bank mit blauem Schalter und förmlicher Bürgschaftsurkunde. **Wiederkehr der Bank:** Wie in Folge 099 wird die Bürgschaft bei der Bank erklärt; der Schauplatz folgt aus dem Fall (Gläubigerin ist eine Bank) und ist anders gebaut (Schalter statt Schreibtisch, gedruckte Urkunde mit Titel „Bürgschaft“ statt handschriftlichem Zettel, anderes Personal). Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Geräusch |
|---|---|---|---|---|
| **A1 Küche** `fall`–`zins` | ab 0,0 s: Küche, Hilke mit Namensschild, Pille „Hilke will eine neue Küche“; Bank + „Kredit: 15.000 €“, „Zinsen: 75 € im Monat“ | tabler:`fridge` (Weiß), `cooker` (Gelb), `microwave` (Weiß), `building-bank` (Blau) | `Fall · Der Kredit für die Küche` | – |
| **A2 Bank** `bank`–`an` | Schalter; Blase Seibold „Den Kredit bekommen Sie, / wenn jemand für Sie bürgt.“; Marlies kommt dazu; Blase Hilke „Marlies, bürgst du für mich?“; Blase Marlies „Klar, für dich mache ich das.“; „verdient netto 3.400 € im Monat“; Urkunde „Bürgschaft / Ich bürge selbstschuldnerisch für den / Kredit von Hilke über 15.000 Euro.“ zeilenweise zum Wort, Kugelschreiber bei „eigenhändig“, Unterschrift „Marlies“ nach dem Urkundentext, „Bank nimmt an“ | tabler:`building-bank`, `ballpen` (Gelb); Schalter als Karte (Blau) | `Fall · Die Bank will eine Bürgschaft` → `Fall · Marlies unterschreibt` | `szene_133unterschrift_1` bei der Unterschrift |
| **A3 Zwei Jahre später, Frage** `spaet`–`frage2` | Hilke besorgt, Kalender, „Bank kündigt“, „offen: 9.000 €“; Seibold, Brief, Marlies; Blase Seibold „Bitte zahlen Sie die 9.000 € / für Ihre Schwester.“; Blase Marlies „Dann holen Sie sich das Geld / doch erst bei Hilke!“; Pillen „Muss Marlies zahlen?“, „Bekommt sie ihr Geld von Hilke zurück?“ | tabler:`calendar`, `building-bank`, `mail` | `Fall · Zwei Jahre später` → `Fall · Die Frage` | `szene_133brief_1` bei „wendet“ |
| **B Sachverhalt** `sv` | Karte vollständig (35 px), ohne Fiktiv-Hinweis | – | `Sachverhalt` | – |
| **C Anspruch** `agl`–`aufbau` | „Bank gegen Marlies: 9.000 €“, Wortlautkarte § 765 Abs. 1 (2 Marker), I./II./III. zum Wort | tabler:`building-bank`, `file-certificate`, `list-numbers` | `Anspruch · Bank gegen Marlies, § 765 Abs. 1 BGB` → `Anspruch › Prüfungsaufbau` | – |
| **D1 I. 1.** `i1`–`hgb` | Bürgschaftsvertrag, ✓ Einigung, Wortlautkarte § 766 S. 1, 2 (2 Marker), nur Erklärung der Bürgin, ✓ eigenhändig (§ 126 Abs. 1), ✓ Form gewahrt, Ausnahme § 350 HGB | tabler:`file-certificate`, `signature`, `briefcase` | `I. Entstanden › 1. Bürgschaftsvertrag` → `› Schriftform, § 766 BGB` → `› Ausnahme, § 350 HGB` | – |
| **D2 I. 2.** `i2`–`s138b` | BGH-Formel krasse Überforderung (XI ZR 82/11 Rn. 9), Vermutung; Marlies 3.400 € / 75 €; ✗ keine krasse Überforderung, ✓ wirksam | tabler:`scale`, `wallet`, `coin-euro` | `I. Entstanden › 2. keine Sittenwidrigkeit, § 138 Abs. 1 BGB` → `2. Sittenwidrigkeit › im Fall` | – |
| **D3 I. 3., II.** `i3`–`erl` | Wortlautkarte § 767 Abs. 1 S. 1 (Marker), Darlehen 9.000 € fällig, ✓ entstanden; II. ✓ niemand hat gezahlt, Zahlung von Hilke → Marlies frei (IX ZR 36/22 Rn. 20) | tabler:`file-text`, `link`, `cash-banknote`, `receipt-euro` | `I. Entstanden › 3. Hauptschuld, § 767 BGB` → `II. Anspruch nicht erloschen` | – |
| **D4 III. §§ 768, 770** `iii`–`keine` | Einreden der Hauptschuldnerin (Verjährung), Anfechtbarkeit/Aufrechenbarkeit, ✗ keine Anhaltspunkte | tabler:`shield`, `arrows-exchange`, `circle-x` | `III. Durchsetzbar › §§ 768, 770 BGB` | – |
| **D5 § 771, § 773** `w771`–`s773` | Wortlautkarten § 771 S. 1 und § 773 Abs. 1 Nr. 1 (je 2 Marker), ✓ „selbstschuldnerisch“ unterschrieben, ✗ Bank muss nicht erst bei Hilke vollstrecken | tabler:`gavel`, `ballpen`, `file-certificate` | `III. Durchsetzbar › Einrede der Vorausklage, § 771 BGB` → `› Ausschluss, § 773 Abs. 1 Nr. 1 BGB` | – |
| **E Ergebnis** `erg` | Bühne: Block „Ergebnis: Marlies muss der Bank 9.000 € zahlen“, Geldschein und Pfeil von Marlies zur Bank | tabler:`building-bank`, `cash-banknote` (Grün) | `Ergebnis · Marlies muss 9.000 € zahlen` | – |
| **F IV. Rückgriff** `iv`–`risiko` | Wortlautkarte § 774 Abs. 1 S. 1 (2 Marker), wie § 426 Abs. 2, Auftrag → § 670, beide Wege nur einmal (XI ZR 362/15 Rn. 20), Insolvenzrisiko (Rn. 21) | tabler:`arrow-back-up`, `file-text`, `alert-triangle` | `IV. Rückgriff › § 774 Abs. 1 Satz 1 BGB` → `› Auftrag, § 670 BGB` → `› Risiko` | – |
| **G Klausurtipp** `tipp`–`tipp4` | hellgelbe Tafel, Lexi warnt; IX ZR 36/22 Rn. 17 | Warnsymbol (Streamline Freehand) | `Klausurtipp · selbstschuldnerisch ist keine Gesamtschuld` | – |
| **H Klausurschema** `sch`–`k4` | breite Karte, I. 1.–3., II., III. (Einreden, Ausschluss § 773), IV. Zeile für Zeile | – | `Klausurschema` → `› II. nicht erloschen` → `› III. durchsetzbar` → `› IV. Rückgriff` | – |
| **I Merksatz** `merke`–`m4` | Lexi erklärt, fünf Marker | – | `Merksatz` | – |

Die Zahl der Bildhalte je Szene steht im [`bildhalt_manifest.json`](bildhalt_manifest.json) und in der [`CUE-TIMELINE.md`](CUE-TIMELINE.md).

**Übergänge:** stumme Schiebeblenden nur zwischen den 15 Folien; innerhalb harte Schnitte und Pops; keine Bewegungsanimation.
**Blasen:** Stil C (`bausteine.blase`), wortgleich mit dem Gesprochenen, Beträge als Ziffern („9.000 €“).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Hilke will sich eine neue Küche kaufen und nimmt dafür bei einer Bank einen Kredit über 15.000 Euro auf; die Zinsen betragen 75 Euro im Monat. Herr Seibold von der Bank verlangt eine Bürgschaft.
>
> Hilke bittet ihre Schwester Marlies, für sie zu bürgen, und Marlies sagt zu. Marlies verdient netto 3.400 Euro im Monat. In der Bank unterschreibt sie eigenhändig eine Urkunde: „Ich bürge selbstschuldnerisch für den Kredit von Hilke über 15.000 Euro.“ Herr Seibold nimmt die Erklärung an.
>
> Zwei Jahre später zahlt Hilke die Raten nicht mehr. Die Bank kündigt den Kredit wirksam, 9.000 Euro sind offen. Sie verlangt das Geld von Marlies. Marlies meint, die Bank müsse es zuerst bei Hilke holen.
>
> **Muss Marlies zahlen, und kann sie das Geld von Hilke zurückverlangen?**
