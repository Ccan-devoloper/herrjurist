# Folge 058 · Heroinspritzen-Fall: Eigenverantwortliche Selbstgefährdung – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_058.py`](src/skript_058.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall, Themenplan-Format „Klassiker-Fall“. Der Hook trägt einen fiktiven Fall: Achim bringt seinem alten Freund Udo, einem erfahrenen, nüchternen Konsumenten, ein Päckchen Heroin; Udo setzt sich allein die zu hohe Dosis. Frage → Sachverhalt mit drei Varianten → der echte Fall (BGHSt 32, 262: dort die Spritzen) → § 222 (Wortlaut), Erfolg, Kausalität, Vorhersehbarkeit → eigenverantwortliche Selbstgefährdung (BGH-Satz) → Begründung (nur Tötung eines anderen, Stufenverhältnis) → Subsumtion → Grenzen: 1. überlegenes Sachwissen (Variante 1, Warnung), 2. fehlende Eigenverantwortlichkeit (Variante 2 Rausch; Irrtum/Täuschung; Lehre zum Maßstab), 3. Fremdgefährdung über die Tatherrschaft (Ausblick Gisela-Fall) → Variante 3: Ingerenz ab Bewusstlosigkeit, § 13 → § 30 Abs. 1 Nr. 3 BtMG (Wortlaut), § 29 → Klausurtipp → Schema → Merksatz.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Achim (AC), um 35 | Freund, besorgt das Heroin | `standing/easing-1`, Kopf `Short 1`, Oberteil Blau `#8DB3F2`, Jacke Grün `#8FD694`, Haut `#E8B894`. Mimiken `Calm`, `Concerned|Serious` (redet, sorgt sich), `Serious`, `Suspicious` (weiß mehr / täuscht), `Fear` (Variante 3), `Solemn`, `Smile` | `niklas` (Mann, jung) |
| Udo (UD), Mitte 50 | erfahrener Konsument | `standing/shirt-4`, Kopf `Gray Short`, Brille `Glasses`, Hemd schwarz, Hose Lila `#B8A9F5`, Haut `#F0C8A8`. Mimiken `Calm`, `Smile` (redet; ahnungslos in Variante 1), `Serious`, `Tired` (betrunken, Variante 2), `Concerned|Serious` | `helmut` (Mann, älter) |
| Lexi | Klausurtipp (warnt) und Merksatz (erklärt) | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Alle Posen blicken im Original nach rechts; Grundansicht gespiegelt (blickt nach links, zur Tafel bzw. in der Wohnung Achim zu Udo), `_r` blickt nach rechts (Udo zu Achim; Achim beim Hinausgehen zur Tür).
- **Alle Grundmimiken mit geschlossenem Mund**; offene Mimiken nur als `Concerned|Serious`. Mundzustände a/o/e nur bei `AC_redet`, `UD_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen (`shirt-1/2`, `blazer-1/2` gemieden), kein „Junkie“-Klischee: Udo ordentlich gekleidet, ruhig. 48 Figuren-PNGs in `../peeps/op_058/` (Drive-Master).
- **Namen** mit eindeutig deutscher Aussprache, in keiner Vorfolge und nicht in der Auftragsliste vergeben (gegen alle Skripte/Dokumente in `preproduction/` geprüft): Achim, Udo. Nie im Genitiv mit -s („die Entscheidung von Udo“).
- **Stimmen** nur aus dem Pool (niklas, helmut; `ela_froh`, `julia` nicht gebraucht). Vorfolgen: 057 sabrina/laura_ruhig/william/marc, 056 julia/niklas/ela_warm, 055 laura_klar/marc. `niklas` war zuletzt in 056 (zwei Folgen Abstand; einzige junge Männerstimme im Pool). Lea nicht verwendet.
- **Reale Personen:** Der Angeklagte und der Verstorbene aus BGHSt 32, 262 erscheinen nicht als Figuren; die Szene „Der echte Fall“ zeigt nur Kalender, Gerichtsgebäude und Hammer.

**Abweichung von den letzten Folgen:** 057 (Seeufer mit Steg und Booten), 056 (Lernplatz, Zimmerwand), 055 (Supermarkt). 054 spielte in einer Wohnung (Gerichtsvollzieher); hier ist es ein anderes Zimmer mit eigener Ausstattung, weil der Fall in der Wohnung des Konsumenten spielt. Hier neu: eine kleine Wohnung am Freitagabend (Fenster mit Mond, Stehlampe, Sofa, Tisch, Wohnungstür), am nächsten Morgen leer mit Rettungswagen-Symbol vor dem Fenster. Variante 3 kehrt bewusst in dieselbe Wohnung zurück (gleicher Abend, Achim bleibt). Neue Posen gegenüber 055/056 (`easing-1`, `shirt-4`).
**Abend:** nur als Pille „Freitagabend“ und Mond-Icon im Fenster auf Cremegrund (die Tageszeit trägt den Fall nicht).

## Szenen (Cremegrund)

| Szene | Ort / Handlung | Requisiten (Iconset:Name) | Tafel / Prüfpfad | Bildhalte | Geräusch |
|---|---|---|---|---|---|
| **A Wohnung** `fall`→`morgen` | Udo steht neben dem Tisch; Achim klopft, kommt herein, übergibt das Päckchen (liegt danach auf dem Tisch), beide reden, Achim geht; Udo allein, Warnschild „Dosis zu hoch“; Morgen: leere Wohnung, Sonne, Rettungswagen im Fenster, graue Pille „jede Hilfe zu spät“ | tabler:`lamp`, `sofa`, `moon-stars`, `package`, `alert-triangle`, `sun`, `ambulance`; Fenster, Tisch, Tür als Bausteine | `Fall · Freitagabend bei Udo` (ab 0,0 s) → `Fall · Am nächsten Morgen` | ≈ 20 | Klopfen (`szene_058klopfen_1`), Tür (`szene_058tuer_1`) |
| **B Die Frage** `frage`, `frage2` | Achim allein, Päckchen | tabler:`package` | `Fall · Die Frage` | 3 | – |
| **C Sachverhalt** `sv` | Karte vollständig, ≈ 11 s | – | `Sachverhalt` | 1 | – |
| **D Der echte Fall** `bgh`→`bgh3` | Tafel; Kalender „1984“, Gerichtsgebäude „BGH“, Hammer „Landgericht“, Pille „aufgehoben“ | tabler:`calendar`, `building-bank`, `gavel` | `Der echte Fall · BGHSt 32, 262` | ≈ 9 | – |
| **E § 222** `p222`→`aber` | Wortlautkarte § 222 (Marker „verursacht“); Haken Erfolg/Kausalität/Vorhersehbarkeit; roter Block; Achim, Päckchen (weggedacht = ausgegraut), Warnschild | tabler:`package`, `alert-triangle` | `A. § 222 StGB › Wortlaut / Erfolg / Kausalität / Vorhersehbarkeit / und doch keine Strafbarkeit?` | ≈ 12 | – |
| **F Selbstgefährdung** `eigen`→`ermoegl` | BGH-Satz zeilenweise; Udo mit Warnschild „eigenes Risiko“, Achim „ermöglicht“ | tabler:`alert-triangle`, `package` | `A. § 222 StGB › objektive Zurechnung › eigenverantwortliche Selbstgefährdung` | ≈ 10 | – |
| **G Begründung** `warum`→`lehre` | Waage „vorsätzlich: straflos“ / „fahrlässig: auch straflos“ | tabler:`scale` | `… › Begründung` | ≈ 8 | – |
| **H Am Fall** `subs`→`ergebnis` | Haken erfahren/nüchtern/Risiko/selbst gesetzt; grüner Block; Udo, Achim | – | `… › am Fall` | ≈ 8 | – |
| **I Variante 1** `var1`→`warn` | Achim „weiß“ (Gehirn, „sehr stark“), Udo ahnungslos (Fragezeichen); Warnschild „Warnung“ | tabler:`brain`, `help-circle`, `alert-triangle` | `B. Grenzen › 1. überlegenes Sachwissen (Variante 1)` → `› Warnung` | ≈ 12 | – |
| **J Variante 2** `var2`→`jung` | Udo müde mit zwei Biergläsern „Rausch“; Achim „Täuschung“; Lehre-Block | tabler:`beer`, `help-circle` | `B. Grenzen › 2. fehlende Eigenverantwortlichkeit (Variante 2)` → `› Irrtum, Täuschung` → `› Maßstab (Lehre)` | ≈ 10 | – |
| **K Fremdgefährdung** `fremd`→`gisela` | Achim „eigenhändig“ (Hand-Icon, keine Spritze), Krone „Tatherrschaft“, Udo „Fremdgefährdung“; Gisela-Block | tabler:`hand-finger`, `crown` | `B. Grenzen › 3. Fremdgefährdung: Tatherrschaft` → `› Ausblick: Gisela-Fall` | ≈ 10 | – |
| **L Variante 3 (Wohnung)** `var3`, `rettung` | dieselbe Wohnung am Abend; Udo nicht im Bild, nur Pulsmonitor auf dem Tisch „Udo bewusstlos“; Achim bleibt, bekommt Angst, geht zur Tür; Telefon durchgestrichen „kein Notruf“; Rettungswagen im Fenster „mit Hilfe: überlebt“ | tabler:`heart-rate-monitor`, `phone-off`, `ambulance` | `C. Variante 3 · Udo wird bewusstlos` | ≈ 8 | – |
| **M Ingerenz** `ing`→`unterl` | Tafel; Achim, Pulsmonitor „Gefahr tritt ein“, Telefon „Garant“ | tabler:`heart-rate-monitor`, `phone-call` | `C. Variante 3 › Unterlassen, § 13 StGB: Ingerenz` → `› kein Verzicht auf Rettung` → `› §§ 222, 212 StGB` | ≈ 10 | – |
| **N BtMG** `btm`→`echt` | Wortlautkarte § 30 I Nr. 3 (Marker „abgibt“, „leichtfertig dessen Tod“); Achim, Päckchen „abgegeben“, Pille „echter Fall“ | tabler:`package` | `D. § 30 Abs. 1 Nr. 3 BtMG › Wortlaut / Selbstgefährdung unerheblich / Leichtfertigkeit / Abgabe, § 29 BtMG` | ≈ 12 | – |
| **O Klausurtipp** `tipp`→`tipp3` | hellgelbe Tafel, Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Selbstgefährdung bei der objektiven Zurechnung` | ≈ 8 | – |
| **P Klausurschema** `sch`→`k5` | breite Karte, progressiv | – | `Klausurschema` | 12 | – |
| **Q Merksatz** `merke`→`m3` | Lexi erklärt, drei Marker | – | `Merksatz` | ≈ 4 | – |

