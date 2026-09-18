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
       ihres Rechtsgebiets (Zivilrecht Blau, Strafrecht Orange, Öffentliches
       Recht Grün) – farbiger
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
    beitragsZeiten: ["09:30", "12:30", "19:30"],   // nur ohne Lernschleife (IG_ZEIT_LERNEN=false); sonst zeiten.mjs
    /* Lernende Uhrzeiten: Der Bot probiert Stunden aus und behält, was
       Reichweite bringt – getrennt nach Reel und Karussell und je Wochentag.
       Siehe zeiten.mjs. */
    zeitLernen: env("IG_ZEIT_LERNEN", "true") === "true",
    zeitFenster: env("IG_ZEIT_FENSTER", "7-22"),         // frühestes und spätestes Erscheinen (lokale Stunden)
    /* Die Untergrenze haengt an der Weckkette, nicht am Geschmack: Der erste
       Lauf des Tages liegt um 05:35 UTC, im Sommer also 07:35 Ortszeit. Ein
       Beitrag um 07:30 geht damit um 07:35 raus - fuenf Minuten spaeter, wie
       jeder andere Slot auch. Ein Beitrag um 06:30 wartete dagegen bis 07:35
       und stand 65 Minuten zu spaet im Feed; genau das ist am 14.09. auf dem
       Steuerkanal passiert. Deshalb 7 und nicht 6 - und nicht 8, denn die
       Sieben ist erreichbar und als Sendezeit zu wertvoll, um sie der
       Lernschleife vorzuenthalten.
       Aendert sich der Cron in .github/workflows/instagram.yml, muss dieser
       Wert mitwandern - ein Test haelt beides zusammen. */
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
    /* Eigene Sperre für Story-Themen. Kürzer als bei Beiträgen, weil täglich
       neun Stories laufen und der Vorrat je Art sonst nicht reicht; greift der
       Vorrat nicht, kommt die Art an diesem Tag seltener dran (planer.mjs). */
    storySperreTage: Number(env("IG_STORYSPERRE_TAGE", "60")),
    /* Story-Arten, die nur alle n Tage laufen. Rechenwege sind in Jura die
       Ausnahme - fünf Themen im ganzen Pool. Täglich wäre das alle fünf Tage
       dieselbe Formel; alle drei Wochen ist es eine Abwechslung. */
    storyArtTakt: { formel: 21 },
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
    /* Zweitmeinung: Fehlerbefunde des Prüfers beurteilt das stärkere Modell,
       bevor ein Entwurf verworfen wird. IG_FAKTENCHECK_ZWEITMEINUNG=false
       schaltet sie ab; IG_KI_MODELL_ZWEITMEINUNG wählt das Modell. */
    zweitmeinung: env("IG_FAKTENCHECK_ZWEITMEINUNG", "true") === "true",
    zweitmeinungModell: env("IG_KI_MODELL_ZWEITMEINUNG", ""),
    /* Prüfer aus einem anderen Haus (Beschluss des Betreibers, 18.09.).
       Der Preis ist der zweite Grund; der erste wiegt schwerer: Prüfer und
       Autor waren bisher dasselbe Modell derselben Familie. Was dem Modell
       beim Schreiben unterläuft, fällt ihm beim Lesen seltener auf - genau
       so ging am 16.09. der Kenntnisträger des § 1365 BGB durch. Ein Prüfer
       eines anderen Anbieters hat diese Blindstelle nicht.

       Die Zweitmeinung bleibt bei Claude: Erst prüft der eine, dann
       beurteilt der andere die Einwände. Zwei Häuser, zwei Blickwinkel.

       Fällt OpenAI aus, übernimmt Claude von selbst.
       GEMESSEN am 18.09. (Workflow "Prüfer · Vergleichsprobe", zwei Texte:
       einer mit dem bekannten § 1365-Fehler, einer ohne):

         Prüfer            findet den Fehler   Falschbefunde   je Prüfung   Dauer
         claude-sonnet-5   ja, als Fehler      keine           0,010 $       5 s
         gpt-5             ja, als Fehler      keine           0,055 $      50 s
         gpt-5-mini        nur als Hinweis     zwei            0,010 $      40 s

       gpt-5-mini hat zwei richtige Sätze für falsch erklärt (§ 1365 BGB gelte
       nicht nur im gesetzlichen Güterstand; die Rechtsfolge sei Nichtigkeit
       statt schwebender Unwirksamkeit) und den wirklichen Fehler auf einen
       Hinweis herabgestuft - ein Hinweis hält nichts auf. gpt-5 prüft sauber
       und fand sogar das ernsthafte Bemühen nach § 24 Abs. 1 Satz 2 StGB,
       kostet aber das Fünffache.

       Deshalb bleibt die Voreinstellung vorerst bei Claude, das seit dem
       18.09. mit "low" prüft und damit so viel kostet wie gpt-5-mini. Der
       Weg zu OpenAI ist gebaut und mit einer Variablen geschaltet:
       IG_FAKTENCHECK_ANBIETER=openai, Modell über
       IG_FAKTENCHECK_OPENAI_MODELL. Die Probe lässt sich jederzeit
       wiederholen, wenn neue Modelle erscheinen. */
    anbieter: env("IG_FAKTENCHECK_ANBIETER", "claude"),
    openai: {
      key: env("OPENAI_API_KEY", ""),
      /* Gemessen wird, nicht geglaubt: bin/pruefer-probe.mjs stellt die
         Modelle an denselben Text mit bekanntem Fehler. */
      modellStreng: env("IG_FAKTENCHECK_OPENAI_MODELL", "gpt-5-mini"),
      modellLocker: env("IG_FAKTENCHECK_OPENAI_MODELL_LOCKER", "gpt-5-mini"),
      aufwand: env("IG_FAKTENCHECK_OPENAI_AUFWAND", "medium"),
      zeitlimitMs: Number(env("IG_FAKTENCHECK_OPENAI_ZEITLIMIT_MS", "120000")),
    },
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
    /* Der strenge Prüfer für Beiträge, in denen gerechnet wird. Am 14.09. ist
       eine falsche Erbquote durchgelaufen: Haiku prüfte, was Sonnet
       geschrieben hatte, und sah die vertauschte Quote des § 1931 BGB nicht.
       Rechenfolien sind selten (1 von 13 Beiträgen in fünf Tagen), deshalb
       kostet die Eskalation im Schnitt fast nichts – am Tag, an dem sie
       greift, etwa 0,009 $ mehr. */
    modellPruefungStreng: env("IG_KI_MODELL_PRUEFUNG_STRENG", "claude-sonnet-5"),
    effort: env("IG_KI_EFFORT", "low"),   // „low“: etwa halbe Kosten je Entwurf, Faktencheck fängt Fehler ab
    /* Messversuch ab 18.09. (Beschluss des Betreibers): Beiträge und Reels
       schreiben mit „medium", Stories bleiben bei „low". In der Nacht zum
       17.09. brauchte ein Beitrag mit „low" drei Prüfrunden und ein
       Neuschreiben (0,19 $). Ein Entwurf mit „medium" kostet mehr je
       Aufruf, könnte aber Prüfrunden sparen - ob das unterm Strich billiger
       ist, hat nie jemand gemessen. Verglichen wird nach einer Woche über
       state/kosten.json: autor + faktencheck je Tag gegen die Woche davor.
       IG_KI_EFFORT_BEITRAG=low stellt zurück. */
    effortBeitrag: env("IG_KI_EFFORT_BEITRAG", "medium"),
    /* Reels getrennt: In der Nacht zum 18.09. kostete das Reel-Skript mit
       "medium" auf beiden Kanälen mehr als die Obergrenze je Beitrag (0,116 $
       und 0,143 $, 7.800 bzw. 10.100 Ausgabe-Token für 140 Wörter) und wurde
       zurückgestellt. Mit "low" lag es am Vortag bei 0,070 $. */
    effortReel: env("IG_KI_EFFORT_REEL", "low"),
    rechercheSuchen: Number(env("IG_KI_RECHERCHE_SUCHEN", "4")),   // Websuchen je Recherche (je 0,01 $ plus Ergebnis-Tokens)
    maxVersuche: Number(env("IG_KI_VERSUCHE", "2")),
    /* Tagesdeckel. Von 0,27 auf 0,32 $ angehoben, nachdem am 15.09. gemessen
       war, was der strenge Prüfer wirklich kostet: Die Faktenchecks lagen an
       dem Tag bei 0,0528 $ gegen 0,0174 $ am 14.09., als noch überwiegend das
       günstige Modell prüfte - also rund 0,035 $ mehr. Genau dieser Betrag
       fehlte danach für die gezeichneten Motive: 0,2529 $ gingen in Texte und
       Prüfung, für "bild" blieb 0,0000 $, und die Beiträge trugen Icons.
       Beides zusammen geht in 0,27 $ nicht auf. Entschieden wurde für die
       strenge Prüfung ALLER Formate einschließlich der Reels - lieber fünf
       Cent mehr am Tag als ein fachlicher Fehler im Feed. */
    tagesBudgetUsd: Number(env("IG_TAGESBUDGET_USD", "0.32")),
    /* Rücklage für das Reel des Tages: Es soll täglich erscheinen, darf also
       nicht daran scheitern, dass Beiträge und Recherche das Budget vorher
       aufbrauchen. */
    reelReserveUsd: Number(env("IG_REEL_RESERVE_USD", "0.11")),
    /* Obergrenze je Beitrag. Ein normaler Beitrag kostet 0.06-0.085 $; wer
       0.10 $ reisst, hat sich in Korrekturrunden verfangen und wird
       zurueckgestellt, statt den Tag aufzuessen (17.09.: ein Beitrag 0.19 $,
       danach fielen b2 und alle neun Stories aus). */
    /* Obergrenze je Beitrag. 0,10 $ stammte aus der Zeit, als ein Entwurf
       0,05 $ und seine Prüfung 0,01 $ kostete. Gemessen am 18.09.: Schreiben
       0,077 $, Prüfung 0,034 $ - zusammen 0,111 $. Ein einziger Beitrag passte
       damit nicht mehr in einen Lauf, und der Beitrag b2 wurde an diesem Tag
       viermal angefasst, ohne je zu erscheinen: Jeder Lauf schrieb oder
       prüfte, riss die Grenze und stellte zurück.

       0,15 $ trägt Schreiben plus zwei Prüfrunden. Die Grenze bleibt, wofür
       sie gedacht war: Am 17.09. verbrauchte EIN Beitrag mit drei Prüfrunden
       und einer Neufassung 0,19 $ und nahm neun Stories mit. Das fängt sie
       weiterhin ab. */
    maxJeBeitragUsd: Number(env("IG_MAX_JE_BEITRAG_USD", "0.15")),
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
    /* App-ID und App-Geheimnis, nur für die Token-Prüfung. debug_token ist der
       einzige Weg, die Berechtigungen eines Tokens ABZULESEN statt sie zu
       erraten - und der Aufruf verlangt ein App-Token aus beidem. Über
       graph.instagram.com antwortet debug_token mit "Application does not have
       permission for this action"; über graph.facebook.com klappt er.
       Der Bot braucht beides für den Betrieb nicht. Fehlen sie, sagt die
       Prüfung das und verlässt sich auf den Kantentest. */
    appId: env("IG_APP_ID", ""),
    appGeheim: env("IG_APP_SECRET", ""),
    tokenSchluessel: env("IG_TOKEN_KEY", ""),               // verschlüsselt den aufgefrischten Token im Asset-Zweig
    trockenlauf: env("IG_DRY_RUN", "false") === "true",     // true: alles erzeugen, nichts veröffentlichen
    sicherheitsabstandLimit: 10,                            // Reserve unter dem 100er-Tageslimit
  },

  /* Interaktive Stories über die private Schnittstelle (instagrapi) ---------
     Die offizielle Publishing-API kennt keinen nativen Umfrage-Sticker. Eine
     ins Bild gemalte Umfrage sieht aus wie eine, ist aber nicht antippbar und
     liefert keine Ergebnisse. Für echte Interaktion führt kein Weg an der
     privaten Schnittstelle vorbei - und die ist nicht freigegeben.

     Deshalb ist das hier ein ZUSATZ, nie der einzige Weg: Scheitert der
     private Weg, geht dieselbe Story über die Graph API raus wie bisher. Und
     der Schalter steht auf aus, bis er mit einem Testkonto belegt ist.

     Die Zugangsdaten sind ein viel größeres Geheimnis als ein API-Token: Sie
     öffnen das ganze Konto. Sie gehören in GitHub-Secrets und nirgendwo sonst
     hin. Die Sitzung liegt verschlüsselt im Asset-Zweig (IG_TOKEN_KEY) - eine
     bestehende Sitzung sieht für Instagram nach dem immer gleichen Gerät aus,
     eine Neuanmeldung von wechselnder Runner-IP nach einer Übernahme. */
  interaktiv: {
    aktiv: env("IG_INTERAKTIV", "false") === "true",
    nutzer: env("IG_PRIVAT_USER", ""),
    passwort: env("IG_PRIVAT_PASS", ""),
    /* Welche Story-Arten eine Umfrage bekommen. "frage" trägt im Bild schon
       A/B/C mit den ausformulierten Antworten - der Sticker muss die langen
       Antworten also gar nicht tragen, er fragt nur ab. */
    arten: env("IG_INTERAKTIV_ARTEN", "frage").split(",").map((a) => a.trim()).filter(Boolean),
    stickerFrage: env("IG_INTERAKTIV_FRAGE", "Was stimmt?"),
    /* Nach einer Challenge oder einer Bremse von Instagram: so lange gar nicht
       erst wieder versuchen. Eine Wiederholungsschleife gegen eine
       Anmeldesperre ist genau das, was ein Konto endgültig kostet. */
    sperreStunden: Number(env("IG_INTERAKTIV_SPERRE_H", 24)),
    /* Die Sitzung, einmal vom eigenen Rechner erzeugt (bin/interaktiv-anmelden.mjs),
       verschlüsselt als Secret. Sie ist die Saat: Fehlt im Asset-Zweig eine
       Sitzung, wird diese genommen. */
    sitzungSaat: env("IG_PRIVAT_SITZUNG", ""),
    /* EIGENER Schlüssel für den Sitzungstresor, nicht IG_TOKEN_KEY. Zwei
       Gründe: Die Sitzung wird am eigenen Rechner erzeugt, also muss der
       Schlüssel dort bekannt sein - IG_TOKEN_KEY ist er nicht, und ihn dafür
       zu wechseln hieße, am Token-Tresor des Bots zu rühren. Und es sind
       zwei verschiedene Geheimnisklassen: ein API-Token gegen ein ganzes
       Konto. Fehlt er, gilt ersatzweise IG_TOKEN_KEY. */
    schluessel: env("IG_PRIVAT_KEY", env("IG_TOKEN_KEY", "")),
    /* Darf sich der Lauf mit Name und Passwort NEU anmelden? Standard nein.
       Am 17.09. hat Instagram die Erstanmeldung vom GitHub-Runner mit
       "Please wait a few minutes" abgewiesen - Rechenzentrums-IP. Eine
       Neuanmeldung gehört an einen normalen Anschluss, nicht in die CI. */
    neuanmeldung: env("IG_PRIVAT_NEUANMELDUNG", "false") === "true",
    zeitlimitSekunden: Number(env("IG_INTERAKTIV_TIMEOUT", 180)),
    python: env("IG_PYTHON", "python3"),
  },

  /* Wissensbasis: verschlüsselter Volltext als Belegstelle beim Schreiben ---
     Das Repo ist öffentlich, das Material nicht: daten/wissen/*.enc liegt im
     Tresor, der Schlüssel steht nur im GitHub-Actions-Secret IG_WISSEN_KEY.
     Fehlt er, schreibt der Bot wie vorher – ohne Belegstelle, aber er
     schreibt. Ein fehlender Schlüssel darf keinen Beitrag kosten. */
  wissen: {
    schluessel: env("IG_WISSEN_KEY", ""),
    /* Wie viel Text das Modell je Beitrag mitbekommt. 4000 Zeichen sind rund
       1200 Token, bei Sonnet also gut 0,004 $ – bei drei Beiträgen am Tag
       etwa 0,012 $ von 0,27 $. Genauigkeit für Kleingeld. */
    zeichen: Number(env("IG_WISSEN_ZEICHEN", "4000")),
    /* Darunter gilt ein Kapitel als "passt nicht wirklich". Lieber keine
       Belegstelle als die zum Nachbarthema – eine falsche Quelle ist
       schlimmer als gar keine. */
    schwelle: Number(env("IG_WISSEN_SCHWELLE", "8")),
    /* Und der Vorsprung vor dem zweitbesten Kapitel: Liegen zwei fast
       gleichauf, passt keines von beiden allein. */
    vorsprung: Number(env("IG_WISSEN_VORSPRUNG", "1.2")),
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
    /* Deutsch geht vor Natuerlichkeit: Eine englische Stimme liest „§ 294 BGB"
       als „Paragraf 294 bie-dschie-bie" und betont deutsche Woerter falsch.
       Steht keine deutschsprachige Stimme zur Verfuegung - im kostenlosen
       ElevenLabs-Abo ist das der Regelfall -, spricht die deutsche
       Offline-Stimme Piper. IG_STIMME_NUR_DEUTSCH=false hebt die Regel auf. */
    nurDeutscheStimme: env("IG_STIMME_NUR_DEUTSCH", "true") === "true",
    /* Zwei Reel-Layouts im Wechsel: „klassisch" ist die bisherige Karte mit
       Animation und Untertiteln, „erklaer" die Buehne mit grosser Figur und
       Stichwort-Plaketten (erklaervideo.mjs). „wechsel" laesst sie sich
       taeglich abloesen, damit die Zahlen sagen koennen, welches traegt. */
    layout: env("IG_REEL_LAYOUT", "wechsel"),
    erklaerMarken: Number(env("IG_REEL_MARKEN", "2")),        // Plaketten je Szene
    erklaerBilder: Number(env("IG_REEL_BILDER", "4")),        // hoechstens so viele Motive je Reel neu zeichnen
    stimmeLernen: env("IG_STIMME_LERNEN", "true") === "true",
    stimmeAnzahl: Number(env("IG_STIMME_ANZAHL", "3")),          // so viele Kandidaten laufen gegeneinander
    stimmeErkundung: Number(env("IG_STIMME_ERKUNDUNG", "0.4")),  // 0 = nur ausnutzen, größer = mehr ausprobieren
    stimmeMessungen: Number(env("IG_STIMME_MESSUNGEN", "6")),    // so viele gemessene Reels je Stimme, bevor entschieden wird
    stimmeVorsprung: Number(env("IG_STIMME_VORSPRUNG", "0.25")), // so viel muss die Beste vor der Zweiten liegen
    stimmeProbeText: env("IG_STIMME_PROBE", "Achtzig Prozent scheitern an dieser Frage. Nach Paragraf 123 Absatz 5 Verwaltungsgerichtsordnung ist die einstweilige Anordnung gesperrt, wenn Paragraf 80 Absatz 5 greift – nicht umgekehrt. Merk dir das für die Zulässigkeit."),
    fps: 30,
    /* Obergrenze, damit ein entgleistes Skript nicht ein Zehn-Minuten-Video
       baut - nicht die Ziellänge. Die steht in dauerFenster. */
    maxSekunden: 150,
    /* Ziellängen, unter denen die Lernschleife wählt. Ein Reel muss nicht kurz
       sein: Wenn ein Prüfschema 80 Sekunden braucht, bekommt es sie. Welches
       Fenster tatsächlich am besten läuft, misst insights.mjs an den
       veröffentlichten Reels; bis genug Messwerte da sind, rotieren sie. */
    dauerFenster: [[30, 45], [45, 60], [60, 80], [80, 105]],
    /* So viele gemessene Reels braucht ein Fenster, bevor es gegen die anderen
       antritt - darunter wird weiter reihum ausprobiert. */
    dauerMessungen: Number(env("IG_REEL_DAUER_MESSUNGEN", "3")),
    hintergrundmusik: env("IG_REEL_MUSIK", "false") === "true",  // Klangbett aus: der Akkord legte sich stoerend unter die Stimme
    /* Split-Screen: das obere Drittel zeigt eine ruhige Animation, täglich
       rotierend. IG_REEL_ANIMATION=labyrinth|marble|ring legt eine fest. */
    animationen: ["labyrinth", "marble", "ring"],
    animation: env("IG_REEL_ANIMATION", ""),
    /* Hintergrund-Clips (state/hintergrund/*.mp4, 1080×1920, 30 fps, stumm):
       liegt mindestens einer vor, läuft er vollflächig im Hintergrund, der
       Inhalt liegt als Karten darüber; die Clips rotieren täglich.
       IG_REEL_HINTERGRUND=animation erzwingt die Canvas-Animationen. */
    hintergrund: env("IG_REEL_HINTERGRUND", "clip"),
    /* Wochentage, an denen ein Reel erscheint (0 = So). Standard: jeden Tag. */
    tage: (env("IG_REEL_TAGE", "0,1,2,3,4,5,6")).split(",").map(Number),
    /* true: Das Reel kommt zu den Beiträgen dazu – der Tag hat dann drei
       Feed-Veröffentlichungen (zwei Karussells und ein Reel). false: Es
       ersetzt den letzten Beitrag, der Tag hat zwei.

       Hier true: Der Kanal baut Reichweite auf, da hilft Frequenz, und das
       Tagesbudget trägt es – ein Tag mit Karussell, Reel und neun Stories lag
       bei 0,16 $ von 0,27 $, das zweite Karussell kostet rund 0,05 $. */
    zusaetzlich: env("IG_REEL_ZUSAETZLICH", "true") === "true",
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
    /* Motive erzeugen statt suchen. Sobald OPENAI_API_KEY gesetzt ist, wird
       das Motiv zum Thema gezeichnet - freigestellt geliefert, ohne
       Bildnachweis und ohne rembg. Stockfotos passten oft nicht zum Text
       (Atemmasken bei Betrugsstrafbarkeit), und das Freistellen misslang
       regelmässig. IG_BILD_KI=false schaltet zurück auf Pexels. */
    ki: {
      key: env("OPENAI_API_KEY", ""),
      aktiv: env("IG_BILD_KI", "true") === "true" && Boolean(env("OPENAI_API_KEY", "")),
      modell: env("IG_BILD_KI_MODELL", "gpt-image-1-mini"),
      guete: env("IG_BILD_KI_GUETE", "low"),          // low ~0,005 $, medium ~0,04 $ je Bild
      /* Aussehen der Titelbilder: "foto" = fotorealistisch (seit 18.09., auf
         Wunsch des Betreibers - die Cover sollen echt wirken), "flach" =
         Flat-Vector wie bisher. Die Figuren des Erklärvideos bleiben flach;
         das ist dort Teil des Layouts. */
      look: env("IG_BILD_LOOK", "foto"),
      groesse: env("IG_BILD_KI_GROESSE", "1024x1024"),
      /* Preis je Bild für den Tagesdeckel. Die Schnittstelle meldet ihn nicht
         zurück, deshalb wird er hier gesetzt - bewusst über dem Listenpreis. */
      preisUsd: Number(env("IG_BILD_KI_PREIS_USD", "0.01")),
      zeitlimitMs: Number(env("IG_BILD_KI_ZEITLIMIT_MS", "120000")),
      /* Gezeichnete Motive werden aufgehoben und spaeter wiederverwendet -
         aber nur mit deutlichem Abstand. Zweimal dasselbe Bild in einer Woche
         faellt auf, zweimal im Quartal bemerkt niemand. */
      wiederTage: Number(env("IG_MOTIV_WIEDER_TAGE", "90")),
      /* Wie genau die Szene treffen muss, damit ein altes Motiv wieder
         hervorgeholt wird. 0,85 heisst: praktisch dieselbe Szene. */
      aehnlich: Number(env("IG_MOTIV_AEHNLICH", "0.85")),
      /* Der Deckel muss groesser sein als das, was in der Ruhefrist plus einem
         Themenumlauf anfaellt - sonst wirft das Archiv ein Motiv genau dann
         hinaus, wenn es wieder verwendbar waere. Bei zwei bis drei Bildern am
         Tag reichen 1500 fuer rund anderthalb Jahre; als WebP sind das etwa
         45 MB. */
      archivMax: Number(env("IG_MOTIV_ARCHIV_MAX", "1500")),
    },
  },

  /* Interaktion: Kommentare unter den eigenen Beiträgen beantworten -------- */
  /* Postfach: Direktnachrichten beantworten. Braucht am Token die Berechtigung
     instagram_business_manage_messages. Fehlt sie, liefert der Endpunkt nichts
     und der Lauf meldet das - er bricht nicht ab. */
  /* Antworten auf Kommentare und Direktnachrichten: eigener Topf, eigenes
     Modell. Entscheidung vom 15.09.: Die ersten beiden Antworten kamen vom
     günstigen Modell und trugen je ein ungenaues Normzitat - inhaltlich
     vertretbar, im Detail falsch. Bei Rechts- und Steuerfragen muss die
     Antwort beim ersten Mal sitzen; ein Nachbessern gibt es öffentlich nicht.
     Deshalb das starke Modell, und damit es den Beiträgen nichts wegnimmt,
     ein eigener Tagesdeckel, der zum Inhaltsdeckel HINZUKOMMT. Ist er
     erreicht, warten die Antworten bis morgen - die Beiträge nicht. */
  antworten: {
    modell: env("IG_KI_MODELL_ANTWORTEN", "claude-opus-5"),
    aufwand: env("IG_ANTWORT_AUFWAND", "high"),                 // Denktiefe: low | medium | high
    tagesBudgetUsd: Number(env("IG_ANTWORT_BUDGET_USD", "0.25")),
  },

  postfach: {
    aktiv: env("IG_POSTFACH", "true") === "true",
    unterhaltungen: Number(env("IG_POSTFACH_UNTERHALTUNGEN", 25)),
    maxJeLauf: Number(env("IG_POSTFACH_MAX", 10)),
    maxZeichen: Number(env("IG_POSTFACH_ZEICHEN", 500)),
  },

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
