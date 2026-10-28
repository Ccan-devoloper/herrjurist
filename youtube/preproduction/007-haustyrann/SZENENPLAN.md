# Folge 007 · Haustyrannen-Fall: Den Peiniger im Schlaf töten? – Szenenplan

**Stand:** 01.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_007.py`](src/skript_007.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Nadine (NA/NG), Ende 30 | Ehefrau, tötet den schlafenden Ehemann (entspricht der Angeklagten in BGHSt 48, 255) | Pose `standing/resting-1`, für den hypothetischen Auszug `standing/walking-1` (gleiche Reihe -1, gleiches Outfit); Kopf `Medium Straight`; lila Oberteil `#B8A9F5`, Haut `#E3B38E`; Mimiken `Calm` (ruhig), `Fear` (Angst), `Tired` (müde), `Serious` (ernst), `Concerned|Serious` (traurig), `Eyes Closed` (zu), `Solemn` (redet), `Smile` (Hoffnung) | `laura_klar` (Frau, mittel) |
| Ralf (RA), um 45 | gewalttätiger Ehemann („Haustyrann“, entspricht M. F.) | Pose `standing/pointing_finger-1` (Drohgeste, Stiefel); Kopf `No Hair 3`, Bart `Full 3`; Kleidung schwarz (Pose ohne einfärbbare Flächen), Haut `#F0C8A8`; Mimiken `Contempt` (kalt), `Very Angry` (wütend), `Angry with Fang` (redet) | `marc` (Mann, mittel) |
| Beraterin (BE) | Mitarbeiterin eines Frauenhauses, nur in der hypothetischen Szene „andere Wege“ | Pose `standing/robot_dance-3` (offene, einladende Hand); Kopf `Medium Bangs 3`, Brille `Glasses 3`; grünes Oberteil `#8FD694`, Haut `#8D5A3B`; Mimiken `Smile`, `Calm` (redet) | `julia` (Frau, jung) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` | Carla Blum |
| Erzählerin | – | – | Carla Blum |

Alle Posen blicken im Original nach rechts; die Grundansicht ist gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Ralf steht in den Fallszenen links und blickt mit der Drohgeste nach rechts zu Nadine. Prothesen-Posen wurden nicht gewählt. Die Pose `pointing_finger-1` gab es in Folge 006 schon (Albers); hier mit anderem Kopf, Bart und dunkler Kleidung, weil nur sie Drohgeste und Stiefel verbindet.

**Sensibles Thema (häusliche Gewalt, Tötung):** Fiktive Namen, keine realen Beteiligten. Keine Waffe im Bild (der Revolver erscheint nur als Wort „Revolver gefunden“ an einer Kiste), kein Blut, kein Opfer im Moment der Tat (nur die geschlossene Schlafzimmertür, danach die Pille „Ralf ist tot“). Ralf ist nach dem Zubettgehen nicht mehr zu sehen, nur das Bett. Gewalt wird nur benannt (Pillen „seit 15 Jahren Misshandlungen“, „beschimpft und schlägt sie“), nie gezeigt. Lea ist nicht besetzt. Die beiden Töchter erscheinen nur als Emoji-Gesichter (Fluent Emoji High Contrast `girl`). Hilfehinweis am Ende der Beschreibung.

Figuren-PNGs: `../peeps/op_007/` (60 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- 005/006: Zivilrecht (Abstraktionsprinzip, Anspruchsaufbau) mit Laden- und Haustürszenen; 004 Ministerbüro; 001 nächtliche Straße.
- Hier: Strafrecht AT, Wohnhaus (Wohnzimmer bei Tag, Flur bei Nacht, Vormittag mit Schlafzimmertür), dazu eine hypothetische Szene „Frauenhaus“. Drei neue Figuren; keine Stimme aus 006 (william, ela_warm, timo).

## Szenen

Tageslicht auf Cremegrund. **Nacht begründet** in Szene B: Ralf kommt gegen 3:30 Uhr heim (Nachtverlauf wie Folge 001, Prüfpfad weiß).

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Das Haus** `haus`→`angst` | Wohnzimmer: Ralf links, Sofa und Lampe in der Mitte, Nadine rechts, Töchter als Gesichter | tabler:`sofa` (Blau), tabler:`lamp` (Gelb), fluent-hc:`girl` ×2 (Gelb), tabler:`calendar` (Rot), tabler:`trending-up` (Rot) | `Fall · Das Haus` | 1 Familie · 2 Kalender + „seit 15 Jahren Misshandlungen“, Mimik wütend/traurig · 3 „immer schlimmer“, „auch die Töchter“, Nadine Angst · 4 Ralf redet, Blase „Wenn du gehst, finde ich dich. Überall.“ · 5 „glaubt ihm“ · 6 „als äußerst gewalttätig bekannt“, Ralf kalt | – |
| **B Die Nacht** `nacht`→`schlaf` | Flur bei Nacht: Haustür links, Ralf kommt herein, Nadine rechts; dann nur das Bett | tabler:`door` (Nachtblau), tabler:`clock-hour-3`, tabler:`moon-stars` (Gelb), tabler:`bed` (Blau), tabler:`zzz` | `Fall · Die Nacht` | 1 Tür, Ralf kommt · 2 „gegen 3:30 Uhr“ · 3 „beschimpft und schlägt sie“, Ralf wütend, Nadine Angst · 4 Ralf weg, Bett, „Ralf schläft“ · 5 „Nadine bleibt wach“ | Haustür bei [nacht] |
| **C Der Vormittag** `morgen`→`frage` | Flur bei Tag: Kiste links, Schlafzimmertür in der Mitte, Nadine rechts | tabler:`sun`, tabler:`archive` (Grau), tabler:`hourglass`, tabler:`door` (Blau) | `Fall · Der Vormittag` → `Fall · Die Frage` | 1 Nadine müde · 2 „Revolver gefunden“ · 3 Sanduhr, „ringt lange mit sich“, Nadine ernst · 4 Schlafzimmertür, Nadine Augen zu · 5 „Ralf ist tot“ · 6 Nadine redet, Blase „Ich sah keinen anderen Ausweg.“ · 7 Frage-Pille „Mord? Oder entschuldigt?“ | – |
| **D Sachverhalt** `sv` | Sachverhaltskarte vollständig, ca. 10 s (5 s Lesepause) | – | `Sachverhalt` | 1 | – |
| **E Tatbestand, Heimtücke** `a`→`heim_erg` | Tafel links, Nadine rechts; Schlafzimmertür bzw. Bett mit „zzz“ | tabler:`door`, tabler:`bed`, tabler:`zzz` | `A. Nadine › §§ 212, 211 StGB` → `› I. 1. Tötung, Vorsatz` → `› I. 2. Heimtücke` → `› Schlafender` → `› I. 2. Heimtücke (+)` | Tafelzeilen je Merkmal mit Haken; Pille „nie gewehrt“; Block „Heimtücke (+)“ (≈ 12 Halte) | – |
| **F Rechtswidrigkeit** `rw`→`rw_erg` | Tafel links, Bett bzw. Waage rechts über Nadine | tabler:`bed`, tabler:`zzz`, tabler:`scale` (Gelb) | `› II. Rechtswidrigkeit` → `› II. 1. Notwehr, § 32 StGB` → `› II. 2. Notstand, § 34 StGB` → `› II. Rechtswidrigkeit (+)` | „kein Angriff“ ✗, Notwehr (−); Waage „Gesundheit“/„Leben“, ✗, Block „Tat rechtswidrig“ (≈ 10 Halte) | – |
| **G Schuld, Gefahr** `schuld`→`ehe` | Tafel links, Nadine rechts | tabler:`alert-triangle`, tabler:`clock`, tabler:`home` (Lila) | `› III. Schuld, § 35 I StGB` → `› Dauergefahr` → `› gegenwärtig` → `› Zumutbarkeit` | Gefahr statt Angriff · Dauergefahr ✓ „jederzeit“ · gegenwärtig ✓ · Ehe ✓ „blieb bei ihm“ (≈ 9 Halte) | – |
| **H Nicht anders abwendbar** `anders`→`offen` | 1) Tafel links; rechts hypothetisch Nadine mit Rollkoffer und Beraterin. 2) Tafel „BGH: Hilfe Dritter geht vor“, Nadine | tabler:`home-shield` (Grün), fluent-hc:`police-car` (Blau), tabler:`luggage` (Lila), fluent-hc:`classical-building` | `› nicht anders abwendbar` → `› Hilfe Dritter geht vor` → `› nicht anders abwendbar (−)` | Frauenhaus/Polizei, Pille „hypothetisch“, Beraterin redet, Blase „Sie und Ihre Töchter können noch heute zu uns kommen.“; Regel, Ausnahme, ✗ keine Hilfe gesucht, „eher fernliegend“, Block „§ 35 I in der Regel (−)“ (≈ 12 Halte) | Rollkoffer bei [hilfe] |
| **I Irrtum** `irrtum`→`zeit` | Tafel links, Nadine rechts mit Denkblase | Denkblase „ausweglos?“, tabler:`search`, tabler:`hourglass` | `› III. 2. Irrtum, § 35 II StGB` → `› Vermeidbarkeit` | unvermeidbar/vermeidbar, Maßstab, strenge Anforderungen, Bedenkzeit (≈ 8 Halte) | – |
| **J Strafe, Ergebnis** `folge`→`erg3` | Tafel links, Hammer bzw. Gericht über Nadine | tabler:`gavel` (Gelb), fluent-hc:`classical-building` | `› IV. Strafe` → `› § 35 II 2 vor Rechtsfolgenlösung` → `A. Nadine › Ergebnis` | lebenslang → LG 9 Jahre → Großer Senat → Vorrang → 3 bis 15 Jahre → stärker mildernd; „aufgehoben“, Klausurergebnis mit Haken/Kreuzen (≈ 14 Halte) | – |
| **K Klausurtipp** `tipp` | hellgelbe Tafel, Lexi rechts (warnt) | Warnsymbol | `Klausurtipp · Angriff und Gefahr trennen` | 4 Halte | – |
| **L Klausurschema** `sch`→`k5` | Schema baut sich auf | – | `Klausurschema` | 9 Halte (A, I., II. mit §§ 32/34, III. mit § 35 I und II, IV.) | – |
| **M Merksatz** `merke`→`m2` | Lexi, Merksatz mit Marker | – | `Merksatz` | 4 Halte | – |

**Mundzustände** (getrennt von den Bildhalten): Ralf `RA_redet_r`, Nadine `NA_redet`, Beraterin `BE_redet`, Lexi `LX_warnt` und `LX_erklaert`, je zu/a/o/e.

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb einer Folie harte Schnitte und Pops.

**Geräusche:** zwei Handlungsgeräusche aus Freesound CC0 (`geraeusche_herkunft.json`): Haustür (Ralf kommt nachts heim), Rollkoffer (hypothetischer Auszug). Kein Schuss, kein Schlaggeräusch.

## Sachverhaltskarte (Szene D, erscheint vollständig)

> Ralf misshandelt seine Frau Nadine seit rund 15 Jahren, zuletzt immer heftiger; inzwischen schlägt er auch die beiden Töchter. Für den Fall einer Trennung droht er, Nadine überall zu finden und den Töchtern etwas anzutun. Nadine nimmt das ernst; Ralf ist als äußerst gewalttätig bekannt. Hilfe bei Polizei oder Frauenhaus sucht sie nicht.
>
> Eines Nachts kommt Ralf gegen 3:30 Uhr heim, beschimpft und schlägt Nadine und legt sich schlafen. Am Vormittag findet sie seinen Revolver. Nach langem Ringen erschießt sie gegen Mittag den schlafenden Ralf. Sie sah keinen anderen Ausweg.
>
> *(Frei nach BGH, Urt. v. 25.3.2003 – 1 StR 483/02 = BGHSt 48, 255; vereinfacht, Namen erfunden.)*
>
> **Wie hat sich Nadine strafbar gemacht?**
