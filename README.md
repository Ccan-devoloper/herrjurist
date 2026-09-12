# Instagram-Bot · Herr Jurist

Erstellt und veröffentlicht **vollautomatisch** täglich Beiträge (Carousels), Stories und ein Reel für
den Instagram-Kanal @herrjurist – Examenswissen für das erste und zweite juristische Staatsexamen.
Kein Inhalt wird 1:1 übernommen: Der Bot bekommt nur Themen-Skelette (Frage, Normen, Stichpunkte),
schreibt alles neu und prüft jeden Entwurf automatisch.

```
Themenpool (daten/themen.mjs)  →  Tagesplan  →  Claude schreibt  →  Prüfung  →  Chromium rendert JPEG
                                                                                        ↓
                                            Asset-Zweig „instagram-assets“ (öffentliche Bild-URLs)
                                                                                        ↓
                                            Instagram Graph API: Carousel / Story / Reel
```

## Markenkern: sortiert nach Rechtsgebiet

Jeder Beitrag gehört zu genau einem Gebiet und trägt dessen Farbe – im Profilraster erkennbar, bevor
ein Wort gelesen ist:

| Gebiet | Farbe | Fächer |
| --- | --- | --- |
| Zivilrecht | Blau `#2d5be3` | BGB AT, Schuldrecht AT/BT, Sachenrecht, Deliktsrecht, Arbeitsrecht, Familien-/Erbrecht, HGB/GesR, ZPO |
| Strafrecht | Orange `#ff7a45` | Strafrecht AT, Strafrecht BT, StPO |
| Öffentliches Recht | Grün `#23d98b` | Staatsrecht, Grundrechte, Verwaltungsrecht AT, Besonderes Verwaltungsrecht, VwGO, Europarecht |

## Unterschiede zum Schwester-Bot (Examenscampus)

Der Code stammt aus dem Steuerberater-Kanal; markenspezifisch sind vier Stellen:

| | Examenscampus | Herr Jurist |
| --- | --- | --- |
| Inhaltsquelle | Lerndaten der Webseite (`src/data`) | `daten/themen.mjs` – 795 Themen aus Pflichtfachkatalog und `daten/handbuch-2026.pdf` |
| Markenachse | Klausurtag 1/2/3 | Rechtsgebiet Zivil/Straf/Öffentlich |
| Normzitat | `§ 7 (1) S. 1 Nr. 1 lit. a) EStG` | `§ 80 Abs. 1 S. 5 VwGO` (römische Ziffern werden umgeschrieben) |
| Prüfungstermin | bundeseinheitlich, mit Countdown | keiner – Jahresrhythmus (Kampagnen Frühjahr/Herbst); `IG_EXAMEN_DATUM` schaltet den Countdown an |

Dazu ein Format, das es dort nicht gibt: **Streitstand** – Sachverhalt, Rechtsprechung gegen
Gegenansicht in zwei Spalten, Streitentscheid. Der Autor bekommt die Auflage, den Streit nur
aufzumachen, wenn er sich auswirkt.

## Was der Bot täglich tut

| | Werktag | Wochenende |
| --- | --- | --- |
| Beiträge (Carousel, 4–5 Folien, 1080×1350) | 3 (07:30 · 12:30 · 18:00) | 2 |
| Stories (1080×1920) | 9, verteilt 07:00–21:30 | 9 |

**Beitragsformate** (Wochenplan in `src/config.mjs`): Prüfungsfrage · Fehlerfalle · Prüfschema ·
Rechenweg · Mini-Fall (frei erfunden) · Gegenüberstellung · Klausurtechnik · Wochenrückblick (So) ·
**Aktuell** (Mi, Web-Recherche: BFH, BMF, Gesetzesänderungen, Prüfungstermine).

**Story-Arten**: Teaser zum Beitrag · Prüfungsfrage + Auflösung (direkt hintereinander) · Norm des Tages · Merksatz ·
Rechenweg · Begriff · Fehlerfalle · Klausurtipp · Zahl des Tages · Countdown bis zur Prüfung.

Themenwahl: gewichtet nach Examenspriorität der Webseite (🔴 60 % / 🟠 25 % / 🟢 15 %), Rotation über
alle Fächer, ein Thema frühestens nach 60 Tagen erneut (Ledger im Asset-Zweig).

**Optik**: Kanzlei-Stil, Kachel für Kachel im Wechsel Schwarz und Weiß (Schachbrett im Profil;
`IG_STIL_WECHSEL=false` schaltet das ab). Auf keiner Folie steht ein Name, ein Handle oder eine
Website – unten links bleibt Platz für das Handle, sobald `IG_HANDLE` gesetzt ist. Eine Website
(`IG_WEBSITE`) wird nur in Captions genannt und nur, wenn sie gesetzt ist. Zusätzlich zur Anweisung an
den Autor entfernt ein Filter jede Nennung von Website, Plattform oder „Link in Bio“.

**Interaktion**: Bei jedem Lauf liest der Bot die Kommentare unter den letzten 12 Beiträgen und
beantwortet neue Kommentare der letzten 14 Tage – kurz, fachlich, mit Norm, per Du. Nicht
beantwortet werden eigene Kommentare, bereits beantwortete, Spam, Werbung, reine Emojis und Bitten um
individuelle Steuerberatung. Höchstens 15 Antworten je Lauf (`IG_MAX_ANTWORTEN`), abschaltbar mit
`IG_INTERAKTION=false`. Alle Antworten stehen im Ledger.

## Einmalige Einrichtung (ca. 30 Minuten, danach nie wieder)

### 1. Instagram-Konto vorbereiten
1. Instagram-Konto in ein **Business-Konto** umwandeln (Einstellungen → Konto → Zu professionellem Konto wechseln → Unternehmen). Stories lassen sich über die API nur mit Business-Konten veröffentlichen.
2. Profil ausfüllen: Name, Bio, Website-Link (die Beiträge sagen „Link in Bio“).

