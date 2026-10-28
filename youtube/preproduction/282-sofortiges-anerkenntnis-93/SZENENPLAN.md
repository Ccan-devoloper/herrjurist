# Folge 282 · Sofortiges Anerkenntnis § 93 ZPO: Verlieren ohne Kosten – Szenenplan

**Format:** Fr · 2. Examen · ZPO · Zweckmäßigkeit (Beklagtenklausur/Anwaltsklausur). Fall nach dem Plan-Hook: Die Gartenbau Fink GmbH (Inhaber Herr Fink) hat bei Frau Mehlhorn die Hecke geschnitten und ein Beet angelegt; Rechnung 1.280 €. Zwei Wochen später, ohne Mahnung und ohne Anruf, kommt die Klage vom Amtsgericht. Frau Mehlhorn will einfach zahlen und geht zu Rechtsanwalt Rosenbaum. Ablauf laut Auftrag: 1. Hook → 2. Problem: zahlen oder anerkennen? (Erledigung, § 91a, ein Satz) → 3. § 307 ZPO (Wortlautkarte) → 4. § 93 ZPO (Wortlautkarte): (a) keine Veranlassung, (b) sofort → 5. Muster: Tenor, Teilanerkenntnis → 6. zwei typische Fehler → 7. Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Belege: [`RECHTSSTAND.md`](RECHTSSTAND.md).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Frau Mehlhorn (ME), um 35 | Kundin, Beklagte; sympathisch, will zahlen | `standing/easing-1` (Jacke Koralle `#F07A6A`, Oberteil Weiß, schwarze Hose der Pose), Kopf `Long Curly` (schwarz), Haut `#F1C9A5`; Mimiken Calm, Concerned\|Serious, Suspicious, Smile, Serious; redet (Concerned\|Serious), redetfest (Serious) | `julia` (Frau, jung) |
| Herr Rosenbaum (RO), um 35 | Rechtsanwalt, Beklagtenvertreter | `standing/blazer-3` (Blazer Marine `#44557A`, Hose `#2E3440`), Kopf `Short 2`, Haut `#B07552`; Calm, Suspicious, Smile, Serious; redet (Serious), redetfroh (Smile) | `niklas` (Mann, jung) |
| Herr Fink (FI), um 60 | Inhaber der (erfundenen) Gartenbau Fink GmbH, Klägerin; ungeduldig, nicht feindselig | `standing/crossed_arms-2` (schwarzes Oberteil, Arbeitshose Moosgrün `#6B8F71`), Kopf `No Hair 3` (Haarkranz Grau `#A8A8A8`), Haut `#EDC3A0`; Calm, Driven, Suspicious; redet (Driven) | `helmut` (Mann, älter) |
| Lexi | Moderatorin (Klausurtipp, Merksatz) | `lexi.py` (`robot_dance-1`, Bun 2, Glasses 5, gelb) | Carla (Erzählerin) |

Stimmenpool laut Auftrag: niklas, helmut, ela_froh, julia; `ela_froh` nicht gebraucht (keine weitere Sprechrolle). Grundmimiken alle mit geschlossenem Mund; Mundzustände a/o/e nur für die sprechenden Ansichten. Präfixe ME_/RO_/FI_ (nie ER_). Figuren-PNGs in `peeps/op_282` (72 Dateien, nicht im Repository).

**Namen:** Mehlhorn, Rosenbaum, Fink – eindeutig deutsch, nicht in der Koordinatorliste, nicht in `namen_reserviert.txt`, `rg -w` unter `youtube/` 0 Treffer; vor der Vertonung als „282: Mehlhorn, Rosenbaum, Fink“ eingetragen. Kein Genitiv.

**Abweichung von den letzten Folgen:** 279 (`robot_dance-3`, `sitting/mid-2`, `blazer-4`), 280 (`resting-1`, `shirt-3`, `resting-2`), 281 (`shirt-4`, `resting-1`): Posen `easing-1`, `blazer-3`, `crossed_arms-2` dort nicht verwendet; keine Polka Dots, keine Bärte, keine Prothesen-Posen. Schauplätze **Gartenbaubetrieb/Garten** (Schild, Schubkarre, Hecke, Beet, Briefkasten) und **Kanzlei** (Tisch, Regal, Waage) – neu gegenüber 270 (Tischlerei), 279 (Prüfungsraum), 280 (Meer/Brett), 281 (Mietwohnung). Kein Gerichtssaal, **kein Richterhammer** (Gericht als `building-bank`, Kostenfrage als `scale`).

**Darstellung:** Kundin sympathisch, Firmeninhaber eilig, nicht böse. Keine echten Firmen.

## Szenen

