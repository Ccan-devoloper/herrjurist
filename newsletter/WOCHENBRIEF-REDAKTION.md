# LexVerse: Redaktion und Bauplan für künftige Wochenbriefe

**Wochenbrief 02 ist der verbindliche Gestaltungs-Master.** Diese Vorlage erzeugt lokales E-Mail-HTML aus einer lokalen JSON-Datei und prüft formale Anforderungen. Die Kit-Ausgabe bleibt ein Entwurf; weder der Befehl noch das Dashboard versendet oder veröffentlicht etwas. Die bestehenden Anmelde- und Bestätigungsmails sind ein anderes Modul.

## Reihenfolge und feste Gestaltung

1. **Betreff, Preheader und starker Hook:** Eine konkrete Irritation, Klausurfrage oder überraschende Folge aus dieser Woche. Präzise und wahr; keine austauschbare Überschrift und keine Zusage, die der Inhalt nicht einlöst. Der Betreff und Preheader ergänzen einander. Der Hook steht als große Titelzeile.
2. **LexVerse-Header:** Logo, direkt darunter linksbündig ausschließlich die gelbe Pille `by herrjurist`, Inter-Schrift, dunkles Navy und Akzente in Gelb, Blau, Orange und Grün. Danach die wiederverwendbare intergalaktische Szene mit Mara, Rex, FORM-7, Flux, Zylla und Brakk. HTML für E-Mail-Clients mit Tabellen und Inline-Stilen, maximal 690 px Webbreite und mobil 100 %.
3. **Kurze Leseanweisung.** Der Wochenrückblick und seine Einzelbeiträge werden im Newsletter weder verlinkt noch mit Vorproduktions-IDs bezeichnet.
4. **Rechtsgebiete als farbige Abschnitte:** Blau für Zivilrecht, Orange für Strafrecht, Grün für Öffentliches Recht. Jede fachliche Karte hat getrennte Examensbadges, Themen-Hook, Einstieg, die gelbe Box „WARUM PRÜFUNGSRELEVANT?“, einen quellengestützten Minifall oder eine konkrete fachliche Prüffrage, die eingerückte Lösung A./I./II./B./I./II., einen Fehlerhinweis oder Merksatz und Links zu überprüfbaren Rechtsgrundlagen.
5. **Klausurtechnik & Kopfsache:** blauer Bereichskopf wie in Ausgabe 02, praktische Karte „DIREKT ANWENDEN“ mit zwei bis vier konkreten Schritten. Für diese Themen gibt es keine Fall-Leiste und keine juristische Lösungsskizze.
6. **Drei Wiederholungsfragen** und kurzer Abschluss. Die Themenzahl folgt den jeweiligen Beiträgen der Woche; sie wird nicht auf die neun Themen der Master-Ausgabe gekürzt.

## Didaktischer Maßstab pro Thema

- **Einstieg:** Worum geht es, und welche Vorfrage entscheidet den Fall? Ein bis drei Sätze.
- **Prüfungsrelevanz:** Lehrbuchartig in einem knappen Absatz: Regel und Anspruchsgrundlage bzw. Prüfungsmaßstab, Voraussetzungen, Gegenansicht/Abgrenzung oder Rechtsfolge soweit relevant, typische Klausurposition und Aussage des Wochenbeitrags. Die verschlüsselten HerrJurist-Themenpools dienen für die fachliche Vertiefung; sie werden nicht im Klartext ins öffentliche Repo kopiert. Jeder Inhalt wird an aktueller Norm und gegebenenfalls einschlägiger Rechtsprechung überprüft.
- **Minifall oder Prüffrage:** Ein Minifall braucht einen konkreten Sachverhalt mit entscheidenden Tatsachen und lösbarer Frage. Fehlen Tatsachen in der geprüften Quelle, steht eine fachliche Prüffrage statt eines erfundenen Falls. Nur Themen aus Zivilrecht, Strafrecht und Öffentlichem Recht erhalten diesen Baustein.
- **Lösungsskizze:** Juristische Prüfungsreihenfolge: Frage/Anspruch, Zulässigkeit oder Eröffnung, Voraussetzungen, Subsumtion und Ergebnis in den Master-Ebenen `A./I./II./B./I./II.`. Die zweite Ebene ist sichtbar eingerückt. Ein bloßes Ergebnis ohne Subsumtion gilt redaktionell nicht als fertige Skizze.
- **Examensbadge:** Kennzeichnung je Fall, ob erstes, zweites oder beide Staatsexamina; fachlich anhand der Tätigkeit und des Prüfungsstoffs gegenlesen.
- **Rechtsgrundlagen:** Mindestens eine zitierfähige Norm oder Entscheidung pro Thema verlinken. Der Wochenrückblick und die Einzelbeiträge dienen beim Schreiben zur Themenauswahl und zum fachlichen Abgleich; ihre IDs und URLs erscheinen nicht im Newsletter.

