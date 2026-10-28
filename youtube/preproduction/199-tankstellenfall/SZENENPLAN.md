# Folge 199 · Tanken ohne Geld – der Tankstellenfall: Vertrag an der Zapfsäule? – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_199.py`](src/skript_199.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall · Zivilrecht/BGB AT, Klassiker-Fall. Hook nach Plan („Du tankst für 80 Euro, gehst zur Kasse – und dein Portemonnaie liegt zu Hause.“). Fiktiver Fall: Armin tankt an Säule 4 für 80 €, sein Portemonnaie liegt zu Hause; Pächterin Margarete. Ablauf: Fall → Frage, Leitentscheidung → Sachverhalt → Anspruch § 433 Abs. 2, zwei Deutungen (Wortlautkarte § 145) → der BGH-Fall (Landgericht §§ 145, 151; BGH: Vertrag schon mit dem Tanken) → Gründe (Supermarkt/Tankstelle, Interessen, objektiver Beobachter) → Eigentum § 929 S. 1 (Wortlautkarte) → Meinungsstand (BGH offen; OLG Düsseldorf / OLG Hamm, Koblenz; § 948) → Folge § 433 Abs. 2 (Wortlautkarte), § 271, Verzug ohne Mahnung, Detektivkosten → Armin sagt Bescheid (Praxis; kein Ausweis als Pfand) → Strafrecht ein Satz (Verweis 022) → Klausurtipp → Prüfschema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Armin (AR), um 35 | Kunde, hat das Portemonnaie vergessen; sympathisch, zahlungswillig, sagt offen Bescheid | `standing/easing-2` (offene Jacke Orange `#F9A66C` über schwarzem Shirt, Hose Schiefer `#3F4A5A`, weiße Turnschuhe), Kopf `Short 4`, Haut `#E3B08C`, keine Brille, kein Bart; Mimiken `Calm` (ruhig, redet), `Smile`, `Awe`, `Fear`, `Concerned\|Serious` (Sorge, klagt), `Suspicious`, `Tired`, `Solemn`, `Serious` | `marc` (Mann, mittel) |
| Margarete (MA), um 50 | Pächterin an der Kasse, freundlich | `standing/pointing_finger-1` (schwarzes Langarmshirt und Hose, erhobener Zeigefinger), Kopf `Medium Bangs 3`, Brille `Glasses 2`, Haut `#F2CDB2`; Mimiken `Calm` (redet), `Smile` (froh, redet), `Serious`, `Suspicious` | `laura_ruhig` (Frau, mittel) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

