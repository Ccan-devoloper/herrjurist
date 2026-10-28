"""Folge 184 · Staatstrojaner und IT-Grundrecht: Darf die Polizei mitlesen? (Mo · Der Fall · Klassiker-Fall; Öffentliches
Recht/Grundrechte; Art. 2 I i.V.m. 1 I, 10, 13 GG; §§ 100a, 100b StPO). Voraussetzung: Folge 016 (Volkszählungsurteil,
informationelle Selbstbestimmung) – nur in einem Satz verwiesen.
Leitentscheidung: BVerfG, Urt. v. 27.2.2008 – 1 BvR 370/07, 595/07 (BVerfGE 120, 274, Online-Durchsuchung; Verfahren gegen
§ 5 Abs. 2 Nr. 11 VSG NRW), Rn. 166–207, 247, 257–259, 271–283. Rechtsstand: BVerfG, Beschl. v. 24.6.2025 – 1 BvR 2466/19
(Trojaner I, LS 3, Rn. 93–110) und – 1 BvR 180/23 (Trojaner II, LS 1–3, Tenor, Rn. 134, 172–176, 201–213, 241–251, 275, 276);
BVerfGE 141, 220 (BKAG, Rn. 212). Normen: Art. 10 Abs. 1, Art. 13 Abs. 1 GG; § 100a Abs. 1 S. 2, 3, § 100b Abs. 1, 2,
§ 100d Abs. 1–3, § 100e Abs. 2 StPO; § 146 StGB (gesetze-im-internet.de, Abruf 04.10.2026). Belege je Cue: ../RECHTSSTAND.md.
Fiktiver Fall: Kriminalhauptkommissar Hollstein (Stimme helmut) ermittelt gegen Herrn Weinhold (Stimme niklas) wegen des
Verdachts der Geldfälschung durch eine Bande (§ 146 Abs. 1, 2 StGB; Katalogtat § 100a Abs. 2 Nr. 1 Buchst. e, § 100b Abs. 2
Nr. 1 Buchst. d StPO). Polizei neutral, keine Behördenlogos, keine echten Messenger-Logos, keine Anleitung zur Überwachung.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Volltextsuche 04.10.2026): Weinhold, Hollstein.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Normen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Hollstein": "helmut", "Weinhold": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall ---------------------------------------------------------------------------------------------------------
    ("[fall]Die Polizei will heimlich Software auf einem Laptop installieren, um die Chats mitzulesen. [weinh]Der Laptop "
     "gehört Herrn Weinhold. [verd]Bestimmte Tatsachen begründen den Verdacht, dass er mit einer Bande Falschgeld herstellt. "
     "[chat]Abgesprochen wird alles über einen verschlüsselten Messenger.", P),
    ("[w1]Alles verschlüsselt. Da liest keiner mit.", P, "Weinhold"),
    ("[holl]Kommissar Hollstein sieht das anders.", 0.2),
    ("[h1]Abhören bringt uns nichts, die Chats sind verschlüsselt. Wir müssen direkt auf seinen Laptop.", P, "Hollstein"),
    ("[frage]Darf der Staat heimlich in einen Computer eindringen? Und welches Grundrecht schützt davor?", 0.6),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Schutzbereich: Art. 10, Art. 13, informationelle Selbstbestimmung ---------------------------------------------
    ("[art10]Erster Kandidat: Artikel zehn. Das Briefgeheimnis sowie das Post- und Fernmeldegeheimnis sind unverletzlich. "
     "[lauf]Geschützt ist die laufende Kommunikation über Distanz, auch im Internet. [gesp]Nicht aber Daten, die "
     "nach Abschluss der Kommunikation auf dem Gerät liegen, [ganz]und nicht das Durchsuchen des ganzen Systems.", P),
    ("[art13]Zweiter Kandidat: Artikel dreizehn. Die Wohnung ist unverletzlich. [raum]Geschützt ist aber der Raum, nicht "
     "das Gerät. [fern]Ein Zugriff über das Netz funktioniert unabhängig vom Standort, gerade bei einem Laptop.", P),
    ("[ris]Bleibt die informationelle Selbstbestimmung aus dem Video zum Volkszählungsurteil. [ris2]Sie reicht hier "
     "nicht ganz aus: [ris3]Wer in ein ganzes System eindringt, bekommt einen riesigen "
     "Datenbestand.", P),
    ("[luecke]Es bleibt eine Schutzlücke. [d08]Zweitausendacht schließt das "
     "Bundesverfassungsgericht sie, in einem Fall zum Verfassungsschutz in Nordrhein-Westfalen. "
     "[itgr]Das allgemeine Persönlichkeitsrecht, Artikel zwei Absatz eins in Verbindung mit Artikel eins Absatz eins, umfasst "
     "das Grundrecht auf Gewährleistung der Vertraulichkeit und Integrität informationstechnischer Systeme, kurz "
     "IT-Grundrecht. [vertr]Geschützt ist, dass die Daten auf dem System vertraulich bleiben, [integr]und dass niemand "
     "das System heimlich infiltriert.", PS),
    # --- D Quellen-TKÜ und Online-Durchsuchung --------------------------------------------------------------------------
    ("[stpo]Nun zur Strafprozessordnung. [q1]Paragraf hundert a Absatz eins Satz zwei erlaubt die "
     "Quellen-Telekommunikationsüberwachung: [q1b]Die Ermittler dürfen in das genutzte System eingreifen, wenn das nötig ist, "
     "um die Kommunikation insbesondere unverschlüsselt zu überwachen. [q2]Satz drei erfasst auch gespeicherte "
     "Nachrichten, die schon während der Übertragung hätten überwacht werden können.", P),
    ("[q08]Zweitausendacht sagte das Gericht: Bleibt die Überwachung sicher auf die laufende Kommunikation "
     "beschränkt, ist allein Artikel zehn der Maßstab. [q25]Zweitausendfünfundzwanzig sieht das Gericht das anders: Wer "
     "dafür in das eigene System eingreift, trifft zugleich das IT-Grundrecht. [beide]Geprüft wird an beiden.", PS),
    ("[od]Noch weiter geht Paragraf hundert b, die Online-Durchsuchung. [od1]Die Ermittler dürfen in das System eingreifen "
     "und Daten daraus erheben, also alles, was dort gespeichert ist. [odm]Maßstab ist das IT-Grundrecht, und weil auch "
     "laufende Kommunikation erfasst wird, zugleich Artikel zehn.", PS),
    # --- E Rechtfertigung -----------------------------------------------------------------------------------------------
    ("[schr]Schrankenlos gilt das IT-Grundrecht nicht. Eingriffe können zur Gefahrenabwehr und zur Strafverfolgung "
     "gerechtfertigt sein. [gef]Zur Gefahrenabwehr verlangt das Gericht tatsächliche Anhaltspunkte einer konkreten Gefahr für "
     "ein überragend wichtiges Rechtsgut: [gut]Leib, Leben und Freiheit der Person oder die Grundlagen des Staates und der "
     "Existenz der Menschen. [straf]Bei der Strafverfolgung kommt es auf das Gewicht der Tat an: Nötig ist der Verdacht einer "
     "besonders schweren Straftat.", P),
    ("[richt]Dazu kommt der Richtervorbehalt: Grundsätzlich muss vorher ein Richter entscheiden. [kern]Und der Kernbereich "
     "privater Lebensgestaltung ist absolut geschützt. [kern2]Höchstpersönliches, etwa tagebuchartige Dateien, soll möglichst "
     "gar nicht erhoben werden. [kern3]Wird es doch erfasst, ist es unverzüglich zu löschen und darf nicht verwertet werden.", PS),
    ("[n1]Seit zweitausendfünfundzwanzig braucht auch die Quellen-Telekommunikationsüberwachung "
     " wegen des Systemzugriffs den Verdacht einer besonders schweren Straftat. [n2]Soweit sie für Taten mit höchstens "
     "drei Jahren Freiheitsstrafe erlaubt war, ist sie nichtig. [zit]Und Paragraf hundert b nennt Artikel zehn nicht, wie es "
     "das Zitiergebot verlangt. [fort]Die Vorschrift ist deshalb verfassungswidrig, gilt aber bis zu einer Neuregelung fort.", PS),
    # --- F Lösung -------------------------------------------------------------------------------------------------------
    ("[loes]Zurück zu Herrn Weinhold. [l1]Geldfälschung ist im Katalog der besonders schweren Straftaten genannt. [l2]Der Verdacht "
     "stützt sich auf bestimmte Tatsachen, [l3]die Tat wiegt auch im Einzelfall besonders schwer, [l4]und ohne die Maßnahme wäre "
     "die Aufklärung wesentlich erschwert.", P),
    ("[l5]Sollen nur die laufenden Chats mitgelesen werden, ist das eine Quellen-Telekommunikationsüberwachung, gemessen an "
     "Artikel zehn und am IT-Grundrecht. [l6]Soll der ganze Laptop durchsucht werden, ist es eine Online-Durchsuchung nach "
     "Paragraf hundert b. [l7]Anordnen muss beides grundsätzlich ein Gericht, auf Antrag der Staatsanwaltschaft, [l8]und Höchstpersönliches "
     "muss gelöscht werden.", P),
    ("[h2]Dann geht der Antrag ans Gericht. Ohne Beschluss läuft nichts.", PS, "Hollstein"),
    # --- G Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bestimme das Grundrecht nach der Art des Zugriffs. [t1]Wird die Kommunikation nur auf dem "
     "Übertragungsweg abgefangen: Artikel zehn. [t2]Wird dafür in das eigene Gerät eingegriffen: Artikel zehn und "
     "IT-Grundrecht. [t3]Wird das System durchsucht: IT-Grundrecht, bei laufender Kommunikation zusätzlich Artikel zehn. [t4]Artikel dreizehn nur, wenn Ermittler die "
     "Wohnung betreten oder über Kamera und Mikrofon in die Wohnung schauen.", PS),
    # --- H Klausurschema ------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfungsschema. [k1]Römisch eins, Schutzbereich: das Grundrecht nach der Zugriffsart. [k2]Römisch "
     "zwei, Eingriff: der heimliche Zugriff auf das System. [k3]Römisch drei, Rechtfertigung: [k4]eine normenklare gesetzliche "
     "Grundlage, [k5]der Verdacht einer besonders schweren Straftat oder eine konkrete Gefahr für ein überragend wichtiges Rechtsgut, "
     "[k6]der Richtervorbehalt, [k7]der Schutz des Kernbereichs [k8]und, wenn Artikel zehn betroffen ist, das Zitiergebot.", PS),
    # --- I Merksatz (Lexi) ----------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer heimlich in einen Computer eindringt, greift in das IT-Grundrecht ein. [m2]Das ist nur beim Verdacht "
     "besonders schwerer Straftaten oder bei konkreter Gefahr für überragend wichtige Rechtsgüter erlaubt, mit "
     "Richtervorbehalt und Schutz des Kernbereichs.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
