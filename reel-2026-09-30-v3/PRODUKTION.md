# 30.09.2026 – § 136a StPO, neue Prüffassung

**Status:** Prüffassung auf `codex/reel-test-20260930`; den vorhandenen Reel-Slot in `instagram-assets` erst nach Sichtung/Freigabe ersetzen.

## Warum diese Fassung anders gebaut ist

Die erste Fassung erfüllte 30 fps und etwa 2–4 verschiedene Bilder pro Sekunde, hatte aber 70 unabhängig gezeichnete Posen. Beim Wechsel sprangen Gesicht, Körper und Objekte zugleich. Die Anhänge und die eigene Sichtung benennen zu lange Starre zwischen zu großen Posewechseln sowie eine kaum lesbare Kausalkette.

Diese Fassung verwendet fünf vollflächige Bildkompositionen in 941 × 1672 Pixel und eng kontrollierte Varianten *derselben* Einstellungen: neue Uhrzeiger innerhalb der Uhr, Zylla mit geschlossenen/geöffneten Augen bzw. minimal veränderter Mundform, Brakks erhobene/gesenkte Faust, eine identische Einstellung mit und ohne Rechtsschutzschild. `make_frames.py` blendet nur den betroffenen Bildbereich, hält den Rest der Zeichnung stabil, setzt Aktionen als kurze Sequenzen mit 30 fps um und lässt Dialogaufnahmen länger stehen. Zwei abrupte, begründete Ausschnittwechsel dienen Scanner-Stopp und Tischschlag. Kein Dauerzoom und keine Kontaktbögen im Film.

## Sichtbare Kausalkette

1. Am Vormittag unterschreibt Zylla ein lesbar als **Einwilligung / Aussage verwerten** gekennzeichnetes Blatt; der Scanner projiziert ein in derselben Einstellung erzeugtes rotes Verbotssymbol. Hook und Rätsel in den ersten drei Sekunden.
2. Eine deutliche Uhr-Einstellung führt zurück in die nächtliche Vernehmung. Brakk bleibt im Raum und hält Zylla bewusst wach; dieselbe Uhr zeigt später eine deutlich andere Zeit.
3. Zyllas Augen fallen zu. Brakks Faust geht in derselben Einstellung hoch und mit einem einzigen harten Geräusch auf den Tisch. Ihre Augen schnellen auf.
4. Erst erschöpft spricht sie. Das kleine Aufnahmegerät leuchtet und zeigt die aufgezeichnete Stimme.
5. Die gezeichnete, frontale Hologrammfläche trägt die exakte Norm `§ 136a StPO`; später `Abs. 3 StPO`.
6. Die Aufnahme läuft sichtbar gegen ein aufleuchtendes Rechtsschutzschild. Ein rotes Kreuz trifft erst auf die unterschriebene Einwilligung, wenn die Pointe ausgesprochen wird: sie heilt die Methode nicht.

**Sprechertext:**

> Zylla willigt ein. Trotzdem: Aussage gesperrt. Warum? Zurück. Brakk hält sie absichtlich die Nacht wach. Stunde um Stunde. Zylla sackt weg. Er fragt weiter. Erschöpft spricht sie. Die Aufnahme läuft. Paragraf einhundertsechsunddreißig A verbietet Ermüdung als Vernehmungsmethode. Absatz drei: Selbst ihre Einwilligung rettet die Aussage nicht. Die Unterschrift heilt den Verstoß nicht.

**Rechtliche Präzision:** Es geht um gezielt herbeigeführte Ermüdung zur Beeinträchtigung der Willensfreiheit, nicht um die Behauptung, jede lange Befragung sei verboten. § 136a Abs. 3 StPO schließt Einwilligung als Heilung aus und verbietet die Verwertung einer so gewonnenen Aussage selbst bei Zustimmung. Amtlicher Gesetzestext: `https://www.gesetze-im-internet.de/stpo/__136a.html` (27.09.2026 geprüft).

**Bilder und Golden References:** Zylla Glitch und Brakk Quarzfaust aus den Golden References des Repositories als bindende Figurenvorlagen. Grüne Haut, genau zwei runde Antennen, pink-violettes Haar, lilafarbene Jacke, schwarzes Herz-Shirt bei Zylla; Brakks Körperbau, blaue Kristalle, weißes Unterhemd und braune Arbeitskleidung. Orange Strafprozessrecht-Palette und identischer Raum. `masters/*.jpg` sind die verwendeten hochauflösenden Projektbilder; die unveränderten ImageGen-PNGs wurden zusätzlich lokal gesichert. Keine Bildkacheln, die später dreifach hochskaliert werden.

**Ton und Text:** Neue Aufnahme mit der bisher freigegebenen ElevenLabs-Erzählerstimme `PhufIH7nYh2Up1uej6aY` (`eleven_multilingual_v2`), exaktes Zeichenalignment. Sieben kleine, ereignisgebundene ElevenLabs-Geräusche: Scanner, Rücklauf, Raum/Uhr, deutlicher Tischschlag, Aufnahmegerät, Rechtsschutzschild und Papiermarkierung. Der Schlag folgt exakt der Faust. Ruhige freigegebene Einzelwort-Captions immer unten, nur der Erzähler, ausgesprochen „einhundertsechsunddreißig A“, als `§ 136a` geschrieben; „Absatz drei“ als `Abs. 3`. Die vom Bildgenerator bewusst frei gelassenen Papier- und Hologrammflächen bekommen ihre überprüfbaren Wörter in Perspektive bzw. innerhalb der gezeichneten Ebene.

**Technik/Abnahme:** 1080 × 1920 H.264, 30 fps, AAC; in der Größenordnung von 30 Sekunden. Ganze Datei mit Ton und auf Mobilgröße ansehen. Vor Freigabe speziell (a) gleiche Figuren- und Raumgeometrie zwischen bearbeiteten Zuständen, (b) kein Doppelbild an Augen/Faust/Schild, (c) Lesbarkeit der Einwilligung, (d) Uhrzeit und Zeit-Rücksprung, (e) Schlag, Scanner und Schild genau im sichtbaren Ereignis, (f) Sprecher und Captions bis zum Schluss prüfen. Nur eine neue Testfassung, keine Slot-Überschreibung.