### 2. Meta-App und Zugriffstoken
Empfohlen: **Instagram-API mit Instagram-Login** (kein Facebook-Seitenzwang).
1. https://developers.facebook.com → *Meine Apps* → *App erstellen* → Anwendungsfall „Instagram“ (Business).
2. Im App-Dashboard unter **Instagram → API-Einrichtung mit Instagram-Login**: das Instagram-Konto hinzufügen und die Berechtigungen `instagram_business_basic`, `instagram_business_content_publish`, `instagram_business_manage_comments` (Kommentar-Antworten), `instagram_business_manage_insights` (Lernschleife) und `instagram_business_manage_messages` (Karten per Nachricht) bestätigen.
3. Dort **„Token generieren“** → es entsteht ein **langlebiger Token (60 Tage)**. Den Token und die angezeigte **Instagram-Konto-ID** kopieren.
4. Der Bot verlängert den Token **automatisch** (spätestens 20 Tage vor Ablauf) und legt ihn verschlüsselt im Asset-Zweig ab. Dafür braucht er einen frei gewählten Schlüssel (`IG_TOKEN_KEY`, beliebige lange Zeichenkette). Es ist danach keine manuelle Erneuerung mehr nötig.

Alternative: Instagram-Konto mit Facebook-Seite verbunden → `IG_GRAPH_HOST=facebook` und einen
**Seiten-Zugriffstoken ohne Ablauf** (über einen langlebigen Nutzer-Token erzeugt) verwenden; dann entfällt
die Verlängerung ganz. Berechtigungen dort: `instagram_basic`, `instagram_content_publish`,
`instagram_manage_comments`, `pages_show_list`, `pages_read_engagement`.

### 3. Claude-API-Schlüssel
https://platform.claude.com → API-Schlüssel erstellen und Guthaben aufladen.

**Warum das Geld kostet:** Der Bot selbst ist kostenlos (GitHub Actions ist für öffentliche
Repositories gratis). Bezahlt wird nur das Schreiben der Texte: Für jeden Beitrag, jede Story-Runde,
jede Recherche und jede Kommentarantwort ruft der Bot die Claude API auf, und Anthropic rechnet das
nach verarbeiteten Wörtern (Tokens) ab – eine eigene Abrechnung mit Guthaben, unabhängig von einem
Claude-Abo.

**Plagiatsprüfung:** Gemeldet wird erst, wenn ein zusammenhängender Lauf von 13 Wörtern mit den Webseitendaten übereinstimmt oder mehrere Fundstellen zusammenkommen. Kürzere Treffer sind Fachsprache (Gesetzeswortlaut wie „Wirtschaftsgüter, die unmittelbar dem Betrieb der Personengesellschaft dienen“) und kein Abschreiben. Beanstandete Story-Entwürfe werden einmal neu geschrieben, statt den Slot zu verlieren.

**Tagesdeckel 0,25 €:** Der Bot gibt pro Tag höchstens `IG_TAGESBUDGET_USD` aus (Standard 0,27 $ ≈ 0,25 €). Die Story-Texte des ganzen Tages entstehen im ersten Lauf in einem einzigen günstigen Aufruf, bevor die teureren Beiträge das Budget beanspruchen; `state/kosten.json` hält je Tag zusätzlich fest, wofür das Geld ausgegeben wurde (`zwecke`).
Vor jedem Claude-Aufruf prüft er den Tagesverbrauch (`state/kosten.json`, Abschnitt `tage`); ist der
Deckel erreicht, warten alle weiteren Texte bis zum nächsten Tag – bereits geschriebene Inhalte werden
trotzdem veröffentlicht. Damit das reicht, läuft alles im Sparbetrieb: Beiträge, Reels, Stories,
Recherche und Kommentare mit `claude-sonnet-5` (2 $ / 10 $ je Million Tokens rein/raus), der
Faktencheck mit `claude-haiku-4-5` (1 $ / 5 $), Denkaufwand „low“ (`IG_KI_EFFORT`), höchstens eine Nachbesserungsrunde je Text, zwei
Beiträge je Tag: ein Carousel und ein Reel.

**Das Reel hat Vorrang.** Es erscheint täglich, deshalb legt der Bot `IG_REEL_RESERVE_USD`
(Standard 0,09 $) des Tagesbudgets dafür zurück, solange es aussteht. Alle anderen Aufrufe – Beiträge,
Recherche, Auffüllen – hören entsprechend früher auf und warten bis zum nächsten Tag; sobald das Reel
steht, ist die Rücklage wieder frei. An Tagen mit teurer Websuche (Format `aktuell`) kann deshalb der
Carousel-Beitrag entfallen, das Reel nicht.

| Aufruf | je Tag | Kosten (ca.) |
| --- | --- | --- |
| Beitrag oder Reel schreiben, Sonnet 5 (inkl. einer Nachbesserung) | 2 | 0,12 $ |
| Faktencheck, Haiku 4.5 | 2–4 | 0,02 $ |
| Stories schreiben, Sonnet 5 (ein Aufruf für alle) | 1 | 0,05 $ |
| Kommentare beantworten, Sonnet 5 | 1–3 | 0,02 $ |

Rund **0,20 $ pro Tag, also etwa 6 $ im Monat**; der Deckel fängt Ausreißer ab. `IG_KI_MODELL` =
`claude-opus-5` schaltet auf das präzisere Modell um – dann reicht der Deckel nur für einen Beitrag am Tag.

**Damit der Bot nie stehen bleibt:** In der Anthropic-Konsole unter *Organisations-Credits* →
**„Automatisches Neuladen aktivieren“** einschalten (z. B. 10 $ nachladen, sobald das Guthaben unter
5 $ fällt). Ohne Guthaben schlagen die Läufe fehl, bis wieder Guthaben da ist.

### 4. Secrets und Variablen im Repository setzen
GitHub → Repository → *Settings* → *Secrets and variables* → *Actions*

**Secrets**

| Name | Wert |
| --- | --- |
| `ANTHROPIC_API_KEY` | Claude-API-Schlüssel |
| `IG_ACCESS_TOKEN` | Instagram-Token aus Schritt 2 |
| `IG_ACCOUNT_ID` | Instagram-Konto-ID (Zahl) |
| `IG_TOKEN_KEY` | frei gewählter Schlüssel für den Token-Tresor |
| `ELEVENLABS_API_KEY` | *optional*: Schlüssel von elevenlabs.io – Reels sprechen dann mit ElevenLabs, solange das Monatsguthaben reicht, danach mit Piper |

