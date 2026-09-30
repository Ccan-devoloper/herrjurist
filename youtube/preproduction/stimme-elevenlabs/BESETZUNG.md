# Stimmen-Besetzung (ElevenLabs v4), Stand 30.09.2026

**Grundsätze** (Entscheidung des Kanalinhabers):
- **Erzähler:** eine feste Stimme für den ganzen Kanal: **Carla Blum** (festgelegt am 30.09.2026). Moritz Wegner bleibt Reserve.
- **Fallfiguren:** Sie werden aus einem festen Ensemble besetzt, wie bei einer Theatertruppe.
  - Innerhalb eines Videos bekommt jede Figur eine eigene, klar unterscheidbare Stimme.
  - Über mehrere Videos hinweg dürfen sich Stimmen wiederholen.
- **Serienfiguren** werden gerade neu aufgebaut. Jede bekommt später genau eine feste Stimme.

**Anforderungen an alle Stimmen:**
- deutsch (de-DE), Standardakzent
- mindestens 2 Jahre garantierte Verfügbarkeit (`notice_period` 730)
- keine Inhaltsmoderation durch den Sprecher (Ausnahme: Lea, siehe unten)

**Ensemble nach Hörprüfung:**

| Typ | gut | unsicher |
|---|---|---|
| Mann, jung | Timo, Niklas | |
| Mann, mittel | Stephan, Marc, Christian | Otto |
| Mann, älter | William, Helmut, Opa Johann | |
| Frau, jung | Lucy Fennek | |
| Frau, mittel | Sabrina, Lea¹ | Leonie |
| Frau, älter | Lisa | |

¹ Bei Lea hat der Sprecher eine Inhaltsmoderation eingeschaltet. Sie ist nur für harmlose Sätze geeignet, nicht für Gewalt- oder Tatbeschreibungen.

**Abgelehnt:** Johannes.

**Offen:** Bei jungen und älteren Frauen ist die Auswahl dünn, dort fehlen Ersatzstimmen.

IDs und Status stehen in [`besetzung.json`](besetzung.json). `synth_el.py` akzeptiert im Skript statt einer ID auch den Ensemble-Namen, z. B. `STIMMEN = {"Frank": "christian", "Gisela": "lea"}`.
