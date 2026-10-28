"""Folge 102 · Anfechtungsurteil Tenor: „in Gestalt des Widerspruchsbescheids“ (Fr · 2. Examen · VwGO-Praxis, Format
Formulierung). Übungsfall nach dem Hook des Themenplans („Ein Gebührenbescheid über 2.400 Euro ist nur in Höhe von
900 Euro rechtswidrig“), Beispielland Nordrhein-Westfalen (dort Vorverfahren bei Kommunalabgaben, § 110 II 1 Nr. 6 JustG NRW):
Frau Rehbein betreibt eine Wäscherei im eigenen Haus. Die Stadt setzt die Abwassergebühr auf 2.400 € fest (Satzung: 6 € je m³,
die Stadt rechnet mit 400 m³); der Zähler zeigt 250 m³. Herr Zimmermann von der Stadt weist den Widerspruch zurück. Frau
Rehbein klagt auf Aufhebung des ganzen Bescheids; das Gericht stellt 250 m³ fest: rechtmäßig 1.500 €, rechtswidrig 900 €.
Tenor progressiv: § 79 I Nr. 1 VwGO (Wortlautkarte) → „Bescheid … in Gestalt des Widerspruchsbescheids …“, § 79 I Nr. 2, II ein
Satz; § 113 I 1 VwGO (Wortlautkarte) „soweit“, Teilbarkeit (BVerwG 9 B 18.23 Rn. 7) → „… aufgehoben, soweit darin eine Gebühr von
mehr als 1.500 Euro festgesetzt wird. Im Übrigen wird die Klage abgewiesen.“; Klausurtipp § 113 II (Lexi); Kosten § 155 I 1
(5/8 zu 3/8); vorläufige Vollstreckbarkeit § 167 II, I 1 VwGO i. V. m. §§ 708 Nr. 11, 711 ZPO; Berufung § 124a I 1, 3 VwGO;
vollständiger Tenor; Schema; Merksatz (Lexi). Tenorformeln als Klausurkonvention (Belege in RECHTSSTAND.md).
Fiktive Figuren: Frau Rehbein (hilde), Herr Zimmermann (christian), der Richter (stephan) – stephan und christian nie in
derselben Szene. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Rehbein": "hilde", "Zimmermann": "christian", "Richter": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Wäscherei, der Bescheid, der Widerspruch ----------------------------------------------------------
    ("[fall]Frau Rehbein betreibt eine kleine Wäscherei im eigenen Haus. [bescheid]Die Stadt schickt ihr einen "
     "Gebührenbescheid: Abwassergebühr, zweitausendvierhundert Euro. [rechnung]Die Satzung verlangt sechs Euro je "
     "Kubikmeter, die Stadt rechnet mit vierhundert. [zaehler]Der Zähler zeigt aber nur zweihundertfünfzig. "
     "[widerspr]Frau Rehbein legt Widerspruch ein. [zimmer]Herr Zimmermann von der Stadt bringt den Widerspruchsbescheid.", 0.2),
    ("[zi1]Frau Rehbein, wir bleiben bei vierhundert Kubikmetern. Ihr Widerspruch wird zurückgewiesen.", 0.3, "Zimmermann"),
    ("[re1]Dann klage ich. Der ganze Bescheid muss weg!", 0.3, "Rehbein"),
    # --- B Gericht: Feststellung, Frage -----------------------------------------------------------------------------------
    ("[klage]Sie klagt beim Verwaltungsgericht auf Aufhebung des ganzen Bescheids. [gericht]Das Gericht prüft den Zähler.", 0.2),
    ("[ri1]Verbraucht wurden zweihundertfünfzig Kubikmeter. Rechtmäßig sind nur tausendfünfhundert Euro.", 0.3, "Richter"),
    ("[hook]Der Bescheid über zweitausendvierhundert Euro ist also nur in Höhe von neunhundert Euro rechtswidrig. "
     "[frage]Wie lautet der Tenor? [frage2]Und welche Rolle spielt der Widerspruchsbescheid?", 0.6),
    # --- C Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Warum ein Widerspruchsbescheid? (NRW) ----------------------------------------------------------------------------
    ("[vv]Zuerst: Warum gibt es hier überhaupt einen Widerspruchsbescheid? [nrw]Unser Fall spielt in Nordrhein-Westfalen. "
     "Dort entfällt das Vorverfahren meist, nicht aber bei Bescheiden nach dem Kommunalabgabengesetz, Paragraf hundertzehn "
     "Absatz zwei Justizgesetz. [land]In deinem Land kann das anders sein. [wsb]Über den Widerspruch entscheidet hier die "
     "Stadt selbst.", P),
    # --- E Gegenstand der Klage, Wortlaut § 79 I Nr. 1 -----------------------------------------------------------------
    ("[wl79]Erstens, der Gegenstand der Klage. Paragraf neunundsiebzig Absatz eins Nummer eins: Gegenstand der "
     "Anfechtungsklage ist der ursprüngliche Verwaltungsakt in der Gestalt, die er durch den Widerspruchsbescheid gefunden "
     "hat. [beide]Angegriffen wird also der Gebührenbescheid, so wie ihn der Widerspruchsbescheid bestätigt hat. "
     "[t1]Deshalb beginnt der Tenor so: Der Gebührenbescheid der Beklagten vom zweiten März zweitausendsechsundzwanzig in "
     "Gestalt des Widerspruchsbescheids vom vierten Mai zweitausendsechsundzwanzig. [bekl]Beklagte ist die Stadt, "
     "Paragraf achtundsiebzig. [isol]Den Widerspruchsbescheid allein greifst du nur an, wenn er erstmals oder zusätzlich "
     "selbständig beschwert, Nummer zwei und Absatz zwei.", P),
    # --- F Umfang: Wortlaut § 113 I 1, Teilbarkeit ------------------------------------------------------------------------
    ("[wl113]Zweitens, der Umfang. Paragraf hundertdreizehn Absatz eins Satz eins: Soweit der Verwaltungsakt rechtswidrig "
     "und der Kläger dadurch in seinen Rechten verletzt ist, hebt das Gericht den Verwaltungsakt und den etwaigen "
     "Widerspruchsbescheid auf. [soweit]Das Schlüsselwort ist: soweit. [teil]Teilweise aufheben darf das Gericht aber nur, "
     "wenn der Bescheid teilbar ist: Der Rest muss sinnvoll und rechtmäßig bestehen bleiben können. [teil2]Hier gelingt "
     "das. Eine Gebühr von tausendfünfhundert Euro kann für sich stehen. [rv]Soweit Frau Rehbein zu viel zahlen soll, ist "
     "sie als Adressatin auch in ihren Rechten verletzt.", P),
    # --- G Tenor Hauptsache -----------------------------------------------------------------------------------------------
    ("[t2]Der Tenor geht also weiter: wird aufgehoben, soweit darin eine Gebühr von mehr als tausendfünfhundert Euro "
     "festgesetzt wird. [t3]Und weil Frau Rehbein den ganzen Bescheid loswerden wollte: Im Übrigen wird die Klage "
     "abgewiesen. [fehler]Ein typischer Klausurfehler ist, diesen Satz zu vergessen.", P),
    # --- H Klausurtipp § 113 II (Lexi) ------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Schau auf den Antrag. [wl1132]Begehrt der Kläger die Änderung eines Verwaltungsakts, der einen "
     "Geldbetrag festsetzt, kann das Gericht den Betrag in anderer Höhe festsetzen, Paragraf hundertdreizehn Absatz zwei. "
     "[tipp2]Der Tenor lautet dann etwa: Der Bescheid wird dahin geändert, dass die Gebühr auf tausendfünfhundert Euro "
     "festgesetzt wird. [tipp3]In beiden Fassungen bleiben tausendfünfhundert Euro.", PS),
    # --- I Kosten § 155 I 1 -----------------------------------------------------------------------------------------------
    ("[kosten]Drittens, die Kosten. Paragraf hundertfünfundfünfzig Absatz eins Satz eins: Wenn ein Beteiligter teils "
     "obsiegt, teils unterliegt, so sind die Kosten gegeneinander aufzuheben oder verhältnismäßig zu teilen. "
     "[quote]Frau Rehbein wollte zweitausendvierhundert Euro loswerden. Sie gewinnt neunhundert und verliert tausendfünfhundert. "
     "[bruch]Tausendfünfhundert von zweitausendvierhundert sind fünf Achtel. [t4]Also: Die Kosten des Verfahrens tragen "
     "die Klägerin zu fünf Achteln und die Beklagte zu drei Achteln.", P),
    # --- J Vorläufige Vollstreckbarkeit, Berufung -------------------------------------------------------------------------
    ("[vollstr]Viertens, die vorläufige Vollstreckbarkeit. Nach Paragraf hundertsiebenundsechzig Absatz zwei können "
     "Anfechtungsurteile nur wegen der Kosten für vorläufig vollstreckbar erklärt werden. [zpo]Nach Absatz eins gilt die "
     "ZPO entsprechend. Die Kosten, die hier vollstreckt werden können, liegen unter tausendfünfhundert Euro: Paragraf "
     "siebenhundertacht Nummer elf, mit der Abwendungsbefugnis nach Paragraf siebenhundertelf. [t5]Der Tenor: Das Urteil "
     "ist wegen der Kosten vorläufig vollstreckbar. [t6]Der jeweilige Vollstreckungsschuldner darf die Vollstreckung durch "
     "Sicherheitsleistung in Höhe von hundertzehn Prozent des vollstreckbaren Betrags abwenden, wenn nicht der jeweilige "
     "Vollstreckungsgläubiger vor der Vollstreckung Sicherheit in Höhe von hundertzehn Prozent des jeweils zu "
     "vollstreckenden Betrags leistet. [jeweils]Jeweils, weil beide Seiten Kosten tragen.", P),
    ("[ber]Und die Berufung? Das Verwaltungsgericht lässt sie nach Paragraf hundertvierundzwanzig a nur zu, wenn ein "
     "Zulassungsgrund nach Paragraf hundertvierundzwanzig Absatz zwei Nummer drei oder vier vorliegt. [ber2]Zu einer "
     "Nichtzulassung ist es nicht befugt.", P),
    # --- K Vollständiger Tenor --------------------------------------------------------------------------------------------
    ("[voll]Hier ist der vollständige Tenor zum Mitschreiben.", 5.0),
    # --- L Schema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für den Tenor. [s1]Erstens, der Gegenstand: [s1a]der Bescheid in Gestalt des Widerspruchsbescheids. "
     "[s1b]Zweitens, der Umfang: aufgehoben, soweit er rechtswidrig ist, [s1c]im Übrigen Klageabweisung. [s2]Drittens, die "
     "Kosten nach Paragraf hundertvierundfünfzig oder hundertfünfundfünfzig. [s3]Viertens, die vorläufige Vollstreckbarkeit "
     "wegen der Kosten. [s4]Und gegebenenfalls die Zulassung der Berufung.", PS),
    # --- M Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Angegriffen wird der Bescheid in Gestalt des Widerspruchsbescheids. [m2]Aufgehoben wird er nur, "
     "soweit er rechtswidrig ist und den Kläger in seinen Rechten verletzt.", 1.4),
]
