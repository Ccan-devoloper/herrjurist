"""Folge 072 · Verfahrensrüge § 344 II 2 StPO: Warum so viele scheitern (Fr · 2. Examen · StPO-Praxis, Format Klausurfehler).
Fall nach dem Plan-Hook („Die Revisionsbegründung rügt die Ablehnung eines Beweisantrags, gibt aber den Ablehnungsbeschluss
nicht wieder“): Das Landgericht verurteilt Herrn Bachmann wegen Betrugs (Gebrauchtwagen mit falschem Tachostand). Den Antrag
seiner Verteidigerin, Rechtsanwältin Hellwig, die Vorbesitzerin Frau Haase als Zeugin zu vernehmen, lehnt die Kammer durch
Beschluss wegen Bedeutungslosigkeit ab (§ 244 III 3 Nr. 2 StPO). Die Revisionsbegründung nennt die Ablehnung rechtsfehlerhaft,
gibt aber weder Antrag noch Beschluss wieder und verweist auf das Protokoll; die Begründungsfrist ist abgelaufen.
Kern als Fehleranalyse, anknüpfend an Folge 066 (Sachrüge nur ein Satz): Wortlaut § 344 II StPO → Maßstab (BGH 1 StR 481/24
Rn. 9) → Checkliste (Antrag/Beschluss, Bezugnahmen, nachteilige Umstände, Beruhen, Frist, Widerspruch) → Ergebnis →
korrigierte Fassung (Verfahrenstatsachen – Rechtsfehler – Beruhen) als Klausurkonvention → Klausurtipp → Schema → Merksatz.
Belege je Aussage: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben:
Bachmann, Hellwig, Haase; der Richter am Bundesgerichtshof bleibt ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Richter": "william", "Hellwig": "laura_ruhig", "Bachmann": "marc"}  # Lexi = Erzählerin (Carla); Frau Haase spricht nicht

SEGMENTE = [
    # --- A Fall: am Bundesgerichtshof ------------------------------------------------------------------------------------------
    ("[fall]Karlsruhe, am Bundesgerichtshof. [akte]Ein Richter des Strafsenats liest die Revisionsbegründung für Herrn "
     "Bachmann. [zitat]Darin steht: Die Ablehnung des Beweisantrags auf Vernehmung der Zeugin Haase war rechtsfehlerhaft. "
     "[zitat2]Wegen der Einzelheiten wird auf das Protokoll verwiesen.", 0.3),
    ("[r1]Und wo sind der Antrag und der Ablehnungsbeschluss?", 0.4, "Richter"),
    # --- B Fall: Rückblick in die Kanzlei ---------------------------------------------------------------------------------------
    ("[zurueck]Vier Wochen vorher, in der Kanzlei von Rechtsanwältin Hellwig. [lg]Das Landgericht hat ihren Mandanten, "
     "Herrn Bachmann, wegen Betrugs verurteilt. [auto]Er hatte einen Gebrauchtwagen mit sechzigtausend Kilometern verkauft. "
     "Tatsächlich waren es hundertsechzigtausend. [antrag]In der Hauptverhandlung beantragte die Verteidigerin, die "
     "Vorbesitzerin, Frau Haase, als Zeugin dafür zu vernehmen, dass der Tacho schon bei der Übergabe an Herrn Bachmann "
     "sechzigtausend Kilometer zeigte. [beschl]Die Kammer lehnte das durch Beschluss ab: Die Tatsache sei für die "
     "Entscheidung ohne Bedeutung.", 0.3),
    ("[b1]Reicht es, wenn wir die Ablehnung in der Revision nur rügen?", 0.4, "Bachmann"),
    ("[h1]Das steht doch alles im Protokoll. Darauf verweise ich.", 0.4, "Hellwig"),
    # --- C Fall: zurück am Bundesgerichtshof ------------------------------------------------------------------------------------
    ("[frist]Inzwischen ist die Begründungsfrist abgelaufen. [frage]Warum scheitert diese Verfahrensrüge? "
     "[frage2]Und wie hätte Rechtsanwältin Hellwig sie schreiben müssen?", 0.6),
    # --- D Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Verfahrensrüge und § 344 II StPO ------------------------------------------------------------------------------------
    ("[sach]Für die Sachrüge genügt ein Satz, aber sie prüft nur das Urteil selbst. [verf]Die Ablehnung des Beweisantrags "
     "ist aber ein Vorgang der Hauptverhandlung. Das ist ein Fall für die Verfahrensrüge. [p344]Paragraf "
     "dreihundertvierundvierzig Absatz zwei verlangt zuerst, dass die Begründung zeigt, ob eine Rechtsnorm über das "
     "Verfahren oder eine andere Rechtsnorm verletzt sein soll. [p344b]Dann Satz zwei: Ersterenfalls müssen die den Mangel enthaltenden Tatsachen "
     "angegeben werden.", PS),
    # --- F Der Maßstab ------------------------------------------------------------------------------------------------------------
    ("[mass]Was heißt das genau? [bgh]Nach dem Bundesgerichtshof muss das Revisionsgericht allein anhand der "
     "Begründungsschrift prüfen können, ob ein Verfahrensfehler vorliegt, wenn die behaupteten Tatsachen bewiesen werden. "
     "[allein]Allein heißt: Der Senat sucht nichts in den Akten zusammen. [wenn]Und er prüft so, als stimme dein Vortrag. "
     "Ob er stimmt, ist erst eine Frage der Begründetheit.", PS),
    # --- G Checkliste: typische Fehler -------------------------------------------------------------------------------------------
    ("[liste]Genau daran scheitern viele Rügen. Hier ist die Checkliste der typischen Fehler.", 0.3),
    ("[c1]Erstens: Antrag und Beschluss fehlen. [c1b]Wer die Ablehnung eines Antrags rügt, muss regelmäßig den Antrag und "
     "die Ablehnungsbegründung vollständig mitteilen, im Wortlaut oder in eigenen Worten. [c1c]Bei Rechtsanwältin Hellwig "
     "fehlt beides. Ohne den Beschluss kann der Senat nicht prüfen, ob die Begründung der Kammer trägt.", P),
    ("[c2]Zweitens: Verweise statt Vortrag. [c2b]Ein Verweis auf das Protokoll oder die Akten genügt nicht. [c2c]Was es "
     "braucht, gehört wörtlich oder als Abschrift in die Begründungsschrift.", P),
    ("[c3]Drittens: verschwiegene Umstände. [c3b]Vorzutragen ist auch, was gegen die Rüge spricht. [c3c]Wer Ungünstiges "
     "weglässt, macht seine Rüge unzulässig.", P),
    ("[c4]Viertens: das Beruhen. [c4b]Dazu muss die Begründung grundsätzlich nichts sagen. [c4c]Liegt das Beruhen aber "
     "nicht auf der Hand, gehören die Tatsachen hinein, mit denen der Senat es prüfen kann.", P),
    ("[c5]Fünftens: die Frist. [c5b]Alle Tatsachen müssen innerhalb der Begründungsfrist vorgetragen sein, Paragraf "
     "dreihundertfünfundvierzig Absatz eins. [c5c]Was danach kommt, rettet die Rüge nicht. Rechtsanwältin Hellwig kann den "
     "Beschluss nicht mehr nachreichen.", P),
    ("[c6]Sechstens: Verlangt die Rechtsprechung einen Widerspruch in der Hauptverhandlung, etwa gegen die Verwertung einer "
     "Aussage ohne Belehrung, gehört auch der rechtzeitige Widerspruch in den Vortrag.", PS),
    # --- H Ergebnis im Fall ----------------------------------------------------------------------------------------------------
    ("[erg]Für Herrn Bachmann heißt das: Die Verfahrensrüge ist unzulässig. [offen]Ob die Kammer den Antrag zu Recht "
     "abgelehnt hat, muss der Senat dann nicht mehr entscheiden.", PS),
    # --- I Die korrigierte Fassung (Klausurkonvention) -------------------------------------------------------------------------
    ("[besser]So hätte die Rüge aussehen müssen, aufgebaut nach Klausurkonvention in drei Schritten. [k1]Erstens die "
     "Verfahrenstatsachen: der Beweisantrag im Wortlaut, wann er gestellt wurde, [k1b]der Ablehnungsbeschluss im Wortlaut, "
     "und dass Frau Haase bis zum Urteil nicht vernommen wurde. [k2]Zweitens der Rechtsfehler: warum die Ablehnung als "
     "bedeutungslos Paragraf zweihundertvierundvierzig Absatz drei verletzt. [k3]Drittens das Beruhen: Hätte Frau Haase "
     "die Beweistatsache bestätigt, wäre das Urteil möglicherweise anders ausgefallen.", PS),
    # --- J Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Lies deine Rüge wie ein Senat, der nur diese Seiten hat. [tipp2]Fehlt ein Schriftstück, auf das "
     "es ankommt, gehört es hinein. [tipp3]Und jede Verfahrensrüge muss aus sich heraus verständlich sein, mit ihrem "
     "eigenen Vortrag.", PS),
    # --- K Schema ----------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für eine Verfahrensrüge. [s1]Erstens die Verfahrenstatsachen: vollständig, Anträge und Beschlüsse "
     "im Wortlaut, auch was gegen dich spricht. [s2]Zweitens der Rechtsfehler, mit der verletzten Norm. [s3]Drittens das "
     "Beruhen, mit Tatsachen, wo es nicht auf der Hand liegt. [s4]Und alles innerhalb der Begründungsfrist.", PS),
    # --- L Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Bei der Verfahrensrüge liest der Senat nur deine Begründung. [mz]Was dort nicht steht, prüft er nicht.", 1.4),
]
