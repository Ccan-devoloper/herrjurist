# Folge 064 · Abschleppfall: Musst du die Kosten zahlen? – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_064.py`](src/skript_064.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker-Fall, Übungsfall nach dem Hook des Themenplans), Beispielland Nordrhein-Westfalen. Frau Kaiser parkt „nur fünf Minuten“ ohne Parkausweis auf einem Parkplatz für schwerbehinderte Menschen vor der Apotheke; Herr Meier vom Ordnungsamt lässt abschleppen; nach zehn Minuten hängt das Auto am Haken; Kostenbescheid über 250 €. Ablauf: Fall → Frage → Sachverhalt → drei Ebenen und Landesrecht → Kostenbescheid (Ermächtigungsgrundlage, formell, Konnexität) → das Schild (Wortlaut Zeichen 314 mit Zusatzzeichen, § 12 II StVO) → Allgemeinverfügung, Sichtbarkeit, Wegfahrgebot → Ersatzvornahme (Wortlaut § 59 I VwVG NRW) → gestreckt oder sofort → Verhältnismäßigkeit (erforderlich, Wartezeit) → angemessen und Gegenfälle → Ergebnis und Kosten → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:47,8 (5.942 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Kaiser (KA), um 40 | Fahrerin und Halterin | Pose `standing/walking-2` (schwarzes Shirt, blaue Hose `#8DB3F2`), Kopf `Medium Straight` (dunkles Haar), Haut `#F1C6A5`; Mimiken `Smile` (froh, redet in A), `Concerned|Serious` (Sorge), `Rage|Serious` (Ärger, redet in C), `Suspicious` (denkt), `Tired` (müde) | `ela_froh` (Frau, jung) |
| Herr Meier (ME), um 55 | Verkehrsüberwachung im Ordnungsamt | Pose `standing/pointing_finger-1` (schwarze Kleidung, Zeigefinger), Kopf `Gray Short`, Haut `#E6B48F`; Mimiken `Calm`, `Serious` (ernst, redet), `Suspicious` (denkt) | `helmut` (Mann, älter) |
| Herr Becker (BE), um 30 | Abschleppdienst (im Auftrag der Stadt) | Pose `standing/crossed_arms-1` (orangefarbenes Arbeitsshirt `#F9A66C`), Kopf `Short 4`, Haut `#D9A07A`; Mimik `Calm` (ruhig, redet) | `niklas` (Mann, jung) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szene A: Frau Kaiser blickt nach rechts zur Apotheke (sie geht hinein); Szene B: Herr Meier blickt nach links zum Auto; Szene C: Frau Kaiser blickt nach links zum Abschleppwagen und zu Herrn Becker, Herr Becker nach rechts zu ihr; an Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `KA_redet`, `KA_aerger_redet`, `ME_redet`, `BE_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Stimmen nur aus dem Pool** ela_froh, helmut, niklas (julia nicht gebraucht; war in 061 besetzt); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Kaiser, Meier, Becker (nicht in der Liste früherer Namen).
- **Respekt:** Menschen mit Behinderung erscheinen nicht als Figuren, sondern nur über das amtliche Sinnbild am Schild; keine Witze, sachliche Begriffe („Parkplatz für schwerbehinderte Menschen“, „Berechtigte“). Frau Kaiser ist keine Bösewichtin: eilig, dann verärgert, am Ende nachdenklich.
- Figuren-PNGs: `../peeps/op_064/` (58 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 061 und die parallel entstehenden 062 (Einwilligung, Strafrecht) und 063 (Käuferrechte, Zivilrecht) mit eigenen Schauplätzen; 061: Wohnzimmer im Winter, Ordnungsamt am Schreibtisch, Haus mit Briefkasten. Hier: Straße vor einer Apotheke mit Parkschild (Zeichen 314 + Zusatzzeichen), Auto, Abschleppwagen mit Haken. Posen `walking-2`, `pointing_finger-1`, `crossed_arms-1` (für Fallfiguren) in 052–061 nicht als Fallfigur verwendet. Tageslicht-Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Vor der Apotheke** `fall`–`ka1` | Straße, Apotheke; Auto fährt ein und parkt; Schild; kein Parkausweis; Blase Kaiser | tabler:`building-store` (Grün), `car` (Rosa, fährt ein), `parking` (Blau) + fluent-hc:`wheelchair-symbol` (Weiß) am Mast | `Fall · Vor der Apotheke` (ab 0,0 s) | Straße · Auto fährt · parkt · Pille Parkplatz · Frau Kaiser · Schild · gut zu sehen · kein Parkausweis · Blase | Autotür (`szene_064tuer_1`), als das Auto steht |
| **B Das Ordnungsamt kommt** `meier`–`me1` | gleiche Straße ohne Frau Kaiser; Herr Meier prüft, bestellt Abschleppwagen; Blase Meier | wie A, fluent-hc:`mobile-phone` | `Fall · Das Ordnungsamt kommt` | Straße · Meier · 3 Pillen nacheinander · Telefon · bestellt · Blase | – |
| **C Am Haken** `zurueck`–`be1` | Frau Kaiser kommt zurück; Abschleppwagen mit Auto am Haken; Herr Becker; Blasen Kaiser und Becker | tabler:`car-crane` (Gelb), `car`, fluent-hc:`hook`, Kette als Tuschelinie | `Fall · Am Haken` | Kaiser · Abschleppwagen · am Haken · Becker · auf den Hof · Blase Kaiser · Blase Becker | Kette (`szene_064kette_1`), als der Abschleppwagen erscheint |
| **D Kostenbescheid** `bescheid`–`frage` | Bescheid, 250 €, Frage | tabler:`receipt-euro` | `Fall · Der Kostenbescheid` → `Fall · Muss Frau Kaiser zahlen?` | Bescheid · Betrag · Frage | – |
| **E Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s | – | `Sachverhalt` | 1 | – |
| **F Drei Ebenen** `ebenen`–`land` | drei Farbblöcke, Landesrecht; Kaiser | Schild, `car-crane`, `receipt-euro` je Ebene | `Prüfung · Drei Ebenen` → `Prüfung · Landesrecht, Beispiel Nordrhein-Westfalen` | Titel · 3 Blöcke · Landesrecht · Zeilen | – |
| **G Der Kostenbescheid** `egl`–`konnex` | § 77 VwVG NRW, Auslagen, Gebühr, ✓ formell, Block Konnexität | `receipt-euro`, `car-crane` | `1. Ermächtigungsgrundlage …` → `2. formell …` → `3. materiell › rechtmäßiges Abschleppen` | Zeilen · ✓ · Block | – |
| **H Das Schild** `gva`–`fuenf` | Wortlautkarte Anlage 3 StVO (6 Marker), Verbot für andere, § 12 II StVO | Schild | `3. materiell › a) Grundverwaltungsakt: das Schild` → `… › Parken, § 12 II StVO` | Karte · Marker · Zeilen | – |
| **I Verwaltungsakt** `va`–`polizei` | Allgemeinverfügung, Bekanntgabe, Sichtbarkeit, Umschau, Block Wegfahrgebot, § 80 analog | Schild, tabler:`eye`, `car` | `… › Allgemeinverfügung, Bekanntgabe` → `… › Wegfahrgebot, sofort vollziehbar` | Zeilen · Block | – |
| **J Ersatzvornahme** `ev`–`evname` | Wortlautkarte § 59 I 1 VwVG NRW (4 Marker), Block; Becker | `car-crane` | `3. materiell › b) Ersatzvornahme, § 59 I VwVG NRW` | Zeilen · Karte · Marker · Block | – |
| **K Zwei Wege** `wege`–`ua` | gestreckt, ✗ Festsetzung, Block NRW Sofortvollzug, ✓ Gefahr, andere Länder; Meier | `car-crane` | `… › gestreckt oder sofort?` → `… › sofortiger Vollzug, § 55 II VwVG NRW` | Zeilen · ✗ · Block · ✓ | – |
| **L Verhältnismäßigkeit** `vhm`–`hier` | Tafel zartgrün; ✓ geeignet, erforderlich, Risiko, Wartezeit, ✓ hier; Meier | tabler:`clock`, `car-crane` | `3. materiell › c) Verhältnismäßigkeit: geeignet` → `…: erforderlich` | Zeilen · ✓ · Block | – |
| **M Angemessen** `angem`–`sicht2` | Zweck, Berechtigte, Block ohne konkrete Behinderung, Gegenfälle; Kaiser | fluent-hc:`wheelchair-symbol`, tabler:`car` | `…: angemessen` → `… › Gegenfälle` | Zeilen · Block · Gegenfälle | – |
| **N Ergebnis** `erg`–`bussgeld` | Block rechtmäßig, Verhaltensstörerin, Auslagen/Gebühr, Block „muss zahlen“, Bußgeld | `receipt-euro` | `3. materiell › Ergebnis …` → `4. Kostenpflicht und Höhe` | Blöcke · Zeilen | – |
| **O Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Drei Ebenen trennen` | drei Hinweise | – |
| **P Klausurschema** `sch`–`q4` | Schema baut sich auf | – | `Klausurschema` | Titel · 1. · 2. · 3. · a) · b) · c) · 4. | – |
| **Q Merksatz** `merke`/`m2` | Lexi erklärt, Marker | – | `Merksatz` | Zeilen · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; das einfahrende Auto (Szene A) ist die einzige Bewegung.
**Geräusche:** zwei Handlungsgeräusche (Autotür, Kette am Haken), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Prüfpfad-Reihenfolge:** wie das Schema: 1. Ermächtigungsgrundlage, 2. formell, 3. materiell (a Grundverwaltungsakt, b Ersatzvornahme, c Verhältnismäßigkeit), 4. Kostenpflicht und Höhe.

