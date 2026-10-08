# Folge 271 · Hells-Angels-Fall: Schüsse auf das SEK – Erlaubnistatbestandsirrtum – Szenenplan

**Stand:** 08.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_271.py`](src/skript_271.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · StGB AT · Klassiker-Fall. Fiktiver Rahmen, der dem echten Fall folgt (BGH, Urt. v. 2.11.2011 – 2 StR 375/11, Rn. nach der amtlichen Fassung). Ablauf laut Auftrag: 1. Hook (frühmorgens, Geräusche, Überfall Rivalen, Schüsse durch die Tür, draußen das SEK) → LG/BGH, Frage → Sachverhalt → § 212 kurz (Vorsatz, Irrtum über die Person) → 2. § 32 Abs. 2 als Wortlautkarte, Notwehr gegen die Polizei offen (Rn. 19 f.) → vorgestellte Lage (Rn. 22) → 3. Erforderlichkeit aus seiner Sicht: Warnschuss? (Rn. 23 f.) → 4. ETI, § 16 Abs. 1 als Wortlautkarte, Vorsatzschuld entfällt (Rn. 21, 24), Theorienstreit ein Satz mit Verweis 231, § 222 unvermeidbar (Rn. 25 f.) → 5. Kritik (ein Satz, Rotsch, ZJS 2012, 109) → 6. Klausurtipp, Schema, Merksatz mit Lexi. Hauptfilm 5:59,5.

**Darstellung (Vorgabe Koordinator):** keine Clubsymbole, keine Kutten, keine Abzeichen, keine echten Namen (nur die Fallbezeichnung „Hells-Angels-Fall“ einmal gesprochen und als Fundstellenzeile). Kein Schuss, kein Mündungsfeuer, keine Waffe im Bild, keine Verletzten: Die Pose von Elmar hält nichts; „Pistole“ und „Schüsse“ erscheinen nur als Text-Pillen. Bildzeichen nur Tür (mit Ornamentglas und Umrissen), Geräusch-Symbol (Tabler `volume`), Uhrzeit (Tabler `clock`), Polizeischild (Tabler `shield` mit Pille „Polizei“). Keine Beamten als Figuren; der getötete Beamte wird nur in einem Satz und einer grauen Pille erwähnt. Kein Schussgeräusch.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Elmar (EL), Ende 30 | führendes Mitglied eines Rockerclubs, schießt im Irrtum | `standing/resting-1` (schlichter Pullover Graublau `#7A8CA8`, schwarze Hose der Pose), Kopf `Short 1`, Haut `#E3B08C`, kein Bart, keine Brille, keine Abzeichen; 100 % Höhe; Mimiken `Calm`, `Tired`, `Serious`, `Concerned\|Serious`, `Fear`, `Awe`, `Suspicious`, `Solemn`, `Eyes Closed`; ruft: `Fear`, klagt: `Concerned\|Serious` | `niklas` (Mann, jung) |
| Gabi (GA), Mitte 30 | seine Verlobte, hört die Geräusche | `standing/easing-1` (offenes Hemd Altrosa `#E7A0B4`, Oberteil Weiß, schwarze Hose der Pose), Kopf `Medium Straight`, Haut `#F0C8A8`; 95 % Höhe; Mimiken `Calm`, `Fear`, `Awe`, `Concerned\|Serious`, `Serious`, `Solemn`; ruft: `Fear` | `julia` (Frau, jung) |
| Lexi | Klausurtipp (warnt), Schema und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- **Blickrichtung:** Posen blicken im Original nach rechts; Grundansicht gespiegelt (nach links), `_r` nach rechts. Schlafzimmer: Gabi (`_r`) blickt zu Elmar, Elmar zunächst nach links zu ihr, beim Blick aus dem Fenster nach rechts (`_r`), danach wieder zu Gabi. Flur: Elmar blickt nach rechts zur Haustür. Tafelfolien: alle nach links zur Tafel. Kontaktbild `out/besetzung_271.png`.
- **Grundmimiken alle mit geschlossenem Mund**; Mundzustände a/o/e nur in `EL_ruft`, `EL_klagt`, `GA_ruft` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen, keine Polka Dots. 62 Figuren-PNGs in `../peeps/op_271/` (Drive-Master).
- **Namen:** Elmar, Gabi – eindeutig deutsch, nicht auf der Koordinatorliste, nicht in `namen_reserviert.txt`, `grep -rlw` über `youtube/` (`*.py/*.md/*.json/*.csv`) ohne Treffer; verworfen: Ralf (007), Sandra (005). Vor der Vertonung als „271: Elmar, Gabi“ eingetragen.
- **Stimmen** aus dem Pool (niklas, julia); helmut und ela_froh nicht benötigt (keine weitere sprechende Figur; der Ruf der Polizei kommt von der Erzählerin, weil keine Beamten gezeigt werden).

