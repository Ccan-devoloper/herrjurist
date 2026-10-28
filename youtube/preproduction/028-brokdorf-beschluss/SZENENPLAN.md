# Folge 028 · Brokdorf-Beschluss: Darf man eine Demo verbieten? (Art. 8 GG) – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_028.py`](src/skript_028.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Klassiker-Fall). Der echte Fall wird sachlich nacherzählt (Allgemeinverfügung des Landrats des Kreises Steinburg vom 23.2.1981 gegen die Großdemonstration am Kernkraftwerk Brokdorf, BVerfG-Beschluss vom 14.5.1985 – 1 BvR 233, 341/81, BVerfGE 69, 315). Den Kern tragen zwei fiktive Figuren: Herr Böhm (Versammlungsbehörde) und Elke (Anwohnerin, will friedlich demonstrieren). Ablauf: Fall → Verbot → Instanzen → Frage → Sachverhalt → Bedeutung der Versammlungsfreiheit → Wortlaut Art. 8 I → I. Schutzbereich (friedlich, Unfriedlichkeit Einzelner) → II. Eingriff → III. Rechtfertigung (Wortlaut Art. 8 II, Grenzen, Anmeldepflicht/Spontanversammlung, Wortlaut § 15 I VersG, enge Auslegung, Kooperation) → Anwendung im Fall → Ergebnis → Rechtslage heute → Klausurtipp → Schema → Merksatz.
**Länge:** Hauptfilm 6:57,9 (5.965 gesprochene Zeichen). Mehr als fünf Minuten wegen der drei Wortlautkarten (Art. 8 I und II GG vorgelesen, § 15 I VersG mit Merkmalen), des Instanzenwegs (VG, OVG, BVerfG mit Teilerfolg), der fünf Maßstäbe des Gerichts (Unfriedlichkeit Einzelner, Anmeldepflicht, enge Auslegung von § 15, Kooperation, Anwendung) und der heutigen Rechtslage (Landesrecht, Art. 125a GG).

## Neutralität und Zurückhaltung

