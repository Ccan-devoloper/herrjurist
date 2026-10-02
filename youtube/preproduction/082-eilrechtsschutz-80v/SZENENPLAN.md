# Folge 082 · § 80 V VwGO: Imbiss sofort geschlossen – was tun? Das Grundschema – Szenenplan

**Stand:** 02.10.2026 · Serienstandard Open Peeps (Katzenkönig) · Cue-Marken wie in [`src/skript_082.py`](src/skript_082.py) · Belege in [`RECHTSSTAND.md`](RECHTSSTAND.md)
**Format:** Mo · Der Fall (Themenplan-Format „Klassiker-Fall“), Voraussetzung laut Plan: Folge 069 (Anfechtungsklage). Übungsfall nach dem Hook: Frau Steinke von der Lebensmittelüberwachung der Stadt findet in der Imbissbude von Herrn Hinrichs Mäusekot und angenagte Brötchentüten; Herr Hinrichs darf sich äußern; am nächsten Tag schließt die Stadt den Imbiss bis zur Schädlingsbekämpfung und ordnet die sofortige Vollziehung an; er klagt. Ablauf: Fall → Klage und Frage → Sachverhalt → Grundsatz § 80 I 1 (Wortlautkarte) → Entfallen § 80 II 1 (Wortlautkarte Nr. 4) → Antrag § 80 V 1 (Wortlautkarte) → A. Zulässigkeit I.–V. → B. I. formelle Rechtmäßigkeit der Anordnung → B. II. Interessenabwägung (drei Fallgruppen) → Erfolgsaussichten im Fall (Wortlautkarte Art. 138 II h VO (EU) 2017/625) → besonderes Vollzugsinteresse → Beschluss (Richterin) → Nachkontrolle → Klausurtipp → Klausurschema → Merksatz.
**Länge:** Hauptfilm 6:37,1 (5.726 gesprochene Zeichen); Begründung in ABNAHME.md.

## Besetzung

| Figur | Rolle | Open Peeps | Stimme |
|---|---|---|---|
| Herr Hinrichs (HI), um 50 | betreibt seit 20 Jahren eine Imbissbude, Antragsteller | Pose `standing/shirt-3` (weißes Hemd `#FFFFFF`, schwarze Hose), Kopf `Short 4` (Haar `#4A3428`), Haut `#EDB98A`; Mimiken `Smile` (ruhig), `Driven` (redet), `Concerned|Serious` (Sorge), `Suspicious` (denkt), `Rage|Serious` (Ärger), `Tired` (müde), `Smile Big|Smile` (froh) | `marc` (Mann, mittel) |
| Frau Steinke (ST), um 40 | Lebensmittelüberwachung der Stadt | Pose `standing/doctor-nurse-02` (weißer Kittel, Überschuhe – Hygienekleidung bei der Kontrolle), Kopf `Medium 2`, Haut `#F2C7A8`; Mimiken `Serious` (ruhig, redet), `Solemn` (denkt) | `sabrina` (Frau, mittel) |
| die Richterin (RI), um 55 | Verwaltungsgericht (Funktionsrolle ohne Namen) | Pose `standing/shirt-4` (schwarzes Hemd, dunkle Hose `#34343C`), Kopf `Medium Bangs`, Brille `Glasses 3`, Haut `#D9A07A`; Mimiken `Calm` (ruhig), `Serious` (redet) | `laura_ruhig` (Frau, mittel) |
| Lexi | Klausurtipp und Merksatz | nach `lexi.py` (`robot_dance-1`, `Serious`/`Smile`) | Carla Blum |
| Erzählerin | – | – | Carla Blum |

