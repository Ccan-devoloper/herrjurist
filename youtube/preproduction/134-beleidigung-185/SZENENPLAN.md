# Folge 134 · Beleidigung, üble Nachrede, Verleumdung: §§ 185–187 StGB erklärt – Szenenplan

**Stand:** 04.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_134.py`](src/skript_134.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mi · Examenswissen, Format „Schema“. Fall nach dem Plan-Hook (Nachbarschafts-Chatgruppe: „Idiot“ und „schlägt seine Kinder“) → Frage und Variante → Sachverhalt → 1. Werturteil oder Tatsachenbehauptung → 2. § 185 (Wortlautkarte) mit Subsumtion und § 193/Art. 5 I GG-Abwägung für Hannelore → 3. § 186 (Wortlautkarte auszugsweise), „nicht erweislich wahr“, § 193 mit Sorgfaltspflicht für Dörte → 4. Variante § 187 (Wortlautkarte auszugsweise) → Qualifikation (offen) und Strafantrag § 194 Abs. 1 → Abgrenzungstabelle mit Ergebnis → Klausurtipp (Lexi) → Klausurschema → Merksatz (Lexi). Vorlagen: 084 (Strafrechts-Schemaformat), 025 (Meinungsfreiheit, nicht wiederholt), 131 (Hilfsfunktionen).

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Henner (HE), um 45 | der Betroffene | `standing/shirt-4` (schwarzes Hemd), Hose Blau `#8DB3F2`, Kopf `Short 3`, Haut `#E3B48C`, ohne Bart/Brille. Mimiken `Calm`, `Awe` (liest), `Concerned|Serious`, `Serious` (redet), `Solemn` | `stephan` (Mann, mittel) |
| Hannelore (HA), um 65 | schreibt „Idiot“ | `standing/blazer-4` (Blazer Grün `#8FD694`, Oberteil Weiß), Kopf `Gray Bun`, Brille `Glasses 2`, Haut `#F0C8A8`. Mimiken `Calm`, `Driven` (redet), `Suspicious`, `Serious`, `Solemn` | `hilde` (Frau, älter) |
| Dörte (DO), um 35 | behauptet die Tatsache | `standing/crossed_arms-2` (schwarzes Oberteil), Hose Lila `#B8A9F5`, Kopf `Medium Bangs`, Haut `#D9A07A`. Mimiken `Calm`, `Concerned|Serious` (redet), `Suspicious`, `Serious`, `Solemn` | `lucy` (Frau, jung) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts (Fallszene: Hannelore und Dörte zum Chatfenster; Henner von rechts zum Chatfenster).
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur bei `HE_redet`, `HA_redet`, `DO_redet` (je links/rechts) und Lexi. Keine Karikatur, keine „fiese“ Figur, keine Prothesen-Posen, keine Bärte. 62 Figuren-PNGs in `../peeps/op_134/` (Drive-Master).
- **Namen** mit eindeutig deutscher Aussprache, nicht auf der Koordinatorliste und in keiner Text-/Codedatei unter `youtube/` (`grep -rlw` in *.py, *.md, *.json, *.csv, *.txt: 0 Treffer): Henner, Hannelore, Dörte.
- **Stimmen** nur aus dem Pool (stephan, hilde, lucy; christian nicht verwendet, also nie zusammen mit stephan).
- **Kinder** kommen im Bild nicht vor; die Behauptung erscheint nur als Chat-Nachricht. Keine Gewaltdarstellung.

