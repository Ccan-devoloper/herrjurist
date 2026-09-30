# Prompt für ChatGPT (Bildgenerierung): neue Open-Peeps-Posen

**So verwenden:** Die PDF `OpenPeeps-Erweiterung-Referenzen.pdf` hochladen, besser zusätzlich die drei PNG-Blätter einzeln, weil das Bildmodell PNGs genauer liest als PDF-Seiten. Dann den Prompt unten einfügen. Immer **eine Pose pro Bild** anfordern und nach jedem Bild mit „Nächste Pose: …“ weitermachen.

---

## Prompt (zum Kopieren)

Du erweiterst die Illustrationsbibliothek „Open Peeps“ von Pablo Stanley (CC0) um neue Posen für juristische Erklärvideos. Die angehängten Referenzblätter zeigen:
- **Blatt 1:** alle vorhandenen Open-Peeps-Posen (stehend, sitzend, Büste). Das ist der verbindliche Zeichenstil.
- **Blatt 2:** alle Gesichter, Frisuren, Bärte und Brillen. Köpfe und Mimik exakt in diesem Stil.
- **Blatt 3:** unsere festen Serienfiguren in Farbe mit Farbpalette. Neue Posen müssen diese Figuren wiedererkennbar treffen.

### Stilregeln (streng einhalten)
1. Exakt der Open-Peeps-Stil: handgezeichnete, gleichmäßig dicke schwarze Tuschelinie (#151515), leicht unregelmäßig wie mit Pinselstift, runde Linienenden. Proportionen, Kopfform, Hände und Füße wie in Blatt 1.
2. Flächen flach gefüllt, **nur** Farben aus der Palette auf Blatt 3. Keine Verläufe, keine Schatten, keine Glanzlichter, keine Texturen, kein 3D, kein Anime-/Pixar-Look.
3. Gesichter nur aus den Ausdrücken von Blatt 2 (z. B. Angry, Rage, Concerned, Fear, Smile, SmileBig, Awe, Serious, Suspicious, Tired). Keine neuen Augen- oder Mundformen erfinden.
4. Die Figur exakt wie auf Blatt 3: gleiche Kleidung, Farben, Frisur, Bart, Brille, Hautton (Hex-Werte stehen dort).
5. Hände mit fünf Fingern, anatomisch plausibel, im vereinfachten Open-Peeps-Stil.

### Technische Vorgaben
- **Transparenter Hintergrund** (PNG mit Alphakanal), kein Boden, kein Schatten, keine Umgebung, kein Text, kein Rahmen.
- **Ganzkörper vollständig** im Bild, nichts angeschnitten (Kopf, Hände, Füße sichtbar), ca. 5 % Rand.
- Hochformat 1024 × 1536 px, Figur ca. 90 % der Bildhöhe, Füße auf gleicher Grundlinie (bei stehenden Posen).
- Blickrichtung: Figur schaut nach **rechts**, sofern nicht anders angegeben. Spiegeln erledigen wir selbst.
- Eine Pose pro Bild. Dateiname im Antworttext nennen: `<FIGUR>_<POSE>.png`.

### Ablauf
Zuerst **nur die Stilprobe** (Nr. 1 unten) erzeugen und auf mein OK warten. Erst danach die weiteren Posen einzeln, in der Reihenfolge der Liste.

### Benötigte Posen

| Nr. | Datei | Figur (Blatt 3) | Pose und Mimik |
|---:|---|---|---|
| 1 | `A_faustschlag.png` | A (gelbes Shirt, Vollbart) | Schlägt mit geballter rechter Faust waagerecht nach vorn, Oberkörper nach vorn gelehnt, Ausfallschritt. Gesicht: Rage |
| 2 | `B_getroffen.png` | B (schwarzes Shirt, blaue Hose, Brille) | Taumelt nach hinten, eine Hand an der Nase, Oberkörper zurückgelehnt. Gesicht: ConcernedFear |
| 3 | `B_sprint.png` | B | Rennt schnell, weiter Laufschritt, Arme schwingen. Gesicht: Explaining (ruft) |
| 4 | `B_handy_zeigen.png` | B | Steht, streckt ein Smartphone mit einer Hand nach vorn entgegen. Gesicht: Smile |
| 5 | `B_liegt_nase.png` | B | Sitzt am Boden, eine Hand an der Nase, andere stützt ab. Gesicht: Tired |
| 6 | `AN_arm_hoch.png` | Anton (türkises Langarmshirt) | Steht, rechter Arm ganz nach oben gestreckt, Handfläche offen (Handzeichen/Gebot). Gesicht: SmileBig |
| 7 | `AN_winkt.png` | Anton | Winkt mit erhobener Hand seitlich. Gesicht: Smile |
| 8 | `AN_schulterzucken.png` | Anton | Schulterzucken, beide Handflächen nach oben. Gesicht: Concerned |
| 9 | `AN_grübelt.png` | Anton | Hand am Kinn, nachdenklich. Gesicht: Serious |
| 10 | `AN_unterschreibt.png` | Anton | Steht leicht vorgebeugt, hält Stift und Blatt Papier, schreibt. Gesicht: Calm |
| 11 | `AN_zahlt.png` | Anton | Reicht mit ausgestrecktem Arm Geldscheine nach vorn. Gesicht: Smile |
| 12 | `AN_telefoniert.png` | Anton | Hält Smartphone ans Ohr. Gesicht: Explaining |
| 13 | `AN_abwehr.png` | Anton | Beide Hände abwehrend vor dem Körper, einen Schritt zurück. Gesicht: Fear |
| 14 | `VK_hammer.png` | Auktionator (lila Blazer, grauer Bart) | Hebt einen Auktionshammer zum Zuschlag. Gesicht: Explaining |
| 15 | `VK_paket.png` | Auktionator | Übergibt mit beiden Händen ein Paket nach vorn. Gesicht: Smile |
| 16 | `ER_zeigt_links.png` | Erzähler (gelbe Jacke, Afro, runde Brille) | Zeigt mit ausgestrecktem Arm nach links, zur Seite schauend (für Tafelhinweise). Gesicht: Explaining |
| 17 | `ER_daumen_hoch.png` | Erzähler | Daumen hoch. Gesicht: SmileBig |
| 18 | `ER_warnt.png` | Erzähler | Erhobener Zeigefinger, warnend. Gesicht: Concerned |
| 19 | `DIEB_rennt_tasche.png` | neue Figur: Hoodie dunkelgrau (#3C3C44), Frisur ShortMessy, Haut #E0A57E | Rennt weg, trägt eine Handtasche unter dem Arm, blickt über die Schulter. Gesicht: Suspicious |
| 20 | `POLIZEI_notiert.png` | neue Figur: blaue Uniform (#8DB3F2) mit Mütze, Frisur Short, Haut #7B4B34 | Steht, schreibt auf Notizblock. Gesicht: Serious |
| 21 | `RICHTER_robe.png` | neue Figur: schwarze Robe, weiße Halsbinde, Frisur GrayMedium, Haut #F6D2B4 | Steht, hält Richterhammer, erhobene Hand. Gesicht: Serious |
| 22 | `ANWAELTIN_akte.png` | neue Figur: Blazer Pink (#F6A5C0), Frisur MediumStraight, Haut #B07552 | Steht, hält Akte unter dem Arm, andere Hand erklärend. Gesicht: Explaining |

### Requisiten (separat, gleicher Stil)
Einzeln auf transparentem Hintergrund, 1024 × 1024 px, gleiche Tuschelinie und Palette, kein Text:
Smartphone, Küchenmesser, Geldscheine (Bündel), Vertrag mit Unterschriftszeile, Paket, Auktionshammer, Weinflasche, Weinglas, Handtasche, Straßenlaterne, Parkbank, Bahnhofsschild (ohne Schrift), Stuhl, Schreibtisch, Tür, Schlüssel, Auto (Seitenansicht), Fahrrad, Einkaufswagen, Ladenregal.

### Nicht erwünscht
Verläufe, Schatten, fotorealistische Details, dicke Konturen um das ganze Bild, abgeschnittene Körperteile, zusätzliche Figuren, Text/Wasserzeichen, andere Farben als die Palette, abweichende Kleidung der Serienfiguren.

---

## Hinweise für uns
- **Prüfen vor der Übernahme:** jede Pose neben Blatt 1 und 3 legen. Achten auf Linienstärke, Kopfform, Hände und exakte Farben (Hex prüfen). Abweichende Bilder verwerfen oder mit „Linie dünner“, „exakt Farbe #… verwenden“ und ähnlichem nachschärfen lassen.
- **Freistellen:** Liefert ChatGPT keinen echten Alphakanal, stelle ich die Bilder frei (einfarbiger Hintergrund lässt sich sauber entfernen).
- **Rechtliches:** Open Peeps ist CC0, als Stilvorlage also unproblematisch. Für KI-generierte Bilder gelten die Nutzungsbedingungen von OpenAI (kommerzielle Nutzung erlaubt). Urheberrechtlichen Schutz genießen solche Bilder in der Regel nicht, sie sind also auch für Dritte frei nutzbar.
