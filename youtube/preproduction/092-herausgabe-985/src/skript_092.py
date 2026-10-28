"""Folge 092 · § 985 BGB: Der Herausgabeanspruch – Prüfungsschema Vindikation (Mi · Examenswissen · Zivilrecht/Sachenrecht,
Format Schema). Beispielfall nach dem Plan-Hook („Dein Ex hat nach der Trennung deinen Plattenspieler behalten“): Theresa hat
sich lange vor dem Zusammenziehen einen Plattenspieler gekauft. In der gemeinsamen Wohnung darf Clemens ihn mitbenutzen. Nach der
Trennung zieht Theresa aus, der Plattenspieler bleibt bei Clemens; sie fordert ihn zurück, er möchte ihn behalten.
Schema § 985 BGB: (1) Eigentum des Anspruchstellers, historisch geprüft (Erwerb vom Händler, kein Verlust durch Zusammenziehen,
kein Erwerb Dritter – Verweis auf 080/083; § 1006 ein Satz), (2) Besitz des Anspruchsgegners (§ 854, § 868 je ein Satz),
(3) kein Recht zum Besitz § 986 (Mitbenutzung/Leihe endet mit der Rückforderung, § 604; abgeleitetes Besitzrecht ein Satz;
Einwendung, ohne Aktenzeichen; Beweislast beim Besitzer), Rechtsfolge Herausgabe am Ort der Sache (Holschuld), § 604 als
konkurrierender Vertragsanspruch, Ausblick §§ 987 ff. Wortlautkarten § 985 und § 986 Abs. 1 S. 1 BGB; Klausurtipp und Merksatz
mit Lexi. Figuren: Theresa (lucy), Clemens (christian); Lexi/Erzählerin Carla. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Theresa": "lucy", "Clemens": "christian"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Kauf ------------------------------------------------------------------------------------------------
    ("[fall]Theresa kauft sich einen Plattenspieler, [lange]lange bevor sie mit Clemens zusammenzieht.", 0.25),
    ("[th1]Endlich mein eigener Plattenspieler!", 0.3, "Theresa"),
    # --- A2 Fall: die gemeinsame Wohnung ------------------------------------------------------------------------------------
    ("[zusammen]Später ziehen die beiden zusammen. Theresa stellt den Plattenspieler ins gemeinsame Wohnzimmer.", 0.25),
    ("[cl1]Darf ich auch mal Platten auflegen?", 0.25, "Clemens"),
    ("[th2]Klar, nutz ihn ruhig mit.", 0.3, "Theresa"),
    # --- A3 Fall: die Trennung --------------------------------------------------------------------------------------------
    ("[trennung]Nach der Trennung zieht Theresa aus. [bleibt]Der Plattenspieler bleibt in der Wohnung bei Clemens.", 0.25),
    ("[th3]Clemens, ich möchte meinen Plattenspieler zurück.", 0.25, "Theresa"),
    ("[cl2]Wir haben ihn doch zusammen genutzt. Er kann hierbleiben.", 0.3, "Clemens"),
    ("[frage]Kann Theresa den Plattenspieler herausverlangen? [frage2]Und wie prüfst du das in der Klausur?", 0.5),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.6),
    # --- C § 985 (Wortlaut) und drei Prüfungspunkte ------------------------------------------------------------------------
    ("[p985]Anspruchsgrundlage ist Paragraf neunhundertfünfundachtzig: [w985]Der Eigentümer kann von dem Besitzer die "
     "Herausgabe der Sache verlangen. [drei]Daraus folgen drei Prüfungspunkte: [v1]Theresa ist Eigentümerin, "
     "[v2]Clemens ist Besitzer, [v3]und er hat kein Recht zum Besitz.", PS),
    # --- D I. Eigentum, historisch ------------------------------------------------------------------------------------------
    ("[eig]Erstens: das Eigentum. Prüfe es historisch, Schritt für Schritt. [urspr]Am Anfang steht fest: Theresa hat den "
     "Plattenspieler gekauft, und der Händler hat ihn ihr übereignet. [verlust]Dann fragst du: Hat sie das Eigentum später "
     "verloren? [zus2]Durch das Zusammenziehen nicht. Sie hat Clemens den Plattenspieler weder geschenkt noch übereignet, "
     "es fehlt schon an der Einigung. [dritte]Auch kein Dritter hat ihn erworben, etwa gutgläubig. Wie das funktioniert, "
     "erklären die Videos zur Übereignung und zum gutgläubigen Erwerb.", P),
    ("[p1006]Die Eigentumsvermutung für den Besitzer aus Paragraf tausendsechs hilft Clemens nicht, denn fest steht: Er hat "
     "den Plattenspieler nur mitbenutzt und nie Eigentum erworben. [eig2]Theresa ist Eigentümerin geblieben.", PS),
    # --- E II. Besitz -------------------------------------------------------------------------------------------------------
    ("[bes]Zweitens: Clemens muss Besitzer sein. Besitz ist die tatsächliche Gewalt über die Sache, Paragraf "
     "achthundertvierundfünfzig. [bes2]Der Plattenspieler steht in seiner Wohnung, Clemens ist unmittelbarer Besitzer. "
     "[mittel]Auch ein mittelbarer Besitzer nach Paragraf achthundertachtundsechzig, etwa wer die Sache verliehen hat, kann "
     "Anspruchsgegner sein.", PS),
    # --- F III. kein Recht zum Besitz, § 986 Abs. 1 Satz 1 (Wortlaut) -------------------------------------------------------
    ("[rzb]Drittens: Clemens darf kein Recht zum Besitz haben. Paragraf neunhundertsechsundachtzig Absatz eins Satz eins: "
     "[w986]Der Besitzer kann die Herausgabe der Sache verweigern, wenn er oder der mittelbare Besitzer, von dem er sein "
     "Recht zum Besitz ableitet, dem Eigentümer gegenüber zum Besitz berechtigt ist.", P),
    ("[eigen]Ein eigenes Besitzrecht kann aus einem Vertrag folgen. [leihe]Theresa hat Clemens die Mitbenutzung "
     "unentgeltlich erlaubt, etwa als Leihe. Solange durfte er den Plattenspieler besitzen. [ende]Eine feste Zeit war nicht "
     "vereinbart. Spätestens als Theresa ihn nach der Trennung zurückfordert, endet dieses Recht. [abgel]Ein abgeleitetes "
     "Besitzrecht hätte etwa ein Freund, dem Clemens den Plattenspieler weiterleiht, aber nur, wenn Clemens selbst "
     "berechtigt ist und ihn weitergeben darf.", P),
    ("[einw]Wichtig: Das Recht zum Besitz ist eine Einwendung, keine Einrede. Das Gericht beachtet es von Amts wegen, "
     "wenn die Tatsachen vorgetragen sind. [beweis]Darlegen und beweisen muss das Besitzrecht aber Clemens. "
     "[kein]Hier hat er keines mehr.", PS),
    # --- G Ergebnis, Rechtsfolge, Konkurrenzen --------------------------------------------------------------------------------
    ("[erg]Ergebnis: Theresa kann den Plattenspieler nach Paragraf neunhundertfünfundachtzig herausverlangen. "
     "[ort]Herausgeben muss Clemens ihn dort, wo er steht, also in seiner Wohnung. Theresa holt ihn ab, es ist eine "
     "Holschuld.", PS),
    ("[p604]Daneben hat Theresa den vertraglichen Rückgabeanspruch aus der Leihe, Paragraf sechshundertvier. Beide "
     "Ansprüche stehen nebeneinander. [ebv]Ob Clemens außerdem Nutzungen herausgeben oder Schadensersatz leisten muss, "
     "regeln die Paragrafen neunhundertsiebenundachtzig folgende, das Eigentümer-Besitzer-Verhältnis.", PS),
    # --- H Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe das Eigentum immer historisch. [tipp2]Beginne bei der Person, die unstreitig Eigentümerin "
     "war, und prüfe jeden späteren Erwerb der Reihe nach. [tipp3]Wer einfach den heutigen Besitzer für den Eigentümer hält, "
     "verschenkt Punkte.", PS),
    # --- I Klausurschema -----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema für den Herausgabeanspruch aus Paragraf neunhundertfünfundachtzig: [k1]Römisch eins: "
     "Eigentum des Anspruchstellers, [k1b]historisch geprüft. [k2]Römisch zwei: Besitz des Anspruchsgegners, [k2b]unmittelbar "
     "oder mittelbar. [k3]Römisch drei: kein Recht zum Besitz nach Paragraf neunhundertsechsundachtzig, [k3b]eigenes oder "
     "abgeleitetes. [k4]Römisch vier: Rechtsfolge, Herausgabe der Sache.", PS),
    # --- J Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Eigentümer bekommt seine Sache vom Besitzer zurück. [m2]Es sei denn, der Besitzer hat ihm gegenüber "
     "ein Recht zum Besitz.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