- Neutral zur Kernkraft: Kraftwerk nur als Gebäude-Icon (Tabler `building-factory-2`, grau), kein Strahlensymbol, keine Bewertung von Anliegen oder Gegnern.
- Gewalt zurückhaltend: Ausschreitungen nur als Textpille, keine Gewaltbilder; Unfriedlichkeit als rot markierte Personensymbole.
- Bürgerinitiativen, Beschwerdeführer, Landrat (nur als Behörde), Richter und Politiker treten nicht als Figuren auf und werden nicht genannt.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Böhm (BO), um 50 | Mitarbeiter beim Landrat des Kreises Steinburg, Versammlungsbehörde | Pose `standing/shirt-4` (schwarzes Hemd, Hose `#3D3D58`), Kopf `Short 1`, Brille `Glasses 3`, Haut `#E8B98F`; Mimiken `Calm` (ruhig), `Serious` (redet/ernst), `Suspicious` (denkt) | `christian` (Mann, mittel) |
| Elke (EL), um 55 | Anwohnerin in der Wilstermarsch, will friedlich demonstrieren | Pose `standing/resting-1` (Pullover Lila `#B8A9F5`), Kopf `Gray Medium` (rotes Haar im Original), Haut `#F1C6A5`; Mimiken `Smile` (ruhig/redet), `Cute` (froh), `Concerned|Serious` (Sorge), `Suspicious` (denkt), `Serious` (ernst) | `hilde` (Frau, älter) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt (blickt nach links zur Tafel bzw. zu Elke), `_r` blickt nach rechts (Elke zur Baustelle, Böhm zu Elke am Tisch).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `BO_redet`, `EL_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (`shirt-1/-2` mit Prothese bewusst nicht verwendet). `EL_redet` auf `Smile` statt `Calm`, weil `Calm` bei diesem Kopf die Augen schließt.
- **Stimmen nur aus dem Pool** timo, julia, christian, hilde: verwendet christian und hilde; Erzählerin/Lexi Carla ohne Rolle. Keine Überschneidung mit 025 (william, julia).
- **Namen mit eindeutig deutscher Aussprache:** Böhm (Umlaut), Elke; beide nicht in früheren Folgen (auch nicht in 026/027: Egon, Bodo, Maren, Anke, Jürgen, Kunze).
- Figuren-PNGs: `../peeps/op_028/` (40 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 025: Versammlungssaal, Behördenzimmer, Auflage mit Stempel (Art. 5 GG); 020: Fußgängerzone; 019: Straßenblockade.
- Hier: flache Marschlandschaft mit Bäumen, Windmühle, Baustelle (Kran, Bauzaun, Kraftwerk), Lagekarte der Wilstermarsch mit Verbotszonen (groß/klein), Instanzensäule rechts, Gesprächstisch Behörde/Anwohnerin. Erstmals Art. 8 GG als Hauptgrundrecht mit drei Wortlautkarten.
- Zwei neue Figuren, Posen `shirt-4` und `resting-1` (nicht in 023–026).

## Szenen

Alle Szenen auf Cremegrund (Tageslicht).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Die Wilstermarsch** `fall`–`e1` | Marsch: Bäume, Windmühle; Baustelle mit Kran, Kraftwerk, Bauzaun; Elke blickt zur Baustelle | tabler:`trees` (Grün), `windmill`, `crane` (Gelb), `building-factory-2` (Grau), `fence`, `speakerphone` (Orange); Pillen „Wilstermarsch, Februar 1981“, „Brokdorf: Bau eines Kernkraftwerks“, „Aufruf: Großdemonstration“, „am 28.2.1981“, „frühere Demos: teilweise unfriedlich“ | `Fall · Die Wilstermarsch` (ab 0,0 s) | Marsch ab 0,0 s · Pille · Kran · Kraftwerk · Bauzaun · Aufruf · Datum · frühere Demos · Elke · Blase | – |
| **B Das Verbot** `boehm`–`sofort` | Behördenzimmer: Tisch, Akten, Lampe, Böhm; Allgemeinverfügung links | tabler:`table` (Orange), `files`, `lamp`, `users-group` (Blau), `news`, `rubber-stamp` (Rot, senkt sich) | `Fall · Das Verbot` | Böhm · Landrat · Menschen · 50.000 · Blase · Flugblatt · Karte · sechs Zeilen zum Wort · Stempel | Stempel `szene_028stempel_1` |
| **C Der Weg durch die Instanzen / Die Frage** `vg`–`frage` | Lagekarte Wilstermarsch: großer roter Ring (210 km²) → kleiner Ring (VG) → großer Ring (OVG, Mond = Nacht) → Menschengruppen; Gerichte rechts; Elke | tabler:`building-bank` (Grau), `moon-stars`, `users-group`, fluent-hc:`classical-building` | `Fall · Der Weg durch die Instanzen` → `Fall · Die Frage` | Karte · kleiner Ring · Umgebung · OVG · großer Ring · Menge · Ausschreitungen · BVerfG · zwei Fragen | Menge `szene_028menge_1` |
| **D Sachverhalt** `sv` | Sachverhaltskarte vollständig (≈ 9,8 s) | – | `Sachverhalt` | 1 | – |
| **E Bedeutung** `demok`–`selbst` | Tafel, Elke | `building-community`, `users-group`, `bell-ringing`, `map-pin` | `Art. 8 GG · Bedeutung für die Demokratie` | sieben Zeilen zum Wort, Icons wechseln | – |
| **F Wortlaut Art. 8 I** `wl8` | Wortlautkarte, vorgelesen, Marker zum Wort | `book` | `Art. 8 GG › Wortlaut Art. 8 I GG` | Karte · sechs Marker | – |
| **G I. Schutzbereich** `sb`/`vers`/`fried` | Tafel, Elke | `users-group`, `hand-stop` | `Art. 8 GG › I. Schutzbereich` → `› friedlich und ohne Waffen` | Titel · Versammlung · Demonstration · unfriedlich · Gewalttätigkeiten · Sachen | – |
| **H Unfriedlichkeit Einzelner** `einzel`–`kollek` | Tafel mit zehn Personensymbolen, zwei werden rot; Elke besorgt → froh | `user`/`user-x` (Tafelpiktogramme), `shield-check` | `… › Unfriedlichkeit Einzelner` | Personen · rote Einzelne · ✓ Schutz bleibt · sonst … · ✗ anders nur … | – |
| **I Ergebnis/II. Eingriff** `elke2`/`ein` | Tafel, Elke | `ban` | `… › Ergebnis` → `Art. 8 GG › II. Eingriff` | Behörde ging davon aus · die meisten · Elke (+) · Block Eingriff ✓ | – |
| **J Wortlaut Art. 8 II** `wl82`/`gleich` | Wortlautkarte, Grenzen darunter; Herr Böhm | `book`, `scale` | `Art. 8 GG › III. Rechtfertigung › Wortlaut Art. 8 II GG` → `› Grenzen der Beschränkung` | Karte · fünf Marker · gleichwertige Rechtsgüter · Verhältnismäßigkeit | – |
| **K Anmeldepflicht** `anm`–`auto` | Tafel, Herr Böhm (ruhig → denkt) | `file-text`, `bolt`, `ban` | `… › Anmeldepflicht, § 14 VersG` | § 14 · nicht ausnahmslos · Spontanversammlung · ✗ kein automatisches Verbot · Eingreifen leichter | – |
| **L Wortlaut § 15 I VersG** `wl15`/`merk` | Wortlautkarte (Zitat), Merkmale markiert zum Wort; Herr Böhm | `book` | `… › § 15 I VersG › Wortlaut` | Karte · sechs Marker | – |
| **M Enge Auslegung** `eng`–`ultima` | Tafel, Elke | `shield-check`, `alert-triangle`, `search`, `stairs` | `… › enge Auslegung` → `› unmittelbare Gefährdung` → `› Verbot als ultima ratio` | drei Punkte mit Unterzeilen, ✗ bloßer Verdacht | – |
| **N Kooperation** `koop`–`abm` | Gesprächstisch: Böhm links (blickt zu Elke), Elke rechts; Kooperationskarte links | `table`, `heart-handshake` (Grün) | `… › Kooperation der Behörde` | Karte · vier Zeilen · Blase Böhm · Blase Elke · Behörde kannte … · ✗ Abmahnung | – |
| **O Anwendung im Fall** `subs`–`mehr` | Lagekarte wie C: kleiner Ring ✓, großer Ring ✗; Pillen rechts; Elke | wie C | `… › Anwendung im Fall` | Ring ✓ · Bauzaun · Entschärfung · Ring ✗ · Befürchtungen · Mehrheit | – |
| **P Ergebnis** `erg`–`kuenft` | Tafel, Herr Böhm | fluent-hc:`classical-building`, `gavel` | `Ergebnis · Beschluss vom 14.5.1985` | Block · teilweise · Verfahrensfehler · OVG … · künftig … | – |
| **Q Rechtslage heute** `heute`–`bind` | Tafel, Elke | `map`, `scale` | `Rechtslage heute · Landesversammlungsgesetze` | 2006 · Ländersache · Bayern · Bundesgesetz fort · Maßstäbe | – |
| **R Klausurtipp** `tipp`/`tipp1` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · erst das mildere Mittel` | zwei Punkte, Unterzeilen einzeln | – |
| **S Klausurschema** `sch`–`k3e` | Schema baut sich Punkt für Punkt auf | – | `Klausurschema` | I · 1. · 2. · II · III · 1. · 2. · 3. · Anmeldung · Kooperation | – |
| **T Merksatz** `merke`/`m2` | Lexi erklärt (redet), Merksatz mit Marker | – | `Merksatz` | Satz 1 · Marker · Satz 2 · Marker | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 20 Folien; innerhalb harte Schnitte und Pops; eine Bewegung (Stempel senkt sich auf die Allgemeinverfügung).
**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`szene_028stempel_1`, `szene_028menge_1`), Herkunft in `geraeusche_herkunft.json`.

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Februar 1981: Bürgerinitiativen rufen bundesweit zu einer Großdemonstration gegen den Weiterbau des Kernkraftwerks Brokdorf (Schleswig-Holstein) am 28. Februar auf; frühere Demonstrationen dort verliefen teilweise unfriedlich. Die Demonstration ist nicht angemeldet. Die Behörde rechnet mit bis zu 50.000 Teilnehmern, darunter Gewaltbereiten. Am 23. Februar verbietet der Landrat des Kreises Steinburg per Allgemeinverfügung jede Demonstration gegen das Kraftwerk vom 27. Februar bis 1. März auf rund 210 km² der Wilstermarsch, sofort vollziehbar. Das Verwaltungsgericht beschränkt das Verbot auf die Umgebung der Baustelle; das Oberverwaltungsgericht stellt es in der Nacht vor der Demonstration vollständig wieder her. Es folgen Verfassungsbeschwerden.
>
> *(Nach BVerfGE 69, 315 – 1 BvR 233, 341/81, Beschluss vom 14. Mai 1985.)*
>
> **Verletzt das Verbot die Versammlungsfreiheit (Art. 8 GG)?**

Kein Fiktiv-Hinweis auf der Karte (Vorgabe Kanalinhaber 01.10.2026); die Quelle des echten Falls bleibt genannt.

## Hinweis zu Blasen- und Tafeltext

Blasentexte sind wortgleich mit dem Gesprochenen. Tafeln schreiben Jahreszahlen, Daten und Normen in Ziffern („1981“, „§ 15 I VersG“), gesprochen als Wörter. Kleine graue Fundstellenzeilen sind Belege, kein Sprechtext. Wortlautkarten sind als Zitat gekennzeichnet (Anführungszeichen, Normangabe).
