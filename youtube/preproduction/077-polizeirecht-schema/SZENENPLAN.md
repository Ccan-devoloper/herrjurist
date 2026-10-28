# Folge 077 · Polizeirecht Schema: Standardmaßnahme vor Generalklausel – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_077.py`](src/skript_077.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen (Schema), Beispielfall nach dem Hook des Themenplans, Beispielland Nordrhein-Westfalen. Herr Schröder feiert nachts mit zwei Freunden im Stadtpark Geburtstag; Anwohnerin Frau Krämer ruft die Polizei; Frau Götz bittet um Ruhe, eine Stunde später ist die Box wieder laut; Platzverweis bis 6 Uhr: „Auf welcher Grundlage eigentlich?“ Ablauf: Fall → Frage → Sachverhalt → Aufbau und Landesrecht → 1. Ermächtigungsgrundlage (Reihenfolge, Versammlungsrecht, Wortlaut § 8 I, warum Standardmaßnahme zuerst, Wortlaut § 34 I 1) → 2. formell → 3. materiell (a Tatbestand: konkrete Gefahr, Wortlaut § 117 I OWiG und § 9 I LImschG NRW; b Adressat; c Rechtsfolge: Ermessen, Verhältnismäßigkeit, zeitlich und räumlich begrenzt, Abgrenzung Aufenthaltsverbot) → Ergebnis und Rechtsschutz → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:28,1 (5.592 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Schröder (SR), um 30 | feiert Geburtstag, Adressat des Platzverweises | Pose `standing/robot_dance-2` (schwarzes Shirt, grüne Hose `#8FD694`), Kopf `Short 2` (braun), Haut `#E8B894`; Mimiken `Smile` (froh, redet in B), `Suspicious` (denkt; fragt in C), `Concerned|Serious` (Sorge), `Tired` (müde) | `stephan` (Mann, mittel) |
| Frau Götz (GO), um 30 | Polizei (Streife) | Pose `standing/shirt-4` (schwarzes Hemd, dunkelblaue Hose `#3D4A7A` wie eine Uniform), Kopf `Bun 2`, Haut `#F0C8A8`; Mimiken `Calm` (ruhig, redet in B), `Serious` (ernst, redet in C), `Suspicious` (denkt) | `lucy` (Frau, jung) |
| Frau Krämer (KR), um 70 | Anwohnerin am Park | Pose `standing/crossed_arms-2` (schwarzes Oberteil, lila Hose), Kopf `Gray Medium` (grau), `Glasses 2`, Haut `#F2CDB0`; Mimiken `Concerned|Serious` (Sorge, redet in A), `Tired` (müde) | `hilde` (Frau, älter) |
| Freundin (FA), um 30 | feiert mit, sitzt im Gras, spricht nicht | Pose `sitting/closed_legs-1` (rosa Jacke), Kopf `Long Curly`, Haut `#C68C66`; `Smile`, `Concerned|Serious` | – |
| Freund (FB), um 30 | feiert mit, sitzt im Gras, spricht nicht | Pose `sitting/hands_back-1` (schwarzes Shirt, hellblaue Hose), Kopf `Short 5`, Haut `#D9A07A`; `Smile`, `Concerned|Serious` | – |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szenen A–C: Herr Schröder und die Freundin blicken nach rechts (zur Gruppe bzw. zur Polizistin), der Freund nach links zur Gruppe; Frau Götz und Frau Krämer blicken nach links zur Gruppe; an Tafeln alle nach links.
- **Alle Menschen im Bild sind Open-Peeps-Figuren** (Vorgabe 02.10.2026): auch die beiden Freunde; keine Emoji- oder Icon-Gesichter. Die Freunde tragen Namensschilder „Freundin“ und „Freund“ ab dem ersten Auftritt.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `SR_redet`, `SR_fragt`, `GO_redet`, `GO_ernst_redet`, `KR_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen.
- **Stimmen nur aus dem Pool:** stephan, lucy, hilde (christian nicht besetzt, damit nicht zwei ähnliche Männerstimmen in einer Szene); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Schröder, Götz, Krämer (nicht in der Liste früherer Namen, nicht in früheren Skripten).
- **Respekt:** Die Gruppe feiert Geburtstag, keine Alkohol-, Drogen- oder Herkunftsklischees; Herr Schröder fragt sachlich nach der Grundlage. Die Polizistin ist sachlich und höflich („Bitte …“).
- Figuren-PNGs: `../peeps/op_077/` (74 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 074 (Altstadt-Café, Verwaltungsgericht), 075 (Hofeinfahrt, Wohnzimmer), 076 (drei Kaufstationen), 064 (Straße vor der Apotheke, Abschleppwagen), 061 (Wohnzimmer im Winter). Hier neu: **Stadtpark bei Nacht** mit Bäumen, Mond, Musikbox, Haus der Anwohnerin am Parkrand und Streifenwagen. Posen `robot_dance-2`, `shirt-4` (für eine Polizistin), `sitting/closed_legs-1`, `sitting/hands_back-1` in 074–076 nicht verwendet. **Nacht** nur in den Fallszenen A–C, weil der Fall in der Nachtruhe spielt (§ 9 LImschG NRW, Platzverweis bis 6 Uhr); Tafeln auf Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Geburtstag im Park** `fall`–`kr1` (Nacht) | Stadtpark; Gruppe; Box läuft; Frau Krämer am Haus ruft an; Blase Krämer | tabler:`trees` (Grün), `moon-stars` (Gelb), `music` (Gelb); ph:`building-apartment` (Blau/Gelb), `speaker-hifi` (Lila); fluent-hc:`birthday-cake`, `mobile-phone` | `Fall · Geburtstag im Park` (ab 0,0 s) | Park · Gruppe · Geburtstag · Box laut · singen · Krämer · ruft an · Mitternacht · wohnt am Park · Blase | – |
| **B Die Polizei kommt** `goetz`–`laut` (Nacht) | Streifenwagen, Frau Götz bittet um Ruhe; Schröder sagt zu; Box leise; eine Stunde später Krämer ruft wieder an; Box wieder laut | wie A, ph:`police-car` (Weiß/Blau) | `Fall · Die Polizei kommt` | Götz · Blase Götz · Blase Schröder · leiser · 1 Stunde später · Krämer · ruft wieder an · laut · aufgedreht | Autotür (`szene_077tuer_1`) beim Streifenwagen |
| **C Der Platzverweis** `zurueck`–`sch2` (Nacht) | Frau Götz kommt zurück, Platzverweis bis 6 Uhr; Freunde besorgt; Schröder fragt nach der Grundlage | wie B | `Fall · Der Platzverweis` | Götz ernst · Blase Götz · Pille bis 6 Uhr · Freunde besorgt · Blase Schröder | Autotür (`szene_077tuer_1`) |
| **D Frage** `frage` | Frage mit Schröder und Götz | tabler:`trees` | `Fall · War der Platzverweis rechtmäßig?` | Frage | – |
| **E Sachverhalt** `sv` | Karte vollständig, ≈ 9,9 s | – | `Sachverhalt` | 1 | – |
| **F Aufbau** `aufbau`–`land` | 3 Farbblöcke, Landesrecht; Götz | ph:`police-car` | `Prüfung · Aufbau` → `Prüfung · Landesrecht, Beispiel Nordrhein-Westfalen` | Titel · 3 Blöcke · Zeilen | – |
| **G Reihenfolge** `egl`–`vers` | Grundlage nötig, Treppe Spezialgesetz/Standardmaßnahme/Generalklausel, Versammlungsrecht ✗; Schröder | tabler:`list-numbers`, fluent-hc:`birthday-cake` | `1. Ermächtigungsgrundlage › Reihenfolge` → `… › Spezialgesetz? Versammlungsrecht` | Zeilen · Blöcke · ✗ | – |
| **H Generalklausel** `wl8`–`soweit` | Wortlautkarte § 8 I (4 Marker), Block „Standardmaßnahme vor Generalklausel“; Götz | tabler:`list-numbers` | `… › Generalklausel, § 8 I PolG NRW` | Karte · Marker · Block | – |
| **I Warum?** `warum`–`sicher` | Grundrechte, Grenzen, Bestimmtheit; Generalklausel für Ungeregeltes; „Musik leiser“ ✓; Box: Sicherstellung; Götz | ph:`speaker-hifi` | `… › Warum Standardmaßnahme zuerst?` | Zeilen · ✓ | – |
| **J Platzverweis** `wl34`–`egl34` | Wortlautkarte § 34 I 1 (3 Marker), Block Ermächtigungsgrundlage ✓; Götz | tabler:`map-pin` | `… › Platzverweis, § 34 I 1 PolG NRW` | Karte · Marker · Block | – |
| **K Formell** `formell`–`form` | Ordnungsamt/§ 24o OBG, Eilzuständigkeit ✓, Anhörung ✓, Form ✓; Götz | ph:`building-office`, tabler:`moon-stars`, ph:`police-car` | `2. formell › Zuständigkeit` → `… › Verfahren und Form` | Zeilen · ✓ | – |
| **L Tatbestand** `mat`–`konkret` | konkrete Gefahr, öffentliche Sicherheit, Definition; Krämer | tabler:`alert-triangle` | `3. materiell › a) Tatbestand: konkrete Gefahr` | Zeilen | – |
| **M Lärm** `owi`–`gja` | Wortlautkarten § 117 I OWiG (4 Marker) und § 9 I LImschG NRW (2 Marker), Subsumtion, Block ✓; Krämer | ph:`speaker-hifi`, tabler:`music`, `moon-stars` | `… › Lärm, § 117 OWiG, § 9 LImschG NRW` | Karten · Marker · Zeilen · Block | – |
| **N Adressat** `adr`–`alle` | § 4 I (Zitat), Block Verhaltensstörer, alle 3 ✓; Gruppe rechts | – | `3. materiell › b) Adressat: Verhaltensstörer, § 4 I PolG NRW` | Zeilen · Block · ✓ | – |
| **O Rechtsfolge** `rf`–`angem` | Ermessen, Verhältnismäßigkeit, geeignet/erforderlich/angemessen ✓; Götz | tabler:`scale` | `3. materiell › c) Rechtsfolge: Ermessen, Verhältnismäßigkeit` | Zeilen · ✓ | – |
| **P Grenzen** `grenze`–`abgr` | vorübergehend (bis 6 Uhr ✓), Ort (Park ✓), Abgrenzung § 34 II; Schröder | tabler:`clock-hour-6`, `map-pin`, `calendar` | `… › zeitlich und räumlich begrenzt` → `… › Abgrenzung: Aufenthaltsverbot, § 34 II` | Zeilen · ✓ | – |
| **Q Ergebnis** `erg`–`rs` | Block rechtmäßig, Rechtsschutz FFK, Verweis Klagearten; Schröder | tabler:`gavel` | `Ergebnis` → `Ergebnis › Rechtsschutz` | Block · Zeilen | – |
| **R Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Generalklausel zuletzt` | drei Hinweise | – |
| **S Klausurschema** `sch`–`q3c` | Schema baut sich auf | – | `Klausurschema` | Titel · 1. · 2. · 3. · a) · b) · c) | – |
| **T Merksatz** `merke`/`m2` | Lexi erklärt, 5 Marker | – | `Merksatz` | Zeilen · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 20 Folien; innerhalb harte Schnitte und Pops; keine Bewegung, kein Zoom.
**Geräusche:** ein Handlungsgeräusch (Autotür beim Streifenwagen, zweimal), Freesound CC0, Herkunft in `geraeusche_herkunft.json`.
**Prüfpfad-Reihenfolge:** wie das Schema: 1. Ermächtigungsgrundlage, 2. formell, 3. materiell (a Tatbestand, b Adressat, c Rechtsfolge), Ergebnis.

