# LexVerse: verschlüsselte Newsletter-Vorschauen

Der Newsletter bleibt in Kit ein Entwurf. Das Dashboard liest ausschließlich verschlüsselte Voransichten aus dem Zweig `instagram-assets/newsletter/`; das Veröffentlichen der Voransicht versendet und veröffentlicht den Kit-Newsletter nicht.

## Neue Ausgabe vorbereiten

1. HTML-Fassung aus dem freigegebenen Kit-Entwurf exportieren. Metadaten lokal als JSON mit `kit_id`, `subject`, `issue_date`, `status: "draft"`, optional `planned_for`, `label` und `updated_at` anlegen.
2. Verschlüsseln:

   ```bash
   node newsletter/encrypt-preview.mjs --encrypt newsletter/preview-public-key.pem /pfad/ausgabe.html /pfad/metadaten.json /pfad/wochenbrief-JJJJ-MM-TT.enc.json
   ```

3. Nur die `.enc.json` in `instagram-assets/newsletter/` ablegen und ihren Dateinamen in `newsletter/index.json` unter `issues` ergänzen. Ausgabe-Datum und Betreff stehen verschlüsselt im Payload. Das Dashboard lädt die nächste Ausgabe beim Aktualisieren automatisch nach.

Die private Datei `LexVerse-Newsletter-Privatschluessel.pem` darf weder in Git noch in ein Ticket, Log oder einen öffentlichen Link gelangen. Das Dashboard liest sie einmal lokal ein und speichert einen nicht exportierbaren WebCrypto-Schlüssel im Browser. Über „Schlüssel auf diesem Gerät entfernen“ wird er gelöscht. Ohne den privaten Schlüssel lassen sich bestehende Vorschauen nicht entschlüsseln.

Verschlüsselung: zufälliger AES-256-GCM-Schlüssel und IV je Ausgabe; der AES-Schlüssel wird mit RSA-OAEP/SHA-256 und dem öffentlichen 3072-Bit-Schlüssel umhüllt. Der private Schlüssel wird nie auf den Server übertragen. Änderungen in Kit erfordern einen erneuten Export und eine erneute Verschlüsselung; das Dashboard stellt den Stand der abgelegten Voransicht dar.

Für künftige Ausgaben gelten die in [WOCHENBRIEF-REDAKTION.md](WOCHENBRIEF-REDAKTION.md) festgehaltenen Aufbau- und Prüfregeln. Der lokale Renderer erstellt nur den Entwurf; Kit-Export und erneute Verschlüsselung bleiben manuelle Schritte.
