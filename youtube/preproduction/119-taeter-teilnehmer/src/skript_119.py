"""Folge 119 · Abgrenzung Täter Teilnehmer: Tatherrschaft vs. subjektive Theorie (Mi · Examenswissen · StGB AT,
Format Streitstand). Einstieg mit den beiden Klassikern als Akten (Badewannen-Fall, RGSt 74, 84; Staschinski-Fall,
BGHSt 18, 87), gelesen von zwei Referendaren (Luise, Oskar) in der Bibliothek; keine Fallbeteiligten als Figuren.
Aufbau: 1. Problem (Wortlaut § 25 I, § 27 I; § 26; Strafrahmen § 27 II 2, § 49 I) → 2. extrem subjektive Theorie des RG
(animus auctoris/socii; Badewannen-Fall), BGHSt 8, 393 (1956), Staschinski (1962) → 3. Kritik und Wende (§ 25 I Alt. 1
seit 1.1.1975; BGH 3 StR 35/92 = BGHSt 38, 315, HRRS Rn. 4–6) → 4. Tatherrschaftslehre (Zentralgestalt; Handlungs-,
Willens-, funktionale Tatherrschaft; Verweis 091/094) → 5. Streitstand im Zweispalter, heutige Rechtsprechung
(3 StR 363/22 Rn. 8; 3 StR 189/19 Rn. 6; Verweis 104) → 6. Streitentscheid, Dahinstehen → Ergebnis nach heutigem Recht
→ Klausurtipp → Schema → Merksatz. Belege je Aussage: ../RECHTSSTAND.md.
Namen der Figuren (eindeutig deutsch, in keiner Vorfolge vergeben): Luise, Oskar. Der Agent heißt im Sprechtext und auf
den Tafeln einheitlich „Staschinski“ (deutsche Schreibung wie Hefendehl-Skript und BGH-Literatur; Plan: „Staschynskij“).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue, je genau einmal."""

P, PS = 0.4, 0.45

STIMMEN = {"Luise": "sabrina", "Oskar": "marc"}   # Lexi = Carla (ohne Rolle)

