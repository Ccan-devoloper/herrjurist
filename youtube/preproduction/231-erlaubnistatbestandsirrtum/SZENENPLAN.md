# Folge 231 · Erlaubnistatbestandsirrtum (ETBI): Alle Schuldtheorien erklärt – Szenenplan

**Stand:** 07.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_231.py`](src/skript_231.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Fr · Klausurpraxis · StGB AT · Streitstand. Ablauf laut Auftrag: 1. Hook (Joggerin, Finder mit Handy, Pfefferspray) → Frage → Sachverhalt → 2. Tatbestand § 223 (§ 224 Abs. 1 Nr. 2 in Betracht) kurz → 3. Rechtswidrigkeit: § 32 Abs. 2 als Wortlautkarte, kein Angriff → rechtswidrig → 4. Irrtum: ETBI (Putativnotwehr), Abgrenzung Erlaubnisirrtum § 17 → Problem zwischen § 16 Abs. 1 Satz 1 und § 17 Satz 1 (zwei Wortlautkarten) → 5. fünf Theorien je als Tafel mit Kern, Ergebnis im Fall und Kritik; Teilnahme-Argument (§§ 26, 27) bei der eingeschränkten und der rechtsfolgenverweisenden Variante; BGH → 6. Ergebnis: keine Vorsatzstrafe, § 229 bei vermeidbarem Irrtum, Gegenfall → 7. Klausurtipp (Prüfungsstandort Schuld), Schema, Merksatz mit Lexi. Hauptfilm 6:36,9.

**Darstellung (Vorgabe Koordinator):** Pfefferspray nur als Symbol (Tabler `spray`, erscheint bei „sprüht“), keine Verletzung im Bild (Helge nur mit geschlossenen Augen, Text „Helges Augen brennen.“ als Pille). Helge als sympathischer älterer Spaziergänger (Ocker-Pullover, Brille, freundliche Mimik, offene Hand mit dem Handy), kein Klischee. Bärbel erschrocken/verängstigt (`Awe`, `Fear`, `Concerned|Serious`), nicht hysterisch. Kein Messer im Bild: „Ein Messer!“ steht nur als Text in Bärbels Denkblase.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Bärbel (BA), Mitte 40 | Joggerin, sprüht | `standing/walking-2` (schwarzes Laufshirt der Pose, Leggings Beere `#C2457A`), Kopf `Bun`, Haut `#EDC3A0`; 95 % Höhe; Mimiken `Calm`, `Smile`, `Fear`, `Concerned\|Serious`, `Serious`, `Suspicious`, `Tired`, `Awe`; ruft: `Fear` | `sabrina` (Frau, mittel) |
| Helge (HE), um 65 | Spaziergänger, Finder | `standing/robot_dance-3` (Pullover Ocker `#D9A066`, Hose Graublau `#5A6B7A`), Kopf `No Hair 2`, Brille `Glasses`, Haut `#E3B08C`; Mimiken `Calm`, `Smile`, `Concerned\|Serious`, `Serious`, `Suspicious`, `Eyes Closed`, `Tired`; ruft: `Smile`, klagt: `Eyes Closed` | `william` (Mann, älter) |
| Lexi | Klausurtipp (warnt), Schema und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. A1: Bärbel joggt nach links (Blick links), dreht sich bei „dreht sich um“ zu Helge (rechts, `_r`); Helge kommt von rechts, blickt nach links zu ihr, die offene Hand mit dem Handy zeigt zu ihr. Tafelfolien: alle nach links zur Tafel. Kontaktbild `out/besetzung_231.png`.
- **Grundmimiken alle mit geschlossenem Mund**; Mundzustände a/o/e nur in `BA_ruft`, `HE_ruft`, `HE_klagt` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots. 62 Figuren-PNGs in `../peeps/op_231/` (Drive-Master).
- **Namen:** Bärbel, Helge – eindeutig deutsch, nicht auf der Koordinatorliste, nicht in `namen_reserviert.txt`; `grep -rlw` über `youtube/` (`*.py/*.md/*.json/*.csv`) ohne Treffer. Verworfen: Roland (Vorname eines im Repo zitierten Hochschullehrers, dessen Lehrmaterial auch hier zitiert wird), Lothar (015 verworfen), Hannes (005), Ortwin (170, 215). Vor der Vertonung als „231: Bärbel, Helge“ eingetragen.
- **Stimmen** aus dem Pool (sabrina, william); marc und laura_ruhig nicht benötigt.

