# Prüfreel 01.10.2026 – § 90 Abs. 2 BVerfGG und Subsidiarität

Status: Prüffassung für die Betreiberentscheidung. Den bestehenden
01.10.-Slot vor Freigabe nicht überschreiben. Der 30.09.-Slot verwendet
bereits die freigegebene V7-Fassung.

Die verbindliche Gesamtregel steht in
vorproduktion/REEL-LEITLINIEN.md im Branch instagram-assets. Die
30.09.-V7-Referenz dokumentiert Schnitt, Ton und Captions als technisches
Vorbild, ohne dessen Handlung zu kopieren.

## Redaktion

Mara hat den fachgerichtlichen Rechtsweg ausgeschöpft und hält das letzte
Urteil. Der Zugang nach Karlsruhe bleibt dennoch verschlossen. Rückblick:
Sie hatte eine zumutbare Gelegenheit, die behauptete Grundrechtsverletzung
vor dem Fachgericht geltend zu machen, nutzte diese aber nicht. Form-7 zeigt
ihre damals leere Grundrechtsseite. Die erste Tür steht für
Rechtswegerschöpfung nach § 90 Abs. 2 Satz 1 BVerfGG, die zweite für den
weitergehenden Grundsatz der Subsidiarität. Pointe: Ein ausgeschöpfter
Rechtsweg öffnet nicht automatisch beide Türen.

Das ist ein konkreter Beispielsfall, keine Behauptung, jede
Grundrechtsrüge verlange immer dieselbe Form. Entscheidend sind zumutbare
fachgerichtliche Möglichkeiten im Einzelfall. Gesetzeswortlaut:
https://www.gesetze-im-internet.de/bverfgg/__90.html.
Zum weitergehenden Subsidiaritätsgrundsatz siehe BVerfG, Beschluss vom
10.04.2025 – 2 BvR 487/25 und Beschluss vom 25.09.2012 – 2 BvR 2819/11.
Subsidiarität darf nicht als wörtlicher Inhalt des § 90 Abs. 2 Satz 1
dargestellt werden.

Exakter Erzählertext:

> Alle Instanzen durch. Karlsruhe bleibt trotzdem zu. Warum?
>
> Zurück. Mara hätte den Grundrechtsverstoß schon beim Fachgericht rügen
> können. Sie schwieg.
>
> Paragraf neunzig Absatz zwei Satz eins verlangt Rechtswegerschöpfung.
> Subsidiarität verlangt darüber hinaus, zumutbare Möglichkeiten vor den
> Fachgerichten zu nutzen.
>
> Ein ausgeschöpfter Rechtsweg öffnet nicht beide Türen. In der Klausur:
> beide Hürden getrennt prüfen.

Mara sagt am wieder erreichten Tor: „Aber ich war doch überall!“ Der
Erzähler überlässt ihr die Irritation, statt sie zu wiederholen. Die
juristische Erklärung folgt erst nach dem Rückblick und dem leeren Blatt.

## Bild und Rhythmus

Neun registrierte vertikale Cels aus acht eigentlichen Bildmotiven:

| Datei | Erzählfunktion |
| --- | --- |
| 00-gate-ajar.png | Eine lokale Türvariante der Auftakteinstellung. |
| 01-gate-closed.png | Tor schlägt im Hook zu, Urteil in Maras Arm. |
| 02-fachgericht.png | Frühere Gelegenheit, Grundrecht geltend zu machen. |
| 03-silence.png | Das Dossier wird zugeschlagen, Mara schweigt. |
| 04-mara-protests.png | Zurück am Tor: Maras kurze Replik. |
| 05-empty-rights.png | Form-7 zeigt die leere Seite des alten Dossiers. |
| 06-law.png | § 90 Abs. 2 S. 1 BVerfGG räumlich an der Wand. |
| 07-two-hurdles.png | Erster Durchgang offen, zweiter gesperrt; Figuren groß. |
| 08-pointe.png | Mara tippt auf die leere Seite und begreift die Hürde. |

Alle Motive wurden mit den Golden References Mara Sternpfad und Form-7
aus Branch main erstellt; die zusätzlichen Reel-PNGs unterstützten Mimik
und Gruppenaktion. Die Umgebung bleibt ein zusammenhängender mintgrüner
Gerichtsraum. Bildtext ist Teil der Illustration; keine nachträglich
aufgeklebte Normtafel. Vor- und Nach-Türbild werden nur im Türbereich
lokal getauscht. Sonst harte motivierte Schnitte und angemessene
Haltezeiten, kein Zoom oder Ken Burns. Kontaktbogen und fertige MP4
werden auf Figurenidentität vom Anfang bis zum Schluss geprüft.

## Ton und Export

render.mjs generiert den Erzähler mit der freigegebenen Moritz-Stimme
PhufIH7nYh2Up1uej6aY, eleven_multilingual_v2, speed 1,08. Mara
verwendet die für sie bereits etablierte deutsche Selena-Stimme
2aL479c8D3QMIPExj0tw, eleven_v3. MP3 und Zeichenalignment werden
neben der MP4 fixiert. Der Erzähler-Take erhält nach „Sie schwieg.“
eine ausgemessene Lücke für Maras Satz und die sichtbare Reaktion.

Handlungsbezogene ElevenLabs-SFX: kräftige Tür, kurze Rückblende, leiser
Saalton, Dossier, Papieraufdeckung, Projektion, verriegeltes zweites Tor.
Jeder Kontakt wird erst mit dem entsprechenden Bildzustand hörbar.
Sinngruppen-Captions für Erzähler und Mara: Nimbus Sans fett, weiß,
dunkle Kontur, immer mittig unten; „Paragraf neunzig Absatz zwei Satz
eins“ erscheint als „§ 90 Abs. 2 S. 1“. Kein Caption-Text für SFX.
Ausgabe 1080 × 1920, 30 fps, H.264/AAC, möglichst um 30 Sekunden.

QA vor Freigabe: fertig gerenderte MP4 mit Ton ansehen; Hook innerhalb
der ersten drei Sekunden; Mara-Satz auf offenem Mund, Norm nach dem
verpassten Vortrag, zwei räumlich plausible Tore, korrekte Schreibweise
aller ins Bild gezeichneten Wörter, Sprecher- und SFX-Timing, lesbare
untere Captions, keine Figuren- oder Ausrüstungsdrift, Ende als
begründete Pointe. Ein neuer TTS-Durchlauf erfordert neues Alignment
und erneute Prüfung.
