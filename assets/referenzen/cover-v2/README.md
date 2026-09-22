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

## Layout-Abnahme

Die Referenzen priorisieren eine dichte mobile Komposition. Der Renderer hält nur die wiederkehrende Marken-Geometrie fest: 4:5-Format, ein bündiges und unverrückbares Fachband mit einheitlicher CSS-Geometrie, obere Titelposition, feste Schriftstufen der Titelpillen, minimal enger Pillenabstand, Pillen-Innenabstände/-maximalbreite, Badge-Geometrie, Footer und Seitenzähler. Der Titel darf nicht wegen der Charakterbühne dynamisch kleingerechnet werden. Mehrwort-Zeilen werden vor dem Rendern auf höchstens ungefähr 21 sichtbare Zeichen neu verteilt; verbleibender Pillen-Overflow ist ein harter Preflight-Fehler statt eines stillen Schrumpfens.

Die konkrete Szene bleibt Aufgabe der dynamischen Regie. Dazu gehören Figuren, Requisiten, Posen sowie die gewünschte Beziehung zwischen handschriftlichem Aha-Hinweis und Szene. Das Bildmodell selbst erzeugt **keine** Handschrift und **keinen** Pfeil.

Nach der Bildgenerierung sieht die bereits vorhandene visuelle KI-QA das tatsächliche freigestellte Motiv und liefert einen normalisierten `annotationPlan`: Mittelpunkt des Hinweises, konkretes Pfeilziel, leichte Rotation und Pfeilkrümmung. Damit bestimmt weiterhin die KI die reale Komposition – aber anhand des wirklich entstandenen Bildes statt anhand starrer Zonen. Der Renderer zeichnet anschließend den redaktionell vorgegebenen `coverText` exakt in Caveat sowie den Markenpfeil entlang dieses KI-Plans. Der Pfeil verwendet die Referenzoptik: lockere Kurve, runder dunkler Strich und offene zweistrichige Pfeilspitze statt gefülltem Dreieck. Er darf nur technisch innerhalb der Safe Area korrigieren; eine eigene links/rechts-Zonensuche oder ein Kompositions-Scoring findet nicht statt.
