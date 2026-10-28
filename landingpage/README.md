# Wochenbrief-Landingpage (LexVerse by herrjurist) – ersetzt die Kit-Seite

Aufbau wie Examenscampus (Repo `steuerberater`): statische Seite auf **Cloudflare Pages**, Formular → `functions/api/anmelden.js`
→ Anmeldung zuerst im KV-Speicher, dann per Brevo-API in die Liste. Fällt Brevo aus, holt
`.github/workflows/anmeldungen-nachtragen.yml` die offenen Einträge stündlich nach. Kein Double-Opt-in (Entscheidung Kanalinhaber).
Figuren: Lexi aus `op/ressourcen/peeps-bibliothek/lexi.py` (Open Peeps, CC0).

## Einrichten (gleiches Cloudflare-Konto wie Examenscampus)
1. Workers & Pages → KV → Namespace `herrjurist-anmeldungen` anlegen.
2. Workers & Pages → Pages → Projekt aus diesem Repo: Build-Befehl leer, Ausgabeordner `landingpage`.
3. Projekt → Settings (Production): KV-Binding `ANMELDUNGEN` → `herrjurist-anmeldungen`;
   Secret `BREVO_API_KEY`; Variable `BREVO_LISTE` (Listen-ID); optional `BREVO_VORLAGE_WILLKOMMEN` (Vorlagen-ID der Begrüßungsmail).
4. GitHub → Settings → Variables → `LANDINGPAGE_URL` = Adresse der Seite (z. B. `https://herrjurist.pages.dev`), sonst läuft das Nachtragen nicht.
