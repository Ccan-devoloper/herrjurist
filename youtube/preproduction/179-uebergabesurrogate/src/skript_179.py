"""Folge 179 · Besitzkonstitut & Co.: Eigentum ohne Übergabe (§§ 929 S. 2, 930, 931) (Mi · Examenswissen · Sachenrecht,
Format Schema).
Hook nach Plan („Du kaufst das Auto deines Nachbarn, der es aber noch eine Woche weiterfahren darf“): Käthe kauft das Auto
ihres Nachbarn Herrn Wöhler für 4.000 €, zahlt sofort und erhält die Zulassungsbescheinigung Teil II; Herr Wöhler zieht um
und darf den Wagen noch bis Samstag fahren (Leihe); beide wollen, dass das Auto ab heute Käthe gehört.
Prüfung: § 929 S. 1 (Verweis Folge 080), Übergabe fehlt; Zulassungsbescheinigung Teil II verbrieft nicht das Eigentum, ist
kein Traditionspapier, Bedeutung nur für den guten Glauben (BGH V ZR 148/21 Rn. 20 f.) → drei Übergabesurrogate in drei
kurzen Fällen mit gleicher Bildstruktur: 1. § 929 S. 2 (Wortlautkarte), Übereignung kurzer Hand (Auto steht schon bei
Käthe) → 2. § 930 (Wortlautkarte), Besitzkonstitut, § 868 (Wortlautkarte), Leihe bis Samstag; konkreter Inhalt
(BGH V ZR 92/25 Rn. 20), abstraktes Konstitut nach h. M. nicht genügend;
Sicherungsübereignung (V ZR 8/15 Rn. 7) und Bestimmtheit (V ZR 174/21 Rn. 10) je ein Satz → 3. § 931 (Wortlautkarte),
Auto in der Werkstatt (Werkvertrag = Besitzmittlungsverhältnis, V ZR 70/16 Rn. 16), Abtretung §§ 398, 870, keine Mitwirkung
der Werkstatt nötig (IX ZR 295/16 Rn. 34), § 986 Abs. 2 → 4. Merktabelle → 5. Ausblick gutgläubiger Erwerb (§§ 932 Abs. 1
S. 2, 933, 934, Verweis Folgen 083/161) → 6. Lösung → Klausurtipp (Lexi) → Prüfschema → Merksatz (Lexi).
Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Volltextsuche 04.10.2026): Käthe, Herr Wöhler
(nie im Genitiv). Stimmen: Käthe sabrina, Herr Wöhler marc; die Werkstattmeisterin spricht nicht. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Käthe": "sabrina", "Wöhler": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall --------------------------------------------------------------------------------------------------------
    ("[fall]Stell dir vor, du kaufst das Auto deines Nachbarn. [kaethe]So geht es Käthe. [kauf]Ihr Nachbar, Herr Wöhler, "
     "verkauft ihr seinen Kleinwagen für viertausend Euro. [zahlt]Käthe zahlt sofort, [zb]und Herr Wöhler gibt ihr die "
     "Zulassungsbescheinigung Teil zwei. [aber]Aber er braucht das Auto noch eine Woche.", P),
    ("[wo1]Ich ziehe nächste Woche um. Darf ich den Wagen bis Samstag noch fahren?", P, "Wöhler"),
    ("[ka1]Gut, ich leihe ihn Ihnen bis Samstag. Aber ab heute gehört er mir.", P, "Käthe"),
    ("[wo2]Einverstanden.", P, "Wöhler"),
    ("[frage]Also fährt Herr Wöhler weiter. [frage2]Ist Käthe trotzdem schon heute Eigentümerin?", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Einordnung --------------------------------------------------------------------------------------------------
    ("[p929]Normalerweise geht Eigentum nach Paragraf neunhundertneunundzwanzig Satz eins über: durch Einigung und "
     "Übergabe; das Schema zeigt das Video zu Einigung und Übergabe. [einig]Einig sind sich die beiden. [fehlt]Aber "
     "übergeben hat Herr Wöhler das Auto nicht, er fährt es ja weiter. [zbk]Und die Zulassungsbescheinigung hilft nicht. "
     "[zbk2]Nach dem Bundesgerichtshof verbrieft sie nicht das Eigentum, und ihre Übergabe ersetzt nicht die Übergabe des "
     "Autos. [zbk3]Wichtig wird sie erst beim guten Glauben.", P),
    ("[surr]Doch das Gesetz kennt drei Wege, die Übergabe zu ersetzen, die Übergabesurrogate. [drei]Wir spielen sie mit "
     "drei kurzen Fällen durch, immer mit demselben Auto.", PS),
    # --- D 1. § 929 S. 2: Übereignung kurzer Hand ----------------------------------------------------------------------
    ("[s1]Erstens: Paragraf neunhundertneunundzwanzig Satz zwei. [s1fall]Angenommen, Käthe hat sich das Auto schon vor "
     "zwei Wochen geliehen, und es steht in ihrer Einfahrt.", P),
    ("[ka2]Das Auto steht ja schon bei mir.", P, "Käthe"),
    ("[wo3]Dann gehört es ab jetzt Ihnen.", P, "Wöhler"),
    ("[w929]Dafür gilt Satz zwei: Ist der Erwerber im Besitz der Sache, so genügt die Einigung über den Übergang des "
     "Eigentums. [s1b]Herr Wöhler muss nichts mehr übergeben. Käthe wird sofort Eigentümerin. [kh]Man nennt das Übereignung "
     "kurzer Hand.", PS),
    # --- E 2. § 930: Besitzkonstitut -----------------------------------------------------------------------------------
    ("[s2]Zweitens, unser Fall: Herr Wöhler behält das Auto. [w930]Das regelt Paragraf neunhundertdreißig: Ist der "
     "Eigentümer im Besitz der Sache, so kann die Übergabe dadurch ersetzt werden, dass zwischen ihm und dem Erwerber ein "
     "Rechtsverhältnis vereinbart wird, vermöge dessen der Erwerber den mittelbaren Besitz erlangt. [bk]Das ist das "
     "Besitzkonstitut.", P),
    ("[p868]Welche Rechtsverhältnisse das sind, zeigt Paragraf achthundertachtundsechzig: [w868]etwa Miete, Verwahrung oder "
     "ein ähnliches Verhältnis, das den Besitzer auf Zeit zum Besitz berechtigt oder verpflichtet. [leih]Eine Leihe gehört "
     "dazu. [sub]Herr Wöhler bleibt unmittelbarer Besitzer, jetzt aber als Entleiher. [sub2]Käthe wird mittelbare "
     "Besitzerin.", PS),
    ("[konk]Aber Vorsicht: [bgh]Nach dem Bundesgerichtshof braucht das Besitzmittlungsverhältnis einen konkreten Inhalt. "
     "Der Besitzer muss auf Zeit zum Besitz berechtigt sein, und der Herausgabeanspruch des anderen darf nicht endgültig "
     "ausgeschlossen sein. [abstr]Ein bloßes „Ab jetzt besitze ich für dich“ reicht nach herrschender Meinung nicht. "
     "[hier]Hier ist alles konkret: Leihe bis Samstag, dann gibt Herr Wöhler den Wagen heraus.", P),
    ("[sue]In der Praxis begegnet dir das Besitzkonstitut vor allem bei der Sicherungsübereignung: Die Bank wird "
     "Eigentümerin, der Kreditnehmer behält die Sache. [best]Dann achte auch auf die Bestimmtheit: Wer die Abreden kennt, "
     "muss ohne Weiteres sehen, welche Sachen übereignet sind.", PS),
    # --- F 3. § 931: Abtretung des Herausgabeanspruchs -----------------------------------------------------------------
    ("[s3]Drittens: Das Auto steht bei einem Dritten. [s3fall]Angenommen, es ist beim Kauf noch in der Werkstatt zur "
     "Reparatur.", P),
    ("[wo4]Holen Sie ihn in der Werkstatt ab. Meinen Anspruch auf Herausgabe trete ich Ihnen ab.", P, "Wöhler"),
    ("[w931]Das ist Paragraf neunhunderteinunddreißig: Ist ein Dritter im Besitz der Sache, so kann die Übergabe dadurch "
     "ersetzt werden, dass der Eigentümer dem Erwerber den Anspruch auf Herausgabe der Sache abtritt. [werk]Die Werkstatt "
     "besitzt den Wagen für Herrn Wöhler, denn der Werkvertrag ist ein Besitzmittlungsverhältnis. [abtr]Abgetreten wird nach "
     "Paragraf dreihundertachtundneunzig, [p870]und mit dem Anspruch geht nach Paragraf achthundertsiebzig der mittelbare "
     "Besitz über. [ohne]Die Werkstatt muss dabei in der Regel weder mitwirken noch davon wissen. [p986]Sie kann Käthe aber "
     "alles entgegenhalten, was sie gegen den abgetretenen Anspruch hat, Paragraf neunhundertsechsundachtzig Absatz zwei, "
     "etwa, dass die Reparatur noch nicht bezahlt ist.", PS),
    # --- G Merktabelle -------------------------------------------------------------------------------------------------
    ("[tab]Zusammengefasst: Es kommt darauf an, wer die Sache hat. [t1]Hat sie der Erwerber, genügt die Einigung. [t2]Behält "
     "sie der Veräußerer, ersetzt ein Besitzmittlungsverhältnis die Übergabe. [t3]Hat sie ein Dritter, ersetzt die Abtretung "
     "des Herausgabeanspruchs die Übergabe. [t4]Die Einigung braucht es immer.", PS),
    # --- H Ausblick gutgläubiger Erwerb --------------------------------------------------------------------------------
    ("[gut]Und wenn das Auto gar nicht Herrn Wöhler gehört? [gut2]Dann gelten für alle drei Wege eigene Regeln zum "
     "gutgläubigen Erwerb, in den Paragrafen neunhundertzweiunddreißig Absatz eins Satz zwei, neunhundertdreiunddreißig und "
     "neunhundertvierunddreißig. [gut3]Beim Besitzkonstitut etwa erst mit der Übergabe; mehr dazu in den Videos zum "
     "gutgläubigen Erwerb und zum Abhandenkommen.", PS),
    # --- I Lösung ------------------------------------------------------------------------------------------------------
    ("[loes]Zurück zu Käthe. [l1]Beide sind sich einig, dass das Eigentum sofort übergehen soll. [l2]Statt der Übergabe "
     "vereinbaren sie eine Leihe bis Samstag, ein konkretes Besitzmittlungsverhältnis. [l3]Herr Wöhler ist Eigentümer und "
     "besitzt das Auto. [l4]Also ist Käthe schon heute Eigentümerin, nach Paragraf neunhundertneunundzwanzig Satz eins in "
     "Verbindung mit Paragraf neunhundertdreißig. [l5]Am Samstag muss Herr Wöhler ihr den Wagen dann herausgeben.", PS),
    # --- J Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst die Einigung und frag dann: Wer hat die Sache gerade? [tp2]Davon hängt ab, welches "
     "Surrogat passt. [tp3]Beim Besitzkonstitut nenne das konkrete Besitzmittlungsverhältnis, hier die Leihe bis Samstag.", PS),
    # --- K Prüfschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema zur Übereignung ohne Übergabe. [c1]Römisch eins: Einigung. [c2]Römisch zwei: Übergabe oder "
     "Surrogat. [c2a]Erwerber besitzt: Satz zwei. [c2b]Veräußerer besitzt: Besitzkonstitut nach Paragraf neunhundertdreißig. "
     "[c2c]Dritter besitzt: Abtretung nach Paragraf neunhunderteinunddreißig. [c3]Römisch drei: Einigsein in diesem "
     "Zeitpunkt. [c4]Römisch vier: Berechtigung, sonst gutgläubiger Erwerb.", PS),
    # --- L Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Eigentum geht auch ohne Übergabe über. [m2]Entscheidend ist, wer die Sache hat: der Erwerber, der "
     "Veräußerer oder ein Dritter.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