**Abweichung von den letzten Folgen:** 228 (`robot_dance-2`, `polka_dots`, `crossed_legs`, `closed_legs-1`, `blazer-2`), 229 (`shirt-3`, `blazer-3`, `easing-2`, `walking-1`), 230 (`pointing_finger-2`, `blazer-3`, `walking-1`), 227 (`blazer-4`, `pointing_finger-1`, `easing-1`, `resting-1`), 226 (`resting-1`, `blazer-4`, `crossed_arms-2`, `walking-3`) – in 231 keine dieser Posen; `walking-2` zuletzt 225, `robot_dance-3` zuletzt 224. Beere-Leggings zum schwarzen Laufshirt und Ocker-Pullover sind neu. Schauplatz **Stadtpark bei Nacht** (Parkweg, Laterne mit Lichtkegel, Mond, Bäume) – neu gegenüber 227 (Weinfest), 228–230 und den Notwehrfolgen 033 (Bibliothek), 214 (Obstwiese). **Nacht** in Szene A1, weil der Fall nachts spielt und die Dunkelheit den Irrtum trägt (Grund im Sachverhalt; Vermeidbarkeit hängt am Licht der Laterne); Nachtverlauf wie Folge 148. Alle übrigen Szenen Tageslicht-Cremegrund.

## Szenen

