"""Folge 187 · Bagger trifft Stromkabel: Reiner Vermögensschaden – kein Ersatz? (Mo · Der Fall · Deliktsrecht, Klassiker-Fall).
Fall nach dem Plan-Hook („Ein Bagger beschädigt ein Stromkabel – eine Fabrik zwei Kilometer weiter steht einen Tag still“),
Baustelle und Fabrik fiktiv: Fiete führt ein kleines Tiefbauunternehmen und hebt mit seinem Bagger am Rand eines
Gewerbegebiets einen Graben aus, ohne vorher in die Leitungspläne zu schauen. Die Schaufel reißt ein Stromkabel des örtlichen
Netzbetreibers auf, das das ganze Gewerbegebiet versorgt. Zwei Kilometer weiter fällt in der Fahrradfabrik von Gotthard der
Strom aus; die Fertigung steht einen Tag still (Produktionsausfall 48.000 €). Nichts geht kaputt.
Vorbild ist der Stromkabel-Fall BGH, Urt. v. 9.12.1958 – VI ZR 199/57, BGHZ 29, 65 (Fundstelle gesichert über BGH VI ZR 155/14
Rn. 20; Kerngehalt über neuere Entscheidungen belegt, kein wörtliches Zitat aus BGHZ 29, 65).
Prüfung: § 823 Abs. 1 BGB (Wortlautkarte, wörtlich) → Rechtsgutsliste, Vermögen fehlt; Grund: Entscheidung des Gesetzgebers
gegen eine allgemeine deliktische Haftung für Vermögensschäden (BGH XI ZR 51/10 Rn. 26), Ausnahme § 826 → I. Eigentum: Kabel
gehört dem Netzbetreiber (BGH VI ZR 295/17 Rn. 10), bloße Unterbrechung der Fertigung keine Eigentumsverletzung (BGH III ZR 215/21
Rn. 44), Nutzungsbeeinträchtigung nur bei unmittelbarer Einwirkung auf die Sache (BGH VI ZR 155/14 Rn. 18) → Gegenfall
Substanzschaden: Anlagensteuerung des Asphaltmischwerks (III ZR 215/21 Rn. 7, 41, 44), Untergang von Sachen → II. Gewerbebetrieb:
sonstiges Recht (I ZR 75/13 Rn. 12), Auffangtatbestand (XIII ZR 22/19 Rn. 22), Betriebsbezogenheit (VI ZR 155/14 Rn. 20; BAG
1 AZR 875/13 Rn. 25 mit BGHZ 29, 65 für Versorgungswege) → § 823 Abs. 2 ein Satz mit Verweis auf Folge 158 → Ergebnis →
Klausurtipp (Lexi) → Prüfschema → Merksatz. Belege: ../RECHTSSTAND.md. Schema zu § 823 I nur verwiesen (Folgen 011, 067).
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Volltextsuche 04.10.2026): Fiete, Gotthard
(nie im Genitiv: „die Fahrradfabrik von Gotthard“). Stimmen: Gotthard helmut, Fiete niklas. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Gotthard": "helmut", "Fiete": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Baustelle und Fabrik -------------------------------------------------------------------------------------
    ("[fall]Eine Baustelle am Rand eines Gewerbegebiets. [fiete]Fiete führt ein kleines Tiefbauunternehmen und hebt mit "
     "seinem Bagger einen Graben aus. [plan]In die Leitungspläne hat er vorher nicht geschaut. [treffer]Die Schaufel reißt "
     "ein Stromkabel auf, [netz]das dem örtlichen Netzbetreiber gehört und das ganze Gewerbegebiet versorgt. [fabrik]Zwei "
     "Kilometer weiter liegt die Fahrradfabrik von Gotthard. [dunkel]Dort fällt der Strom aus, [still]und die Fertigung "
     "steht einen ganzen Tag still. [heil]Kaputt geht dabei nichts: Am nächsten Morgen laufen die Maschinen wieder.", P),
    # --- A2 Fall: am Graben ------------------------------------------------------------------------------------------------
    ("[g1]Ein Tag Stillstand kostet mich achtundvierzigtausend Euro. Das zahlen Sie!", P, "Gotthard"),
    ("[f1]Ich habe ein Kabel getroffen, nicht Ihre Fabrik!", P, "Fiete"),
    ("[frage]Muss Fiete den Produktionsausfall ersetzen? [klass]Der Fall ist ein Klassiker: Schon neunzehnhundertachtundfünfzig "
     "entschied der Bundesgerichtshof den Stromkabel-Fall.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Die Norm: § 823 Abs. 1 BGB ---------------------------------------------------------------------------------------
    ("[norm]Anspruchsgrundlage ist Paragraf achthundertdreiundzwanzig Absatz eins BGB: [w1]Wer vorsätzlich oder fahrlässig "
     "das Leben, den Körper, die Gesundheit, die Freiheit, das Eigentum oder ein sonstiges Recht eines anderen widerrechtlich "
     "verletzt, ist dem anderen zum Ersatz des daraus entstehenden Schadens verpflichtet. [schema]Das ganze Prüfschema zeigt "
     "das Video zum Deliktsrecht; hier geht es um das erste Merkmal, die Rechtsgutsverletzung.", P),
    ("[liste]Die Norm zählt bestimmte Rechtsgüter auf. [fehlt]Das Vermögen als solches fehlt. [grund]Das ist gewollt: Der "
     "Gesetzgeber hat sich, so der Bundesgerichtshof, gegen eine allgemeine deliktische Haftung für Vermögensschäden "
     "entschieden. [ufer]Sonst würde die Haftung uferlos, denn ein einziger Kabelschaden kann viele Betriebe treffen. "
     "[ausn]Reines Vermögen schützt das Deliktsrecht nur ausnahmsweise, etwa bei vorsätzlicher sittenwidriger Schädigung "
     "nach Paragraf achthundertsechsundzwanzig.", PS),
    ("[pruef]Also prüfen wir, ob ein geschütztes Recht der Fabrik verletzt ist: [p1]zuerst das Eigentum, [p2]dann den "
     "Gewerbebetrieb.", PS),
    # --- D I. Eigentum -----------------------------------------------------------------------------------------------------
    ("[eig]Erstens: das Eigentum. [kabel]Am Kabel ist es verletzt, doch das Kabel gehört dem Netzbetreiber. [netzan]Er kann "
     "von Fiete Ersatz verlangen, Gotthard nicht. [masch]Und die Maschinen der Fabrik? Sie sind unversehrt. [bgh1]Führt ein "
     "Stromausfall nur dazu, dass die Fertigung vorübergehend unterbrochen wird, ist das nach dem Bundesgerichtshof keine "
     "Eigentumsverletzung. [nutz]Auch eine Beeinträchtigung der Nutzung reicht hier nicht, denn sie setzt eine unmittelbare "
     "Einwirkung auf die Sache selbst voraus. [nutz2]Der Bagger hat die Maschinen nie berührt. [eigerg]Das Eigentum der "
     "Fabrik ist also nicht verletzt.", PS),
    # --- E Gegenfall: Substanzschaden --------------------------------------------------------------------------------------
    ("[gegen]Anders ist es, wenn der Stromausfall Sachen der Fabrik beschädigt. [gg1]So lag es bei einem Asphaltmischwerk: "
     "Dort beschädigte der Ausfall nach einem Kabelschaden die Anlagensteuerung. [gg2]Dann ist das Eigentum verletzt, und "
     "ersetzt werden auch die Folgeschäden des Stillstands. [gg3]Dasselbe gilt, wenn durch den Ausfall Sachen untergehen, "
     "etwa Ware verdirbt.", PS),
    # --- F II. Gewerbebetrieb ----------------------------------------------------------------------------------------------
    ("[gew]Zweitens: das Recht am eingerichteten und ausgeübten Gewerbebetrieb. [sonst]Die Rechtsprechung schützt es als "
     "sonstiges Recht. [auff]Es ist aber nur ein Auffangtatbestand: Es schließt Schutzlücken und dehnt den Schutz nicht "
     "dorthin aus, wo das Gesetz ihn verwehrt. [bez]Deshalb muss der Eingriff betriebsbezogen sein, also unmittelbar gegen "
     "den Betrieb als solchen gerichtet. [subs]Hier traf der Bagger zwei Kilometer entfernt ein Kabel, an dem das ganze "
     "Gewerbegebiet hängt. [zuf]Der Ausfall traf die Fabrik rein zufällig, wie jeden anderen Abnehmer auch. [bgh2]So sah es "
     "schon der Bundesgerichtshof im Stromkabel-Fall: kein betriebsbezogener Eingriff.", PS),
    # --- G § 823 Abs. 2 BGB (ein Satz, Verweis Folge 158) --------------------------------------------------------------------
    ("[abs2]Und Absatz zwei hilft nur, wenn Fiete ein Schutzgesetz verletzt hätte, das gerade auch das Vermögen der Fabrik "
     "schützt; das ist hier nicht ersichtlich, mehr dazu im Video zum Schutzgesetz.", PS),
    # --- H Ergebnis --------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Aus Paragraf achthundertdreiundzwanzig bekommt Gotthard von Fiete nichts. [erg2]Fiete haftet dem "
     "Netzbetreiber für das Kabel. [erg3]Hätte der Ausfall Maschinen beschädigt oder Ware verderben lassen, sähe es anders "
     "aus. [vertrag]Ob die Fabrik vom Netzbetreiber etwas verlangen kann, ist eine eigene Frage.", PS),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst die genannten Rechtsgüter, vor allem das Eigentum. [tp2]Erst wenn sie nicht greifen, "
     "kommt der Gewerbebetrieb als Auffangtatbestand. [tp3]Und dort entscheidet die Betriebsbezogenheit, nicht die Höhe des "
     "Schadens.", PS),
    # --- J Prüfschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für die Rechtsgutsverletzung bei einem Stromausfall. [c1]Römisch eins: Eigentum, also "
     "Substanzschaden oder Nutzungsbeeinträchtigung durch Einwirkung auf die Sache. [c2]Römisch zwei: Gewerbebetrieb, nur "
     "subsidiär und nur bei betriebsbezogenem Eingriff. [c3]Römisch drei: für reines Vermögen vor allem Absatz zwei mit "
     "Schutzgesetz und Paragraf achthundertsechsundzwanzig.", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer nur Geld verliert, ohne dass ein geschütztes Recht verletzt ist, bekommt aus Paragraf "
     "achthundertdreiundzwanzig Absatz eins nichts. [m2]Und der Gewerbebetrieb ist nur bei einem betriebsbezogenen Eingriff "
     "verletzt.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
