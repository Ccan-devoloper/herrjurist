"""Folge 090 · Drittanfechtung Baugenehmigung: Eilrechtsschutz nach §§ 80a, 80 V (Fr · 2. Examen · VwGO-Praxis, Format Schema).
Übungsfall nach dem Hook des Themenplans: Frau Dorn wohnt in einem kleinen Haus mit Garten (unbeplanter Innenbereich,
Umgebung zweigeschossig). Herr Weber erhält von der Stadt die Baugenehmigung für ein Mehrfamilienhaus mit vier Geschossen
und baut sofort; die Hauswand zu ihr ist 12,5 m hoch und steht 3 m vor der Grenze (Abstandsfläche nach § 6 Abs. 5 Satz 1
BauO NRW 2018: 0,4 H = 5 m, also 2 m auf ihrem Grundstück; keine Abweichung zugelassen). Frau Dorn klagt (NRW: kein
Vorverfahren, § 110 Abs. 3 Satz 2 Nr. 8 JustG NRW), Herr Weber baut weiter; Rechtsanwalt Falk stellt den Eilantrag
(Anwaltsklausur aus Sicht der Nachbarin).
Kern: § 80 I 1, § 212a I BauGB (Wortlautkarte) = Fall des § 80 II 1 Nr. 3; § 80a III (Wortlautkarte), Antrag nach § 80a III 2
i. V. m. § 80 V 1 Alt. 1 (Anordnung); A. Statthaftigkeit (§ 123 V), Antragsbefugnis analog § 42 II (drittschützende Norm,
Verweis Folge 088), Rechtsschutzbedürfnis (Klage erhoben; § 80 VI nur bei Nr. 1 – Wortlaut), Beiladung § 65 II;
B. dreipolige Interessenabwägung (BVerwG 7 VR 7.19 Rn. 8; § 212a-Wertung OVG NRW 7 B 359/25 Rn. 12, 10 B 603/20 Rn. 16),
summarisch nur drittschützende Normen (OVG NRW 10 B 645/23 Rn. 3; 10 B 1891/20 Rn. 5), Abstandsflächen verletzt
(§ 6 Abs. 1, 2, 5 BauO NRW 2018; BVerwG 4 B 52.15 Rn. 9; OVG NRW 10 B 603/20 Rn. 16) → Anordnung; Tenor (Klausurkonvention,
vgl. Tenor OVG NRW 10 B 603/20); Sicherungsmaßnahmen § 80a III 1, I Nr. 2 (OVG NRW 10 B 2060/99 Rn. 10); Klausurtipp
(Prüfprogramm, § 64 Abs. 1 Satz 1 Nr. 1 Buchst. b BauO NRW 2018), Schema, Merksatz (Lexi).
Fiktive Figuren: Frau Dorn (julia), Herr Weber (helmut), Rechtsanwalt Falk (niklas). Belege je Aussage: ../RECHTSSTAND.md.
Namen nie im Genitiv mit -s. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Dorn": "julia", "Weber": "helmut", "Falk": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Haus, Rohbau, Klage, Kanzlei -----------------------------------------------------------------------------
    ("[fall]Frau Dorn wohnt in einem kleinen Haus mit Garten. [bau]Nebenan wächst seit drei Wochen ein Rohbau: Vier "
     "Geschosse soll das Haus von Herrn Weber bekommen. [licht]Schon jetzt nimmt es ihrem Wohnzimmer fast das ganze "
     "Tageslicht.", 0.2),
    ("[do1]Das steht doch viel zu nah an meiner Grenze!", 0.3, "Dorn"),
    ("[we1]Ich habe eine Baugenehmigung der Stadt. Ich baue weiter.", 0.3, "Weber"),
    ("[klage]Frau Dorn erhebt Klage beim Verwaltungsgericht. In Nordrhein-Westfalen geht das bei Baugenehmigungen ohne "
     "Widerspruch, in deinem Land kann ein Widerspruch vorgeschrieben sein. [weiter]Doch auf der Baustelle wird weiter "
     "gemauert. [kanzlei]Frau Dorn geht zu Rechtsanwalt Falk.", 0.2),
    ("[fa1]Ihre Klage allein stoppt den Bau nicht. Wir brauchen einen Eilantrag.", 0.3, "Falk"),
    ("[frage]Warum hält die Klage den Bau nicht auf? Und wie prüfst du den Eilantrag in der Anwaltsklausur?", 0.6),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Das Problem: § 80 I 1 und § 212a I BauGB -------------------------------------------------------------------------
    ("[grund]Normalerweise haben Widerspruch und Anfechtungsklage aufschiebende Wirkung, Paragraf achtzig Absatz eins. "
     "[wl212]Hier aber gilt Paragraf zweihundertzwölf a Absatz eins des Baugesetzbuchs: Widerspruch und Anfechtungsklage "
     "eines Dritten gegen die bauaufsichtliche Zulassung eines Vorhabens haben keine aufschiebende Wirkung. [nr3]Das ist "
     "ein Fall von Paragraf achtzig Absatz zwei Satz eins Nummer drei: Ein Bundesgesetz schließt die Wirkung aus. "
     "[darf]Herr Weber darf also vorerst weiterbauen.", P),
    # --- D Der Antrag: § 80a III -------------------------------------------------------------------------------------------
    ("[wl80a]Den Ausweg zeigt Paragraf achtzig a Absatz drei: Das Gericht kann auf Antrag Maßnahmen nach den Absätzen eins "
     "und zwei ändern oder aufheben oder solche Maßnahmen treffen. Paragraf achtzig Absatz fünf bis acht gilt entsprechend. "
     "[antrag]Rechtsanwalt Falk beantragt deshalb nach Satz zwei in Verbindung mit Paragraf achtzig Absatz fünf Satz eins, "
     "die aufschiebende Wirkung der Klage anzuordnen. [anord]Anordnen, nicht wiederherstellen: Die Wirkung entfällt kraft "
     "Gesetzes, nicht durch eine Anordnung der Behörde.", P),
    # --- E A. Zulässigkeit -------------------------------------------------------------------------------------------------
    ("[zul]A, Zulässigkeit. [statt]Erstens, die Statthaftigkeit: In der Hauptsache ficht Frau Dorn einen Verwaltungsakt an, "
     "der Herrn Weber begünstigt und sie belastet. Deshalb gilt Paragraf achtzig a, nicht Paragraf hundertdreiundzwanzig. "
     "[befugt]Zweitens, die Antragsbefugnis entsprechend Paragraf zweiundvierzig Absatz zwei: Frau Dorn muss geltend "
     "machen, dass eine Norm verletzt ist, die gerade sie als Nachbarin schützt. [abst]Hier sind das die Abstandsflächen "
     "der Landesbauordnung. Welche Normen den Nachbarn schützen, zeigt unser Video zum Rücksichtnahmegebot.", P),
    ("[rsb]Drittens, das Rechtsschutzbedürfnis: Ihre Klage ist erhoben, [rsb2]und der Beschluss würde ihr nützen, denn "
     "noch wird gebaut. [abs6]Muss sie vorher bei der Behörde die Aussetzung beantragen? Nach dem Wortlaut nein. Paragraf "
     "achtzig a verweist zwar auch auf Absatz sechs. Der verlangt den Behördenantrag aber nur bei öffentlichen Abgaben und "
     "Kosten. [beil]Herrn Weber lädt das Gericht notwendig bei, Paragraf fünfundsechzig Absatz zwei: Die Entscheidung kann "
     "ihm gegenüber nur einheitlich ergehen.", PS),
    # --- F B. Begründetheit: dreipolige Interessenabwägung -------------------------------------------------------------------
    ("[begr]B, Begründetheit. Das Gericht wägt selbst ab, und zwar in einem Dreieck: [pole]das Aussetzungsinteresse von "
     "Frau Dorn gegen das Vollzugsinteresse von Herrn Weber. [wert]Dazu kommt die Wertung des Gesetzgebers in Paragraf "
     "zweihundertzwölf a: Die Baugenehmigung soll während des Prozesses grundsätzlich vollziehbar bleiben. [eaus]Wesentlich "
     "sind die Erfolgsaussichten der Klage, summarisch geprüft. [offen]Sind sie offen, entscheidet eine Folgenabwägung, und "
     "dann wiegt diese Wertung schwer.", P),
    ("[nurdritt]Aber Achtung: Das Gericht fragt nicht, ob die Genehmigung irgendwie rechtswidrig ist. [nur2]Es zählt nur, "
     "ob sie gegen Normen verstößt, die gerade Frau Dorn schützen. [mass]Ob sich vier Geschosse nach dem Maß der baulichen "
     "Nutzung in die zweigeschossige Umgebung einfügen, kann offenbleiben. Darauf kann sie sich nur berufen, wenn zugleich "
     "das Rücksichtnahmegebot verletzt ist.", P),
    # --- G Subsumtion: Abstandsflächen -----------------------------------------------------------------------------------------
    ("[abf]Anders die Abstandsflächen der Landesbauordnung. [schutz]Sie schützen auch den Nachbarn, gerade wenn es um "
     "Sonne geht. [nrw]In Nordrhein-Westfalen müssen sie vor Außenwänden auf dem eigenen Grundstück liegen, ihre Tiefe "
     "beträgt null Komma vier mal die Wandhöhe, mindestens drei Meter. In deinem Land kann die Regel anders lauten. [fall2]Die Hauswand ist zwölfeinhalb Meter hoch und braucht also fünf Meter. Sie steht aber nur drei Meter "
     "vor der Grenze. [verst]Zwei Meter der Abstandsfläche liegen auf dem Grundstück von Frau Dorn, eine Abweichung hat "
     "die Stadt nicht zugelassen. [rw]Die Genehmigung verletzt Frau Dorn deshalb offensichtlich in ihren Rechten. "
     "[rueck]Ob der Bau außerdem rücksichtslos ist, kann offenbleiben.", P),
    # --- H Ergebnis, Tenor, Sicherungsmaßnahmen --------------------------------------------------------------------------------
    ("[ergeb]Damit überwiegt das Aussetzungsinteresse von Frau Dorn, trotz Paragraf zweihundertzwölf a. [tenor]Der Tenor "
     "lautet nach Klausurkonvention: Die aufschiebende Wirkung der Klage der Antragstellerin gegen die dem Beigeladenen "
     "erteilte Baugenehmigung wird angeordnet. Dazu kommen Kosten und Streitwert. [stopp]Ab jetzt darf Herr Weber die "
     "Genehmigung nicht mehr ausnutzen. [sich]Baut er trotzdem weiter, kann das Gericht auf Antrag nach Paragraf achtzig a "
     "Absatz drei Satz eins in Verbindung mit Absatz eins Nummer zwei Sicherungsmaßnahmen treffen, etwa die Stilllegung "
     "der Baustelle.", 0.3),
    ("[we2]Dann muss ich wohl umplanen.", PS, "Weber"),
    # --- I Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Schreib nie, die Genehmigung sei rechtswidrig, also habe der Antrag Erfolg. [tipp1]Frage immer: "
     "Verletzt sie eine Norm, die gerade die Antragstellerin schützt? [tipp2]Und prüfe beim Bauordnungsrecht, ob die "
     "Behörde die Norm im Genehmigungsverfahren deines Landes überhaupt prüft. In Nordrhein-Westfalen gehören die "
     "Abstandsflächen dazu.", PS),
    # --- J Klausurschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sa]A, Zulässigkeit: [s1]Statthaftigkeit nach Paragraf achtzig a Absatz drei in Verbindung "
     "mit Paragraf achtzig Absatz fünf, [s2]Antragsbefugnis über eine drittschützende Norm, [s3]Rechtsschutzbedürfnis mit "
     "erhobenem Rechtsbehelf. [s4]Dazu die Beiladung des Bauherrn. [sb]B, Begründetheit: [s5]Interessenabwägung im Dreieck "
     "mit der Wertung von Paragraf zweihundertzwölf a, [s6]summarisch geprüft nur drittschützende Normen, [s7]hier die "
     "Abstandsflächen. [s8]Am Ende der Tenor.", PS),
    # --- K Merksatz (Lexi) ----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Gegen eine Baugenehmigung hat der Rechtsbehelf des Nachbarn keine aufschiebende Wirkung. [m2]Das "
     "Gericht ordnet sie auf Antrag an, wenn die Genehmigung voraussichtlich eine Norm verletzt, die gerade den Nachbarn "
     "schützt.", 1.4),
]

if __name__ == "__main__":
    import re
    alle = re.findall(r"\[(\w+)\]", " ".join(s[0] for s in SEGMENTE))
    doppelt = {m for m in alle if alle.count(m) > 1}
    assert not doppelt, f"Marke mehrfach: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(alle), "Marken,", zeichen, "Zeichen")