SEGMENTE = [
    # --- A1 Fall: Badewannen-Fall (nur Akte, Gerichtsgebäude, Jahreszahl) ----------------------------------------------
    ("[fall]Neunzehnhundertvierzig, ein Urteil des Reichsgerichts. [geburt]Eine junge Frau hat ihre Schwangerschaft aus "
     "Angst vor ihrem Vater verheimlicht und das Kind heimlich zur Welt gebracht, mit Hilfe ihrer Schwester. "
     "[draengen]Auf Drängen der Mutter tötet die Schwester das Neugeborene unmittelbar nach der Geburt. [rg]Das "
     "Reichsgericht sieht in ihr nur eine Gehilfin. Täterin sei die Mutter, denn sie habe die Tat als eigene gewollt.", 0.3),
    ("[l1]Die Schwester hat doch selbst gehandelt. Warum nur Gehilfin?", 0.3, "Luise"),
    # --- A2 Fall: Staschinski-Fall (Akte, Stadtsilhouette, Jahreszahl; keine Waffe) --------------------------------------
    ("[bw]In der Lehre heißt der Fall Badewannen-Fall. [stasch]Neunzehnhundertzweiundsechzig urteilt der "
     "Bundesgerichtshof über einen Agenten des sowjetischen Geheimdienstes. [muc]Er hatte in München zwei "
     "ukrainische Exilpolitiker getötet, im Auftrag seiner Vorgesetzten. [bgh62]Der Bundesgerichtshof verurteilt ihn nur "
     "wegen Beihilfe zum Mord. Das ist der Staschinski-Fall.", 0.3),
    ("[o1]Wer selbst tötet, ist doch Täter. Oder etwa nicht?", 0.3, "Oskar"),
    ("[frage]Wann ist jemand Täter, wann nur Anstifter oder Gehilfe? [frage2]Darüber streiten Rechtsprechung und Lehre "
     "seit Jahrzehnten.", 0.6),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier sind beide Fälle zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Problem: Wortlaut § 25 I, § 27 I, § 26; Strafrahmen ---------------------------------------------------------
    ("[prob]Erst das Problem. Paragraf fünfundzwanzig Absatz eins: [p25w]Als Täter wird bestraft, wer die Straftat selbst "
     "oder durch einen anderen begeht. [p27]Paragraf siebenundzwanzig Absatz eins: [p27w]Als Gehilfe wird bestraft, wer "
     "vorsätzlich einem anderen zu dessen vorsätzlich begangener rechtswidriger Tat Hilfe geleistet hat. [p26]Dazwischen "
     "steht der Anstifter, der einen anderen zur Tat bestimmt.", PS),
    ("[straf]Warum die Abgrenzung so wichtig ist: [anst]Der Anstifter wird gleich einem Täter bestraft. [mild]Beim Gehilfen "
     "dagegen muss die Strafe gemildert werden, Paragraf siebenundzwanzig Absatz zwei, nach Paragraf neunundvierzig "
     "Absatz eins. [mord]Beim Mord heißt das: statt "
     "lebenslanger Freiheitsstrafe eine Freiheitsstrafe nicht unter drei Jahren.", PS),
    # --- D 2. Extrem subjektive Theorie des Reichsgerichts --------------------------------------------------------------
    ("[rg1]Das Reichsgericht fragte nach dem inneren Willen. [auct]Täter ist, wer mit Täterwillen handelt und die Tat als "
     "eigene will: animus auctoris. [socii]Teilnehmer ist, wer sie als fremde will: animus socii. [rgbw]Im Badewannen-Fall habe sich die Schwester nur dem "
     "Willen der Mutter gebeugt. Also nur Gehilfin.", PS),
    # --- E Bundesgerichtshof 1956 und Staschinski 1962 --------------------------------------------------------------------
    ("[bgh56]Neunzehnhundertsechsundfünfzig rückte der Bundesgerichtshof davon ab: [zit56]Wer mit "
     "eigener Hand einen Menschen tötet, ist grundsätzlich auch dann Täter, wenn er es unter dem Einfluss und in Gegenwart "
     "eines anderen nur in dessen Interesse tut. [st1]Im Staschinski-Fall stellte er aber wieder entscheidend auf den "
     "Willen ab. [st2]Der Agent habe sich den Befehlen nur widerwillig gebeugt und kein eigenes Interesse an der Tat "
     "gehabt. [st3]Die Auftraggeber dagegen hätten das Ob und Wie der Taten beherrscht. Sie seien die Täter.", PS),
    # --- F 3. Kritik und Wende: § 25 I Alt. 1 --------------------------------------------------------------------------
    ("[krit]Die Kritik: [k1]Der Täterwille ist kaum greifbar, die Abgrenzung hängt am richterlichen Ermessen. "
     "[k2]Und die Theorie löst sich vom Tatbestand. [wende]Die Wende brachte der Gesetzgeber. [w25]Seit "
     "neunzehnhundertfünfundsiebzig gilt Paragraf fünfundzwanzig Absatz eins, erste Alternative: Als Täter wird bestraft, "
     "wer die Straftat selbst begeht. "
     "[bgh92]Der Bundesgerichtshof folgert: Wer alle "
     "Tatbestandsmerkmale selbst verwirklicht, ist grundsätzlich Täter, auch wenn er nur im Interesse eines anderen "
     "handelt. [stets]In der Lehre heißt es sogar: stets.", PS),
    # --- G 4. Tatherrschaftslehre ------------------------------------------------------------------------------------
    ("[thl]Die heute herrschende Lehre stellt auf die Tatherrschaft ab. [zg]Täter ist die Zentralgestalt des Geschehens: "
     "wer es vom Vorsatz umfasst in den Händen hält. [rand]Teilnehmer ist nur eine Randfigur. [formen]Drei Formen: "
     "[hh]Handlungsherrschaft hat, wer selbst handelt. [wh]Willensherrschaft hat, wer einen anderen als "
     "Werkzeug steuert. [fh]Und funktionale "
     "Tatherrschaft hat, wer arbeitsteilig mit anderen zusammenwirkt.", PS),
    # --- H 5. Streitstand im Zweispalter, heutige Rechtsprechung --------------------------------------------------------
    ("[zw]Beide Seiten im Vergleich. [zl0]Links die Rechtsprechung: [zl1]Das Reichsgericht entschied nach dem "
     "Täterwillen. [zl2]Der Bundesgerichtshof entscheidet heute in einer wertenden Gesamtbetrachtung. [zl3]Maßgeblich "
     "sind der Grad des eigenen Interesses an der Tat, der Umfang der Tatbeteiligung und die Tatherrschaft oder "
     "wenigstens der Wille dazu. [zl4]Die Tatherrschaft ist also nur ein Kriterium, Schwächen dort können andere "
     "ausgleichen. [zr0]Rechts die Lehre: [zr1]Sie entscheidet nach der Tatherrschaft, [zr2]also danach, wer "
     "Zentralgestalt ist. [v104]Wie beide Ansichten bei Mittätern arbeiten, zeigt unsere Folge zur Mittäterschaft.", PS),
    # --- I 6. Streitentscheid ------------------------------------------------------------------------------------------
    ("[ents]Wir folgen der Tatherrschaftslehre. [e1]Sie knüpft an das an, was das Gesetz verlangt: das Begehen der Tat. "
     "[e2]Die Kriterien der Rechtsprechung haben dagegen keine feste Rangfolge. So lassen sich fast beliebige Ergebnisse "
     "begründen. [dahin]In der Klausur gilt: Kommen beide Ansichten zum selben Ergebnis, kann der Streit "
     "dahinstehen. [dahin2]Entscheiden musst du ihn nur, wenn sie auseinanderfallen.", PS),
    # --- J Ergebnis nach heutigem Recht ---------------------------------------------------------------------------------
    ("[erg]Und nach heutigem Recht? [erg1]Die Schwester im Badewannen-Fall ist Täterin: Sie hat alle Merkmale "
     "selbst verwirklicht, Paragraf fünfundzwanzig Absatz eins, erste Alternative. [erg2]Auch Staschinski wäre heute "
     "Täter, nach der Tatherrschaftslehre ohnehin und nach dem Bundesgerichtshof wohl ebenso. [erg3]Für die Auftraggeber stellt sich dann die Frage nach dem Täter hinter dem Täter, wie im "
     "Katzenkönig-Fall.", PS),
    # --- K Klausurtipp (Lexi) -------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst den Tatnächsten. [tipp2]Hat er alle Merkmale selbst erfüllt, ist er Täter, und ein "
     "Satz genügt. [tipp3]Den Streit breitest du nur dort aus, wo die Ansichten auseinanderfallen können.", PS),
    # --- L Klausurschema -----------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema zur Abgrenzung. [s_i]Römisch eins: Deliktstyp. Bei Sonder- und eigenhändigen "
     "Delikten entscheidet schon der Tatbestand. [s_ii]Römisch zwei: Hat der Beteiligte alle Merkmale selbst "
     "verwirklicht? Dann ist er Täter. [s_iii]Römisch drei: Sonst der Streit, [s3a]Tatherrschaftslehre [s3b]und wertende "
     "Gesamtbetrachtung der Rechtsprechung, [s3c]entschieden nur, wenn die Ergebnisse auseinanderfallen. [s_iv]Römisch "
     "vier: Ohne Täterschaft prüfst du Anstiftung oder Beihilfe.", PS),
    # --- M Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer die Tat selbst begeht, ist Täter, auch im Interesse eines anderen. [m_2]Bei allen anderen fragt "
     "die Lehre nach der Tatherrschaft, die Rechtsprechung nach einer wertenden Gesamtbetrachtung. [m_3]Der Täterwille "
     "allein entscheidet nicht mehr.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