**Variables** (Reiter *Variables*)

| Name | Beispiel | Bedeutung |
| --- | --- | --- |
| `IG_HANDLE` | leer | Handle unten links auf jeder Kachel – solange leer, steht dort nichts |
| `IG_STIL` | `bunt` | Stil: `bunt` (vollflächig in der Klausurtag-Farbe, Pills, mehrere Elemente) · `kanzlei` (schwarz, herrjurist-Look) · `klausurbogen` (Papier/Tinte wie die Webseite) · `campus` (Indigo/Limette). Der Workflow liest diese Variable bewusst **nicht** aus den Repo-Variablen; wer den Stil ändern will, setzt sie im Workflow unter `env`. |
| `IG_KI_RECHERCHE_SUCHEN` | `4` | Websuchen je Recherche (Format `aktuell`, Lösungsskizzen); jede Suche kostet 0,01 $ plus die Ergebnis-Tokens |
| `IG_WEBSITE` | leer | nur in Captions, nur wenn gesetzt – nie auf Kacheln |
| `IG_MARKE` | leer | Kanalname im Prompt (nicht auf den Kacheln) |
| `IG_STIL_WECHSEL` | `true` | Kanzlei-Stil im Wechsel Schwarz/Weiß |
| `IG_INTERAKTION` | `true` | Kommentare automatisch beantworten |
| `ELEVENLABS_VOICE_ID` | leer | feste Stimme für ElevenLabs; leer = der Bot sucht und lernt selbst |
| `ELEVENLABS_MODEL` | `eleven_flash_v2_5` | Sprachmodell; `eleven_v3` betont ausdrucksstärker, verbraucht aber doppelt so viel Guthaben |
| `IG_STIMME_LERNEN` | `true` | Stimme selbst suchen und über die Reichweite lernen |
| `IG_STIMME_ANZAHL` / `IG_STIMME_MESSUNGEN` / `IG_STIMME_VORSPRUNG` | `3` / `6` / `0.25` | Kandidaten, nötige Messungen je Stimme, nötiger Vorsprung zur Entscheidung |
| `IG_STIMME` | leer | Stimmanbieter erzwingen: `elevenlabs` · `piper` · `pico` · `aus` |
| `IG_REELS` | `true` | Reels abschalten mit `false` |
| `IG_REEL_TAGE` | `0,1,2,3,4,5,6` | Wochentage mit Reel (0 = So); Standard täglich |
| `IG_ZEIT_LERNEN` | `true` | Uhrzeiten lernen statt fester Zeiten |
| `IG_ZEIT_FENSTER` | `6-21` | Früheste und späteste Stunde für Beiträge |
| `IG_ZEIT_ABSTAND` | `4` | Mindestabstand zwischen zwei Beiträgen in Stunden |
| `IG_ZEIT_ERKUNDUNG` | `0.35` | Wie stark neue Uhrzeiten ausprobiert werden |
| `IG_ZEIT_REIFE_TAGE` | `2` | Mindestalter eines Beitrags, damit seine Zahlen für die Uhrzeit zählen |
| `IG_ZEIT_MESSUNGEN` / `IG_ZEIT_WIRKUNG` | `8` / `1` | Ab wann die Zahlen die Uhrzeit bestimmen statt Erkundung |
| `IG_REEL_RESERVE_USD` | `0.09` | Rücklage im Tagesbudget, damit das Reel des Tages nicht ausfällt |
| `IG_GRAPH_HOST` | `instagram` | `instagram` (Instagram-Login) oder `facebook` (Seiten-Token) |
| `IG_EXAMEN_DATUM` / `IG_EXAMEN_ENDE` | `2026-10-06` / `2026-10-08` | Countdown; nach der Prüfung auf das Folgejahr setzen (bundeseinheitlich Anfang Oktober) |

### 5. Erster Lauf
*Actions* → *Instagram-Bot* → *Run workflow* → Modus **trocken**. Der Lauf schreibt und rendert alles,
legt Bilder und Zustand im Zweig `instagram-assets` ab, veröffentlicht aber nichts. Bilder ansehen unter
`instagram-assets/bilder/<Datum>/`. Danach Modus **live** einmal manuell starten – ab dann läuft der
Zeitplan (stündlich, Cron in `.github/workflows/instagram.yml`) von selbst.

## Pausieren und Modus

- **Manueller Start** (Actions → Instagram-Bot → Run workflow): Vorgabe ist **trocken** – es wird alles
  erzeugt und in den Zweig `instagram-assets` gelegt, nichts veröffentlicht. Nur die Auswahl **live**
  veröffentlicht.
- **Zeitplan** (stündlich): veröffentlicht live. Zum Pausieren die Variable `IG_PAUSE` auf `true`
  setzen (Settings → Secrets and variables → Actions → Variables); die Läufe erzeugen dann weiter
  Bilder in den Asset-Zweig, posten aber nicht. Zum Weitermachen die Variable löschen oder auf `false`
  setzen. Alternativ den Workflow unter Actions über „…“ → „Disable workflow“ ganz anhalten.

## Betrieb

- **Ablauf je Stunde**: Plan des Tages laden (oder erzeugen) → alle Einträge, deren Uhrzeit erreicht ist, schreiben, rendern, hochladen, veröffentlichen → Zustand committen. Wurde ein Lauf verpasst, holt der nächste ihn nach. Nichts wird doppelt veröffentlicht (Status je Eintrag im Tagesplan).
- **Tageslimit** der Instagram-API: 100 Veröffentlichungen je 24 h; der Bot hält 10 Reserve.
- **Fehler**: Ein fehlgeschlagener Eintrag wird beim nächsten Lauf erneut versucht; der Workflow ist dann rot und hängt die Ausgaben als Artefakt an. Läufe, in denen nichts fällig ist, dauern unter einer Minute.
- **Zustand** (`instagram-assets/state/`): `ledger.json` (was wann veröffentlicht wurde), `plaene/<Datum>.json`, `inhalte/<Datum>-<Slot>.json` (die fertigen Texte), `token.enc` (verschlüsselter Token). Bilder älter als 21 Tage werden gelöscht.

## Lokal ausprobieren

