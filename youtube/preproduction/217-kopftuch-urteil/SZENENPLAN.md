# Folge 217 · Kopftuch-Urteil: Darf eine Lehrerin mit Kopftuch unterrichten? – Szenenplan

**Stand:** 06.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_217.py`](src/skript_217.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Grundrechte, Klassiker-Fall. Fiktiver Fall nach dem Muster von Kopftuch II. Ablauf laut Auftrag: 1. Hook (Zahlen als Ziffern: „1. Stunde“, „Klasse 8b · 27 Kinder“, „Ab dem 1. August“) → Fragen → Sachverhalt → 2. Art. 4 Abs. 1, 2 GG (Wortlautkarte), einheitliches Grundrecht, plausibles Glaubensgebot, schwerer Eingriff → 3. vorbehaltlos, kollidierendes Verfassungsrecht: negative Glaubensfreiheit, Art. 6 Abs. 2 und Art. 7 Abs. 1 GG (Wortlautkarten), Vater Röder → 4. Kopftuch I → 5. Kopftuch II: abstrakte vs. konkrete Gefahr, Gründe, Ausnahme gleichheitswidrig (Art. 33 Abs. 3 GG als Wortlautkarte, Art. 3 Abs. 3 GG), Ergebnis im Fall → 6. Rechtsreferendarin (BVerfGE 153, 1) → 7. § 34 Abs. 2 S. 4 BeamtStG (Wortlautkarte) → 8. Klausurtipp (Lexi) → Merksatz (Lexi). Hauptfilm 6:36,6.

**Darstellung (Vorgabe Koordinator):** Frau Sander ist eine sympathische, kompetente Lehrerin (Mimik freundlich, entschlossen, strahlend; nie verbissen). Kopftuch: das unveränderte Open-Peeps-Kopfteil **„Hijab“** der Bibliothek (schwarzes Tuch, farbiges Unterband) – würdig, kein eigenes Zeichnen nötig; Kontaktbild `out/figuren_bogen.png`, Mundzustände `out/mund_sa.png` geprüft. Keine religiösen Symbole im Bild (kein Kreuz, keine Kippa), also auch kein Gegeneinander-Ausspielen; der Vergleich mit dem staatlich aufgehängten Symbol steht nur als Text. Schulleiter und Land neutral (sachlich, bedauernd), der Vater mit legitimem Anliegen (besorgt, nicht feindselig). Reale Beschwerdeführerinnen weder benannt noch gezeigt; Rechtsreferendarin und Richterin als Funktionsrollen.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Sander (SA), um 30 | Mathematiklehrerin der 8b | `standing/blazer-3` (Blazer Lila `#B8A9F5`, Hose Dunkelblau `#3D3D58`), Kopf `Hijab` (Unterband Lila), Haut `#C98E66`; Mimiken `Smile` (ruhig), `Calm` (froh), `Smile Big|Smile` (strahlt), `Driven` (entschlossen, redet), `Solemn` (betroffen) | `lucy` (Frau, jung) |
| Herr Steffens (ST), um 55 | Schulleiter | `standing/shirt-4` (schwarzes Hemd der Pose, Hose Hellblau `#8DB3F2`), Kopf `Short 1` (Grau), Brille `Glasses 3`, Haut `#E3B08C`; Mimiken `Smile`, `Serious` (redet st1), `Smile` (redet st2), `Tired` (bedauert), `Calm` | `stephan` (Mann, mittel) |
| Herr Röder (RD), um 45 | Vater eines Schülers | `standing/crossed_arms-1` (Pullover Türkis `#7FD6D0`, schwarze Hose), Kopf `Short 4`, Haut `#F0C8A8`; Mimiken `Concerned|Serious`, `Serious` (redet), `Tired` (nachdenklich), `Smile` | `christian` (Mann, mittel) – nie in einer Szene mit Steffens |
| Kinder der 8b (K1–K3), um 13 | Schülerinnen und Schüler, K2 = Röders Sohn; sprechen nicht, ohne Namen | `resting-2` (Kopf `Buns`, Hose Rot), `walking-1` (Kopf `Short 2`, T-Shirt Gelb), `easing-1` (Kopf `Medium 2`, Jacke Blau); Höhe 68 % (Fallszene 299 px, Tafelszene 326 px); Mimiken `Smile`/`Cute`/`Calm` | – |
| Rechtsreferendarin (RF), um 27, Funktionsrolle | Referendarin im Gerichtssaal; spricht nicht | `standing/shirt-3` (Bluse Grün `#8FD694`, schwarze Hose), Kopf `Hijab` (Unterband Grün), Haut `#E0AC84`; Mimiken `Smile`, `Calm`, `Solemn` | – |
| Vorsitzende Richterin (RI), um 60, Funktionsrolle | Ausbilderin | `standing/pointing_finger-2` (schwarzes Oberteil wie eine Robe), Kopf `Gray Medium`, Brille `Glasses`, Haut `#F0CDB2`; Mimiken `Smile` (redet), `Serious` | `hilde` (Frau, älter) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Grundansicht gespiegelt (nach links), `_r` nach rechts. Klassenzimmer: Frau Sander (`_r`) blickt zu den Kindern rechts, die Kinder nach links zu ihr und zur Tafel. Büro: Steffens (`_r`) blickt zu Frau Sander, sie nach links zu ihm. Elternabend: Röder (`_r`) blickt zu seinem Sohn, der nach links blickt. Ergebnis: Steffens rechts blickt nach links zu Frau Sander. Gerichtssaal: Referendarin (`_r`) blickt zur Richterin, diese nach links. Tafelszenen: alle nach links zur Tafel.
- **Grundmimiken alle mit geschlossenem Mund**; Mundzustände a/o/e nur in `SA_redet`, `ST_redet`, `ST_redet2`, `RD_redet`, `RI_redet` (je links/rechts) und Lexi. 96 Figuren-PNGs in `../peeps/op_217/` (Drive-Master).
- **Namen:** Sander, Steffens, Röder – eindeutig deutsch, nicht auf der Koordinatorliste, nicht in `namen_reserviert.txt`, per `grep -rlw` über `*.py/*.md/*.csv/*.json` unter `youtube/` ohne Treffer; vor der Vertonung als „217: Sander, Steffens, Röder“ eingetragen.
- **Stimmen** nur aus dem Pool (lucy, stephan, christian, hilde); stephan und christian nie im selben Bild.

