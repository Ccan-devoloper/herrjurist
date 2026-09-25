# Newsletter-Landingpage einrichten (Versuchsaufbau)

Ziel: Ein Beitrag sagt „Trag dich ein, dann bekommst du die Übersicht“ – die
Seite nimmt die Adresse entgegen, bestätigt sie per Mail und zeigt die
Übersicht sofort an. Damit lässt sich messen, ob überhaupt jemand den Weg
von Instagram auf eine eigene Seite geht. Erst wenn das trägt, lohnt sich
mehr.

## Was passiert, Schritt für Schritt

1. Jemand tippt seine Adresse auf der Startseite ein.
   **Gespeichert wird noch nichts.** Die Adresse steht nur signiert im
   Bestätigungslink (HMAC-SHA256) – ohne Datenbank, ohne Speicherplatz.
2. Der Worker stößt den Actions-Lauf an, der die Bestätigungsmail verschickt.
3. Klick auf den Link → **jetzt** wird die Adresse in die verschlüsselte
   Liste im Asset-Zweig aufgenommen, und die Übersicht erscheint sofort im
   Browser. Dieselben Links kommen noch einmal per Mail, damit sie später
   wiederzufinden sind.
4. Abmelden geht über einen Klick in jeder Mail.

Das ist **Double-Opt-In**. Es ist nicht Umstand um des Umstands willen: Ohne
Bestätigung ließe sich jede fremde Adresse eintragen, die Liste füllte sich
mit Tippfehlern, und Werbemails an nicht bestätigte Adressen sind in
Deutschland angreifbar (§ 7 UWG; Einwilligung nach Art. 6 Abs. 1 lit. a
DSGVO). Die Bestätigung kostet einen Klick und erledigt beides.

## Was es kostet

Nichts. Cloudflare Workers Free deckt 100.000 Anfragen am Tag ab, GitHub
Actions ist für öffentliche Repositories kostenlos, und der Mailversand läuft
über den SMTP-Zugang, der für den Wochenbericht ohnehin eingerichtet ist. Es
kommt kein Dienst dazu, der eine Rechnung schreiben oder ausfallen kann. Der
Tagesdeckel des Bots wird nicht berührt – hier ruft nichts die Claude-API auf.

## Warum ein eigener Worker

Der Webhook-Worker trägt inzwischen den Story-Bezug für die Antworten des
Bots. Ein Versuchsaufbau darf ihn nicht mit in den Ausfall ziehen können.
Zwei Worker kosten dasselbe wie einer und haben getrennte Fehlerräume.

## Einrichten

### 1. Ein Geheimnis erzeugen

Lokal im Terminal:

```
node -e "console.log(require('crypto').randomBytes(32).toString('base64url'))"
```

Dieses Geheimnis wird an **zwei** Stellen eingetragen und muss dort identisch
sein: bei Cloudflare und bei GitHub. Es gehört **nirgendwo sonst hin** – nicht
ins Repository, nicht in eine Datei, nicht in einen Chat. Mit ihm ließen sich
gültige Bestätigungslinks fälschen und die Liste entschlüsseln.

### 2. GitHub: Secret und Variable

Repository → Settings → Secrets and variables → Actions:

- **Secrets** → New: `NEWSLETTER_SECRET` = das Geheimnis aus Schritt 1
- **Variables** → New: `NEWSLETTER_URL` = die Adresse des Workers aus
  Schritt 3 (nachtragen, sobald sie feststeht), z. B.
  `https://herrjurist-newsletter.<dein-name>.workers.dev`

`SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `SMTP_FROM` sind vom
Wochenbericht her schon gesetzt und werden mitbenutzt.

### 3. Worker bereitstellen

Im Ordner `newsletter/`:

```
npx wrangler deploy
npx wrangler secret put NEWSLETTER_SECRET   # dasselbe Geheimnis wie oben
npx wrangler secret put GITHUB_TOKEN        # Fine-grained PAT, Contents: Read and write
```

Wrangler nennt danach die Adresse des Workers. Die gehört in Schritt 2 als
`NEWSLETTER_URL` zu GitHub – sonst zeigen alle Links ins Leere und der Lauf
bricht mit genau dieser Meldung ab.

Der GitHub-Token darf derselbe sein wie beim Webhook-Worker, solange er auf
dieses Repository zeigt.

### 4. Pflichtangaben eintragen

Cloudflare-Dashboard → Worker → Settings → Variables, drei Klartextvariablen:

- `ANBIETER` – Name
- `ANSCHRIFT` – ladungsfähige Anschrift
- `KONTAKT` – E-Mail-Adresse

Sie stehen bewusst **nicht** im Repository: Eine private Anschrift gehört
nicht in ein öffentliches Repository. Solange sie fehlen, zeigt die
Impressumsseite einen gelb hinterlegten Hinweis – sichtbar, statt still
gegen § 5 DDG zu verstoßen. **Vor dem ersten Link aus einem Beitrag
ausfüllen.**

### 5. Ausprobieren

Adresse des Workers aufrufen, die eigene E-Mail eintragen, Mail abwarten,
Link klicken. Danach:

```
NEWSLETTER_SECRET=... node bin/newsletter.mjs --ereignis zeigen \
  --datei <Asset-Zweig>/state/newsletter.enc
```

Kommt keine Mail an, steht der Grund im Actions-Lauf „Newsletter“. Die
Adressen stehen dort nur maskiert (`t***@beispiel.de`) – die Läufe eines
öffentlichen Repositories kann jeder lesen.

## Ohne Bereitstellung ansehen

```
node bin/newsletter-vorschau.mjs --bilder
```

legt alle Seiten als HTML und PNG unter `out/newsletter/` ab und erzeugt das
PDF so, wie es beim Leser über „Drucken → Als PDF sichern“ entsteht. Keine
Mail, kein Cloudflare, kein GitHub – der Weg nach GitHub wird abgefangen.

## Missbrauch

Am Ende des Formulars steht eine Mail an eine fremde Adresse. Ohne Bremse
ließe sich damit jemand zumüllen. Drei zustandslose Hürden sind eingebaut:
ein signiertes Formularticket (wer absendet, muss die Seite geholt haben),
eine Mindestverweildauer von zwei Sekunden und ein unsichtbares Feld, das nur
Skripte ausfüllen. Das hält Gelegenheitsunsinn ab.

Gegen einen entschlossenen Angreifer hilft das nicht. Wenn die Adresse
öffentlich beworben wird, zusätzlich im Cloudflare-Dashboard unter
**Security → WAF → Rate limiting rules** eine Regel anlegen: Pfad
`/anmelden`, Methode POST, höchstens 5 Anfragen pro Minute je IP. Das ist im
Free-Tarif enthalten.

## Was hier bewusst fehlt

- **Kein Tracking.** Keine Analyse, keine Pixel, keine Cookies. Wie viele sich
  eintragen, sagt `state/newsletter-zahlen.json` – nur Zahlen, keine Adressen.
- **Kein gesetztes PDF.** Die Übersicht ist eine druckbare Seite. Ein
  gestaltetes PDF lohnt erst, wenn sich zeigt, dass überhaupt jemand kommt.
- **Kein Versandwerkzeug.** Eine Ausgabe an die Liste zu schicken, gibt es
  noch nicht. Erst kommt die Frage, ob sich jemand einträgt.
- **Kein Aufruf in den Beiträgen.** Der Bot verweist noch nirgends auf die
  Seite. Das ist eine Entscheidung für danach, nicht für den Aufbau.

## LexVerse-Wochenbrief als Entwurf

Der Wochenrückblick-Brief mit Minifällen ist ein eigenständiges redaktionelles Format. Aufbau, formale Prüfregeln, lokaler HTML-Renderer und Schritte zur verschlüsselten Vorschau stehen in [WOCHENBRIEF-REDAKTION.md](WOCHENBRIEF-REDAKTION.md). Das hier beschriebene Anmeldeexperiment verschickt keine solchen Wochenbriefe.