```bash
cd social && npm install
npm run beispiele                                  # rendert die Beispielposts in allen drei Stilen nach beispiele/out
node src/planer.mjs 2026-09-14                     # Tagesplan ansehen
IG_AUTOR=beispiele IG_DRY_RUN=true IG_NO_PUSH=true node src/lauf.mjs --alles   # ganzer Tageslauf ohne API-Aufrufe
ANTHROPIC_API_KEY=… IG_DRY_RUN=true IG_NO_PUSH=true node src/lauf.mjs --alles  # mit echten Texten, ohne Veröffentlichung
npm test
```

Für das Rendern wird Chromium gebraucht: `npx playwright install chromium` (oder `CHROMIUM_PATH` setzen).

## Projektstruktur

```
social/
  src/
    config.mjs      Marke, Zeiten, Formatplan, Modell, Hosting – alles Einstellbare
    inhalte.mjs     Themenpool aus src/data (ohne Fälle, Namen, Quellenbezüge)
    planer.mjs      Tagesplan (deterministisch je Datum) + Ledger
    autor.mjs       Claude API: Beiträge, Stories, Web-Recherche; Formate
    pruefung.mjs    Eigenständigkeitsprüfung (7-Wort-Shingles gegen alle Webseitendaten, Namen, Längen)
    stile.mjs       drei Stile + Icon-Set
    vorlagen.mjs    HTML/CSS der Folien- und Story-Arten
    interaktion.mjs Kommentare lesen, Antworten formulieren, posten
    insights.mjs    Lernschleife: Statistiken lesen, Strategie ableiten
    kalender.mjs    Saisonkalender des Prüfungsjahres
    faktencheck.mjs zweiter Prüfaufruf je Text
    verteilen.mjs   Threads, YouTube, Facebook, TikTok, LinkedIn
    nachrichten.mjs Schlüsselwort → Karte per Direktnachricht
    bericht.mjs     Wochenbericht per E-Mail
    kosten.mjs      API-Verbrauch mitschreiben
    reel.mjs        Reel: Zeitplan, Frame-Animation, ffmpeg-Schnitt
    stimme.mjs      Sprecherstimme (ElevenLabs mit Wort-Zeitmarken, Kontingent + Rückfall auf Piper)
    stimmen.mjs     Stimmenauswahl: deutsche Kandidaten suchen, über die Reichweite lernen
    render.mjs      Playwright → JPEG
    hosting.mjs     Asset-Zweig: Bilder, Zustand, öffentliche URLs
    instagram.mjs   Graph API: Container, Carousel, Stories, Limit, Token-Tresor
    lauf.mjs        Tageslauf (Actions-Einstiegspunkt)
    beispiele.mjs   Beispielposts rendern
  beispiele/inhalte.json   Beispielinhalte (auch als Vorbild im Prompt)
  config/namen-sperrliste.json  zusätzlich gesperrte Namen
  fonts/            Anton, Oswald, Inter, Space Grotesk, IBM Plex (OFL)
  test/             node --test
```

## Redaktionsplan: Der Jahreszyklus des Examens

Der Bot folgt dem Prüfungsjahr (`kalender.mjs`), Markenkern ist **„Examensvorbereitung, sortiert nach
Klausurtag“**:

- **Farbe je Klausurtag** statt Schwarz/Weiß-Wechsel (`IG_FARBE_JE_KLAUSUR`, Standard an): Tag 1 Blau,
  Tag 2 Orange, Tag 3 Grün – Balken oben, Akzente, Pille, Fußzeile. So ist im Profil auf einen Blick
  sichtbar, zu welcher Klausur ein Beitrag gehört. `IG_FARBE_JE_KLAUSUR=false` stellt den Wechsel wieder her.
- **Endspurt (letzte 30 Tage)**: Klausurtechnik, Zeitmanagement, Dauerbrenner-Wiederholung
  (`formateEndspurt`), nur Themen mit Priorität „hoch“. Ziel: Reichweite und Weiterleitungen, nichts verkaufen.
- **Prüfungstage**: morgens ein ruhiger Anlass-Beitrag, um 18:30 die **Lösungsskizze** zu den
  Themen, die Kandidat:innen berichten (Web-Recherche, ausdrücklich vorläufig), am Tag danach der
  Überblick über alle drei Tage. Stories an Prüfungstagen nur Teaser – das Budget gehört der Skizze.
- **Okt–Dez**: montags „Zweiter Anlauf“ (Fehleranalyse, Lernplan, Klausuren unter Zeit).
- **Jan–30. April**: jeden zweiten Montag Entscheidungs- und Anmeldefenster (Antreten?, Lernplan,
  Fristen) – ohne Verkaufsbotschaft.
- **Mai–Sept**: Hauptlernphase mit Systematik, Schemata, Klausurtraining.
- **CTA**: Haupt-Aufforderung ist immer „Schick das deiner Lerngruppe“, dann Speichern, dann Folgen –
  Lerngruppen sind der Wachstumsmotor. Kennzahlen der Lernschleife: Saves und Shares vor Likes.
- **Samstags-Reel = Mindset** (Prüfungsangst, Blackout, Zeitdruck, Perfektionismus …) als Ersatz für
  ein Talking-Head-Video; holt Menschen ab, die Fachposts nie sehen.

Was der Bot nicht kann und von Hand zu tun ist: Bio-Text („Examensvorbereitung, sortiert nach
Klausurtag“), ein Story-Highlight je Klausur, und ein Lead-Magnet gegen E-Mail (z. B. „Die 30
Dauerbrenner, sortiert nach Klausurtag“ als PDF) – dafür braucht es eine Landingpage oder ein
Newsletter-Tool.

## Follower gewinnen: was der Bot tut – und was er bewusst nicht tut

Der Bot kann nur über die offizielle API arbeiten. Die erlaubt: veröffentlichen, eigene Kommentare
beantworten, Nachrichten an Menschen, die zuerst schreiben, Statistiken lesen. Sie erlaubt nicht:
fremden Konten folgen, fremde Beiträge liken oder kommentieren. Follow/Unfollow- und Like-Bots
arbeiten über inoffizielle Wege, verstoßen gegen die Instagram-Regeln und führen zuverlässig zur
Sperre des Kontos – das baut dieser Bot nicht.

