"""Folge 131 · Klagearten EuGH: Vorlage, Nichtigkeitsklage, Vertragsverletzung (Mi · Examenswissen · Öffentliches Recht/
Europarecht, Format Schema). Hook nach dem Plan („Ein deutsches Gericht zweifelt, ein Unternehmen klagt, die Kommission
verklagt Deutschland – die Verfahren in Luxemburg“) als drei fiktive Mini-Fälle mit je einer Figur:
Richterin Eichhorn (Verwaltungsgericht, Auslegungszweifel an einer EU-Verordnung), Frau Pfister (Unternehmerin, Geldbuße der
Kommission per Beschluss), Herr Teichmann (Beamter der Kommission, deutsches Gesetz mit Zusatzgenehmigung für Handwerker aus
anderen Mitgliedstaaten). Kern: Raster Wer? Wogegen? Voraussetzungen? Folge? für
1. Vorabentscheidungsverfahren Art. 267 AEUV (Wortlautkarte auszugsweise; CILFIT Rn. 9, 21; C-561/19 Rn. 33, 35, 54;
   Foto-Frost Rn. 15, 20; Elchinov Rn. 29; BVerfGE 126, 286 Rn. 88),
2. Nichtigkeitsklage Art. 263 AEUV (Wortlautkarte Abs. 4; Plaumann, Slg. 1963, 213, 238; Inuit C-583/11 P Rn. 60 f.;
   Abs. 6; Art. 256 Abs. 1 AEUV mit Art. 51 Satzung; Art. 264),
3. Vertragsverletzungsverfahren Art. 258 AEUV (Wortlautkarte, vorgelesen; C-152/98 Rn. 23 f.; Art. 259, 260 Abs. 1, 2),
Art. 265, 340 AEUV je ein Halbsatz. Ergebnis je Mini-Fall, Klausurtipp, Klausurschema als Übersicht, Merksatz.
Belege: ../RECHTSSTAND.md. Keine echten Personen.
Figuren: Richterin Eichhorn (hilde), Frau Pfister (lucy), Herr Teichmann (christian); Lexi/Erzählerin Carla.
Namen nicht im Genitiv. Abkürzungen im Sprechtext ausgeschrieben (synth_el buchstabiert sonst bzw. kennt sie nicht).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Artikel im Sprechtext als Wörter."""

P, PS = 0.3, 0.55

