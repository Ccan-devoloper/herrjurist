# Folge 270 · Amtsgericht Zuständigkeit 2026: Streitwert bis 10.000 Euro – Szenenplan

**Format:** Fr · 2. Examen · ZPO · Sonderlage (Rechtsänderung). Fall nach dem Plan-Hook: Tischlermeister Herr Haberkorn hat bei einem Kunden eine Holztreppe eingebaut; die Rechnung über 9.200 € ist offen. Muss er zum Landgericht und damit zwingend zum Anwalt? Seine Tochter Irmela (Referendarin) antwortet; Frau Bergfeld aus dem Büro erinnert an die Klage vom Dezember (7.000 €, Eingang beim LG 10.12.2025, Zustellung 8.1.2026). Ablauf laut Auftrag: Hook mit Zahlen → § 23 Nr. 1 GVG (Wortlautkarte) und § 71 Abs. 1 GVG (Wortlautkarte), Reform → Rechenbeispiel 9.200 € (§§ 4, 5 ZPO) → § 78 Abs. 1 S. 1 ZPO (Wortlautkarte), § 79 ZPO → Altverfahren § 44 S. 1 EGGVG (Wortlautkarte), § 261 Abs. 3 Nr. 2 ZPO (Wortlautkarte), § 506 ZPO → § 495a ZPO (Wortlautkarte) → Sonderzuständigkeiten (Tafel) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Belege: [`RECHTSSTAND.md`](RECHTSSTAND.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Haberkorn (HA), um 55 | Tischlermeister, Inhaber der (erfundenen) Tischlerei Haberkorn; sympathisch, besorgt, dann erleichtert | `standing/resting-1` (Arbeitspullover Moosgrün `#6B8F71`, schwarze Hose der Pose), Kopf `Short 4`, Haut `#E3B48C`, kein Bart; Mimiken Calm, Concerned\|Serious, Suspicious, Smile; redet (Concerned\|Serious), redetfroh (Smile) | `christian` (Mann, mittel) |
| Irmela (IR), Mitte 20 | Referendarin, seine Tochter | `standing/robot_dance-2` (schwarzes Oberteil, Hose Lila `#B8A9F5`), Kopf `Bangs 2`, Haut `#F1C9A5`; Calm, Suspicious, Smile, Serious; redet (Smile) | `lucy` (Frau, jung) |
| Frau Bergfeld (BE), um 65 | Büro der Tischlerei | `standing/blazer-4` (Blazer Türkis `#7FD6D0`, Hose `#3D4A5C`), Kopf `Gray Medium` (Haar `#C8C8C8`), Brille `Glasses 2`, Haut `#EDC3A0`; Calm, Suspicious, Concerned\|Serious, Smile; redet (Serious) | `hilde` (Frau, älter) |
| Lexi | Moderatorin (Klausurtipp, Merksatz) | `lexi.py` (`robot_dance-1`, Bun 2, Glasses 5, gelb) | Carla (Erzählerin) |

Stimmenpool laut Auftrag: stephan, hilde, christian, lucy; `stephan` nicht verwendet (also nie stephan und christian in einer Szene). Grundmimiken alle mit geschlossenem Mund; Mundzustände a/o/e nur für die sprechenden Ansichten. Präfixe HA_/IR_/BE_ (nie ER_).

**Namen:** Haberkorn, Irmela, Bergfeld – eindeutig deutsch, nicht in der Koordinatorliste, nicht in `namen_reserviert.txt`, `rg -w` unter `youtube/` 0 Treffer; vor der Vertonung als „270: Haberkorn, Irmela, Bergfeld“ eingetragen. Kein Genitiv.

**Abweichung von den letzten Folgen:** 266 (`crossed_arms-1`, `blazer-2`, `shirt-3`), 267 (`robot_dance-3`, `walking-3`, `polka_dots`, `easing-2`), 269 (`blazer-1`, `pointing_finger-1`, `resting-2`): Posen `resting-1`, `robot_dance-2`, `blazer-4` dort nicht verwendet; keine Polka Dots, keine Bärte, keine Prothesen-Posen. Schauplatz **Tischlerwerkstatt** (Werkbank, Holz, Werkzeugbrett, Tür zum Büro) – neu gegenüber 262/265 (Autohof, Kfz-Werkstatt; deshalb bewusst kein Kfz-Fall), 267 und 269 (Diskothek/Ordnungsamt). Die Holztreppe erscheint nur im Rückblick-Feld („beim Kunden eingebaut“).

**Darstellung:** Handwerker sympathisch; Kunde erscheint nicht als Person. **Kein Richterhammer** (Gericht als `building-bank`), kein Hammer in der Werkstatt (Verwechslungsgefahr), stattdessen Werkzeug-Icon, Zollstock, Lineal. Keine echten Firmen.

## Szenen

| Szene (Cues) | Ort / Bild | Requisiten (Iconset:Name) | Prüfpfad | Bildhalte (Auswahl) | Geräusch |
|---|---|---|---|---|---|
| **A Tischlerei** `fall`→`frage3` | Werkstatt: Fenster, Werkzeugbrett, Holz, Werkbank (programmatisch), Tür; HA links (blickt nach rechts), IR Mitte, BE rechts (blicken nach links) | tabler:`window`, `tools`, `ruler-measure`, `wood`, `ruler-2`, `door`, `receipt-euro`, `stairs`, `home` | `Fall · In der Tischlerei` (ab 0,0 s) → `… Muss ich zum Landgericht?` → `… Die Klage vom Dezember` → `Einstieg · Die Frage` | Titelpille; Rechnung hebt sich (0,35 s); „Tischlermeister“; Rückblick „Holztreppe“/„beim Kunden eingebaut“; „Rechnung: 9.200 €“; Irmela + „Referendarin“; Blase HA; Blase IR; Frau Bergfeld + „Büro“; Blase BE; Hook-Pillen „10.000 € statt 5.000 €“, „die neue Wertgrenze“; drei Fragen | Papier (`szene_270rechnung_1`) |
| **B Sachverhalt** `sv` | Karte | – | `Sachverhalt` | Karte vollständig, ≈ 10 s | – |
| **C1 § 23 Nr. 1 GVG** `w23`→`bis` | Tafel, IR rechts | tabler:`building-bank`, `coin-euro` | `§ 23 Nr. 1 GVG › Wertgrenze 10.000 €` → `… 10.000 € gehören noch dazu` | Wortlautkarte; fünf Marker zum Wort; Block „Genau 10.000 € …“ mit Haken | – |
| **C2 § 71 Abs. 1 GVG** `w71`, `w71b` | Tafel, HA | `building-bank` | `§ 71 Abs. 1 GVG › sonst das Landgericht` | Blöcke AG/LG, Wortlautkarte, drei Marker | – |
| **C3 Reform** `reform`→`kraft` | Tafel, HA | `calendar-event` | `Reform › bis 31.12.2025: 5.000 €` → `… Gesetz vom 8.12.2025` → `… seit 1.1.2026: 10.000 €` | 5.000 € → Pfeil → 10.000 €; Gesetzestitel + BGBl.; „in Kraft seit 1.1.2026“ | – |
| **D1 Rechenbeispiel** `rech`→`r6` | Tafel, HA | `receipt-euro`, `building-bank`, `receipt-2` | `Rechenbeispiel › 9.200 € Werklohn` → `… ohne Nebenforderungen, § 4 ZPO` → `… Amtsgericht` → `… mehrere Ansprüche, § 5 ZPO` | Zeilen zum Wort, Haken, Kreuz „über 10.000 €: Landgericht“ | – |
| **D2 Anwaltszwang** `w78`→`ir2` | Tafel, HA und IR | – | `§ 78 Abs. 1 ZPO › Anwaltszwang?` → `… nicht am Amtsgericht` → `§ 79 Abs. 1 ZPO › Partei führt den Prozess selbst` | Wortlautkarte, Kreuz/Haken, Blasen HA und IR | – |
| **E1 Altverfahren § 44 EGGVG** `alt`→`be2` | Tafel, BE | `calendar-event` | `Altverfahren › die Klage vom Dezember` → `… § 44 EGGVG` → `… anhängig = eingegangen` → `… alte Grenze: 5.000 €` | Daten-Pillen, Wortlautkarte, „anhängig = …“, Blase BE | – |
| **E2 perpetuatio fori** `w261`→`pf3` | Tafel, IR | `coin-euro`, `building-bank` | `Altverfahren › § 261 Abs. 3 Nr. 2 ZPO` → `… perpetuatio fori` | Wortlautkarte, Beispiel Teilzahlung, „ab Rechtshängigkeit = Zustellung“ | – |
| **E3 § 506 ZPO** `w506` | Tafel, HA | `arrows-exchange` | `Ausnahme › § 506 ZPO: Klageerweiterung` | AG-Block → Pfeil → LG-Block | – |
| **F § 495a ZPO** `w495`→`frei` | Tafel, BE | `file-text`, `receipt-euro` | `Abgrenzung › § 495a ZPO` → `… keine Zuständigkeitsnorm` → `… 800 €: Amtsgericht, freieres Verfahren` | Wortlautkarte, Haken/Kreuz, 600 → 1.000 €, Beispiel 800 € | – |
| **G Sonderzuständigkeiten** `sonder`→`wert` | Tafel, HA | `home`, `deer`, `fence`, `home-cog`, `stethoscope`, `news`, `file-text`, `stairs` | `Sonderzuständigkeiten › ohne Rücksicht auf den Wert` → `… § 23 Nr. 2 GVG` → `… § 71 Abs. 2 GVG` → `… beim Werklohn zählt der Wert` | je Beispiel eine Zeile und ein Requisit zum Wort | – |
| **H Klausurtipp** `tipp`→`tipp3` | Tafel hellgelb, Lexi warnt | tabler:`books`, `calendar-event`; Warnsymbol Streamline Freehand | `Klausurtipp · alte Skripte, Eingangsstempel` | Zeilen zum Wort | – |
| **I Schema** `sch`→`k5a` | breite Karte | – | `Schema · …` → `Schema › I. … V. perpetuatio fori` | neun Zeilen progressiv | – |
| **J Merksatz** `merke`, `m2` | Karte, Lexi erklärt | – | `Merksatz` | sechs Marker | – |

## Sachverhaltskarte (wörtlich)

> Tischlermeister Haberkorn hat bei einem Kunden eine Holztreppe eingebaut. Seine Rechnung über 9.200 € Werklohn ist offen. Er will klagen und fragt, ob er zum Landgericht und damit zwingend zu einem Anwalt muss.
> Frau Bergfeld aus dem Büro erinnert an eine ältere Klage der Tischlerei gegen einen anderen Kunden über 7.000 €: eingegangen beim Landgericht am 10.12.2025, zugestellt am 8.1.2026.
> Fragen: Welches Gericht ist für die 9.200 € zuständig, braucht er einen Anwalt? Und was gilt für die Klage vom Dezember?

Kein Fiktiv-Hinweis auf Tafeln oder im Sprechtext.