## Sachverhaltskarte (Szene E, erscheint vollständig)

> Nordrhein-Westfalen: Frau Kaiser parkt ihr Auto ohne Parkausweis auf einem Parkplatz für schwerbehinderte Menschen vor einer Apotheke. Das Schild mit Zusatzzeichen ist gut zu sehen. „Nur 5 Minuten“, denkt sie. Herr Meier vom Ordnungsamt findet niemanden am Wagen und keinen Zettel. Er bestellt einen Abschleppwagen. Nach 10 Minuten hängt das Auto am Haken; Herr Becker vom Abschleppdienst bringt es auf den Hof. Die Stadt hört Frau Kaiser an und schickt einen Kostenbescheid über 250 €: Abschleppkosten und Verwaltungsgebühr.
>
> **Muss Frau Kaiser zahlen?**

Kein Fiktiv-Hinweis auf Karte, Tafeln oder im Sprechtext.

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen, Zahlen in Ziffern („Nur 5 Minuten …“, „5 Minuten weg!“). Tafeln schreiben Normen, Zahlen und Beträge in Ziffern („§ 77 Abs. 1 VwVG NRW“, „250 €“, „30 bis 180 €“), gesprochen als Wörter. Kleine graue Fundstellenzeilen (26 px) sind Belege, kein Sprechtext. Die Wortlautkarten (Anlage 3 StVO lfd. Nr. 7, § 59 Abs. 1 Satz 1 VwVG NRW) und die Zitatzeile § 12 Abs. 2 StVO sind als Zitat gekennzeichnet (Anführungszeichen, Normangabe).