## Sachverhaltskarte (Szene E, erscheint vollständig)

> Nordrhein-Westfalen, Samstagnacht: Herr Schröder feiert mit zwei Freunden im Stadtpark Geburtstag. Eine Musikbox läuft laut, die 3 singen mit. Gegen Mitternacht ruft Anwohnerin Frau Krämer die Polizei: Die Musik dröhnt bis in ihr Schlafzimmer. Frau Götz von der Polizei bittet die Gruppe, die Musik leiser zu machen. 1 Stunde später ist die Box wieder voll aufgedreht. Das Ordnungsamt ist nachts nicht erreichbar. Frau Götz verweist alle 3 bis 6 Uhr morgens aus dem Park. Herr Schröder fragt: „Auf welcher Grundlage eigentlich?“
>
> **War der Platzverweis rechtmäßig?**

Kein Fiktiv-Hinweis auf Karte, Tafeln oder im Sprechtext.

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen, Zahlen in Ziffern („… bis morgen früh um 6.“). Tafeln schreiben Normen, Zahlen und Uhrzeiten in Ziffern („§ 34 Abs. 1 Satz 1“, „bis 6 Uhr“, „3 Monate“), gesprochen als Wörter. Kleine graue Fundstellenzeilen (26 px) sind Belege, kein Sprechtext. Die Wortlautkarten (§ 8 Abs. 1 und § 34 Abs. 1 Satz 1 PolG NRW, § 117 Abs. 1 OWiG, § 9 Abs. 1 LImschG NRW) und die Zitatzeile § 4 Abs. 1 PolG NRW sind als Zitat gekennzeichnet (Anführungszeichen, Normangabe).
