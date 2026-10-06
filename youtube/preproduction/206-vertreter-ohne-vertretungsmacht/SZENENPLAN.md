# Folge 206 · § 179 BGB: Vertreter ohne Vertretungsmacht – haftet er persönlich? – Szenenplan

**Stand:** 06.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_206.py`](src/skript_206.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen · Zivilrecht/BGB AT · Schema. Hook nach Plan („Ein Bekannter verkauft ‚in deinem Namen' dein Motorrad – du willst davon nichts wissen.“). Fiktiver Fall: Das Motorrad von Enno steht über den Winter in der Garage von Kuno; Kuno verkauft es ohne Vollmacht ausdrücklich im Namen von Enno für 4.500 € an Silja, Silja hat keinen Anlass zu Zweifeln; Enno verweigert die Genehmigung; Silja kauft beim Händler ein gleichwertiges Motorrad für 5.300 € und verlangt von Kuno 800 €. Ablauf: Fall → Frage → Sachverhalt → Ausgangslage (Verweis Folge 043) → § 177 Abs. 1 (Wortlautkarte) → § 177 Abs. 2 (Wortlautkarte) → § 178 (Wortlautkarte) → § 179 Abs. 1 (Wortlautkarte) → Wahl/Erfüllungsinteresse → § 179 Abs. 2 (Wortlautkarte) → § 179 Abs. 3 (Wortlautkarte) → Lösung (800 €) → Kuno zahlt → § 180 in einem Satz → Klausurtipp → Prüfschema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Enno (EN), um 28 | Eigentümer, verweigert die Genehmigung | `standing/pointing_finger-1` (schwarzer Pullover, schwarze Hose und Stiefel der Pose, erhobener Zeigefinger), Kopf `Short 5`, Haut `#D9A47E`, kein Bart; Mimiken `Calm`, `Smile`, `Serious` (redet), `Suspicious`, `Concerned\|Serious`, `Awe` | `niklas` (Mann, jung) |
| Kuno (KU), um 60 | Bekannter, verkauft ohne Vertretungsmacht; verlegen, kein Bösewicht | `standing/robot_dance-2` (schwarzes Oberteil der Pose, Hose Braun `#6B5440`, weiße Schuhe, anbietende offene Hand), Kopf `No Hair 2`, Brille `Glasses`, Haut `#EDC3A0`, kein Bart; Mimiken `Calm`, `Smile` (redet in A1), `Concerned\|Serious` (redet in J2), `Fear`, `Suspicious`, `Solemn` | `helmut` (Mann, älter) |
| Silja (SI), um 30 | Käuferin | `standing/resting-1` (Pullover Rosa `#F6A5C0`, schwarze Hose der Pose), Kopf `Long Curly`, Haut `#F2CDB0`; Mimiken `Calm`, `Smile`, `Smile Big\|Smile` (redet in A1), `Awe`, `Serious` (fordert in A3), `Suspicious`, `Concerned\|Serious` | `ela_froh` (Frau, jung) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Stimmen:** nur aus dem Pool (niklas, helmut, ela_froh; `julia` gemieden). `ela_froh` spricht die Käuferin mit zwei sachlichen Sätzen („Abgemacht! …“, „Kuno, die 800 € Mehrkosten zahlst du mir!“) – keine ernste Rolle (keine Gewalt, keine Tat). Vorfolgen: 203 helmut/niklas (Pool bedingt), 204/205 andere Stimmen.
**Namen** mit eindeutig deutscher Aussprache, nicht in der Namensliste des Auftrags, nicht in der Reservierungsliste der parallelen Folgen (202–205) und in keinem Skript, Szenenplan, Rechtsstand, Abnahmebogen oder JSON unter `youtube/preproduction/` (Volltextsuche 06.10.2026; verworfen: Jannik (010), Merle, Hannes, Jonas, Lasse (vergeben), Alwin/Wigbert (mögliche englische Lesart des „w“), Erhard (zweimal E mit Enno)). Reserviert als „206: Enno, Kuno, Silja“. Nie im Genitiv (Skript-Assertion). Namensschilder Enno Blau, Kuno Grün, Silja Gelb.
**Blickrichtung:** Grundansicht gespiegelt (blickt nach links), `_r` nach rechts. A0: Enno und Kuno blicken nach links zum Motorrad. A1: Kuno blickt nach rechts zu Silja (Hand bietet an), Silja nach links zu ihm. A2: Kuno und Silja nach rechts zu Enno, Enno nach links. A3: Silja (am Telefon) nach rechts zu Kuno, Kuno nach links. J2: Kuno nach rechts zu Silja. Tafelszenen: beide nach links zur Tafel. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `EN_redet`, `KU_redet`, `KU_klagt`, `SI_redet`, `SI_fordert` (je links/rechts) und Lexi. Figuren-PNGs `../peeps/op_206/` (86 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- Posen der letzten drei Folgen nicht verwendet (203: crossed_arms-1, pointing_finger-2; 204: shirt-3, crossed_arms-2, easing-2; 205: shirt-3, resting-2, easing-1), ebenso nicht die von 202 (robot_dance-3, blazer-3, shirt-4). Prothesen-Posen (blazer-1, blazer-2, shirt-1/2) verworfen; keine Polka Dots, keine Bärte, keine Karikatur. Kleidung neu: ganz in Schwarz mit Stiefeln (Enno), braune Hose (Kuno), rosa Pullover (Silja); 203 orange/blau, 204 graublau/lila/grün, 205 lila/türkis/gelb.
- **Schauplätze neu:** Garage von innen (Rückwand mit aufgerolltem Tor, Lochwand mit Werkzeug, Regal mit Eimer und Kiste, Motorrad), Motorradhändler (Laden, blaues Motorrad). Grundformen aus `garage()`, Requisiten aus Tabler.
- Cremegrund durchgehend, Tageslicht.

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A0 Das Motorrad** `fall`–`garage` | Garage ab 0,0 s vollständig (Wand, Lochwand, Regal, Motorrad); Hook-Pillen; Enno erscheint bei seinem Namen; „über den Winter“ (Schneeflocke), Kuno, „Garage von Kuno“ | tabler:`motorbike` (Rot), `snowflake`, `tool`, `hammer`, `bucket`, `box` | `Fall · Das Motorrad` → `… Enno und sein Motorrad` → `… Über den Winter in der Garage von Kuno` | ≈ 9 | – |
| **A1 Der Verkauf** `silja`–`zweifel` | „Eines Tages“; Silja, „Zu verkaufen?“; Kuno redet (Blase), Silja redet (Blase); Kaufvertrag mit Unterschrift, „Kaufvertrag: 4.500 €“; „Kuno weiß: Enno hat nie zugestimmt“; „Silja: kein Anlass zu Zweifeln“ | tabler:`file-text`, `writing-sign` | `Fall · Silja fragt …` → `… Kuno verkauft im Namen von Enno` → `… Silja: Abgemacht!` → `… Der Kaufvertrag` → `… Kuno weiß …` → `… Silja hat keinen Anlass zu Zweifeln` | ≈ 12 | `szene_206unterschrift_1` (Freesound CC0 326961) beim Wort „unterschreiben“ |
| **A2 Samstag** `samstag`, `e1` | Enno kommt in die Garage, redet (Blase „Davon will ich nichts wissen …“), Kuno erschrickt, Silja staunt | wie A0 | `Fall · Samstag …` → `… Enno verweigert die Genehmigung` | ≈ 3 | – |
| **A3 Beim Händler** `haendler`–`frage2` | Laden, blaues Motorrad, „gleichwertig: 5.300 €“; Silja telefoniert mit Kuno (Blase „Kuno, die 800 € Mehrkosten …“); Frage-Pillen | tabler:`building-store`, `motorbike` (Blau), `phone` | `Fall · Silja kauft beim Händler: 5.300 €` → `… 800 € Mehrkosten` → `Fall · Die Frage` | ≈ 6 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Ausgangslage** `vor`–`falsus` | drei Voraussetzungen (Verweis 043), Haken „erklärt im Namen von Enno“, Kreuze Vollmacht und Rechtsschein, Block „Vertreter ohne Vertretungsmacht (falsus procurator)“ | tabler:`motorbike`, `file-text`, `license`, `user-x` | `Ausgangslage › Stellvertretung, § 164 Abs. 1 BGB › …` | Zeile für Zeile | – |
| **D Schwebezeit** `p177`–`verw` | **Wortlautkarte § 177 Abs. 1**, Block schwebend unwirksam, Punkte Genehmigung (§ 184, V ZR 194/23) und Verweigerung | tabler:`hourglass-high`, `circle-check`, `circle-x` | `§ 177 Abs. 1 BGB › …` | Zeile für Zeile | – |
| **E Aufforderung** `auff`–`schweigt` | **Wortlautkarte § 177 Abs. 2** mit fünf Markern, Punkte Frist und Schweigen | tabler:`mail-question`, `calendar`, `message-off` | `§ 177 Abs. 2 BGB › …` | Zeile für Zeile | – |
| **F Widerruf** `p178`–`adr` | **Wortlautkarte § 178**, Block „nur echte Kenntnis“, Haken Widerruf gegenüber Kuno | tabler:`arrow-back-up`, `eye`, `message-2` | `Widerruf, § 178 BGB › …` | Zeile für Zeile | – |
| **G1 Haftung** `jetzt`–`beweis` | Punkt Verweigerung, **Wortlautkarte § 179 Abs. 1** (fünf Marker), Block Beweislast (III ZR 266/11 Rn. 39) | tabler:`circle-x`, `scale`, `license` | `Haftung: § 179 Abs. 1 BGB › …` | Zeile für Zeile | – |
| **G2 Wahl** `wahl`–`stellt` | Block Erfüllung (Motorrad gehört Enno), Block Schadensersatz/Erfüllungsinteresse, Umschreibung, Fundstellen III ZR 266/11 Rn. 34, VII ZR 122/14 Rn. 24 | tabler:`arrows-split`, `motorbike`, `coin-euro` | `§ 179 Abs. 1 BGB › Wahl › …` | Zeile für Zeile | – |
| **H Abs. 2** `p1792`–`deckel` | **Wortlautkarte § 179 Abs. 2**, Block Vertrauensschaden, Beispiel Anhänger 90 €, Obergrenze | tabler:`eye-off`, `heart-handshake`, `truck`, `arrow-bar-to-up` | `§ 179 Abs. 2 BGB › …` | Zeile für Zeile | – |
| **I Abs. 3** `p1793`–`nichts` | **Wortlautkarte § 179 Abs. 3**, Fundstelle § 122 Abs. 2, Kreuze „kein Anlass zu Zweifeln“, „volljährig“ | tabler:`eye`, `user-question`, `circle-check` | `§ 179 Abs. 3 BGB › …` | Zeile für Zeile | – |
| **J1 Lösung** `loes`–`erg` | Kreuz gegen Enno, Haken gegen Kuno und volle Haftung, Rechnung 5.300 € – 4.500 €, Block „Kuno muss Silja 800 € ersetzen“ | tabler:`scale`, `circle-x`, `circle-check`, `calculator`, `coin-euro` | `Lösung › …` → `Ergebnis · Kuno zahlt 800 €` | Zeile für Zeile | – |
| **J2 Kuno zahlt** `k2` | Garage, Kuno (klagt) redet (Blase), Geldschein „800 €“, Silja | tabler:`cash-banknote` | `Fall · Kuno zahlt 800 €` | 1 | – |
| **K § 180** `p180`, `ausn` | Kündigung, Block „unzulässig, nichtig“ (VIII ZR 4/23 Rn. 37), Ausnahme (§ 180 S. 2) | tabler:`file-x`, `user-check` | `Einseitige Rechtsgeschäfte: § 180 BGB › …` | Zeile für Zeile | – |
| **L Klausurtipp** `tipp`–`tp4` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | Zeile für Zeile | – |
| **M Prüfschema** `sch`–`c8` | breite Karte: I. Silja gegen Enno (kein Vertrag), II. Silja gegen Kuno § 179 Abs. 1 mit 1.–5. | – | `Prüfschema › …` | 10 Aufbaustufen | – |
| **N Merksatz** `merke`, `mk2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | 2 | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Mund der Sprecherfigur. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („4.500 €“, „5.300 €“, „800 €“, „90 €“, „2 Wochen“, Daten, Paragrafen).
**Bewertungszeichen:** Haken/Kreuz nur bei gesprochener Bejahung/Verneinung (erklärt im Namen von Enno; keine Vollmacht; Rechtsschein scheidet aus; Widerruf auch gegenüber Kuno; Ausschlüsse greifen nicht; nicht gegen Enno; gegen Kuno; volle Haftung). Rechtsfolgen und Fristen als neutrale Aufzählungspunkte.
**Übergänge:** stumme Schiebeblenden nur zwischen den 19 Folien; innerhalb harte Schnitte und Pops; kein Zoom.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Garage, Boden aus Grundformen (`folien_206.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Das Motorrad von Enno steht über den Winter in der Garage seines Bekannten Kuno. Silja fragt, ob es zu verkaufen ist. Kuno sagt: „Enno will es loswerden. Ich verkaufe es dir in seinem Namen, für 4.500 €.“ Beide unterschreiben einen Kaufvertrag; am Samstag will Silja das Motorrad abholen.
>
> Kuno weiß, dass Enno nie zugestimmt hat. Silja hat keinen Anlass, daran zu zweifeln.
>
> Am Samstag trifft Enno in der Garage auf Silja: „Davon will ich nichts wissen. Das genehmige ich nicht!“ Silja kauft ein gleichwertiges Motorrad beim Händler für 5.300 € und verlangt von Kuno 800 € Mehrkosten.
>
> **Haftet Kuno persönlich?**
