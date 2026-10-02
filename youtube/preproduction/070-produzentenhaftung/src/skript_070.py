"""Folge 070 · Explodierende Flasche: Produzentenhaftung nach § 823 I BGB (Mo · Der Fall · Zivilrecht/Deliktsrecht,
Format Klassiker-Fall). Erfundener Ausgangsfall nach dem Plan-Hook („Eine Mineralwasserflasche explodiert beim Öffnen und
verletzt dein Auge“): Bettina kauft im Supermarkt einen Kasten Mineralwasser in Mehrweg-Glasflaschen; beim Öffnen
explodiert eine Flasche, ein Splitter trifft ihr Auge (keine Wunde im Bild, nur abstrakte Augenklappe). Ein Gutachter
findet einen feinen Haarriss. Herr Kroll betreibt den Mineralbrunnen (Hersteller); seine Leute sehen die Flaschen am Band
nur flüchtig an. Danach die echten Fälle: Hühnerpest (BGH, Urt. v. 26.11.1968 – VI ZR 212/66, BGHZ 51, 91:
Beweislastumkehr beim Verschulden), Limonadenflasche (BGH, Urt. v. 7.6.1988 – VI ZR 91/87, BGHZ 104, 323:
Befundsicherungspflicht) und Mineralwasserflasche II (BGH, Urt. v. 9.5.1995 – VI ZR 158/94, BGHZ 129, 353).
Kern: Verkehrssicherungspflichten des Herstellers (Konstruktion, Fabrikation, Instruktion, Produktbeobachtung), Beweisnot,
Beweislastumkehr, Befundsicherung bei Mehrwegflaschen, Ausreißer und Entlastung, Fall-Ergebnis mit § 253 II; Abgrenzung
§ 1 ProdHaftG (verschuldensunabhängig, § 11 Selbstbeteiligung, § 15 II, RL (EU) 2024/2853) kurz.
Figuren: Bettina (lucy), Herr Kroll (stephan); Lexi/Erzählerin Carla. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.6

STIMMEN = {"Bettina": "lucy", "Kroll": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Küche, explodierende Flasche --------------------------------------------------------------------------
    ("[fall]Bettina hat im Supermarkt einen Kasten Mineralwasser gekauft, in Mehrwegflaschen aus Glas. "
     "[oeffnen]Zu Hause will sie eine Flasche öffnen. [knall]Da explodiert die Flasche. "
     "[auge]Ein Splitter trifft Bettina am Auge, sie muss ärztlich behandelt werden.", 0.3),
    ("[b1]Mein Auge! Die Flasche ist einfach geplatzt!", 0.3, "Bettina"),
    ("[riss]Ein Gutachter findet an der Bruchstelle einen feinen Haarriss im Glas. "
     "[kroll]Abgefüllt hat das Wasser der Mineralbrunnen von Herrn Kroll.", 0.3),
    ("[kr1]Unsere Leute schauen sich jede Flasche an. Vielleicht ist sie bei Ihnen heruntergefallen!", 0.3, "Kroll"),
    ("[ford]Bettina verlangt von Herrn Kroll die Behandlungskosten und ein Schmerzensgeld. "
     "[frage]Einen Vertrag hat sie aber nur mit dem Supermarkt. [frage2]Haftet der Hersteller trotzdem? "
     "Und wie soll sie beweisen, was in seinem Betrieb passiert ist?", 0.6),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 823 I und Beweisnot ----------------------------------------------------------------------------------------
    ("[norm]Ohne Vertrag hilft das Deliktsrecht, Paragraf achthundertdreiundzwanzig Absatz eins: [w823]Wer "
     "vorsätzlich oder fahrlässig den Körper oder die Gesundheit eines anderen widerrechtlich verletzt, muss ihm den "
     "daraus entstehenden Schaden ersetzen.", P),
    ("[bew]Aus dem Schema kennst du den Grundsatz: Der Anspruchsteller beweist alle anspruchsbegründenden "
     "Tatsachen, auch das Verschulden. [bew2]Doch was im Betrieb des Herstellers geschieht, kann Bettina nicht sehen.", PS),
    # --- D Herstellerpflichten -----------------------------------------------------------------------------------------
    ("[vsp]Wer ein Produkt herstellt, schafft eine Gefahrenquelle. Deshalb treffen ihn Verkehrssicherungspflichten: "
     "die notwendigen und zumutbaren Vorkehrungen, um andere vor Schäden zu bewahren. "
     "[p1]Erstens die Konstruktionspflicht: Schon die Planung muss dem gebotenen Sicherheitsstandard genügen. "
     "[p2]Zweitens die Fabrikationspflicht: Kein einzelnes Stück darf in der Herstellung vom sicheren Plan abweichen.", P),
    ("[p3]Drittens die Instruktionspflicht: Er muss vor Gefahren warnen, die beim bestimmungsgemäßen Gebrauch oder "
     "naheliegenden Fehlgebrauch drohen. [p4]Viertens die Produktbeobachtungspflicht: Auch nach dem Inverkehrbringen muss er sein "
     "Produkt auf unbekannte Gefahren hin beobachten. [pfall]Ein Haarriss in einer einzelnen Flasche ist ein "
     "Fabrikationsfehler.", PS),
    # --- E Hühnerpest ---------------------------------------------------------------------------------------------------
    ("[huhn]Wer hier was beweisen muss, hat der Bundesgerichtshof im Hühnerpest-Fall von "
     "neunzehnhundertachtundsechzig entschieden. [h1]Ein Tierarzt hatte die Hühner einer Hühnerfarm gegen die "
     "Hühnerpest geimpft. [h2]Einige Tage später brach die Seuche aus, mehr als viertausend Hühner verendeten. "
     "[h3]Der Impfstoff war bakteriell verunreinigt, wahrscheinlich beim Abfüllen. [h4]Einen Vertrag mit dem "
     "Impfstoffwerk hatte die Farm nicht; ihr blieb nur das Deliktsrecht.", P),
    ("[regel]Die Regel: Die Geschädigte muss beweisen, dass ein Fehler des Produkts den Schaden verursacht "
     "hat, und zwar aus dem Organisations- und Gefahrenbereich des Herstellers. [umkehr]Dann muss der Hersteller "
     "beweisen, dass ihn kein Verschulden trifft. [grund]Denn er ist näher daran: Er überblickt die "
     "Produktion, der Geschädigte kann sie nicht aufklären.", P),
    ("[huhn2]Das Impfstoffwerk konnte sich nicht entlasten. Es füllte große Flaschen noch von Hand ab, und zumutbare "
     "bessere Sicherungen fehlten. [huhn3]Es haftete dem Grunde nach.", PS),
    # --- F Befundsicherung -----------------------------------------------------------------------------------------------
    ("[mehr]Bei Mehrwegflaschen bleibt eine Lücke: Ein Haarriss kann auch später entstehen, etwa zu Hause. [wann]Wer beweist, dass der Fehler schon da war, als die Flasche den Betrieb verließ?", P),
    ("[limo]Hier hilft die Befundsicherungspflicht, so schon im Limonadenflaschen-Fall von "
     "neunzehnhundertachtundachtzig. [befund]Wer Flaschen mit Sprudelgetränken wieder befüllt, muss sie auf ihren "
     "einwandfreien Zustand prüfen und den Befund sichern. [bumk]Tut er das nicht, kann sich die Beweislast umkehren: Dann muss er beweisen, dass der "
     "Fehler nicht in seinem Bereich entstanden ist.", P),
    ("[mw]Im Mineralwasserflaschen-Fall von neunzehnhundertfünfundneunzig explodierte eine Mehrwegflasche in der Hand "
     "eines neunjährigen Mädchens, Splitter trafen ihr Auge. [mw2]Verlangt ist ein Kontrollverfahren, "
     "das den Zustand jeder Flasche ermittelt. [mw3]Sichtkontrollen bei rund vier Flaschen pro Sekunde hielt der Bundesgerichtshof "
     "dafür kaum für geeignet.", PS),
    # --- G Ausreißer und Entlastung ----------------------------------------------------------------------------------------
    ("[aus]Und wenn der Hersteller alles Zumutbare getan hat? [aus2]Dann kann der Fehler ein Ausreißer sein, "
     "der sich trotz aller zumutbaren Vorkehrungen nicht vermeiden lässt. [aus3]Beweist der Hersteller das, fehlt sein "
     "Verschulden, und aus Paragraf achthundertdreiundzwanzig haftet er nicht.", PS),
    # --- H Lösung des Falls -------------------------------------------------------------------------------------------------
    ("[loes]Zurück zu Bettina. [l1]Ihr Auge ist verletzt, also Körper und Gesundheit. [l2]Der Haarriss ist ein "
     "Fabrikationsfehler und hat die Explosion verursacht; das belegt das Gutachten. [l3]Herr Kroll lässt die Flaschen "
     "am Band nur flüchtig ansehen und verletzt damit seine Befundsicherungspflicht. Deshalb muss er beweisen, dass der "
     "Riss erst später entstand.", P),
    ("[l4]Für das Verschulden gilt die Hühnerpest-Regel: Herr Kroll müsste sich entlasten, und das gelingt ihm nicht. "
     "[erg]Ergebnis: Er haftet nach Paragraf achthundertdreiundzwanzig Absatz eins. [erg2]Bettina bekommt die "
     "Behandlungskosten und nach Paragraf zweihundertdreiundfünfzig Absatz zwei ein Schmerzensgeld.", PS),
    # --- I Abgrenzung Produkthaftungsgesetz ----------------------------------------------------------------------------------
    ("[phg]Daneben steht das Produkthaftungsgesetz. [w1]Paragraf eins: Wird durch den Fehler eines Produkts jemand "
     "verletzt, muss der Hersteller den Schaden ersetzen. [ohne]Auf ein Verschulden kommt es nicht an, und er haftet "
     "auch für Ausreißer. [sach]Bei Sachschäden trägt der Geschädigte aber fünfhundert Euro selbst, und geschützt "
     "sind nur Sachen für den privaten Gebrauch.", P),
    ("[beide]Beide Ansprüche bestehen nebeneinander. [eu]Und die Reform läuft: Eine neue Produkthaftungsrichtlinie der "
     "EU muss bis zum neunten Dezember zweitausendsechsundzwanzig umgesetzt sein.", PS),
    # --- J Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe Paragraf eins Produkthaftungsgesetz und Paragraf achthundertdreiundzwanzig getrennt. "
     "[tipp1]Und schreib nie, die Produzentenhaftung sei eine Haftung ohne Verschulden. [tipp2]Nur die Beweislast "
     "kehrt sich um; entlastet sich der Hersteller, haftet er nicht.", PS),
    # --- K Klausurschema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema zur Produzentenhaftung: [k1]Römisch eins, Tatbestand: Rechtsgutsverletzung, Verletzung "
     "einer Herstellerpflicht durch einen Produktfehler, Kausalität. [k1b]Den Fehler beweist der Geschädigte, bei "
     "Mehrwegflaschen hilft die Befundsicherung.", P),
    ("[k2]Römisch zwei: Rechtswidrigkeit. [k3]Römisch drei: Verschulden, mit Beweislastumkehr zulasten des Herstellers. "
     "[k4]Römisch vier: Schaden und Rechtsfolge, mit Schmerzensgeld.", PS),
    # --- L Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Den Produktfehler und seine Folgen beweist der Geschädigte. [m2]Dass ihn kein Verschulden trifft, "
     "muss der Hersteller beweisen.", 1.4),
]
