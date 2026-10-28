"""Folge 025 · Auschwitzlüge: Warum sie nicht von der Meinungsfreiheit geschützt ist (Art. 5 I, II GG).
Echter Fall sachlich nacherzählt: BVerfG, Beschl. v. 13.4.1994 – 1 BvR 23/94 (BVerfGE 90, 241), Auflage der Landeshauptstadt
München für eine Versammlung am 12.5.1991 (§ 5 Nr. 4 VersG). Heutige Rechtslage: § 130 Abs. 3 StGB; BVerfG (Kammer),
Beschl. v. 22.6.2018 – 1 BvR 673/18 und 1 BvR 2083/15; Wunsiedel-Beschluss BVerfGE 124, 300 (§ 130 Abs. 4 StGB).
Veranstalter, Redner, Richter und Politiker treten nicht als Figuren auf und werden nicht genannt. Fiktive Figuren:
Herr Möller (Versammlungsbehörde, Behördenfigur), Svenja (Referendarin in der Verwaltungsstation).
Würde und Zurückhaltung: keine leugnende Aussage wörtlich; nur abstrakt („die Judenverfolgung leugnen“).
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.9

STIMMEN = {"Moeller": "william", "Svenja": "julia"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Versammlungsbehörde -------------------------------------------------------------------------
    ("[fall]München, Frühjahr neunzehnhunderteinundneunzig. [einl]Ein Parteiverband lädt zu einer Versammlung in einen "
     "Saal ein. [erwart]Nach Einladung und Redner erwartet die Stadt, dass dort die Judenverfolgung im Dritten Reich "
     "geleugnet wird.", 0.3),
    ("[moeller]Herr Möller von der Versammlungsbehörde bespricht das mit der Referendarin Svenja.", 0.2),
    ("[m1]Wir erteilen eine Auflage. Auf der Versammlung darf die Judenverfolgung nicht geleugnet werden.", 0.3, "Moeller"),
    ("[auflage]Der Verband soll zu Beginn auf die Strafbarkeit hinweisen, solche Beiträge sofort unterbinden und "
     "notfalls die Versammlung auflösen.", 0.2),
    ("[s1]Darf der Staat vorschreiben, was auf einer Versammlung gesagt wird? Es gibt doch die Meinungsfreiheit.", 0.4,
     "Svenja"),
    # --- B Fall: der Weg nach Karlsruhe ---------------------------------------------------------------------------
    ("[klage]Die Versammlung findet statt. Danach klagt der Verband erfolglos durch drei Instanzen. [vb]Dann "
     "erhebt er Verfassungsbeschwerde. [frage]Verletzt die Auflage die Meinungsfreiheit? Und ist die sogenannte "
     "Auschwitzlüge überhaupt eine Meinung?", 0.6),
    # --- C Sachverhalt --------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Maßstab und Wortlaut Art. 5 I 1 GG ---------------------------------------------------------------------
    ("[mass]Maßstab ist vorrangig die Meinungsfreiheit, nicht die Versammlungsfreiheit. [gegenst]Denn die Auflage "
     "betrifft bestimmte Äußerungen.", P),
    ("[wl5]Artikel fünf Absatz eins Satz eins: Jeder hat das Recht, seine Meinung in Wort, Schrift und Bild frei zu "
     "äußern und zu verbreiten.", P),
    # --- E I. Schutzbereich: Meinung und Tatsache -----------------------------------------------------------------
    ("[sb]Römisch eins: der Schutzbereich. [meinung]Meinungen sind durch Stellungnahme und Dafürhalten geprägt. Sie "
     "lassen sich nicht als wahr oder unwahr erweisen. [egal]Geschützt sind sie, ob begründet oder grundlos, wertvoll "
     "oder wertlos.", P),
    ("[tats]Tatsachenbehauptungen dagegen lassen sich auf ihren Wahrheitsgehalt prüfen. [vor]Geschützt sind auch sie, "
     "soweit sie Voraussetzung für die Bildung von Meinungen sind. [grenze]Der Schutz endet bei bewusst oder erwiesen "
     "unwahren Tatsachenbehauptungen. Unrichtige Information ist kein schützenswertes Gut. [pflicht]Die Wahrheitspflicht "
     "darf man aber nicht überspannen.", P),
    ("[misch]Oft sind Tatsache und Wertung verbunden. [trenn]Trennen darf man sie nur, wenn der Sinn der Äußerung "
     "nicht verfälscht wird. [ganz]Sonst gilt die ganze Äußerung als Meinung.", PS),
    # --- F Subsumtion und Gegenbeispiel ---------------------------------------------------------------------------
    ("[subs]Und hier? Wer die Judenverfolgung im Dritten Reich leugnet, stellt eine Tatsachenbehauptung auf. "
     "[belegt]Sie ist erwiesen unwahr: [b1]durch ungezählte Augenzeugenberichte und Dokumente, [b2]durch die "
     "Feststellungen der Gerichte [b3]und durch die Erkenntnisse der Geschichtswissenschaft. "
     "[nicht]Für sich genommen schützt sie die Meinungsfreiheit also nicht.", P),
    ("[schuld]Anders bei der Schuld am Zweiten Weltkrieg: Urteile über Schuld und Verantwortung sind "
     "komplexe Beurteilungen. [ereig]Wer dagegen ein Ereignis selbst leugnet, behauptet in aller Regel eine Tatsache.", PS),
    # --- G Hilfsweise: Eingriff und Rechtfertigung ----------------------------------------------------------------
    ("[hilfs]Das Gericht prüft trotzdem weiter: Im Zusammenhang mit dem Versammlungsthema kann die Äußerung Teil "
     "einer Meinung sein, und dann ist sie geschützt. [ein]Römisch zwei: Die Auflage ist dann ein Eingriff.", P),
    ("[wl52]Römisch drei: die Rechtfertigung. Artikel fünf Absatz zwei: Diese Rechte finden ihre Schranken in den "
     "Vorschriften der allgemeinen Gesetze, den gesetzlichen Bestimmungen zum Schutze der Jugend und in dem Recht der "
     "persönlichen Ehre.", P),
    ("[grundl]Grundlage der Auflage war Paragraf fünf Nummer vier des Versammlungsgesetzes. [vers]Danach kann "
     "eine Versammlung in geschlossenen Räumen verboten werden, wenn dort Äußerungen drohen, die als Straftat von Amts "
     "wegen verfolgt werden. Die Auflage ist das mildere Mittel. [streng]Weil die Behörde vorbeugend eingreift, verlangt das Gericht eine "
     "strenge Gefahrenprognose und eine zweifelsfreie Strafbarkeit.", P),
    ("[ehre]Als Strafnorm genügt dem Gericht die Beleidigung, Paragraf hundertfünfundachtzig, also das Recht der "
     "persönlichen Ehre. [gruppe]Nach der Rechtsprechung der "
     "Strafgerichte sind die in Deutschland lebenden Juden eine beleidigungsfähige Gruppe. [wuerde]Die Leugnung ihres Verfolgungsschicksals greift "
     "ihren Achtungsanspruch und ihre Menschenwürde an. [antrag]Einen Strafantrag braucht es dafür nicht.", P),
    ("[abw]Bleibt die Abwägung. [leicht]Weil der Tatsachenkern erwiesen unwahr ist, wiegt der Eingriff nicht besonders "
     "schwer. Der Persönlichkeitsschutz geht vor. [verm]Zwar spricht bei Fragen, die die Öffentlichkeit wesentlich "
     "berühren, eine Vermutung für die freie Rede. [vnicht]Sie greift aber nicht bei kränkenden Äußerungen, die auf "
     "erwiesen unwahren Tatsachen beruhen.", P),
    ("[erg]Am dreizehnten April neunzehnhundertvierundneunzig verwirft das Gericht die Verfassungsbeschwerde als "
     "offensichtlich unbegründet. [offen]Ob sie zulässig war, lässt es offen.", PS),
    # --- H Rechtslage heute: Wortlaut § 130 III StGB, Wunsiedel ---------------------------------------------------
    ("[heute]Heute ist die Leugnung eigens strafbar, nach Paragraf hundertdreißig Absatz drei. "
     "[wl130]Bestraft wird, wer den Völkermord unter der Herrschaft des Nationalsozialismus öffentlich oder in einer "
     "Versammlung billigt, leugnet oder verharmlost, in einer Weise, die geeignet ist, den öffentlichen Frieden "
     "zu stören.", P),
    ("[sonder]Ein allgemeines Gesetz ist das nicht, denn es erfasst nur Äußerungen zum Nationalsozialismus. "
     "[wuns]Der Wunsiedel-Beschluss erkennt dafür eine Ausnahme an, zunächst für Absatz vier. [kammer]Eine Kammer "
     "übertrug sie zweitausendachtzehn auf Absatz drei. [geist]Rechtsradikales Gedankengut allein wegen seiner geistigen "
     "Wirkung zu verbieten, erlaubt das Grundgesetz aber nicht. [frieden]Nötig ist, dass die Äußerung den öffentlichen "
     "Frieden gefährdet. Bei der Leugnung ist das in der Regel indiziert.", PS),
    # --- I Klausurtipp (Lexi) -------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Ob Tatsache oder Meinung, entscheidest du am Gesamtkontext der Äußerung. [tipp1]Den "
     "Schutzbereich verneinst du nur für die erwiesen unwahre Tatsache selbst. [tipp2]Kannst du sie nicht sauber von der "
     "Wertung trennen, prüfst du weiter die Rechtfertigung.", PS),
    # --- J Klausurschema ------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Römisch eins, Schutzbereich: [k1a]Meinung oder Tatsachenbehauptung, [k1b]erwiesen "
     "unwahre Tatsache nicht geschützt, [k1c]bei untrennbarer Verbindung insgesamt Meinung. [k2]Römisch zwei: Eingriff. "
     "[k3]Römisch drei, Rechtfertigung: [k3a]Schranke aus Artikel fünf Absatz zwei, [k3b]bei Paragraf hundertdreißig "
     "Absatz drei die Wunsiedel-Ausnahme, [k3c]dann die Abwägung im Einzelfall.", PS),
    # --- K Merksatz (Lexi) ----------------------------------------------------------------------------------------
    ("[merke]Merke: Meinungen schützt Artikel fünf, ob wertvoll oder wertlos. [m2]Die erwiesen unwahre "
     "Tatsachenbehauptung selbst, wie die Leugnung des Holocaust, schützt er nicht.", 1.4),
]
