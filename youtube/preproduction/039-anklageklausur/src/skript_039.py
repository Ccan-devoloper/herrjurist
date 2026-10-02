"""Folge 039 · Anklageklausur Aufbau: Gutachten, Prozessuales, Abschlussverfügung (Fr · 2. Examen · StPO-Praxis, Format Schema).
Beispielfall: Herr Rösch (24, nicht vorbestraft) steckt im Elektronikmarkt Kopfhörer für 249 Euro ein, legt die leere Packung
zurück und zahlt an der Kasse nur eine Cola; Ladendetektiv Herr Brehm stellt ihn. Einlassung: „Bezahlen vergessen.“ Drei Tage
später ruft Rösch Brehm vor dem Markt „Du Idiot!“ zu; Brehm stellt keinen Strafantrag. Im August liegt die Akte bei der
Staatsanwältin. Aufbau: A. materiell-rechtliches Gutachten (hinreichender Tatverdacht, § 170 I StPO; Beweiswürdigung aus der
Akte), B. prozessuales Gutachten (Strafantrag §§ 194 I, 77b StGB; Zuständigkeit § 7 I StPO, §§ 24, 25 GVG; prozessuale Tat,
§ 264 StPO), C. Abschlussverfügung (Einstellung § 170 II StPO, Abgrenzung §§ 153, 154 StPO, Vermerk § 169a StPO, Anklageschrift
§ 200 I, II StPO). Gliederung = Ausbildungs- und Prüfungskonvention, Länderunterschiede ausdrücklich.
Belege je Aussage: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache: Rösch, Brehm; Staatsanwältin ohne Namen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/Prüfpfad."""

P, PS = 0.4, 0.9

