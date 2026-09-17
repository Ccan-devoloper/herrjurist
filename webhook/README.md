# Webhook-Mitschnitt einrichten

Ziel dieses Schritts: **herausfinden, was Instagram bei einer Story-Antwort
wirklich schickt.** Es wird nichts beantwortet, nichts veröffentlicht, nichts
verändert — nur mitgeschrieben.

Hintergrund: Am 16.09. lieferte die nachträgliche Abfrage über
`/conversations` bei einer echten Story-Antwort ein leeres `reply_to.story`
— weder ID noch URL. Daraus wurde geschlossen, Instagram gebe den Bezug
überhaupt nicht heraus. Das ist ein Schluss von *einem* Abfrageweg auf die
ganze Plattform und nicht belegt. Meta dokumentiert die Story-Referenz im
**eingehenden Ereignis**. Ob sie bei diesem Konto und diesem Zugang ankommt,
beantwortet nur ein Mitschnitt.

## Kosten

Keine. Cloudflare Workers Free deckt 100.000 Anfragen pro Tag ab — für einen
Instagram-Kanal um Größenordnungen zu viel. GitHub Actions ist für
öffentliche Repositories kostenlos. Es wird keine Datenbank gebraucht: Die
Ereignisse landen als JSONL im Asset-Zweig, wo der Bot ohnehin seinen Zustand
führt.

## Schritt für Schritt

### 1. Cloudflare-Konto

Auf `dash.cloudflare.com` registrieren (kostenlos, keine Zahlungsdaten nötig
für den Free-Tarif).

### 2. Worker bereitstellen

Im Ordner `webhook/`:

```
npx wrangler login
npx wrangler deploy
```

Danach nennt Wrangler eine Adresse der Form
`https://instagram-webhook-mitschnitt.<dein-name>.workers.dev`.
**Diese Adresse brauchst du in Schritt 5.**

### 3. GitHub-Token anlegen

GitHub → Settings → Developer settings → **Fine-grained personal access
tokens** → *Generate new token*:

- Repository access: **Only select repositories** → `Ccan-devoloper/herrjurist`
- Permissions → Repository permissions → **Contents: Read and write**
- Laufzeit: 90 Tage reichen für den Versuch

### 4. Secrets in Cloudflare setzen

```
npx wrangler secret put VERIFY_TOKEN
npx wrangler secret put APP_SECRET
npx wrangler secret put GITHUB_TOKEN
```

- `VERIFY_TOKEN` — frei gewählt, irgendeine lange Zeichenfolge. Du brauchst
  sie gleich in Schritt 5 noch einmal.
- `APP_SECRET` — der **Instagram**-App-Geheimcode:
  Meta-Dashboard → Instagram → *API-Einrichtung mit Instagram-Login* → Schritt 1.

  > Nicht der Geheimcode unter *App-Einstellungen → Grundeinstellungen*. Bei
  > einer App mit Instagram-Login signiert Meta mit dem Instagram-eigenen
  > Geheimcode. Der falsche Wert fällt nirgends auf: Die Einrichtungsprüfung
  > ist ein GET und läuft durch, erst die eingehenden Ereignisse scheitern
  > still an der Signatur — 401, kein Eintrag, kein Fehler im Protokoll.
  > Genau daran hing es am 17.09. einen Abend lang.

- `ROUTEN` — optional, `<kontoId>=<owner/repo>,<kontoId>=<owner/repo>`.
  Beide Kanäle hängen an derselben Meta-App, ihre Ereignisse kommen also über
  dieselbe Adresse herein. Ohne Verteilung landeten Campus-Nachrichten im
  Jura-Repository. Die Konto-ID steht im Ereignis unter `entry[].id`.
  Unbekannte Konten fallen auf `GITHUB_REPO` zurück.

  Der `GITHUB_TOKEN` braucht dann Schreibrechte (*Contents*) auf **beide**
  Repositories.
- `GITHUB_TOKEN` — der Token aus Schritt 3.

**Die Werte gehören nur hierhin, nicht in den Chat und nicht ins Repository.**

### 5. Webhook bei Meta eintragen

Meta-Dashboard → deine App → **Webhooks**:

- Callback-URL: die Worker-Adresse aus Schritt 2
- Verify Token: derselbe Wert wie `VERIFY_TOKEN`
- **Verifizieren und speichern** — Meta ruft die Adresse einmal per GET auf;
  der Worker antwortet mit der Challenge.
- Feld **`messages`** abonnieren.

Dann unter **Instagram → Webhooks** prüfen, dass das Abonnement auf
Kontoebene aktiv ist. Ein App-Level-Abonnement allein genügt bei Instagram
Login nicht immer.

### 6. Testen

Auf eine eigene Story antworten — am besten von einem anderen Konto — und
zusätzlich eine ganz normale DM schicken. Beides sollte binnen einer Minute
als Actions-Lauf „Webhook-Mitschnitt" auftauchen.

### 7. Auswerten

```
node bin/webhook-zeigen.mjs
```

(im Asset-Zweig, oder mit `IG_STATE_DIR` auf das `state/`-Verzeichnis
zeigend). Die Ausgabe sagt, ob im eingehenden Ereignis eine Story-ID steht.

## Was danach kommt

Steht die Story-ID im Ereignis, ist die Zuordnung ein reiner
Schlüssel-Vergleich — kein Raten, kein Zeitfenster, keine Rückfrage. Dann
wird der Mitschnitt zum Eingangskanal ausgebaut.

Steht sie nicht darin, ist die Frage endgültig beantwortet, und es bleibt
bei der Rückfrage mit den laufenden Stories zur Auswahl. Auch das ist ein
Ergebnis — nur eben eines, das wir dann belegen können.

## Was dieser Schritt NICHT tut

- Er beantwortet keine Nachricht.
- Er ändert nichts am laufenden Bot.
- Er schreibt nur in `state/webhook-roh.jsonl` im Asset-Zweig.

Abschalten: Webhook bei Meta löschen, Worker mit `npx wrangler delete`
entfernen.
