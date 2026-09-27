# Kit-Wochenbriefe ohne wöchentlichen Versandklick

Der GitHub-Workflow `kit-wochenbrief.yml` prüft sonntags morgens den in
`kit-versandplan.json` freigegebenen Kit-Entwurf und terminiert ihn für 09:00
Uhr **Europe/Berlin**. Kit verschickt ihn selbst. Die Liste enthält derzeit
Wochenbrief 04–13 (11. Oktober bis 13. Dezember 2026). Danach geschieht
nichts, bis weitere geprüfte Ausgaben mit ID, Datum und Betreff eingetragen
sind. Die Redaktion und Rechtsstandsprüfung bleiben eigene Arbeitsschritte.

## Einmalige Aktivierung

1. In Kit unter **Settings → Email** die vollständige gewünschte
   LexVerse-Absenderadresse hinzufügen und bestätigen. Derzeit ist
   `herrjurist@gmx.de` der einzige bestätigte Absender. Die Sendezeitzone
   möglichst ebenfalls auf Europe/Berlin setzen, damit die Anzeige in Kit
   stimmt; der Workflow nutzt ausdrücklich UTC-Zeitpunkte mit Berliner
   Sommerzeitumstellung.
2. In GitHub unter **Settings → Secrets and variables → Actions** den geheimen
   Kit-V4-Schlüssel als Secret `KIT_API_KEY` und die exakte bestätigte Adresse
   als Variable `KIT_FROM_ADDRESS` eintragen. Den Schlüssel nie in ein Issue,
   einen Chat, eine Datei oder die Variable kopieren.
3. Den Pull Request mergen. Danach einmal **Run workflow** mit `dry_run=true`
   und `as_of=2026-10-11T05:20:00Z` ausführen. So wird Wochenbrief 04 schon
   vor seinem Sendetag aus Kit gelesen und geprüft, ohne ihn zu terminieren.
   Geplante Workflows laufen nur vom Standardzweig.

Jeder Lauf prüft Ausgabe, Datum, Betreff, Entwurfsstatus, Absender,
`all_subscribers`, Mailinhalt und HTML-Größe. Bei Abweichungen scheitert
der Lauf sichtbar, statt eine andere oder unfertige Mail zu versenden.
Ein bereits terminierter oder versendeter Brief wird nicht doppelt versendet.
Der Versand ist an 09:00 Berliner Zeit gebunden; die UTC-Termine im Plan
berücksichtigen die Zeitumstellung. Bei einer anderen Uhrzeit müssen Plan und
Prüfung vor dem Merge gemeinsam angepasst werden.

Kit dokumentiert, dass die Empfängerliste beim Terminieren fixiert werden
kann. Deshalb terminiert der Workflow erst am Sonntagmorgen. GitHub-Cron
kann verzögert laufen; erreicht der Lauf Kit weniger als 20 Minuten vor
dem Termin, bricht er ab. GitHub-Actions-Fehlbenachrichtigungen sollten für
dieses Repository aktiviert sein.

Die Kit-V4-API setzt `send_at` und – gemäß ihrer Update-Dokumentation –
`public=true`. Damit wird die Webausgabe nach dem Mailversand ebenfalls
veröffentlicht. Es findet kein Versand direkt aus GitHub statt.
