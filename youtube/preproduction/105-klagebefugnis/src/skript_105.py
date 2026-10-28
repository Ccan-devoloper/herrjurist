"""Folge 105 · Klagebefugnis § 42 II VwGO: Möglichkeitstheorie und Adressatentheorie (Fr · Klausurpraxis · Schema).
Übungsfall nach dem Hook des Themenplans („Du bekommst einen Gebührenbescheid – dein Freund will aus Solidarität
mitklagen“): Frau Nolte will die kranke Kastanie in ihrem Garten fällen lassen; die Stadt erteilt die Fällgenehmigung und
setzt mit Gebührenbescheid an Frau Nolte eine Verwaltungsgebühr von 180 € fest. Ihr Freund Herr Wilke wohnt in derselben
Stadt, findet solche Gebühren ungerecht und klagt aus Solidarität mit. Länderneutral (kein Landesrecht nötig).
Schema der Klagebefugnis: 1. Wortlaut § 42 II (Wortlautkarte), „soweit gesetzlich nichts anderes bestimmt ist“
(§ 2 I 1 UmwRG, ein Satz); 2. eigene Rechte; 3. Möglichkeitstheorie (BVerwG 6 C 2.23 Rn. 13; 4 C 3.20 Rn. 9);
4. Adressatentheorie (BVerwG 6 B 20.10 Rn. 16; 9 B 4.19 Rn. 18), Wortlautkarte Art. 2 I GG; 5. Dritte: Schutznormtheorie
(BVerwG 6 C 2.23 Rn. 24; Verweis 088/090); 6. Zweck: keine Popularklage (Lehrbegriff, ohne Az.) – Herr Wilke nicht
klagebefugt (vgl. 6 C 2.23 Rn. 14), seine Klage unzulässig. Klausurtipp (ein Satz; Verpflichtungsklage: möglicher Anspruch,
Verweis 093), Schema, Merksatz (Lexi).
Fiktive Figuren: Frau Nolte (sabrina), Herr Wilke (marc), die Richterin (laura_ruhig). Namen nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Nolte": "sabrina", "Wilke": "marc", "Richterin": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: der Garten, die Kastanie, der Gebührenbescheid --------------------------------------------------------
    ("[fall]Frau Nolte will die kranke Kastanie in ihrem Garten fällen lassen. [erlaubt]Die Stadt erlaubt es ihr. "
     "[bescheid]Dann kommt ein Gebührenbescheid: hundertachtzig Euro für die Genehmigung. [wilke]Ihr Freund Herr Wilke "
     "ist gerade zu Besuch.", 0.2),
    ("[no1]Hundertachtzig Euro für einen Stempel? Dagegen klage ich.", 0.3, "Nolte"),
    ("[wi1]Ich klage mit! Ich wohne auch in dieser Stadt, und solche Gebühren sind einfach ungerecht.", 0.3, "Wilke"),
    ("[klage]Beide erheben Anfechtungsklage gegen den Gebührenbescheid. [frage]Sind beide klagebefugt? [frage2]Die "
     "Antwort steht in Paragraf zweiundvierzig Absatz zwei.", 0.6),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Einordnung, 1. Wortlaut § 42 II ------------------------------------------------------------------------------
    ("[einord]Die Klagebefugnis prüfst du in der Zulässigkeit, gleich nach der statthaften Klageart. Das ganze Schema zeigt "
     "unser Video zur Anfechtungsklage. [wl422]Erstens, der Wortlaut. Paragraf zweiundvierzig Absatz zwei: Soweit "
     "gesetzlich nichts anderes bestimmt ist, ist die Klage nur zulässig, wenn der Kläger geltend macht, durch den "
     "Verwaltungsakt oder seine Ablehnung oder Unterlassung in seinen Rechten verletzt zu sein. [umw]Etwas anderes bestimmt "
     "etwa das Umwelt-Rechtsbehelfsgesetz: Anerkannte Umweltvereinigungen können gegen bestimmte Entscheidungen klagen, ohne eine Verletzung in eigenen "
     "Rechten geltend machen zu müssen.", P),
    # --- D 2. Eigene Rechte ---------------------------------------------------------------------------------------------
    ("[eigen]Zweitens, der Kläger muss eine Verletzung in seinen eigenen Rechten geltend machen. [eigen2]Gemeint sind "
     "subjektive Rechte, also Rechte, die ihm selbst zustehen. [objektiv]Dass ein Bescheid nur objektiv rechtswidrig sein "
     "könnte, genügt nicht.", P),
    # --- E 3. Möglichkeitstheorie ---------------------------------------------------------------------------------------
    ("[mt]Drittens, wie sicher muss die Verletzung sein? Nach der Möglichkeitstheorie genügt, dass sie auf der Grundlage "
     "des Klagevorbringens möglich erscheint. [mt2]Auszuschließen ist sie nur, wenn offensichtlich und nach keiner "
     "Betrachtungsweise subjektive Rechte des Klägers verletzt sein können. [mt3]Ob er wirklich verletzt ist, prüfst du "
     "erst in der Begründetheit.", P),
    # --- F 4. Adressatentheorie, Wortlaut Art. 2 I GG -------------------------------------------------------------------
    ("[adr]Viertens, die Adressatentheorie. Frau Nolte ist Adressatin des Gebührenbescheids. Er verpflichtet sie, "
     "hundertachtzig Euro zu zahlen. [wl2]Damit greift er jedenfalls in ihre allgemeine Handlungsfreiheit ein, Artikel zwei "
     "Absatz eins Grundgesetz: Jeder hat das Recht auf die freie Entfaltung seiner Persönlichkeit. [stets]Das "
     "Bundesverwaltungsgericht sagt: Weil der Adressat eines belastenden Verwaltungsakts stets einem staatlichen "
     "Freiheitseingriff unterliegt, ist er allein deshalb klagebefugt. [nolte]Frau Nolte ist also klagebefugt.", P),
    # --- G 5. Dritte: Schutznormtheorie ---------------------------------------------------------------------------------
    ("[dritt]Fünftens, Dritte. Wer nicht Adressat ist, braucht eine Norm, die zumindest auch ihn schützt und nicht nur "
     "reflexartig seine Interessen berührt. [snt]Das ist die Schutznormtheorie. [nachbar]Typisch ist der Nachbar, der eine "
     "Baugenehmigung angreift. Mehr dazu in unseren Videos zum Rücksichtnahmegebot und zur Drittanfechtung.", P),
    # --- H 6. Zweck: keine Popularklage; Herr Wilke ---------------------------------------------------------------------
    ("[zweck]Sechstens, der Zweck: Paragraf zweiundvierzig Absatz zwei schließt die Popularklage aus. [zweck2]Niemand soll "
     "fremde Rechte oder das Allgemeininteresse vor Gericht bringen. [wilke2]Und Herr Wilke? Der Bescheid richtet sich nicht "
     "an ihn und verpflichtet ihn zu nichts. [wilke3]Eine Norm, die ihn hier schützt, ist nicht ersichtlich. Dass er in derselben "
     "Stadt wohnt und die Gebühr ungerecht findet, ist kein eigenes Recht. [urteil]Das Verwaltungsgericht entscheidet:", 0.2),
    ("[ri1]Herr Wilke, Sie sind nicht klagebefugt. Ihre Klage ist unzulässig.", 0.6, "Richterin"),
    # --- I Klausurtipp (Lexi) -------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Klagt der Adressat gegen einen belastenden Bescheid, schreibst du zur Klagebefugnis nur einen Satz. "
     "[tipp2]Etwa: Als Adressatin eines belastenden Verwaltungsakts ist Frau Nolte möglicherweise in ihrem Recht aus "
     "Artikel zwei Absatz eins Grundgesetz verletzt und daher klagebefugt. [tipp3]Mehr gehört da nicht hin. [vk]Bei der "
     "Verpflichtungsklage fragst du dagegen, ob ein Anspruch auf den Verwaltungsakt möglich ist. Das zeigt unser Video zur "
     "Verpflichtungsklage.", PS),
    # --- J Schema -------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema zur Klagebefugnis. [s1]Eins, der Wortlaut: Paragraf zweiundvierzig Absatz zwei, soweit gesetzlich "
     "nichts anderes bestimmt ist. [s2]Zwei, eine Verletzung in eigenen Rechten geltend machen. [s3]Drei, die "
     "Möglichkeitstheorie: nicht offensichtlich ausgeschlossen. [s4]Vier, der Adressat eines belastenden Verwaltungsakts: "
     "Artikel zwei Absatz eins. [s5]Fünf, Dritte: eine drittschützende Norm. [s6]Sechs, keine Popularklage.", PS),
    # --- K Merksatz (Lexi) ----------------------------------------------------------------------------------------------
    ("[merke]Merke: Klagebefugt ist, wer möglicherweise in eigenen Rechten verletzt ist. [m2]Der Adressat eines "
     "belastenden Bescheids ist es immer. Wer nur aus Solidarität klagt, ist es nie.", 1.4),
]