**Stimmen:** nur aus dem Pool (marc, laura_ruhig; william und sabrina nicht gebraucht). Vorfolge 198 nutzte helmut/niklas, 197 hilde/christian – keine Überschneidung. marc und laura_ruhig auch in 195 (Pool vorgegeben).
**Namen** mit eindeutig deutscher Aussprache, nicht in der Liste des Auftrags und in keinem Skript, Szenenplan, Rechtsstand, Abnahmebogen, JSON oder Cache unter `youtube/preproduction/` (Volltextsuche 04.10.2026; verworfen: Henrike (146, 159), Lothar (015), Erich (146), Hanne (005)): Armin, Margarete – nie im Genitiv. Namensschilder Armin Gelb, Margarete Grün.
**Blickrichtung:** Grundansicht gespiegelt (blickt nach links), `_r` nach rechts. A1: Armin blickt zur Säule (links), ab „Dann geht er in den Shop“ nach rechts zum Shop. A2/H1: Margarete hinter der Theke blickt nach rechts zu Armin, Armin nach links zu ihr. Tafelszenen: beide blicken nach links zur Tafel. **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `AR_redet`, `AR_klagt`, `MA_redet`, `MA_froh_redet` (je links/rechts) und Lexi. Figuren-PNGs `../peeps/op_199/` (66 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:**
- Posen der letzten drei Folgen nicht verwendet (196: robot_dance-2, blazer-4, crossed_arms-2; 197: easing-1, blazer-1; 198: easing-1, resting-1). Keine Polka Dots, keine Bärte, keine Prothesen-Posen, keine Karikatur. Kleidung neu (orange Jacke; 197 grüne Jacke, 198 lila Jacke/türkises Shirt).
- **Schauplatz Tankstelle wie in Folge 022 – bewusst**, weil der Fall dort spielt; neu gebaut: Seitenansicht mit Tankstellendach (`dach()`), Säule 4 mit Preisanzeige, blauer Kombi, Shop-Icon; Shop innen mit Regal (`regal()`), Kassentheke (`theke()`) und Kasse. 022 zeigte Shop und Säule als Querschnitt mit Bildschirm. Keine Mineralöl-Marke, kein Logo.
- Cremegrund durchgehend, Tageslicht („Samstagmorgen“).

## Szenen (Cremegrund, Tageslicht)

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A1 Zapfsäule** `fall`–`a1` | Dach, Säule 4, Kombi (ab 0,0 s); „80,00 €“ bei „achtzig“, „Portemonnaie: zu Hause“; Armin (froh) mit „Samstagmorgen“, „Selbstbedienungstankstelle“, Tropfen beim Tanken; Shop „Shop · Kasse“; Armin besorgt, redet (Blase) | tabler:`gas-station` (Rot), `car` (Blau), `wallet-off` (Hellrot), `droplet` (Gelb), `building-store` (Hellblau); Dach programmatisch | `Fall · Du tankst für 80 €` → `Fall · Armin an Säule 4` → `Fall · Ab zur Kasse` → `Fall · Armin: Portemonnaie vergessen` | 12 | `szene_199zapfen_1` (Freesound CC0 451551) beim Tanken, `szene_199klingel_1` (494565) beim Shop |
| **A2 Kasse** `marg`–`bgh2` | Regal mit Süßigkeiten/Getränken, Theke, Kasse; Margarete (Pächterin) redet, „Säule 4: 80,00 €“; Armin redet; Frage-Pillen; Leitentscheidung mit Fundstelle | tabler:`candy`, `bottle`; ph:`cash-register`; Regal, Theke programmatisch | `Fall · An der Kasse: Pächterin Margarete` → `… Margarete: 80 € an Säule 4` → `… Armin: schon gekauft?` → `… Die Frage` → `… Der Tankstellenfall des BGH` | 10 | – |
| **B Sachverhalt** `sv` | Karte vollständig, ≈ 10 s | – | `Sachverhalt` | 1 | – |
| **C Kaufvertrag: wann?** `ansp`–`d2` | Anspruch § 433 Abs. 2, Kaufvertrag; **Wortlautkarte § 145** (Marker „anträgt“, „gebunden“); zwei Deutungen als Blöcke | tabler:`coin-euro`, `gas-station`; ph:`cash-register` | `Anspruch: § 433 Abs. 2 BGB › Kaufvertrag? › …` | Zeile für Zeile | – |
| **D Der Fall des BGH** `urteil`–`nkasse` | Sachverhalt BGH (10,01 €, Schokoriegel, 2 Vignetten, Detektivbüro), Landgericht (§§ 145, 151), BGH bestätigt, Kreuz „nicht erst an der Kasse“ | tabler:`gas-station`, `candy`, `gavel`; ph:`detective` | `BGH, 4.5.2011 – VIII ZR 171/10 › …` | Zeile für Zeile | – |
| **E Gründe** `gr`–`armfalsch` | Supermarkt/Tankstelle als Blöcke, Haken Betreiber/Kunde, grüner Block objektiver Beobachter; „Armin hat schon gekauft“ | tabler:`basket`, `droplet`, `gas-station`, `car`, `receipt-euro` | `Kaufvertrag beim Tanken › Gründe › …` → `Ergebnis · Armin hat schon gekauft` | Zeile für Zeile | – |
| **F1 Eigentum** `eig`–`einig` | § 433 Abs. 1 verpflichtet nur; **Wortlautkarte § 929 S. 1** (Marker „übergibt“, „einig“); Haken Übergabe; Block „Einigung: schon beim Tanken?“ | tabler:`droplet`, `car`, `users` | `Eigentum am Benzin: § 929 Satz 1 BGB › …` | Zeile für Zeile | – |
| **F2 Meinungsstand** `offen`–`egal` | BGH offen (Rn. 16); Ansicht 1 (OLG Düsseldorf), Ansicht 2 (OLG Hamm, Koblenz), Konstruktionen, Vermischung §§ 948, 947; „Für die Zahlungspflicht: egal“ | tabler:`gavel`, `droplet`, `coin-euro`, `receipt-euro` | `§ 929 Satz 1 › Einigung: Meinungsstand › …` | Zeile für Zeile | – |
| **G Folge** `w433`–`kosten` | **Wortlautkarte § 433 Abs. 2** (Marker „Kaufpreis“); fällig sofort § 271; Verzug ohne Mahnung (Leitsatz 2); Detektivkosten | tabler:`coin-euro`, `car`; ph:`detective` | `Folge: Kaufpreis, § 433 Abs. 2 BGB › …` | Zeile für Zeile | – |
| **H1 Kasse** `praxis`, `g2` | zurück an der Kasse; Armin sagt Bescheid; Margarete (froh) redet, Notizblock | tabler:`notes` | `Fall · Armin sagt Bescheid` → `Fall · Margarete notiert Name und Adresse` | 3 | – |
| **H2 Praxis und Strafrecht** `keinrs`–`str2` | „Praxis, kein Rechtssatz“; Kreuz Personalausweis (§ 1 Abs. 1 S. 3 PAuswG); Haken „nicht strafbar“; Block (versuchter) Betrug mit Fundstelle, Verweis Video „Tankbetrug“ | tabler:`notes`, `id-off`, `user-check`, `gavel` | `Praxis und Strafrecht › …` | Zeile für Zeile | – |
| **I Klausurtipp** `tipp`–`tp3` | hellgelbe Tafel, Lexi warnt (redet) | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | Zeile für Zeile | – |
| **J Prüfschema** `sch`–`c7` | breite Karte, I. (1.–3.), II. (1.–2.) | – | `Prüfschema › …` | 8 Aufbaustufen | – |
| **K Merksatz** `merke`, `mk2` | Lexi erklärt (redet), zwei Sätze mit Marker | – | `Merksatz` | Satz für Satz | – |

**Blasen:** Stil C (`bausteine.blase`, Rückfall auf Stil e per Assertion ausgeschlossen), Schwanzspitze außerhalb der Blase am Kopf/Mund der Sprecherfigur. **Zahlen** auf Tafeln, Pillen und Blasen in Ziffern („80 €“, „Säule 4“, „10,01 €“, „2 Vignetten“, „4.5.2011“, Paragrafen).
**Übergänge:** stumme Schiebeblenden nur zwischen den 14 Folien; innerhalb harte Schnitte und Pops; kein Zoom.
**Lizenzen der Requisiten:** Tabler Icons (MIT), Phosphor (MIT), Haken/Kreuz Fluent Emoji High Contrast (MIT), Warnsymbol Streamline Freehand (CC BY 4.0, Namensnennung in `beschreibung.txt`). Boden, Dach, Regal und Theke aus Grundformen (`folien_199.py`).

## Sachverhaltskarte (Szene B, erscheint vollständig)

> Samstagmorgen an einer Selbstbedienungstankstelle: Armin tankt an Säule 4 seinen Kombi voll, für 80 €. Dann geht er in den Shop zur Kasse und merkt, dass sein Portemonnaie zu Hause auf dem Küchentisch liegt. Er will bezahlen, kann es aber gerade nicht.
>
> Pächterin Margarete verkauft den Kraftstoff im eigenen Namen. Sie sagt: „80 € an Säule 4. Das Benzin ist aber schon in Ihrem Tank.“
>
> Armin fragt: „Heißt das, ich habe schon gekauft? Bezahlt wird doch erst hier an der Kasse.“
>
> **Wann ist der Kaufvertrag geschlossen – und wem gehört das Benzin?**
