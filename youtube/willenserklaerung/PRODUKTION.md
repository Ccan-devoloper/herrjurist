# Herr Jurist · YouTube-Pilot „Willenserklärung“

## Dramaturgie

16:9, etwa 5:08 Minuten. Ein einziger Fahrradfall trägt den Film. Die ersten Sekunden zeigen Maras direktes Angebot an Rex und seine Annahme; Maras nur innerlich gefasstes Nein eröffnet die Rechtsfrage. Die Erzählung geht über den objektiven Erklärungswert und die innere Seite zu Angebot/Annahme, Abgabe/Zugang und § 116 BGB. Die Folge nach § 433 BGB und vier kurze Prüfungsfragen schließen den Film. Die letzten 7,8 Sekunden sind für YouTube-Endelemente frei.

Die Leitlinien unter `instagram-assets/vorproduktion/REEL-LEITLINIEN.md` und die freigegebene V7-Referenz wurden vor der Produktion gelesen. Übernommen sind der sofortige Fallkonflikt, dieselbe Figurengestalt über alle Einstellungen, die Zivilrechtsfarbe `#2d5be3`, der harte Schnitt zwischen registrierten Posen, kurze Figurenrede mit eigenem Handlungsbeitrag, die festgelegte Erzählerstimme, Untertitel in Sinngruppen und die Ton-Zeitmarken als Schnittgrundlage. Die 9:16-Safe-Area wurde für 16:9 neu gestaltet. Es gibt keine Musik und keinen digitalen Zoom auf Standbilder.

Die fünf Szenenbilder wurden mit Maras und Rex' Golden References aus `main/assets/charaktere/*.jpg.b64` und passenden zusätzlichen Reel-Referenzen erstellt. Es sind Varianten derselben blauen Bühne und desselben Fahrrads. PNG-Masters liegen lokal bei der Produktion; die kompakten JPGs unter `assets/` reichen für einen erneuten Render. Die juristischen Tafeln sind redaktionelle Grafiken außerhalb der gezeichneten Requisiten. Untertitel sind eine separate ASS-Spur und als SRT beigelegt.

## Ton und technische Daten

- Erzähler: freigegebene Stimme Moritz, Voice-ID `PhufIH7nYh2Up1uej6aY`, `eleven_multilingual_v2`, Einstellungen aus der V7-Produktionsreferenz (Stabilität 0,42; Ähnlichkeit 0,82; Stil 0,38; Speaker Boost; Tempo 1,08). Die neun MP3s und Zeichen-Alignments stammen aus GitHub-Actions-Lauf 36358083600. Der gewählte Take bleibt fixiert.
- Mara: zwei kurze deutschsprachige Charakter-Takes; Rex: ein kurzer eigener Take. Keine Figur wiederholt den Erzählertext.
- 44 Bildzustände; harte Schnitte und stabile Hintergründe. 185 Untertitel-Cues aus den tatsächlichen Erzähler-Alignments; juristische Normen erscheinen im Subtitle als Kurznotation.
- Ausgabe: H.264, 1920 × 1080, 30 fps, yuv420p; AAC mono 48 kHz, 192 kbit/s; MP4 mit Faststart. Sprachende etwa 4:59, Gesamtdauer etwa 5:07,6.
- Render: `python youtube/willenserklaerung/render.py` und danach `ffmpeg` mit der lokalen `work/slides.txt`, `work/master.wav` und `work/captions.ass`. Die Ton-Masters gehören nach `audio/` und die drei Figuren-Takes nach `character-audio/`.

## Rechtsprüfung

Der Themenpool `daten/themen.json.enc` wurde nicht als Autorität vorausgesetzt. Die für seine AES-Entschlüsselung nötige Umgebungsvariable `IG_WISSEN_KEY` stand in dieser Arbeitsumgebung nicht zur Verfügung. Das Skript wurde anhand des geltenden Gesetzestextes und einer universitären Prüfungserklärung neu aufgebaut.

