"""Folge 109 · Regelverjährung in 5 Minuten: Drei Jahre und der Silvester-Trick (Mo · Der Fall · Zivilrecht/BGB AT,
Format Schema). Beispielfall nach dem Plan-Hook („Du schuldest einem Freund seit 2022 Geld – ab wann darfst du dich auf
Verjährung berufen?“): Im März 2022 leiht Finn seiner Freundin Pia 2.000 € für die Kaution ihrer ersten Wohnung; als
Rückzahlungstag vereinbaren beide den 1. Juli 2022. Pia zahlt nicht, Finn fragt nicht nach, klagt nicht und beantragt
keinen Mahnbescheid. Im Oktober 2026 verlangt er das Geld. Variante: Abschlag von 200 € am 15. Mai 2024.
Kern als Rechenschema I.–VI.: § 194 Abs. 1 (Wortlaut), § 195 (Wortlaut), § 199 Abs. 1 (Wortlaut; Entstehung = Fälligkeit,
BGH IX ZR 129/17 Rn. 6; Kenntnis) mit dem Silvester-Trick am Zeitstrahl, § 199 Abs. 4 (Abs. 2, 3 genannt), Hemmung
(§§ 203, 204 Abs. 1 Nr. 1, 3, § 209) und Neubeginn (§ 212 Abs. 1 Nr. 1 auszugsweise; taggenau, BGH XII ZR 86/11 Rn. 33),
Rechtsfolge § 214 Abs. 1; Ergebnis mit Datum; Klausurtipp (§ 488 Abs. 3; Abschlag vor Beginn/nach Ablauf); Schema; Merksatz.
Figuren: Pia (julia), Finn (niklas); Lexi/Erzählerin Carla. Belege: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Pia": "julia", "Finn": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: im Café, März 2022 ---------------------------------------------------------------------------------
    ("[fall]März zweitausendzweiundzwanzig. Pia braucht Geld für die Kaution ihrer ersten Wohnung. "
     "[leih]Ihr guter Freund Finn leiht ihr zweitausend Euro.", 0.3),
    ("[fi1]Aber bis zum ersten Juli will ich es zurück.", 0.3, "Finn"),
    ("[pi1]Versprochen. Am ersten Juli hast du es.", 0.4, "Pia"),
    ("[juli]Der erste Juli kommt und geht. Pia zahlt nicht, [still]und Finn fragt nicht nach.", 0.5),
    # --- A2 Fall: im Park, Oktober 2026 ------------------------------------------------------------------------------
    ("[okt]Im Oktober zweitausendsechsundzwanzig treffen sich die beiden im Park.", 0.3),
    ("[fi2]Pia, ich hätte gern endlich meine zweitausend Euro zurück!", 0.3, "Finn"),
    ("[pi2]Das ist über vier Jahre her. Ist das nicht längst verjährt?", 0.4, "Pia"),
    ("[frage]Seit wann darf sich Pia auf die Verjährung berufen? [frage2]Und was, wenn sie zwischendurch etwas "
     "zurückgezahlt hätte?", 0.5),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Rechenweg in sechs Schritten ------------------------------------------------------------------------------
    ("[plan]Die Regelverjährung prüfst du in sechs Schritten: [s1]Anspruch, [s2]Frist, [s3]Beginn, [s4]Höchstfrist, "
     "[s5]Hemmung und Neubeginn, [s6]Rechtsfolge.", PS),
    # --- D I. Anspruch, § 194 Abs. 1 (Wortlaut) -----------------------------------------------------------------------
    ("[a194]Erstens: der Anspruch. Paragraf hundertvierundneunzig Absatz eins: Das Recht, von einem anderen ein Tun oder "
     "Unterlassen zu verlangen, also der Anspruch, unterliegt der Verjährung. [a488]Finn hat einen Anspruch auf "
     "Rückzahlung des Darlehens, Paragraf vierhundertachtundachtzig Absatz eins Satz zwei.", P),
    # --- E II. Frist, § 195 (Wortlaut) ---------------------------------------------------------------------------------
    ("[f195]Zweitens: die Frist. Paragraf hundertfünfundneunzig: Die regelmäßige Verjährungsfrist beträgt drei Jahre. "
     "[fdarl]Sie gilt auch für die Rückzahlung von Darlehen.", P),
    # --- F III. Beginn, § 199 Abs. 1 (Wortlaut) -----------------------------------------------------------------------
    ("[b199]Drittens: der Beginn. Nach Paragraf hundertneunundneunzig Absatz eins beginnt die "
     "Frist mit dem Schluss des Jahres, in dem zwei Dinge zusammenkommen. [bentst]Der Anspruch ist entstanden, das "
     "heißt in der Regel: fällig. [bkennt]Und der Gläubiger kennt die Umstände und die Person des Schuldners, oder er "
     "müsste sie ohne grobe Fahrlässigkeit kennen.", P),
    ("[bfall]Hier wurde das Darlehen am ersten Juli zweitausendzweiundzwanzig fällig, [bfall2]und Finn kannte Pia und "
     "alle Umstände von Anfang an.", PS),
    # --- G Silvester-Trick (Zeitstrahl) --------------------------------------------------------------------------------
    ("[silv]Jetzt der Silvester-Trick: Ob der Anspruch im Januar oder im Dezember entsteht: Die Frist startet erst "
     "mit dem Jahresende. [s31]Hier am einunddreißigsten Dezember zweitausendzweiundzwanzig um Mitternacht. "
     "[sjahre]Dann laufen drei volle Jahre: zweitausenddreiundzwanzig, vierundzwanzig, fünfundzwanzig. [sende]Verjährt "
     "ist der Anspruch mit dem Ablauf des einunddreißigsten Dezember zweitausendfünfundzwanzig. [sneu]Seit dem ersten "
     "Januar zweitausendsechsundzwanzig darf Pia die Zahlung verweigern.", PS),
    # --- H IV. Höchstfristen, § 199 Abs. 4 ----------------------------------------------------------------------------
    ("[hoech]Viertens: Fehlt dem Gläubiger die Kenntnis, greift eine Höchstfrist. Nach Paragraf hundertneunundneunzig "
     "Absatz vier verjähren Ansprüche wie dieser in zehn Jahren ab ihrer Entstehung, ohne Rücksicht auf die Kenntnis. "
     "[h23]Für Schadensersatz gelten die Absätze zwei und drei.", PS),
    # --- I V. Hemmung und Neubeginn ------------------------------------------------------------------------------------
    ("[hemm]Fünftens: Hemmung und Neubeginn. Die Hemmung hält die Uhr an; diese Zeit wird nach Paragraf zweihundertneun "
     "nicht mitgerechnet. [h203]Gehemmt ist die Verjährung, solange die Parteien über den Anspruch verhandeln, Paragraf "
     "zweihundertdrei. [h204a]Ebenso durch die Erhebung der Klage, Paragraf zweihundertvier Absatz eins Nummer eins, "
     "[h204b]und durch die Zustellung eines Mahnbescheids, Nummer drei. [hnein]Hier nichts davon: keine Verhandlungen, "
     "keine Klage, kein Mahnbescheid.", P),
    ("[neu]Der Neubeginn stellt die Uhr dagegen auf null. Paragraf zweihundertzwölf Absatz eins Nummer eins: Die "
     "Verjährung beginnt erneut, wenn der Schuldner dem Gläubiger gegenüber den Anspruch durch Abschlagszahlung "
     "anerkennt.", P),
    ("[var]Angenommen, Pia hätte Finn am fünfzehnten Mai zweitausendvierundzwanzig zweihundert Euro gezahlt. [vtag]Dann "
     "läuft ab dem nächsten Tag eine neue Dreijahresfrist, taggenau, ohne Silvester-Trick. [vende]Sie endet mit "
     "dem Ablauf des fünfzehnten Mai zweitausendsiebenundzwanzig. [vrest]Die restlichen achtzehnhundert Euro müsste sie "
     "noch zahlen.", PS),
    # --- J VI. Rechtsfolge, § 214 Abs. 1 -------------------------------------------------------------------------------
    ("[r214]Sechstens: die Rechtsfolge. Nach Paragraf zweihundertvierzehn Absatz eins darf der Schuldner nach Eintritt "
     "der Verjährung die Leistung verweigern. Der Anspruch erlischt nicht; Pia muss sich darauf berufen.", PS),
    # --- K Ergebnis ----------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Der Anspruch von Finn ist mit dem Ablauf des einunddreißigsten Dezember "
     "zweitausendfünfundzwanzig verjährt. [erg2]Beruft sich Pia darauf, muss sie nicht zahlen. [erg3]Mit dem "
     "Abschlag wäre der Rest dagegen bis Mai zweitausendsiebenundzwanzig durchsetzbar.", PS),
    # --- L Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst die Fälligkeit. Ist beim Darlehen kein Rückzahlungstag vereinbart, hängt sie von "
     "einer Kündigung ab, Paragraf vierhundertachtundachtzig Absatz drei, und erst dann kann die Frist beginnen. "
     "[tipp2]Und ein Abschlag wirkt nur, während die Frist läuft.", PS),
    # --- M Klausurschema -----------------------------------------------------------------------------------------------
    ("[sch]Dein Rechenschema: [k1]Römisch eins: Anspruch. [k2]Römisch zwei: Frist, drei Jahre. [k3]Römisch drei: Beginn, "
     "mit Entstehung, Kenntnis und Jahresschluss. [k4]Römisch vier: Höchstfristen. [k5]Römisch fünf: Hemmung und "
     "Neubeginn. [k6]Römisch sechs: Rechtsfolge.", PS),
    # --- N Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Drei Jahre, gerechnet ab Silvester des Jahres, in dem der Anspruch fällig wird und der Gläubiger "
     "davon weiß oder wissen müsste. [mk2]Die Hemmung hält die Uhr an, [mk3]ein Anerkenntnis stellt sie auf null.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
