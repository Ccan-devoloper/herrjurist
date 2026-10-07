"""Folge 240 · Schwerer Raub § 250: Spielzeugpistole & Labello-Fall (Fr · Klausurpraxis · StGB BT, Format Streitstand).
Fall nach dem Plan-Hook („Ein Räuber bedroht eine Bäckereiverkäuferin mit einer täuschend echt aussehenden Spielzeugpistole“),
zurückhaltend erzählt: Die Spielzeugpistole erscheint nur als stilisiertes, neutral graues Symbol, nie auf eine Person
gerichtet; keine Gewalt im Bild, Wiltrud bleibt unverletzt. Gegenfall: Labello-Fall (BGH NStZ 1997, 184), Lippenpflegestift
als neutrales Icon ohne Marke.
Aufbau: Fall → Frage → Sachverhalt → Raub § 249 bejaht (Verweis Folge 087; Drohung genügt, BGH 2 StR 618/10 Rn. 4) →
§ 250 Abs. 1 Nr. 1 (Wortlautkarte) → Nr. 1a: Waffe (BGHSt 45, 92 = 4 StR 380/98 Rn. 5 f.; Spielzeugpistolen ausgeklammert)
→ Nr. 1b: Scheinwaffe erfasst (BT-Drucks. 13/9064 S. 18; BGH 4 StR 394/06 Rn. 6; 4 StR 61/23 Rn. 5) → Grenze Labello
(4 StR 394/06 Rn. 7–8; 2 StR 618/10 Rn. 4 f. Wasserpistole) mit Kritik (4 StR 394/06 Rn. 8) → Abs. 2 Nr. 1 (Wortlautkarte;
BGHSt 45, 92 Rn. 7; 4 StR 227/07 Rn. 3) → Ergebnis → Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Figuren: Alois (niklas), Ottfried (helmut); Wiltrud spricht nicht. Lexi/Erzählerin Carla. Namen nie im Genitiv.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Alois": "niklas", "Ottfried": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Überfall in der Bäckerei ----------------------------------------------------------------------------
    ("[fall]Ein Räuber bedroht eine Bäckereiverkäuferin mit einer Pistole, die täuschend echt aussieht. [wiltrud]Früh am "
     "Morgen steht Wiltrud allein hinter der Theke einer Bäckerei. [alois]Da kommt Alois herein [zieht]und zieht eine "
     "schwarze Pistole aus der Jacke.", P),
    ("[a1]Keine Bewegung! Das Geld aus der Kasse nehme ich mir selbst.", P, "Alois"),
    ("[weicht]Wiltrud hält die Pistole für echt und weicht zurück. [nimmt]Alois greift in die offene Kasse, nimmt "
     "dreihundert Euro [flieht]und rennt hinaus. Er will das Geld behalten.", P),
    # --- A2 Fall: die Pistole an der Tür, Frage ---------------------------------------------------------------------------
    ("[faellt]An der Tür fällt ihm die Pistole aus der Jacke. [ottfried]Bäckermeister Ottfried kommt aus der Backstube und "
     "hebt sie auf.", P),
    ("[o1]Die ist ja aus Plastik. Ein Spielzeug, aber täuschend echt.", P, "Ottfried"),
    ("[unverl]Wiltrud ist zum Glück unverletzt. [frage]Hat Alois einen schweren Raub begangen? [frage2]Und was gilt, wenn er "
     "Wiltrud nur einen Lippenpflegestift in den Rücken drückt?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Grundtatbestand § 249 ------------------------------------------------------------------------------------------
    ("[raub]Zuerst der Grundtatbestand, der Raub nach Paragraf zweihundertneunundvierzig. [r1]Das Geld ist für Alois eine "
     "fremde bewegliche Sache, und er nimmt es gegen den Willen von Wiltrud an sich. [r2]Das Nötigungsmittel ist eine "
     "Drohung mit gegenwärtiger Gefahr für Leib oder Leben. [r3]Dass Alois nicht schießen kann, schadet nicht. Es genügt, "
     "dass Wiltrud die Drohung für möglich halten soll. [r4]Er droht, um das Geld zu nehmen, mit Vorsatz und "
     "Zueignungsabsicht. Der Raub liegt vor. [r5]Die Einzelheiten kennst du aus unserer Folge zum Raub. [r6]Hätte Wiltrud "
     "ihm das Geld selbst gegeben, wäre es räuberische Erpressung. Auch dann gilt Paragraf zweihundertfünfzig, denn der "
     "Täter wird gleich einem Räuber bestraft.", PS),
    # --- D § 250 Abs. 1 Nr. 1 (Wortlaut), Buchstabe a ---------------------------------------------------------------------
    ("[q]Jetzt die Qualifikation, Paragraf zweihundertfünfzig. [w1]Absatz eins: Freiheitsstrafe nicht unter drei Jahren, "
     "wenn der Täter oder ein anderer Beteiligter am Raub, [w1a]nach Nummer eins a eine Waffe oder ein anderes gefährliches "
     "Werkzeug bei sich führt, [w1b]oder nach b sonst ein Werkzeug oder Mittel bei sich führt, um den Widerstand einer "
     "anderen Person durch Gewalt oder Drohung mit Gewalt zu verhindern oder zu überwinden.", PS),
    ("[na]Zuerst Buchstabe a. [na1]Eine Waffe muss nach ihrer Beschaffenheit geeignet sein, erhebliche Verletzungen "
     "zuzufügen. [na2]Spielzeugpistolen klammert der Bundesgerichtshof ausdrücklich aus. [na3]Und ein anderes gefährliches "
     "Werkzeug ist das leichte Plastikspielzeug auch nicht. Buchstabe a scheidet aus.", PS),
    # --- E Buchstabe b: Scheinwaffe erfasst --------------------------------------------------------------------------------
    ("[nb]Bleibt Buchstabe b, sonst ein Werkzeug oder Mittel. [nb1]Hier hat der Gesetzgeber mit dem sechsten "
     "Strafrechtsreformgesetz von neunzehnhundertachtundneunzig die Scheinwaffen erfasst. [nb2]Der Rechtsausschuss nennt "
     "als Beispiel ausdrücklich die Spielzeugpistole. [nb3]Der Bundesgerichtshof folgt dem: Erfasst sind auch Gegenstände, "
     "die objektiv ungefährlich sind und deren Gefährlichkeit nur vorgetäuscht wird. [nb4]Alois führt die Pistole bei sich, "
     "um den Widerstand von Wiltrud durch Drohung mit Gewalt zu verhindern. [nb5]Sie sieht täuschend echt aus, die "
     "Drohwirkung geht vom Gegenstand selbst aus. Buchstabe b ist erfüllt.", PS),
    # --- F Die Grenze: Labello-Fall ---------------------------------------------------------------------------------------
    ("[lab]Doch der Bundesgerichtshof zieht eine Grenze, bekannt als Labello-Fall. [lab1]Abwandlung: Alois hat keine "
     "Pistole. Er drückt Wiltrud von hinten einen Lippenpflegestift in den Rücken. [lab2]Sie hält ihn für die Spitze eines "
     "Messers.", PS),
    ("[lab3]Ist ein Gegenstand schon nach seinem äußeren Erscheinungsbild offensichtlich ungefährlich, fällt er nicht unter "
     "Buchstabe b. [lab4]Dann steht die Täuschung im Vordergrund, nicht der Gegenstand. [lab5]Maßgeblich ist der Blick "
     "eines objektiven Betrachters, nicht, ob das Opfer den Gegenstand sehen kann. [lab6]So reichte auch eine grellbunte "
     "Wasserpistole nicht, die keiner echten Waffe ähnelte, obwohl sie in der Jackentasche verborgen blieb.", PS),
    ("[krit]Teile der Literatur kritisieren, die Grenze sei kaum trennscharf. [krit2]Der Bundesgerichtshof räumt sogar ein, "
     "dass der Wortlaut eher auf die Vorstellung des Täters abstellt. [krit3]Er hält trotzdem an der Grenze fest, so wie es "
     "der Gesetzgeber erwartet hat.", PS),
    # --- G § 250 Abs. 2 Nr. 1 (Wortlaut) -----------------------------------------------------------------------------------
    ("[abs2]Und Absatz zwei? [w2]Nach Nummer eins gilt eine Mindeststrafe von fünf Jahren, wenn der Täter bei der Tat eine "
     "Waffe oder ein anderes gefährliches Werkzeug verwendet. [v1]Verwenden heißt auch: als Drohmittel einsetzen. Das tut "
     "Alois. [v2]Aber die Spielzeugpistole ist eben keine Waffe und kein gefährliches Werkzeug. [v3]Nach ständiger "
     "Rechtsprechung fällt eine Scheinwaffe als Drohmittel nicht unter Absatz zwei Nummer eins, sondern unter Absatz eins "
     "Nummer eins b.", PS),
    # --- H Ergebnis --------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Mit der Spielzeugpistole begeht Alois einen schweren Raub nach Paragraf zweihundertfünfzig Absatz eins "
     "Nummer eins b. [erg2]Die Mindeststrafe beträgt drei Jahre, nicht fünf. [erg3]Mit dem Lippenpflegestift bleibt es beim "
     "Raub nach Paragraf zweihundertneunundvierzig.", PS),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe Paragraf zweihundertfünfzig vom schwersten Fall her. [tipp2]Zuerst Absatz zwei Nummer eins, "
     "das Verwenden einer Waffe. [tipp3]Scheitert es an der Waffe, gehst du zu Absatz eins Nummer eins a und dann zu b. "
     "[tipp4]Bei b sprichst du die Labello-Grenze an: Ist der Gegenstand schon äußerlich offensichtlich ungefährlich?", PS),
    # --- J Klausurschema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema: [s1]Römisch eins: Raub nach Paragraf zweihundertneunundvierzig. [s2]Römisch zwei: die "
     "Qualifikation. [s2a]Erstens Absatz zwei Nummer eins: Waffe oder gefährliches Werkzeug verwendet. [s2b]Zweitens "
     "Absatz eins Nummer eins a: bei sich geführt. [s2c]Drittens Absatz eins Nummer eins b: sonst ein Werkzeug oder Mittel, "
     "mit Verwendungsabsicht [s2d]und nicht offensichtlich ungefährlich. [s2e]Dazu der Vorsatz für die Qualifikation. "
     "[s3]Römisch drei: Rechtswidrigkeit und Schuld.", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Eine Scheinwaffe ist keine Waffe, aber ein sonstiges Mittel nach Absatz eins Nummer eins b. [mk2]Wirkt "
     "der Gegenstand schon äußerlich offensichtlich harmlos, droht der Täter nur durch Täuschung. [mk3]Dann bleibt es beim "
     "einfachen Raub.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
    assert not re.search(r"\b(Alois'|Wiltruds|Ottfrieds)\b", text), "Genitiv eines Namens"
    assert not re.search(r"\d", text), "Ziffer im Sprechtext"
