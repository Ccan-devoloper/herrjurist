"""Folge 120 · Gesamtschuld §§ 421, 426 BGB: Einer zahlt für alle – und dann? (Fr · Klausurpraxis · Zivilrecht/Schuldrecht AT,
Format Schema). Fall nach dem Plan-Hook („Drei Mitbewohner haften für die Stromrechnung – der Versorger holt sich alles von
einem“): Insa, Lars und Rieke wohnen in einer WG; alle drei haben den Stromvertrag unterschrieben. Rieke ist ausgezogen und
zahlungsunfähig. Die Jahresabrechnung ergibt 900 € Nachzahlung; der Versorger verlangt alles von Insa, sie zahlt. Lars will
ihr nur 300 € erstatten. Schema: I. Außenverhältnis – 1. Entstehen § 421 (Wortlautkarte § 421 S. 1), § 427, § 840 I,
Gleichstufigkeit (BGH VII ZR 7/11 Rn. 18); 2. Erfüllung § 422 I, Einzelwirkung § 425. II. Innenverhältnis – 1. § 426 I 1
(Wortlautkarte), Abrede (BGH XII ZR 53/08 Rn. 9); 2. Ausfall § 426 I 2; 3. Legalzession § 426 II 1 (Wortlautkarte),
§§ 412, 401 (Verweis Folge 089); Verhältnis I/II (BGH IX ZR 216/20 Rn. 19, XI ZR 234/11 Rn. 20). Rechnung, Ergebnis
(Lars schuldet 450 €). Klausurtipp (Lexi): beide Wege, §§ 412, 404, Befreiungsanspruch (BGH VI ZR 200/15 Rn. 11).
Klausurschema, Merksatz (Lexi). Figuren: Insa (ela_froh), Lars (niklas), Rieke (spricht nicht), Sachbearbeiter des
Versorgers (helmut); Lexi/Erzählerin Carla. Belege: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Insa": "ela_froh", "Lars": "niklas", "Versorger": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die WG und der Stromvertrag ------------------------------------------------------------------------
    ("[fall]Insa, Lars und Rieke wohnen zusammen in einer Wohngemeinschaft. [vertrag]Den Stromvertrag haben alle drei unterschrieben. "
     "[auszug]Im Frühjahr zieht Rieke aus. [pleite]Sie ist inzwischen zahlungsunfähig. [abr]Dann kommt die "
     "Jahresabrechnung: neunhundert Euro Nachzahlung. [anruf]Der Versorger meldet sich bei Insa.", 0.3),
    # --- A2 Fall: der Versorger verlangt alles von Insa -------------------------------------------------------------
    ("[sb1]Die neunhundert Euro verlangen wir vollständig von Ihnen.", 0.25, "Versorger"),
    ("[in1]Von mir allein? Wir waren doch zu dritt!", 0.3, "Insa"),
    ("[zahlt]Insa zahlt die neunhundert Euro. [lars]Dann wendet sie sich an Lars.", 0.25),
    ("[in2]Du schuldest mir die Hälfte, vierhundertfünfzig Euro.", 0.25, "Insa"),
    ("[la1]Wir waren drei. Ich zahle dir dreihundert, mehr nicht.", 0.3, "Lars"),
    ("[frage]Durfte der Versorger alles von Insa verlangen? [frage2]Und wie viel muss Lars ihr erstatten?", PS),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.6),
    # --- C Zwei Ebenen ------------------------------------------------------------------------------------------------------
    ("[eben]Die Gesamtschuld hat zwei Ebenen. [aussen]Im Außenverhältnis geht es um den Gläubiger und die Schuldner. "
     "[innen]Im Innenverhältnis um den Ausgleich der Schuldner untereinander.", PS),
    # --- D1 I. 1. Entstehen, § 421 S. 1 (Wortlaut) ------------------------------------------------------------------------
    ("[w421]Römisch eins: das Außenverhältnis. Erstens: Entstehen der Gesamtschuld nach Paragraf vierhunderteinundzwanzig. "
     "[m1]Mehrere schulden eine Leistung. [m2]Jeder muss die ganze Leistung bewirken, [m3]der Gläubiger darf sie aber nur "
     "einmal fordern. [m4]Er kann nach seinem Belieben wählen, von wem er sie verlangt, ganz oder zu einem Teil.", P),
    # --- D2 Entstehungsgründe, Gleichstufigkeit, Subsumtion --------------------------------------------------------------
    ("[p427]Oft entsteht die Gesamtschuld durch gemeinsamen Vertrag: Verpflichten sich mehrere gemeinschaftlich zu einer "
     "teilbaren Leistung, haften sie nach Paragraf vierhundertsiebenundzwanzig im Zweifel als Gesamtschuldner. [p840]Sie "
     "kann auch aus dem Gesetz folgen, etwa nach Paragraf achthundertvierzig Absatz eins, wenn mehrere für einen Schaden aus "
     "unerlaubter Handlung verantwortlich sind. [gleich]Nach dem Bundesgerichtshof müssen die Pflichten gleichstufig sein: "
     "Keiner haftet nur nachrangig oder vorläufig.", P),
    ("[sub1]Im Fall haben alle drei den Stromvertrag unterschrieben, und eine Geldzahlung ist teilbar. [sub2]Also sind sie "
     "Gesamtschuldner. Der Versorger durfte die ganzen neunhundert Euro von Insa verlangen.", PS),
    # --- E I. 2. Wirkung der Erfüllung, § 422 I, § 425 --------------------------------------------------------------------
    ("[p422]Zweitens: die Wirkung der Erfüllung. Nach Paragraf vierhundertzweiundzwanzig Absatz eins wirkt die Erfüllung "
     "durch einen Gesamtschuldner auch für die übrigen. [frei]Mit der Zahlung von Insa sind auch Lars und Rieke gegenüber "
     "dem Versorger frei. [p425]Andere Tatsachen, etwa Verzug oder Verjährung, wirken nach Paragraf "
     "vierhundertfünfundzwanzig grundsätzlich nur für den, bei dem sie eintreten.", PS),
    # --- F II. 1. Ausgleich, § 426 I 1 (Wortlaut) -------------------------------------------------------------------------
    ("[w426]Römisch zwei: das Innenverhältnis. Erstens: der Ausgleichsanspruch. Paragraf vierhundertsechsundzwanzig "
     "Absatz eins Satz eins: Die Gesamtschuldner sind im Verhältnis zueinander zu gleichen Anteilen verpflichtet, soweit "
     "nicht ein anderes bestimmt ist. [anteil]Drei Mitbewohner, neunhundert Euro: Auf jeden entfallen dreihundert. "
     "[abrede]Hätte die Wohngemeinschaft etwas anderes vereinbart, etwa eine Verteilung nach Zimmergröße, gälte diese.", P),
    # --- G II. 2. Ausfall, § 426 I 2 (Wortlaut) ---------------------------------------------------------------------------
    ("[w426s2]Zweitens: die Ausfallhaftung nach Satz zwei. Kann von einem Gesamtschuldner der auf ihn entfallende Beitrag "
     "nicht erlangt werden, so ist der Ausfall von den übrigen zur Ausgleichung verpflichteten Schuldnern zu tragen. "
     "[ausfall]Rieke ist zahlungsunfähig. [halb]Ihre dreihundert Euro tragen Insa und Lars je zur Hälfte, also je "
     "hundertfünfzig.", PS),
    # --- H II. 3. Legalzession, § 426 II 1 (Wortlaut), §§ 412, 401, Verhältnis I/II ------------------------------------
    ("[w426b]Drittens: die Legalzession nach Absatz zwei. Soweit ein Gesamtschuldner den Gläubiger befriedigt und von den "
     "übrigen Schuldnern Ausgleichung verlangen kann, geht die Forderung des Gläubigers gegen die übrigen Schuldner auf ihn "
     "über. [ueber]Die Forderung des Versorgers gegen Lars geht also kraft Gesetzes auf Insa über, soweit sie Ausgleich "
     "verlangen kann. [sich]Nach den Paragrafen vierhundertzwölf und vierhunderteins gehen dabei Sicherheiten wie eine "
     "Bürgschaft mit, wie bei der Abtretung.", P),
    ("[neben]Absatz eins und Absatz zwei sind also zwei Anspruchsgrundlagen. [neben2]Nach dem Bundesgerichtshof bestehen "
     "sie selbständig nebeneinander.", PS),
    # --- I Rechnung -------------------------------------------------------------------------------------------------------
    ("[rech]Jetzt rechnen wir. [r1]Insa hat neunhundert Euro gezahlt, ihr eigener Anteil sind dreihundert. [r2]Lars "
     "schuldet seinen Anteil von dreihundert Euro [r3]plus die Hälfte des Ausfalls von Rieke, hundertfünfzig. "
     "[r4]Zusammen vierhundertfünfzig Euro. [r5]Insa trägt am Ende ebenfalls vierhundertfünfzig.", PS),
    # --- J Ergebnis -------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Der Versorger durfte die vollen neunhundert Euro von Insa verlangen. [erg2]Lars muss Insa "
     "vierhundertfünfzig Euro erstatten, nach Paragraf vierhundertsechsundzwanzig Absatz eins und aus der übergegangenen "
     "Forderung nach Absatz zwei. [erg3]Mit dreihundert Euro ist es nicht getan.", 0.3),
    ("[la2]Na gut, dann vierhundertfünfzig.", PS, "Lars"),
    # --- K Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe den Regress immer auf beiden Wegen. [tipp2]Die übergegangene Forderung bringt Sicherheiten "
     "mit, nach Paragraf vierhundertzwölf in Verbindung mit Paragraf vierhundertvier aber auch die Einwendungen aus dem "
     "Vertrag mit dem Gläubiger. [tipp3]Verjährung und Einreden prüfst du für beide Ansprüche getrennt. [tipp4]Und der "
     "Ausgleichsanspruch entsteht schon mit der Gesamtschuld: Vor der Zahlung ist er auf Mitwirkung und Befreiung "
     "gerichtet, danach auf Zahlung.", PS),
    # --- L Klausurschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: [k1]Römisch eins: Außenverhältnis. [k1a]Eins: Entstehen der Gesamtschuld nach Paragraf "
     "vierhunderteinundzwanzig, durch Vertrag oder Gesetz. [k1b]Zwei: Wirkung der Erfüllung, Paragraf "
     "vierhundertzweiundzwanzig. [k2]Römisch zwei: Innenverhältnis. [k2a]Eins: Ausgleich nach Paragraf "
     "vierhundertsechsundzwanzig Absatz eins Satz eins. [k2b]Zwei: Ausfall nach Satz zwei. [k2c]Drei: Legalzession nach "
     "Absatz zwei.", PS),
    # --- M Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Außen haftet jeder auf das Ganze, innen nur auf seinen Anteil. [mk2]Fällt einer aus, teilen die übrigen "
     "seinen Anteil. [mk3]Und wer zahlt, hat zwei Wege zum Regress: Absatz eins und die übergegangene Forderung aus Absatz "
     "zwei.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
