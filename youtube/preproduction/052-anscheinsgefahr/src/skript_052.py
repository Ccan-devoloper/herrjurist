"""Folge 052 · Anscheinsgefahr: Hilfeschrei aus dem Fernseher – Polizeirecht erklärt (Mo · Der Fall · Polizei- und
Ordnungsrecht). Übungsfall nach dem Hook des Themenplans, Beispielland Nordrhein-Westfalen (PolG NRW, OBG NRW):
Sonntagabend, kurz vor elf. Nachbarin Frau Jäger hört aus der Wohnung von Herrn Böttcher (lebt allein) eine Frau um Hilfe
schreien und ruft die Polizei. Polizist Ahrens klingelt, klopft und ruft, niemand öffnet, es schreit weiter. Ein
Schlüsseldienst bricht das Schloss auf; drinnen läuft nur ein Krimi in voller Lautstärke. Das Polizeipräsidium verlangt
250 Euro für den Schlüsseldienst, das Schloss ist kaputt.
Primärebene (ex ante): § 41 I 1 Nr. 4, II PolG NRW (Standardbefugnis vor § 8 I), Art. 13 VII GG, formell § 1 I PolG NRW,
Gefahrbegriff (§ 8 I PolG NRW; konkrete und gegenwärtige Gefahr), Anscheinsgefahr, Abgrenzung Putativgefahr und
Gefahrenverdacht, Verhältnismäßigkeit, Ersatzvornahme im sofortigen Vollzug (§§ 50 II, 52 PolG NRW).
Sekundärebene (ex post): Kosten (§ 52 I PolG NRW; OVG NRW 5 A 95/00), Entschädigung (§ 67 PolG NRW i. V. m. § 39 I a,
§ 40 IV OBG NRW), Gegenfall OLG Köln 7 U 146/94 (Zeitschaltuhr, Entschädigung mit zwei Dritteln Mitverschulden).
Wortlautkarten: § 41 I 1 Nr. 4 PolG NRW, Art. 13 VII GG, § 8 I PolG NRW, § 39 I OBG NRW.
Fiktive Figuren: Frau Jäger (sabrina), Polizist Ahrens (niklas), Herr Böttcher (helmut).
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Jaeger": "sabrina", "Ahrens": "niklas", "Boettcher": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Sonntagabend im Mietshaus ---------------------------------------------------------------------------
    ("[fall]Sonntagabend, kurz vor elf, in einem Mietshaus. [schrei]Frau Jäger hört durch die Wand Schreie aus der Wohnung "
     "nebenan. [schrei2]Dort wohnt Herr Böttcher. Eine Frau ruft um Hilfe, dann ist es still, dann wieder Schreie.", 0.2),
    ("[ja1]Polizei? Bei meinem Nachbarn schreit eine Frau um Hilfe! Er wohnt allein. Bitte kommen Sie schnell!", 0.3, "Jaeger"),
    ("[polizei]Wenige Minuten später ist Polizist Ahrens da. [klingel]Er klingelt, klopft und ruft. Niemand öffnet. "
     "Hinter der Tür schreit es weiter.", 0.2),
    ("[ah1]Wir können nicht warten. Da drin ist vielleicht jemand in Lebensgefahr.", 0.3, "Ahrens"),
    ("[tuer]Ein Schlüsseldienst bricht das Schloss auf. [drin]Drinnen sitzt Herr Böttcher allein vor dem Fernseher. "
     "Ein Krimi läuft, in voller Lautstärke.", 0.2),
    ("[bo1]Was ist denn hier los? Ich schaue doch nur meinen Krimi!", 0.3, "Boettcher"),
    ("[bescheid]Wochen später verlangt das Polizeipräsidium zweihundertfünfzig Euro für den Schlüsseldienst. [schloss]Und "
     "das Schloss ist kaputt.", 0.3),
    ("[bo2]Ich soll zahlen? Ich habe doch nur ferngesehen!", 0.3, "Boettcher"),
    # --- B Die Frage --------------------------------------------------------------------------------------------------
    ("[frage]Durfte die Polizei in die Wohnung, obwohl nur ein Krimi lief? [frage2]Und wer trägt am Ende die Kosten?", 0.6),
    # --- C Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Landesrecht und zwei Ebenen ----------------------------------------------------------------------------------
    ("[land]Polizeirecht ist Landesrecht. Wir nehmen Nordrhein-Westfalen als Beispiel. Die anderen Länder haben eigene, "
     "ähnliche Regeln, oft unter anderer Nummer. [ebenen]Geprüft wird auf zwei Ebenen: [prim]erst, ob das Betreten "
     "rechtmäßig war, [sek]dann, wer am Ende zahlt.", P),
    # --- E Ermächtigungsgrundlage: Wortlaut § 41 PolG NRW ----------------------------------------------------------------
    ("[egl]Ermächtigungsgrundlage ist nicht die Generalklausel, Paragraf acht, sondern die speziellere Standardbefugnis, "
     "Paragraf einundvierzig Polizeigesetz. [wl41]Danach kann die Polizei eine Wohnung ohne Einwilligung des Inhabers "
     "betreten, wenn das zur Abwehr einer gegenwärtigen Gefahr für Leib, Leben oder Freiheit einer Person erforderlich "
     "ist. [nacht]Nach Absatz zwei gilt das auch nachts.", P),
    # --- F Art. 13 GG und formell ------------------------------------------------------------------------------------------
    ("[art13]Das Betreten greift in die Unverletzlichkeit der Wohnung ein, Artikel dreizehn Grundgesetz. [wl13]Absatz sieben "
     "erlaubt solche Eingriffe zur Abwehr einer Lebensgefahr, auf Grund eines Gesetzes auch zur Verhütung dringender "
     "Gefahren. [formell]Formell ist die Polizei für die Gefahrenabwehr zuständig, Paragraf eins.", P),
    # --- G Gefahrbegriff: Wortlaut § 8 PolG NRW ----------------------------------------------------------------------------
    ("[gefahr]Materiell braucht es eine Gefahr. [wl8]Paragraf acht spricht von einer im einzelnen Falle bestehenden, "
     "konkreten Gefahr für die öffentliche Sicherheit oder Ordnung. [wahrsch]Sie liegt vor, wenn in absehbarer Zeit ein Schaden "
     "mit hinreichender Wahrscheinlichkeit droht. Je größer der Schaden, desto geringer die Anforderungen an die "
     "Wahrscheinlichkeit. [gegenw]Gegenwärtig ist die Gefahr, wenn die Schädigung schon begonnen hat oder mit an Sicherheit "
     "grenzender Wahrscheinlichkeit unmittelbar bevorsteht.", P),
    # --- H Anscheinsgefahr ---------------------------------------------------------------------------------------------------
    ("[problem]Aber hier gab es gar keine Gefahr, nur einen Krimi. [exante]Entscheidend ist die Sicht im Moment des "
     "Einschreitens, ex ante. [anschein]Deuten objektive Tatsachen für einen verständigen, besonnenen Beamten auf eine "
     "Gefahr hin, liegt eine Anscheinsgefahr vor. Sie ist eine echte Gefahr. [subs]Hilfeschreie einer Frau bei einem Mann, "
     "der allein wohnt, und niemand öffnet: Das durfte Ahrens für Lebensgefahr halten.", P),
    # --- I Abgrenzung: Putativgefahr und Gefahrenverdacht ---------------------------------------------------------------------
    ("[schein]Anders die Putativgefahr, auch Scheingefahr genannt: Der Beamte nimmt eine Gefahr an, ohne dass hinreichende "
     "Anhaltspunkte bestehen. [schein2]Hätte man durch die Tür klar Filmmusik und Werbung gehört, wäre die Gefahr nur "
     "eingebildet und das Hineingehen rechtswidrig. [verdacht]Beim Gefahrenverdacht hält die Polizei eine Gefahr für möglich, ist sich aber nicht "
     "sicher. Dann darf sie die Maßnahmen treffen, die zur Aufklärung nötig sind.", P),
    # --- J Verhältnismäßigkeit, Vollzug, Ergebnis Primärebene -------------------------------------------------------------------
    ("[verh]Verhältnismäßig war es auch: Ahrens hat erst geklingelt, geklopft und gerufen. [vollzug]Das Schloss öffnen zu "
     "lassen, war eine Ersatzvornahme im sofortigen Vollzug, Paragrafen fünfzig und zweiundfünfzig. [erg1]Ergebnis der "
     "ersten Ebene: Das Betreten war rechtmäßig.", PS),
    # --- K Sekundärebene: Kosten -----------------------------------------------------------------------------------------------
    ("[ebene2]Jetzt die zweite Ebene. Hier wechselt der Blick: [expost]Für Kosten und Entschädigung zählt, wie es wirklich "
     "war, ex post. [kosten]Die Ersatzvornahme geht nach Paragraf zweiundfünfzig auf Kosten der betroffenen Person. "
     "[zurech]Ein Anscheinsstörer zahlt aber nur, wenn er die Umstände, die den Anschein begründet haben, selbst zu "
     "verantworten hat.", P),
    ("[bo_subs]Herr Böttcher hat den Krimi so laut gestellt, dass die Nachbarin Hilfeschreie hörte und er selbst weder "
     "Klingel noch Polizei. [zahlt]Das liegt in seinem Verantwortungsbereich. Vieles spricht also dafür, dass er die "
     "zweihundertfünfzig Euro zahlen muss.", P),
    # --- L Sekundärebene: Entschädigung, Wortlaut § 39 OBG NRW ---------------------------------------------------------------
    ("[entsch]Und das kaputte Schloss? [wl39]Paragraf siebenundsechzig Polizeigesetz verweist auf das "
     "Ordnungsbehördengesetz. Danach ist ein Schaden zu ersetzen, wenn er infolge einer Inanspruchnahme als Nichtstörer "
     "oder durch rechtswidrige Maßnahmen entstanden ist. [rechtm]Rechtswidrig war hier nichts. [analog]Aber ein "
     "Anscheinsstörer, der den Anschein nicht zu verantworten hat, wird wie ein Nichtstörer entschädigt. [bo_ent]Herr "
     "Böttcher hat ihn zu verantworten. Dann geht er leer aus.", P),
    # --- M Gegenfall: OLG Köln, Zeitschaltuhr ------------------------------------------------------------------------------------
    ("[gegen]Anders ein echter Fall des Oberlandesgerichts Köln: Eine Familie ist im Urlaub, eine Zeitschaltuhr schaltet "
     "abends den Fernseher ein. [gegen2]Nachbarn vermuten einen Einbrecher, die Polizei bricht die Tür auf. [olg]Das Gericht "
     "sprach Entschädigung zu. Die Zeitschaltuhr war nur eine mittelbare Ursache. [mitv]Aber der Mann hätte seine "
     "Nachbarn einweihen müssen. Wegen Mitverschuldens bekam er nur ein Drittel.", PS),
    # --- N Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne die Ebenen. [tipp1]Die Rechtmäßigkeit prüfst du ex ante, Kosten und Entschädigung ex post. "
     "[tipp2]Die Standardbefugnis geht der Generalklausel vor. [tipp3]Und über die Entschädigung entscheiden die "
     "ordentlichen Gerichte, Paragraf dreiundvierzig Ordnungsbehördengesetz.", PS),
    # --- O Klausurschema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [q1]A, Primärebene: Rechtmäßigkeit des Betretens. [q2]Eins, Ermächtigungsgrundlage, "
     "Paragraf einundvierzig. [q3]Zwei, formell: Zuständigkeit. [q4]Drei, materiell: gegenwärtige Gefahr, Anscheinsgefahr "
     "genügt, Putativgefahr nicht. [q5]Dann Ermessen und Verhältnismäßigkeit. [q6]B, Sekundärebene: Kosten nur bei "
     "zu verantwortendem Anschein. [q7]Entschädigung wie ein Nichtstörer, gemindert bei Mitverschulden.", PS),
    # --- P Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Über die Maßnahme entscheidet der Anschein, über die Kosten die Wirklichkeit. [m2]Wer den Anschein "
     "nicht zu verantworten hat, zahlt nicht und wird wie ein Nichtstörer entschädigt.", 1.4),
]
