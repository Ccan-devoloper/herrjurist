# Cover v2 – Golden References

Diese Dateien definieren die **visuelle Sprache und das Qualitätsniveau** der Herr-Jurist-Cover. Sie sind **keine Storyboards** und dürfen nicht als feste Zuordnung von Rechtsgebiet, Charakteren, Requisiten oder Choreografie interpretiert werden.

## Konstant halten

- Feed-Cover im 4:5-Format.
- Dunkles Fachband oben links.
- Sehr dominante weiße Headline in 2–4 dunklen, einzeln gerundeten Titelblöcken.
- Kleine helle redaktionelle Badge direkt unter dem Titel.
- Kurzer handschriftlicher juristischer Aha-Hinweis mit klarer Pfeilbeziehung zur Szene. Seine konkrete Position, Neigung und Pfeilführung entstehen aus der jeweiligen Bildregie und sind nicht auf eine feste Seite beschränkt.
- Große, hochwertige 2D-Charakterbühne im unteren Bereich; Figuren und Hauptrequisiten sind auf Mobilgröße sofort erkennbar.
- Kleine Fach-/Bereichspille unten rechts.
- Bei Karussells: dunkler runder Seitenzähler oben rechts, z. B. „1/6“.
- Kräftige fachabhängige Vollflächenfarben und klare Silhouetten.

## Ausdrücklich variieren

- Auswahl der 1–2 Charaktere.
- Links-/Rechts-Positionen und Posen.
- Requisiten, Metaphern und konkrete Handlung.
- Anzahl und Art der Objekte, soweit der juristische Sinn nicht davon abhängt.
- Literalität vs. visuelle Metapher.
- Komposition innerhalb der vorgesehenen Markenbühne.

Insbesondere darf aus diesen Referenzen **keine Regel wie „ZPO = FORM-7 + Flux“** oder „Versuch = Rex + Mara“ abgeleitet werden. Die konkrete Szene entsteht aus dem jeweiligen Thema durch die dynamische `coverRegie`.

## Dateien

`reference-images.zip` enthält zehn bewusst verkleinerte Repo-Kopien der freigegebenen Referenzcover. Die hochgeladenen Ausgangsbilder lagen bei 1122×1402 px; das Archiv enthält bewusst kompakte Vorschaubilder als visuelle Anker für Layout, QA und Creative Direction. Es ist nicht für OCR oder Pixel-Matching gedacht und hält das Repository klein.

Die zehn Motive sind:
1. Strafrecht AT – Versuch / unmittelbares Ansetzen
2. Klausur- und Lernmethodik – Anspruchsgrundlage zuerst
3. Sachenrecht – Besitz vs. Eigentum
4. Öffentliches Recht AT – § 80 Abs. 5 VwGO
5. BGB AT – Anfechtung / Irrtum und Kausalität
6. Zivilrecht AT – Schaufenster / invitatio ad offerendum
7. Strafrecht BT – § 142 StGB / Nachholpflicht
8. ZPO – Zulässigkeit vor Begründetheit
9. Arbeitsrecht – Kündigungszugang / Fristbeginn
10. Klausur- und Lernmethodik – Ergebnisse vergleichen

## Verwendung

Für visuelle QA und Renderer-Entwicklung dienen die Referenzen als **Qualitätsmaßstab**, nicht als Pixel- oder Szenen-Matching. Neue Cover sollen sich wie dieselbe Marke anfühlen, aber als neue Episode des Universums erkennbar bleiben.

## AI-first-Abnahme

Die Golden References definieren die visuelle Gesamtwirkung. Neue Feed-Cover werden deshalb als **vollständige Bildkomposition** erzeugt: Vollflächenfarbe, Fachband, Titelpillen, Badge, Handschrift/Pfeil, Charakterbühne, Fachpille und ggf. Seitenzähler entstehen gemeinsam im Bildmodell.

Vor der Generierung werden die Solltexte redaktionell festgelegt und die Titelzeilen semantisch normalisiert. Das Bildmodell erhält ausgewählte Golden References nur als Marken-/Layoutanker und die gewählten Charakterreferenzen nur als Identitätsanker. Es darf daraus keine feste Fach→Figur-, Prop- oder Szenenformel ableiten.

Die finale Vision-QA prüft insbesondere:
- exakte Schreibweise aller vorgesehenen sichtbaren Texte,
- keine zusätzliche lesbare Schrift,
- Golden-Reference-Markenwirkung und visuelle Dichte,
- große, klare Szene ohne tote Fläche,
- Charakteridentität/Anatomie,
- sauberes Fachband, Titelpillen, Badge, Handschrift und Pfeil.

Bei Fehlern gibt es höchstens einen gezielten Retry. Besteht auch dieser nicht, darf das Cover nicht ungeprüft veröffentlicht werden.

Der Renderer baut ein bestandenes AI-first-Cover **nicht** nochmals aus CSS-Elementen zusammen. Er behandelt es als fertiges 1080×1350-Vollbild und übernimmt nur technische Ausgabe/Export. Die bisherige Renderer-Komposition bleibt ausschließlich als Fallback für Altinhalte bzw. nicht-AI-first-Cover erhalten.