Was er stattdessen automatisch tut:

- **Follower-Messung je Beitrag**: `follows` und `profile_visits` aus den Insights fließen mit
  hohem Gewicht in die Lernschleife; Formate, Fächer, Hooks und Uhrzeiten richten sich danach.
- **Hashtag-Lernschleife**: Jeder Beitrag merkt sich seine Hashtags. Die Strategie gewichtet Tags
  danach, welche Follower und Reichweite brachten; zwei rotierende Entdecker-Tags je Tag probieren
  Long-Tail-Begriffe aus (`config.hashtags.entdecker`). Der Wochenbericht zeigt die Tags mit den
  meisten neuen Followern.
- **Zweitreichweite**: Threads, TikTok, YouTube Shorts, Facebook, LinkedIn (siehe Weiterverteilen) –
  sobald Tokens gesetzt sind, geht jeder Beitrag und jedes Reel automatisch dorthin.
- **Profil-Check im Bericht**: fehlende Bio, fehlendes Profilbild, nicht verbundene Kanäle und – unter
  50 Followern – die drei Handgriffe, die kein Bot ersetzen kann (täglich 10 Minuten in der Nische
  kommentieren, Beiträge in Lerngruppen teilen, Kolleg:innen persönlich einladen).

## Uhrzeiten: der Bot sucht sie selbst

Beiträge erscheinen nicht zu festen Uhrzeiten, sondern dann, wann sie am besten ankommen. Nach jeder
Messung (Reichweite, Speichern, Teilen, neue Follower) merkt sich der Bot, was eine Stunde gebracht
hat – getrennt nach **Reel** und **Karussell** und, sobald genug Daten vorliegen, je Wochentag.

Die Wahl folgt dem Prinzip „optimistisch bei Unsicherheit“ (UCB1): Eine Stunde kommt dran, wenn sie
entweder gut lief oder noch kaum getestet wurde. Am Anfang wandern die Zeiten deshalb durch den Tag,
mit jeder Messung wird die Erkundung kleiner, bis die Zeiten stehen. Der Wochenbericht zeigt die
besten Stunden je Art mit Faktor zum Schnitt und Anzahl der Messungen.

Damit nicht ein paar Aufrufe die Uhrzeit bestimmen, zählen nur Beiträge, die mindestens
`IG_ZEIT_REIFE_TAGE` (2) alt sind; und die Zahlen entscheiden erst, wenn mindestens
`IG_ZEIT_MESSUNGEN` (8) Beiträge überhaupt Wirkung zeigten und im Schnitt `IG_ZEIT_WIRKUNG` (1)
Punkte je Beitrag zusammenkommen. Bis dahin verteilt der Bot die Zeiten bewusst über den Tag und
sammelt Daten – bei einem jungen Konto mit Reichweite null ist jeder Unterschied Rauschen.

Randbedingungen: Fenster `IG_ZEIT_FENSTER` (Standard 6–21 Uhr), Mindestabstand zwischen zwei
Beiträgen `IG_ZEIT_ABSTAND` (4 h), Erkundungsdrang `IG_ZEIT_ERKUNDUNG` (0.35; 0 = nur ausnutzen).
`IG_ZEIT_LERNEN=false` schaltet zurück auf die festen Startzeiten. Die Teaser-Story übernimmt
automatisch die Uhrzeit ihres Beitrags. Der Bot läuft stündlich, die Auflösung beträgt also eine
Stunde.

## Reels (Video mit Sprecherstimme)

Reels sind der größte Reichweiten-Hebel auf Instagram und erscheinen deshalb **täglich**: Der letzte
Beitrag des Tages ist immer ein Reel, davor ein Carousel. Der Bot baut sie aus einem Skript mit
6–8 Szenen: Bildschirmtext (Essenz) plus Sprechertext (Erklärung), 45–60 Sekunden, Hochformat,
mitlaufende Untertitel Wort für Wort, dezentes Klangbett, Cover-Bild. Format: MP4, H.264, AAC,
1080×1920, 30 fps – direkt über die Graph API als `REELS` veröffentlicht (`share_to_feed`).

**Normen:** Auf dem Bildschirm steht immer die Klausur-Kurzform – `§ 7 (1) S. 1 Nr. 1 lit. a) aa) EStG`.
Der Absatz in Klammern, Satz, Nummer, Buchstabe und Doppelbuchstabe abgekürzt. Das gilt für Beiträge,
Stories, Reels und Captions. `src/normen.mjs` schreibt die Angaben nach dem KI-Aufruf um, das Modell
bekommt die Regel zusätzlich im Auftrag. Im Sprechertext der Reels steht die ausgeschriebene Fassung
(„Paragraf 7 Absatz 1 Satz 1“), sonst liest die Stimme „Klammer auf eins“.

**Hook:** Die ersten zwei Sekunden entscheiden über die Reichweite eines Reels. Instagram bewertet vor
allem, wie viele Zuschauer über die Drei-Sekunden-Marke hinaus dabeibleiben. Deshalb bekommt jedes Reel
einen Hook nach festem Muster (`src/hooks.mjs`). Zehn Muster stehen zur Wahl: Fehler, direkte Frage,
Wissenslücke, steile Behauptung, Preisschild, Szene aus der Klausur, Alltag beim Lernen, Widerspruch,
Problem und Abhilfe, Vorher-Nachher. Das Muster rotiert täglich, in zehn Tagen kommt jedes einmal dran;
sobald die Lernschleife Gewichte liefert, fallen schwache Muster aus der Rotation. Der Bildschirmtext
trägt den Hook allein (höchstens sechs Wörter, weil viele ohne Ton schauen), gesprochen ist er ein Satz
mit höchstens 18 Wörtern. Begrüßungen und Ankündigungen wie „In diesem Reel“ lässt die Prüfung nicht
durch.

**Stimme des Hooks:** Der Aufhänger wird anders gesprochen als der Rest – etwas langsamer, einen Tick
lauter, mit längerer Pause am Satzende und einem Moment Stille danach. Die freie Offline-Stimme (Piper
„Thorsten“) kann nicht schauspielern; Tempo, Pause und Lautheit sind ihre Stellschrauben. Mit einem
Schlüssel für ElevenLabs (`ELEVENLABS_API_KEY`) spricht der Hook zusätzlich mit weniger Stabilität und
mehr Stil, also hörbar lebendiger.

