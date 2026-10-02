"""Folge 035 · Tötungsdelikte Überblick: §§ 211–229 StGB inkl. Körperverletzung (Examenswissen, Format Schema).
Überblicksfolge als Landkarte: Lernsituation in der Unibibliothek (Britta, Florian) mit einem Übungsfall auf dem
Whiteboard (Fritz stößt seinen Nachbarn Henning im Treppenhaus; nur abstrakte Symbole, keine Gewaltbilder).
Totschlag § 212 (Wortlaut), Mord § 211 (drei Gruppen), Streit Rspr./Lehre (BGH 5 StR 341/05 Rn. 44–48), §§ 213, 216, 222;
Körperverletzung § 223 (Wortlaut; BGH 3 StR 354/16 Rn. 4, 4 StR 168/13 Rn. 13), § 224 (Wortlaut; BGHSt 47, 383 Rn. 11),
§ 226, § 227 (BGH 5 StR 435/07 Rn. 8), § 229, § 230; Prüfreihenfolge als Konvention; Klausurtipp und Merksatz mit Lexi.
Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.7

STIMMEN = {"Britta": "julia", "Florian": "marc"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Lerngruppe in der Bibliothek ----------------------------------------------------------------------------
    ("[fall]Dienstagabend in der Unibibliothek. [britta]Britta und [florian]Florian lernen für die Strafrechtsklausur. "
     "[fritz]Ihr Übungsfall am Whiteboard: Im Treppenhaus streiten Fritz und sein Nachbar Henning um ein Fahrrad. "
     "[stoss]Fritz stößt Henning, [sturz]und Henning stürzt die Treppe hinunter.", 0.3),
    ("[f1]Klare Sache: Körperverletzung.", 0.3, "Florian"),
    ("[b1]Und wenn Henning dabei stirbt?", 0.4, "Britta"),
    ("[frage]Welches Delikt passt? [frage2]Das hängt von zwei Fragen ab: Welche Folge tritt ein, und was wollte Fritz?", 0.6),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall mit allen Varianten zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Landkarte -----------------------------------------------------------------------------------------------------
    ("[karte]Die Delikte gegen Leib und Leben bilden zwei Säulen: [leben]Tötung [koerper]und Körperverletzung. [grund]Jede "
     "hat einen Grundtatbestand, [hoch]darüber schärfere Formen, [runter]darunter mildere, [folge]dazu schwere Folgen "
     "[fahrl]und ganz unten die Fahrlässigkeit.", PS),
    # --- D Totschlag ------------------------------------------------------------------------------------------------------
    ("[p212]Grundtatbestand der Tötungsdelikte ist der Totschlag, Paragraf zweihundertzwölf: [p212w]Wer einen Menschen tötet, "
     "ohne Mörder zu sein, wird als Totschläger mit Freiheitsstrafe nicht unter fünf Jahren bestraft. [v1]In Variante eins "
     "will Fritz Henning töten, und Henning stirbt. [p212s]Den Tatbestand des Totschlags "
     "erfüllt er.", PS),
    # --- E Mord ----------------------------------------------------------------------------------------------------------
    ("[p211]Mord, Paragraf zweihundertelf, verlangt zusätzlich ein Mordmerkmal. [gruppen]Man ordnet die Merkmale in drei "
     "Gruppen. [g1]Erste Gruppe, die Beweggründe: etwa Mordlust, Habgier oder sonst niedrige Beweggründe. [g2]Zweite Gruppe, "
     "die Art der Tat: heimtückisch, grausam oder mit gemeingefährlichen Mitteln. [g3]Dritte Gruppe, der Zweck: eine andere "
     "Straftat zu ermöglichen oder zu verdecken. [lebensl]Die Strafe: lebenslange Freiheitsstrafe.", PS),
    # --- F Streit Rechtsprechung / Lehre ---------------------------------------------------------------------------------
    ("[streit]Wie hängen Mord und Totschlag zusammen? [lehre]Die Lehre sieht im Totschlag den Grundtatbestand und im Mord "
     "eine Qualifikation. [rspr]Der Bundesgerichtshof behandelt beide bisher als selbständige Tatbestände.", 0.3),
    ("[f2]Und wozu brauche ich den Streit?", 0.4, "Florian"),
    ("[p28]Für Teilnehmer, wegen Paragraf achtundzwanzig. [p28a]Wer als Gehilfe die niedrigen Beweggründe des Täters kennt, "
     "aber nicht teilt, ist nach der Rechtsprechung wegen Beihilfe zum Mord strafbar, gemildert nach Absatz eins. [p28b]Nach "
     "der Lehre nur wegen Beihilfe zum Totschlag. [offen]Der fünfte Strafsenat nannte die Einwände zweitausendsechs gewichtig, "
     "ließ die Frage aber offen.", PS),
    # --- G Milder: §§ 213, 216 --------------------------------------------------------------------------------------------
    ("[milder]Milder sind zwei Vorschriften. [p213]Paragraf zweihundertdreizehn senkt beim minder schweren Fall des "
     "Totschlags die Strafe auf ein bis zehn Jahre, [zorn]etwa wenn das Opfer den Täter ohne dessen Schuld schwer beleidigt "
     "und so auf der Stelle zur Tat hingerissen hat. [p216]Tötung auf Verlangen, Paragraf zweihundertsechzehn, setzt ein "
     "ausdrückliches und ernstliches Verlangen des Getöteten voraus. [s216]Strafe: sechs Monate bis fünf Jahre.", PS),
    # --- H Fahrlässige Tötung ----------------------------------------------------------------------------------------------
    ("[p222]Ganz unten steht die fahrlässige Tötung, Paragraf zweihundertzweiundzwanzig. [v2]In Variante zwei rempelt Fritz "
     "Henning beim Tragen des Fahrrads nur aus Unachtsamkeit an. [p222s]Stirbt Henning, drohen bis zu fünf Jahre oder "
     "Geldstrafe.", PS),
    # --- I Körperverletzung -----------------------------------------------------------------------------------------------
    ("[p223]Rechte Säule: Grundtatbestand ist die Körperverletzung, Paragraf zweihundertdreiundzwanzig. [p223w]Strafbar ist, "
     "wer eine andere Person körperlich misshandelt oder an der Gesundheit schädigt. [v3]In Variante drei erleidet Henning "
     "Prellungen. [nicht]Nicht jeder Stoß genügt: Die Behandlung muss das körperliche Wohlbefinden nicht nur unerheblich "
     "beeinträchtigen. [prell]Prellungen tun das; zugleich schädigen sie die Gesundheit.", PS),
    # --- J Gefährliche Körperverletzung ----------------------------------------------------------------------------------
    ("[p224]Eine Stufe höher steht die gefährliche Körperverletzung, Paragraf zweihundertvierundzwanzig, [nall]mit fünf "
     "Begehungsweisen: [n1]Gift oder andere gesundheitsschädliche Stoffe, [n2]eine Waffe oder ein anderes gefährliches "
     "Werkzeug, [n3]ein hinterlistiger Überfall, [n4]die gemeinschaftliche Begehung mit einem anderen Beteiligten [n5]und "
     "eine das Leben gefährdende Behandlung. [v4]In Variante vier versperrt ein Freund von Fritz Henning "
     "bewusst den Weg. [nr4]Nach dem Bundesgerichtshof genügt das für Nummer vier: Ein zweiter Beteiligter verstärkt am "
     "Tatort bewusst die Wirkung des Angriffs. [nr5]Nummer fünf prüfst du gesondert.", PS),
    # --- K Schwere Körperverletzung ---------------------------------------------------------------------------------------
    ("[p226]Paragraf zweihundertsechsundzwanzig, die schwere Körperverletzung, knüpft an schwere Dauerfolgen an, [folgen]etwa "
     "den Verlust eines wichtigen Glieds [v5]oder, wie in Variante fünf, des Sehvermögens auf einem Auge. [p18]Für diese Folge "
     "genügt nach Paragraf achtzehn wenigstens Fahrlässigkeit. [abs2]Verursacht Fritz sie absichtlich oder wissentlich, gilt "
     "Absatz zwei: mindestens drei Jahre.", PS),
    # --- L Körperverletzung mit Todesfolge --------------------------------------------------------------------------------
    ("[p227]Und wenn Henning stirbt, obwohl Fritz ihn nur verletzen wollte, wie in [v6]Variante sechs? [k227]Dann greift die "
     "Körperverletzung mit Todesfolge, Paragraf zweihundertsiebenundzwanzig. [gefahr]Ein bloßer Kausalzusammenhang genügt dem "
     "Bundesgerichtshof nicht: Im Tod muss sich die spezifische Gefahr der Körperverletzung niederschlagen. [treppe]Beim Stoß "
     "auf der Treppe liegt das nahe. [t227]Für den Tod genügt Fahrlässigkeit, die Strafe beträgt mindestens drei Jahre.", PS),
    # --- M Fahrlässige Körperverletzung, Strafantrag ----------------------------------------------------------------------
    ("[p229]Daneben steht die fahrlässige Körperverletzung, Paragraf zweihundertneunundzwanzig, [v2b]etwa wenn Henning in "
     "Variante zwei verletzt überlebt. [p230]Wichtig: Einfache und fahrlässige Körperverletzung werden nach Paragraf "
     "zweihundertdreißig nur auf Antrag verfolgt, [oeff]außer die Strafverfolgungsbehörde bejaht ein besonderes öffentliches "
     "Interesse.", PS),
    # --- N Prüfreihenfolge ------------------------------------------------------------------------------------------------
    ("[reihe]Und womit fängst du an? [r1]Als Faustregel mit dem schwersten Delikt. Bei einem Todesfall also zuerst die "
     "vorsätzliche Tötung: [r2]Totschlag und Mord. [r3]Fehlt der "
     "Tötungsvorsatz, folgen die Körperverletzungsdelikte bis zur Todesfolge. [r4]Fahrlässigkeit kommt zuletzt. [konv]Das ist "
     "Klausurkonvention, kein Gesetz.", PS),
    # --- O Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Ordne die Mordmerkmale im Aufbau richtig ein. [tipp2]Die zweite Gruppe ist tatbezogen: Prüfe sie im "
     "objektiven Tatbestand, der Vorsatz muss sie umfassen. [tipp3]Die erste und dritte Gruppe sind täterbezogen und gehören "
     "in den subjektiven Tatbestand.", PS),
    # --- P Klausurschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Römisch eins: vorsätzliche Tötung, also Totschlag und Mord, [k1b]dazu die Paragrafen "
     "zweihundertdreizehn und zweihundertsechzehn. [k2]Römisch zwei: Körperverletzung, [k2b]gefährliche, [k2c]schwere und "
     "mit Todesfolge. [k3]Römisch drei: die Fahrlässigkeitsdelikte. [k4]Am Ende der Strafantrag.", PS),
    # --- Q Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Grundtatbestände sind Totschlag und Körperverletzung. [m2]Mordmerkmale und die Nummern des Paragrafen "
     "zweihundertvierundzwanzig führen zu schärferer Strafe. [m3]Für schwere Folgen genügt nach Paragraf achtzehn wenigstens "
     "Fahrlässigkeit.", 1.3),
]