| Aussage im Film | Beleg und Präzisierung |
| --- | --- |
| Willenserklärung: objektive Äußerung und innere Seite; Handlungswille, Erklärungsbewusstsein, Geschäftswille | Universität Potsdam, Rechtskunde Online, [Willenserklärung](https://www.uni-potsdam.de/de/rechtskunde-online/rechtsgebiete/zivilrecht/vertrag/willenserklaerung); fehlendes Erklärungsbewusstsein ist dogmatisch differenziert und wird im Film nicht als pauschale Nichtigkeitsregel behandelt. |
| Auslegung über Wortlaut und Umstände | [§ 133 BGB](https://www.gesetze-im-internet.de/bgb/__133.html), [§ 157 BGB](https://www.gesetze-im-internet.de/bgb/__157.html); der Film schildert den objektiven Empfängerhorizont, ohne den inneren Willen zu ignorieren. |
| Angebot, sofortige Annahme unter Anwesenden, geänderte Annahme als neuer Antrag | [§ 145 BGB](https://www.gesetze-im-internet.de/bgb/__145.html), [§ 147 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__147.html), [§ 150 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__150.html), Universität Potsdam, [Vertragsschluss](https://www.uni-potsdam.de/de/rechtskunde-online/rechtsgebiete/zivilrecht/vertrag/vertragsschluss). Das Rad wird persönlich Rex angeboten; die bloße Auslage ist nur ein abgegrenzter Vergleich. |
| Zugang einer empfangsbedürftigen Erklärung unter Abwesenden | [§ 130 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__130.html); die Briefkasten-Erklärung ist ein klar als Nebenbeispiel markierter Vergleich zum unmittelbaren Gespräch. |
| Geheimer Vorbehalt; Kenntnis des Erklärungsempfängers | [§ 116 Sätze 1 und 2 BGB](https://www.gesetze-im-internet.de/bgb/__116.html). Im Fall hat Rex keine Kenntnis; ein offen erkennbarer Scherz wird nicht mit dem geheimen Vorbehalt verwechselt. |
| Vertragliche Hauptpflichten, kein automatischer Eigentumsübergang allein durch Kaufvertrag | [§ 433 Abs. 1 und 2 BGB](https://www.gesetze-im-internet.de/bgb/__433.html), zum getrennten dinglichen Erwerb [§ 929 Satz 1 BGB](https://www.gesetze-im-internet.de/bgb/__929.html). |

## Aufbau des Lernvideos

YouTube wertet die Bindung der Zuschauer in den ersten 30 Sekunden gesondert aus und empfiehlt, dass Einstieg, Titel und Vorschaubild dieselbe Erwartung erfüllen: [Audience retention](https://support.google.com/youtube/answer/9314415). Der Film beginnt daher mit der Fallfrage und löst sie am Schluss am selben Fahrrad auf. Die empirische MOOC-Studie von Guo/Kim/Rubin empfiehlt für Lehrvideos kurze, gut geplante Einheiten unter sechs Minuten: [Originalarbeit, MIT](https://up.csail.mit.edu/other-pubs/las2014-pguo-engagement.pdf). Die neun Themenabschnitte sind kapitelbar; YouTube verlangt Zeitstempel ab 00:00 und mindestens drei Kapitel: [Video chapters](https://support.google.com/youtube/answer/9884579). Das freie Schlussbild erlaubt [End Screens](https://support.google.com/youtube/answer/6388789) in den letzten 5–20 Sekunden.

## Prüfung vor Veröffentlichung

Nach dem Export sind durchgehende Figurengestalt, Objektzustand, Bild-/Ton-Kausalität, Übergänge, Kapitelgrenzen und die normierten Untertitel im Film zu prüfen. Technisch wurden Format, Laufzeit, Tonspur, Spitzenpegel und Standbildproben kontrolliert. Der finale Höreindruck der gesprochenen Normen und die Wiedergabe auf einem echten Mobilgerät bleiben eine menschliche Freigabehandlung.
