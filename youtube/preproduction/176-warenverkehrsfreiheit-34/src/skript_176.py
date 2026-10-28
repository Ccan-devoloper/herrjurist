"""Folge 176 · Warenverkehrsfreiheit Schema: Art. 34 AEUV mit Dassonville (Mi · Examenswissen · Öffentliches Recht/
Europarecht, Format Schema). Übungsfall nach dem Plan-Hook (Staaten bewusst unbenannt): Frau Trautmann betreibt einen
Getränkegroßhandel und kauft Whisky als Parallelimporteurin bei einem Großhändler im Nachbarland; eine Verordnung ihres Landes
verlangt für importierten Whisky ein Echtheitszeugnis der Behörden des Herstellerlandes (ebenfalls EU-Staat), das praktisch
nur bekommt, wer direkt beim Hersteller kauft. Herr Kleinschmidt (Lebensmittelüberwachung) verbietet den Verkauf.
Whisky nur als neutrale Flaschen-/Kisten-Icons ohne Marke, kein Trinken, keine Bar.
Aufbau: Fall → Sachverhalt → Norm (Art. 34 AEUV als Wortlautkarte, vorgelesen) → Prüfschema mit eigener Farbe je Punkt:
1. Schutzbereich (Ware nach Kommission/Italien, Rs. 7/68; grenzüberschreitender Bezug), 2. Adressat (Mitgliedstaat,
staatliche Maßnahme), 3. Beschränkung (mengenmäßig oder Maßnahme gleicher Wirkung; der echte Fall Dassonville knapp, Formel
wörtlich nach Rn. 5; Keck Rn. 16 in einem Satz), 4. Rechtfertigung (Art. 36 AEUV als Wortlautkarte, Merkmale gesprochen;
Cassis de Dijon Rn. 8 in einem Satz; Verhältnismäßigkeit nach C-110/05 Rn. 59; Dassonville Rn. 6 und 7/9) → Lösung
(unmittelbare Wirkung, Iannelli Rn. 13; Anwendungsvorrang, Verweis Folge 127) → Klausurtipp (Lexi; Art. 30 AEUV ein Halbsatz,
Keck) → Klausurschema → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Volltextsuche 04.10.2026): Trautmann,
Kleinschmidt (nie im Genitiv). Stimmen: Frau Trautmann laura_ruhig (Frau, mittel), Herr Kleinschmidt william (Mann, älter).
Lexi = Erzählerin Carla. Reale Beteiligte (Dassonville, Keck) nur als Fallnamen, keine Figuren.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Normen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Trautmann": "laura_ruhig", "Kleinschmidt": "william"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Lager des Getränkegroßhandels ------------------------------------------------------------------------
    ("[fall]Frau Trautmann betreibt einen Getränkegroßhandel. [kauf]Ihren Whisky kauft sie günstig bei einem Großhändler im "
     "Nachbarland, wo die Flaschen schon rechtmäßig im Handel sind. [para]Sie ist Parallelimporteurin: Sie kauft nicht beim "
     "offiziellen Alleinimporteur. [zeug]Doch eine Verordnung ihres Landes verlangt für importierten Whisky ein "
     "Echtheitszeugnis der Behörden des Herstellerlandes, [hland]eines anderen EU-Staats. [allein]Das bekommt praktisch nur, "
     "wer direkt beim Hersteller kauft.", P),
    ("[klein]Herr Kleinschmidt von der Lebensmittelüberwachung prüft das Lager.", P),
    ("[k1]Ohne Echtheitszeugnis dürfen Sie diese Kisten nicht verkaufen.", P, "Kleinschmidt"),
    ("[t1]Das Zeugnis bekomme ich nie. Die Flaschen sind echt, hier sind meine Rechnungen.", P, "Trautmann"),
    ("[frage]Verstößt die Pflicht zum Echtheitszeugnis gegen die Warenverkehrsfreiheit?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Norm und Schema ---------------------------------------------------------------------------------------------
    ("[norm]Die Norm ist Artikel vierunddreißig des Vertrags über die Arbeitsweise der Union: [a34]Mengenmäßige "
     "Einfuhrbeschränkungen sowie alle Maßnahmen gleicher Wirkung sind zwischen den Mitgliedstaaten verboten. [sch4]Du prüfst "
     "in vier Schritten: [p1]Schutzbereich, [p2]Adressat, [p3]Beschränkung [p4]und Rechtfertigung.", PS),
    # --- D 1. Schutzbereich ----------------------------------------------------------------------------------------------
    ("[s1]Erstens: der Schutzbereich. [ware]Waren sind nach dem Gerichtshof Erzeugnisse, die einen Geldwert haben und deshalb "
     "Gegenstand von Handelsgeschäften sein können. [ital]So entschied er neunzehnhundertachtundsechzig gegen Italien, sogar für "
     "Kunstwerke und historische Gegenstände. [whisky]Whisky ist also eine Ware. [grenz]Und der Bezug ist grenzüberschreitend: "
     "Die Flaschen kommen aus anderen Mitgliedstaaten.", PS),
    # --- E 2. Adressat ---------------------------------------------------------------------------------------------------
    ("[s2]Zweitens: der Adressat. [mst]Artikel vierunddreißig bindet die Mitgliedstaaten, es braucht also eine staatliche "
     "Maßnahme. [vo]Hier verlangt das Land selbst das Zeugnis, durch eine Verordnung.", PS),
    # --- F 3. Beschränkung: Dassonville, Keck -----------------------------------------------------------------------------
    ("[s3]Drittens: die Beschränkung. [menge]Mengenmäßige Beschränkungen sind ganze oder teilweise Einfuhrverbote. "
     "[mgw]Spannender ist die Maßnahme gleicher Wirkung. [dass]Was das ist, bestimmte der Gerichtshof neunzehnhundertvierundsiebzig "
     "im Fall Dassonville. [bel]Belgien verlangte für Scotch Whisky eine Ursprungsbescheinigung der britischen Zollbehörden. "
     "[frank]Händler hatten den Whisky in Frankreich gekauft, wo er im freien Verkehr war. [schwer]Für sie war die "
     "Bescheinigung nur unter erheblichen Schwierigkeiten zu beschaffen. [formel]Der Gerichtshof: Jede Handelsregelung der "
     "Mitgliedstaaten, die geeignet ist, den innergemeinschaftlichen Handel unmittelbar oder mittelbar, tatsächlich oder "
     "potentiell zu behindern, ist als Maßnahme mit gleicher Wirkung wie eine mengenmäßige Beschränkung anzusehen. "
     "[weit]Das ist weit: Schon die Eignung zur Behinderung genügt.", PS),
    ("[keck]Eine Grenze zog der Gerichtshof neunzehnhundertdreiundneunzig im Fall Keck: Regeln über bestimmte "
     "Verkaufsmodalitäten fallen nicht darunter, wenn sie für alle Wirtschaftsteilnehmer im Inland gelten und den Absatz "
     "inländischer wie eingeführter Waren rechtlich wie tatsächlich gleich berühren. [kfall]Das Zeugnis regelt aber keine Verkaufsmodalität, "
     "sondern die Einfuhr, und es trifft nur eingeführten Whisky. [mgw2]Also ist es eine Maßnahme gleicher Wirkung.", PS),
    # --- G 4. Rechtfertigung: Art. 36, Cassis, Verhältnismäßigkeit, Dassonville -------------------------------------------
    ("[s4]Viertens: die Rechtfertigung. [a36]Nach Artikel sechsunddreißig können Beschränkungen gerechtfertigt sein, etwa "
     "zum Schutz der Gesundheit [eig]oder des gewerblichen und kommerziellen Eigentums. [satz2]Sie dürfen aber weder ein "
     "Mittel zur willkürlichen Diskriminierung noch eine verschleierte Beschränkung des Handels sein. [cassis]Daneben erkennt "
     "der Gerichtshof seit Cassis de Dijon zwingende Erfordernisse an, etwa den Verbraucherschutz und die Lauterkeit des "
     "Handelsverkehrs. [vhm]In beiden Fällen muss die Maßnahme geeignet sein und darf nicht über das Erforderliche "
     "hinausgehen.", PS),
    ("[dfal]Im Fall Dassonville durfte der Staat gegen unlautere Verhaltensweisen bei Ursprungsbezeichnungen vorgehen. "
     "[sinn]Aber nur mit Maßnahmen, die sinnvoll sind und deren Nachweise von allen Staatsangehörigen erbracht werden können. "
     "[direkt]Knüpft er den Nachweis an Formalitäten, die praktisch nur Direktimporteure erfüllen, kann das eine verschleierte "
     "Beschränkung sein.", PS),
    # --- H Lösung ----------------------------------------------------------------------------------------------------------
    ("[loes]Zurück zu Frau Trautmann. [l1]Whisky ist eine Ware aus anderen Mitgliedstaaten. [l2]Das Zeugnis verlangt ihr "
     "Land, eine staatliche Maßnahme. [l3]Es behindert die Einfuhr, ist also eine Maßnahme gleicher Wirkung. [l4]Der Schutz "
     "der Verbraucher vor gefälschtem Whisky ist ein legitimes Ziel. [l5]Aber das Zeugnis schließt Parallelimporteure faktisch aus. "
     "[mild]Das Land kann auch Nachweise zulassen, die jeder Händler erbringen kann, etwa Rechnungen über die Lieferkette. "
     "[l6]Die Pflicht ist also unverhältnismäßig und verstößt gegen Artikel vierunddreißig. [unm]Darauf kann sich Frau "
     "Trautmann unmittelbar berufen. [vorr]Die Verordnung bleibt insoweit unangewendet, der Anwendungsvorrang aus dem Video "
     "zu Costa gegen Enel.", 0.3),
    ("[k2]Dann prüfe ich eben Ihre Rechnungen.", PS, "Kleinschmidt"),
    # --- I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Geht es um Geld, also um Zölle oder Abgaben gleicher Wirkung, prüfst du Artikel "
     "dreißig, nicht Artikel vierunddreißig. [tf]Und Keck prüfst du nur bei Verkaufsmodalitäten, etwa einem Verbot, unter "
     "dem Einkaufspreis weiterzuverkaufen.", PS),
    # --- J Klausurschema -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema in vier Schritten. [z1]Römisch eins: Schutzbereich, [z1a]eine Ware [z1b]mit grenzüberschreitendem "
     "Bezug. [z2]Römisch zwei: Adressat, eine staatliche Maßnahme. [z3]Römisch drei: Beschränkung, [z3a]mengenmäßig oder "
     "gleicher Wirkung nach Dassonville, [z3b]mit der Grenze Keck. [z4]Römisch vier: Rechtfertigung, [z4a]nach Artikel "
     "sechsunddreißig oder aus zwingenden Erfordernissen, [z4b]jeweils verhältnismäßig.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Jede staatliche Regel, die den Handel zwischen Mitgliedstaaten auch nur potentiell behindern kann, ist "
     "eine Maßnahme gleicher Wirkung. [m2]Und ein Echtheitsnachweis muss für jeden Händler erreichbar sein, auch für "
     "Parallelimporteure.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
