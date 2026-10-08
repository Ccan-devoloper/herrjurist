# Folge 260 · Freiheitsberaubung § 239 im Schlaf: Muss das Opfer es merken? – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_260.py`](src/skript_260.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · StGB BT · Streitstand. Beispielfall nach dem Plan-Hook: Nachts in einer Altbauwohnung schließt Vermieter Herr Gerber das Zimmer seines schlafenden Untermieters Joscha von außen ab (kein anderer Ausgang), sicher, dass Joscha durchschläft; um 3 Uhr schließt er wieder auf, Joscha merkt nichts. Ablauf: Fall → Frage → Sachverhalt → § 239 Abs. 1 (Wortlautkarte), Rechtsgut Fortbewegungsfreiheit → 1. Ansicht potenzielle Fortbewegungsfreiheit (Argument Wortlaut) → 2. Ansicht aktuelle Fortbewegungsfreiheit (Argumente Versuchsstrafbarkeit seit 1998, Spezialfall der Nötigung) → Was sagt der BGH (Linie seit 1960, Urteil 5 StR 406/21: Täuschungsfall, kein Schlafender; Zitatkarte Rn. 21; Gründe Rn. 24–26) → Lösung nach der 1. Ansicht/BGH (vollendet) → Lösung nach der 2. Ansicht mit Versuch (Wortlautkarte § 239 Abs. 2; Tatentschluss fehlt) → Streitentscheid → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
**Länge:** Hauptfilm 5:45,4 (5.065 Zeichen Skript); Begründung in ABNAHME.md.
**Darstellung:** kein Gewaltbild. Joscha schläft ruhig im Bett (Augen zu, „zzz“), die Freiheitsberaubung ist nur ein Schloss-Icon an der Tür und ein Schlüssel; der Vermieter ist ein gewöhnlicher älterer Herr (Pullover, Brille), keine „fiese“ Figur.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Gerber (GE), um 60 | Vermieter, wohnt selbst in der Wohnung, schließt ab | Pose `standing/robot_dance-3` (Pullover Ocker `#C9A66B`, Hose Schiefergrau `#3D4A5C`; ausgestreckte Hand zur Tür), Kopf `No Hair 1`, Brille `Glasses 4`, Haut `#E3B38E`, kein Bart; Mimiken `Suspicious` (ärgert sich), `Serious`, `Smile` (redet; sicher), `Calm`, `Concerned\|Serious`, `Solemn` | `helmut` (Mann, älter) |
| Joscha (JO), um 25 | Untermieter, schläft | Pose `sitting/one_leg_up-2` (sitzt im Bett; T-Shirt Lila `#B8A9F5`, Hose der Pose schwarz, Beine unter einer programmatisch gezeichneten Bettdecke), Kopf `Short 5`, Haut `#F0C8A8`; Mimiken `Eyes Closed` (schläft), `Calm` (wach), `Smile` (redet), `Suspicious` | `niklas` (Mann, jung) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links), `_r` nach rechts. Fall: Joscha (links, im Zimmer) blickt nach rechts; Gerber (im Flur rechts) blickt nach links zur Tür. An den Tafeln: Joscha im Bett rechts der Tafel (blickt nach rechts, schläft), Gerber ganz rechts blickt nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `GE_redet`, `JO_redet` (je links/rechts) und Lexi. Keine Bärte, keine Polka Dots, keine Prothesen-Posen (`shirt-1/-2`, `blazer-1/-2` verworfen).
- **Namen** mit eindeutig deutscher Aussprache, nicht in der Koordinatorliste, nicht in `namen_reserviert.txt`: zuerst als „260: Gerber, Timo“ eingetragen; **Timo vor der Vertonung durch Joscha ersetzt** (gleichnamige Ensemble-Stimme `timo`, 67 Treffer unter `youtube/`), nachgetragen als „260: Joscha (ersetzt Timo …)“. `grep -rliw` über `youtube/` (*.py, *.md, *.csv, *.json, *.txt): Joscha 0 Treffer; Gerber 3 Treffer, aber nie als Figur (015: Fehlerkennung von „Gerda“; 244: als Kandidat verworfen). Kein Name im Genitiv („Joschas“ vor der Vertonung umformuliert).
- **Stimmen nur aus dem Pool:** helmut, niklas; `ela_froh` und `julia` nicht verwendet (keine Frauenrolle im Fall). Keine Stimme der Vorfolge 259 (william, laura_ruhig). Erzählerin/Lexi Carla ohne Rolle.
- Figuren-PNGs: `../peeps/op_260/` (44 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 257 (`shirt-4`, `easing-1`, `robot_dance-2`; Mehrfamilienhaus außen), 258 (`pointing_finger-2`, `crossed_arms-2`, `blazer-3`), 259 (`blazer-4`, `crossed_arms-1`, `resting-1`, `sitting/bike`) – keine dieser Posen; erstmals seit 038 eine sitzende Fallfigur, hier im Bett. Schauplatz neu: **Altbauwohnung bei Nacht im Schnitt** (links Joschas Zimmer mit Bett und Fenster, rechts Flur mit Zimmertür und Wanduhr). Nacht ist vom Fall verlangt; sie wird über das Fenster (Mond → Sonne) und die Uhr (1 → 3 → 7 Uhr) erzählt, der Grund bleibt Creme. Gegenüber 191 (Wohnung, Abschließen der Zimmertür bei Tag) und 038 (WG-Sofa) eigener Ort und eigene Requisiten.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Altbauwohnung bei Nacht** `fall`–`frage2` | Zimmer/Flur im Schnitt; Joscha schläft (zzz), Gerber kommt, Schlüssel, Schloss zu (rot), Pillen „von außen abgeschlossen“, „kein anderer Ausgang“, Blase Gerber, Pille „Gerber ist sicher …“, 3 Uhr Schloss auf (grün), Morgen: Sonne, Gerber weg, Joscha wach, Blase Joscha; zwei Fragepillen | tabler:`moon-stars`, `sun`, `clock-hour-1/-3/-7` (Weiß), `key` (Gelb), `lock` (Rot), `lock-open` (Grün), `zzz`; Wände, Tür, Bett, Decke, Boden programmatisch | `Fall · Nachts in der Altbauwohnung` (ab 0,0 s) → … → `Fall · Die Frage` (11 Stände) | 14 | Schlüssel im Schloss (`szene_260schloss_1`) beim Abschließen und beim Aufschließen |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C § 239 Abs. 1** `norm`–`kern` | **Wortlautkarte § 239 Abs. 1** (Marker „einsperrt“, „Freiheit beraubt“), Rechtsgut mit BGH Rn. 21, zwei Haken am Fall, gelber Block „Aber er will gar nicht …“; Joscha schläft im Bett | tabler:`book`, `walk`, `lock`, `zzz` | `§ 239 Abs. 1 StGB › …` (3) → `Streitstand · Was heißt Fortbewegungsfreiheit?` | 9 | – |
| **D 1. Ansicht** `pot`–`potarg` | grüner Block, Kriterium, zwei Haken (ohne Belang; auch Schlafende), Fundstelle Rn. 21/BGHSt 14, 314; Argument Wortlaut (Rn. 24) | tabler:`walk`, `door`, `zzz`, `book` | `Streitstand › 1. Ansicht … › …` (4) | 10 | – |
| **E 2. Ansicht** `akt`–`aktarg2` | oranger Block, Fundstelle Rn. 22, Definition, drei Argumente (1998, Vorverlegung, Spezialfall § 240) | tabler:`walk`, `door`, `book` | `Streitstand › 2. Ansicht … › …` (4) | 9 | – |
| **F Was sagt der BGH?** `bgh`–`bghfall` | Linie seit 1960, Urteil 8.6.2022, Block „Der Fall: kein Schlafender“, Sachverhalt der Entscheidung; Gerber hört zu | tabler:`building-bank`, `car`, `plane`, `masks-theater` | `Was sagt der BGH? › …` (4) | 11 | – |
| **G1 Kernsatz** `bghrn`, `bgherg` | **Zitatkarte Rn. 21** (Marker „potentielle persönliche Bewegungsfreiheit“, „ohne Belang“), Ergebnis der Entscheidung | tabler:`building-bank`, `masks-theater` | `Was sagt der BGH? › …` (2) | 6 | – |
| **G2 Gründe** `bghgr`–`bghvers` | 1.–4. mit Haken (Wortlaut, hohes Gut, Systematik mit Strafrahmen, Versuch: Schlüssel passt nicht) | tabler:`book`, `walk`, `scale`, `key` | `Was sagt der BGH? › Gründe …` (3) | 11 | – |
| **H Lösung 1. Ansicht** `loes`–`erg1` | I. 1. objektiv, I. 2. subjektiv, II./III., grüner Ergebnisblock; Joscha schläft, Gerber | tabler:`door`, `clock-hour-3`, `zzz`, `key`, `scale`, `lock` | `Lösung · …` → `Lösung › 1. Ansicht (BGH) › …` (6) | 10 | – |
| **I Lösung 2. Ansicht** `erg2`–`abw` | Kreuz Erfolg, **Wortlautkarte § 239 Abs. 2** (Marker „Versuch“), Tatentschluss, Kreuz, roter Ergebnisblock, grauer Abwandlungssatz | tabler:`zzz`, `book`, `bulb`, `lock-open`, `clock-hour-7` | `Lösung › 2. Ansicht › …` (5) | 10 | – |
| **J Streitentscheid** `streit`, `streit2` | zwei Ergebnisblöcke, Haken für die 1. Ansicht, grüner Block „Dann ist Gerber strafbar.“; Joscha wach | tabler:`arrows-split`, `scale` | `Streitentscheid · …` (2) | 5 | – |
| **K Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt (redet), vier Punkte | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` (4) | 7 | – |
| **L Schema** `sch`–`s7` | breite Karte I. (1., Merkmal mit Streit, 2.), II., III., Versuch, Verweis Folge 011 | – | `Schema › …` (8) | 9 | – |
| **M Merksatz** `merke`, `m2` | Lexi erklärt (redet), drei Marker | – | `Merksatz` | 5 | – |

**Blasen:** Stil C (Standard seit 02.10.2026; Assertion gegen stillen Rückfall auf Stil e). Gerber: „Bis 3 bleibt die Tür zu. / Merkt er ja eh nicht.“; Joscha: „Ah, ich hab super geschlafen!“ – wortgleich, Zahl als Ziffer.
**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops; keine Bewegung, kein Zoom.
**Geräusche:** ein Handlungsgeräusch (Schlüssel im Schloss, Freesound CC0 737284), zweimal am sichtbaren Ab- und Aufschließen; Freesound-API am 08.10.2026 über den Proxy HTTP 403, daher unveränderte Kopie der Datei aus Folge 191 unter eigenem Namen, Herkunft in `geraeusche_herkunft.json`.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Fluent Emoji High Contrast (MIT: Haken/Kreuz), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Wände, Tür, Fenster, Bett, Decke und Boden programmatisch aus Palettenflächen.
**Prüfpfad-Reihenfolge:** wie das Schema: Wortlaut/Rechtsgut → Streitstand (1., 2. Ansicht) → BGH → Lösung (I. 1. objektiv, I. 2. subjektiv, II./III.; Versuch) → Streitentscheid.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Kurz vor 1 Uhr nachts in einer Altbauwohnung: Untermieter Joscha schläft fest in seinem Zimmer. Sein Vermieter, Herr Gerber, wohnt in derselben Wohnung und ärgert sich über ihn. Er schließt das Zimmer von außen ab und steckt den Schlüssel ein; einen anderen Ausgang hat das Zimmer nicht. Gerber: „Bis 3 bleibt die Tür zu. Merkt er ja eh nicht.“
>
> Gerber ist sicher, dass Joscha bis zum Morgen durchschläft. Um 3 Uhr schließt er wieder auf. Joscha wacht um 7 Uhr auf und hat nichts bemerkt.
>
> **Hat Gerber sich wegen Freiheitsberaubung (§ 239 StGB) strafbar gemacht?**

Kein Fiktiv-Hinweis auf Karte, Tafeln oder im Sprechtext.

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen. Kleine graue Fundstellenzeilen (26 px) sind Belege, kein Sprechtext (auch die Strafrahmenzeile „§ 239 Abs. 1: bis 5 Jahre · § 240 Abs. 1: bis 3 Jahre“ zum gesprochenen „schwerer bestraft“). Die Wortlautkarten § 239 Abs. 1 und Abs. 2 werden vollständig vorgelesen; die Zitatkarte Rn. 21 steht wörtlich (Originalschreibung „potentielle“, Auslassung „[…]“) und wird wörtlich gesprochen („potenzielle“).