STIMMEN = {"Rösch": "niklas", "Brehm": "stephan", "Staatsanwältin": "laura_klar"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: im Elektronikmarkt ----------------------------------------------------------------------------------------
    ("[fall]Ein Elektronikmarkt, Anfang März. [regal]Herr Rösch öffnet am Regal eine Packung Kopfhörer für "
     "zweihundertneunundvierzig Euro. [tasche]Die Kopfhörer steckt er in seine Jackentasche, [leer]die leere Packung legt er "
     "zurück. [kasse]An der Kasse bezahlt er nur eine Cola. [detektiv]Dahinter spricht ihn der Ladendetektiv an, Herr Brehm.", 0.3),
    ("[b1]Bitte zeigen Sie mir Ihre Jackentasche.", 0.4, "Brehm"),
    ("[fund]In der Tasche: die Kopfhörer.", 0.2),
    ("[r1]Die wollte ich doch bezahlen! Das hab ich vergessen.", 0.5, "Rösch"),
    # --- B Fall: vor dem Markt, drei Tage später ---------------------------------------------------------------------------
    ("[drei]Drei Tage später trifft Herr Rösch den Detektiv vor dem Markt.", 0.2),
    ("[r2]Da ist ja der Detektiv. Du Idiot!", 0.4, "Rösch"),
    ("[polizei]Herr Brehm schildert das der Polizei. [kein]Einen Strafantrag stellt er aber nicht.", 0.4),
    # --- C Fall: bei der Staatsanwältin ------------------------------------------------------------------------------------
    ("[akte]Im August liegt die Ermittlungsakte bei der Staatsanwältin.", 0.2),
    ("[sa1]Ein Diebstahl, eine Beleidigung. Was verfüge ich?", 0.4, "Staatsanwältin"),
    ("[frage]Wie baust du diese Anklageklausur auf? [frage2]Vom Gutachten bis zur Abschlussverfügung.", 0.6),
    # --- D Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Aufbau und Länderunterschiede --------------------------------------------------------------------------------------
    ("[aufbau]Die Anklageklausur hat meist drei Teile: [teilA]Teil A, das materiell-rechtliche Gutachten. [teilB]Teil B, das "
     "prozessuale Gutachten. [teilC]Teil C, der praktische Teil mit der Abschlussverfügung. [land]Wie genau du gliederst, ist Ausbildungs- und "
     "Prüfungskonvention und unterscheidet sich von Land zu Land. [strafa]Ob etwa der Strafantrag im materiellen oder im "
     "prozessualen Teil steht, wird unterschiedlich gehandhabt. [vermerk]Maßgeblich sind der Bearbeitervermerk und die Hinweise "
     "deines Prüfungsamts.", PS),
    # --- F Maßstab § 170 I StPO -----------------------------------------------------------------------------------------------
    ("[p170]Den Maßstab setzt Paragraf hundertsiebzig Absatz eins StPO: Bieten die Ermittlungen genügenden Anlass zur Erhebung der "
     "öffentlichen Klage, erhebt die Staatsanwaltschaft sie durch Einreichung einer Anklageschrift. [hinr]Genügender Anlass "
     "heißt hinreichender Tatverdacht. [wahr]Nach dem Bundesgerichtshof muss eine Verurteilung bei vorläufiger Bewertung "
     "wahrscheinlich sein.", PS),
    # --- G A. Materiell-rechtliches Gutachten -----------------------------------------------------------------------------------
    ("[mat]Teil A fragt deshalb zweierlei: [mat1]Ist die Tat strafbar? [mat2]Und lässt sie sich mit den Beweismitteln der Akte "
     "nachweisen? [dieb]Erst der Diebstahl, Paragraf zweihundertzweiundvierzig StGB. [weg]Fremde Kopfhörer eingesteckt, an der "
     "Kasse nicht bezahlt: Wegnahme. [einl]Herr Rösch sagt, er habe das Bezahlen vergessen. Dann fehlten Vorsatz und "
     "Zueignungsabsicht.", P),
    ("[bw]Jetzt kommt die Beweiswürdigung aus der Akte. [bw1]Das Video zeigt, wie er die Packung öffnet und leer zurücklegt. "
     "[bw2]Das spricht gegen ein Versehen, zumal er an der Kasse die Cola bezahlt. [bw3]Die Einlassung überzeugt nicht. Eine "
     "Verurteilung ist wahrscheinlich: hinreichender Tatverdacht.", P),
    ("[bel]Dann die Beleidigung, Paragraf hundertfünfundachtzig StGB. [offen]Ob das Schimpfwort hier strafbar ist, kann "
     "offenbleiben. Herr Brehm wäre Zeuge. [scheit]Das Verfahren scheitert an etwas anderem.", PS),
    # --- H B. Prozessuales Gutachten ------------------------------------------------------------------------------------------
    ("[proz]Teil B, das prozessuale Gutachten. [pv]Hier prüfst du die Prozessvoraussetzungen. [p194]Die Beleidigung wird nur "
     "auf Antrag verfolgt, Paragraf hundertvierundneunzig StGB. [frist]Die Frist beträgt drei Monate ab Kenntnis von Tat und "
     "Täter, Paragraf siebenundsiebzig b. [juni]Herr Brehm hat keinen Antrag gestellt, die Frist ist im Juni abgelaufen. "
     "[hind]Das ist ein Verfahrenshindernis. Eine Verurteilung ist ausgeschlossen. [diebst]Der Diebstahl braucht keinen "
     "Strafantrag: Kopfhörer für zweihundertneunundvierzig Euro sind nicht geringwertig.", P),
    ("[zust]Dann die Zuständigkeit. [oertl]Örtlich das Gericht des Tatorts, Paragraf sieben StPO. [sachl]Sachlich das "
     "Amtsgericht, Paragraf vierundzwanzig Gerichtsverfassungsgesetz. [strafr]Und weil es um ein Vergehen geht und keine höhere Strafe als zwei Jahre "
     "Freiheitsstrafe zu erwarten ist, der Strafrichter, Paragraf fünfundzwanzig.", P),
    ("[tat]Wichtig ist der prozessuale Tatbegriff, Paragraf zweihundertvierundsechzig StPO. [ges]Tat ist nach dem "
     "Bundesgerichtshof der geschichtliche Vorgang, der nach natürlicher Auffassung ein einheitliches Geschehen bildet. "
     "[zwei]Der Diebstahl im Markt und die Beleidigung drei Tage später sind also zwei Taten. [jede]Und jede Tat braucht ihre "
     "eigene Abschlussentscheidung.", PS),
    # --- I C. Abschlussverfügung -----------------------------------------------------------------------------------------------
    ("[verf]Teil C, die Abschlussverfügung. [p170b]Für die Beleidigung gilt Paragraf hundertsiebzig Absatz zwei: Andernfalls "
     "stellt die Staatsanwaltschaft das Verfahren ein. [mitt]Das teilt sie Herrn Rösch mit, denn er wurde als Beschuldigter "
     "vernommen. [opp]Eine Einstellung nach Paragraf hundertdreiundfünfzig oder hundertvierundfünfzig ist etwas anderes. "
     "[opp2]Sie knüpft nicht an fehlenden Tatverdacht an, sondern an geringe Schuld ohne öffentliches Interesse oder daran, "
     "dass die Strafe neben der für eine andere Tat nicht beträchtlich ins Gewicht fällt.", P),
    ("[verm]Für den Diebstahl vermerkt die Staatsanwältin den Abschluss der Ermittlungen, Paragraf hundertneunundsechzig a, "
     "[ankl]und erhebt Anklage zum Strafrichter.", PS),
    # --- J Anklageschrift § 200 StPO ----------------------------------------------------------------------------------------
    ("[p200]Was in die Anklageschrift gehört, sagt Paragraf zweihundert Absatz eins: [as1]der Angeschuldigte, [as2]die Tat mit "
     "Zeit und Ort, [as3]die gesetzlichen Merkmale [as4]und die anzuwendenden Strafvorschriften. [satz]Das ist der Anklagesatz. "
     "[bm]Dazu kommen die Beweismittel, hier Herr Brehm als Zeuge und das Video, [ger]das Gericht und der Verteidiger, falls er "
     "einen hat.", P),
    ("[wes]Das wesentliche Ergebnis der Ermittlungen darf nach Absatz zwei beim Strafrichter fehlen. [rist]Die Richtlinien für "
     "das Strafverfahren sehen es trotzdem vor, wenn die Sach- oder Rechtslage Schwierigkeiten bietet.", PS),
    # --- K Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bilde zuerst die prozessualen Taten. [tipp2]Dann triffst du für jede eine Entscheidung, Anklage oder "
     "Einstellung. [tipp3]Und in den Anklagesatz gehört das Geschehen, nicht deine Beweiswürdigung.", PS),
    # --- L Klausurschema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Anklageklausur. [sA]Teil A: das materiell-rechtliche Gutachten, für jede Tat Strafbarkeit und "
     "Nachweis. [sB]Teil B: das prozessuale Gutachten, mit Prozessvoraussetzungen, Zuständigkeit und prozessualen Taten. "
     "[sC]Teil C: die Abschlussverfügung. [sC1]Einstellung nach Paragraf hundertsiebzig Absatz zwei, wo der Tatverdacht fehlt oder "
     "ein Hindernis besteht. [sC2]Und für den Rest die Anklageschrift nach Paragraf zweihundert.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Angeklagt wird nur, was hinreichend verdächtig und verfolgbar ist. [mz]Und jede prozessuale Tat bekommt "
     "ihre eigene Entscheidung.", 1.4),
]
