"""Folge 032 · Verhältnismäßigkeit prüfen: Die 4 Schritte im Öffentlichen Recht (Examenswissen, Format Schema).
Beispielfall (Übungsfall, länderneutral, Hook laut Themenplan): Um Graffiti zu stoppen, verbietet das Ordnungsamt einer
Stadt per Allgemeinverfügung den Verkauf aller Spraydosen. Betroffen: Herr Kühn (Farbengeschäft, Art. 12 I GG),
Kundin Frauke (Wandmalerin). Ermächtigungsgrundlage und ihre Voraussetzungen sind unterstellt (Bearbeitervermerk);
geprüft wird nur die Verhältnismäßigkeit. Herleitung (Art. 20 III GG, Rechtsstaatsprinzip, Wesen der Grundrechte),
Prüfungsort (Schranken-Schranke; Ermessensgrenze, § 40 VwVfG), Ausformulierung in § 15 BPolG, die vier Schritte
legitimer Zweck – Geeignetheit – Erforderlichkeit – Angemessenheit, Variante „nur Farbsprühdosen“ für die Abwägung.
Wortlautkarten: Art. 20 III GG (vorgelesen), § 40 VwVfG (vorgelesen), § 15 I, II BPolG (Merkmale).
Fiktive Figuren: Herr Kühn (christian), Frauke (ela_warm), Frau Dörr vom Ordnungsamt (julia).
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Kuehn": "christian", "Frauke": "ela_warm", "Doerr": "julia"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Graffiti in der Altstadt ---------------------------------------------------------------------------
    ("[fall]Montagmorgen in der Altstadt. Über Nacht sind wieder Hauswände besprüht worden. [kuehn]Herr Kühn hat gleich "
     "um die Ecke ein Farbengeschäft. Bei ihm gibt es Lacke, Pinsel und Spraydosen.", 0.3),
    # --- B Fall: die Allgemeinverfügung -------------------------------------------------------------------------------
    ("[frauke]Frauke kauft dort ein, sie malt Wandbilder. [doerr]Da kommt Frau Dörr vom Ordnungsamt mit einer "
     "Allgemeinverfügung.", 0.2),
    ("[do1]Um die Graffiti zu stoppen, darf ab sofort niemand in der Stadt Spraydosen verkaufen. Und zwar alle.", 0.3, "Doerr"),
    ("[ku1]Alle? Auch Deo und Haarspray?", 0.3, "Kuehn"),
    ("[fr1]Ich male nur Wände, die ich bemalen darf. Dafür brauche ich Sprühfarbe.", 0.3, "Frauke"),
    ("[frage]Ist dieses Verbot verhältnismäßig? An diesem Fall lernst du die vier Schritte, die du in jeder Klausur im "
     "Öffentlichen Recht brauchst.", 0.6),
    # --- C Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Herleitung --------------------------------------------------------------------------------------------------
    ("[herk]Woher kommt der Grundsatz? [wl20]Artikel zwanzig Absatz drei: Die Gesetzgebung ist an die verfassungsmäßige "
     "Ordnung, die vollziehende Gewalt und die Rechtsprechung sind an Gesetz und Recht gebunden. [nicht]Das Wort "
     "Verhältnismäßigkeit steht da nicht.", P),
    ("[rsp]Das Bundesverfassungsgericht leitet den Grundsatz aus dem Rechtsstaatsprinzip ab, im Grunde schon aus dem "
     "Wesen der Grundrechte selbst. [wesen]Der Staat darf Freiheit nur so weit beschränken, wie es zum Schutz "
     "öffentlicher Interessen unerlässlich ist. [rang]Der Grundsatz hat Verfassungsrang und gilt auch beim Anwenden "
     "einfacher Gesetze.", PS),
    # --- E Prüfungsort ---------------------------------------------------------------------------------------------------
    ("[ort]Wo prüfst du ihn? In der Grundrechtsprüfung bei den Schranken-Schranken. [art12]Hier greift das Verbot in die "
     "Berufsausübung von Herrn Kühn ein, Artikel zwölf Absatz eins. [ermess]Im Verwaltungsrecht begrenzt der Grundsatz "
     "außerdem das Ermessen der Behörde.", P),
    ("[wl40]Paragraf vierzig Verwaltungsverfahrensgesetz: Ist die Behörde ermächtigt, nach ihrem Ermessen zu handeln, hat "
     "sie ihr Ermessen entsprechend dem Zweck der Ermächtigung auszuüben und die gesetzlichen Grenzen des Ermessens "
     "einzuhalten. [land]Eine Stadt wendet zwar das Verfahrensgesetz ihres Landes an. Die Grenze der "
     "Verhältnismäßigkeit gilt aber schon von Verfassungs wegen.", P),
    ("[wl15]Manche Gesetze schreiben den Grundsatz sogar aus, etwa Paragraf fünfzehn Bundespolizeigesetz. [abs1]Absatz "
     "eins verlangt die Maßnahme, die voraussichtlich am wenigsten beeinträchtigt. [abs2]Absatz zwei verbietet einen "
     "Nachteil, der zum erstrebten Erfolg erkennbar außer Verhältnis steht.", PS),
    # --- F 1. legitimer Zweck --------------------------------------------------------------------------------------------
    ("[s1]Jetzt die vier Schritte. Erstens: der legitime Zweck. [zweckb]Bei einer Behörde zählt der Zweck der "
     "Ermächtigung, hier die Abwehr von Gefahren. [graff]Wer fremde Wände unerlaubt besprüht, begeht eine Sachbeschädigung, "
     "Paragraf dreihundertdrei Absatz zwei Strafgesetzbuch. [legit]Hauswände davor zu schützen, ist ein legitimer Zweck.", P),
    # --- G 2. Geeignetheit -----------------------------------------------------------------------------------------------
    ("[s2]Zweitens: die Geeignetheit. Geeignet ist ein Mittel schon, wenn es den Zweck fördern kann. Die Möglichkeit "
     "genügt.", 0.3),
    ("[ku2]Das bringt doch nichts. Die Sprayer bestellen ihre Dosen einfach im Internet.", 0.3, "Kuehn"),
    ("[foerd]Viele bestimmt. Aber wer um die Ecke keine Dose mehr bekommt, sprayt vielleicht seltener. [geeig]Das Verbot "
     "muss den Zweck nicht vollständig erreichen. Es ist geeignet. [fehl1]Typischer Fehler: die Eignung verneinen, nur "
     "weil ein Mittel nicht perfekt wirkt.", PS),
    # --- H 3. Erforderlichkeit -------------------------------------------------------------------------------------------
    ("[s3]Drittens: die Erforderlichkeit. Es darf kein milderes Mittel geben, das gleich wirksam ist. Beides muss "
     "zusammenkommen. [eind]Die Gleichwertigkeit muss eindeutig feststehen. Dem Gesetzgeber lässt das "
     "Bundesverfassungsgericht dabei einen Einschätzungsspielraum. [jung]Ein Verkaufsverbot nur an Jugendliche wäre "
     "milder, aber nicht gleich wirksam. Auch Erwachsene sprayen.", P),
    ("[farbe]Anders ein Verbot nur für Farbsprühdosen. Mit Deo und Haarspray malt niemand Graffiti. Das engere Verbot "
     "wirkt genauso und belastet weniger. [kein]Das ist eindeutig, da hilft kein Spielraum. [erg1]Das Verbot aller "
     "Spraydosen ist nicht erforderlich. Die Stadt überschreitet die Grenzen ihres Ermessens, die Allgemeinverfügung "
     "ist rechtswidrig.", PS),
    # --- I Variante: nur Farbsprühdosen ------------------------------------------------------------------------------------
    ("[var]Im Gutachten ist die Prüfung hier beendet. Doch die Stadt bessert nach und verbietet nur noch Farbsprühdosen. "
     "[var2]Zweck und Eignung bleiben, ein gleich wirksames milderes Mittel ist nicht ersichtlich. Jetzt entscheidet der "
     "vierte Schritt.", P),
    # --- J 4. Angemessenheit -----------------------------------------------------------------------------------------------
    ("[s4]Viertens: die Angemessenheit, auch Verhältnismäßigkeit im engeren Sinne. Zweck und zu erwartende "
     "Zweckerreichung dürfen nicht außer Verhältnis zur Schwere des Eingriffs stehen. [je]Je empfindlicher der Einzelne "
     "getroffen wird, desto gewichtiger muss das Gemeinwohlinteresse sein.", P),
    ("[last]Auf die eine Seite gehört die Last: Herr Kühn verliert eine ganze Warengruppe, Frauke ihr Arbeitsmaterial "
     "in der Stadt. [streu]Und das Verbot trifft fast nur Menschen, die nichts falsch machen.", 0.3),
    ("[fr2]Ich darf meine Wände doch bemalen. Warum darf ich die Farbe nicht kaufen?", 0.3, "Frauke"),
    ("[nutzen]Auf die andere Seite gehört der Nutzen: Eigentum zu schützen, wiegt schwer. Aber die Sprayer weichen leicht "
     "aus, der Gewinn an Schutz ist klein. [erg2]Deshalb spricht viel dafür, dass auch dieses Verbot unangemessen ist. "
     "Gut begründet ist auch das Gegenteil vertretbar. [abw]Entscheidend ist, dass du gewichtest und nicht nur "
     "behauptest.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die vier Schritte sind Klausurkonvention, das Gesetz schreibt den Aufbau nicht vor. "
     "[ausf]Ausführlich wirst du nur, wo es streitig ist, meist bei Erforderlichkeit und Angemessenheit. "
     "[fehler]Typische Fehler: [t1]behaupten, der Grundsatz stehe im Wortlaut von Artikel zwanzig Absatz drei, "
     "[t2]ein milderes Mittel nennen, das weniger wirksam ist, [t3]und in der Angemessenheit nur das Ergebnis "
     "hinschreiben.", PS),
    # --- L Klausurschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [q0]Verhältnismäßigkeit: [q1]Eins: legitimer Zweck, bei Behörden der Zweck der "
     "Ermächtigung. [q2]Zwei: Geeignetheit, Förderung genügt. [q3]Drei: Erforderlichkeit, kein milderes, gleich "
     "wirksames Mittel. [q4]Vier: Angemessenheit, Abwägung von Eingriffsschwere und Gewicht des Zwecks.", PS),
    # --- M Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein milderes Mittel zählt nur, wenn es genauso gut wirkt. [m2]Und angemessen ist ein Eingriff erst, "
     "wenn sein Nutzen die Last trägt.", 1.4),
]
