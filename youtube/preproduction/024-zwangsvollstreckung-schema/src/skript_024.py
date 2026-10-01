"""Folge 024 · Zwangsvollstreckung Schema: Titel, Klausel, Zustellung (Fr · 2. Examen · ZV, Format Schema).
Beispielfall frei erfunden: Malermeisterin Köhler hat gegen Herrn Vogel ein rechtskräftiges Urteil des Amtsgerichts über
4.800 Euro (Werklohn). Sie legt dem Gerichtsvollzieher ihre Ausfertigung ohne Vollstreckungsklausel vor; er lehnt ab.
Schema der allgemeinen Vollstreckungsvoraussetzungen: I. Antrag (§ 753 I, § 754a n. F.) → II. zuständiges
Vollstreckungsorgan (§§ 753, 808; §§ 764, 828; § 867; §§ 887–890 ZPO) → III. allgemeine Voraussetzungen: 1. Titel (§ 704,
§§ 708, 709, § 794 ZPO), 2. Klausel (§§ 724, 725 ZPO; Gegenfall Vollstreckungsbescheid § 794 I Nr. 4, § 796 I ZPO),
3. Zustellung (§ 750 I ZPO n. F. seit 1.10.2026, § 317 I ZPO) → IV. besondere Voraussetzungen (§§ 751, 756 ZPO) →
V. keine Vollstreckungshindernisse (§ 775 ZPO) → Pfändung beim Schuldner (§ 808 ZPO), Ausblick Rechtsbehelfe
(§§ 766, 767, 771 ZPO). Belege je Aussage: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache: Köhler, Vogel;
Gerichtsvollzieher und Urkundsbeamtin ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Koehler": "laura_ruhig", "Gerichtsvollzieher": "marc", "Urkundsbeamtin": "hilde", "Vogel": "timo"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall: die Wohnung, das Urteil, beim Gerichtsvollzieher --------------------------------------------------------
    ("[fall]Frau Köhler ist Malermeisterin. [wohnung]Sie streicht die Wohnung von Herrn Vogel, für viertausendachthundert "
     "Euro. [zahlt]Doch Herr Vogel zahlt nicht. [urteil]Frau Köhler klagt und gewinnt: Das Amtsgericht verurteilt ihn zur "
     "Zahlung, das Urteil ist rechtskräftig. [buero]Damit geht sie zum Gerichtsvollzieher.", 0.3),
    ("[k1]Hier ist mein Urteil. Bitte holen Sie mein Geld!", 0.4, "Koehler"),
    ("[g1]Auf Ihrem Urteil fehlt die Vollstreckungsklausel. So darf ich nicht anfangen.", 0.4, "Gerichtsvollzieher"),
    ("[k2]Aber das Urteil ist doch rechtskräftig!", 0.5, "Koehler"),
    ("[frage]Warum legt der Gerichtsvollzieher nicht los? Und was prüft er, bevor er vollstreckt?", 0.6),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Überblick -----------------------------------------------------------------------------------------------------
    ("[ueber]In der Klausur prüfst du die Zwangsvollstreckung nach festem Schema: [ue1]Antrag, [ue2]zuständiges "
     "Vollstreckungsorgan, [ue3]die allgemeinen Voraussetzungen Titel, Klausel und Zustellung, [ue4]besondere "
     "Voraussetzungen [ue5]und keine Vollstreckungshindernisse.", PS),
    # --- D I. Antrag -----------------------------------------------------------------------------------------------------
    ("[antrag]Römisch eins: der Antrag. Der Gerichtsvollzieher vollstreckt im Auftrag der Gläubigerin, Paragraf "
     "siebenhundertdreiundfünfzig Absatz eins. [elektr]Seit Oktober zweitausendsechsundzwanzig gilt: Beim elektronischen "
     "Auftrag wegen einer Geldforderung genügen Titel und Klausel als elektronische Dokumente, Paragraf "
     "siebenhundertvierundfünfzig a. [versich]Die Gläubigerin versichert dann auch, dass die Forderung noch besteht.", PS),
    # --- E II. Vollstreckungsorgan ---------------------------------------------------------------------------------------
    ("[organ]Römisch zwei: das zuständige Vollstreckungsorgan. Es hängt davon ab, worin vollstreckt wird. [sachen]Bewegliche "
     "Sachen pfändet der Gerichtsvollzieher, Paragraf achthundertacht. [ford]Forderungen wie Lohn oder Kontoguthaben pfändet "
     "das Vollstreckungsgericht, Paragraf achthundertachtundzwanzig. [grund]Eine Zwangshypothek trägt das Grundbuchamt ein, "
     "Paragraf achthundertsiebenundsechzig. [handl]Für Handlungen ist das Prozessgericht zuständig, Paragrafen "
     "achthundertsiebenundachtzig folgende. [hier]Frau Köhler will Sachen pfänden lassen: Zuständig ist der Gerichtsvollzieher.", PS),
    # --- F III. 1. Titel -------------------------------------------------------------------------------------------------
    ("[titel]Römisch drei: die allgemeinen Voraussetzungen. Erstens der Titel. [p704]Paragraf siebenhundertvier: Die "
     "Zwangsvollstreckung findet statt aus Endurteilen, die rechtskräftig oder für vorläufig vollstreckbar erklärt sind. "
     "[vorl]Für vorläufig vollstreckbar erklärt das Gericht Urteile bis zwölfhundertfünfzig Euro "
     "ohne Sicherheitsleistung, sonst grundsätzlich nur gegen Sicherheit, Paragrafen siebenhundertacht und siebenhundertneun. [p794]Weitere Titel nennt "
     "Paragraf siebenhundertvierundneunzig, etwa Prozessvergleich, vollstreckbare notarielle Urkunde und Vollstreckungsbescheid. "
     "[titel_ok]Frau Köhler hat ein rechtskräftiges Endurteil. Der Titel liegt vor.", PS),
    # --- G III. 2. Klausel -----------------------------------------------------------------------------------------------
    ("[klausel]Zweitens die Klausel. Daran ist Frau Köhler gescheitert. [p724]Nach Paragraf siebenhundertvierundzwanzig "
     "Absatz eins wird die Zwangsvollstreckung auf Grund einer mit der Vollstreckungsklausel versehenen Ausfertigung des "
     "Urteils durchgeführt, der vollstreckbaren Ausfertigung. [ub]Sie erteilt der Urkundsbeamte der Geschäftsstelle des "
     "Gerichts erster Instanz, hier des Amtsgerichts.", 0.3),
    ("[u1]Vorstehende Ausfertigung wird der Klägerin zum Zwecke der Zwangsvollstreckung erteilt.", 0.4, "Urkundsbeamtin"),
    ("[p725]So lautet die Klausel, Paragraf siebenhundertfünfundzwanzig.", PS),
    # --- H Gegenfall Vollstreckungsbescheid ------------------------------------------------------------------------------
    ("[vb]Anders beim Vollstreckungsbescheid aus dem Mahnverfahren, einem Titel nach Paragraf "
     "siebenhundertvierundneunzig Absatz eins Nummer vier. [p796]Er braucht eine Klausel nur, wenn für oder gegen andere "
     "Personen vollstreckt wird als die im Bescheid genannten, Paragraf siebenhundertsechsundneunzig Absatz eins.", PS),
    # --- I III. 3. Zustellung ----------------------------------------------------------------------------------------------
    ("[zust]Drittens die Zustellung. Paragraf siebenhundertfünfzig ist seit dem ersten Oktober zweitausendsechsundzwanzig "
     "neu gefasst. [p750]Nach Absatz eins darf die Vollstreckung nur beginnen, wenn die Personen im Urteil oder in der Klausel "
     "namentlich bezeichnet sind [p750b]und dem Schuldner das Urteil zugestellt ist oder gleichzeitig zugestellt wird. "
     "[zust_ok]Das Urteil wurde Herrn Vogel schon von "
     "Amts wegen zugestellt, Paragraf dreihundertsiebzehn. Auch das liegt vor.", PS),
    # --- J IV. besondere Voraussetzungen -------------------------------------------------------------------------------------
    ("[bes]Römisch vier: besondere Voraussetzungen. [p751]Hängt der Anspruch von einem Kalendertag ab, muss der Tag "
     "abgelaufen sein. [sicher]Muss die Gläubigerin Sicherheit leisten, weist sie das durch Urkunde nach, "
     "Paragraf siebenhunderteinundfünfzig. [p756]Bei Leistung Zug um Zug bietet der Gerichtsvollzieher die Gegenleistung "
     "grundsätzlich zuerst an, Paragraf siebenhundertsechsundfünfzig. [bes_ok]Bei Frau Köhler greift nichts davon: Ihr Urteil "
     "ist rechtskräftig und unbedingt.", PS),
    # --- K V. keine Vollstreckungshindernisse ------------------------------------------------------------------------------
    ("[hind]Römisch fünf: keine Vollstreckungshindernisse. [p775]Nach Paragraf siebenhundertfünfundsiebzig wird die "
     "Vollstreckung etwa eingestellt, wenn eine Entscheidung vorgelegt wird, die das Urteil aufhebt, [quitt]oder eine "
     "Quittung der Gläubigerin, dass sie nach dem Urteil befriedigt ist. [hind_ok]Herr Vogel kann nichts davon vorlegen.", PS),
    # --- L Pfändung bei Herrn Vogel -----------------------------------------------------------------------------------------
    ("[auftrag]Mit der vollstreckbaren Ausfertigung erteilt Frau Köhler den Auftrag. [pfand]Der Gerichtsvollzieher pfändet "
     "bei Herrn Vogel ein Gemälde, Paragraf achthundertacht.", 0.3),
    ("[g2]Dieses Gemälde ist gepfändet. Hier ist das Siegel.", 0.4, "Gerichtsvollzieher"),
    ("[v1]Das Gemälde gehört doch meiner Schwester!", 0.5, "Vogel"),
    # --- M Ausblick Rechtsbehelfe ------------------------------------------------------------------------------------------
    ("[rb]Ausblick auf die Rechtsbehelfe: [rb771]Behauptet ein Dritter ein Recht, das die Veräußerung hindert, hilft "
     "ihm die Drittwiderspruchsklage, Paragraf siebenhunderteinundsiebzig. [rb767]Einwendungen gegen den Anspruch selbst, "
     "etwa eine spätere Zahlung, gehören in die Vollstreckungsabwehrklage, Paragraf siebenhundertsiebenundsechzig. "
     "[rb766]Verfahrensfehler, etwa eine fehlende Klausel, rügt der Schuldner mit der Erinnerung, Paragraf "
     "siebenhundertsechsundsechzig.", PS),
    # --- N Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Lies bei der Zustellung genau den Wortlaut. Zugestellt sein muss das Urteil. [tipp2]Die einfache "
     "Klausel musst du nicht zustellen. [tipp3]Das verlangt Paragraf siebenhundertfünfzig nur in Sonderfällen, etwa bei "
     "Rechtsnachfolge.", PS),
    # --- O Klausurschema -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s1]Römisch eins: Antrag. [s2]Römisch zwei: zuständiges Vollstreckungsorgan. [s3]Römisch "
     "drei: allgemeine Vollstreckungsvoraussetzungen, [s3a]erstens Titel, [s3b]zweitens Klausel, [s3c]drittens Zustellung. "
     "[s4]Römisch vier: besondere Vollstreckungsvoraussetzungen. [s5]Römisch fünf: keine Vollstreckungshindernisse.", PS),
    # --- P Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein Urteil allein reicht nicht. Vollstreckt wird in der Regel erst mit Titel, Klausel und Zustellung, "
     "[m2]und zwar durch das Organ, das für den Gegenstand zuständig ist.", 1.4),
]
