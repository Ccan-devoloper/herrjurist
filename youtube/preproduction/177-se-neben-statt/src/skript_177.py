"""Folge 177 · Schadensersatz neben der Leistung oder statt? Die eine Kontrollfrage (Fr · Klausurpraxis · Zivilrecht/
Schuldrecht AT, Format Abgrenzung). Fall nach dem Plan-Hook („Ein defekter Chip zerstört eine bis dahin intakte
Steuerungseinheit – was ersetzt welcher Anspruch?“): Elfriede (Druckerei) kauft bei Dietrich, der Steuerchips selbst
herstellt, einen Chip zum Nachrüsten ihrer Druckmaschine für 300 €. Der Chip ist fehlerhaft (Fertigungsfehler), überhitzt
und zerstört die bis dahin einwandfreie Steuerungseinheit; drei Tage Stillstand. Elfriede meldet den Fehler am selben Tag.
Posten: 1. 300 € für den Chip (Mangelschaden), 2. 6.000 € neue Steuerungseinheit (Mangelfolgeschaden), 3. 4.500 €
entgangener Gewinn (Betriebsausfall). Keine Frist gesetzt. Beide sind Kaufleute (§ 377 HGB).
Kern: § 437 Nr. 3 → § 280 Abs. 1 (Wortlautkarte) als Grundtatbestand im Fall; § 280 Abs. 3 und § 281 Abs. 1 Satz 1
(Wortlautkarten, Frist als letzte Chance); Kontrollfrage (Lehre/Klausurformel; BGH VII ZR 63/18 Rn. 17 ff., VIII ZR 169/12
Rn. 26 f.); Anwendung je Posten mit gleicher Tafel (Posten – Kontrollfrage – Anspruchsgrundlage): Chip → statt, Frist
fehlt; Steuerungseinheit → neben; Produktionsausfall → neben (BGH V ZR 93/08 Rn. 12, 14; BT-Drucks. 14/6040 S. 225),
Verzögerungsschaden §§ 280 Abs. 2, 286 ein Satz (Verweis 112); Lösung (Tabelle), Klausurtipp, Schema, Merksatz.
Belege: ../RECHTSSTAND.md. Figuren: Elfriede (hilde), Dietrich (christian); Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Elfriede": "hilde", "Dietrich": "christian"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Kauf ----------------------------------------------------------------------------------------------
    ("[fall]Elfriede führt eine Druckerei. [kauf]Bei Dietrich, der Steuerchips selbst herstellt, kauft sie für ihre "
     "Druckmaschine einen Chip zum Nachrüsten, für dreihundert Euro. [einbau]Ihr Techniker setzt ihn ein.", 0.3),
    # --- A2 Fall: der Schaden -------------------------------------------------------------------------------------------
    ("[heiss]Doch der Chip ist fehlerhaft. Er überhitzt [zerst]und zerstört die Steuerungseinheit der Maschine, die bis "
     "dahin einwandfrei lief. [still]Drei Tage steht die Maschine still, bis eine neue Steuerungseinheit eingebaut ist. "
     "[melden]Elfriede meldet den Fehler noch am selben Tag.", 0.3),
    ("[el1]Meine Maschine stand drei Tage still! Sie zahlen mir alles, und zwar sofort.", 0.3, "Elfriede"),
    ("[di1]Ich schicke Ihnen gern einen neuen Chip. Aber zahlen werde ich nichts.", 0.3, "Dietrich"),
    # --- A3 Fall: drei Posten, Frage ------------------------------------------------------------------------------------
    ("[pos]Elfriede verlangt drei Posten: [pa]Erstens dreihundert Euro für den Chip, [pb]zweitens sechstausend Euro für "
     "die neue Steuerungseinheit, [pc]drittens viertausendfünfhundert Euro Gewinn, der ihr durch den Stillstand entgangen "
     "ist. [frist0]Eine Frist hat sie nicht gesetzt. [frage]Welcher Posten läuft über welchen Anspruch, [frage2]und "
     "wofür braucht sie eine Frist?", 0.5),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 280 Abs. 1 (Wortlaut) ---------------------------------------------------------------------------------------
    ("[agl]Beim Kauf führt Paragraf vierhundertsiebenunddreißig Nummer drei ins allgemeine Schuldrecht. [w280]Paragraf "
     "zweihundertachtzig Absatz eins: Verletzt der Schuldner eine Pflicht aus dem Schuldverhältnis, so kann der Gläubiger "
     "Ersatz des hierdurch entstehenden Schadens verlangen. [w280b]Dies gilt nicht, wenn der Schuldner die "
     "Pflichtverletzung nicht zu vertreten hat. [g046]Das ganze System zeigt das Video zum Schadensersatz.", P),
    # --- D Grundtatbestand im Fall ---------------------------------------------------------------------------------------
    ("[gt1]Im Fall haben Elfriede und Dietrich einen Kaufvertrag, also ein Schuldverhältnis. [gt2]Ein Chip, der "
     "überhitzt, eignet sich nicht für die gewöhnliche Verwendung, er ist mangelhaft. [gt2b]Damit hat Dietrich seine "
     "Pflicht verletzt, eine mangelfreie Sache zu liefern. [gt3]Weil der Kauf für beide ein Handelsgeschäft ist, musste Elfriede "
     "den Mangel unverzüglich anzeigen, nach Paragraf dreihundertsiebenundsiebzig HGB. Das hat sie getan. [gt4]Das Vertretenmüssen "
     "wird vermutet. Dietrich kann sich nicht entlasten, der Fehler entstand durch Unsorgfalt in seiner eigenen Fertigung. [gt5]Ein bloßer "
     "Händler müsste sich das Verschulden des Herstellers dagegen nicht zurechnen lassen.", PS),
    # --- E § 280 Abs. 3, § 281 Abs. 1 Satz 1 (Wortlaut) ------------------------------------------------------------------
    ("[w3]Für Schadensersatz statt der Leistung verlangt Absatz drei zusätzliche Voraussetzungen, bei einem behebbaren "
     "Mangel aus Paragraf zweihunderteinundachtzig. [w281]Nach dessen Absatz eins Satz eins muss der Gläubiger dem Schuldner "
     "erfolglos eine angemessene Frist zur Leistung oder Nacherfüllung bestimmt haben. [sinn]Die Frist gibt dem Verkäufer "
     "eine letzte Chance, doch noch richtig zu erfüllen.", PS),
    # --- F Die Kontrollfrage ---------------------------------------------------------------------------------------------
    ("[kf]Aber welcher Weg passt zu welchem Schaden? [kf1]Die Lehre gibt eine Kontrollfrage: Würde eine ordnungsgemäße "
     "Nacherfüllung im letztmöglichen Zeitpunkt den Schaden noch beseitigen? [kf2]Wenn ja, geht es um Schadensersatz statt "
     "der Leistung, grundsätzlich nur nach Frist. [kf3]Wenn nein, geht es um Schadensersatz neben der Leistung, hier aus "
     "Paragraf zweihundertachtzig Absatz eins, ohne Frist. [kf4]Der Bundesgerichtshof fragt genauso, ob eine Nacherfüllung "
     "den Schaden beseitigen würde.", PS),
    # --- G Posten 1: der Chip --------------------------------------------------------------------------------------------
    ("[a1]Posten eins, der Chip. [a1k]Liefert Dietrich einen fehlerfreien Chip, ist dieser Schaden weg. [a1e]Also "
     "Schadensersatz statt der Leistung, nach Paragraf zweihundertachtzig Absatz eins und drei mit Paragraf "
     "zweihunderteinundachtzig. [a1f]Ohne Frist gibt es dafür kein Geld. [a1n]Elfriede muss zuerst Nacherfüllung "
     "verlangen und eine Frist setzen. [a1x]Ausnahmen stehen in Paragraf zweihunderteinundachtzig Absatz zwei und "
     "Paragraf vierhundertvierzig.", PS),
    # --- H Posten 2: die Steuerungseinheit -------------------------------------------------------------------------------
    ("[b1]Posten zwei, die Steuerungseinheit. [b1k]Ein neuer Chip repariert sie nicht, der Schaden bliebe. [b1e]Also "
     "Schadensersatz neben der Leistung, allein aus Paragraf zweihundertachtzig Absatz eins. [b1s]Elfriede bekommt die "
     "sechstausend Euro, ohne Frist.", PS),
    # --- I Posten 3: der Produktionsausfall ------------------------------------------------------------------------------
    ("[c1]Posten drei, der Produktionsausfall. [c1k]Die drei Tage Stillstand macht auch die beste Nacherfüllung nicht "
     "ungeschehen. [c1e]Also ebenfalls neben der Leistung. [c1b]So hat es der Bundesgerichtshof zweitausendneun "
     "entschieden: Den Nutzungsausfall wegen einer mangelhaften Sache kann der Käufer, der am Vertrag festhält, nach "
     "Paragraf zweihundertachtzig Absatz eins verlangen, ohne die Voraussetzungen des Verzugs. [c1g]Schon die "
     "Gesetzesbegründung nennt als Beispiel den Betriebsausfall bei einer mangelhaften Maschine. [c1s]Elfriede bekommt die "
     "viertausendfünfhundert Euro. [c1v]Anders der Schaden, der erst entsteht, weil der Verkäufer die Nacherfüllung "
     "verzögert: Dafür braucht es Verzug, nach Paragraf zweihundertachtzig Absatz zwei mit Paragraf "
     "zweihundertsechsundachtzig, dazu das Video zum Schuldnerverzug.", PS),
    # --- J Lösung (Tabelle) ----------------------------------------------------------------------------------------------
    ("[loes]Die Lösung: [l1]Für den Chip braucht Elfriede erst eine Frist. [l2]Die Steuerungseinheit [l3]und den "
     "Produktionsausfall bekommt sie sofort, [l4]zusammen zehntausendfünfhundert Euro.", PS),
    # --- K Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe Schadensposten für Schadensposten. [t1]Stelle bei jedem die Kontrollfrage, [t2]erst dann "
     "wählst du die Anspruchsgrundlage. [t3]Wirf nie alle Posten in einen Topf.", PS),
    # --- L Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für jeden Posten: [k1]Römisch eins: die Kontrollfrage, statt oder neben der Leistung. [k2]Römisch "
     "zwei: Schuldverhältnis und Pflichtverletzung. [k3]Römisch drei: nur statt der Leistung, die erfolglose Frist. "
     "[k4]Römisch vier: Vertretenmüssen, vermutet. [k5]Römisch fünf: der Schaden.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Was eine Nacherfüllung noch beseitigen könnte, gibt es nur statt der Leistung, [mk2]also grundsätzlich "
     "erst nach Frist. [mk3]Was trotz Nacherfüllung bleibt, gibt es neben der Leistung, [mk4]ohne Frist.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
