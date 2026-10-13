# Kit-Wochenbriefe ohne wöchentlichen Versandklick

Der GitHub-Workflow `kit-wochenbrief.yml` prüft sonntags morgens den in
`kit-versandplan.json` freigegebenen Kit-Entwurf und terminiert ihn für 09:00
Uhr **Europe/Berlin**. Kit verschickt ihn selbst. Die Liste enthält derzeit
Wochenbrief 04–56 (11. Oktober 2026 bis 10. Oktober 2027). Danach geschieht
nichts, bis weitere geprüfte Ausgaben mit ID, Datum und Betreff eingetragen
sind. Die Redaktion und Rechtsstandsprüfung bleiben eigene Arbeitsschritte;
insbesondere bei Ausgaben weit in der Zukunft müssen Normen und Entscheidungen
kurz vor dem Versand erneut auf Änderungen geprüft werden.

## Einmalige Aktivierung

1. In Kit unter **Settings → Email** die vollständige gewünschte
   LexVerse-Absenderadresse hinzufügen und bestätigen. Derzeit ist
   `herrjurist@gmx.de` der einzige bestätigte Absender. Die Sendezeitzone
   möglichst ebenfalls auf Europe/Berlin setzen, damit die Anzeige in Kit
   stimmt; der Workflow nutzt ausdrücklich UTC-Zeitpunkte mit Berliner
   Sommerzeitumstellung.
2. In GitHub unter **Settings → Secrets and variables → Actions** den geheimen
   Kit-V4-Schlüssel als Secret `KIT_API_KEY` und die exakte bestätigte Adresse
   als Variable `KIT_FROM_ADDRESS` eintragen. Der Workflow prüft die
   Bestätigung über das Kit-Konto und setzt diese Adresse bei der Terminierung;
   die Entwürfe müssen dafür nicht einzeln umgestellt werden.
   Den Schlüssel nie in ein Issue,
   einen Chat, eine Datei oder die Variable kopieren.
3. Den Pull Request mergen. Danach einmal **Run workflow** mit `dry_run=true`
   und `as_of=2026-10-11T05:20:00Z` ausführen. So wird Wochenbrief 04 schon
   vor seinem Sendetag aus Kit gelesen und geprüft, ohne ihn zu terminieren.
   Geplante Workflows laufen nur vom Standardzweig.

Jeder Lauf prüft Ausgabe, Datum, Betreff, Entwurfsstatus, bestätigten Absender,
`all_subscribers`, Mailinhalt und HTML-Größe. Bei Abweichungen scheitert
der Lauf sichtbar, statt eine andere oder unfertige Mail zu versenden.
Ein bereits terminierter oder versendeter Brief wird nicht doppelt versendet.
Der Versand ist an 09:00 Berliner Zeit gebunden; die UTC-Termine im Plan
berücksichtigen die Zeitumstellung. Bei einer anderen Uhrzeit müssen Plan und
Prüfung vor dem Merge gemeinsam angepasst werden.

Die bearbeitbaren Entwürfe 04–56 folgen gestalterisch Wochenbrief 02 als Master. Der Bereich Klausurtechnik & Kopfsache hat daher wie in 02 einen blauen Kopf; Gelb kennzeichnet Prüfungsrelevanz und den Kurzcheck. Die zweistufige Skizze A./I./II./B./I./II. und die getrennten Examensbadges wurden in allen Entwürfen geprüft. Wo ein Fachbeitrag keinen Sachverhalt enthält, steht eine quellengestützte Prüffrage statt eines erfundenen Minifalls. Ausgabe 03 ist bereits versendet und in Kit nicht rückwirkend editierbar. Die HTML-Bodys liegen bei 86–99 KB; der Workflow akzeptiert höchstens 100 KB, damit eine weiter angewachsene oder unvollständige Mail auffällt. Die tatsächliche Darstellung und mögliche Kürzung hängen zusätzlich vom empfangenden Mailprogramm und Kit-Template ab.

Die Entwürfe 14–56 wurden aus den 18 Einzelbeiträgen der jeweils
vorangehenden Montag-bis-Samstag-Woche erzeugt. Der Klartext des
verschlüsselten Themenpools wurde anschließend über einen einmaligen,
verschlüsselten GitHub-Actions-Abgleich lokal eingesehen. 570 benutzte IDs
standen im Pool, acht Kopfsache-IDs in der separaten statischen Definition.
Bei 38 Beiträgen in 23 Ausgaben stimmen Poolnormen und Beitragsquellen nicht
direkt überein. Diese Ausgaben tragen im Versandplan `review_required: true`;
der Workflow terminiert sie auch mit API-Schlüssel erst nach Klärung und
Entfernung dieser Markierung. Die verlinkten amtlichen Normseiten wurden auf
Erreichbarkeit geprüft. Das ersetzt keine erneute fachliche
Rechtsstandsprüfung zu den jeweiligen Sendeterminen.

Kit dokumentiert, dass die Empfängerliste beim Terminieren fixiert werden
kann. Deshalb terminiert der Workflow erst am Sonntagmorgen. GitHub-Cron
kann verzögert laufen; erreicht der Lauf Kit weniger als 20 Minuten vor
dem Termin, bricht er ab. GitHub-Actions-Fehlbenachrichtigungen sollten für
dieses Repository aktiviert sein.

Die Kit-V4-API setzt `send_at` und – gemäß ihrer Update-Dokumentation –
`public=true`. Damit wird die Webausgabe nach dem Mailversand ebenfalls
veröffentlicht. Es findet kein Versand direkt aus GitHub statt.
