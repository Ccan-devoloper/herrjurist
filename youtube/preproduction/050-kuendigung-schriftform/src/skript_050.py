"""Folge 050 · Kündigung per WhatsApp wirksam? Schriftform nach § 623 BGB (Mi · Examenswissen, Format Klausurfehler).
Übungsfall nach dem Plan-Hook: Frau Kuhlmann, Inhaberin einer Fahrradwerkstatt, unterschreibt die Kündigung ihres
Mechanikers Bastian, fotografiert das Schreiben und schickt das Foto per WhatsApp; das Original bleibt im Ordner.
Fünf Wochen später klagt Bastian; Frau Kuhlmann beruft sich auf die Klagefrist (§§ 4, 7 KSchG).
Prüfung der Wirksamkeit: I. Kündigungserklärung, II. Schriftform (§ 623 BGB, Wortlaut; § 126 I BGB, Wortlaut; Zugang
des Originals; Foto/Fax/Scan/E-Mail; § 125 S. 1), III. Zugang (§ 130, Original), IV. Vertretung (§ 174, Ausblick mit
Werkstattleiterin Frau Petersen), V. Klagefrist (§ 4 S. 1 KSchG, Wortlaut: „schriftlichen“ Kündigung; § 7 KSchG).
Rechtsstand 02.10.2026: § 623 BGB unverändert (elektronische Form ausgeschlossen), BEG IV 2024 hat § 623 nicht geändert.
Belege je Aussage: ../RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) =
Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor. Keine Genitivformen der Namen."""

P, PS = 0.4, 0.9

