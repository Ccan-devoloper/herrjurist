"""Folge 031 · Gemüseblatt-Fall: Vertrag mit Schutzwirkung für Dritte erklärt (Mo · Der Fall · Schuldrecht AT).
Echter Fall, sachlich nacherzählt: BGH, Urt. v. 28.1.1976 – VIII ZR 246/74 = BGHZ 66, 51 (Gemüseblatt-/Salatblattfall).
Beteiligte nur als namenlose Funktionsfiguren (die Mutter, die Tochter, der Betreiber des Ladens); keine echten Namen.
Kern: culpa in contrahendo (heute § 311 II Nr. 2, § 241 II BGB), warum die Tochter selbst keinen Vertrag anbahnt, Vertrag
mit Schutzwirkung für Dritte (Leistungsnähe, Einbeziehungsinteresse, Erkennbarkeit/Zumutbarkeit, Schutzbedürfnis nach
BGH, Urt. v. 5.7.2024 – V ZR 34/24, Rn. 14), Vorteile gegenüber §§ 823, 831 BGB, Streitstand zur Herleitung.
Wortlautkarten: § 311 II und § 241 II BGB. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.9

STIMMEN = {"Mutter": "lucy", "Betreiber": "marc"}  # Lexi = Erzählerstimme (Carla); die Tochter spricht nicht

SEGMENTE = [
    # --- A Fall: im Selbstbedienungsladen --------------------------------------------------------------------------------
    ("[fall]November neunzehnhundertdreiundsechzig, ein kleiner Selbstbedienungsladen. [mutter]Eine Mutter kauft ein, "
     "[tochter]ihre vierzehnjährige Tochter begleitet sie. [kasse]Die Mutter hat ihre Waren ausgesucht und steht an der Kasse. "
     "[pack]Die Tochter geht um die Kasse herum zur Packablage, um beim Einpacken zu helfen. "
     "[rutscht]Dort rutscht sie auf einem Gemüseblatt aus und stürzt.", 0.3),
    ("[m1]Hast du dir wehgetan?", 0.3, "Mutter"),
    ("[knie]Sie verletzt sich am Knie und muss länger behandelt werden. "
     "[klage]Erst neunzehnhundertsiebzig verklagt die Tochter den Betreiber des Ladens auf Ersatz ihres Schadens.", 0.3),
    ("[b1]Die Ansprüche sind doch längst verjährt!", 0.4, "Betreiber"),
    ("[frage]Hat die Tochter, die selbst nichts kaufen wollte, trotzdem einen vertraglichen Anspruch?", 0.6),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Warum ein vertraglicher Anspruch? ------------------------------------------------------------------------------
    ("[delikt]Naheliegend ist Paragraf achthundertdreiundzwanzig, wegen verletzter Verkehrssicherungspflicht. "
     "[verj]Doch deliktische Ansprüche verjährten damals schneller, nach Paragraf achthundertzweiundfünfzig alter Fassung. "
     "[dreissig]Für das Verschulden bei Vertragsschluss galten dreißig Jahre.", P),
    ("[vorteil]Der Bundesgerichtshof nennt weitere Vorteile. [v278]Für Gehilfen haftet der Betreiber nach Paragraf "
     "zweihundertachtundsiebzig, ohne die Entlastung des Paragrafen achthunderteinunddreißig. "
     "[vbew]Und die Beweislast für das Verschulden trägt er selbst.", PS),
    # --- D Die Mutter: culpa in contrahendo, § 311 II, § 241 II --------------------------------------------------------------
    ("[mutter2]Wäre die Mutter gestürzt, hätte sie aus Verschulden bei Vertragsschluss Ersatz verlangen können. "
     "[p311]Heute steht diese culpa in contrahendo in Paragraf dreihundertelf Absatz zwei. [nr2]Nummer zwei: "
     "die Anbahnung eines Vertrags, bei der ein Teil dem anderen die Einwirkung auf seine Rechtsgüter ermöglicht. "
     "[laden]Das tut, wer sein Geschäft für Kunden öffnet.", P),
    ("[p241]Die Pflichten folgen aus Paragraf zweihunderteinundvierzig Absatz zwei: Rücksicht auf die Rechte, Rechtsgüter "
     "und Interessen des anderen Teils.", PS),
    # --- E Die Tochter selbst --------------------------------------------------------------------------------------------------
    ("[kind]Und die Tochter? [kind2]Sie wollte selbst nichts kaufen, sie begleitete nur ihre Mutter. "
     "[kind3]Eine eigene culpa in contrahendo setzt aber voraus, dass man den Laden zumindest als möglicher Kunde betritt. "
     "[kind4]Wer nur Schutz vor dem Wetter sucht oder den Laden als Durchgang nutzt, bahnt keinen Vertrag an. "
     "[kind5]Ein eigenes vorvertragliches Schuldverhältnis hat die Tochter also nicht.", PS),
    # --- F Vertrag mit Schutzwirkung für Dritte ---------------------------------------------------------------------------------
    ("[vsd]Hier hilft der Vertrag mit Schutzwirkung für Dritte. [vsd2]Der Dritte wird in den Schutzbereich eines fremden "
     "Schuldverhältnisses einbezogen. [vsd3]Er kann keine Leistung verlangen, aber Schutz, und bei Verletzung "
     "Schadensersatz im eigenen Namen. [vsd4]Dafür gelten strenge Voraussetzungen.", P),
    # --- G Die vier Voraussetzungen ---------------------------------------------------------------------------------------------
    ("[ln]Erstens: Leistungsnähe. Der Dritte kommt bestimmungsgemäß mit der Leistung in Berührung und ist den Gefahren "
     "ebenso ausgesetzt wie der Gläubiger. [ln2]Die Tochter war mit der Mutter im Laden, in derselben Kassenzone.", P),
    ("[gn]Zweitens: Einbeziehungsinteresse, auch Gläubigernähe. [gn2]Die Mutter war für das Wohl und Wehe ihrer "
     "Tochter verantwortlich.", P),
    ("[ek]Drittens: Erkennbarkeit und Zumutbarkeit. [ek2]Für den Betreiber ist erkennbar, dass die Tochter dazugehört, "
     "und ihr den gleichen Schutz zu geben, ist ihm zumutbar.", P),
    ("[sb]Viertens: Schutzbedürfnis. [sb2]Die Tochter hat keinen eigenen, gleichwertigen vertraglichen Anspruch.", PS),
    # --- H Schutzwirkung schon vor dem Vertragsschluss -------------------------------------------------------------------------
    ("[vor]Aber der Kauf war noch gar nicht geschlossen. [vor2]Für den Bundesgerichtshof ohne Bedeutung: "
     "Die Schutzpflicht gilt vor wie nach dem Vertragsschluss. "
     "[begr]Die Gesetzesbegründung zu Paragraf dreihundertelf nennt den Fall ausdrücklich, als Salatblattfall. "
     "[begr2]Danach gilt die Schutzwirkung auch im vorvertraglichen Schuldverhältnis.", PS),
    # --- I Streitstand: Woraus folgt die Schutzwirkung? -----------------------------------------------------------------------
    ("[streit]Woraus folgt die Schutzwirkung? Das ist umstritten. "
     "[st1]Die Rechtsprechung leitet sie aus ergänzender Vertragsauslegung her, Paragraf hundertsiebenundfünfzig. "
     "[st2]Andere sehen Gewohnheitsrecht oder Rechtsfortbildung; der Bundesgerichtshof ließ das offen. "
     "[st3]Zitiert wird oft Paragraf dreihundertachtundzwanzig analog. "
     "[st4]Paragraf dreihundertelf Absatz drei kennt Schuldverhältnisse auch zu Personen, die nicht Vertragspartei "
     "werden sollen; [st5]die Gesetzesbegründung lässt die Weiterentwicklung dort offen.", PS),
    # --- J Prüfung des Anspruchs der Tochter ----------------------------------------------------------------------------------
    ("[a]Prüfen wir den Anspruch der Tochter. [p1]Römisch eins: das Schuldverhältnis zwischen Mutter und Betreiber, "
     "mit Schutzwirkung für die Tochter. Liegt vor. [p2]Römisch zwei: Pflichtverletzung. Der Betreiber muss den Boden "
     "verkehrssicher halten. [p2b]Das Gemüseblatt am Boden ist eine Gefahr aus seinem Bereich.", P),
    ("[p3]Römisch drei: Vertretenmüssen. Es wird vermutet, Paragraf zweihundertachtzig Absatz eins Satz zwei. "
     "[p3b]Der Betreiber konnte nicht beweisen, dass er alle zumutbare Sorgfalt beachtet hatte. "
     "[p3c]Fehler seiner Angestellten rechnet ihm Paragraf zweihundertachtundsiebzig zu.", P),
    ("[p4]Römisch vier: Schaden. Ihre Aufwendungen sind zu ersetzen, [p4b]gekürzt um ein Mitverschulden von einem Viertel, "
     "Paragraf zweihundertvierundfünfzig. [erg]Ergebnis: Der Bundesgerichtshof bestätigt den Anspruch, und er war nicht verjährt.", PS),
    # --- K Und heute? -------------------------------------------------------------------------------------------------------------
    ("[heute]Und heute? [h1]Der Verjährungsvorteil ist weg: Beide Ansprüche verjähren regelmäßig in drei Jahren, "
     "Paragraf hundertfünfundneunzig. [h2]Schmerzensgeld gibt es nach Paragraf zweihundertdreiundfünfzig Absatz zwei "
     "auch bei vertraglicher Haftung. [h3]Geblieben ist der Vorteil bei Gehilfen: Sie werden nach Paragraf "
     "zweihundertachtundsiebzig ohne Entlastung zugerechnet.", PS),
    # --- L Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst, ob der Dritte selbst ein Schuldverhältnis hat. [tipp1]Erst wenn nicht, kommt die "
     "Schutzwirkung. [tipp2]Und verwechsle sie nicht mit dem echten Vertrag zugunsten Dritter, Paragraf "
     "dreihundertachtundzwanzig: [tipp3]Der gibt einen Anspruch auf die Leistung, die Schutzwirkung nur auf Schutz.", PS),
    # --- M Klausurschema ----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s1]Anspruch aus Paragrafen zweihundertachtzig, dreihundertelf, zweihunderteinundvierzig, "
     "mit Schutzwirkung für Dritte. [s2]Römisch eins: Schuldverhältnis mit Schutzwirkung. Erstens: Schuldverhältnis "
     "zwischen Gläubiger und Schuldner. [s3]Zweitens: Leistungsnähe. [s4]Drittens: Einbeziehungsinteresse. "
     "[s5]Viertens: Erkennbarkeit und Zumutbarkeit. [s6]Fünftens: Schutzbedürfnis.", P),
    ("[s7]Römisch zwei: Pflichtverletzung. [s8]Römisch drei: Vertretenmüssen, mit Paragraf zweihundertachtundsiebzig. "
     "[s9]Römisch vier: Schaden, mit Mitverschulden.", PS),
    # --- N Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer nur begleitet, bahnt keinen Vertrag an. [m2]Geschützt ist er trotzdem, wenn er dem Kunden so nahe "
     "steht, dass dessen Schutz erkennbar auch ihm gilt.", 1.4),
]
