"""Folge 081 · Zulässigkeit und Begründetheit: Aufbau im Öffentlichen Recht (Fr · Methodik · Klausuraufbau).
Beispielfall als roter Faden (Übungsfall): Die Studentin Tabea teilt ihr kleines Auto mit zwei Mitbewohnern. Jemand wird
damit geblitzt, 25 km/h zu schnell; den Anhörungsbogen lässt Tabea liegen, den Fahrer findet die Stadt nicht. Dann ordnet die
Stadt per Bescheid an, dass Tabea ein halbes Jahr ein Fahrtenbuch führen muss (§ 31a Abs. 1 Satz 1 StVZO). Tabea: „Ich bin
doch gar nicht gefahren!“ Ihr Mitbewohner Lennart (Jurastudent) vermischt Zulässigkeit und Begründetheit.
Gezeigt werden: Obersatz (Klausurkonvention), Trennung Zulässigkeit/Begründetheit (§ 109 VwGO), Bausteine der Zulässigkeit
als Überblick (§§ 40, 42, 68, 74, 78, 61, 62 VwGO; § 88 VwGO), Klagebefugnis § 42 II (Wortlautkarte; BVerwG 4 C 3.20 Rn. 9,
9 B 4.19 Rn. 18), Begründetheit § 113 I 1 (Wortlautkarte), Übertragung auf die Verfassungsbeschwerde (Art. 94 I Nr. 4a GG
n. F., §§ 90 ff., 95 I BVerfGG) und § 80 V VwGO (BVerwG 7 VR 5.20 Rn. 8), Gewichtung (Verweis Folge 003), typische Fehler.
Fiktive Figuren: Tabea (julia), Lennart (niklas). Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Tabea": "julia", "Lennart": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Blitzer und Bescheid -----------------------------------------------------------------------------------
    ("[fall]Die Studentin Tabea teilt ihr kleines Auto mit zwei Mitbewohnern. [blitz]Vor drei Monaten wurde jemand damit "
     "geblitzt, fünfundzwanzig Kilometer pro Stunde zu schnell. [bogen]Den Anhörungsbogen hat Tabea liegen lassen, "
     "[fahrer]und wer gefahren ist, hat die Stadt nicht herausgefunden. [bescheid]Heute liegt ein Bescheid im Briefkasten.", 0.3),
    ("[ta1]Ich soll ein halbes Jahr ein Fahrtenbuch führen? Ich bin doch gar nicht gefahren!", 0.3, "Tabea"),
    ("[le1]Dann ist der Bescheid rechtswidrig. Deine Klage ist also zulässig.", 0.3, "Lennart"),
    ("[ta2]Und hat meine Klage Erfolg?", 0.4, "Tabea"),
    ("[frage]Lennart vermischt hier zwei Fragen. [frage2]Wie du Zulässigkeit und Begründetheit sauber trennst, zeigt "
     "dieser Fall.", 0.6),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Obersatz und Trennung ------------------------------------------------------------------------------------------
    ("[ober]Im Öffentlichen Recht beginnt die Lösung meist mit dem Satz: Die Klage hat Erfolg, soweit sie zulässig und "
     "begründet ist. [konv]Das ist eine Klausurkonvention, kein Gesetzestext. [zul]Die Zulässigkeit fragt: Darf das "
     "Gericht überhaupt in der Sache entscheiden? [sev]Man spricht deshalb von Sachentscheidungsvoraussetzungen. "
     "[begr]Die Begründetheit fragt: Hat die Klägerin in der Sache recht?", P),
    ("[unz]Fehlt eine Voraussetzung der Zulässigkeit, entscheidet das Gericht nicht in der Sache. [unz2]Meist weist es die "
     "Klage als unzulässig ab, beim falschen Rechtsweg verweist es den Rechtsstreit an das zuständige Gericht. [p109]Über "
     "die Zulässigkeit kann es sogar vorab durch Zwischenurteil entscheiden, Paragraf hundertneun "
     "Verwaltungsgerichtsordnung.", PS),
    # --- D Bausteine der Zulässigkeit --------------------------------------------------------------------------------------
    ("[bau]Die Zulässigkeit hat typische Bausteine, hier im Überblick. [b1]Erstens, der "
     "Verwaltungsrechtsweg, Paragraf vierzig: eine öffentlich-rechtliche Streitigkeit nichtverfassungsrechtlicher Art. "
     "[b1a]Die Fahrtenbuchauflage ordnet eine Behörde nach Straßenverkehrsrecht an. [b2]Zweitens, die statthafte "
     "Klageart. Sie richtet sich nach dem Begehren. [b2a]Tabea will den Bescheid loswerden, also die Anfechtungsklage.", P),
    ("[b3]Drittens, die besonderen Voraussetzungen dieser Klageart: Klagebefugnis, ein Vorverfahren, wenn es nötig ist, "
     "und die Klagefrist. [b4]Viertens, die Beteiligten: der richtige Klagegegner, Beteiligten- und Prozessfähigkeit. "
     "[b5]Fünftens, das Rechtsschutzbedürfnis. [b6]Jeden Punkt im Einzelnen zeigt unser Video zur Anfechtungsklage.", PS),
    # --- E Klagebefugnis und typische Fehler ----------------------------------------------------------------------------------
    ("[wl42]Bei der Klagebefugnis passieren die meisten Fehler. Paragraf zweiundvierzig Absatz zwei verlangt, dass der "
     "Kläger geltend macht, in seinen Rechten verletzt zu sein. [mt]Das heißt: Eine Verletzung muss möglich sein. Ob sie "
     "wirklich vorliegt, ist hier noch nicht die Frage. [adr]Tabea ist Adressatin eines belastenden Bescheids. Sie kann "
     "also jedenfalls in ihrer allgemeinen Handlungsfreiheit verletzt sein. [f1]Typischer Fehler: schon hier die ganze "
     "Rechtsverletzung prüfen.", P),
    ("[f2]Den zweiten Fehler hat Lennart gemacht: Er begründet die Zulässigkeit damit, dass der Bescheid rechtswidrig sei. "
     "[f2a]Das ist eine Frage der Begründetheit.", 0.3),
    ("[le2]Stimmt. Erst die Zulässigkeit, und ob der Bescheid rechtswidrig ist, kommt in die Begründetheit.", 0.4, "Lennart"),
    ("[zulerg]Nehmen wir an, auch die übrigen Voraussetzungen liegen vor. Dann ist die Klage zulässig.", PS),
    # --- F Begründetheit, Wortlaut § 113 I 1 -------------------------------------------------------------------------------
    ("[wl113]Jetzt die Begründetheit. Bei der Anfechtungsklage gilt Paragraf hundertdreizehn Absatz eins Satz eins: "
     "Soweit der Verwaltungsakt rechtswidrig und der Kläger dadurch in seinen Rechten verletzt ist, hebt das "
     "Gericht den Verwaltungsakt und den etwaigen Widerspruchsbescheid auf. [zwei]Daraus folgen zwei Prüfungspunkte: "
     "Rechtswidrigkeit und Rechtsverletzung.", P),
    ("[rw]Bei der Rechtswidrigkeit prüfst du die Ermächtigungsgrundlage, dann die formelle und die materielle "
     "Rechtmäßigkeit. [egl]Hier ist das Paragraf einunddreißig a der Straßenverkehrs-Zulassungs-Ordnung: [tb]Die Behörde "
     "kann gegenüber dem Halter ein Fahrtenbuch anordnen, wenn die Feststellung des Fahrers nach einem Verkehrsverstoß "
     "nicht möglich war. [arg]Erst hier hat das Argument von Tabea seinen Platz. [arg2]Nach dem Wortlaut kommt es nicht "
     "darauf an, ob sie selbst gefahren ist, sondern ob der Fahrer festgestellt werden konnte. [rv]Ist der Bescheid "
     "rechtswidrig, ist Tabea als Adressatin regelmäßig auch in ihren Rechten verletzt.", P),
    ("[erg]Hat die Klage also Erfolg? Zulässig ist sie. [erg2]Über den Erfolg entscheidet die Begründetheit, vor allem die "
     "Frage, ob der Fahrer festzustellen war.", PS),
    # --- G Übertragbarkeit --------------------------------------------------------------------------------------------------
    ("[ueb]Dieser Grundaufbau trägt auch andere Verfahren. [vb]Bei der Verfassungsbeschwerde prüfst du zuerst die "
     "Zulässigkeit nach Artikel vierundneunzig Absatz eins Nummer vier a Grundgesetz und den Paragrafen neunzig und "
     "folgende des Bundesverfassungsgerichtsgesetzes, [vb2]etwa Beschwerdebefugnis, Rechtswegerschöpfung und Frist. "
     "[vb3]Begründet ist sie, soweit die Beschwerdeführerin tatsächlich in einem Grundrecht oder grundrechtsgleichen "
     "Recht verletzt ist.", P),
    ("[eil]Und im Eilverfahren nach Paragraf achtzig Absatz fünf prüfst du ebenfalls Zulässigkeit und Begründetheit. "
     "[eil2]In der Begründetheit wägt das Gericht dort die Interessen ab, vor allem nach den Erfolgsaussichten in der "
     "Hauptsache.", PS),
    # --- H Gewichtung --------------------------------------------------------------------------------------------------------
    ("[gew]Und wie ausführlich schreibst du? [gew1]Was unproblematisch ist, stellst du knapp im Urteilsstil fest, etwa den "
     "Rechtsweg. [gew2]Wo das Problem liegt, schreibst du im Gutachtenstil, hier bei der Feststellung des Fahrers. "
     "[gew3]Wie das geht, zeigt unser Video zum Gutachtenstil.", PS),
    # --- I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Frag dich bei jedem Gedanken, wohin er gehört. [tipp1]Geht es darum, ob das Gericht entscheiden "
     "darf, gehört er in die Zulässigkeit. [tipp2]Geht es darum, ob die Behörde richtig gehandelt hat, gehört er in die "
     "Begründetheit.", PS),
    # --- J Klausurschema -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s0]Obersatz: Die Klage hat Erfolg, soweit sie zulässig und begründet ist. [sa]A, "
     "Zulässigkeit: [s1]Rechtsweg, [s2]statthafte Klageart, [s3]besondere Voraussetzungen der Klageart, [s4]Beteiligte, "
     "[s5]Rechtsschutzbedürfnis. [sb]B, Begründetheit, bei der Anfechtungsklage nach Paragraf hundertdreizehn: "
     "[s6]Rechtswidrigkeit, mit Ermächtigungsgrundlage, formeller und materieller Rechtmäßigkeit, [s7]und "
     "Rechtsverletzung. [sc]C, Ergebnis.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Zulässigkeit fragt, ob das Gericht entscheiden darf, die Begründetheit, wer in der Sache recht hat. "
     "[m2]Was die Sache betrifft, gehört erst in die Begründetheit.", 1.4),
]
