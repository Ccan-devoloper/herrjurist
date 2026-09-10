/* ==========================================================================
   Zentrale Einstellungen des Instagram-Bots.
   Alles, was ein Mensch je anfassen müsste, steht hier oder in den Secrets
   (siehe README). Umgebungsvariablen überschreiben die Werte in dieser Datei.
   ========================================================================== */

const env = (name, fallback) => (process.env[name] != null && process.env[name] !== "" ? process.env[name] : fallback);

export const CONFIG = {
  /* Marke -------------------------------------------------------------- */
  marke: {
    /* Bewusst leer: Auf den Kacheln erscheint vorerst kein Name, kein Handle
       und keine Website. Sobald IG_HANDLE gesetzt ist, steht das Handle unten
       links auf jeder Kachel; IG_WEBSITE erscheint dann in den Captions. */
    name: env("IG_MARKE", ""),
    handle: env("IG_HANDLE", ""),
    website: env("IG_WEBSITE", ""),
    stil: env("IG_STIL", "bunt"),                          // bunt | kanzlei | klausurbogen | campus (siehe stile.mjs)
    /* true: Kanzlei-Stil wechselt Kachel für Kachel zwischen Schwarz und Weiß
       (Schachbrett im Profil). Für andere Stile ohne Wirkung. */
    stilWechsel: env("IG_STIL_WECHSEL", "true") === "true",
    /* Markenkern „sortiert nach Klausurtag“: jede Kachel trägt die feste Farbe
       ihres Prüfungstags (Tag 1 Blau, Tag 2 Orange, Tag 3 Grün) – farbiger
       Balken oben, Akzente, Pille, Fußzeile. Ersetzt den Schwarz/Weiß-Wechsel. */
    farbeJeKlausur: env("IG_FARBE_JE_KLAUSUR", "true") === "true",
    zeitzone: "Europe/Berlin",
  },

  /* Prüfungstermin für den Countdown. Anders als beim Steuerberaterexamen gibt
     es im Jura-Examen keinen bundeseinheitlichen Termin – die Kampagnen liegen
     je nach Land und Durchgang unterschiedlich. Deshalb standardmäßig leer:
     dann entfallen Countdown-Stories, Endspurt-Formate und Prüfungstags-
     Anlässe. Wer einen konkreten Termin bespielen will, setzt IG_EXAMEN_DATUM. */
  examen: {
    schriftlich: env("IG_EXAMEN_DATUM", ""),
    ende: env("IG_EXAMEN_ENDE", ""),
  },

  /* Tagesplan ------------------------------------------------------------ */
  plan: {
    beitraegeWerktag: Number(env("IG_BEITRAEGE_WERKTAG", 2)),
    beitraegeWochenende: Number(env("IG_BEITRAEGE_WOCHENENDE", 2)),
    storiesProTag: Number(env("IG_STORIES_PRO_TAG", 9)),   // Instagram-Limit über die API: 100 Veröffentlichungen / 24 h
    /* Lokale Uhrzeiten (Europe/Berlin), zu denen Beiträge erscheinen. */
    beitragsZeiten: ["07:30", "12:30", "18:00"],   // Startwerte, solange nichts gemessen ist
    /* Lernende Uhrzeiten: Der Bot probiert Stunden aus und behält, was
       Reichweite bringt – getrennt nach Reel und Karussell und je Wochentag.
       Siehe zeiten.mjs. */
    zeitLernen: env("IG_ZEIT_LERNEN", "true") === "true",
    zeitFenster: env("IG_ZEIT_FENSTER", "6-21"),         // frühestes und spätestes Erscheinen (lokale Stunden)
    zeitAbstandStunden: Number(env("IG_ZEIT_ABSTAND", "4")),
    zeitErkundung: Number(env("IG_ZEIT_ERKUNDUNG", "0.35")),   // 0 = nur ausnutzen, größer = mehr ausprobieren
    zeitReifeTage: Number(env("IG_ZEIT_REIFE_TAGE", "2")),     // so alt muss ein Beitrag sein, damit seine Zahlen zählen
    zeitMindestMessungen: Number(env("IG_ZEIT_MESSUNGEN", "8")),   // so viele Beiträge müssen überhaupt Wirkung zeigen, sonst wird nur ausprobiert
    zeitMindestWirkung: Number(env("IG_ZEIT_WIRKUNG", "1")),       // mittlere Punkte je Beitrag, ab denen die Zahlen die Uhrzeit bestimmen
    /* Zeitfenster, über das die Stories verteilt werden. */
    storyFenster: ["07:00", "21:30"],
    /* Ein Thema kommt frühestens nach so vielen Tagen erneut dran. Bei 795
       Themen und zwei Beiträgen am Tag ist der Pool erst nach gut 13 Monaten
       durch – 200 Tage Sperre lassen sich also mühelos halten. Kommt ein Thema
       doch wieder, bekommt der Autor die Auflage, es anders zu verpacken
       (planer.mjs, thema.zuletzt). */
    themenSperreTage: Number(env("IG_THEMENSPERRE_TAGE", "200")),
    /* Gewichtung nach Examenspriorität (🔴/🟠/🟢) – wie auf der Webseite. */
    prioritaetGewicht: { hoch: 60, mittel: 25, selten: 15 },
    /* Wöchentlicher Formatplan der Beiträge (0 = Sonntag). Ein Format aus
       autor.mjs → FORMATE. "aktuell" recherchiert im Web. */
    /* Zwei Beiträge je Tag (Tagesbudget 0,25 €); an Reel-Tagen ersetzt das
       Reel den zweiten Beitrag. */
    formateJeWochentag: {
      1: ["pruefungsfrage", "schema"],
      2: ["streitstand", "minifall"],
      3: ["aktuell", "pruefungsfrage"],
      4: ["spickzettel", "vergleich"],
      5: ["minifall", "pruefungsfrage"],
      6: ["spickzettel", "klausurtechnik"],
      0: ["wochenrueckblick", "schema"],
    },
    /* Endspurt (letzte 30 Tage vor der Prüfung): Klausurtechnik, Zeitmanagement,
       Dauerbrenner-Wiederholung – Reichweite und Weiterleitungen statt neuer Stoff. */
    formateEndspurt: {
      1: ["klausurtechnik", "pruefungsfrage"],
      2: ["pruefungsfrage", "rechenweg"],
      3: ["aktuell", "klausurtechnik"],
      4: ["spickzettel", "schema"],
      5: ["klausurtechnik", "minifall"],
      6: ["spickzettel", "klausurtechnik"],
      0: ["wochenrueckblick", "pruefungsfrage"],
    },
    endspurtTage: 30,
    /* Lernschleife: Formate/Fächer/Uhrzeiten nach Insights anpassen (state/strategie.json). */
    lernen: env("IG_LERNEN", "true") === "true",
  },

  /* Faktencheck: zweiter, unabhängiger Prüfaufruf je Beitrag/Reel --------- */
  faktencheck: {
    aktiv: env("IG_FAKTENCHECK", "true") === "true",
    /* Streng: Fällt der Faktencheck technisch aus, erscheint der Beitrag
       nicht. Bei juristischen Inhalten ist ein ungeprüfter Beitrag teurer als
       ein fehlender – ein falsch dargestellter Streitstand fällt genau der
       Zielgruppe auf, die ihn gerade lernt. IG_FAKTENCHECK_STRIKT=false
       lässt ungeprüfte Beiträge wieder durch. */
    strikt: env("IG_FAKTENCHECK_STRIKT", "true") === "true",
  },

  /* Schlüsselwort-Nachrichten: „Kommentiere SCHEMA …“ → Karte per Direktnachricht */
  nachrichten: {
    /* Aus: Beiträge fordern nicht mehr zum Kommentieren auf, um eine Karte per
       Nachricht zu bekommen. Das kommt später über einen Newsletter. */
    aktiv: env("IG_NACHRICHTEN", "false") === "true",
    schluesselwort: env("IG_SCHLUESSELWORT", "SCHEMA"),
    maxJeLauf: 25,
  },

  /* Weiterverteilen derselben Inhalte – jeder Kanal ist aktiv, sobald seine Secrets da sind */
  verteilen: {
    threads: { token: env("THREADS_ACCESS_TOKEN", ""), nutzerId: env("THREADS_USER_ID", "") },
    youtube: { clientId: env("YT_CLIENT_ID", ""), clientSecret: env("YT_CLIENT_SECRET", ""), refreshToken: env("YT_REFRESH_TOKEN", "") },
    facebook: { seitenId: env("FB_PAGE_ID", ""), token: env("FB_PAGE_TOKEN", "") },
    tiktok: { clientKey: env("TT_CLIENT_KEY", ""), clientSecret: env("TT_CLIENT_SECRET", ""), refreshToken: env("TT_REFRESH_TOKEN", "") },
    linkedin: { token: env("LI_ACCESS_TOKEN", ""), personUrn: env("LI_PERSON_URN", "") },
  },

  /* Wochenbericht per E-Mail (Montag, erster Lauf) ----------------------- */
  bericht: {
    an: env("BERICHT_EMAIL", ""),
    smtp: { host: env("SMTP_HOST", ""), port: Number(env("SMTP_PORT", 587)), user: env("SMTP_USER", ""), pass: env("SMTP_PASS", ""), von: env("SMTP_FROM", env("SMTP_USER", "")) },
    wochentag: 1,
  },

  /* Claude API ----------------------------------------------------------- */
  ki: {
    /* Sparbetrieb: Sonnet 5 für alle Texte (Beiträge, Reels, Stories,
       Recherche, Kommentare), Haiku 4.5 für den Faktencheck. Opus 5 wäre
       präziser, kostet aber das Fünffache – IG_KI_MODELL=claude-opus-5 schaltet um.
       Harter Tagesdeckel in USD (0,27 $ ≈ 0,25 €): Ist er erreicht, warten alle
       weiteren Claude-Aufrufe bis zum nächsten Tag (state/kosten.json, „tage“). */
    modell: env("IG_KI_MODELL", "claude-sonnet-5"),
    modellNeben: env("IG_KI_MODELL_NEBEN", env("IG_KI_MODELL", "claude-sonnet-5")),
    modellPruefung: env("IG_KI_MODELL_PRUEFUNG", "claude-haiku-4-5-20251001"),
    effort: env("IG_KI_EFFORT", "low"),   // „low“: etwa halbe Kosten je Entwurf, Faktencheck fängt Fehler ab
    rechercheSuchen: Number(env("IG_KI_RECHERCHE_SUCHEN", "4")),   // Websuchen je Recherche (je 0,01 $ plus Ergebnis-Tokens)
    maxVersuche: Number(env("IG_KI_VERSUCHE", "2")),
    tagesBudgetUsd: Number(env("IG_TAGESBUDGET_USD", "0.27")),
    /* Rücklage für das Reel des Tages: Es soll täglich erscheinen, darf also
       nicht daran scheitern, dass Beiträge und Recherche das Budget vorher
       aufbrauchen. */
    reelReserveUsd: Number(env("IG_REEL_RESERVE_USD", "0.09")),
  },

  /* Instagram Graph API -------------------------------------------------- */
  instagram: {
    /* Pause zwischen zwei Beiträgen beim Auffüllen. Das Stundenlimit der App
       (~200 Aufrufe) erlaubt bei ~20 Aufrufen je Carousel etwa 7 Beiträge/Stunde. */
    auffuellPauseSekunden: Number(process.env.IG_AUFFUELL_PAUSE || 480),
    /* "facebook": graph.facebook.com (Instagram-Konto mit Facebook-Seite verbunden, Page-Token ohne Ablauf)
       "instagram": graph.instagram.com (Instagram-API mit Instagram-Login, 60-Tage-Token mit Auto-Refresh) */
    host: env("IG_GRAPH_HOST", "instagram"),
    version: env("IG_GRAPH_VERSION", "v23.0"),
    kontoId: env("IG_ACCOUNT_ID", ""),
    token: env("IG_ACCESS_TOKEN", ""),
    tokenSchluessel: env("IG_TOKEN_KEY", ""),               // verschlüsselt den aufgefrischten Token im Asset-Zweig
    trockenlauf: env("IG_DRY_RUN", "false") === "true",     // true: alles erzeugen, nichts veröffentlichen
    sicherheitsabstandLimit: 10,                            // Reserve unter dem 100er-Tageslimit
  },

  /* Reels: kurze Videos aus den Beiträgen mit Sprecherstimme --------------- */
  reel: {
    /* Reels sind standardmäßig aktiv; die Stimme kommt von ElevenLabs (Schlüssel)
       oder kostenlos von Piper (im Workflow installiert). Siehe stimme.mjs. */
    aktiv: env("IG_REELS", "true") === "true",
    elevenlabsKey: env("ELEVENLABS_API_KEY", ""),
    stimme: env("ELEVENLABS_VOICE_ID", ""),   // fest eingestellte Stimme; leer = der Bot sucht und lernt selbst
    /* Flash statt v3: halber Verbrauch je Zeichen. Das kostenlose Monatsguthaben
       (10.000 Kredite) trägt damit rund 33 Reels – also den ganzen Monat mit
       einer Stimme, statt Mitte des Monats auf Piper zu wechseln. */
    modell: env("ELEVENLABS_MODEL", "eleven_flash_v2_5"),
    /* Stimmenwahl: Der Bot sucht in der ElevenLabs-Bibliothek deutsche
       Sprecher, probiert drei davon über die Reels aus und behält die, bei der
       die Zahlen stimmen (stimmen.mjs). ELEVENLABS_VOICE_ID + IG_STIMME_LERNEN=false
       stellt stattdessen eine feste Stimme ein. */
    stimmeLernen: env("IG_STIMME_LERNEN", "true") === "true",
    stimmeAnzahl: Number(env("IG_STIMME_ANZAHL", "3")),          // so viele Kandidaten laufen gegeneinander
    stimmeErkundung: Number(env("IG_STIMME_ERKUNDUNG", "0.4")),  // 0 = nur ausnutzen, größer = mehr ausprobieren
    stimmeMessungen: Number(env("IG_STIMME_MESSUNGEN", "6")),    // so viele gemessene Reels je Stimme, bevor entschieden wird
    stimmeVorsprung: Number(env("IG_STIMME_VORSPRUNG", "0.25")), // so viel muss die Beste vor der Zweiten liegen
    stimmeProbeText: env("IG_STIMME_PROBE", "Achtzig Prozent scheitern an dieser Frage. Nach Paragraf 7 Absatz 1 Satz 1 EStG beginnt die Abschreibung im Monat der Anschaffung – nicht im Januar. Merk dir das für Tag 2."),
    fps: 30,
    maxSekunden: 90,
    hintergrundmusik: env("IG_REEL_MUSIK", "true") === "true",  // dezentes, synthetisch erzeugtes Klangbett
    /* Split-Screen: das obere Drittel zeigt eine ruhige Animation, täglich
       rotierend. IG_REEL_ANIMATION=labyrinth|marble|ring legt eine fest. */
    animationen: ["labyrinth", "marble", "ring"],
    animation: env("IG_REEL_ANIMATION", ""),
    /* Hintergrund-Clips (state/hintergrund/*.mp4, 1080×1920, 30 fps, stumm):
       liegt mindestens einer vor, läuft er vollflächig im Hintergrund, der
       Inhalt liegt als Karten darüber; die Clips rotieren täglich.
       IG_REEL_HINTERGRUND=animation erzwingt die Canvas-Animationen. */
    hintergrund: env("IG_REEL_HINTERGRUND", "clip"),
    /* Wochentage, an denen der letzte Beitrag ein Reel ist (0 = So). Standard:
       jeden Tag. Reels tragen die Reichweite, deshalb erscheint täglich eines;
       der zweite Beitrag des Tages ist dann statt eines Carousels ein Reel. */
    tage: (env("IG_REEL_TAGE", "0,1,2,3,4,5,6")).split(",").map(Number),
    /* Kurz-Reels (20–35 s) an allen Tagen, sonntags ein langes Schema-Reel (bis 60 s). */
    langeTage: [0],
  },

  /* Bilder auf der Titelfolie (Pexels) ------------------------------------
     Der Autor liefert je Beitrag eine Szene; bilder.mjs sucht danach. Ohne
     Schlüssel oder ohne Treffer bleibt es bei der Icon-Bühne. */
  bilder: {
    aktiv: env("IG_BILDER", "true") === "true",
    key: env("PEXELS_API_KEY", ""),
    /* Motiv freistellen (rembg) statt als Rechteck aufzukleben – so laufen die
       Bilder aus der Kachel wie in den bisherigen Beiträgen des Kanals. */
    freistellen: env("IG_BILDER_FREISTELLEN", "true") === "true",
    /* Wenn das Freistellen misslingt: kein Bild (false) oder das Foto doch als
       Karte (true). Standard ist kein Bild – ein halb ausgeschnittenes oder
       aufgeklebtes Motiv fällt sofort auf. */
    rechteckErlaubt: env("IG_BILDER_RECHTECK", "false") === "true",
  },

  /* Interaktion: Kommentare unter den eigenen Beiträgen beantworten -------- */
  interaktion: {
    aktiv: env("IG_INTERAKTION", "true") === "true",
    maxAntwortenJeLauf: Number(env("IG_MAX_ANTWORTEN", 15)),
    beitraegeZurueck: 12,          // so viele der letzten Beiträge werden auf neue Kommentare geprüft
    maxAlterTage: 14,              // ältere Kommentare bleiben unbeantwortet
  },

  /* Bild-Hosting ----------------------------------------------------------- */
  hosting: {
    /* Instagram braucht öffentlich erreichbare JPEG-URLs. Standard: der Zweig
       "instagram-assets" dieses Repositories über raw.githubusercontent.com. */
    zweig: env("IG_ASSET_BRANCH", "instagram-assets"),
    basisUrl: env("IG_ASSET_BASE_URL", ""),                 // leer = automatisch aus dem git-Remote ableiten
    verzeichnis: env("IG_ASSET_DIR", "assets"),             // lokaler Checkout des Asset-Zweigs
  },

  /* Hashtags: kleiner fester Kern + themenabhängige aus dem Autor. */
  hashtags: {
    kern: ["#jura", "#jurastudium", "#staatsexamen", "#erstesstaatsexamen", "#zweitesstaatsexamen", "#examensvorbereitung"],
    /* Entdecker-Hashtags: Long-Tail-Tags, die täglich zu zweit rotieren – so
       wird jeder Tag ausprobiert und die Lernschleife sieht, welche neue
       Follower bringen. */
    entdecker: ["#jurastudent", "#jurastudentin", "#referendariat", "#rechtsreferendar", "#assessorexamen", "#examenskandidat", "#repetitorium", "#zivilrecht", "#strafrecht", "#öffentlichesrecht", "#verwaltungsrecht", "#staatsrecht", "#grundrechte", "#bgbat", "#schuldrecht", "#sachenrecht", "#zpo", "#stpo", "#klausurtraining", "#examenswissen", "#juratipps", "#lernenmitsystem", "#studygram", "#rechtswissenschaften"],
    maxJeBeitrag: 14,
  },
};

export default CONFIG;
