"""Folge 142 · Äste auf dem Garagendach: Beseitigungsanspruch aus § 1004 BGB (Mo · Der Fall · Zivilrecht/Sachenrecht,
Format Schema). Übungsfall nach dem Plan-Hook („Die Äste vom Baum des Nachbarn hängen auf dein Garagendach und verstopfen die
Rinne“): Franziska (Nordrhein-Westfalen) hat neben ihrem Haus eine Garage; der große Ahorn ihrer Nachbarin Rosemarie steht vier
Meter von der Grenze entfernt (Grenzabstand nach § 41 NachbG NRW eingehalten). Seit dem letzten Sommer ragen seine Äste über
das Garagendach, im Herbst verstopft das Laub die Dachrinne. Rosemarie lehnt den Rückschnitt ab („Laub im Herbst ist ganz normal“).
Schema: I. Beseitigungsanspruch § 1004 Abs. 1 S. 1 (Wortlautkarte; § 903): 1. Eigentum, 2. Beeinträchtigung (nicht durch
Besitzentziehung), 3. Störerin (Handlungs-/Zustandsstörer; Naturereignis, ordnungsgemäße Bewirtschaftung – BGH V ZR 218/18,
V ZR 102/18; Gegenfall Laub vom Baum selbst bei eingehaltenem Grenzabstand, § 906 Abs. 2 S. 2 analog ein Satz), 4. keine
Duldungspflicht § 1004 Abs. 2: beim Überhang allein § 910 Abs. 2, nicht § 906 (V ZR 102/18 Rn. 8); Verjährung ein Satz;
II. Selbsthilferecht § 910 (Wortlautkarte): Frist, Verhältnis zu § 1004 (gleichrangig, V ZR 102/18 Rn. 5), unverjährbar,
nur Zweige, Baumschutzsatzung ein Satz, Kosten (vgl. V ZR 67/22 Rn. 10); III. Unterlassung § 1004 Abs. 1 S. 2 (ein Satz).
Ergebnis mit Fristsetzung, Klausurtipp und Merksatz mit Lexi. Figuren: Franziska (lucy), Rosemarie (hilde); Lexi/Erzählerin
Carla. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Franziska": "lucy", "Rosemarie": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Garage und Ahorn ---------------------------------------------------------------------------------------------
    ("[fall]Franziska wohnt in Nordrhein-Westfalen und hat neben ihrem Haus eine Garage. [ahorn]Im Garten ihrer Nachbarin "
     "Rosemarie steht ein großer Ahorn, vier Meter von der Grenze entfernt. [aeste]Seit dem letzten Sommer ragen seine Äste "
     "über die Grenze auf das Garagendach. [laub]Im Herbst fällt das Laub in die Dachrinne und verstopft sie. "
     "[leiter]Franziska muss immer wieder auf die Leiter.", 0.25),
    # --- A2 Fall: Gespräch am Zaun ---------------------------------------------------------------------------------------------
    ("[fr1]Rosemarie, kannst du bitte die Äste über meiner Garage zurückschneiden?", 0.25, "Franziska"),
    ("[ro1]Laub im Herbst ist ganz normal. Das ist hier überall so.", 0.3, "Rosemarie"),
    ("[frage]Kann Franziska verlangen, dass Rosemarie die Äste zurückschneidet? [frage2]Und darf sie notfalls selbst zur "
     "Astschere greifen?", 0.5),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.6),
    # --- C § 1004 Abs. 1 Satz 1 (Wortlaut), § 903, vier Prüfungspunkte ---------------------------------------------------------
    ("[p1004]Anspruchsgrundlage ist Paragraf tausendvier Absatz eins Satz eins: [w1004]Wird das Eigentum in anderer Weise als "
     "durch Entziehung oder Vorenthaltung des Besitzes beeinträchtigt, so kann der Eigentümer von dem Störer die Beseitigung "
     "der Beeinträchtigung verlangen. [p903]Die Norm schützt die Befugnis aus Paragraf neunhundertdrei, andere von jeder "
     "Einwirkung auszuschließen. [vier]Du prüfst vier Punkte: [v1]Eigentum, [v2]Beeinträchtigung, [v3]Störer [v4]und keine "
     "Duldungspflicht.", PS),
    # --- D1 1. Eigentum, 2. Beeinträchtigung ------------------------------------------------------------------------------------
    ("[eig]Erstens: Franziska ist Eigentümerin des Grundstücks mit der Garage. [beein]Zweitens: Ihr Eigentum muss "
     "beeinträchtigt sein, und zwar nicht durch Entziehung des Besitzes, dafür gibt es Paragraf neunhundertfünfundachtzig. "
     "[aeste2]Hier ragen fremde Äste über ihr Garagendach, und deren Laub verstopft die Rinne. [beein2]Das ist eine "
     "Beeinträchtigung.", P),
    # --- D2 3. Störerin -----------------------------------------------------------------------------------------------------------
    ("[stoer]Drittens: Rosemarie muss Störerin sein. [hand]Handlungsstörer ist, wer die Beeinträchtigung durch sein Verhalten "
     "verursacht. Das ist Rosemarie nicht. [zust]Sie kommt als Zustandsstörerin in Betracht, denn die Störung geht von ihrem "
     "Baum aus. [natur]Bei Naturereignissen genügt das Eigentum am Baum allein aber nicht. Entscheidend ist nach dem "
     "Bundesgerichtshof, ob das Grundstück ordnungsgemäß bewirtschaftet wird. [grenze]Wer Äste über die Grenze wachsen lässt, "
     "tut das nicht. [stoer2]Rosemarie ist Störerin.", P),
    # --- D3 Gegenfall: Laub vom Baum selbst -----------------------------------------------------------------------------------
    ("[gegen]Anders beim Laub, das der Wind vom Baum selbst herüberweht: [abstand]Hält der Baum den Grenzabstand des "
     "Nachbarrechtsgesetzes ein, hier Paragraf einundvierzig in Nordrhein-Westfalen, ist die Eigentümerin dafür in aller Regel "
     "nicht verantwortlich. [ausgl]Ein Geldausgleich analog Paragraf neunhundertsechs Absatz zwei Satz zwei scheidet dann "
     "ebenfalls aus.", PS),
    # --- D4 4. keine Duldungspflicht: § 910 Abs. 2 statt § 906 -----------------------------------------------------------------
    ("[duld]Viertens: keine Duldungspflicht, Paragraf tausendvier Absatz zwei. [orts]Rosemarie meint, Laub im Herbst sei "
     "normal, und denkt an Paragraf neunhundertsechs mit seinen ortsüblichen Einwirkungen. [nur910]Für herüberragende Zweige "
     "gilt aber allein Paragraf neunhundertzehn Absatz zwei, auch wenn die Störung im Laubfall besteht. Ortsüblichkeit spielt "
     "keine Rolle. [w910b]Dulden muss Franziska den Überhang nur, wenn er die Benutzung ihres Grundstücks nicht "
     "beeinträchtigt. [obj]Das wird objektiv beurteilt; beweisen muss es die Baumeigentümerin. [rinne]Eine verstopfte "
     "Dachrinne ist eine solche Beeinträchtigung. [lnr]Und der eingehaltene Grenzabstand hilft beim Überhang nicht.", P),
    ("[verj]Verjährt ist der Anspruch nicht: Die Frist beträgt drei Jahre, und die Äste ragen erst seit dem letzten Sommer "
     "herüber. [erg1]Franziska kann also verlangen, dass Rosemarie den Überhang beseitigt.", PS),
    # --- E II. Selbsthilferecht § 910 (Wortlaut) -------------------------------------------------------------------------------------
    ("[sh]Daneben hat Franziska ein Selbsthilferecht aus Paragraf neunhundertzehn. [w910]Herüberragende Zweige darf der "
     "Eigentümer abschneiden und behalten, wenn er dem Besitzer des Nachbargrundstücks eine angemessene Frist zur Beseitigung "
     "bestimmt hat und die Beseitigung nicht innerhalb der Frist erfolgt. [w910c]Auch hier gilt: nicht, wenn die Zweige die "
     "Benutzung nicht beeinträchtigen.", P),
    ("[neben]Anspruch und Selbsthilferecht stehen gleichrangig nebeneinander. [nverj]Das Selbsthilferecht ist kein Anspruch "
     "und verjährt nicht. [nurzw]Es erlaubt nur, die Zweige abzuschneiden, nicht den Baum zu fällen. [schutz]Eine Grenze kann "
     "das öffentliche Naturschutzrecht ziehen, etwa eine Baumschutzsatzung der Gemeinde. [kosten]Schneidet Franziska selbst, "
     "kann sie die erforderlichen Kosten von Rosemarie verlangen, denn eigentlich war Rosemarie zur Beseitigung verpflichtet.",
     PS),
    # --- F III. Unterlassung § 1004 Abs. 1 Satz 2 -------------------------------------------------------------------------------------
    ("[unt]Und wenn die Äste wieder hinüberwachsen? [unt2]Sind weitere Beeinträchtigungen zu besorgen, kann Franziska nach "
     "Paragraf tausendvier Absatz eins Satz zwei auf Unterlassung klagen. [wgef]Nach einer Störung ist die Wiederholungsgefahr "
     "meist indiziert.", PS),
    # --- G Ergebnis im Fall --------------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Franziska kann von Rosemarie nach Paragraf tausendvier verlangen, die Äste über der Garage "
     "zurückzuschneiden. [frist]Zugleich setzt sie ihr eine Frist.", 0.25),
    ("[fr2]Bitte schneide die Äste in den nächsten vier Wochen zurück.", 0.25, "Franziska"),
    ("[ro2]Gut, ich kümmere mich darum.", 0.3, "Rosemarie"),
    ("[schnitt]Tut sie es nicht, darf Franziska die Zweige nach Fristablauf an der Grenze selbst abschneiden.", PS),
    # --- H Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bei überhängenden Ästen prüfst du die Duldungspflicht nicht an Paragraf neunhundertsechs, sondern "
     "an Paragraf neunhundertzehn Absatz zwei. [tipp2]Wer mit Ortsüblichkeit argumentiert, verschenkt Punkte. [tipp3]Und nenne "
     "beide Wege: Anspruch und Selbsthilfe.", PS),
    # --- I Klausurschema ------------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: [k1]Römisch eins: Beseitigungsanspruch aus Paragraf tausendvier Absatz eins Satz eins: "
     "[k11]Eigentum, [k12]Beeinträchtigung, nicht durch Besitzentziehung, [k13]Störer, Handlungs- oder Zustandsstörer, "
     "[k14]keine Duldungspflicht, beim Überhang nach Paragraf neunhundertzehn Absatz zwei. [k2]Römisch zwei: "
     "Selbsthilferecht aus Paragraf neunhundertzehn: [k2b]Frist erfolglos abgelaufen, [k2c]Benutzung beeinträchtigt. [k3]Römisch drei: "
     "Unterlassungsanspruch aus Absatz eins Satz zwei, [k3b]Wiederholungsgefahr.", PS),
    # --- J Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Was über die Grenze wächst, muss der Baumeigentümer auf Verlangen zurückschneiden. [m2]Es sei denn, die Zweige "
     "beeinträchtigen die Benutzung des Nachbargrundstücks nicht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
