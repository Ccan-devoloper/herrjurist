"""Folge 205 · Recht auf Vergessen: Muss dein Name aus dem Online-Archiv? (Mo · Der Fall · Klassiker-Fall; Art. 2 I i. V. m.
Art. 1 I GG, Art. 5 I GG). Leitentscheidung: BVerfG, Beschl. v. 6.11.2019 – 1 BvR 16/13, BVerfGE 152, 152 (Recht auf
Vergessen I; Volltext bundesverfassungsgericht.de, zitiert mit Rn.; LS = Leitsatz). Abgrenzung in einem Satz: BVerfG, Beschl.
v. 6.11.2019 – 1 BvR 276/17, BVerfGE 152, 216 (Recht auf Vergessen II), Rn. 33 f., 42, 50.
DARSTELLUNG: kein echtes Magazin, kein Suchmaschinenlogo (fiktives Archiv ohne Namen, neutrale Suchmaske); keine Tatdetails
des historischen Falls (nur „Verurteilung wegen eines schweren Verbrechens“); der Betroffene ist kein Täter-Klischee; reale
Beteiligte werden nicht genannt. Herr Dornbusch bildet den Grundfall nur nach.
Fiktiver Rahmen: Gerhild (neue Nachbarin; Stimme sabrina), Herr Dornbusch (um 65; william), Herr Stöver (Archivleiter des
Verlags; marc). Erzählerin und Lexi: Carla ohne Rolle.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Artikel im Sprechtext als Wörter; keine Abkürzungen (synth_el buchstabiert BGH, GG). Belege je Cue:
../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Dornbusch": "william", "Gerhild": "sabrina", "Stöver": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die neue Nachbarin googelt (fiktiv, Nachbildung des Grundfalls) ---------------------------------------
    ("[fall]Gerhild zieht in eine neue Wohnung. [nachbar]Nebenan wohnt Herr Dornbusch, ein freundlicher älterer Herr.", P),
    ("[d1]Willkommen in der Nachbarschaft! Wenn Sie etwas brauchen, klingeln Sie einfach.", P, "Dornbusch"),
    ("[google]Am Abend gibt Gerhild seinen Namen in eine Suchmaschine ein. [treffer]Der erste Treffer: ein über dreißig "
     "Jahre alter Artikel im Onlinearchiv eines Nachrichtenmagazins. [prozess]Er berichtet über den Strafprozess gegen "
     "Herrn Dornbusch und seine Verurteilung wegen eines schweren Verbrechens.", P),
    ("[g1]Ausgerechnet mein netter Nachbar?", P, "Gerhild"),
    ("[haft]Herr Dornbusch hat seine Strafe längst verbüßt. [klage]Er verlangt vom Verlag, nicht mehr unter Nennung seines "
     "Namens über die Tat zu berichten.", P),
    ("[d2]Nehmen Sie wenigstens meinen Namen heraus.", P, "Dornbusch"),
    ("[s1]Der Bericht war damals rechtmäßig. Unser Archiv bleibt vollständig.", P, "Stöver"),
    ("[frage]Muss sein Name aus dem Onlinearchiv? [grund]Unser Fall bildet den Grundfall nach, den das "
     "Bundesverfassungsgericht im November zweitausendneunzehn entschieden hat: im Beschluss Recht auf Vergessen eins.", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Verfahren und Prüfungsmaßstab (Rn. 4–6, 37, 41 f., 74; LS 1a; RvV II Rn. 33 f., 42, 50) ------------------------
    ("[weg]Im echten Fall gaben Landgericht und Oberlandesgericht der Unterlassungsklage statt; [bgh]der "
     "Bundesgerichtshof wies sie ab. [vb]Dagegen erhob der Betroffene Verfassungsbeschwerde, eine "
     "Urteilsverfassungsbeschwerde gegen das Zivilurteil.", P),
    ("[mass]Doch welcher Maßstab gilt: das Grundgesetz oder die Grundrechte der Europäischen Union? [privileg]Das "
     "Datenschutzrecht der Union lässt den Mitgliedstaaten für die Presse einen Spielraum, das Medienprivileg. [gg]Wo "
     "Unionsrecht nicht vollständig vereinheitlicht ist, prüft das Gericht primär am Grundgesetz. [rvv2]Anders im "
     "Beschluss Recht auf Vergessen zwei vom selben Tag: Dort ging es um eine Suchmaschine im vollständig "
     "vereinheitlichten Datenschutzrecht, deshalb prüfte das Gericht an der Grundrechtecharta.", P),
    # --- D Schutzbereich: allgemeines Persönlichkeitsrecht (Wortlautkarten; LS 2a–c; Rn. 79 f., 91 f., 105, 107, 109) -------
    ("[apr]Auf der Seite von Herrn Dornbusch steht das allgemeine Persönlichkeitsrecht. [a21]Artikel zwei Absatz eins: "
     "Jeder hat das Recht auf die freie Entfaltung seiner Persönlichkeit. [a11]In Verbindung mit Artikel eins Absatz eins: "
     "Die Würde des Menschen ist unantastbar.", P),
    ("[aeuss]Maßgeblich ist hier nicht das Recht auf informationelle Selbstbestimmung, sondern der Schutz vor "
     "Gefährdungen durch die Verbreitung personenbezogener Berichte. [zeit]Und dabei zählt die Zeit. [vergessen]Das "
     "Gericht sagt: Zur Zeitlichkeit der Freiheit gehört die Möglichkeit des Vergessens. [neu]Erst wenn Vergangenes "
     "zurücktreten kann, hat der Einzelne die Chance zum Neubeginn in Freiheit. [jederzeit]Deshalb muss sich die "
     "Verbreitung zu jedem Zeitpunkt rechtfertigen lassen, in dem sie zugänglich ist. [kein]Aber: Ein Recht, alles aus "
     "dem Internet löschen zu lassen, folgt daraus nicht.", P),
    # --- E Gegenseite: Presse- und Meinungsfreiheit (Wortlautkarte Art. 5 I 2; Rn. 75 f., 93 f., 112 f., 115, 118 f.) --------
    ("[presse]Auf der anderen Seite steht der Verlag. [a51]Artikel fünf Absatz eins Satz zwei: Die Pressefreiheit und "
     "die Freiheit der Berichterstattung durch Rundfunk und Film werden gewährleistet. [archiv]Dazu gehört die "
     "Entscheidung, alte Berichte dauerhaft im Archiv zugänglich zu machen. [oeff]Solche Archive sind auch für die "
     "Öffentlichkeit wichtig, etwa für zeitgeschichtliche Recherchen. [rechtm]Und die ursprüngliche Berichterstattung "
     "war rechtmäßig.", P),
    ("[dritt]Zwischen Herrn Dornbusch und dem Verlag wirken die Grundrechte mittelbar, über das Zivilrecht; das kennst du "
     "aus dem Lüth-Urteil. [pruef]Der Verlag muss sein Archiv nicht von sich aus ständig überprüfen. [beanst]Schutzpflichten "
     "entstehen erst, wenn sich Betroffene an ihn wenden.", P),
    # --- F Abwägung (Rn. 121–125, 129–141, 146–153) -----------------------------------------------------------------------
    ("[abw]Jetzt die Abwägung. [zeitab]Erstens der Zeitablauf: Die Tat liegt über dreißig Jahre zurück, die Strafe ist "
     "vollständig verbüßt. [breite]Zweitens die Breitenwirkung: Nachbarn und neue Bekannte geben den Namen schon aus "
     "oberflächlichem Interesse in eine Suchmaschine ein, und der erste Treffer prägt dann das Bild der Person. "
     "[verhalten]Drittens das Verhalten des Betroffenen: Er ist mit der Tat nicht wieder an die Öffentlichkeit getreten. "
     "[selbst]Wer selbst wieder Aufmerksamkeit sucht, dessen Schutzinteresse wiegt geringer.", P),
    ("[stufen]Viertens, und das ist der Kern: abgestufte Schutzmaßnahmen. [loesch]Eine Pflicht, alte Berichte endgültig zu "
     "löschen oder zu verändern, wäre mit der Pressefreiheit grundsätzlich unvereinbar. [suche]Aber der Verlag kann die Auffindbarkeit "
     "über namensbezogene Suchabfragen begrenzen, etwa so, dass Suchmaschinen den Artikel zum Namen nicht mehr anzeigen. "
     "[sach]Wer zu den damaligen Ereignissen recherchiert, findet den Bericht dann weiterhin, unverändert. [fach]Welche "
     "Maßnahme zumutbar ist, entscheiden die Fachgerichte.", PS),
    # --- G Ergebnis (Tenor; Rn. 143, 145, 153, 155, 157) ------------------------------------------------------------------
    ("[erg]Ergebnis: Der Bundesgerichtshof hatte die Belastung durch den Zeitablauf nicht hinreichend gewichtet und keine "
     "Zwischenlösungen geprüft. [verl]Sein Urteil verletzte das allgemeine Persönlichkeitsrecht. [zurueck]Das "
     "Bundesverfassungsgericht hob es auf und verwies die Sache zurück, einstimmig.", PS),
    # --- H Zurück zu Herrn Dornbusch -------------------------------------------------------------------------------------
    ("[zur]Und Herr Dornbusch? [loes1]Sein Name muss nicht aus dem Archiv gelöscht werden. [loes2]Gegen die Suche nach "
     "seinem Namen kommen aber zumutbare Schutzvorkehrungen in Betracht; welche, klären die Zivilgerichte.", PS),
    # --- I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Kläre zuerst den Prüfungsmaßstab. Ist das Unionsrecht vollständig vereinheitlicht, prüfst du die "
     "Grundrechtecharta, sonst das Grundgesetz. [tipp2]Prüfe beim Pressebericht nicht die informationelle "
     "Selbstbestimmung, sondern das Persönlichkeitsrecht in seiner äußerungsrechtlichen Ausprägung. [tipp3]Und suche in "
     "der Abwägung nach Zwischenlösungen statt nach Alles oder Nichts.", PS),
    # --- J Prüfschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für die Begründetheit. [k1]Römisch eins: Prüfungsmaßstab, Grundgesetz oder Charta. "
     "[k2]Römisch zwei: Schutzbereich, das allgemeine Persönlichkeitsrecht. [k3]Römisch drei: das Gegenrecht, Meinungs- "
     "und Pressefreiheit, mittelbar über das Zivilrecht. [k4]Römisch vier: Abwägung, mit Zeitablauf, Breitenwirkung, "
     "Verhalten des Betroffenen und abgestuften Schutzmaßnahmen.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Zur Zeitlichkeit der Freiheit gehört die Möglichkeit des Vergessens. [m2]Vergessen heißt aber nicht "
     "löschen: Statt den Bericht zu ändern, kann der Verlag die Auffindbarkeit über den Namen begrenzen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
