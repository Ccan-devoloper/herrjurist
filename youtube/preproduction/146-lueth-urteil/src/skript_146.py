"""Folge 146 · Lüth-Urteil: Mittelbare Drittwirkung der Grundrechte erklärt (Mi · Examenswissen · Klassiker-Fall;
Art. 1 III, 5 I, II GG; § 826 BGB). Echter Fall sachlich nacherzählt: BVerfG, Urt. v. 15.1.1958 – 1 BvR 400/51,
BVerfGE 7, 198 (Lüth), Volltext DFR (servat.unibe.ch/dfr/bv007198.html), Seiten der amtlichen Sammlung <…>.
Prüfungsmaßstab „spezifisches Verfassungsrecht“: BVerfGE 18, 85 <92> (Beschl. v. 10.6.1964 – 1 BvR 37/63).
SENSIBEL: Erich Lüth und Veit Harlan treten nicht als Figuren auf; keine NS-Symbole, keine Filmbilder, keine Plakate,
nichts aus dem Film „Jud Süß“ gezeigt oder zitiert – nur sachlich benannt (BVerfGE 7, 198 <199, 222>).
Moderner Einstieg mit fiktiven Figuren: Wenke (Bloggerin, Stimme lucy) und Herr Gerstner (Filmproduzent, Stimme stephan).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter. Belege je Cue: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Wenke": "lucy", "Gerstner": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Moderner Einstieg (fiktiv) ------------------------------------------------------------------------------------
    ("[fall]Wenke schreibt einen Filmblog. [neu]Über einen neuen Kinofilm schreibt sie:", P),
    ("[w1]Dieser Film verherrlicht illegale Autorennen. Schaut ihn euch nicht an!", P, "Wenke"),
    ("[gerst]Der Produzent, Herr Gerstner, fürchtet um seinen Kinostart.", P),
    ("[g1]Ihr Aufruf kostet uns Zuschauer. Ich verklage Sie auf Unterlassung.", P, "Gerstner"),
    ("[frage0]Zwei Private streiten vor einem Zivilgericht. Gelten die Grundrechte auch zwischen ihnen? "
     "[klassiker]Diese Frage hat das Bundesverfassungsgericht im Lüth-Urteil beantwortet.", PS),
    # --- B Der echte Fall (BVerfGE 7, 198 <199–202>) ------------------------------------------------------------------
    ("[lueth]Hamburg, zwanzigster September neunzehnhundertfünfzig. [rede]Erich Lüth, Senatsdirektor und Vorsitzender "
     "des Hamburger Presseklubs, spricht vor Filmverleihern und Filmproduzenten. [harlan]Er wendet sich gegen das "
     "Wiederauftreten des Regisseurs Veit Harlan, [jud]der in der Zeit des Nationalsozialismus den antisemitischen Film "
     "Jud Süß gedreht hatte. [brief]In einem offenen Brief ruft Lüth dazu auf, sich gegen Harlan auch zum Boykott "
     "bereitzuhalten. [film]Harlans neuer Film heißt Unsterbliche Geliebte.", P),
    ("[klage]Die Produktionsfirma und die Verleiherin klagen. [lg]Am zweiundzwanzigsten November neunzehnhunderteinundfünfzig "
     "verurteilt das Landgericht Hamburg Lüth zur Unterlassung. [sitten]Der Boykottaufruf sei sittenwidrig nach Paragraf achthundertsechsundzwanzig BGB, "
     "[frei]denn Harlan sei rechtskräftig freigesprochen und dürfe seinen Beruf wieder ausüben. [vb]Lüth erhebt "
     "Verfassungsbeschwerde.", P),
    ("[frage]Welche Rolle spielt die Meinungsfreiheit in einem Streit unter Privaten?", PS),
    # --- C Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Grundrechte im Privatrecht (<204–207>) ----------------------------------------------------------------------
    ("[urteil]Am fünfzehnten Januar neunzehnhundertachtundfünfzig entscheidet das Bundesverfassungsgericht. "
     "[abwehr]Die Grundrechte sind in erster Linie Abwehrrechte des Bürgers gegen den Staat. [wert]Aber das Grundgesetz "
     "hat in seinem Grundrechtsabschnitt auch eine objektive Wertordnung aufgerichtet. [alle]Sie gilt als "
     "verfassungsrechtliche Grundentscheidung für alle Bereiche des Rechts, [buerg]auch für das bürgerliche Recht: "
     "Jede Vorschrift muss in ihrem Geist ausgelegt werden.", P),
    ("[medium]Im Privatrecht wirken die Grundrechte durch das Medium der privatrechtlichen Vorschriften; [bleibt]der "
     "Streit bleibt ein bürgerlicher Rechtsstreit. [einbruch]Einbruchstellen sind vor allem die Generalklauseln, wie die "
     "guten Sitten in Paragraf achthundertsechsundzwanzig. [mittelbar]Man spricht von mittelbarer Drittwirkung.", P),
    ("[a13]Wer ist dann unmittelbar gebunden? Artikel eins Absatz drei: Die nachfolgenden Grundrechte binden "
     "Gesetzgebung, vollziehende Gewalt und Rechtsprechung als unmittelbar geltendes Recht. [richter]Gebunden ist also "
     "der Zivilrichter. [verkennt]Verkennt er den Einfluss der Grundrechte, "
     "verletzt er als Träger öffentlicher Gewalt durch sein Urteil das Grundrecht.", P),
    ("[kontrast]Anders im Fraport-Fall: Dort war der Staat Mehrheitsaktionär und das Unternehmen deshalb selbst "
     "unmittelbar gebunden. [privatmann]Lüth dagegen war zwar Senatsdirektor, sprach aber als Privatmann.", PS),
    # --- E Art. 5 GG und Wechselwirkung (<207–212>) --------------------------------------------------------------------
    ("[a5]Artikel fünf Absatz eins schützt das Recht, seine Meinung in Wort, Schrift und Bild frei zu äußern und zu "
     "verbreiten. [a52]Absatz zwei: Diese Rechte finden ihre Schranken in den Vorschriften der allgemeinen Gesetze. "
     "[wirkung]Geschützt ist auch die Wirkung der Äußerung: Wer ein Werturteil fällt, will andere überzeugen. "
     "[allg]Und auch Paragraf achthundertsechsundzwanzig BGB ist ein allgemeines Gesetz.", P),
    ("[g2]Aber Paragraf achthundertsechsundzwanzig schützt doch auch mein Geschäft.", P, "Gerstner"),
    ("[wechsel]Nach seinem Wortlaut setzt er dem Grundrecht eine Schranke. [licht]Aber er muss seinerseits im Licht der "
     "Meinungsfreiheit ausgelegt werden und wird so in seiner begrenzenden Wirkung selbst wieder eingeschränkt. "
     "[ww]Das Gericht nennt das eine Wechselwirkung.", P),
    ("[abw]Am Ende steht eine Güterabwägung auf Grund aller Umstände des Falles. [verm]Geht es um einen Beitrag zum "
     "geistigen Meinungskampf in einer die Öffentlichkeit wesentlich berührenden Frage durch einen dazu Legitimierten, spricht die Vermutung für die "
     "Zulässigkeit der freien Rede.", PS),
    # --- F Abwägung im Fall Lüth (<215–221>) ---------------------------------------------------------------------------
    ("[motiv]So bei Lüth: Er verfolgte keine eigenen wirtschaftlichen Interessen und stand mit den Filmgesellschaften "
     "nicht in Konkurrenz. [sorge]Er sorgte sich um das Ansehen Deutschlands in der Welt. [zwang]Zwangsmittel hatte er keine; er appellierte nur an die "
     "freie Entscheidung der Angesprochenen. [erwidern]Und wer sich angegriffen fühlt, kann öffentlich "
     "erwidern.", P),
    # --- G Prüfungsmaßstab der Urteilsverfassungsbeschwerde (<207, 214 f.>) ---------------------------------------------
    ("[pruef]Was prüft das Bundesverfassungsgericht bei einem Zivilurteil? [superrev]Nicht jeden Rechtsfehler: Es ist "
     "keine Superrevisionsinstanz. [ausstr]Es prüft, ob das Zivilgericht die Ausstrahlungswirkung der Grundrechte auf "
     "das bürgerliche Recht richtig beurteilt hat.", P),
    ("[erg]Ergebnis: Das Landgericht hat die besondere Bedeutung der Meinungsfreiheit verkannt. [aufh]Sein Urteil "
     "verletzt Lüth in seinem Grundrecht aus Artikel fünf Absatz eins Satz eins und wird aufgehoben. [zurueck]Die Sache "
     "geht zurück an das Landgericht.", PS),
    # --- H Zurück zum Einstieg ---------------------------------------------------------------------------------------------
    ("[w2]Darf ich also zum Boykott aufrufen, auch wenn es dem Film schadet?", P, "Wenke"),
    ("[h1]Auch über diese Klage entscheidet ein Zivilgericht, gebunden an die Meinungsfreiheit. [h2]Verfolgt Wenke "
     "keine eigenen wirtschaftlichen Ziele, äußert sie sich zu einer öffentlichen Frage und hat sie keine Zwangsmittel, "
     "[h3]dann spricht in der Abwägung viel für ihre freie Rede. [h4]Herr Gerstner kann öffentlich widersprechen.", PS),
    # --- I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bei der Urteilsverfassungsbeschwerde ist Prüfungsmaßstab nur das spezifische Verfassungsrecht. "
     "Frag nicht, ob das Zivilrecht richtig angewendet wurde, [tipp2]sondern ob das Gericht Bedeutung und Reichweite des "
     "Grundrechts verkannt hat.", PS),
    # --- J Prüfschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für die Begründetheit. [k1]Römisch eins: Schutzbereich, Artikel fünf Absatz eins Satz eins, "
     "auch für den Boykottaufruf. [k2]Römisch zwei: Eingriff durch das Zivilurteil als Akt öffentlicher Gewalt. "
     "[k3]Römisch drei: Rechtfertigung. Schranke ist ein allgemeines Gesetz, hier Paragraf achthundertsechsundzwanzig. "
     "[k4]Dann die Wechselwirkung: Auslegung im Licht der Meinungsfreiheit [k5]und Abwägung aller Umstände. "
     "[k6]Maßstab bleibt: Hat das Gericht die Ausstrahlungswirkung verkannt?", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Zwischen Privaten wirken die Grundrechte mittelbar, über die Generalklauseln und über den Richter. "
     "[m2]Und bei einem Beitrag zum Meinungskampf in einer wesentlichen öffentlichen Frage spricht die Vermutung für die freie Rede.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