Formale Prüfungen erkennen fehlende Bausteine, falsche Anzahl/Nummerierung, unpaarige oder übersprungene Gliederungspunkte, fehlende Quellenreferenzen, fehlende Examensbadges und grob zu kurze/zu lange Inhalte. **Juristische Richtigkeit, Qualität eines Hooks, aktuelle Rechtslage, Subsumtion und tatsächliche Verknüpfung zum Beitrag müssen vor jeder Verwendung redaktionell geprüft werden.**

## Lokales JSON-Format und Prüfung

Die JSON-Quelldatei enthält unveröffentlichte Inhalte und bleibt **außerhalb des öffentlichen Repos** (oder unter `newsletter/entwuerfe/`, das durch `.gitignore` gesperrt ist). Sie hat diese Struktur; die eckigen Werte sind redaktionell auszufüllen:

```json
{
  "version": 1,
  "status": "draft",
  "issue": {
    "number": 2,
    "date": "2026-09-27",
    "subject": "[konkreter E-Mail-Betreff]",
    "preheader": "[ergänzender Vorschautext]",
    "hook": "[starker Einstieg auf der Titelseite]",
    "deck": "[ein Satz zum Nutzen dieser Woche]",
    "topic_count": 2,
    "quick_check": ["[konkrete Frage 1]", "[konkrete Frage 2]", "[konkrete Frage 3]"]
  },
  "sections": [{
    "area": "zivilrecht",
    "title": "Zivilrecht",
    "subtitle": "[roter Faden der Fälle]",
    "cases": [{
      "id": "01",
      "field": "[Rechtsgebiet/Normenkomplex]",
      "headline": "[konkrete Klausurspannung]",
      "exams": [1, 2],
      "intro": "[Thema und Kernproblem in wenigen Sätzen]",
      "relevance": "[lehrbuchartige Einordnung mit Norm, Abgrenzung und Prüfungsort]",
      "fact": "[lösbarer Minifall und konkrete Frage]",
      "solution": [
        { "marker": "A.", "text": "[erster Prüfungsschritt]" },
        { "marker": "I.", "text": "[erste Voraussetzung und Subsumtion]" },
        { "marker": "II.", "text": "[zweite Voraussetzung und Subsumtion]" },
        { "marker": "B.", "text": "[zweiter Prüfungsschritt]" },
        { "marker": "I.", "text": "[Anwendung im Sachverhalt]" },
        { "marker": "II.", "text": "[Ergebnis und Rechtsfolge]" }
      ],
      "trap": "[typische Fehlleistung und richtige Abgrenzung]",
      "sources": [{ "label": "[Norm oder Entscheidung]", "url": "https://www.gesetze-im-internet.de/..." }]
    }]
  }],
  "method_subtitle": "Konkrete Übungen für die nächste Klausur",
  "methods": [{
    "id": "02",
    "field": "KOPFSACHE",
    "headline": "[praktischer Nutzen in einer konkreten Situation]",
    "exams": [1, 2],
    "intro": "[Problem und Nutzen der Übung in zwei Sätzen]",
    "steps": ["[erster ausführbarer Schritt]", "[zweiter ausführbarer Schritt]"],
    "note": "[ein konkreter Merksatz für die Anwendung]"
  }]
}
```

Vorlage lokal anwenden (ohne Kit- oder GitHub-Zugang):

```bash
node bin/wochenbrief-entwurf.mjs /pfad/entwurf.json
node bin/wochenbrief-entwurf.mjs /pfad/entwurf.json /pfad/wochenbrief.html
```

Die zweite Form schreibt nur eine HTML-Datei. **Betreff und Preheader** stehen im JSON für die spätere manuelle Übernahme nach Kit; das HTML ist nur der Mailkörper. Erst nach inhaltlicher Sichtung den HTML-Körper manuell in einen **Kit-Entwurf** übernehmen. Für die Dashboard-Vorschau wie in `PREVIEW-VERSCHLUESSELUNG.md` beschrieben mit dem öffentlichen Schlüssel verschlüsseln und ausschließlich die `.enc.json` im Asset-Zweig ablegen. Kein automatischer Kit-Abgleich, keine Sendefunktion, keine automatische Veröffentlichung.

Die Zuordnung zu den Vorproduktionsbeiträgen bleibt eine interne Redaktionsaufgabe. Die JSON-Quelldatei für die E-Mail benötigt dazu keine Pool-IDs und keine Instagram-URLs; der Renderer gibt solche Angaben auch dann nicht aus, wenn sie in älteren Entwurfsdateien noch vorhanden sind. Der Mailkörper darf 100 KB nicht überschreiten; je nach Mailprogramm und Kit-Template kann selbst darunter eine Darstellungskontrolle sinnvoll sein.