| Szene (Cues) | Ort / Bild | Requisiten (Iconset:Name) | Prüfpfad | Bildhalte (Auswahl) | Geräusch |
|---|---|---|---|---|---|
| **A1 Fall** `fall`→`me1` | geteilte Bühne: links Gartenbau Fink (Schild, Schubkarre, Pflanze), Herr Fink blickt nach rechts; Trennlinie; rechts Garten von Frau Mehlhorn (Hecke programmatisch, Beet, Briefkasten), sie blickt nach links | tabler:`garden-cart`, `plant`, `scissors`, `flower`, `mailbox`, `receipt-euro` (fliegt von Fink zu Mehlhorn, 1,0 s), `calendar-time`, `building-bank`, `bell-off`, `phone-off`, `mail` (gelb) | `Fall · Gartenbau Fink` (ab 0,0 s) → `… Keine Zahlung? Dann zum Amtsgericht` → `… Klage ohne Mahnung` | Titelpille, Fink + Schild; Garten + Frau Mehlhorn; Schere/„Hecke geschnitten, Beet angelegt“; Rechnung fliegt, „Rechnung: 1.280 €“; Kalender „2 Wochen später: kein Geld“; Blase Fink + Gericht; „ohne Mahnung“/„ohne Anruf“; gelber Brief im Briefkasten + „Klage vom Amtsgericht“; Blase Mehlhorn | Briefkastenklappe (`szene_282briefkasten_1`) |
| **A2 Kanzlei** `kanzlei`→`frage3` | Kanzlei: Fenster, Tisch mit gelbem Brief, Regal mit Büchern und Waage; Rosenbaum links (blickt nach rechts), Mehlhorn rechts | tabler:`window`, `books`, `scale`, `mail` | `Fall · In der Kanzlei` → `Einstieg · Die Frage` | Rosenbaum + „Rechtsanwalt“, Mehlhorn + „Beklagte“; Blase RO; Hook-Pille; drei Fragen | – |
| **B Sachverhalt** `sv` | Karte | – | `Sachverhalt` | Karte vollständig, ≈ 10 s | – |
| **C Problem** `zahl`→`direkt` | Tafel, ME rechts | `coins`, `file-check` | `Problem › zahlen oder anerkennen?` → `… Zahlung: Erledigung, § 91a ZPO` → `… direkter: das Anerkenntnis` | Zeilen zum Wort | – |
| **D § 307 ZPO** `w307`→`ausn` | Wortlautkarte, ME | `file-check`, `coins` | `§ 307 ZPO › Anerkenntnisurteil` → `§ 91 ZPO › Grundsatz …` → `§ 91 ZPO › Ausnahme?` | fünf Marker, Haken „verliert“, § 91, Pille „Doch: eine Ausnahme“ | – |
| **E § 93 ZPO** `w93`, `zwei` | Wortlautkarte, RO | `scale` | `§ 93 ZPO › Kosten bei sofortigem Anerkenntnis` → `… zwei Voraussetzungen` | fünf Marker, zwei Blöcke | – |
| **E1 Veranlassung** `ver`→`me2` | Tafel, ME (Blase) | `receipt-euro`, `bell-off` | `§ 93 ZPO › 1. keine Veranlassung` → `… der Fall` → `… kein Verzug, § 286 BGB` → `… keine Veranlassung gegeben` | Definition (BGH Rn. 10), typisch (Rn. 19), Haken/Kreuze Rechnung/Mahnung/Anruf, Verzug, Ergebnis | – |
| **E2 sofort** `sof`→`erg2` | Tafel mit Zeitstrahl, RO und ME (Dialog) | – | `§ 93 ZPO › 2. sofort` → `… in der Klageerwiderungsfrist` → `… Verteidigungsanzeige ohne Abweisungsantrag` → `Ergebnis › Kosten: Klägerin` | 2 Wochen → mind. 2 weitere Wochen; „sofort = …“; Haken; BGH-Fundstellen; Blase RO; Ergebnis in zwei Zeilen | – |
| **F1 Tenor** `ten`→`ten4` | Urteilsblatt auf der Tafel, RO | `file-certificate`, `scale`, `file-check` | `Muster › Tenor …` → `… Kosten: § 93 ZPO` → `… vorläufig vollstreckbar, § 708 Nr. 1 ZPO` | Überschrift, Nr. 1–3 zum Wort, „ohne Sicherheitsleistung“ | – |
| **F2 Teilanerkenntnis** `teil`→`teil8` | Tafel, ME | `lawn-mower`, `file-check`, `hourglass` | `Abwandlung › Teilanerkenntnis` → `… Teil-Anerkenntnisurteil` → `… Kosten im Schlussurteil` | 300 €/980 €, Teil-Anerkenntnisurteil, Vorbehalt, Schlussurteil | – |
| **G Fehler** `fehl`→`f2b` | Tafel, RO | `file-x`, `coins` | `Typische Fehler` → `› 1. Abweisungsantrag angekündigt` → `› 2. Sicherheitsleistung im Tenor` | zwei Kreuze, § 711-Block | – |
| **H Klausurtipp** `tipp`→`tipp5` | Tafel hellgelb, Lexi warnt | tabler:`file-text`, `scale`; Warnsymbol Streamline Freehand | `Klausurtipp · Anwaltsklausur: § 93 prüfen` | Zeilen zum Wort | – |
| **I Schema** `sch`→`k4a` | breite Karte | – | `Schema · …` → `Schema › I. … IV. Tenor` | sieben Zeilen progressiv | – |
| **J Merksatz** `merke`, `m2` | Karte, Lexi erklärt | – | `Merksatz` | fünf Marker | – |

## Sachverhaltskarte (wörtlich)

> Herr Fink, Inhaber der Gartenbau Fink GmbH, hat bei Frau Mehlhorn die Hecke geschnitten und ein Beet angelegt. Die Rechnung über 1.280 € ging ihr Anfang September zu, ohne Zahlungsfrist und ohne Hinweis auf Verzugsfolgen. Zwei Wochen später reicht die GmbH ohne Mahnung und ohne Anruf Klage beim Amtsgericht ein.
> Das Gericht ordnet das schriftliche Vorverfahren an. Frau Mehlhorn will die Rechnung einfach bezahlen und geht zu Rechtsanwalt Rosenbaum.
> Fragen: Zahlen oder anerkennen: Wer trägt die Kosten? Wie lautet der Tenor?

Kein Fiktiv-Hinweis auf Tafeln oder im Sprechtext.