STIMMEN = {"Kuhlmann": "hilde", "Bastian": "timo", "Petersen": "lea"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: das Foto in der Werkstatt ---------------------------------------------------------------------------
    ("[fall]Frau Kuhlmann führt eine kleine Fahrradwerkstatt. [unterschr]Am Freitagabend unterschreibt sie die Kündigung "
     "ihres Mechanikers Bastian. [foto]Dann fotografiert sie das Schreiben mit dem Handy.", 0.3),
    ("[ku1]Das Foto schicke ich ihm per WhatsApp. Das Original kommt in den Ordner.", 0.4, "Kuhlmann"),
    # --- B Fall: Bastian liest die Nachricht -----------------------------------------------------------------------------
    ("[whats]Bastian sieht die Nachricht sofort.", 0.3),
    ("[b1]Gekündigt per WhatsApp? Das kann doch nicht wirksam sein!", 0.4, "Bastian"),
    # --- C Fall: fünf Wochen später, die Frage ---------------------------------------------------------------------------
    ("[wochen]Fünf Wochen später erhebt Bastian Klage beim Arbeitsgericht.", 0.3),
    ("[ku2]Zu spät! Nach drei Wochen gilt die Kündigung als wirksam.", 0.4, "Kuhlmann"),
    ("[frage]Hat das Foto per WhatsApp das Arbeitsverhältnis beendet? Und lief überhaupt eine Klagefrist?", 0.6),
    # --- D Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Prüfungsaufbau ---------------------------------------------------------------------------------------------------
    ("[pruef]Wir prüfen die Wirksamkeit der Kündigung: [glied]Kündigungserklärung, Schriftform, Zugang, Vertretung und "
     "am Ende die Klagefrist.", PS),
    # --- F I. Kündigungserklärung -----------------------------------------------------------------------------------------
    ("[erkl]Römisch eins: die Kündigungserklärung. [erkl_ok]Frau Kuhlmann will das Arbeitsverhältnis erkennbar beenden. "
     "Das ist eindeutig.", PS),
    # --- G II. Schriftform: Wortlaut § 623, Zweck, Rechtsstand ---------------------------------------------------------------
    ("[form]Römisch zwei: die Schriftform. [p623]Paragraf sechshundertdreiundzwanzig: Die Beendigung von "
     "Arbeitsverhältnissen durch Kündigung oder Auflösungsvertrag bedürfen zu ihrer Wirksamkeit der Schriftform; die "
     "elektronische Form ist ausgeschlossen. [zweck]Die Schriftform soll Rechtssicherheit schaffen, den Beweis "
     "erleichtern und eine bewusste Hürde vor die Kündigung setzen. [stand]Der Wortlaut gilt bis heute unverändert. "
     "Das Vierte Bürokratieentlastungsgesetz von zweitausendvierundzwanzig hat andere Formvorschriften gelockert, etwa "
     "beim Arbeitszeugnis, Paragraf sechshundertdreiundzwanzig aber nicht.", PS),
    # --- H II. Schriftform: Wortlaut § 126 I, Zugang der Urkunde -------------------------------------------------------------
    ("[p126]Was Schriftform heißt, sagt Paragraf hundertsechsundzwanzig Absatz eins: Die Urkunde muss von dem Aussteller "
     "eigenhändig durch Namensunterschrift unterzeichnet werden. [zugeh]Und weil die Kündigung empfangsbedürftig ist, "
     "muss genau diese unterschriebene Urkunde dem Arbeitnehmer zugehen.", PS),
    # --- I II. Schriftform: Foto, Fax, E-Mail; Rechtsfolge --------------------------------------------------------------------
    ("[subs]Bastian hat nur ein Foto bekommen. [abbild]Es zeigt die Unterschrift bloß als Abbild, das Original liegt im "
     "Ordner. [fax]Nach dem Bundesarbeitsgericht genügt schon ein Fax nicht, weil es nur eine Ablichtung der Unterschrift "
     "wiedergibt. [mail]Für Foto, Scan und E-Mail gilt dasselbe, und die elektronische Form schließt Paragraf "
     "sechshundertdreiundzwanzig ohnehin aus.", P),
    ("[nichtig]Die Schriftform ist nicht gewahrt. Nach Paragraf hundertfünfundzwanzig Satz eins ist die Kündigung "
     "nichtig. [treu]Ausnahmen über Treu und Glauben sind selten: Ein Formmangel ist nur ganz ausnahmsweise unbeachtlich, wenn "
     "das Ergebnis schlechthin untragbar wäre.", PS),
    # --- J III. Zugang ----------------------------------------------------------------------------------------------------------
    ("[zug]Römisch drei: der Zugang. [zug2]Das Foto ist zwar sofort auf dem Handy von Bastian. Zugehen muss aber die "
     "formgerechte Erklärung. [brief]Wirft Frau Kuhlmann das Original später in seinen Briefkasten, kann die Kündigung "
     "erst mit dessen Zugang wirksam werden, Paragraf hundertdreißig. [frist_ab]Erst ab dann läuft auch die Klagefrist.", PS),
    # --- K IV. Vertretung, § 174 (Ausblick) --------------------------------------------------------------------------------------
    ("[vertr]Römisch vier: die Vertretung, als Ausblick. [peters]Angenommen, die Werkstattleiterin Frau Petersen übergibt "
     "ein Original, das sie selbst unterschrieben hat.", 0.3),
    ("[pe1]Hier ist deine Kündigung, unterschrieben in Vertretung.", 0.4, "Petersen"),
    ("[p174]Legt sie keine Vollmachtsurkunde vor, kann Bastian die Kündigung aus diesem Grund unverzüglich zurückweisen, "
     "Paragraf hundertvierundsiebzig Satz eins. [woche]Mehr als eine Woche ist nach dem Bundesarbeitsgericht ohne "
     "besondere Umstände zu spät. [kennt]Ausgeschlossen ist die Zurückweisung, wenn Frau Kuhlmann ihn von der "
     "Bevollmächtigung in Kenntnis gesetzt hatte, Satz zwei.", PS),
    # --- L V. Klagefrist, §§ 4, 7 KSchG ---------------------------------------------------------------------------------------------
    ("[klage]Römisch fünf: die Klagefrist. [p4]Nach Paragraf vier Satz eins des Kündigungsschutzgesetzes muss der "
     "Arbeitnehmer innerhalb von drei Wochen nach Zugang der schriftlichen Kündigung Klage erheben. [p7]Sonst gilt sie nach "
     "Paragraf sieben als von Anfang an rechtswirksam. [schrift]Entscheidend ist das Wort schriftlich. Eine schriftliche "
     "Kündigung ist Bastian nie zugegangen. [lauf]Die Frist lief also nicht, und Bastian kann den Formmangel auch nach "
     "fünf Wochen noch geltend machen.", PS),
    ("[erg]Ergebnis: Die Kündigung per WhatsApp ist nichtig. Das Arbeitsverhältnis besteht fort.", PS),
    # --- M Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Der typische Fehler steckt in der Klagefrist. [tipp2]Lass dich vom Fristablauf nicht täuschen. "
     "Paragraf sieben greift nur, wenn eine schriftliche Kündigung zugegangen ist. [tipp3]Und verwechsle die gesetzliche "
     "nicht mit einer vereinbarten Schriftform. Nur bei der vereinbarten genügt nach Paragraf hundertsiebenundzwanzig "
     "Absatz zwei im Zweifel auch die telekommunikative Übermittlung.", PS),
    # --- N Klausurschema -----------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema zur Wirksamkeit der Kündigung: [k1]Römisch eins: Kündigungserklärung. [k2]Römisch zwei: "
     "Schriftform nach Paragraf sechshundertdreiundzwanzig mit Paragraf hundertsechsundzwanzig, [k2a]also eine "
     "eigenhändig unterschriebene Urkunde, [k2b]sonst Nichtigkeit nach Paragraf hundertfünfundzwanzig. [k3]Römisch drei: "
     "Zugang des Originals. [k4]Römisch vier: Vertretung, mit Zurückweisung nach Paragraf hundertvierundsiebzig. "
     "[k5]Römisch fünf: Klagefrist, nur bei schriftlicher Kündigung.", PS),
    # --- O Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Eine Kündigung des Arbeitsverhältnisses braucht das eigenhändig unterschriebene Original beim Empfänger. [m2]Foto, Fax und "
     "E-Mail genügen nicht. Und ohne schriftliche Kündigung läuft keine Klagefrist.", 1.4),
]
