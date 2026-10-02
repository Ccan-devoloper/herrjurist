"""Folge 059 · Sachmangel § 434 BGB: Wann ist eine Sache mangelhaft? (Mi · Examenswissen · Zivilrecht/Kaufrecht, Format
Schema). Beispielfall nach dem Plan-Hook („Der Laptop funktioniert – nur nicht mit der Software, die ihr ausdrücklich
vereinbart hattet“): Kerstin (Verbraucherin) kauft im Computerladen von Herrn Kranich (Unternehmer) einen Laptop für 900 €;
vereinbart ist, dass ihr Schnittprogramm darauf läuft. Zu Hause funktioniert der Laptop, das Programm startet nicht
(Grafikkarte zu schwach).
Kern: Wortlautkarte § 434 I (gleichrangige subjektive, objektive und Montageanforderungen bei Gefahrübergang, § 446 S. 1),
§ 434 II (Beschaffenheit inkl. Kompatibilität, vorausgesetzte Verwendung, Zubehör/Anleitungen), § 434 III (gewöhnliche
Verwendung, übliche Beschaffenheit, Werbung, Ausnahme III 3, Reparierbarkeit seit 31.7.2026, Art. 229 § 72 EGBGB),
Gleichrang, § 476 I 2, § 475b (je ein Satz), § 434 IV, § 434 V (andere Sache; Menge als Beschaffenheit), § 435 abgrenzend,
§ 477 (ein Satz), Ausblick § 437 (Folge 063).
Figuren: Kerstin (sabrina), Herr Kranich (marc); Lexi/Erzählerin Carla. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.7

STIMMEN = {"Kerstin": "sabrina", "Kranich": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: im Laden, zu Hause ----------------------------------------------------------------------------------------
    ("[fall]Kerstin schneidet in ihrer Freizeit Videos. [laden]Im Computerladen von Herrn Kranich sucht sie einen neuen "
     "Laptop.", 0.3),
    ("[ke1]Auf dem Laptop muss mein Schnittprogramm laufen. Geht das?", 0.3, "Kerstin"),
    ("[h1]Ja, das läuft darauf. Netzteil und Anleitung sind dabei.", 0.4, "Kranich"),
    ("[kauf]Kerstin kauft den Laptop für neunhundert Euro und nimmt ihn gleich mit. [haus]Zu Hause startet er sofort, "
     "Internet und E-Mail funktionieren. [prog]Nur das Schnittprogramm startet nicht: Die Grafikkarte ist zu schwach.", 0.3),
    ("[ke2]Der Laptop läuft, aber mein Programm nicht!", 0.4, "Kerstin"),
    ("[frage]Ist der Laptop mangelhaft, obwohl er funktioniert? [frage2]Und woran misst man das überhaupt?", 0.6),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 434 Abs. 1 -----------------------------------------------------------------------------------------------------
    ("[norm]Kerstin hat einen Anspruch auf eine mangelfreie Sache, Paragraf vierhundertdreiunddreißig Absatz eins Satz "
     "zwei. Was ein Sachmangel ist, sagt Paragraf vierhundertvierunddreißig. [w1]Absatz eins: Die Sache ist frei von "
     "Sachmängeln, wenn sie bei Gefahrübergang den subjektiven Anforderungen, den objektiven Anforderungen und den "
     "Montageanforderungen dieser Vorschrift entspricht.", P),
    ("[und]Achte auf das Wort und: Seit der Reform zweitausendzweiundzwanzig stehen die drei "
     "Anforderungen gleichrangig nebeneinander. Die Sache muss alle erfüllen. [gefahr]Maßgeblich ist der Gefahrübergang, "
     "nach Paragraf vierhundertsechsundvierzig in der Regel die Übergabe, hier also im Laden.", PS),
    # --- D I. subjektive Anforderungen --------------------------------------------------------------------------------------
    ("[sub]Römisch eins: die subjektiven Anforderungen, Absatz zwei. [s1]Die Sache muss erstens die vereinbarte "
     "Beschaffenheit haben, [s2]zweitens sich für die nach dem Vertrag vorausgesetzte Verwendung eignen [s3]und drittens "
     "mit dem vereinbarten Zubehör und den vereinbarten Anleitungen übergeben werden. [kompat]Zur Beschaffenheit gehören "
     "nach Satz zwei ausdrücklich auch Funktionalität und Kompatibilität.", P),
    ("[subs]Kerstin und Herr Kranich haben vereinbart: Das Schnittprogramm läuft darauf. [s1n]Diese Kompatibilität fehlt. "
     "[s2n]Auch für den vorausgesetzten Zweck, den Videoschnitt, eignet sich der Laptop nicht. [s3j]Netzteil und Anleitung "
     "waren dabei, das ist erfüllt. [sube]Die subjektiven Anforderungen sind also verfehlt.", PS),
    # --- E II. objektive Anforderungen --------------------------------------------------------------------------------------
    ("[obj]Römisch zwei: die objektiven Anforderungen, Absatz drei. Sie gelten, soweit nicht wirksam etwas anderes "
     "vereinbart ist. [o1]Die Sache muss sich für die gewöhnliche Verwendung eignen, [o2]eine übliche Beschaffenheit haben, "
     "die der Käufer erwarten kann, [o4]und mit dem Zubehör und den Anleitungen kommen, die er erwarten kann.", P),
    ("[osub]Der Laptop von Kerstin eignet sich zum Surfen und Schreiben. Ein Laptop dieser Klasse muss nicht jedes anspruchsvolle "
     "Schnittprogramm schaffen. [ook]Die objektiven Anforderungen sind erfüllt.", PS),
    ("[werb]Zur Erwartung zählen auch öffentliche Äußerungen von Verkäufer oder Hersteller, etwa in der Werbung. "
     "[akku]Verspricht die Werbung zehn Stunden Akku und hält er nur drei, wäre der Laptop auch objektiv mangelhaft. "
     "[ausn]Nicht gebunden ist der Verkäufer nur, wenn er die Äußerung nicht kannte und nicht kennen konnte, wenn sie bei "
     "Vertragsschluss berichtigt war oder wenn sie den Kauf nicht beeinflussen konnte.", PS),
    ("[rep]Zur üblichen Beschaffenheit zählen nach Satz zwei etwa Haltbarkeit und Sicherheit, "
     "[rep2]bei Verträgen ab dem einunddreißigsten Juli zweitausendsechsundzwanzig auch die Reparierbarkeit. "
     "Zwischen Unternehmern gilt das erst ab zweitausendachtundzwanzig.", PS),
    # --- F Gleichrang, Verbrauchsgüterkauf ----------------------------------------------------------------------------------
    ("[gleich]Deshalb gilt: [gl1]Der Laptop erfüllt die objektiven Anforderungen, "
     "aber nicht die vereinbarten. [gl2]Das genügt für einen Sachmangel. [gl3]Umgekehrt hilft die Vereinbarung allein auch "
     "nicht: Läuft das Programm, ist aber der Akku defekt, ist der Laptop ebenfalls mangelhaft.", PS),
    ("[vgk]Kerstin ist Verbraucherin, Herr Kranich Unternehmer: ein Verbrauchsgüterkauf. [p476]Von den objektiven "
     "Anforderungen kann er dann nur abweichen, wenn er Kerstin vor ihrer Vertragserklärung eigens auf das abweichende "
     "Merkmal hinweist und die Abweichung ausdrücklich und gesondert vereinbart wird, Paragraf vierhundertsechsundsiebzig "
     "Absatz eins Satz zwei. [p475b]Für digitale Elemente wie das vorinstallierte Betriebssystem gehören beim "
     "Verbrauchsgüterkauf zusätzlich Aktualisierungen dazu, Paragraf vierhundertfünfundsiebzig b.", PS),
    # --- G III. Montageanforderungen ----------------------------------------------------------------------------------------
    ("[mont]Römisch drei: die Montageanforderungen, Absatz vier. Sie spielen nur eine Rolle, soweit eine Montage "
     "durchzuführen ist, etwa bei einer Einbauküche. [mo1]Mangelhaft ist die Sache dann, wenn der Verkäufer unsachgemäß "
     "montiert [mo2]oder wenn eine falsche Montage auf einem Fehler in seiner Anleitung beruht. [mo3]Beim Laptop war "
     "nichts zu montieren.", PS),
    # --- H IV. andere Sache, Menge ------------------------------------------------------------------------------------------
    ("[ali]Römisch vier: Absatz fünf. Liefert der Verkäufer eine andere Sache als die geschuldete, etwa ein anderes "
     "Modell, steht das einem Sachmangel gleich. [menge]Und wer zu wenig liefert, verfehlt die vereinbarte Menge; sie "
     "gehört seit der Reform zur Beschaffenheit.", PS),
    # --- I Rechtsmangel, Beweislast, Ergebnis -------------------------------------------------------------------------------
    ("[recht]Davon zu trennen ist der Rechtsmangel nach Paragraf vierhundertfünfunddreißig: Dort geht es um Rechte Dritter "
     "an der Sache, nicht um ihre Beschaffenheit.", P),
    ("[p477]Und der Beweis? Zeigt sich beim Verbrauchsgüterkauf innerhalb eines Jahres seit Gefahrübergang ein abweichender "
     "Zustand, wird grundsätzlich vermutet, dass die Ware schon bei Gefahrübergang mangelhaft war, Paragraf vierhundertsiebenundsiebzig. "
     "[erg]Hier ist das ohnehin klar: Die Grafikkarte war von Anfang an zu schwach. Der Laptop ist mangelhaft. "
     "[p437]Welche Rechte Kerstin jetzt hat, regelt Paragraf vierhundertsiebenunddreißig. Dazu gibt es eine eigene Folge.", PS),
    # --- J Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe alle drei Anforderungen in der Reihenfolge des Gesetzes, zuerst die Vereinbarung. "
     "[tipp2]Und schreib nie: Die Sache funktioniert, also ist sie mangelfrei.", PS),
    # --- K Klausurschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: Sachmangel nach Paragraf vierhundertvierunddreißig, maßgeblich bei Gefahrübergang. "
     "[k1]Römisch eins: subjektive Anforderungen, [k1a]also vereinbarte Beschaffenheit, vorausgesetzte Verwendung, "
     "vereinbartes Zubehör und Anleitungen. [k2]Römisch zwei: objektive Anforderungen, [k2a]also gewöhnliche Verwendung, "
     "übliche Beschaffenheit samt Werbung und erwartbares Zubehör.", P),
    ("[k3]Römisch drei: Montageanforderungen, falls montiert wird. [k4]Römisch vier: Gleichstellung der anderen Sache. "
     "[k5]Fehlt nur eine Anforderung, liegt ein Sachmangel vor.", PS),
    # --- L Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Mangelfrei ist eine Sache nur, wenn sie alle Anforderungen zugleich erfüllt. [m2]Funktioniert sie, "
     "aber nicht wie vereinbart, ist sie mangelhaft.", 1.4),
]
