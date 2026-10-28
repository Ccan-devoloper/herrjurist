"""Folge 127 · Costa/ENEL: Anwendungsvorrang – EU-Recht verdrängt deutsches Recht (Mo · Der Fall · Öffentliches Recht/
Europarecht, Format Klassiker-Fall). Hook nach dem Plan („Ein deutsches Gesetz verbietet, was eine EU-Verordnung
ausdrücklich erlaubt – woran hält sich das Amt?“) als Übungsfall: Hedwig (Limonadenmanufaktur) will eine Limonade mit einem
neuen Süßstoff verkaufen; eine EU-Verordnung lässt ihn ausdrücklich zu, ein deutsches Gesetz verbietet ihn; Herr Lammert
(Lebensmittelüberwachung) will den Verkauf untersagen. Danach der echte Fall sachlich: EuGH, Urt. v. 15.7.1964 – Rs. 6/64
(Costa/ENEL), Slg. 1964, 1253 (S. 1267–1270; Sachverhalt aus den Schlussanträgen GA Lagrange); Simmenthal II (Rs. 106/77,
Rn. 21/23, 24); Fratelli Costanzo (Rs. 103/88, Rn. 31, 33); Anwendungsvorrang statt Geltungsvorrang (IN.CO.GE.'90,
C-10/97, Rn. 21; BVerfGE 123, 267 Rn. 335); Rechtsgrundlage: kein Vorrangartikel (Gutachten zur Erklärung Nr. 17),
Erklärung Nr. 17 (Wortlaut auszugsweise), Art. 4 Abs. 3 EUV (Wortlaut; C-430/21 Rn. 55); Grenzen aus deutscher Sicht
(BVerfGE 123, 267 Rn. 240 f.); Lösung mit Art. 288 Abs. 2 AEUV (Wortlaut) → Ergebnis → Klausurtipp (C-430/21 Rn. 53) →
Schema → Merksatz. Belege: ../RECHTSSTAND.md. Herr Costa nur namentlich, nicht als Figur.
Figuren: Hedwig (sabrina), Herr Lammert (william); Lexi/Erzählerin Carla. Namen nicht im Genitiv.
Abkürzungen im Sprechtext ausgeschrieben („Europäischer Gerichtshof“, „Vertrag über die Arbeitsweise der Union“,
„EU-Vertrag“, „Bundesverfassungsgericht“), weil synth_el sie sonst buchstabiert bzw. nicht kennt.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.55

STIMMEN = {"Hedwig": "sabrina", "Lammert": "william"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Limonade mit neuem Süßstoff ------------------------------------------------------------------------------
    ("[fall]Hedwig betreibt eine kleine Limonadenmanufaktur. [suess]Ihre neue Limonade süßt sie mit einem neuen Süßstoff. "
     "[vo]Eine EU-Verordnung lässt genau diesen Süßstoff für Limonaden ausdrücklich zu. [gesetz]Ein deutsches Gesetz "
     "verbietet ihn dagegen. [amt]Herr Lammert von der Lebensmittelüberwachung kommt zur Kontrolle.", 0.3),
    ("[l1]Das deutsche Gesetz verbietet diesen Süßstoff. Sie dürfen die Limonade nicht verkaufen.", 0.3, "Lammert"),
    ("[h1]Aber die EU-Verordnung erlaubt ihn ausdrücklich!", 0.3, "Hedwig"),
    ("[l2]An das deutsche Gesetz bin ich gebunden.", 0.4, "Lammert"),
    ("[frage]Zwei Regeln, ein Widerspruch. Woran hält sich das Amt? [frage2]Und was wird dann aus dem deutschen Gesetz?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Der echte Fall: Costa gegen Enel ----------------------------------------------------------------------------------
    ("[costa]Die Antwort beginnt mit einem Klassiker: Costa gegen Enel, Europäischer Gerichtshof, Urteil vom fünfzehnten "
     "Juli neunzehnhundertvierundsechzig. [verst]Italien hatte neunzehnhundertzweiundsechzig die Stromwirtschaft "
     "verstaatlicht, Versorger war nun Enel. [rechn]Flaminio Costa, ein Mailänder Rechtsanwalt, "
     "wollte eine Stromrechnung über neunzehnhundertfünfundzwanzig Lire nicht bezahlen. Das Verstaatlichungsgesetz verstoße "
     "gegen den EWG-Vertrag. [vorl]Das Friedensgericht Mailand legte dem Gerichtshof vor, nach dem heutigen "
     "Artikel zweihundertsiebenundsechzig.", PS),
    ("[ital]Die italienische Regierung hielt dagegen: Das Gericht müsse das italienische Gesetz anwenden. [vg]Und das "
     "italienische Verfassungsgericht hatte entschieden: Das jüngere Gesetz geht dem älteren Vertrag vor.", PS),
    ("[ro]Der Gerichtshof sah das anders. Der Vertrag hat eine eigene Rechtsordnung geschaffen, die in die Rechtsordnungen "
     "der Mitgliedstaaten aufgenommen wurde und von ihren Gerichten anzuwenden ist. [zitat]Diesem Recht aus einer autonomen "
     "Rechtsquelle können keine wie immer gearteten innerstaatlichen Rechtsvorschriften vorgehen. [spaet]Auch keine "
     "späteren einseitigen Maßnahmen.", PS),
    # --- D Simmenthal und Costanzo -------------------------------------------------------------------------------------------
    ("[simm]Wer setzt den Vorrang durch? Das klärte neunzehnhundertachtundsiebzig der Fall Simmenthal. [susa]Ein "
     "italienisches Gericht sollte über Gebühren für Rindfleischeinfuhren entscheiden. Nach der damaligen italienischen "
     "Rechtsprechung hätte es das widersprechende Gesetz erst dem Verfassungsgericht vorlegen müssen. [jedes]Der Gerichtshof: "
     "Jedes nationale Gericht muss entgegenstehendes nationales Recht, auch späteres, aus eigener Entscheidungsbefugnis "
     "unangewendet lassen. [warten]Es muss nicht warten, bis Gesetzgeber oder Verfassungsgericht das Gesetz beseitigen. [behoerd]Und seit dem Fall Fratelli Costanzo, neunzehnhundertneunundachtzig, ist klar: Auch die "
     "Verwaltung, bis hin zur Gemeinde, muss widersprechendes nationales Recht unangewendet lassen.", PS),
    # --- E Anwendungsvorrang statt Geltungsvorrang --------------------------------------------------------------------------
    ("[gueltig]Und was passiert mit dem nationalen Gesetz? Es bleibt gültig. [inex]Der Gerichtshof: Die widersprechende "
     "Vorschrift wird nicht inexistent, sondern nur nicht angewendet. [bv335]Das Bundesverfassungsgericht "
     "sagt es so: Der Anwendungsvorrang lässt das deutsche Gesetz in seinem Geltungsanspruch unberührt und drängt es nur in "
     "der Anwendung zurück. [art31]Anders als Bundesrecht, das nach Artikel einunddreißig Grundgesetz Landesrecht bricht. "
     "[gv]Deshalb heißt es Anwendungsvorrang, nicht Geltungsvorrang. [rest]Wo keine Kollision besteht, wird das Gesetz "
     "weiter angewendet.", PS),
    # --- F Rechtsgrundlage: Erklärung Nr. 17 und Art. 4 Abs. 3 EUV ----------------------------------------------------------
    ("[grund]Wo steht der Vorrang eigentlich? Einen ausdrücklichen Vorrangartikel enthalten die Verträge nicht. [e17]Der "
     "Schlussakte von Lissabon ist aber die Erklärung Nummer siebzehn beigefügt. [e17b]Danach haben die Verträge und "
     "das Unionsrecht im Einklang mit der ständigen Rechtsprechung des Gerichtshofs Vorrang vor dem Recht der Mitgliedstaaten. "
     "[gut]Das beigefügte Gutachten stellt fest: Bei Costa war der Vorrang im Vertrag nicht erwähnt, und das ist bis heute "
     "so.", PS),
    ("[a43]Im Vertrag selbst knüpft der Gerichtshof an Artikel vier Absatz drei des EU-Vertrags an, die loyale "
     "Zusammenarbeit. [ergr]Die Mitgliedstaaten ergreifen alle geeigneten Maßnahmen, um ihre Pflichten aus den Verträgen und den "
     "Handlungen der Organe zu erfüllen. "
     "[unterl]Und sie unterlassen alles, was die Ziele der Union gefährden könnte. [ausdr]Die Pflicht zur Nichtanwendung ist nach dem Gerichtshof Ausdruck "
     "dieses Grundsatzes.", PS),
    # --- G Grenzen aus deutscher Sicht --------------------------------------------------------------------------------------
    ("[grenz]Aus deutscher Sicht gilt der Vorrang nicht grenzenlos. Das Bundesverfassungsgericht behält sich eine "
     "Ultra-vires-Kontrolle und eine Identitätskontrolle vor. [nurbv]Feststellen darf einen solchen Verstoß aber nur das "
     "Bundesverfassungsgericht selbst, nicht das Amt.", PS),
    # --- H Lösung: Hedwig und Herr Lammert ------------------------------------------------------------------------------------
    ("[zurueck]Zurück zu Hedwig. [p288]Erstens: Die Verordnung gilt unmittelbar. Artikel zweihundertachtundachtzig Absatz "
     "zwei des Vertrags über die Arbeitsweise der Union: Die Verordnung hat allgemeine Geltung. Sie ist in allen ihren Teilen "
     "verbindlich und gilt unmittelbar in jedem Mitgliedstaat. [quelle]Sie braucht kein Umsetzungsgesetz und gibt auch "
     "Hedwig unmittelbar Rechte.", PS),
    ("[kol]Zweitens: Die Verordnung erlaubt, das Gesetz verbietet. Das klare Verbot lässt sich nicht "
     "unionsrechtskonform auslegen, die Normen kollidieren. [folge]Drittens die Rechtsfolge: "
     "Anwendungsvorrang. Herr Lammert muss das Verbot unangewendet lassen und die Verordnung anwenden. [bleibt]Das Gesetz "
     "bleibt dabei gültig.", PS),
    ("[erg]Ergebnis: Das Amt hält sich an die EU-Verordnung. Es darf Hedwig den Verkauf nicht untersagen.", PS),
    # --- I Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bevor du ein Gesetz unangewendet lässt, versuche es unionsrechtskonform auszulegen. [tipp2]Erst "
     "wenn das nicht geht, greift der Anwendungsvorrang. [tipp3]Und schreib nie, das deutsche Gesetz sei nichtig. Es ist "
     "nur unanwendbar.", PS),
    # --- J Klausurschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Römisch eins: unmittelbar anwendbares Unionsrecht, etwa eine Verordnung. [k2]Römisch zwei: Kollision mit nationalem Recht, [k2a]erst nach dem Versuch "
     "unionsrechtskonformer Auslegung. [k3]Römisch drei, Rechtsfolge: Anwendungsvorrang. [k3a]Gerichte und Behörden lassen "
     "das nationale Recht unangewendet, [k3b]das Gesetz bleibt gültig. [k4]Römisch vier: Grenzen, "
     "Ultra-vires- und Identitätskontrolle, nur durch das Bundesverfassungsgericht.", PS),
    # --- K Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: EU-Recht bricht deutsches Recht nicht, es verdrängt es nur in der Anwendung. [m2]Und daran sind nicht "
     "nur Gerichte gebunden, sondern auch jedes Amt.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