**Abweichung von den letzten Folgen:** Posen der Hauptfiguren nicht aus 212–215 (blazer-4, resting-2, robot_dance-3, easing-1, walking-2, shirt-1, easing-2, walking-1/-3, robot_dance-2, resting-1, crossed_arms-2); die Kinder sind Nebenfiguren. Keine Polka Dots, keine Bärte, keine Prothesen-Posen. Lila Blazer, grüne Bluse, türkiser Pullover neu gegenüber 212–214. Schauplätze **Klassenzimmer mit Schultafel und Pulten**, **Büro der Schulleitung**, **Elternabend vor der Tür der 8b**, **Gerichtssaal mit Richtertisch und Zuschauerbank** – neu gegenüber 212 (Kauf/Laden), 213 (Straße, Ordnungsamt), 214 (Bagatelle/Notwehr). Rückkehr ins Klassenzimmer (F4), weil die Geschichte mit dem Ergebnis dorthin zurückkehrt. Cremegrund durchgehend, Tageslicht.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Klassenzimmer** `fall`→`nie` | Schultafel (Formel „a² + b² = c²“, „Klasse 8b“ in Kreide), Frau Sander, drei Kinder hinter der Pultfront; Pillen „Gymnasium · Montag, 1. Stunde“ (ab 0,0 s), „Mathematik · Klasse 8b · 27 Kinder“, „Kopftuch: für sie ein Gebot ihres Glaubens“, „Streit darüber gab es nie.“ | programmatisch (Tafel, Pulte) | `Fall · Gymnasium, Montag, 1. Stunde` → `· Mathematik in der 8b` → `· Das Kopftuch` → `· Nie Streit` | 6 | Kreide an der Tafel (`szene_217kreide_1`) |
| **A2 Büro** `pause`→`ausn` | Fenster, Tisch mit Schulgesetz, Schulglocke; Steffens und Sander; Blasen st1, sa1; Pillen Ausnahme | tabler:`bell-ringing` (Gelb), `file-text` | `Fall · In der Pause` → `· Das neue Schulgesetz` → `· Das Verbot` → `· Frau Sander` → `· Die Ausnahme` | 6 | Pausengong (`szene_217gong_1`) |
| **A3 Die Fragen** `frage`→`echt` | Tafel mit zwei Fragen, gelber Block mit den drei Fundstellen; Sander, Steffens | tabler:`school`, `gavel`, `building-bank` | `Die Fragen · …` | 3 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s, ohne Fiktiv-Zusatz | – | `Sachverhalt` | 1 | – |
| **C1 Art. 4 GG** `art4`, `wl4` | Wortlautkarte Abs. 1, 2 mit Markern „Glaubens“, „Bekenntnisses“, „Religionsausübung“ | tabler:`book`, `heart` | `Art. 4 GG · Maßstab` → `· Wortlaut` | 5 | – |
| **C2 Schutzbereich, Eingriff** `einh`→`schwer` | einheitliches Grundrecht, Streit unerheblich, Haken „plausibel dargelegtes Glaubensgebot genügt“, roter Block „Beruf oder Glaubensgebot“, Haken „schwerer Eingriff“ | `book`, `heart`, `briefcase`, `alert-triangle` | `I. Schutzbereich › …` → `II. Eingriff › …` | 7 | – |
| **D1 Schranken** `vorb`→`drei` | Kreuz „Gesetzesvorbehalt: keiner“, kollidierendes Verfassungsrecht, gelber Block „hinreichend bestimmtes Gesetz“, drei Gegenpositionen | `book`, `scale`, `file-text`, `school` | `III. Rechtfertigung › …` | 5 | – |
| **D2 Gegenpositionen** `neg`→`neutral` | Wortlautkarten Art. 6 Abs. 2 (S. 1, „…“) und Art. 7 Abs. 1, Block „Auftrag religiös neutral erfüllen“; zwei Kinder | `school`, `home`, `building-bank`, `scale` | `III. Rechtfertigung › 1.–3.` | 6 | – |
| **D3 Elternabend** `roeder`, `rd1` | Tür „8b“, Röder und sein Sohn; Blase rd1 | – | `Fall · Herr Röder …` → `· Das Anliegen der Eltern` | 2 | – |
| **E Kopftuch I** `k1`→`folge` | Rubrum, Kreuz „ausdrückliches Gesetz: fehlte“, gelber Block, Haken Parlamentsvorbehalt, NRW | `building-bank`, `file-text`, `book`, `building-community`, `book-2` | `Kopftuch I (2003) · …` | 7 | – |
| **F1 Kopftuch II** `k2`→`konkr` | Rubrum, Kreuz „unverhältnismäßig“, grüner Block „hinreichend konkrete Gefahr“ | `building-bank`, `help-circle`, `alert-triangle` | `Kopftuch II (2015) › …` | 6 | – |
| **F2 Warum** `zurech`→`bezirk` | kein Zeichen des Staates, Haken Schüler, Kreuz Eltern, roter Block Störung; Röder und Sohn | `school`, `speakerphone`, `home`, `flame`, `map-2` | `Kopftuch II (2015) › …` |7 | – |
| **F3 Die Ausnahme** `priv`→`alle` | Wortlautkarte Art. 33 Abs. 3 S. 2, Kreuz „benachteiligt andere Religionen“, roter Block „nichtig“, gelber Block „unterschiedslos“ | `scale`, `circle-x`, `equal` | `Kopftuch II (2015) › …` | 7 | – |
| **F4 Ergebnis** `erg`→`st2` | zurück im Klassenzimmer; Pillen Ergebnis; Steffens Blase st2; Sander strahlt | – | `Ergebnis im Fall · …` | 3 | – |
| **G1 Gerichtssaal** `ref`→`ri1` | Zuschauerbank, Richtertisch, Richterin, Referendarin; Pillen Hessen 2020, Aufgaben; Blase ri1 | tabler:`gavel` | `Justiz · …` | 6 | – |
| **G2 BVerfGE 153, 1** `ref2`→`muss` | Haken „verfassungsgemäß“, hoheitlich, Robe/Ritual, Schule spiegelt, gelber Block „darf, muss nicht“; Referendarin, Richterin | `building-bank`, `gavel`, `school`, `scale` | `Rechtsreferendarin (2020) › …` | 6 | – |
| **H Heute** `heute`→`laender` | Wortlautkarte § 34 Abs. 2 S. 4 BeamtStG (Marker „objektiv“, „neutrale“), Fundstelle § 61 Abs. 2 BBG, Block Landesrecht | `book`, `scale`, `map-2` | `Heute · …` | 5 | – |
| **I Klausurtipp** `tipp`→`t4` | Prüfungsaufbau I.–III., Kern, Schule und Justiz trennen, Art. 33 Abs. 3; Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp › …` | 8 | – |
| **J Merksatz** `merke`→`m3` | Merksatz mit Markern „abstrakte“, „konkrete“, „strenger“, „alle“; Lexi erklärt | – | `Merksatz` | 7 | – |

**Bildhalte:** 103 eigenständige Bildhalte (Manifest), bei 6:36,6 ≈ 15,6 je Minute (Soll ≈ 9, also ≥ 60). Mundzustände getrennt.
**Übergänge:** stumme Schiebeblenden nur zwischen den 19 Folien; innerhalb harte Schnitte/Pops; kein Zoom.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Frau Sander unterrichtet an einem staatlichen Gymnasium Mathematik, unter anderem in der Klasse 8b mit 27 Kindern. Sie trägt ein Kopftuch, weil sie es als verpflichtendes Gebot ihres Glaubens versteht. Streit darüber gab es an der Schule nie.
>
> Das Land beschließt ein neues Schulgesetz: Lehrkräfte dürfen im Dienst an allen Schulen des Landes keine religiösen Zeichen tragen. Ausgenommen ist nur die Darstellung christlicher und abendländischer Bildungs- und Kulturwerte. Schulleiter Steffens teilt Frau Sander mit, dass das Verbot ab dem 1. August auch für sie gilt.
>
> Herr Röder, Vater eines Schülers der 8b, will, dass sein Sohn in der Schule nicht religiös beeinflusst wird.
>
> **Ist das pauschale Verbot mit dem Grundgesetz vereinbar?**
