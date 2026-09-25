# LexVerse: Redaktion und Bauplan für künftige Wochenbriefe

Diese Vorlage ist das **redaktionelle Muster** für eine Ausgabe zum veröffentlichten Instagram-Wochenrückblick. Sie erzeugt nur lokales E-Mail-HTML aus einer lokalen JSON-Datei und prüft formale Anforderungen. Die Kit-Ausgabe bleibt ein Entwurf; weder der Befehl noch das Dashboard versendet oder veröffentlicht etwas. Die bestehenden Anmelde- und Bestätigungsmails sind ein anderes Modul.

## Reihenfolge und feste Gestaltung

1. **Betreff, Preheader und starker Hook:** Eine konkrete Irritation, Klausurfrage oder überraschende Folge aus dieser Woche. Präzise und wahr; keine austauschbare Überschrift und keine Zusage, die der Inhalt nicht einlöst. Der Betreff und Preheader ergänzen einander. Der Hook steht als große Titelzeile.
2. **LexVerse-Header:** Logo, direkt darunter linksbündig ausschließlich die gelbe Pille `by herrjurist`, Inter-Schrift, dunkles Navy und Akzente in Gelb, Blau, Orange und Grün. Danach die wiederverwendbare intergalaktische Szene mit Mara, Rex, FORM-7, Flux, Zylla und Brakk. HTML für E-Mail-Clients mit Tabellen und Inline-Stilen, maximal 600 px breit.
3. **Kurze Leseanweisung** und Link zum Instagram-Wochenrückblick.
4. **Rechtsgebiete als farbige Abschnitte:** je Thema in derselben nachvollziehbaren Reihenfolge wie im Wochenrückblick eine Karte mit Kennzeichnung `1. Staatsexamen` und/oder `2. Staatsexamen`, prägnantem Themen-Hook, kurzem Einstieg, gelb hervorgehobener Einordnung der Prüfungsrelevanz, neuem Minifall, eingerückter Lösungsskizze, typischer Fehlerquelle sowie Links zum jeweiligen Beitrag und zu überprüfbaren Rechtsquellen.
5. **Drei Wiederholungsfragen** und kurzer Abschluss. Die Zahl der Fälle entspricht den Themen des Wochenrückblicks; acht ist nur die Zahl des ersten Beispiels.

## Didaktischer Maßstab pro Thema

- **Einstieg:** Worum geht es, und welche Vorfrage entscheidet den Fall? Ein bis drei Sätze.
- **Prüfungsrelevanz:** Lehrbuchartig in einem knappen Absatz: Regel und Anspruchsgrundlage bzw. Prüfungsmaßstab, Voraussetzungen, Gegenansicht/Abgrenzung oder Rechtsfolge soweit relevant, typische Klausurposition und Aussage des Wochenbeitrags. Die verschlüsselten HerrJurist-Themenpools dienen für die fachliche Vertiefung; sie werden nicht im Klartext ins öffentliche Repo kopiert. Jeder Inhalt wird an aktueller Norm und gegebenenfalls einschlägiger Rechtsprechung überprüft.
- **Minifall:** Neuer Sachverhalt mit konkreter Prüfungsfrage und entscheidenden Tatsachen; keine bloße Wiederholung des Beitrags. Der Fall muss mit den danach genannten Tatsachen lösbar sein.
- **Lösungsskizze:** Juristische Prüfungsreihenfolge: Frage/Anspruch, Zulässigkeit oder Eröffnung, Voraussetzungen, Subsumtion und Ergebnis in der passenden Ebene. Keine zusätzliche Gliederungsebene allein wegen der Optik. Geschwisterpunkte immer mindestens paarweise: kein `A.` ohne `B.`, kein `I.` ohne `II.`, kein `1.` ohne `2.`; das gilt ebenso für `a)`/`b)` und `aa)`/`bb)`. Ebenen werden um je 22 px eingerückt. Ein bloßes Ergebnis ohne Subsumtion gilt redaktionell nicht als fertige Skizze.
- **Examensbadge:** Kennzeichnung je Fall, ob erstes, zweites oder beide Staatsexamina; fachlich anhand der Tätigkeit und des Prüfungsstoffs gegenlesen.
- **Quellen:** Beim unveröffentlichten Beitrag den eindeutigen Vorproduktions-Slug, nach Veröffentlichung den echten Instagram-Link hinterlegen; dazu mindestens eine zitierfähige Norm oder Entscheidung. Die Quelle muss die konkrete Aussage tatsächlich tragen. Niemals einen Instagram-Link erfinden.

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
    "weekly_post_url": "https://www.instagram.com/p/BEITRAG/",
    "topic_count": 1,
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
        { "marker": "B.", "text": "[zweiter Prüfungsschritt mit Ergebnis]" }
      ],
      "trap": "[typische Fehlleistung und richtige Abgrenzung]",
      "instagram_post_url": "https://www.instagram.com/p/THEMENBEITRAG/",
      "sources": [{ "label": "[Norm oder Entscheidung]", "url": "https://www.gesetze-im-internet.de/..." }]
    }]
  }]
}
```

Vorlage lokal anwenden (ohne Kit- oder GitHub-Zugang):

```bash
node bin/wochenbrief-entwurf.mjs /pfad/entwurf.json
node bin/wochenbrief-entwurf.mjs /pfad/entwurf.json /pfad/wochenbrief.html
```

Die zweite Form schreibt nur eine HTML-Datei. **Betreff und Preheader** stehen im JSON für die spätere manuelle Übernahme nach Kit; das HTML ist nur der Mailkörper. Erst nach inhaltlicher Sichtung den HTML-Körper manuell in einen **Kit-Entwurf** übernehmen. Für die Dashboard-Vorschau wie in `PREVIEW-VERSCHLUESSELUNG.md` beschrieben mit dem öffentlichen Schlüssel verschlüsseln und ausschließlich die `.enc.json` im Asset-Zweig ablegen. Kein automatischer Kit-Abgleich, keine Sendefunktion, keine automatische Veröffentlichung.

**Vorproduktion ohne Instagram-Permalink:** Statt `issue.weekly_post_url` ist `issue.weekly_source_slug` zulässig (z. B. `2026-09-27-b1`); statt `instagram_post_url` pro Fall `instagram_source_slug` (z. B. `2026-09-24-b2`). Die Vorschau zeigt den Slug als interne Quellenreferenz und verlinkt keine erfundene Instagram-Adresse. Vor dem Versand die Slugs mit den tatsächlichen Beiträgen abgleichen und die echten Links ergänzen.