**Abweichung von den letzten Folgen (Kontaktbögen 131, 132 verglichen, `out/vergleich_131_132_134.png`; Posenliste 131–133):** 131 Gericht/Firma/Kommission, 132 Polizeiwache/Turnhalle, 133 Bürgschaft. Hier neu: Nachbarschafts-Chatgruppe als großes Chatfenster mit Handys. Posen `shirt-4`, `blazer-4`, `crossed_arms-2` in 131–133 nicht verwendet; kein Polka-Dots-Muster.
**Tageslicht:** durchgehend Cremegrund.

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Fall** `fall`→`var` | Bodenlinie; Chatfenster „Nachbarn Ahornweg · 63 Mitglieder“ (Karten); Henner rechts, Pille „Thema: die laute Gartenparty von Henner“; Hannelore erscheint mit Handy, Nachricht „Henner ist ein Idiot.“; Dörte mit Handy, Nachricht „Henner schlägt seine Kinder.“; Pillen „Belege: keine“, „Ob es stimmt: nicht zu klären“; Henner spricht (Blase); Frage; Variante | tabler:`messages`; fluent:`party-popper`, `mobile-phone` (3×) | `Fall · Die Chatgruppe` (ab 0,0 s) → `… Die Gartenparty` → `… Hannelore schreibt` → `… Dörte legt nach` → `… Henner stellt Strafantrag` → `… Die Frage` → `… Die Variante` | 12 | Handy vibriert beim Erscheinen beider Nachrichten (`szene_134handy_1`) |
| **B Sachverhalt** `sv` | Karte vollständig, 9,4 s | – | `Sachverhalt` | 1 | – |
| **C1 Werturteil/Tatsache** `schritt1`→`kontext` | zwei Karten (erscheinen beim Wort), Kriterium Beweisbarkeit, Sinnermittlung; Hannelore, Dörte rechts | fluent:`balance-scale`, `thought-balloon`, `magnifying-glass-tilted-left`, `speech-balloon`; tabler:`microscope` | `1. Werturteil oder Tatsache?` → `… › Werturteil` → `… › Tatsachenbehauptung` → `… › Kriterium: Beweisbarkeit` → `… › Sinn: Wortlaut, Kontext, Umstände` | 14 | – |
| **C2 Einordnung** `sub1`, `sub2` | beide Nachrichten als Chat-Karten auf der Tafel, Pillen „Werturteil“/„Tatsachenbehauptung“ | wie C1 | `1. Einordnung › …` | 6 | – |
| **D1 § 185** `p185`→`t185` | Wortlautkarte § 185 vollständig (Marker „Freiheitsstrafe bis zu einem Jahr“ bei „Strafe“), Definition, Erfasst | fluent:`balance-scale`, `speech-balloon`, `thought-balloon`, `magnifying-glass-tilted-left`; tabler:`file-text` | `A. Hannelore: § 185 StGB › …` | 8 | – |
| **D2 Hannelore** `sub185`, `vors185` | Chat-Karte, „vor der ganzen Gruppe“, Haken | fluent:`speech-balloon`; tabler:`brain` | `… › Kundgabe (+)` → `… › Vorsatz (+)` | 5 | – |
| **E § 193** `rw185`→`ehre` | Wortlautkarte § 193 (Auszug, Marker „Wahrnehmung berechtigter Interessen“), Art. 5 I GG, Hannelore spricht (Blase), Kreuze, Ergebnisblock | fluent:`balance-scale` | `A. … › II. Rechtswidrigkeit …` → `A. Hannelore: § 185 StGB (+)` | 11 | – |
| **F1 § 186** `p186`→`vors186` | Wortlautkarte § 186 (Auszug; Marker „in Beziehung auf einen anderen“, „Tatsache behauptet oder verbreitet“, „verächtlich …/öffentlichen Meinung herabzuwürdigen“), Chat-Karte, Haken | fluent:`balance-scale`, `magnifying-glass-tilted-left`, `mobile-phone`; tabler:`alert-triangle`, `brain` | `B. Dörte: § 186 StGB › I. Tatbestand …` | 9 | – |
| **F2 nicht erweislich wahr** `erweis`→`sub_erw` | Klausel als Wortlautkarte, Risiko, h. L. objektive Bedingung, Ergebnisblock | fluent:`magnifying-glass-tilted-left`, `balance-scale`; tabler:`file-certificate`, `circle-check` | `B. … › II. …` | 8 | – |
| **F3 § 193 bei Dörte** `do1`→`erg186` | Chat-Karte; Dörte spricht (Blase); Sorgfaltspflicht, Kreuze, Ergebnisblock | fluent:`balance-scale`, `magnifying-glass-tilted-left`; tabler:`file-text` | `B. … › III. Rechtswidrigkeit …` → `B. Dörte: § 186 StGB (+)` | 9 | – |
| **G1 Variante § 187** `p187`→`erg187` | Wortlautkarte § 187 (Auszug; Marker „wider besseres Wissen“, „unwahre Tatsache“), Dörte mit Denkblase „Stimmt nicht.“ | – | `C. Variante: § 187 StGB …` | 9 | – |
| **G2 Qualifikation, Strafantrag** `quali`→`antrag` | Qualifikation, „unser Sachverhalt: offen“, Wortlautkarte § 194 Abs. 1 S. 1; Henner allein rechts | fluent:`megaphone`, `mobile-phone`, `page-facing-up` | `Qualifikation · …` → `Strafantrag · § 194 Abs. 1 StGB` | 8 | – |
| **H Abgrenzung** `tab`→`erg3` | breite Tabelle Norm/Inhalt/gegenüber/Wahrheit/unser Fall, Zeile für Zeile; Ergebnis-Pillen zum Namen | – | `Abgrenzung › …` → `Ergebnis` | 8 | – |
| **I Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · …` | 6 | – |
| **J Klausurschema** `sch`→`k5` | breite Karte, progressiv | – | `Klausurschema › …` | 10 | – |
| **K Merksatz** `merke`→`m3` | Lexi erklärt, Marker | – | `Merksatz` | 7 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 16 Folien; innerhalb harte Schnitte und Pops; keine Bewegung, kein Zoom.
**Geräusche:** ein Handlungsgeräusch (Handy vibriert beim Eintreffen der Nachricht, zweimal), Freesound CC0, Herkunft in `geraeusche_herkunft.json`. Keine Geräusche bei Tafeln.
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 185 vollständig, §§ 186, 187 auszugsweise, § 193 als Auszug, § 194 Abs. 1 S. 1 – wörtlich nach gesetze-im-internet.de (Abruf 04.10.2026), mit Normangabe und „…“ bei Auslassungen.

## Sachverhaltskarte (Szene B, erscheint vollständig)

> In der Chatgruppe „Nachbarn Ahornweg“ mit 63 Mitgliedern geht es um die laute Gartenparty von Henner am Wochenende. Hannelore schreibt: „Henner ist ein Idiot.“ Dörte legt nach: „Henner schlägt seine Kinder.“ Belege hat sie keine; ob es stimmt, lässt sich nicht klären. Henner stellt Strafantrag.
>
> Variante: Dörte weiß, dass ihre Behauptung nicht stimmt.
>
> **Wer hat sich strafbar gemacht?**