**Übergänge:** stumme Schiebeblenden nur zwischen den 17 Folien; innerhalb harte Schnitte und Pops; Bewegungen: Achim kommt zur Tür herein, Achim geht hinaus (A), Achim geht ohne Notruf (L).
**Geräusche:** zwei Handlungsgeräusche (Freesound CC0), je einmal: Klopfen, als Achim in der Tür steht; Tür fällt ins Schloss, als er verschwindet. Herkunft in `geraeusche_herkunft.json`.
**Zurückhaltende Darstellung (Auftrag):** keine Spritzen, kein Konsum, keine Drogen- oder Sterbebilder; Heroin nur als geschlossenes Päckchen-Icon, die Überdosis nur als Warnschild „Dosis zu hoch“, der Tod nur als leere Wohnung mit Rettungswagen-Symbol und grauer Pille „jede Hilfe zu spät“, die Bewusstlosigkeit nur als Pulsmonitor-Icon. Das Wort „Spritzen“ fällt nur bei der Wiedergabe des echten Falls (Tafeltext, kein Bild). Keine Verharmlosung: Udo „kennt die Gefahren“, Achim „Pass auf dich auf.“
**Wortlautkarten** (FOLGE-ABLAUF Abschnitt 2): § 222 vollständig, § 30 Abs. 1 Nr. 3 BtMG mit markierten Auslassungen, wörtlich nach gesetze-im-internet.de mit Normangabe; Marker synchron zum gesprochenen Wort.

## Sachverhaltskarte (Szene C, erscheint vollständig)

> Freitagabend bringt Achim seinem alten Freund Udo (Mitte 50) wie verabredet ein Päckchen Heroin. Udo nimmt seit vielen Jahren Heroin, ist nüchtern und kennt die Gefahren. Allein setzt er sich die Dosis selbst; sie ist zu hoch. Am nächsten Morgen kommt jede Hilfe zu spät.
>
> Variante 1: Achim weiß, dass das Heroin ungewöhnlich stark ist; Udo weiß es nicht.
> Variante 2: Udo ist schwer betrunken und kann das Risiko nicht mehr abwägen.
> Variante 3: Achim bleibt. Udo wird bewusstlos, Achim geht ohne Notruf. Mit Hilfe hätte Udo überlebt.
>
> **Hat Achim Udo fahrlässig getötet?**
