# Produktionsreferenz: freigegebenes Reel 30.09.2026, § 136a StPO

Diese Datei dokumentiert die vom Betreiber am 27.09.2026 ausdrücklich als gewünschtes Ergebnis bestätigte Prüffassung V7. Sie ergänzt REEL-LEITLINIEN.md um überprüfbare Zahlen und die tatsächlich verwendete Herstellungsweise. Zeiten, Bildzahl und Mischwerte beschreiben **diese** Folge; für einen neuen Fall wird die Dramaturgie neu geschrieben und anhand des neuen Sprecher-Takes getaktet.

Quelle: Ccan-devoloper/herrjurist, Branch codex/reel-test-20260930-v7-ruhiger-schnitt, Commit 6c56e3fa2919fde6ff90437390a65636375a5e37. Im [Quellverzeichnis](https://github.com/Ccan-devoloper/herrjurist/tree/6c56e3fa2919fde6ff90437390a65636375a5e37/reel-2026-09-30-v7) liegen render.mjs, make_frames.py, PRODUKTION.md, das zusätzliche Nachschlagbild sowie die fixierten ElevenLabs-MP3s und Alignment-JSONs. Erfolgreicher GitHub-Actions-Lauf 36344722242. Maßgeblich für den fertigen Schnitt ist die [dauerhaft gespeicherte MP4](referenzen/2026-09-30-v7.mp4), nicht ein Entwurf oder ein neu synthetisierter Take; SHA-256 der MP4: 7f4b84ed52b28a1cccef65bc86c9a0bef44a9c0759bb04b2fff8a0754c3d1a72. [Timing-JSON](referenzen/2026-09-30-v7-timing.json) und [Caption-Datei](referenzen/2026-09-30-v7-captions.ass) stammen aus demselben GitHub-Render.

## 1. Redaktion und Sprechertext

**Hook:** Sie unterschreibt die Verwertung; trotzdem ist das Geständnis unverwertbar. Die rote Ablehnung weckt die Frage „Warum?“. **Rückblende:** Brakk hält Zylla die Nacht über wach, sie nickt weg, er startet die Aufnahme und schlägt auf den Tisch. Brakk fordert sie auf, wach zu bleiben; Zylla gibt erschöpft eine Aussage ab. **Rückkehr zur Einwilligung und Auflösung:** § 136a verbietet die Beeinträchtigung des Willens durch Ermüdung; nach Absatz 3 macht die Zustimmung zur Verwertung die Aussage nicht verwertbar.

Exakter Erzählertext des freigegebenen Takes (sieben Sätze/Abschnitte, insgesamt 49 Wörter):

> Sie unterschreibt. Trotzdem ist ihr Geständnis unverwertbar. Warum?
>
> Zurück. Brakk hält Zylla die ganze Nacht wach.
>
> Sie nickt immer wieder weg.
>
> Er startet die Aufnahme.
>
> Später willigt sie in die Verwertung ein.
>
> Paragraf einhundertsechsunddreißig A verbietet Ermüdung als Vernehmungsmethode.
>
> Absatz drei: Auch ihre Einwilligung macht das Geständnis nicht verwertbar.

Brakk sagt „Nicht einschlafen! Rede endlich!“. Zylla antwortet „Ich war’s.“ Der Erzähler beschreibt in dieser Lücke nicht zusätzlich den Schlag oder das Geständnis. Der Rechtssatz kommt erst nach der gespielten Handlung. Das Skript ist knapp, weil die Figuren einen Teil der Information tragen; künftige Texte sollen nicht pauschal auf 49 Wörter gekürzt werden.

## 2. Bilder: Zahl, Dauer und Einsatz

11 registrierte vertikale Bild-Masters im Verhältnis 9:16, darunter eine neu generierte Nachschlagpose, ergeben 13 aufeinanderfolgende Bildzustände. Zwei Grundbilder werden später erzählerisch wiederaufgenommen. Die 30 fps entstehen durch bewusst gehaltene und gezielt gewechselte Cels; es werden **nicht** 2–4 verschiedene Illustrationen pro Sekunde verlangt. Die 941 × 1672 großen Bildquellen werden beim Export auf 1080 × 1920 skaliert. Alle Szenentexte stehen bereits im gemalten Papier oder Hologramm. Captions sind die getrennte Untertitelspur.

| Zeit im Export (ca.) | Bildzustand / Master | Funktion und Ton |
| --- | --- | --- |
| 0,00–0,95 s | 01-consent | Unterschriebene Einwilligung als vorweggenommenes Ergebnis; 0,20 s Vorlauf vor dem Erzähler. |
| 0,95–4,48 s | 01-consent mit lokal maskiertem 01-reject | Rotes Ablehnungssignal im Recorder und Scanner-SFX; Papier und Figuren bleiben stabil. „Trotzdem unverwertbar. Warum?“ |
| 4,48–7,83 s | 02-interrogation | Erkennbarer Schnitt zurück zur Nacht, kurzer Rückspul-SFX und zurückhaltender Raumton; Brakk und Zylla bleiben groß im Bild. |
| 7,83–11,15 s | 02-later-tired | Fortgeschrittene Uhrzeit, Zylla nickt weg. Aufnahme-Klick bei 9,76 s zu „Er startet ...“; noch keine Wellenform auf dem Recorder. |
| 11,15–13,73 s | 03-slam | Faustkontakt im ersten Frame mit kräftigem metallischem Treffer-SFX. Brakk beginnt nach 0,12 s zu sprechen. Die Pose hält 2,58 s; kein Kamera-Zoom oder Zittern. |
| 13,73–14,48 s | 03-aftershock | Generierte, zur ersten Pose passende Nachwirkung: Faust bleibt auf dem Tisch, Funken klingen ab, Brakks Kiefer schließt sich, Zylla zuckt zusammen. Der Schlagbeat umfasst damit insgesamt 3,33 s. |
| 14,48–16,33 s | 04-statement | Zylla sagt erschöpft „Ich war’s.“; erst jetzt ist die Aufnahmewellenform sichtbar. |
| 16,33–19,11 s | 01-consent erneut | Jetzt ist die unterschriebene Verwertung chronologisch erklärt, ohne ein neues, abweichendes Dokument zu erfinden. |
| 19,11–21,86 s | 05-law1 | Bereits mitgenerierte, perspektivisch passende Projektion „§ 136a StPO / ERMÜDUNG“. 2,75 s Lesedauer statt langer Tafelpräsentation. |
| 21,86–24,57 s | 04-statement erneut | Ruhiger Rückschnitt auf Zyllas Müdigkeit während „verbietet Ermüdung als Vernehmungsmethode“. Das Normbild steht nicht bis zum nächsten Absatz unbewegt. |
| 24,57–26,54 s | 06-law2 | Mitgenerierte zweite Projektion „§ 136a Abs. 3 StPO / EINWILLIGUNG“. |
| 26,54–27,91 s | 07-shield | Aufnahme prallt am Schutzschild ab, passender kurzer SFX; die Figuren reagieren. |
| 27,91–29,70 s | 07-shield mit lokal maskiertem 08-cross | Rotes X nur auf demselben unterschriebenen Papier; kräftiger kurzer Papier-/Ablehnungs-SFX, dann Ruhe für die Pointe. |

Die Zeiten kommen aus reel-2026-09-30-v7/out/timing.json des Renderlaufs. Der geplante Inhalt dauert 29,701 s; die fertige MP4 umfasst nach Rundung auf volle 30-fps-Frames 29,733 s. Reine Bildzählung ist kein Qualitätsmaß: Entscheidend sind unterscheidbare Handlung, ausreichende Haltezeit und ein logischer Zustandswechsel.

**Bildtechnik:** V7 verwendet harte Schnitte zwischen stabilen Einstellungen und zwei örtlich begrenzte Bildänderungen: Ablehnungssignal am Recorder, X auf dem Papier. Keine digitalen Ausschnitt-Zooms, kein zoompan/Ken Burns, keine Ganzbildüberblendung zwischen verschieden gezeichneten Gesichtern. Die Nachschlagpose wurde aus dem Kontaktbild mit den Golden References für Brakk und Zylla erzeugt, gleicher Kamerastandpunkt, gleiche Kleidung und Raumgeometrie. Die maßgeblichen Golden References liegen im Branch main unter assets/charaktere/ als Base64-codierte JPG-Dateien; die sechs dort geprüften Dateien stimmen nach Decodierung mit den für diese Produktion lokal verwendeten Referenzen überein. Die [zusätzlichen Reel-Bildreferenzen](../assets/referenzen/reels/README.md) ergänzen künftig den Blick auf Posen, Kostüm, Mimik und Handlungsrequisiten; bei Widerspruch zur Figurengestalt gilt immer die jeweilige Golden Reference. Sie wurden nach Freigabe dieser V7-Fassung bereitgestellt und sind keine rückwirkende Produktionsquelle für sie. Das Bild des Geständnisses darf später als Reaktion erneut erscheinen, wenn sein Zustand und die Wellenform dort sinnvoll sind. Für andere Reels Bildzahl und Pausen nach dem konkreten Geschehen neu planen.

## 3. Stimme, Dialog, Pausen und Mischung

| Rolle | Tatsächlich verwendete Stimme und Modell | Regie und technische Referenz |
| --- | --- | --- |
| Erzähler Moritz | Voice-ID PhufIH7nYh2Up1uej6aY, eleven_multilingual_v2, Deutsch | Stabilität 0,42; Ähnlichkeit 0,82; Stil 0,38; Speaker Boost an; Geschwindigkeit 1,08. Ruhige, klare Rechtsfolge statt durchgängiger Action-Kommentar. |
| Brakk | Voice-ID JiW03c2Gt43XNUQAumRP, eleven_v3, Deutsch | Stabilität 0,32; Ähnlichkeit 0,78; Stil 0,85; Speaker Boost an; Geschwindigkeit 1,08. Ärger und Befehl passend zur sichtbaren Faustpose. |
| Zylla | Voice-ID xLCJR8xcZX2YjImGFyGw, eleven_v3, Deutsch | Stabilität 0,38; Ähnlichkeit 0,78; Stil 0,72; Speaker Boost an; Geschwindigkeit 1,00. TTS-Regie „[exhausted, whispering]“ vor „Ich war’s.“; schwach und erschöpft, aber im Mix verständlich. |

Die Erzählerstimme wurde **nicht ausgetauscht**. Neu ist ihre Funktion im gespielten Reel: Sie eröffnet das Rätsel, gibt den knappen Kontext und erklärt anschließend den konkreten Rechtspunkt. Die Figuren tragen die emotionale und kausale Mitte. Diese Rollenverteilung ist der übertragbare Teil; die Voice-IDs von Brakk und Zylla gelten nur bei Auftritten dieser Figuren.

- Erzähler beginnt bei 0,20 s. Nach „Er startet die Aufnahme.“ wurde anhand der ElevenLabs-Zeichenzeiten eine 5,36-s-Lücke in seine Tonspur eingefügt. Das ist Platz für Schlag, beide Figuren und Atempausen, keine allgemeine Pflichtpause von 5,36 s.
- Aufnahme-Klick: 9,76 s. Tischkontakt/SFX: 11,15 s. Brakk-Spur beginnt bei 11,27 s; seine Wort-Caption reicht ungefähr bis 13,75 s. Nach seinem Satz bleibt rund 0,73 s bis zu Zyllas **hörbaren Worten**. Ihre TTS-Datei beginnt bei 14,20 s mit rund 0,28 s natürlichem Anlauf; „Ich war’s.“ ist von etwa 14,48 bis 15,88 s sichtbar und captioniert. Der Erzähler setzt bei ungefähr 16,33 s wieder ein: rund 0,45 s nach Zyllas Worten.
- Gesprochene Worte, Stille, Bildpose und SFX werden nach **tatsächlichen Audio-Alignments** geschnitten; nicht Sprache nach einem unabhängig festgezurrten Bildraster verschieben. Bevor das Geständnis im Bild erscheint, darf die Recorder-Wellenform nicht laufen.
- Acht getrennte ElevenLabs-SFX (Scanner, Rückspulen, Raum, Aufnahme, Tisch, Hologramm, Schutzschild, Papier) wurden handlungsbezogen mit eleven_text_to_sound_v2 erzeugt. Im freigegebenen Mix hat der Tisch-SFX den relativen Faktor 0,62; Zyllas leise TTS-Spur wurde um den Faktor 2,7 angehoben. Der Erzähler läuft mit Loudness-Normalisierung auf Ziel -16 LUFS, der Summenmix über einen Limiter. Diese Faktoren sind **keine Universalwerte**: jede neue Datei nach Gehör und Pegel neu prüfen. Kein sanftes Klirren auf einen schweren Schlag legen.
- Die in diesem Reel freigegebenen MP3-Dateien und zugehörigen Alignment-JSONs sind im Testbranch fixiert. Eine identische Texteingabe lieferte in einem neuen ElevenLabs-Take einmal 30,90 statt 29,73 s; deshalb vor Freigabe einen Take wählen und bei reinen Bildkorrekturen die geprüften Tondateien wiederverwenden.

## 4. Captions und Export

Die V7-Captions folgen den Zeichenzeiten der gewählten ElevenLabs-Takes, werden aber **vor** dem Render redigiert: meist zwei bis fünf sinntragende Wörter zusammen, einzelne rhetorische Wörter („Warum?“, „Zurück.“) oder Normen („§ 136a“, „Abs. 3:“) dürfen allein stehen. Erzähler **und tatsächlich gesprochener Figurendialog** werden untertitelt; Schreie, Seufzer und SFX nicht. Kein automatisches Transkript ungeprüft einblenden. Weiße, fette Nimbus Sans mit dunkler Kontur, bei 1080 × 1920 mittig unten (ASS Alignment 2, MarginV 280; Referenzgrößen 72/64/55 px je nach Länge), nur dezentes Ein-/Ausblenden von 70 ms. Keine wandernde Position und kein Wort-für-Wort-Skalieren. Gesprochenes „Paragraf einhundertsechsunddreißig A“ erscheint als „§ 136a“; Text im Hologramm bleibt als Teil der generierten Szene.

Technik des freigegebenen Exports: H.264, yuv420p, 1080 × 1920, 30 fps, AAC 192 kbit/s, MP4 mit faststart. Die Zeitachse kommt aus den Audio-Alignments, die Bildzustände aus make_frames.py und die finalen Ton-/Caption-Filter aus render.mjs. Alle tatsächlich verwendeten 11 Masters samt Varianten, die acht SFX, Sprecher-MP3s, Alignment-JSONs und der Rendercode müssen für eine nachvollziehbare Fassung auffindbar bleiben.

## 5. Ablauf für das nächste Reel

1. Rechtsaussage verifizieren und einen Fall mit sichtbarer Ursache, Gegenkraft und Folge auswählen. Ein Satz benennt den Mehrwert und einer die Pointe; „Merke“ nur, falls er hilft.
2. Szenenplan als Tabelle schreiben: Ereignis und Objektzustand, Bild-Master, gesprochene Worte, gewünschte Pause, SFX und Caption. Bildtexte als physische Teile der Illustration briefen; Fachfarbe, Landschaft und Golden References je Figur festlegen.
3. Bild-Masters zunächst als geordnete Geschichte und Kontaktbogen prüfen; Figuren in jeder Szene **untereinander und gegen ihre Golden References** vergleichen. Aktionsvarianten aus demselben Standpunkt mit derselben Geometrie erzeugen. Keine zusätzliche Bildmenge erzwingen.
4. Erzähler und nur geeignete Figurenrede mit konsistenten Stimmen generieren; Charaktere sprechen nicht bloß zur Dekoration. Die Tondateien tatsächlich beurteilen, vor allem Stimme, Normaussprache, Pausen und natürliches Spiel. Gewählten Take und Alignment fixieren.
5. Schnitt aus dem Ton heraus setzen: Hook innerhalb der ersten drei Sekunden, längere Wirkungseinstellung am Wendepunkt, juristische Auflösung nicht als stehende Folie. Geräusche exakt zum sichtbaren Ereignis legen; Verhältnis von Erzähler, Figur und SFX in der fertigen Mischung prüfen.
6. Sinngruppen-Captions unten anlegen, juristische Schriftform und Satzgrenzen prüfen. Ganzen Export mit Ton in Handygröße ansehen, an Zustandswechseln und Figurengesichtern frameweise prüfen, ffprobe für Format und Dauer, danach erst freigeben.

Das Muster ist so genau dokumentiert, dass sein Aufbau rekonstruierbar ist; es **garantiert** keine passende neue Folge durch bloßes Kopieren von Bildzahl, Voice-Parametern oder Sekunden. Inhalt, Schauplatz, Figuren und Gewichtung müssen bei jedem neuen Rechtspunkt neu entschieden und vom Betreiber an einer Prüffassung beurteilt werden. Der juristische Kern wurde gegen den [amtlichen § 136a StPO](https://www.gesetze-im-internet.de/stpo/__136a.html) geprüft: Abs. 1 nennt Ermüdung als Mittel der Willensbeeinträchtigung, Abs. 3 schließt die Verwertung trotz Zustimmung aus.