STIMMEN = {"Eichhorn": "hilde", "Pfister": "lucy", "Teichmann": "christian"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Drei Mini-Fälle -------------------------------------------------------------------------------------------------
    ("[fall]Drei Fälle für Luxemburg. [eich]Richterin Eichhorn am Verwaltungsgericht entscheidet über einen Bescheid, der auf "
     "einer EU-Verordnung beruht. [unklar]Ein Begriff der Verordnung ist unklar.", 0.3),
    ("[ei1]Wie ist dieser Begriff auszulegen? Das soll der Gerichtshof klären.", 0.3, "Eichhorn"),
    ("[pfist]Frau Pfister führt eine Baustofffirma. [busse]Die Kommission verhängt gegen ihr Unternehmen per Beschluss eine "
     "Geldbuße wegen eines Kartellverstoßes.", 0.3),
    ("[pf1]Diesen Beschluss lasse ich nicht stehen. Ich klage!", 0.3, "Pfister"),
    ("[teich]Herr Teichmann von der Europäischen Kommission prüft ein deutsches Gesetz. [hand]Handwerker aus anderen "
     "Mitgliedstaaten brauchen danach eine zusätzliche Genehmigung.", 0.3),
    ("[te1]Das verstößt gegen die Dienstleistungsfreiheit. Wir gehen gegen Deutschland vor.", 0.3, "Teichmann"),
    ("[frage]Ein Gericht zweifelt, ein Unternehmen klagt, die Kommission verklagt Deutschland. [frage2]Welches Verfahren "
     "passt jeweils?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Überblick -------------------------------------------------------------------------------------------------------
    ("[ueber]Die drei wichtigsten Verfahren: [u1]die Vorabentscheidung, [u2]die Nichtigkeitsklage [u3]und das "
     "Vertragsverletzungsverfahren. [raster]Jeweils fragen wir: Wer? Wogegen? Voraussetzungen? Folge?", PS),
    # --- D 1. Vorabentscheidungsverfahren, Art. 267 AEUV -----------------------------------------------------------------
    ("[wl267]Erstens, das Vorabentscheidungsverfahren, Artikel zweihundertsiebenundsechzig des Vertrags über die Arbeitsweise "
     "der Union. [ausl]Der Gerichtshof entscheidet über die Auslegung der Verträge [guelt]und über die Gültigkeit und die "
     "Auslegung der Handlungen der Organe. [abs2]Hält ein Gericht eines Mitgliedstaats eine Entscheidung darüber für "
     "erforderlich, kann es die Frage vorlegen. [abs3]Ein Gericht, dessen Entscheidungen nicht mehr mit Rechtsmitteln "
     "angefochten werden können, muss vorlegen.", PS),
    ("[wer1]Wer? Nur das Gericht legt vor. Für die Parteien ist die Vorlage kein Rechtsbehelf. [teil1]Der Gerichtshof legt "
     "das Unionsrecht aus, das nationale Recht und den Fall beurteilt allein das vorlegende Gericht. [cilf]Ausnahmen von der "
     "Vorlagepflicht nach CILFIT: Die Frage ist nicht entscheidungserheblich, [acte]schon vom Gerichtshof geklärt oder die Antwort "
     "so offenkundig, dass kein vernünftiger Zweifel bleibt, kurz: acte éclairé und acte clair. [foto]Hält ein Gericht eine "
     "Handlung der Union für ungültig, muss es vorlegen. Verwerfen darf sie nur der Gerichtshof der Europäischen Union.", PS),
    ("[bind]Die Folge: Das Urteil bindet das vorlegende Gericht. [gg]Verletzt ein deutsches Gericht die Vorlagepflicht "
     "in offensichtlich unhaltbarer Weise, entzieht es nach dem Bundesverfassungsgericht den gesetzlichen Richter, Artikel hunderteins "
     "Absatz eins Satz zwei Grundgesetz. [l1]Und Richterin Eichhorn? Gegen ihr Urteil gibt es noch ein Rechtsmittel. "
     "[l1b]Sie darf vorlegen, muss aber nicht.", PS),
    # --- E 2. Nichtigkeitsklage, Art. 263 AEUV ---------------------------------------------------------------------------
    ("[ni]Zweitens, die Nichtigkeitsklage, Artikel zweihundertdreiundsechzig. [wog]Wogegen? Gegen Handlungen der Union mit "
     "Rechtswirkung, etwa einen Beschluss der Kommission. [priv]Wer? "
     "Privilegiert sind Mitgliedstaaten, Parlament, Rat und Kommission: Sie müssen keine eigene Betroffenheit darlegen. "
     "[tprv]Teilprivilegiert sind Rechnungshof, Europäische Zentralbank und Ausschuss der Regionen, nur zur Wahrung ihrer Rechte. "
     "[nprv]Nichtprivilegiert sind natürliche und juristische Personen.", PS),
    ("[wl263]Für sie gilt Absatz vier: Klagen können sie gegen an sie gerichtete Handlungen, [unind]gegen Handlungen, die sie "
     "unmittelbar und individuell betreffen, [vochar]und gegen Rechtsakte mit Verordnungscharakter, die sie unmittelbar "
     "betreffen und keine Durchführungsmaßnahmen nach sich ziehen. [plaum]Individuell betroffen ist nach der Plaumann-Formel "
     "nur, wen die Handlung wegen persönlicher Eigenschaften oder besonderer Umstände aus dem Kreis aller übrigen heraushebt "
     "und ähnlich individualisiert wie einen Adressaten. [inuit]Rechtsakte mit Verordnungscharakter sind nach dem Gerichtshof "
     "Handlungen mit allgemeiner Geltung, aber keine Gesetzgebungsakte.", PS),
    ("[frist]Die Frist: zwei Monate, Absatz sechs. [eug]Klagen Einzelner gehen zuerst an das Gericht der "
     "Europäischen Union, Artikel zweihundertsechsundfünfzig. [nichtig]Die Folge: Die Handlung wird für nichtig erklärt, "
     "Artikel zweihundertvierundsechzig. [l2]Frau Pfister ist Adressatin des Beschlusses. Auf Plaumann kommt es nicht an. "
     "[l2b]Sie muss aber binnen zwei Monaten klagen.", PS),
    # --- F 3. Vertragsverletzungsverfahren, Art. 258 AEUV ----------------------------------------------------------------
    ("[wl258]Drittens, das Vertragsverletzungsverfahren, Artikel zweihundertachtundfünfzig. Meint die Kommission, ein "
     "Mitgliedstaat habe gegen die Verträge verstoßen, gibt sie ihm Gelegenheit zur Äußerung [stell]und dann eine mit Gründen "
     "versehene Stellungnahme ab. [w258b]Kommt der Staat ihr nicht fristgerecht nach, kann die Kommission den Gerichtshof "
     "anrufen.", PS),
    ("[wer3]Wer? Die Kommission, nach Artikel zweihundertneunundfünfzig auch ein anderer Mitgliedstaat. Wogegen? Gegen einen "
     "Verstoß eines Mitgliedstaats. [vor]Voraussetzung ist dieses Vorverfahren: erst das Mahnschreiben, dann die begründete "
     "Stellungnahme. "
     "[fest]Die Folge: Der Gerichtshof stellt den Verstoß fest. Der Staat muss die Maßnahmen ergreifen, die sich aus dem "
     "Urteil ergeben. [zwang]Tut er das nicht, kann der Gerichtshof in einem zweiten Verfahren einen Pauschalbetrag oder ein "
     "Zwangsgeld verhängen, Artikel zweihundertsechzig Absatz zwei.", PS),
    ("[l3]Für Herrn Teichmann heißt das: Zuerst kommt das Vorverfahren. [l3b]Ändert Deutschland das Gesetz "
     "nicht fristgerecht, kann die Kommission klagen. [rest]Daneben gibt es die Untätigkeitsklage, Artikel "
     "zweihundertfünfundsechzig, und die Schadensersatzklage gegen die Union, Artikel dreihundertvierzig.", PS),
    # --- G Ergebnis --------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: [e1]Richterin Eichhorn, Vorabentscheidung. [e2]Frau Pfister, Nichtigkeitsklage. [e3]Herr Teichmann, "
     "Vertragsverletzungsverfahren.", PS),
    # --- H Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Vorlage ist keine Klage. Prüfe also keine Klagebefugnis und keine Frist, [tipp2]sondern "
     "Vorlagegegenstand, vorlageberechtigtes Gericht und Entscheidungserheblichkeit. [tipp3]Bei der Nichtigkeitsklage "
     "Privater liegt der Schwerpunkt dagegen bei Absatz vier.", PS),
    # --- I Klausurschema als Übersicht ------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema als Übersicht. [r1]Eins, wer? [r1a]Ein Gericht, [r1b]ein Kläger, "
     "[r1c]die Kommission. [r2]Zwei, wogegen? [r2a]Eine Frage zum Unionsrecht, [r2b]eine Handlung der Union, [r2c]ein Verstoß "
     "eines Mitgliedstaats. [r3]Drei, Voraussetzungen: [r3a]Entscheidungserheblichkeit, [r3b]Klageberechtigung und Frist, "
     "[r3c]das Vorverfahren. [r4]Vier, die Folge: [r4a]Bindung, [r4b]Nichtigerklärung, [r4c]Feststellungsurteil.", PS),
    # --- J Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Das Gericht fragt, [m1]der Betroffene klagt gegen die Union, [m2]und die Kommission klagt gegen den "
     "Staat.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