**Cover:** Das Standbild, das im Feed und im Profilraster für das Reel steht, wird eigens
gerendert: Thema, Fach und Dauer auf der Fläche des Klausurtags, dazu ein Icon. So ist auf einen
Blick zu sehen, worum es geht; ein Bild aus dem Video zeigte sonst nur den Hintergrundclip. Alles
Wichtige liegt im mittleren 4:5-Bereich, den Instagram im Raster zeigt. Zusätzliche Kosten entstehen
nicht, die Angaben stehen schon im Reel-Skript. Schlägt das Rendern fehl, greift der bisherige Weg
über ein Videobild.

**Hintergrund-Clip (Standard, sobald einer vorliegt):** Liegen unter `state/hintergrund/` im
Asset-Zweig Videos (`*.mp4`, ideal 1080 × 1920, 30 fps, stumm, nahtlos loopbar), läuft der Clip des
Tages vollflächig im Hintergrund, geloopt über die Reel-Länge; der Inhalt liegt als Karte in der
Tagesfarbe darüber, die Untertitel als weiße Karte darunter. Mehrere Clips rotieren täglich.
Einen neuen Clip vorbereiten:
`ffmpeg -i quelle.mov -vf "scale=1080:-2,crop=1080:1920,fps=30" -an -c:v libx264 -crf 24 clip.mp4`
und im Zweig `instagram-assets` unter `state/hintergrund/` ablegen. `IG_REEL_HINTERGRUND=animation`
erzwingt die Animationen unten. Achtung Urheberrecht: nur eigenes oder lizenzfreies Material verwenden.

**Split-Screen (ohne Clip):** Das obere Drittel des Videos zeigt eine ruhige, selbst berechnete Animation, die
das Auge beschäftigt, während unten der Inhalt läuft – täglich rotierend: Labyrinth (Kugel rollt den
Lösungsweg), Marble Run (Kugeln über Rampen) und Ring (Kugel entkommt rotierenden Ringen). Kein
Fremdmaterial, alles deterministisch in den Farben des Tages-Stils. `IG_REEL_ANIMATION` =
`labyrinth` | `marble` | `ring` legt eine Animation fest. Die Untertitel stehen als Block aus drei bis
vier Wörtern fest im Bild; nur die Farbe des gesprochenen Wortes wechselt.

**Stimme – drei Varianten, automatisch gewählt** (`IG_STIMME` erzwingt eine):

| Anbieter | Qualität | Kosten | Wann aktiv |
| --- | --- | --- | --- |
| `elevenlabs` | am natürlichsten (Atmung, Betonung, Pausen), Wort-Zeitmarken für die Untertitel | kostenloses Abo: 10.000 Zeichen/Monat · Starter ≈ 5 $/Monat: 30.000 Zeichen | sobald Secret `ELEVENLABS_API_KEY` gesetzt ist **und** das Monatsguthaben reicht |
| `piper` | gut – neuronale Offline-Stimme „Thorsten“ (`de_DE-thorsten-high`), klar und ruhig, hörbar synthetischer als ElevenLabs | kostenlos | ohne ElevenLabs-Schlüssel und sobald dessen Monatsguthaben aufgebraucht ist |
| `pico` | Notlösung (SVOX Pico, Navi-Qualität) | kostenlos | nur wenn nichts anderes verfügbar ist |

**Kontingent und Rückfall.** Vor jedem Reel fragt der Bot bei ElevenLabs das verbleibende
Monatsguthaben ab (`/v1/user/subscription`). Trägt es den kompletten Sprechertext, spricht
ElevenLabs; reicht es nicht mehr, spricht **von der ersten Szene an** Piper – innerhalb eines Reels
wird die Stimme nie gewechselt, das hört jeder. Ist das Guthaben leer, merkt sich der Bot das in
`state/stimme.json` bis zum Stichtag des Abos und fragt nicht bei jedem Lauf erneut nach; danach
läuft ElevenLabs von selbst wieder an. Geht das Guthaben mitten in einem Reel aus, wird das Reel
einmal komplett offline neu gesprochen. Der Wochenbericht zeigt den Stand.

**Welche Stimme spricht?** Ist keine `ELEVENLABS_VOICE_ID` gesetzt, sucht der Bot beim ersten Lauf
selbst. Wo er sucht, hängt am Tarif: **Im kostenlosen Abo dürfen über die API nur die Stimmen des
eigenen Kontos sprechen** – die vorinstallierten mehrsprachigen, die Deutsch mit leichtem englischem
Einschlag lesen. Bibliotheksstimmen (deutsche Muttersprachler) beantwortet ElevenLabs dort mit
HTTP 402 `paid_plan_required`; erst ab Starter (≈ 5 $/Monat) stehen sie offen. Der Bot merkt das
selbst, wirft eine gesperrte Stimme aus der Liste und sucht neu. Aus der Bibliothek werden deutsche Sprecher gefiltert (Muttersprachler, erwachsen,
erzählend oder erklärend – Werbe- und Charakterstimmen fallen raus, siehe `BEWERTUNG` in
`src/stimmen.mjs`), die drei besten landen in `state/stimmen.json`. Welche davon **ankommt**,
entscheidet danach das Publikum: Jedes Reel bekommt eine der drei zugeteilt, die Stimme steht beim
Beitrag im Ledger, und aus den Insights entsteht dieselbe UCB1-Rechnung wie bei den Uhrzeiten. Hat
eine Stimme genug gemessene Reels (`IG_STIMME_MESSUNGEN`, Standard 6) **und** liegt sie deutlich vor
der zweiten (`IG_STIMME_VORSPRUNG`, Standard 0,25× Schnitt), wird sie festgeschrieben – ab dann
klingt der Kanal immer gleich. Der Wochenbericht zeigt den Zwischenstand.

Selbst hören und eingreifen: Workflow **Stimmen** (`.github/workflows/stimmen.yml`) von Hand starten.
Er listet die Kandidaten, spricht auf Wunsch je einen Probesatz nach `state/stimmen/` im Asset-Zweig
und kann mit *setzen: 2* eine Stimme sofort festlegen. Lokal: `npm run stimmen -- --proben`.
`IG_STIMME_LERNEN=false` plus `ELEVENLABS_VOICE_ID` schaltet die Suche ganz ab.

