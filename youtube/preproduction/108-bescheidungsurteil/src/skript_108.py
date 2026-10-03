"""Folge 108 · Bescheidungsurteil oder Verpflichtungsurteil? Spruchreife erklärt (Fr · 2. Examen · VwGO-Praxis, Format Schema).
Übungsfall nach dem Hook des Themenplans („Ein Wirt klagt auf eine Sondernutzungserlaubnis für seine Terrasse, über die die
Stadt nach Ermessen entscheidet“), Beispielland Brandenburg (Ermessen ausdrücklich in § 18 II 3 BbgStrG; Vorverfahren findet
statt; Behördenprinzip § 8 II BbgVwGG), bewusst anders als 074/093 (NRW, Café/Gehweg): Herr Haberland führt das Gasthaus am
Marktplatz und beantragt acht Tische auf dem Platz. Frau Seeger von der Stadt lehnt ab, um die anderen Wirte vor Konkurrenz
zu schützen (sachfremd); der Widerspruch bleibt erfolglos. Er klagt auf Erteilung (Verpflichtungsantrag). Die Richterin:
Konkurrenzschutz ist kein straßenbezogener Grund, Markttage und Wege muss die Stadt noch abwägen → nicht spruchreif.
Kern (Urteils- und Antragsseite): § 88 VwGO (Wortlautkarte), Bescheidung als Minus (BVerwG 6 B 22.22 Rn. 19 f.), Tenor beider
Varianten nach § 113 V VwGO (Wortlautkarte), Kosten § 155 I 1 VwGO (Wortlautkarte), Klausurtipp mit Kostenvergleich (Lexi),
vorläufige Vollstreckbarkeit ein Satz (Verweis Video Anfechtungsurteil), vollständiger Tenor, Schema, Merksatz (Lexi).
Spruchreife nur kurz mit Verweis auf das Video zur Verpflichtungsklage (Folge 093).
Fiktive Figuren: Herr Haberland (stephan), Frau Seeger (hilde), die Richterin (lucy). christian nicht verwendet.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Haberland": "stephan", "Seeger": "hilde", "Richterin": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Gasthaus am Marktplatz, Antrag, Ablehnung --------------------------------------------------------------
    ("[fall]Herr Haberland führt das Gasthaus am Marktplatz einer Stadt in Brandenburg. [antrag]Er beantragt eine "
     "Sondernutzungserlaubnis: acht Tische auf dem Platz, von Mai bis September. [seeger]Frau Seeger von der Stadt "
     "bringt die Antwort.", 0.2),
    ("[se1]Am Markt gibt es schon zwei Terrassen. Wir schützen die anderen Wirte vor Konkurrenz. Abgelehnt.", 0.3, "Seeger"),
    ("[wsp]Auch sein Widerspruch bleibt erfolglos.", 0.2),
    ("[ha1]Dann klage ich. Die Stadt muss mir die Erlaubnis erteilen!", 0.3, "Haberland"),
    # --- B Gericht: Feststellung, Frage -----------------------------------------------------------------------------------
    ("[klage]Er erhebt Verpflichtungsklage und beantragt genau das. [gericht]Im Prozess stellt die Richterin fest:", 0.2),
    ("[ri1]Konkurrenzschutz hat mit der Straße nichts zu tun. Über Markttage und Wege muss die Stadt aber noch selbst "
     "entscheiden.", 0.3, "Richterin"),
    ("[frage]Bekommt Herr Haberland ein Verpflichtungsurteil oder nur ein Bescheidungsurteil? [frage2]Und was bedeutet "
     "das für die Kosten?", 0.6),
    # --- C Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Spruchreife kurz (Verweis Video Verpflichtungsklage) --------------------------------------------------------------
    ("[spr]Kurz zur Spruchreife. Über die Erlaubnis ist nach pflichtgemäßem Ermessen zu entscheiden, Paragraf achtzehn "
     "Absatz zwei Brandenburgisches Straßengesetz. [sach]Konkurrenzschutz hat keinen Bezug zur Straße, die Ablehnung ist "
     "ermessensfehlerhaft. [null]Spruchreif wäre die Sache aber nur bei einer Ermessensreduzierung auf null. Hier bleiben "
     "Markttage und Wege abzuwägen. [verweis]Wie man das prüft, zeigt unser Video zur Verpflichtungsklage.", P),
    # --- E 1. Antrag: § 88 VwGO --------------------------------------------------------------------------------------------
    ("[wl88]Erstens, der Antrag. Paragraf achtundachtzig: Das Gericht darf über das Klagebegehren nicht hinausgehen, ist "
     "aber an die Fassung der Anträge nicht gebunden. [ziel]Maßgeblich ist das wirkliche Rechtsschutzziel. [minus]Und ein "
     "Verpflichtungsantrag enthält regelmäßig als Minus den Antrag auf Bescheidung. [hilfs]Ein ausdrücklicher Hilfsantrag "
     "auf Neubescheidung ist deshalb nicht nötig. [mehr]Mehr als beantragt gibt es aber nie, etwa zehn statt acht Tische.", P),
    # --- F 2. Tenor: § 113 V VwGO, Verpflichtungsurteil -----------------------------------------------------------------------
    ("[wl113]Zweitens, der Tenor. Paragraf hundertdreizehn Absatz fünf: Soweit die Ablehnung oder Unterlassung des "
     "Verwaltungsakts rechtswidrig und der Kläger dadurch in seinen Rechten verletzt ist, spricht das Gericht die "
     "Verpflichtung der Verwaltungsbehörde aus, die beantragte Amtshandlung vorzunehmen, wenn die Sache spruchreif ist. "
     "[satz2]Andernfalls spricht es die Verpflichtung aus, den Kläger unter Beachtung der Rechtsauffassung des Gerichts "
     "zu bescheiden.", P),
    ("[bekl]Vorweg: In Brandenburg richtet sich die Klage gegen die Behörde selbst, Paragraf acht Absatz zwei "
     "Verwaltungsgerichtsgesetz, hier also gegen den Bürgermeister. [vu]Wäre die Sache spruchreif, hieße es: Der Bescheid "
     "des Beklagten vom zehnten März zweitausendsechsundzwanzig in Gestalt des Widerspruchsbescheids vom fünften Mai "
     "zweitausendsechsundzwanzig wird aufgehoben. [vu2]Der Beklagte wird verpflichtet, dem Kläger die beantragte "
     "Sondernutzungserlaubnis zu erteilen. [klar]Die Aufhebung spricht das Gericht üblicherweise zur Klarstellung mit aus.", P),
    # --- G Bescheidungsurteil -----------------------------------------------------------------------------------------------
    ("[bu]Hier fehlt die Spruchreife. Der erste Satz bleibt, dann folgt: [bu2]Der Beklagte wird verpflichtet, über den "
     "Antrag des Klägers vom zweiten Februar zweitausendsechsundzwanzig unter Beachtung der Rechtsauffassung des Gerichts "
     "erneut zu entscheiden. [ueb]Und weil Herr Haberland die Erlaubnis selbst verlangt hat: Im Übrigen wird die Klage "
     "abgewiesen.", P),
    # --- H 3. Kosten: § 155 I 1 VwGO ----------------------------------------------------------------------------------------
    ("[kosten]Drittens, die Kosten. Paragraf hundertfünfundfünfzig Absatz eins Satz eins: Wenn ein Beteiligter teils "
     "obsiegt, teils unterliegt, so sind die Kosten gegeneinander aufzuheben oder verhältnismäßig zu teilen. [teil]Wer die "
     "Erlaubnis verlangt und nur die Bescheidung bekommt, unterliegt teilweise. [quote]Eine feste Quote nennt das Gesetz "
     "nicht. Häufig teilen die Gerichte hälftig: [t3]Die Kosten des Verfahrens tragen der Kläger und der Beklagte je zur "
     "Hälfte.", P),
    # --- I Klausurtipp mit Kostenvergleich (Lexi) -----------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Ist das Ermessen nicht auf null reduziert, beantrage von Anfang an nur die Bescheidung. "
     "[rech]Angenommen, das Verfahren kostet insgesamt dreitausend Euro. Mit dem Verpflichtungsantrag trägt Herr Haberland "
     "die Hälfte, also tausendfünfhundert Euro. [rech2]Mit dem Bescheidungsantrag gewinnt er ganz, und der Beklagte trägt "
     "alle Kosten, Paragraf hundertvierundfünfzig Absatz eins. [rech3]Das gilt, soweit das Gericht seiner Rechtsauffassung "
     "folgt.", PS),
    # --- J 4. Vorläufige Vollstreckbarkeit (ein Satz) ---------------------------------------------------------------------------
    ("[vollstr]Viertens: Vorläufig vollstreckbar ist das Urteil nur wegen der Kosten, Paragraf hundertsiebenundsechzig "
     "Absatz zwei. Die Formel kennst du aus dem Video zum Anfechtungsurteil.", P),
    # --- K Vollständiger Tenor --------------------------------------------------------------------------------------------
    ("[voll]Hier ist der vollständige Tenor zum Mitschreiben.", 5.0),
    # --- L Schema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema. [s1]Erstens, der Antrag: das Klagebegehren nach Paragraf achtundachtzig, die Bescheidung steckt "
     "als Minus darin. [s2]Zweitens, der Tenor: Aufhebung, dann Verpflichtung zum Erlass, wenn die Sache spruchreif ist, "
     "[s2b]sonst Verpflichtung zur Neubescheidung, [s2c]und im Übrigen Klageabweisung. [s3]Drittens, die Kosten nach "
     "Paragraf hundertvierundfünfzig oder hundertfünfundfünfzig. [s4]Viertens, die vorläufige Vollstreckbarkeit wegen der "
     "Kosten.", PS),
    # --- M Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Fehlt die Spruchreife, ergeht nur ein Bescheidungsurteil. [m2]Wer trotzdem die Verpflichtung "
     "beantragt, unterliegt teilweise und trägt anteilig die Kosten.", 1.4),
]