- Grundansicht gespiegelt (blickt nach links zur Tafel), `_r` blickt nach rechts. Szene A und N: Herr Hinrichs blickt nach rechts zu Frau Steinke, sie nach links zu ihm; Szene B: Herr Hinrichs blickt nach links zum Verwaltungsgericht; Szene M: Herr Hinrichs blickt nach rechts zur Richterin, die nach links blickt; an den Tafeln alle nach links.
- **Alle Grundmimiken mit geschlossenem Mund**; Mundzustände a/o/e nur in `HI_redet`, `ST_redet`, `RI_redet` (je links/rechts) und Lexi. Keine Bärte, keine Prothesen-Posen (`blazer-1/-2`, `shirt-1/-2` nicht verwendet).
- **Stimmen nur aus dem Pool** (`marc`, `sabrina`, `laura_ruhig`; `william` nicht gebraucht); Erzählerin/Lexi Carla ohne Rolle.
- **Namen mit eindeutig deutscher Aussprache, neu:** Hinrichs, Steinke (nicht in der Liste früherer Namen; `grep` über alle Folgenordner ohne Treffer); die Richterin bleibt namenlos.
- Herr Hinrichs ist respektvoll gezeichnet: langjähriger Wirt, erschrocken und verärgert, am Ende froh über die Wiedereröffnung; keine Herkunftsmerkmale, keine Klischees. Frau Steinke sachlich.
- Figuren-PNGs: `../peeps/op_082/` (50 Dateien, nicht im Repository, im Drive-Master).

**Abweichung von den letzten Folgen:** 069 (Gewerbegebiet mit Foodtruck, Verwaltungsgericht mit Waage), 074 (Altstadt mit Café), 080/081 (Zivilrecht/Test). Hier **Imbissbude** (Tabler `building-store`, Pommes, Wurst), Kontrolle mit Klemmbrett, Maus als Zeichen des Befalls, Schloss als Schließung. Das Verwaltungsgericht (Säulengebäude, Waage) kehrt bewusst wieder, weil Klage und Eilantrag dort spielen – andere Besetzung und Posen (`shirt-3`, `doctor-nurse-02`, `shirt-4` in 069/074 nicht verwendet). Die Imbissbude kehrt am Ende zurück (Nachkontrolle), weil die Geschichte dorthin zurückkehrt. Kein Richterhammer. Tageslicht-Cremegrund.

## Szenen

