"""Folge 022 · Tankbetrug: Tanken ohne zu zahlen – Diebstahl oder Betrug?
Fiktiver Fall (Personen erfunden): Jens tankt an einer Selbstbedienungstankstelle mit vorgefasstem Zahlungsunwillen und fährt weg.
Linie: BGH, Urt. v. 5.5.1983 – 4 StR 121/83 (NJW 1983, 2827) → BGH, Beschl. v. 28.7.2009 – 4 StR 254/09 → BGH, Beschl. v.
10.1.2012 – 4 StR 632/11 (NJW 2012, 1092) → BGH 4 StR 497/12, 4 StR 532/15, 6 StR 676/24 (2025). Gegenfall (Entschluss nach dem
Tanken): Streit um den Eigentumsübergang – OLG Düsseldorf NStZ 1982, 249 einerseits, OLG Hamm NStZ 1983, 266 und OLG Koblenz
(10.8.1998 – 2 Ss 206/98) andererseits; vom BGH offengelassen. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Jens": "timo", "Birgit": "laura_klar", "Renate": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Säule drei ----------------------------------------------------------------------------------------------
    ("[fall]Dienstagabend an einer Selbstbedienungstankstelle am Stadtrand. [jens]Jens fährt an Säule drei. Sein Konto ist leer, "
     "[plan]und er hat schon zu Hause beschlossen: Heute zahlt er nicht.", 0.3),
    ("[j1]Einmal volltanken, und dann nichts wie weg.", 0.4, "Jens"),
    ("[tanken]Er tankt sechzig Liter Super für hundertzehn Euro. [birgit]Birgit sitzt an der Kasse. Auf ihrem Bildschirm sieht "
     "sie, wie an Säule drei ein Kunde tankt, und lässt ihn tanken. [weg]Dann hängt Jens den Zapfhahn ein, steigt ein und fährt davon.", 0.2),
    ("[b1]Halt! Säule drei ist nicht bezahlt!", 0.4, "Birgit"),
    ("[frage]Hat Jens das Benzin gestohlen, oder hat er Birgit betrogen? [frage2]Und was gilt, wenn Birgit gar nicht hingesehen hat?", 0.6),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Diebstahl --------------------------------------------------------------------------------------------------------
    ("[a]Wir beginnen mit Jens. [p242]Naheliegend ist Diebstahl, Paragraf zweihundertzweiundvierzig. [wegn]Dafür müsste Jens das "
     "Benzin weggenommen, also fremden Gewahrsam gebrochen haben. [erlaubt]Doch die Tankstelle lässt ihn tanken: Birgit ist mit dem "
     "Einfüllen einverstanden. [geben]Der Bundesgerichtshof sieht darin ein durch Täuschung bewirktes Geben, kein Nehmen. "
     "[kein242]Ein Diebstahl scheidet aus.", PS),
    # --- D Betrug -----------------------------------------------------------------------------------------------------------
    ("[p263]Also Betrug, Paragraf zweihundertdreiundsechzig. [merkm]Er verlangt Täuschung, Irrtum, Vermögensverfügung und Schaden, "
     "dazu Vorsatz und die Absicht rechtswidriger Bereicherung.", P),
    ("[taeu]Erstens die Täuschung. Jens tritt auf wie jeder Kunde. [konkl]Damit erklärt er schlüssig: Ich bezahle nach dem Tanken. "
     "[falsch]Das stimmt nicht, denn er wollte von Anfang an nicht zahlen.", P),
    ("[irr]Zweitens der Irrtum. Birgit sieht den Tankvorgang und hält Jens für zahlungsbereit. [verf]Drittens die Verfügung: "
     "Weil sie irrt, gestattet sie das Tanken. [schad]Viertens der Schaden: Jens hat das Benzin, die Tankstelle verliert es ohne Gegenwert.", P),
    ("[subj]Jens handelt vorsätzlich und will sich zu Unrecht bereichern. [erg1]Er ist wegen Betruges strafbar.", PS),
    # --- E Abwandlung: niemand bemerkt den Tankvorgang -----------------------------------------------------------------------
    ("[abw]Jetzt die Abwandlung: Birgit telefoniert und bemerkt Jens gar nicht. [kirr]Dann gibt es keinen Irrtum, und ohne Irrtum "
     "ist der Betrug nicht vollendet. [vers]Nach seiner Vorstellung hat Jens aber unmittelbar zum Betrug angesetzt. [vers2]Er ist "
     "wegen versuchten Betrugs strafbar, Paragrafen zweihundertdreiundsechzig, zweiundzwanzig und dreiundzwanzig.", P),
    ("[bgh12]So entschied der Bundesgerichtshof zweitausendzwölf. Das Gericht konnte nicht klären, ob die Kassiererin etwas bemerkt "
     "hatte. [zugunsten]Also ging der Bundesgerichtshof zugunsten des Täters nur von einem Versuch aus. [subs]Eine Unterschlagung "
     "tritt dahinter zurück. Paragraf zweihundertsechsundvierzig greift nur, wenn die Tat nicht anderswo mit schwererer Strafe bedroht ist.", PS),
    # --- F Gegenfall: Entschluss erst nach dem Tanken ------------------------------------------------------------------------
    ("[gegen]Gegenfall: Renate tankt und will ganz normal bezahlen. [schlange]Dann sieht sie die lange Schlange an der Kasse.", 0.2),
    ("[r1]Die Schlange ist mir zu lang. Dann eben nicht.", 0.4, "Renate"),
    ("[rweg]Sie fährt davon. [r263]Ein Betrug scheidet aus: Beim Tanken wollte sie noch zahlen, sie hat also nicht getäuscht. "
     "[r242]Ein Diebstahl auch, denn das Tanken war erlaubt. [p246]Bleibt Unterschlagung, Paragraf zweihundertsechsundvierzig.", P),
    ("[fremd]Dafür muss das Benzin beim Wegfahren noch fremd sein. Genau das ist umstritten. [ans1]Nach einer Ansicht wird die "
     "Kundin schon beim Einfüllen Eigentümerin. Dann bleibt Renate straflos und schuldet nur den Kaufpreis. [ans2]Die Gegenansicht "
     "sagt: Ware gegen Geld. Das Eigentum geht erst mit dem Bezahlen über. [unt]Dann eignet sich Renate mit dem Wegfahren fremdes "
     "Benzin zu und begeht eine Unterschlagung.", P),
    ("[olg]So sehen es die Oberlandesgerichte Hamm und Koblenz, das Oberlandesgericht Düsseldorf sah es anders. [misch]Selbst wenn "
     "Renate durch die Vermischung im Tank Miteigentümerin würde, stünde das der Unterschlagung nach Koblenz nicht entgegen. "
     "[offen]Der Bundesgerichtshof hat die Frage offengelassen.", PS),
    # --- G Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Entscheidend ist, wann der Täter beschließt, nicht zu zahlen. [tipp1]Schon vor dem Tanken: Prüfe Betrug "
     "und frage, ob das Personal den Vorgang bemerkt hat. [tipp2]Bleibt das offen, gilt zugunsten des Täters nur der Versuch. "
     "[tipp3]Erst danach: Prüfe Unterschlagung und entscheide den Streit ums Eigentum.", PS),
    # --- H Klausurschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]A, Entschluss schon vor dem Tanken. [k1a]Römisch eins: Diebstahl scheitert an der Wegnahme. "
     "[k1b]Römisch zwei: Betrug mit Täuschung, Irrtum, Verfügung, Schaden, Vorsatz und Bereicherungsabsicht. [k1c]Römisch drei: "
     "Fehlt der Irrtum, versuchter Betrug. [k1d]Die Unterschlagung tritt zurück.", P),
    ("[k2]B, Entschluss erst nach dem Tanken. [k2a]Betrug und Diebstahl scheiden aus. [k2b]Unterschlagung nur, wenn das Benzin "
     "noch der Tankstelle gehört.", PS),
    # --- I Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer schon zahlungsunwillig tankt, begeht Betrug. [m2]Bemerkt ihn niemand, bleibt es beim Versuch. "
     "[m3]Wer sich erst danach entschließt, begeht höchstens eine Unterschlagung, und das nur, wenn das Benzin noch fremd ist.", 1.4),
]