| Nr. | Cue(s) | Ort / Handlung | Figuren | Tafel / Pillen / Requisiten (Iconset:Name) | Prüfpfad | Geräusch |
|---|---|---|---|---|---|---|
| A1 | `fall`–`he2` | Stadtpark bei Nacht: Bärbel joggt ab 0,0 s nach links (Kopfhörer), Handy fällt auf den Weg, Helge erscheint rechts, hebt es auf, läuft hinterher (1. Bewegung), ruft, rennt bei „rennt“ bis unter die Laterne (2. Bewegung); Bärbel dreht sich um, Handy glänzt (Funkeln), Denkblase „Ein Messer!“, Ruf, Spray-Symbol, Helge mit geschlossenen Augen, Helge redet | BA ruhig → schreck_r → angst_r → ruft_r → angst_r → sorge_r; HE ruhig → froh (laufend) → ruft → froh (rennend) → froh → augen → klagt | Pillen „Herbstabend im Stadtpark, es ist schon dunkel“, „Musik im Ohr“, „Handy verloren, ohne dass sie es merkt“, „Helge, ein älterer Spaziergänger“, „Ein Mann rennt im Dunkeln auf sie zu.“, „Unter der Laterne glänzt etwas in seiner Hand.“, „Pfefferspray“, „Helges Augen brennen.“; Blasen (Stil C) Helge 2×, Bärbel 1×, Denkblase Bärbel; tabler:trees, headphones, device-mobile, sparkles, spray; `mond()`, `laterne()`, `lichtkegel()` (ostil), Parkweg programmatisch | Fall · Herbstabend im Stadtpark … Fall · Nur das Handy (9 Stände) | Laufschritte (`szene_231schritte_1`) bei „rennt“; Sprühstoß (`szene_231spray_1`) bei „sprüht“ |
| A2 | `frage`, `frage2` | Tafel „Die Frage“ | BA, HE | tabler:device-mobile „Angriff, den es nie gab“, scale „Streitstand“ | Die Frage · … | – |
| B | `sv` | Sachverhaltskarte (≈ 9,6 s, Hinweis zum Anhalten, mit Vermeidbarkeits-Annahme) | – | Pille „Wie hat sich Bärbel strafbar gemacht?“ | Sachverhalt | – |
| C | `tb`–`vors` | Tafel I. Tatbestand | BA, HE | Haken; BGH 1 StR 112/17; tabler:book, spray, target | A. Bärbel, §§ 223, 224 StGB › I. Tatbestand › … | – |
| D | `rw`–`rw_neg` | Wortlautkarte § 32 Abs. 2 (vorgelesen, Marker synchron); kein Angriff (Kreuz bei „Angriff“), keine Notwehrlage | BA, HE | BGH 4 StR 36/22 Rn. 10; tabler:shield-check, device-mobile, shield-x | A. Bärbel › II. Rechtswidrigkeit: Notwehr, § 32 StGB › … | – |
| E | `irrtum`–`eti` | Tafel „Bärbel hat sich geirrt“: Vorstellung, hypothetische Rechtfertigung, ETBI/Putativnotwehr, Abgrenzung Erlaubnisirrtum | BA, HE | BGH 4 StR 36/22 Rn. 11, 3 StR 450/10 Rn. 12; tabler:zoom-question, alert-triangle, eye, book | A. Bärbel › Irrtum › … / Erlaubnistatbestandsirrtum / Abgrenzung | – |
| F | `gesetz`–`dazw` | Wortlautkarten § 16 Abs. 1 Satz 1 und § 17 Satz 1 (vorgelesen, Marker „Umstand“, „vorsätzlich“, „Einsicht“, „Schuld“); „wie § 16 / wie § 17“ | BA | tabler:book, arrows-exchange | A. Bärbel › Erlaubnistatbestandsirrtum › … | – |
| G1–G5 | `t1`–`hm` | je eine Theorietafel: Kern (blau), Ergebnis im Fall (grün/rot), Kritik (Kreuz), Fundstelle; G4 zusätzlich Zitat §§ 26, 27; G5 Teilnahme (Haken), Kritik (Kreuz), h. M. | BA | tabler:bulb, book, gavel, scale, puzzle, git-branch, users, circle-check | … › Rechtsfolge: 1.–5. … | – |
| G6 | `bgh`, `bgh2` | Tafel Bundesgerichtshof: § 16 entsprechend; mal Vorsatz, mal Vorsatzschuld; im Ergebnis keine Vorsatzstrafe | HE | BGH 4 StR 36/22, 2 StR 375/11, 3 StR 199/15; tabler:gavel | … › Bundesgerichtshof … | – |
| H | `erg`–`gegen` | Tafel Ergebnis: keine Vorsatzstrafe; § 229; Ruf und Laterne; vermeidbar → strafbar; Gegenfall | BA, HE | BGH 2 StR 375/11 Rn. 36, BGHSt 45, 378; tabler:shield-x, bulb, gavel, moon-stars | A. Bärbel › Ergebnis / B. Bärbel, § 229 StGB › … | – |
| I | `tipp`–`k4` | Klausurtipp | Lexi (warnt) | Warnsymbol (Streamline Freehand) | Klausurtipp › … | – |
| J | `sch`–`s4` | Klausurschema progressiv | Lexi (erklärt) | (+)/(−) | Klausurschema › … | – |
| K | `merke`, `m2` | Merksatz mit Markern „Vorsatztat“, „Fahrlässigkeit“, „vermeiden“ | Lexi | – | Merksatz | – |

**Sachverhaltskarte:** wörtlich in `src/folien_231.py` (`sachverhalt_231`), Schrift 36 px, ohne Fiktiv-Hinweis.
**Lizenzen:** Open Peeps (CC0), Tabler Icons (MIT), Fluent Emoji High Contrast (MIT, Haken/Kreuz), Streamline Freehand (CC BY 4.0, Warnsymbol, Namensnennung in der Beschreibung); Geräusche Freesound CC0 (`geraeusche_herkunft.json`).
