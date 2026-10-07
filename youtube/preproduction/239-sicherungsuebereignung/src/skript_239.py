"""Folge 239 · Sicherungsübereignung: Du fährst das Auto, es gehört der Bank (Mi · Examenswissen · Sachenrecht, Format Schema).
Beispielfall nach dem Plan-Hook („Die Bank finanziert deinen Firmenwagen und lässt ihn sich zur Sicherheit übereignen.“):
Sieglinde (Malermeisterin, eigener Malerbetrieb) braucht einen neuen Transporter. Ihre Bank (ohne Namen, keine echte Marke)
leiht ihr 30.000 €; Bankberater Herr Lohberg verlangt den Transporter als Sicherheit, sie darf ihn nutzen, solange sie die
Raten zahlt. Sie kauft den Wagen beim Autohändler, zahlt mit dem Kredit, bekommt ihn übergeben (Eigentum nach § 929 S. 1),
unterschreibt danach bei der Bank Sicherungsvertrag und Übereignung und fährt den Wagen weiter jeden Tag.
Schema: Problem (Übergabe passt nicht, Besitzkonstitut; Verweis 179) → §§ 929 S. 1, 930 (Wortlautkarten) → I. Einigung
(Trennung vom Sicherungsvertrag) → II. Besitzmittlungsverhältnis (§ 868 Wortlautkarte; Sicherungsvertrag nach h. M.;
konkreter Inhalt BGH V ZR 92/25 Rn. 20) → III. Berechtigung → IV. Bestimmtheit (V ZR 174/21 Rn. 10, 13; Raumsicherungsvertrag
IX ZR 110/17 Rn. 3) → Treuhand (VI ZR 174/24 Rn. 27; Rückübereignung IX ZR 208/11 Rn. 11, IX ZR 177/15 Rn. 11; § 158 II) →
Insolvenz (§ 51 Nr. 1 InsO Wortlautkarte; IX ZR 156/12 Rn. 9; §§ 166, 170 InsO) → Einzelvollstreckung (§ 771 ZPO, h. M.;
vgl. IX ZR 181/05 Rn. 2, 10 f.; Verweis 096) → Abgrenzung Eigentumsvorbehalt (§ 449 I; Verweis 139) → Klausurtipp (§§ 985,
986) → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Figuren: Sieglinde (hilde), Herr Lohberg (christian); die Gerichtsvollzieherin spricht nicht; Lexi/Erzählerin Carla.
Namen nie im Genitiv. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue; jede Marke genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Sieglinde": "hilde", "Lohberg": "christian"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: in der Bank -------------------------------------------------------------------------------------------
    ("[fall]Die Bank finanziert deinen Firmenwagen und lässt ihn sich zur Sicherheit übereignen. [du]Du fährst das Auto, "
     "aber es gehört der Bank. [sieg]So geht es Sieglinde. [maler]Sie führt einen Malerbetrieb und braucht einen neuen "
     "Transporter. [lohb]In der Bank sitzt sie bei Herrn Lohberg.", P),
    ("[lo1]Wir leihen Ihnen dreißigtausend Euro. Als Sicherheit übereignen Sie uns den Transporter.", P, "Lohberg"),
    ("[si1]Und womit fahre ich dann zu meinen Kunden?", P, "Sieglinde"),
    ("[lo2]Den Wagen behalten Sie. Sie dürfen ihn nutzen, solange Sie die Raten zahlen.", P, "Lohberg"),
    # --- A2 Fall: der Transporter ---------------------------------------------------------------------------------------
    ("[kauf]Sieglinde kauft den Transporter beim Autohändler, bezahlt ihn mit dem Kredit und bekommt ihn übergeben. "
     "[unter]Dann unterschreibt sie bei der Bank den Sicherungsvertrag mit der Übereignung. [taeg]Seitdem fährt sie jeden "
     "Tag damit zu ihren Kunden.", P),
    ("[frage]Wem gehört der Transporter jetzt? [frage2]Und was gilt, wenn Sieglinde pleitegeht oder ein anderer Gläubiger "
     "den Wagen pfänden lässt?", PS),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Das Problem ----------------------------------------------------------------------------------------------------
    ("[prob]Das Problem: Die Bank will Eigentümerin werden, Sieglinde braucht den Wagen. [prob2]Eine Übergabe nach "
     "Paragraf neunhundertneunundzwanzig Satz eins scheidet deshalb aus. [prob3]Die Lösung ist das Besitzkonstitut: Statt "
     "der Übergabe vereinbaren beide ein Besitzmittlungsverhältnis. [prob4]Alle Übergabesurrogate erklärt das Video zum "
     "Besitzkonstitut.", PS),
    # --- D §§ 929 Satz 1, 930 (Wortlaut) ------------------------------------------------------------------------------------
    ("[norm]Prüfen musst du also Paragraf neunhundertneunundzwanzig Satz eins in Verbindung mit Paragraf "
     "neunhundertdreißig. [w930]Dort heißt es: Ist der Eigentümer im Besitz der Sache, so kann die Übergabe dadurch "
     "ersetzt werden, dass zwischen ihm und dem Erwerber ein Rechtsverhältnis vereinbart wird, vermöge dessen der Erwerber "
     "den mittelbaren Besitz erlangt. [vier]Daraus folgen vier Prüfungspunkte: [p1]Einigung, [p2]Besitzmittlungsverhältnis, "
     "[p3]Berechtigung [p4]und Bestimmtheit.", PS),
    # --- E I. Einigung ----------------------------------------------------------------------------------------------------
    ("[einig]Erstens die Einigung. Sieglinde und die Bank sind sich einig, dass das Eigentum am Transporter auf die Bank "
     "übergeht, und zwar zur Sicherheit für den Kredit. [trenn]Davon zu trennen ist der Sicherungsvertrag. Er ist das "
     "schuldrechtliche Geschäft, die Übereignung das dingliche.", P),
    # --- F II. Besitzmittlungsverhältnis, § 868 (Wortlaut) -------------------------------------------------------------------
    ("[bmv]Zweitens das Besitzmittlungsverhältnis. [w868]Paragraf achthundertachtundsechzig nennt etwa Miete, Verwahrung "
     "oder ein ähnliches Verhältnis, das den Besitzer auf Zeit zum Besitz berechtigt oder verpflichtet. [sa]Nach "
     "herrschender Meinung genügt dafür der Sicherungsvertrag selbst. [sa2]Er erlaubt Sieglinde, den Wagen zu nutzen, "
     "solange sie zahlt. Zahlt sie nicht mehr, muss sie ihn herausgeben. [konk]Wichtig ist der konkrete Inhalt: Nach dem "
     "Bundesgerichtshof muss das Verhältnis den Besitzer auf Zeit zum Besitz berechtigen. [besitz]So bleibt Sieglinde "
     "unmittelbare Besitzerin, und die Bank wird mittelbare Besitzerin.", P),
    # --- G III. Berechtigung --------------------------------------------------------------------------------------------------
    ("[ber]Drittens die Berechtigung. Sieglinde muss Eigentümerin sein. [ber2]Das ist sie: Der Händler hat ihr den "
     "Transporter übergeben und übereignet.", P),
    # --- H IV. Bestimmtheit, Raumsicherungsvertrag ------------------------------------------------------------------------------
    ("[best]Viertens die Bestimmtheit. Die Einigung muss sich auf eine bestimmte Sache beziehen. [best2]Beim Transporter "
     "ist das leicht, denn er steht mit seiner Fahrzeug-Identifizierungsnummer im Vertrag. [best3]Schwieriger ist ein "
     "Warenlager mit wechselndem Bestand. [best4]Lassen sich die Sachen nicht anders eindeutig feststellen, verlangt der "
     "Bundesgerichtshof eine räumliche Abgrenzung, etwa alle Waren in Halle zwei. [raum]Das ist der "
     "Raumsicherungsvertrag. [zw]Zwischenergebnis: Die Bank ist Eigentümerin des Transporters.", PS),
    # --- I Treuhand, Rückübereignung ----------------------------------------------------------------------------------------------
    ("[treu]Und zwar volle Eigentümerin. Sicherungseigentum ist nach dem Bundesgerichtshof echtes Eigentum. [treu2]Im "
     "Innenverhältnis bindet der Sicherungsvertrag die Bank aber wie einen Treuhänder: Sie hält das Eigentum nur als "
     "Sicherheit. [verw]Verwerten darf sie den Wagen nach dem Vertrag erst, wenn Sieglinde nicht mehr zahlt. [rueck]Ist "
     "der Kredit getilgt, muss die Bank den Wagen zurückübereignen. Das folgt schon aus dem Zweck des Sicherungsvertrags. "
     "[aufl]Anders, wenn die Übereignung auflösend bedingt vereinbart ist: Dann fällt das Eigentum mit der letzten Rate "
     "von selbst zurück, Paragraf hundertachtundfünfzig Absatz zwei.", PS),
    # --- J Insolvenz: § 51 Nr. 1 InsO (Wortlaut) ------------------------------------------------------------------------------------
    ("[ins]Was passiert, wenn Sieglinde insolvent wird? [ins2]Dann kann die Bank den Wagen nicht wie eine fremde Sache "
     "aussondern. [w51]Paragraf einundfünfzig Nummer eins der Insolvenzordnung stellt sie einem Pfandgläubiger gleich, "
     "denn ihr hat der Schuldner zur Sicherung eines Anspruchs eine bewegliche Sache übereignet. [abs]Sie hat also nur "
     "ein Absonderungsrecht. [abs2]Hat der Insolvenzverwalter den Wagen, verwertet er ihn und befriedigt die Bank aus dem "
     "Erlös, nach Abzug der Kosten.", PS),
    # --- K Einzelvollstreckung: § 771 ZPO -------------------------------------------------------------------------------------------
    ("[zv]Anders in der Einzelvollstreckung. [zv2]Lässt ein anderer Gläubiger von Sieglinde den Transporter pfänden, "
     "[zv3]kann sich die Bank nach herrschender Meinung als Eigentümerin mit der Drittwiderspruchsklage wehren, Paragraf "
     "siebenhunderteinundsiebzig der Zivilprozessordnung. [zv4]Mehr dazu im Video zur Drittwiderspruchsklage.", PS),
    # --- L Abgrenzung Eigentumsvorbehalt ----------------------------------------------------------------------------------------------
    ("[ev]Nicht verwechseln mit dem Eigentumsvorbehalt: Dort bleibt der Verkäufer Eigentümer, bis der Kaufpreis bezahlt "
     "ist. [ev2]Bei der Sicherungsübereignung überträgt dagegen der Kreditnehmer sein Eigentum auf den Kreditgeber. "
     "[ev3]Mehr dazu im Video zum Eigentumsvorbehalt.", PS),
    # --- M Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Oft steckt die Sicherungsübereignung im Herausgabeanspruch der Bank aus Paragraf "
     "neunhundertfünfundachtzig. [tipp2]Dann prüfst du sie inzident beim Eigentum der Bank. [tipp3]Und beim Recht zum "
     "Besitz schaust du in den Sicherungsvertrag: Solange Sieglinde zahlt, darf sie den Wagen behalten, Paragraf "
     "neunhundertsechsundachtzig.", PS),
    # --- N Klausurschema ----------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Sicherungsübereignung: [k1]Römisch eins: Einigung, zur Sicherheit. [k2]Römisch zwei: Besitzmittlungsverhältnis "
     "statt Übergabe, meist der Sicherungsvertrag. [k3]Römisch drei: Berechtigung des Sicherungsgebers. [k4]Römisch vier: "
     "Bestimmtheit, bei Warenlagern etwa durch Raumsicherung.", PS),
    # --- O Merksatz (Lexi) ------------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Bei der Sicherungsübereignung ersetzt ein Besitzmittlungsverhältnis die Übergabe, meist der "
     "Sicherungsvertrag selbst. [mk2]Die Bank wird volle Eigentümerin, bleibt aber gebunden. [mk3]Und in der Insolvenz des "
     "Sicherungsgebers hat sie nur ein Absonderungsrecht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
    assert not re.search(r"\b(Sieglindes|Lohbergs)\b", text), "Genitiv eines Namens"
    assert not re.search(r"\d", text), "Ziffer im Sprechtext"
    assert not re.search(r"\b(BGB|ZPO|InsO|BGH)\b", text), "Abkürzung im Sprechtext"