Ein Reel braucht ≈ 600 Zeichen Sprechertext, also ≈ 18.000 Zeichen im Monat. Mit dem Standardmodell
`eleven_flash_v2_5` zählt jedes Zeichen nur halb: Die 10.000 Kredite des kostenlosen Abos tragen
damit ≈ 33 Reels und reichen für den ganzen Monat – eine Stimme durchgehend, statt Mitte des Monats
auf Piper zu wechseln. `eleven_v3` klingt beim Hook ausdrucksstärker, verbraucht aber das Doppelte
und reicht dann nur für die halbe Monatsstrecke; Tarif Starter (30.000 Kredite) trägt beides.

Der Sprechertext wird bewusst fürs Sprechen geschrieben: kurze Hauptsätze, Pausen, „Also:“,
„Kurz gesagt:“ – nicht Lehrbuch. Bei Piper und Pico wird satzweise synthetisiert, damit die
Untertitel je Satz sauber sitzen. Reels sind damit **auch ohne jeden Schlüssel aktiv**
(`IG_REELS=false` schaltet sie ab).

ElevenLabs einrichten (optional, 5 Minuten):
1. https://elevenlabs.io → Konto anlegen (das kostenlose Abo genügt zum Start).
2. Unter *Voices* eine deutsche Stimme wählen (Voice Library → Deutsch → ruhige, erwachsene
   Erzählstimme) und ihre **Voice ID** kopieren. Die Stimme prägt den Kanal – anhören lohnt sich.
3. Unter *API Keys* einen Schlüssel erzeugen.
4. Im Repository: Secret `ELEVENLABS_API_KEY`, Variable `ELEVENLABS_VOICE_ID`.

Hinweis zum kostenlosen Abo: ElevenLabs verlangt dort eine Namensnennung („Elevenlabs.io“) und
erlaubt keine kommerzielle Nutzung. Wird der Kanal beworben oder verkauft er etwas, ist der Tarif
Starter der saubere Weg.

Rhythmus: An Reel-Tagen (Standard Di, Do, Sa – `reel.tage` in `src/config.mjs`) ist der 18-Uhr-Beitrag
ein Reel statt eines Carousels.

Lokal testen: `node src/reel.mjs beispiele/reel.json beispiele/reel-out` baut das Beispiel-Reel
mit der besten verfügbaren Stimme (`IG_STIMME=aus` für ein stummes Storyboard). Voraussetzung: `ffmpeg`
im Pfad (auf den GitHub-Runnern vorinstalliert) oder `FFMPEG_PATH`.

## Wachstumsbausteine (alle automatisch)

**Lernschleife.** Einmal täglich liest der Bot die Instagram-Statistiken (Reichweite, Speicherungen,
Teilungen, Likes, Kommentare, Reel-Aufrufe) für alle Beiträge der letzten 30 Tage und die Online-Zeiten
der Follower. Daraus entsteht `state/strategie.json`: Gewichte je Format, Fach und Hook-Typ
(Frage / Fehler / Zahl / Aussage) sowie die drei besten Uhrzeiten. Ab sechs bewerteten Beiträgen
passt der Planer den Wochenplan an (schwache Formate weichen dem stärksten), der Autor wählt aus
drei Hook-Varianten die nach Erfahrung beste, und die Beiträge wandern zu den Uhrzeiten, zu denen
die Follower online sind. Berechtigung in der Meta-App: `instagram_business_manage_insights`.
Abschaltbar mit `IG_LERNEN=false`.

**Reels täglich.** Jeden Tag um 18 Uhr ein Kurz-Reel (20–35 s, ein Aha-Punkt), sonntags ein langes
Schema-Reel (bis 60 s). Stimme: Piper „Thorsten“ oder ElevenLabs (siehe oben).

**Spickzettel.** Donnerstags und samstags ein Beitrag, dessen zweite Folie das komplette Prüfschema
als dichte Karte zeigt – das Format, das am meisten gespeichert und geteilt wird. Der CTA lautet
„Kommentiere SCHEMA, dann schicke ich dir die Karte als Nachricht“ (Schlüsselwort: `IG_SCHLUESSELWORT`).

**Schlüsselwort-Nachrichten.** Wer unter einem Spickzettel das Schlüsselwort kommentiert, bekommt die
Karte als Bild per Direktnachricht (private Antwort auf den Kommentar, bis 7 Tage danach möglich).
Voraussetzung: Berechtigung `instagram_business_manage_messages` mit **Advanced Access**. Dafür
verlangt Meta einmalig eine App-Prüfung („App Review“): im App-Dashboard unter *App-Prüfung →
Berechtigungen und Features* die Berechtigung beantragen, Anwendungsfall beschreiben („Automatische
Antwort mit Lernkarte auf Kommentare mit Schlüsselwort unter eigenen Beiträgen“) und ein kurzes
Bildschirmvideo hochladen. Bis zur Freigabe setzt der Bot den Versand selbständig aus und versucht
es täglich neu; alles andere läuft normal. Abschaltbar mit `IG_NACHRICHTEN=false`.

**Saisonkalender.** An Terminen des Prüfungsjahres wird der erste Beitrag des Tages zum Anlass-Beitrag:
100/60/30/14/7/3/1 Tage vor der schriftlichen Prüfung, die drei Prüfungstage, der Tag danach,
Anmeldeschluss 30. April, Vorbereitung auf die mündliche Prüfung (Mitte Januar), Jahreswechsel.
Alle Texte kennen außerdem die Phase im Prüfungsjahr (Grundlagen, Aufbau, heiße Phase, Endspurt).

**Faktencheck.** Jeder Beitrag und jedes Reel-Skript geht vor der Veröffentlichung durch einen zweiten,
unabhängigen Prüfaufruf (Normen, Fristen, Prozentsätze, Rechtsstand). Eindeutige Fehler gehen mit
Korrekturvorschlag an den Autor zurück. Abschaltbar mit `IG_FAKTENCHECK=false`.