| Szene | Ort / Handlung | Requisiten (Iconset:Name, Füllung) | Tafel / Prüfpfad | Bildhalte (Zwiebelschale) | Geräusch |
|---|---|---|---|---|---|
| **A Imbiss** `fall`–`hi1` | Imbissbude, Sonne; Herr Hinrichs; Frau Steinke kontrolliert; Mäusekot; Blase Steinke; Bescheid; Schloss; Blase Hinrichs | tabler:`building-store` (Gelb), fluent-hc:`french-fries`, tabler:`sausage` (Rot), `sun`, `clipboard-check`, fluent-hc:`mouse`, tabler:`file-text`, `lock`; Pillen | `Fall · Mittag an der Imbissbude` (ab 0,0 s), `Fall · Die Kontrolle`, `Fall · Der Bescheid` | Imbiss · Speisen · Steinke · Klemmbrett · Mäusekot · Tüten · Sorge · Blase · Bescheid · Schloss · Schließung · Vollziehung · Grund · Ärger · Blase Hinrichs | Papier (`szene_082brief_1`), als der Bescheid erscheint |
| **B Verwaltungsgericht** `klage`–`frage` | Herr Hinrichs mit der Klage vor dem Gericht; Fragen | fluent-hc:`classical-building`, tabler:`file-text` | `Fall · Die Klage`, `Fall · Darf er wieder öffnen?` | Gericht · Pille · Klage · Frage 1 · Frage 2 | – |
| **C Sachverhalt** `sv` | Karte zum Nachlesen | – | `Sachverhalt` | 1 | – |
| **D Grundsatz** `wl801`–`aw2` | Wortlautkarte § 80 I 1 | tabler:`hand-stop` (Grün) | `Grundsatz · Aufschiebende Wirkung, § 80 I 1 VwGO` | Karte · Marker · Vollziehung · hätte recht (froh) | – |
| **E Entfallen** `wl802`–`hier` | Nr. 1–3a, Wortlautkarte Nr. 4, „hier“ | `hand-stop` + Kreuz | `Entfallen · § 80 II 1 VwGO`, `… Nr. 4 VwGO` | Titel · Nr. 1–3a · Karte · Marker · Anordnung · Kreuz | – |
| **F Antrag** `wl805`–`antrag` | Wortlautkarte § 80 V 1; Anordnung/Wiederherstellung | fluent-hc:`classical-building` + Pille | `Rechtsschutz · Antrag nach § 80 V 1 VwGO` | Karte · 2 Marker · 2 Zeilen · Antrag | – |
| **G A. I.–II.** `zul`–`statt2` | Rechtsweg, Statthaftigkeit, § 123 V | `classical-building` | `A. Zulässigkeit › I. …`, `› II. Statthaftigkeit` | Zeilen · Haken · Block · Abgrenzung | – |
| **H A. III.–V.** `befugt`–`zul2` | Antragsbefugnis, Antragsgegner, Rechtsschutzbedürfnis, § 80 VI, zulässig | tabler:`building` + Pille „Stadt“ | `› III. …`, `› IV. …`, `› V. Rechtsschutzbedürfnis` | Zeilen · Haken · Block | – |
| **I B. I. formell** `begr`–`anh` | Zuständigkeit, § 80 III 1, Einzelfall, Inhalt egal, Fehlerfolge, Fall, Anhörung str. | `file-text` + Pille; Frau Steinke | `B. Begründetheit › I. formelle Rechtmäßigkeit der Anordnung (› Anhörung?)` | Zeilen · Fundstellen · Haken | – |
| **J B. II. Abwägung** `abw`–`fg3` | eigene Abwägung, drei Fallgruppen | fluent-hc:`balance-scale` + Pillen | `B. Begründetheit › II. Interessenabwägung (› Erfolgsaussichten, › Folgenabwägung)` | Zeilen · drei Blöcke · Fundstellen | – |
| **K Erfolgsaussichten im Fall** `egl`–`offen` | Wortlautkarte Art. 138 II h; Hygieneregeln; Verhältnismäßigkeit | fluent-hc:`mouse` + Pille | `… › Erfolgsaussichten im Fall` | Karte · Marker · Verstoß · Fundstelle · Block · Haken | – |
| **L Vollzugsinteresse** `eilig` | Gäste, Dringlichkeit | tabler:`users`; Frau Steinke | `… › besonderes Vollzugsinteresse` | Zeilen · Block | – |
| **M Beschluss** `urteil`–`ri1` | Richterin, Herr Hinrichs; Blase | `balance-scale` | `Ergebnis · Der Beschluss` | Hinrichs · Richterin · Blase · Pille · müde | – |
| **N Nachkontrolle** `ende` | zurück an der Imbissbude; Schloss weg; Haken | Imbiss, `lock`, `clipboard-check` | `Ergebnis · Die Nachkontrolle` | Imbiss · bekämpft · Steinke · Haken · froh | – |
| **O Klausurtipp** `tipp`–`tipp2` | Lexi warnt | Warnsymbol (Streamline Freehand) | `Klausurtipp · Anordnung oder Wiederherstellung?` | Zeilen | – |
| **P Klausurschema** `sch`–`s10` | progressiv: A I.–V., B I., II. 1.–3. | – | `Klausurschema · § 80 V VwGO` | 14 Aufbaustufen | – |
| **Q Merksatz** `merke`–`m2` | Lexi erklärt | – | `Merksatz` | Marker | – |

## Sachverhaltskarte

„Herr Hinrichs betreibt seit 20 Jahren eine Imbissbude. Bei einer Kontrolle findet Frau Steinke von der Lebensmittelüberwachung der Stadt Mäusekot auf der Arbeitsfläche und angenagte Brötchentüten; Herr Hinrichs kann sich dazu äußern. Am nächsten Tag erhält er den schriftlichen Bescheid: Die Stadt schließt den Imbiss, bis die Mäuse bekämpft sind und eine Nachkontrolle das bestätigt. Sie ordnet die sofortige Vollziehung an und begründet das schriftlich: Die Gesundheit der Gäste könne nicht bis zum Ende eines Prozesses warten. Herr Hinrichs erhebt Klage beim Verwaltungsgericht.“ – Frage: „Darf er jetzt wieder öffnen? Und was kann er sofort tun?“ (kein Fiktiv-Hinweis)
