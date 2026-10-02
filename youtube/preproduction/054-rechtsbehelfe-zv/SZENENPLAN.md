# Folge 054 · Rechtsbehelfe Zwangsvollstreckung: §§ 766, 767, 771, 805 ZPO – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_054.py`](src/skript_054.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · 2. Examen · ZV, Themenplan-Format „Schema“. Ein Beispielfall nach dem Plan-Hook trägt das Schema: Frau Hollmann (Autowerkstatt) hat gegen Herrn Steinbach ein rechtskräftiges Urteil über 2.400 €; einen Monat nach dem Urteil zahlt er; trotzdem pfändet der Gerichtsvollzieher in seiner Wohnung einen Fernseher, den ihm seine Schwester Frau Weidner geliehen hat. Aufbau: Leitfrage „Wer wehrt sich wogegen?“ → Erinnerung (Wortlautkarte § 766 I 1; § 764; § 811 als typischer Fall; GV prüft nur Gewahrsam; materielle Einwendungen nicht) → sofortige Beschwerde (Wortlautkarte § 793; § 569 I) → Vollstreckungsabwehrklage (Wortlautkarte § 767 I; § 362 BGB; Präklusion § 767 II) → kurz § 768 → Drittwiderspruchsklage (Wortlautkarte § 771 I; Eigentum) → kurz § 805 (Vermieterpfandrecht) → Klausurtipp (§§ 769, 771 III) → Schema (Zulässigkeit/Begründetheit) → Merksatz. Hauptfilm 5:34,1 (Begründung für mehr als 4.600 Zeichen in ABNAHME.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Hollmann (HO), um 60 | Inhaberin einer Autowerkstatt, Gläubigerin | Pose `standing/polka_dots` (gepunktete Bluse), Kopf `Gray Bun`; Hose Grün `#8FD694`, Haut `#F0C8A8`; Mimiken `Calm` (ruhig), `Serious` (redet), `Suspicious` (streng), `Concerned|Serious` (Sorge), `Smile` (froh) | `hilde` (Frau, älter) |
| Herr Steinbach (ST), um 45 | Schuldner | Pose `standing/pointing_finger-2` (erhobener Zeigefinger), Kopf `Short 4`; schwarzes Oberteil, Hose Blau `#8DB3F2`, Haut `#D9A07A`; Mimiken `Calm`, `Driven` (redet), `Fear`, `Concerned|Serious` (Sorge), `Smile`, `Serious` (denkt) | `stephan` (Mann, mittel) |
| Frau Weidner (WE), um 35 | Schwester des Schuldners, Dritte (Eigentümerin des Fernsehers) | Pose `standing/resting-2`, Kopf `Medium Straight`; schwarzes Oberteil, Hose Lila `#B8A9F5`, Haut `#E8B98F`; Mimiken `Calm`, `Driven` (redet), `Concerned|Serious`, `Smile`, `Serious` | `lucy` (Frau, jung) |
| Gerichtsvollzieher (GV), um 55, ohne Namen | Vollstreckungsorgan | Pose `standing/shirt-4` (dunkles Hemd), Kopf `No Hair 1`, Brille `Glasses 4`, kein Bart; Hose `#3A3A48`, Haut `#C99470`; Mimiken `Calm`, `Serious` (redet), `Suspicious` (denkt) | `christian` (Mann, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt und blickt nach links zur Tafel bzw. zur Mitte, `_r` blickt nach rechts (Hollmann in der Werkstatt, Steinbach und Weidner in der Wohnung). Keine Prothesen-Posen, keine Bärte (Mund frei). **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `HO_redet`, `ST_redet`, `WE_redet`, `GV_redet` (je links/rechts) und Lexi. Verworfen: `pointing_finger-1` (Kleidung nur als schwarze Tuschfläche, nicht einfärbbar). Stimmen ausschließlich aus dem zugeteilten Pool (stephan, hilde, christian, lucy). **Namen mit eindeutig deutscher Aussprache**, in keiner früheren Folge vergeben: Hollmann, Steinbach, Weidner. Figuren-PNGs: `../peeps/op_054/` (70 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 053: Kaufvertrag (Posen `easing-1`, `robot_dance-2`; Stimmen ela_froh, timo); 052: Anscheinsgefahr (`crossed_arms-2`, `shirt-3`, `walking-1`); 048: `pointing_finger-2` für einen älteren grauhaarigen Kläger – hier jüngerer Schuldner mit dunklem Haar; 024 (Grundschema ZV): Gerichtsvollzieher `blazer-4` mit Sakko, Wohnzimmer mit Gemälde, und Ausblick „Gemälde gehört meiner Schwester“ – 054 löst diesen Ausblick mit eigenem Fall auf, aber mit neuem Personal und neuem Schauplatz (Autowerkstatt; Wohnung mit Sideboard, großem und altem Fernseher).
- Cremegrund durchgehend (Tageslicht).

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Autowerkstatt** `fall`→`h1` | Bodenlinie; Hollmann links (blickt nach rechts), Auto in der Mitte, Steinbach rechts; später der Gerichtsvollzieher rechts | tabler:`car` (Rot), `tool` (dreht), `cash-off` (Rot), `building-bank` (Blau), `cash-banknote` (Grün, wandert von Steinbach zu Hollmann) | `Fall · Die Reparatur` (ab 0,0 s) → `Fall · Das Urteil` → `Fall · Die Zahlung` → `Fall · Der Vollstreckungsauftrag` | Werkstatt · Ratsche · Steinbach kommt · „Reparatur: 2.400 €“ · „zahlt nicht“, Hollmann streng · Amtsgericht · Urteil · „rechtskräftig“, Hollmann froh, Steinbach besorgt · Überweisung wandert, „einen Monat nach dem Urteil“, „überwiesen: 2.400 €“ · GV kommt, „Trotzdem: Vollstreckungsauftrag“ · Hollmann redet, Blase | Ratsche (`szene_054ratsche_1`) |
| **B Wohnung** `wohn`→`frage` | Steinbach und Weidner links (blicken nach rechts), Sideboard mit großem Fernseher in der Mitte, Tischchen mit altem Gerät, GV rechts | tabler:`device-tv` (Dunkel), `device-tv-old` (Grau), `sticker` (Siegel, Rot) | `Fall · Die Pfändung` → `Fall · Die Frage` | zweiter Fernseher · altes Gerät · Weidner kommt, „geliehen von der Schwester“ · GV redet, Siegel, „gepfändet“ · Steinbach redet · Weidner redet · GV redet · zwei Frage-Pillen, Steinbach und Weidner besorgt, GV denkt | Klebesiegel (`szene_054siegel_1`) |
| **C Sachverhalt** `sv` | Karte vollständig (≈ 9,7 s) | – | `Sachverhalt` | 1 | – |
| **D Leitfrage** `ueber`→`l805` | Tafel links, Steinbach und Weidner rechts | tabler:`users` | `Leitfrage · Wer wehrt sich wogegen?` → `› Art und Weise: § 766 ZPO` → `› titulierter Anspruch: § 767 ZPO` → `› Recht eines Dritten: §§ 771, 805 ZPO` | Frage · § 766 · § 767 · § 771 (Weidner froh) · § 805 | – |
| **E Erinnerung** `e766`→`beschw` | Tafel mit **Wortlautkarte § 766 I 1**; Steinbach und GV | tabler:`list-check`, `building-bank`, `lock` (Gelb), `device-tv` | `Erinnerung, § 766 ZPO › Art und Weise` → `› Vollstreckungsgericht, § 764 ZPO` → `› Beispiel: unpfändbare Sache, § 811 ZPO` → `› hier: kein Verfahrensfehler` → `› Zahlung und Eigentum: nicht hier` | Karte · Marker · Amtsgericht · § 811 · Kreuz „kein Verfahrensfehler“ · Gewahrsam + BGH · materielle Einwendungen, Steinbach besorgt · eigene Beschwer + BGH | – |
| **F Sofortige Beschwerde** `p793`→`frist` | Tafel: drei Kästen Erinnerung › Entscheidung › Beschwerde, **Wortlautkarte § 793** | tabler:`file-text`, `calendar-event` | `Sofortige Beschwerde, § 793 ZPO` → `› Notfrist, § 569 Abs. 1 ZPO` | Erinnerung · Entscheidung · Beschwerde + Karte · Notfrist · 2 Wochen | – |
| **G Vollstreckungsabwehrklage** `e767`→`tenor` | Tafel mit **Wortlautkarte § 767 I**; Steinbach und Hollmann | tabler:`cash-banknote`, `building-bank`, `receipt`, `calendar-event`, `file-x` | `Vollstreckungsabwehrklage, § 767 ZPO › Einwand: Zahlung` → `› Prozessgericht des ersten Rechtszuges` → `› Erfüllung, § 362 BGB` → `› § 767 Abs. 2 ZPO` → `› Ergebnis: begründet` | Einwand · Karte · Marker · Amtsgericht · erloschen · Abs. 2 · Kreuz „vorher“ · Haken „nach dem Urteil“, Hollmann besorgt · Block „unzulässig“, Steinbach froh | – |
| **H Klauselgegenklage** `p768` | hell-lila Tafel (kurzer Abzweig) | tabler:`file-certificate` (Lila) | `Kurz: Klauselgegenklage, § 768 ZPO` | 3 Zeilen · Pille „Rechtsnachfolge?“ | – |
| **I Drittwiderspruchsklage** `e771`→`ok771` | Tafel mit **Wortlautkarte § 771 I**; Weidner und Hollmann | tabler:`device-tv` | `Drittwiderspruchsklage, § 771 ZPO › Frau Weidner ist Dritte` → `› Eigentum am Fernseher` → `› Klage gegen die Gläubigerin` → `› Ergebnis` | Dritte · Karte · Marker · Haken Eigentum + BGH · Klage gegen Hollmann (streng) · Block „unzulässig“, Weidner froh, Hollmann besorgt | – |
| **J Vorzugsklage** `p805`→`p805b` | hell-lila Tafel (kurzer Abzweig); Hollmann und GV | tabler:`home` (Gelb), `coins` (Gelb) | `Kurz: Vorzugsklage, § 805 ZPO` → `Vorzugsklage › vorzugsweise Befriedigung aus dem Erlös` | Dritter ohne Besitz · Vermieter · Kreuz kein Widerspruch · Haken Klage auf vorzugsweise Befriedigung + BGH | – |
| **K Klausurtipp** `tipp`→`tipp2` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · mehrere Rechtsbehelfe zugleich` → `· einstweilige Einstellung, § 769 ZPO` | mehrere Beteiligte · Steinbach § 767 · Weidner § 771 · Klage hält nicht auf · Einstellung · § 769/§ 771 III | – |
| **L Klausurschema** `sch`→`sb3` | breite Karte, Schema baut sich auf | – | `Klausurschema` → `› A. Zulässigkeit` → `› B. Begründetheit` | Titel · A · 1 · 2 (+ Zuständigkeiten) · 3 · B · § 766 · § 767 · § 771 | – |
| **M Merksatz** `merke`→`m2` | Lexi erklärt (redet), drei Merkzeilen mit Marker | – | `Merksatz` | Erinnerung · Vollstreckungsabwehrklage · Drittwiderspruchsklage | – |

**Blasen:** Sprechblasen Stil C (Standard seit 02.10.2026). **Zahlen** auf Blasen, Tafeln und Pillen in Ziffern.
**Übergänge:** stumme Schiebeblenden nur zwischen den 13 Folien; innerhalb harte Schnitte und Pops; Bewegungen: Ratsche (A), Geldschein von Steinbach zu Hollmann (A), Siegel auf den Fernseher (B).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_054ratsche_1`, `szene_054siegel_1`), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Frau Hollmann repariert in ihrer Autowerkstatt das Auto von Herrn Steinbach für 2.400 Euro. Er zahlt nicht. Das Amtsgericht verurteilt ihn zur Zahlung; das Urteil wird rechtskräftig. Einen Monat nach dem Urteil überweist Herr Steinbach die 2.400 Euro an Frau Hollmann.
>
> Trotzdem beauftragt Frau Hollmann den Gerichtsvollzieher. Er pfändet in der Wohnung von Herrn Steinbach einen großen Fernseher, den ihm seine Schwester, Frau Weidner, geliehen hat. Daneben steht sein eigenes altes Gerät.
>
> Annahme: Titel, Klausel und Zustellung liegen vor; Pfändungsverbote greifen nicht.
>
> **Wer kann sich wogegen wehren – und womit?**