**Suchtext.** Die erste Caption-Zeile nennt das Thema mit den Wörtern, die jemand bei Instagram oder
Google eintippen würde – Beiträge tauchen so auch in der Suche auf.

**Weiterverteilen auf andere Plattformen.** Jeder Kanal ist aktiv, sobald seine Zugangsdaten hinterlegt
sind; Fehler auf einem Kanal berühren Instagram nie.

| Kanal | Was | Einmalige Einrichtung | Secrets / Variablen |
| --- | --- | --- | --- |
| Threads | Beiträge als Bild-Carousel + Text, Reels als Video | Meta-App: Anwendungsfall „Threads API“ hinzufügen, Threads-Konto verbinden, langlebigen Token erzeugen (60 Tage; der Bot verlängert ihn wie den Instagram-Token) | `THREADS_ACCESS_TOKEN`, `THREADS_USER_ID` |
| YouTube Shorts | Reels als Shorts | Google Cloud: Projekt, YouTube Data API v3 aktivieren, OAuth-Client (Desktop), einmal per OAuth-Playground `youtube.upload` freigeben → Refresh-Token (läuft nicht ab, solange die App „In Produktion“ steht) | `YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN` |
| Facebook-Seite | Beiträge als Foto-Post, Reels als Reel | Facebook-Seite anlegen, Seiten-Token ohne Ablauf (über langlebigen Nutzer-Token) mit `pages_manage_posts`, `pages_read_engagement` | `FB_PAGE_TOKEN`, `FB_PAGE_ID` |
| TikTok | Reels (Datei-Upload) | TikTok for Developers: App mit „Login Kit“ + „Content Posting API“ (Direct Post), Rückleit-Adresse auf eigener Domain, einmal `node bin/tiktok-anmelden.mjs` → Refresh-Token (365 Tage; der Bot erneuert ihn und legt den neuesten verschlüsselt ab). Öffentlich posten darf die App erst nach der Prüfung durch TikTok – bis dahin postet der Bot nicht und meldet das im Log | `TT_CLIENT_KEY`, `TT_CLIENT_SECRET`, `TT_REFRESH_TOKEN` |
| LinkedIn | Beiträge als Text mit Titelbild auf dem eigenen Profil | LinkedIn-App mit „Share on LinkedIn“, Token mit `w_member_social` (60 Tage – LinkedIn erneuert nicht automatisch; der Wochenbericht meldet, wenn er abläuft) | `LI_ACCESS_TOKEN`, `LI_PERSON_URN` |

**TikTok einrichten (einmalig, ca. 20 Minuten plus Wartezeit auf TikTok).**
1. Auf [developers.tiktok.com](https://developers.tiktok.com) eine App anlegen (Kategorie „Content Posting“), Produkte **Login Kit** und **Content Posting API** hinzufügen, Scopes `user.info.basic`, `video.upload`, `video.publish`.
2. Unter Login Kit eine Rückleit-Adresse (Redirect URI) auf einer eigenen, in der App verifizierten Domain eintragen – eine leere Seite reicht, sie muss nur den Parameter `code` in der Adresszeile zeigen.
3. App zur Prüfung einreichen („Submit for review“). Bis zur Freigabe darf die App nur „nur ich“-Videos posten; der Bot erkennt das und wartet.
4. Auf dem eigenen Rechner: `TT_CLIENT_KEY=… TT_CLIENT_SECRET=… TT_REDIRECT_URI=… node bin/tiktok-anmelden.mjs`, die gezeigte Adresse mit dem Konto des Kanals öffnen, den `code` aus der Adresszeile im zweiten Aufruf übergeben. Der ausgegebene Refresh-Token kommt als Secret `TT_REFRESH_TOKEN` ins Repository – zusammen mit `TT_CLIENT_KEY` und `TT_CLIENT_SECRET`.
5. Ab dem nächsten Reel lädt der Bot das Video hoch (Datei-Upload, weil TikTok für URL-Abrufe eine verifizierte Video-Domain verlangt). Der Refresh-Token braucht für die Erneuerung den Schlüssel `IG_TOKEN_KEY`, der ohnehin gesetzt ist.

**Wochenbericht.** Montags beim ersten Lauf: Follower und Zuwachs, Reichweite, Beiträge/Stories/Reels,
beantwortete Kommentare, verschickte Karten, Kosten der Woche, beste Beiträge, gelernte Gewichte,
Fehler. Liegt immer unter `state/berichte/` im Asset-Zweig und geht per E-Mail, wenn SMTP
konfiguriert ist:

| Name | Typ | Beispiel |
| --- | --- | --- |
| `BERICHT_EMAIL` | Variable | deine Adresse |
| `SMTP_HOST` / `SMTP_PORT` | Variable | `smtp.gmail.com` / `587` (Gmail: App-Passwort nötig), `mail.gmx.net` / `587`, `smtp.web.de` / `587` |
| `SMTP_USER` / `SMTP_PASS` | Secret | Postfach und Passwort bzw. App-Passwort |
| `SMTP_FROM` | Variable | Absender (Standard: `SMTP_USER`) |

## Was der Bot bewusst nicht tut

- Kein automatisches Folgen, Liken oder Kommentieren fremder Konten – das verstößt gegen die
  Instagram-Nutzungsbedingungen und bringt keine echten Follower. Die offizielle API erlaubt es ohnehin nicht.
  Interaktion findet nur unter den eigenen Beiträgen statt (Antworten auf Kommentare).
- Keine Sticker (Umfragen, Quiz-Sticker) in Stories – die API unterstützt sie nicht; Quiz-Stories arbeiten
  deshalb mit Frage- und Auflösungskarte.

## Grenzen und Ehrlichkeit

Der Bot liefert Konsistenz, Qualität und Frequenz – die drei Dinge, die organisches Wachstum
tragen. Ob 5.000 Follower bis Anfang 2027 und 15.000 bis Mitte 2027 erreicht werden, hängt
zusätzlich von Faktoren ab, die kein Skript steuert (Reels, Interaktion in Kommentaren, Kooperationen
mit Repetitorien, Nischengröße: pro Jahr etwa 5.000 Prüflinge). Die Zahlen im Instagram-Insights-Reiter
sind die Messlatte; die Formate und der Wochenplan lassen sich in `src/config.mjs` jederzeit anpassen.