**Abweichung von den letzten Folgen:** 267 (`robot_dance-3`, `walking-3`, `polka_dots`, `easing-2`), 269 (`blazer-1`, `pointing_finger-1`, `resting-2`), 266 (`crossed_arms-1`, `blazer-2`, `shirt-3`); 270 lag beim Bau noch nicht vor. In 271 keine dieser Posen; Graublau-Pullover und Altrosa-Hemd neu. Schauplätze **Schlafzimmer in der Dämmerung** (Bett, Fenster mit halb geschlossenem Rollladen, Uhr) und **Flur mit Treppe und Haustür** (Ornamentglas, Deckenlampe, Licht im Flur, draußen nur Geräusch-Symbol und Polizeischild) – neu gegenüber 267–269 und den Notwehrfolgen 214 (Obstwiese), 227 (Weinfest), 231 (Stadtpark bei Nacht). **Dämmerung/Nachtverlauf** in A1 und A2 begründet: Der Einsatz begann „bei Dämmerung“, im Haus brannte kein Licht (Rn. 8); das Einschalten des Lichts ist ein Fallmoment (Rn. 9, 25). Alle übrigen Szenen Cremegrund.

## Szenen

| Nr. | Cue(s) | Ort / Handlung | Figuren | Tafel / Pillen / Requisiten (Iconset:Name) | Prüfpfad | Geräusch |
|---|---|---|---|---|---|---|
| A1 | `fall`–`handy` | Schlafzimmer, Dämmerung: Gabi steht ab 0,0 s, hört das Knacken (Ohr, Geräusch-Symbol), weckt Elmar (Blase); Gerüchte (Warnsymbol), Vortag; Elmar geht zum Fenster (Bewegung), erkennt niemanden; Denkblase „Der Überfall!“; Pistole nur als Text; Gabi mit Handy | GA ruhig → schreck → ruft → sorge → angst; EL müde → ernst → sorge → denkt (läuft) → angst → ernst | Pillen „Frühmorgens, gegen 6 Uhr – es dämmert“, „lautes Knacken an der Haustür“, „Elmar: führendes Mitglied eines Rockerclubs“, „Gerücht: …“, „Am Vortag: neue Hinweise“, „Draußen: niemand zu erkennen“, „Er nimmt seine Pistole – mit Waffenerlaubnis.“, „Gabi: zurück ins Schlafzimmer, Familie verständigen“; tabler:bed, clock, ear, volume, alert-triangle, device-mobile; Fenster mit Rollladen programmatisch | Fall · Frühmorgens, gegen 6 Uhr … Fall · Gabi soll Hilfe holen (8 Stände) | Knacken (`szene_271knacken_1`) bei „knackt“ |
| A2 | `licht`–`verdeckt` | Flur: Licht geht an (Lampe, Raumlicht), Elmar kommt die Treppe herunter (Bewegung), draußen Geräusch-Symbol, Umrisse im Glas, Ruf (Blase), Pillen zu Schüssen und zum Beamten, Polizeischild, „Hier ist die Polizei!“, Waffe weg, Blase „Warum habt ihr nicht geklingelt?“, SEK, Auftrag (Lupe-Dokument), verdeckt | EL ernst (läuft) → sorge → denkt → angst → ruft → angst → schreck → klagt → still → Augen zu | tabler:bulb, bulb-filled, volume, shield, file-search; Treppe, Haustür mit Ornamentglas, Umrisse, Raumlicht, Wand programmatisch | Fall · Licht im Flur … Fall · Verdeckt geblieben (8 Stände) | Lichtschalter (`szene_271schalter_1`) bei „Licht“; Knacken bei „Trotzdem“ (Geräusch-Symbol an der Tür) |
| A3 | `lg`–`frage` | Tafel „Die Frage“: LG Totschlag, BGH Freispruch, Fallbezeichnung, zwei Fragen | EL | tabler:scale, building-bank, question-mark | Die Frage · … | – |
| B | `sv` | Sachverhaltskarte (≈ 9,8 s, Hinweis zum Anhalten) | – | Pille „Hat sich Elmar strafbar gemacht?“ | Sachverhalt | – |
| C | `tb`, `ident` | Tafel I. Totschlag, § 212: getötet, Vorsatz, Irrtum über die Person | EL | tabler:book, user-question | A. Elmar, § 212 StGB › I. Tatbestand › … | – |
| D | `rw`–`offen` | Wortlautkarte § 32 Abs. 2 (vorgelesen, Marker synchron); Notwehr gegen die Polizei, Zweifel, offengelassen | EL | tabler:shield-check, shield, file-search, help-circle | … › II. Rechtswidrigkeit: Notwehr, § 32 StGB › … | – |
| E | `vorst`–`spaeter` | Tafel „Seine Vorstellung“ | GA, EL | tabler:door, alert-triangle, hourglass | … › Erlaubnistatbestandsirrtum › … | – |
| F | `erf`–`erfja` | Tafel „Erforderlich aus seiner Sicht?“: Regel, Warnschuss nur wenn geeignet, Kreuz bei „Gegenteil“, kein Kampf mit ungewissem Ausgang, Ruf | EL | tabler:scale, hand-stop, door, circle-check | … › Erforderlichkeit aus seiner Sicht › … | – |
| G | `eti`–`streit` | Wortlautkarte § 16 Abs. 1 (beide Sätze, vorgelesen); BGH entsprechend, Vorsatzschuld entfällt; Verweis 231 | EL | tabler:eye, book, arrows-split | … › Erlaubnistatbestandsirrtum › … | – |
| H | `fahr`–`frei` | Tafel B. § 222: vermeidbar? drei Gründe (Haken), Freispruch | EL | tabler:hourglass, eye-off, circle-check | B. Elmar, § 222 StGB › … | – |
| I | `kritik`, `lehre` | Tafel „Kritik“ | EL | tabler:speakerphone, book | Kritik · … | – |
| J | `tipp`–`k4` | Klausurtipp | Lexi (warnt) | Warnsymbol (Streamline Freehand) | Klausurtipp › … | – |
| K | `sch`–`s4` | Klausurschema progressiv | Lexi (erklärt) | (+)/(−) | Klausurschema › … | – |
| L | `merke`, `m2` | Merksatz mit Markern „Vorstellung“, „Erforderlichkeit“, „Vorsatzschuld“, „vermeiden“ | Lexi | – | Merksatz | – |

**Sachverhaltskarte:** wörtlich in `src/folien_271.py` (`sachverhalt_271`), Schrift 34 px, ohne Fiktiv-Hinweis.
**Lizenzen:** Open Peeps (CC0), Tabler Icons (MIT), Fluent Emoji High Contrast (MIT, Haken/Kreuz), Streamline Freehand (CC BY 4.0, Warnsymbol, Namensnennung in der Beschreibung); Geräusche Freesound CC0 (`geraeusche_herkunft.json`).
