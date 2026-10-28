# Folge 053 · § 433 BGB: Die Pflichten aus dem Kaufvertrag – Prüfungsschema – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_053.py`](src/skript_053.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/Kaufrecht, Themenplan-Format „Schema“ (Leitentscheidung im Plan leer). Beispielfall nach dem Plan-Hook („Du kaufst ein gebrauchtes Fahrrad – was genau darfst du vom Verkäufer verlangen?“): Inga kauft am Freitag im Vorgarten von Herrn Lüders dessen altes Trekkingrad für 250 €, Abholung am Samstag. Am Samstag will sie das Rad mitnehmen und erst am Montag überweisen; Herr Lüders: „Erst das Geld, dann das Rad.“ Inga holt das Geld am Automaten, beide tauschen, Inga fährt davon. Ablauf: Fall → Frage → Sachverhalt → Wortlaut § 433 I → Pflichten des Verkäufers → Wortlaut § 433 II → Trennungsprinzip (Verweis Folge 005) → drei Schritte (Folge 006) → I. entstanden → II. nicht erloschen (Wortlaut § 362 I) → III. durchsetzbar (Wortlaut § 320 I 1) → Zug um Zug, § 322, Abnahme → Erfüllung beim Tausch → Ausblick Gefahrübergang (§§ 434 I, 446, 437) → Ausblick Verbrauchsgüterkauf (§§ 474, 475 I) → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 5:51,8 (4.904 Zeichen). Begründung in [`ABNAHME.md`](ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Inga (IN), um 22 | Käuferin | `standing/easing-1` (Jacke Grün `#8FD694`, Oberteil Weiß, schwarze Hose, weiße Schuhe), Kopf `Medium Bangs`, Haut `#E8B98F`; beim Davonfahren `sitting/bike` mit derselben Jacke und demselben Oberteil (rosa Rad der Pose = das gekaufte Rad); Mimiken `Calm`, `Smile` (redet), `Smile Big|Smile` (froh), `Serious` (denkt), `Suspicious` (überlegt), `Concerned|Serious` (Sorge) | `ela_froh` (Frau, jung) |
| Herr Lüders (LU), um 35 | Verkäufer (privat) | `standing/robot_dance-2` (offene Hand; schwarzes Oberteil, Hose Blau `#8DB3F2`, Schuhe `#3D3D58`), Kopf `Short 2`, Haut `#D9A07A`, kein Bart, keine Brille; Mimiken `Calm`, `Smile` (froh, redet), `Serious` (streng, redet; ernst), `Suspicious` (denkt), `Concerned|Serious` | `timo` (Mann, jung) |
| Lexi | Klausurtipp (warnt), Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Namen** mit eindeutig deutscher Aussprache, in keiner früheren Folge vergeben (geprüft gegen alle `skript_*.py`, `SZENENPLAN.md` und die Liste des Koordinators): Inga, Lüders. Kein Genitiv im Sprechtext („von Herrn Lüders“).
- Grundansicht gespiegelt (blickt nach links zur Tafel bzw. zu Herrn Lüders), `_r` blickt nach rechts (Herr Lüders in den Fallszenen zu Inga; Inga fährt nach rechts davon).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `IN_redet`, `LU_redet`, `LU_streng` (je links/rechts) und Lexi.
- **Stimmen nur aus dem Pool** timo, julia, otto, ela_froh; gebraucht: ela_froh (zuletzt 048), timo (zuletzt 050). julia (zuletzt 049) und otto („unsicher“) nicht gebraucht.
- Kopfprobe: `pointing_finger-2` für Herrn Lüders verworfen (andere Statur als `robot_dance-2`). Keine Prothesen-Posen, keine Bärte.
- Figuren-PNGs: `../peeps/op_053/` (54 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 052 (Anscheinsgefahr, Wohnung/Polizei), 051 (Diebstahl, Laden), 050 (Kündigung, Büro), 046 (Waschmaschine, Bad), 027 (Rad im WG-Keller, Fahrradladen), 014 (Kombi im Hof, E-Mails). Hier neu: Vorgarten mit Haus und Pflanze, Internetanzeige, Geldautomat an der Ecke, Davonfahren auf der Fahrrad-Pose. Das Rad ist ein anderes Motiv als in 027 (dort Leihe/Besitz); die Posen `easing-1`, `robot_dance-2` und `sitting/bike` erscheinen in 047–052 nicht.

## Szenen

Alle Szenen auf Cremegrund (Tag).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A1 Freitag** `fall`–`l1` | Inga allein (sucht), Anzeige im Internet, dann Vorgarten: Haus, Pflanze, Rad, Herr Lüders; Einigung | tabler:`search`, `device-mobile`, `home` (Gelb), `plant` (Grün); ph:`bicycle` (Rosa) | `Fall · Die Anzeige` (ab 0,0 s) → `Fall · Freitag im Vorgarten` | Suche · Anzeigekarte · Trekkingrad · 250 € · Vorgarten · Inga redet (Blase) · Lüders redet (Blase) | – |
| **A2 Samstag** `sams`–`frage2` | Vorgarten wie A1; Inga will mitnehmen (Blase, Handy), Lüders streng (Blase); Automat an der Ecke; Geld wandert zu Lüders, Schlüssel und Rad zu Inga; Inga fährt davon; Fragen | tabler:`building-bank`, `cash-banknote` (Grün), `key` (Gelb), `device-mobile`; ph:`bicycle` | `Fall · Samstag: das Rad gleich mitnehmen?` → `Fall · Der Tausch` → `Fall · Die Frage` | Samstag · Inga redet · Lüders denkt · Lüders redet streng · Automat · Geld in der Hand · Geld wandert · 250 € · Schlüssel/Rad wandern · Inga fährt davon · 3 Fragen | Geldscheine `szene_053geld_1`, Freilauf `szene_053freilauf_1` |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 9,8 s, ohne Fiktiv-Hinweis | – | `Sachverhalt` | 1 | – |
| **C § 433 I** `ansp`, `w1` | Tafel, Wortlautkarte mit Markern | ph:`bicycle`, tabler:`shield-check` | `Inga gegen Herrn Lüders · § 433 Abs. 1 BGB` → `§ 433 Abs. 1 BGB › Wortlaut` | Anspruchsgrundlage · Karte · 3 Marker · Satz 1 · Satz 2 | – |
| **D Pflichten des Verkäufers** `vk`–`rm` | Tafel; Rad wandert zu Inga | ph:`bicycle`, tabler:`certificate`, `tool`, `users` | `§ 433 Abs. 1 BGB › Pflichten des Verkäufers` → `§ 433 Abs. 1 Satz 2 BGB › frei von Mängeln` | 1. Übergabe (2) · 2. Übereignung · 3. ohne Mängel · Sachmangel (2) · Rechtsmangel (2) | – |
| **E § 433 II** `w2`–`ab` | Wortlautkarte, Pflichten der Käuferin | tabler:`cash-banknote`, ph:`bicycle` | `§ 433 Abs. 2 BGB › Pflichten des Käufers` | Karte · 2 Marker · Kaufpreis · Abnahme | – |
| **F Trennungsprinzip** `trenn`–`f005` | zwei Blöcke, Lila-Block, Verweis | tabler:`file-certificate`, `certificate` | `Trennungsprinzip · Verpflichtung und Übereignung` | Kaufvertrag · Übereignung · Eigentümerin · Trennungsprinzip · Verweis Folge 005 | – |
| **G Drei Schritte** `drei`–`s3` | drei Farbblöcke | tabler:`list-check` | `Aufbau · entstanden, nicht erloschen, durchsetzbar` | 3 | – |
| **H I. entstanden** `ent`–`kv_ok` | Tafel | tabler:`calendar-event` | `I. Anspruch entstanden › Kaufvertrag` | Einigung · Rad · Preis · ✓ · Block | – |
| **I II. nicht erloschen** `erl`–`erl_ok` | Wortlautkarte § 362 I | ph:`bicycle` | `II. nicht erloschen › Erfüllung, § 362 Abs. 1 BGB` | Karte · 2 Marker · ✗ Samstagmorgen · ✓ besteht | – |
| **J III. durchsetzbar** `dur`–`kein` | Wortlautkarte § 320 I 1 | ph:`bicycle`, tabler:`lock` | `III. durchsetzbar? › der Streit vom Samstag` → `III. durchsetzbar › Einrede, § 320 Abs. 1 BGB` | Streit · Karte · 3 Marker · ✗ Montag · ✓ zurückhalten · Schloss | – |
| **K Zug um Zug** `zug`–`abn` | Tafel | tabler:`cash-banknote`, `arrows-exchange`, `scale`; ph:`bicycle` | `III. durchsetzbar › Zug um Zug` → `› im Prozess, § 322 Abs. 1 BGB` → `› Abnahme keine Gegenleistung` | nicht vorleisten · Block · § 322 (2) · ✗ Abnahme (2) · BGH-Zeile | – |
| **L Erfüllung** `erf`–`abg` | Tafel; Rad und Schlüssel wandern zu Inga, Geld zu Lüders, Inga auf dem Rad | ph:`bicycle`, tabler:`key`, `cash-banknote` | `Erfüllung · der Tausch am Samstag` → `Erfüllung · beide Ansprüche erloschen, § 362 Abs. 1 BGB` | 3 Haken · Block · Abnahme, Inga auf dem Rad | – |
| **M Gefahrübergang** `gew`–`p437` | Tafel, Wortlautkarte § 434 I (gekürzt) | tabler:`calendar-event`, `tool` | `Ausblick · Gewährleistung ab Gefahrübergang` → `› Gefahrübergang, § 446 Satz 1 BGB` → `› Mängelrechte, § 437 BGB` | Frage · Karte · Marker · § 446 · Bremse · § 437 · BGH-Zeile | – |
| **N Verbrauchsgüterkauf** `vgk`–`priv` | Tafel | tabler:`building-store`, `home` | `Ausblick · Verbrauchsgüterkauf, § 474 Abs. 1 BGB` → `Ausblick · Sonderregeln, § 475 Abs. 1 BGB` | § 474 (2) · § 475 (3) · ✗ privat | – |
| **O Klausurtipp** `tipp`–`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · was wohin gehört` | 4 | – |
| **P Klausurschema** `sch`–`k4` | breite Karte, Aufbau Punkt für Punkt | – | `Klausurschema` → `Klausurschema › Kaufpreis, § 433 Abs. 2 BGB` | Titel · I. (2) · II. (2) · III. (2) · Kaufpreis | – |
| **Q Merksatz** `merke`, `m2` | Lexi erklärt, Merksatz mit Markern | – | `Merksatz` | 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 18 Folien; innerhalb harte Schnitte und Pops; Bewegungen nur, wo etwas übergeben wird (Geld, Schlüssel, Rad) und beim Davonfahren.
**Blasen:** wortgleich mit dem Gesprochenen (Zahlen als Wort).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Herr Lüders bietet sein altes Trekkingrad privat im Internet für 250 Euro an. Am Freitag sieht Inga es sich bei ihm an und sagt: „Das Rad nehme ich, für 250 Euro.“ Herr Lüders antwortet: „Abgemacht! Holen Sie es morgen ab.“
>
> Am Samstag will Inga das Rad gleich mitnehmen und das Geld erst am Montag überweisen. Herr Lüders lehnt ab: „Erst das Geld, dann das Rad.“ Inga holt das Geld am Automaten an der Ecke und zahlt bar. Herr Lüders gibt ihr das Rad und den Schlüssel für das Schloss, Inga fährt damit nach Hause.
>
> **Was durfte Inga verlangen, durfte Herr Lüders das Rad zurückhalten?**
