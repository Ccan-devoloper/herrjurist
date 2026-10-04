# Open-Peeps-Vorproduktion (Variante C)

Rendert Karussells, Reels und Stories für Herrjurist aus Tagesbeschreibungen in `tage/<datum>.json` (Kanal-Einstellungen in `marke.json`; derselbe Renderer läuft beim Schwesterkanal Examenscampus).
Die Redaktionsregeln stehen in [REDAKTION.md](REDAKTION.md), das Eingabeformat in [SPEC.md](SPEC.md), ein vollständiger Tag in [BEISPIEL.json](BEISPIEL.json).

```
bash op/einrichten.sh                         # einmalig: Schriften, Icons, Blasen-Engine (.res/)
python3 op/tag.py 2026-10-04 --ziel <instagram-assets-Checkout>
python3 op/tag.py 2026-10-04 --ziel … --pruefen-nur   # nur rendern und prüfen, nichts schreiben
```

| Datei | Aufgabe |
|---|---|
| `opkern.py` | Palette, Rahmen in der Klausurfarbe, Schlagzeile, Normzeile, Kalenderblatt, Zahlblock, Gesetzesseite |
| `figuren.py` | Besetzung je Beitrag aus der Open-Peeps-Bibliothek (CC0), Kürzel `A:froh` (Brustbild) / `A/eilt` (stehend) |
| `karussell.py` | Folientypen cover, schritte, inhalt, zeitstrahl, rechnung, vergleich, merke, gesetz |
| `story.py` | Story-Arten frage, antwort, teaser, norm, countdown, tipp, merksatz, anlass |
| `reel.py`, `stimme.py` | Reel mit Hook-Stilen, Szenen, Merke; Vertonung ElevenLabs (Laura) mit Wortzeiten |
| `tag.py` | Tageslauf: rendern, Quellenprüfung (`bin/op-pruefen.mjs`), Ablage für `vorproduktion-live.mjs` und Dashboard |

Kosten: Rendern lokal (0 €). Reels verbrauchen nur das Zeichenkontingent des ElevenLabs-Abos; gleiche Texte
kommen aus dem Cache. Lizenzen: Open Peeps CC0, Nunito/DM Sans/Liberation SIL OFL, Tabler/Phosphor/Fluent MIT,
MingCute Apache 2.0, Pepicons/Streamline CC BY 4.0, Comical.js/perfect-freehand MIT, Geräusche Freesound CC0
(Herkunft in `ressourcen/sfx/herkunft.json`).
