"""Folge 101 · Formelle Verfassungsmäßigkeit: So entsteht ein Bundesgesetz (Mi · Examenswissen · Schema).
Beispielfall nach dem Hook des Themenplans („Ein Gesetz wird nachts ohne ordnungsgemäße Beteiligung des Bundesrats
beschlossen – ist es wirksam?“), Vorbild offengelegt: Zuwanderungsgesetz (BVerfG, Urt. v. 18.12.2002 – 2 BvF 1/02,
BVerfGE 106, 310; uneinheitliche Stimmabgabe eines Landes, Art. 51 Abs. 3 Satz 2 GG). Kurz vor Mitternacht beschließt der
Bundestag ein Gesetz, das den Meldebehörden der Länder ein digitales Verfahren ohne Abweichungsmöglichkeit vorschreibt
(zustimmungsbedürftig nach Art. 84 Abs. 1 Satz 6 GG). Im Bundesrat stimmen für ein Land Ministerin Hensel „Ja“ und Minister
Rieger „Nein“; der Bundesratspräsident wertet das als Ja. Ohne das Land fehlt die Mehrheit. Der Bundespräsident fertigt aus,
das Gesetz wird im (elektronischen) Bundesgesetzblatt verkündet. Frau Kähler arbeitet in einer Meldebehörde.
Schema der formellen Verfassungsmäßigkeit: I. Zuständigkeit (zwei Sätze, Verweis Folge 098), II. Verfahren: 1. Initiative
Art. 76, 2. Beschluss des Bundestages Art. 77 I 1 (Wortlautkarte), Art. 42 II, 3. Beteiligung des Bundesrates
(Einspruchs- oder Zustimmungsgesetz, Vermittlungsausschuss, Einspruch und Zurückweisung, Art. 78 als Wortlautkarte,
einheitliche Stimmabgabe Art. 51 III 2), III. Form (Gegenzeichnung, Ausfertigung, Verkündung Art. 82 I als Auszug,
elektronisches BGBl., Inkrafttreten Art. 82 II) → Ergebnis nichtig → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
Belege: ../RECHTSSTAND.md. Fiktive Figuren: der Bundesratspräsident (helmut), Frau Hensel (julia), Herr Rieger (niklas),
Frau Kähler (ela_froh, heitere Nebenrolle).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.3, 0.6

STIMMEN = {"Praesident": "helmut", "Hensel": "julia", "Rieger": "niklas", "Kaehler": "ela_froh"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall: Bundestag kurz vor Mitternacht ----------------------------------------------------------------------------
    ("[fall]Kurz vor Mitternacht im Bundestag. [entw]Die Bundesregierung hat einen Gesetzentwurf eingebracht, der Bundesrat "
     "hat dazu Stellung genommen. [gesetz]Jetzt wird beschlossen: Die Meldebehörden der Länder sollen Anträge nur noch "
     "digital bearbeiten, nach einem festen Verfahren, von dem kein Land abweichen darf. [leer]Der Saal ist ziemlich leer, "
     "aber niemand zweifelt die Beschlussfähigkeit an. [mehrheit]Die Mehrheit stimmt mit Ja.", 0.5),
    # --- B Fall: Bundesrat --------------------------------------------------------------------------------------------------
    ("[br]Einige Wochen später stimmt der Bundesrat ab. [land]Für ein Land sind Ministerin Hensel und Minister Rieger im "
     "Saal.", 0.3),
    ("[p1]Ich rufe das Land auf. Wie stimmt das Land ab?", 0.3, "Praesident"),
    ("[hen1]Für das Land: Ja.", 0.2, "Hensel"),
    ("[rie1]Und ich sage: Nein.", 0.3, "Rieger"),
    ("[p2]Das werte ich als Ja. Damit hat der Bundesrat zugestimmt.", 0.4, "Praesident"),
    ("[knapp]Ohne die vier Stimmen dieses Landes hätte es keine Mehrheit gegeben.", 0.5),
    # --- C Fall: Ausfertigung, Verkündung, Meldebehörde -----------------------------------------------------------------------
    ("[aus]Der Bundespräsident fertigt das Gesetz aus, [bgbl]und es wird im Bundesgesetzblatt verkündet, heute im Internet. "
     "[ka]Frau Kähler arbeitet in einer Meldebehörde.", 0.3),
    ("[ka1]Ab dem ersten März machen wir also alles digital!", 0.4, "Kaehler"),
    ("[frage]Aber ist das Gesetz überhaupt wirksam zustande gekommen? [vorbild]Vorbild ist das Zuwanderungsgesetz. Darüber hat "
     "das Bundesverfassungsgericht zweitausendzwei entschieden.", 0.6),
    # --- D Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.6),
    # --- E Einordnung, I. Zuständigkeit ----------------------------------------------------------------------------------------
    ("[einord]Du prüfst die formelle Verfassungsmäßigkeit des Bundesgesetzes: [zust]erst die Zuständigkeit, [verf]dann das "
     "Verfahren, [form]dann die Form. [komp]Die Zuständigkeit ist hier kein Problem: Das Meldewesen gehört nach Artikel "
     "dreiundsiebzig Absatz eins Nummer drei zur ausschließlichen Gesetzgebung des Bundes. [verw]Mehr dazu im Video "
     "zur Gesetzgebungskompetenz.", PS),
    # --- F II. 1. Initiative --------------------------------------------------------------------------------------------------
    ("[ini]Im Verfahren folgst du dem Weg des Gesetzes. Erstens: die Gesetzesinitiative, Artikel sechsundsiebzig Absatz eins. "
     "[ini2]Vorlagen bringen die Bundesregierung, der Bundesrat oder Abgeordnete aus der Mitte des Bundestages ein. "
     "[vor]Vorlagen der Bundesregierung gehen zuerst an den Bundesrat, [vor2]Vorlagen des Bundesrates über die "
     "Bundesregierung, beide haben in der Regel sechs Wochen Zeit. [ini3]Im Fall ist das so "
     "geschehen.", PS),
    # --- G II. 2. Beschluss des Bundestages, Wortlaut Art. 77 I 1 ----------------------------------------------------------------
    ("[bt]Zweitens: der Beschluss des Bundestages. Artikel siebenundsiebzig Absatz eins Satz eins: Die Bundesgesetze werden "
     "vom Bundestage beschlossen. [mehr]Nötig ist nach Artikel zweiundvierzig Absatz zwei die Mehrheit der abgegebenen "
     "Stimmen. [nacht]Dass es nachts ist, schadet nicht: Beschlussfähig ist der Bundestag nach seiner Geschäftsordnung, wenn "
     "mehr als die Hälfte seiner Mitglieder im Saal ist, gezählt wird aber erst, wenn etwa eine Fraktion das vor der "
     "Abstimmung bezweifelt. [bt2]Das hat hier niemand getan. Der Beschluss ist in Ordnung.", PS),
    # --- H II. 3. Bundesrat: Einspruchs- oder Zustimmungsgesetz ---------------------------------------------------------------
    ("[brt]Drittens: die Beteiligung des Bundesrates. Zuerst klärst du: Einspruchsgesetz oder Zustimmungsgesetz? "
     "[regel]Die Regel ist das Einspruchsgesetz. Zustimmungsbedürftig ist ein Gesetz nur, wenn das Grundgesetz es "
     "ausdrücklich anordnet. [b84]Zum Beispiel nach Artikel vierundachtzig Absatz eins Satz sechs, wenn der Bund den Ländern "
     "das Verwaltungsverfahren ohne Abweichungsmöglichkeit vorschreibt. [b84b]Genau das tut unser Gesetz. Es braucht die "
     "Zustimmung.", P),
    # --- I Ablauf: Vermittlungsausschuss, Einspruch, Zurückweisung, Wortlaut Art. 78 ---------------------------------------------
    ("[vma]Der Bundesrat kann binnen drei Wochen den Vermittlungsausschuss anrufen, Artikel "
     "siebenundsiebzig Absatz zwei. Bei Zustimmungsgesetzen dürfen das auch Bundestag und Bundesregierung. [ein]Beim "
     "Einspruchsgesetz kann der Bundesrat danach binnen zwei Wochen Einspruch einlegen. [zur]Den Einspruch kann der "
     "Bundestag zurückweisen, mit der Mehrheit seiner Mitglieder. War der Einspruch mit zwei Dritteln beschlossen, braucht "
     "auch der Bundestag zwei Drittel. [zug]Beim Zustimmungsgesetz dagegen muss der Bundesrat zustimmen.", P),
    ("[wl78]Artikel achtundsiebzig fasst zusammen, wann ein Gesetz zustande kommt: [z1]wenn der Bundesrat zustimmt, "
     "[z2]den Vermittlungsausschuss nicht anruft, [z3]keinen Einspruch einlegt oder ihn zurücknimmt, [z4]oder wenn der "
     "Bundestag den Einspruch überstimmt.", PS),
    # --- J Stimmabgabe, Wortlaut Art. 51 III 2 ------------------------------------------------------------------------------------
    ("[st]Der Bundesrat beschließt mit mindestens der Mehrheit seiner Stimmen, Artikel "
     "zweiundfünfzig Absatz drei. [wl51]Und nach Artikel einundfünfzig Absatz drei Satz zwei können die Stimmen eines "
     "Landes nur einheitlich abgegeben werden. [uneinh]Frau Hensel sagt ja, Herr Rieger sagt nein. Das ist nicht "
     "einheitlich. [nichtja]Der Präsident durfte diese Stimmen nicht als Ja werten. So hat das Bundesverfassungsgericht "
     "beim Zuwanderungsgesetz entschieden. [keine]Ohne das Land fehlt die Mehrheit. Der Bundesrat hat nicht zugestimmt, das "
     "Gesetz ist nicht zustande gekommen.", PS),
    # --- K III. Form, Auszug Art. 82 I ------------------------------------------------------------------------------------------
    ("[form1]Römisch drei: die Form. [wl82]Nach Artikel zweiundachtzig Absatz eins wird das Gesetz gegengezeichnet, vom "
     "Bundespräsidenten ausgefertigt und im Bundesgesetzblatt verkündet. [gegen]Gegenzeichnen muss der Bundeskanzler oder "
     "der zuständige Minister, Artikel achtundfünfzig. [pruef]Bei der Ausfertigung prüft der Bundespräsident, ob das "
     "Gesetz nach den Vorschriften des Grundgesetzes zustande gekommen ist. [ebgbl]Das Bundesgesetzblatt erscheint seit dem "
     "ersten Januar zweitausenddreiundzwanzig elektronisch im Internet, nach dem Verkündungs- und Bekanntmachungsgesetz. "
     "[inkr]In Kraft tritt es an dem Tag, den es bestimmt, sonst am vierzehnten Tag nach dem Tag der Ausgabe, "
     "Artikel zweiundachtzig Absatz zwei. [heil]Aber Ausfertigung und Verkündung heilen den Fehler im Bundesrat nicht.", PS),
    # --- L Ergebnis -------------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Das Gesetz wurde ohne wirksame Zustimmung des Bundesrates ausgefertigt. Es ist formell "
     "verfassungswidrig und nichtig. [erg2]So war es auch beim Zuwanderungsgesetz.", 0.3),
    ("[ka2]Ein Gesetz im Gesetzblatt, und trotzdem nichtig!", 0.6, "Kaehler"),
    # --- M Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Nicht jeder Verfahrensfehler macht ein Gesetz nichtig. [tipp1]Ein Verstoß nur gegen die "
     "Geschäftsordnung reicht in der Regel nicht. Es kommt darauf an, ob zugleich das Grundgesetz verletzt ist. [tipp2]Und "
     "ein Verfahrensverstoß gegen das Grundgesetz macht das Gesetz nach dem Bundesverfassungsgericht nur nichtig, "
     "wenn er evident ist. [tipp3]Hier ist er offensichtlich: Das Grundgesetz verlangt einheitliche Stimmen.", PS),
    # --- N Klausurschema: der Weg des Gesetzes ----------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: der Weg des Gesetzes. [s1]Römisch eins: Zuständigkeit. [s2]Römisch zwei: Verfahren, "
     "[s21]mit der Initiative, [s22]dem Beschluss des Bundestages [s23]und der Beteiligung des Bundesrates: Einspruch oder "
     "Zustimmung, [s24]Vermittlungsausschuss, [s25]einheitliche Stimmen. [s3]Römisch drei: Form, [s31]mit Gegenzeichnung, "
     "Ausfertigung und Verkündung. [s4]Dann das Ergebnis, [s5]und bei Fehlern die Frage "
     "nach der Nichtigkeit.", PS),
    # --- O Merksatz (Lexi) ----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein Zustimmungsgesetz kommt nur zustande, wenn der Bundesrat zustimmt. [m2]Dafür braucht es die "
     "Mehrheit seiner Stimmen, und jedes Land kann nur einheitlich abstimmen.", 1.1),
]
