"""Folge 160 · Mephisto-Beschluss: Wie viel Wahrheit darf ein Roman enthalten? (Mo · Der Fall · Klassiker-Fall;
Art. 5 III 1, 1 I, 2 I GG). Echte Fälle sachlich: BVerfG, Beschl. v. 24.2.1971 – 1 BvR 435/68, BVerfGE 30, 173 (Mephisto;
Volltext DFR, zitiert mit Seite) und BVerfG, Beschl. v. 13.6.2007 – 1 BvR 1783/05, BVerfGE 119, 1 (Esra; Volltext
bundesverfassungsgericht.de, zitiert mit Rn.; LS = Leitsatz). Formaler und offener Kunstbegriff: BVerfGE 67, 213 <226 f.>
(Anachronistischer Zug); praktische Konkordanz: BVerfGE 93, 1 <21> (Kruzifix).
DARSTELLUNG: keine intimen oder sexuellen Darstellungen, keine Zitate aus Romanen; „intime Szenen“ nur als Text-Pille.
Reale Personen (Klaus Mann, Gustaf Gründgens, die Klägerinnen im Esra-Fall) sind KEINE Figuren; im Esra-Fall keine Namen
(nur „der Roman Esra“, „der Autor“, „seine frühere Partnerin“, „deren Mutter“). Keine Buchcover.
Fiktiver Rahmen: Leseabend in einer Buchhandlung – Autorin Liesel (Stimme lucy), ihr früherer Partner Winfried (stephan),
Buchhändlerin Frau Hollerbach (hilde). stephan und christian nie gemeinsam; christian nicht besetzt.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Artikel im Sprechtext als Wörter. Belege je Cue: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Liesel": "lucy", "Winfried": "stephan", "Hollerbach": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Leseabend in der Buchhandlung (fiktiv) -------------------------------------------------------------------
    ("[fall]Leseabend in einer Buchhandlung.", P),
    ("[hgruss]Willkommen! Heute liest Liesel aus ihrem neuen Roman.", P, "Hollerbach"),
    ("[ex]In der ersten Reihe sitzt Winfried, ihr früherer Partner. [erkennt]Beim Zuhören erkennt er sich in der "
     "Hauptfigur wieder, bis in intime Szenen der Beziehung.", P),
    ("[wi1]Das bin ja ich! So darf das Buch nicht verbreitet werden.", P, "Winfried"),
    ("[li1]Das ist ein Roman. Die Figur ist erfunden.", P, "Liesel"),
    ("[frage]Wie viel Wahrheit darf ein Roman enthalten? [klassiker]Darauf antworten zwei Klassiker des "
     "Bundesverfassungsgerichts: der Mephisto-Beschluss und der Esra-Beschluss.", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C I. Schutzbereich (Wortlautkarte Art. 5 Abs. 3 Satz 1 GG; BVerfGE 30, 173 <188 f., 191>; 67, 213 <226 f.>) --------
    ("[a53]Artikel fünf Absatz drei Satz eins: Kunst und Wissenschaft, Forschung und Lehre sind frei. [vorb]Ein Vorbehalt "
     "fehlt. Die Kunstfreiheit ist vorbehaltlos gewährleistet.", P),
    ("[kunst]Was ist Kunst? [mat]Nach dem materiellen Kunstbegriff des Mephisto-Beschlusses ist das Wesentliche die freie "
     "schöpferische Gestaltung, in der Eindrücke, Erfahrungen, Erlebnisse des Künstlers durch das Medium einer bestimmten "
     "Formensprache zu unmittelbarer Anschauung gebracht werden. [formal]Der formale Kunstbegriff fragt, ob die "
     "Gattungsanforderungen eines Werktyps erfüllt sind, etwa Malen, Bildhauen, Dichten. [offen]Der offene Kunstbegriff fragt, ob sich der Darstellung durch "
     "fortgesetzte Interpretation immer weiterreichende Bedeutungen entnehmen lassen. [roman]Ein Roman ist Kunst.", P),
    ("[werk]Geschützt ist der Werkbereich, also das Schreiben, [wirk]und der Wirkbereich, also Darbietung und Verbreitung. "
     "[verlag]Deshalb kann sich auch der Verlag auf die Kunstfreiheit berufen.", P),
    # --- D II. Eingriff (BVerfGE 119, 1, Rn. 58, 66, 69) -------------------------------------------------------------------
    ("[eingriff]Verbietet ein Gericht den Roman, greift es in die Kunstfreiheit ein, und zwar besonders stark. "
     "[dritt]Dass ein Privater klagt, ändert daran nichts: Das Gericht ist den Grundrechten beider Seiten verpflichtet; "
     "das kennst du aus dem Lüth-Urteil.", P),
    # --- E III. Rechtfertigung: verfassungsimmanente Schranken (BVerfGE 30, 173 <191–193>; 119, 1, Rn. 68, 70) -------------
    ("[schranke]Vorbehaltlos heißt aber nicht schrankenlos. [verf]Grenzen zieht nur die Verfassung selbst, also "
     "kollidierendes Verfassungsrecht. [nicht52]Die Schranken aus Artikel fünf Absatz zwei gelten für die Kunst nicht.", P),
    ("[apr]Hier kollidiert das allgemeine Persönlichkeitsrecht. [a21]Artikel zwei Absatz eins: Jeder hat das Recht auf die "
     "freie Entfaltung seiner Persönlichkeit. [a11]In Verbindung mit Artikel eins Absatz eins: Die Würde des Menschen ist "
     "unantastbar. [entst]Es schützt vor verfälschenden oder entstellenden Darstellungen.", P),
    # --- F Mephisto (BVerfGE 30, 173 <174 f., 176–181, 194–200>) -----------------------------------------------------------
    ("[meph]Zuerst der Mephisto-Beschluss von neunzehnhunderteinundsiebzig. [mann]Klaus Manns Roman Mephisto schildert den "
     "Aufstieg des Schauspielers Hendrik Höfgen im nationalsozialistischen Deutschland. [vorbild]Als Vorbild diente der "
     "Schauspieler Gustaf Gründgens. [klage1]Nach dessen Tod klagte sein Adoptivsohn. Oberlandesgericht und "
     "Bundesgerichtshof untersagten dem Verlag, den Roman zu veröffentlichen.", P),
    ("[tot]Weil Gründgens gestorben war, schützte ihn Artikel zwei Absatz eins nicht mehr; geschützt blieb sein Achtungsanspruch aus der "
     "Menschenwürde. [urbild]Maßstab ist, ob das Abbild gegenüber dem Urbild so verselbständigt ist, dass das "
     "Individuelle zugunsten des Allgemeinen, Zeichenhaften der Figur objektiviert ist. [schmaeh]Die Gerichte sahen ein "
     "negativ verfälschendes Porträt, eine Schmähschrift in Romanform. [patt]Im Senat ergab sich Stimmengleichheit, "
     "drei zu drei. [erg1]Damit blieb die Verfassungsbeschwerde ohne Erfolg, und das Verbot blieb bestehen.", PS),
    # --- G Esra (BVerfGE 119, 1: LS 2, 4; Rn. 2 f., 7, 57, 74, 84, 88, 90, 99–103, 109) -------------------------------------
    ("[esra]Sechsunddreißig Jahre später der Esra-Beschluss. [esra1]Im Roman Esra erzählt ein Autor die Liebesgeschichte "
     "eines Schriftstellers und einer Schauspielerin. [klaeg]Seine frühere Partnerin und deren Mutter erkannten sich in "
     "den Figuren wieder und klagten.", P),
    ("[kspez]Das Gericht verlangt eine kunstspezifische Betrachtung. [vermut]Ein Roman ist zunächst als Fiktion anzusehen, "
     "auch wenn reale Vorbilder erkennbar sind. [erkenn]Erkennbarkeit allein ist noch keine Verletzung.", P),
    ("[jed]Es gilt die Je-desto-Formel: [je1]Je stärker Abbild und Urbild übereinstimmen, desto schwerer wiegt die "
     "Beeinträchtigung des Persönlichkeitsrechts. [je2]Je mehr die künstlerische Darstellung besonders geschützte "
     "Dimensionen des Persönlichkeitsrechts berührt, desto stärker muss die Fiktionalisierung sein, um eine "
     "Persönlichkeitsrechtsverletzung auszuschließen. [intim]Besonders geschützt ist die Intimsphäre: Sie gehört zum "
     "Menschenwürdekern.", P),
    ("[erg2]Ergebnis: Die Verfassungsbeschwerde des Verlags hatte nur teilweise Erfolg. [mutter]Das Verbot zugunsten der "
     "Mutter verletzte die Kunstfreiheit, weil die Gerichte die Vermutung der Fiktion nicht hinreichend beachtet hatten. [partn]Das Verbot "
     "zugunsten der früheren Partnerin hielt: Sie war erkennbar, und der Roman schilderte intimste Details, dazu die "
     "Krankheit ihrer Tochter.", PS),
    # --- H Zurück zur Lesung -------------------------------------------------------------------------------------------
    ("[zur]Zurück zur Lesung. [loes1]Erkennen Bekannte Winfried in der Figur, und schildert der Roman intime Szenen der "
     "gemeinsamen Beziehung, wiegt sein Persönlichkeitsrecht schwer. [loes2]Dann ist ein Verbot möglich, je nach "
     "Abwägung im Einzelfall.", PS),
    # --- I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bei einem vorbehaltlosen Grundrecht prüfst du keinen Gesetzesvorbehalt und nicht Artikel fünf "
     "Absatz zwei. [tipp2]Benenne das kollidierende Verfassungsgut mit seiner Norm. [tipp3]Dann stellst du praktische "
     "Konkordanz her: Beide Rechte sollen einen möglichst schonenden Ausgleich erfahren.", PS),
    # --- J Prüfschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema; das Grundschema kennst du aus der Folge zur Grundrechtsprüfung. [k1]Römisch eins: "
     "Schutzbereich, Kunst im Werk- und Wirkbereich. [k2]Römisch zwei: Eingriff, etwa das gerichtliche Verbot. "
     "[k3]Römisch drei: Rechtfertigung. [k3a]Erstens: verfassungsimmanente Schranke, also kollidierendes "
     "Verfassungsrecht. [k3b]Zweitens: praktische Konkordanz, mit kunstspezifischer Betrachtung und "
     "Je-desto-Formel.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Kunstfreiheit ist vorbehaltlos, aber nicht schrankenlos. [m2]Je erkennbarer das Urbild und je "
     "intimer das Geschilderte, desto stärker muss der Roman fiktionalisieren.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
