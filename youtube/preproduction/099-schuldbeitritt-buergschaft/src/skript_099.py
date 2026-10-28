"""Folge 099 · Schuldbeitritt, Schuldübernahme oder Bürgschaft? Die Abgrenzung (Fr · Klausurpraxis · Zivilrecht/
Schuldrecht AT, Format Abgrenzung). Fall nach dem Plan-Hook („Die Freundin ‚übernimmt‘ schriftlich die Autoschulden ihres
Partners“): Jochen finanziert ein gebrauchtes Auto mit einem Bankkredit über 18.000 €; das Auto gehört ihm, nur er fährt es.
Die Bank (Frau Zöllner) verlangt eine weitere Sicherheit, Jochen bleibt Kreditnehmer. Seine Freundin Katja (verdient gut,
braucht kein Auto) schreibt der Bank mit der Hand „Ich übernehme die Schulden von Jochen aus dem Autokredit über 18.000 Euro“
und unterschreibt. Ein Jahr später zahlt Jochen nicht mehr (12.000 € offen), die Bank verlangt Zahlung von Katja.
Abgrenzung durch Auslegung (§§ 133, 157; BGH III ZR 56/19 Rn. 19, 20): 1. befreiende Schuldübernahme §§ 414, 415, 417
(Wortlautkarte § 414; BGH VII ZR 13/11 Rn. 7), 2. Schuldbeitritt (§ 311 I, Gesamtschuld § 421, nicht akzessorisch,
grundsätzlich formfrei; BGH I ZR 168/14 Rn. 40, IX ZR 208/15 Rn. 7), 3. Bürgschaft (Wortlautkarte § 765 I; §§ 767, 768,
770, 771; Wortlautkarte § 766 S. 1, 2). Dreispalter progressiv, Abgrenzungskriterien, Subsumtion, Ergebnis Bürgschaft.
Klausurtipp (Lexi): Verbraucherdarlehensrecht beim Beitritt (BGH XI ZR 650/20 Rn. 11), Sittenwidrigkeit bei krasser
Überforderung Nahestehender (BGH XI ZR 82/11 Rn. 9). Klausurschema, Merksatz (Lexi).
Figuren: Jochen (christian), Katja (lucy), Frau Zöllner (hilde); Lexi/Erzählerin Carla. Belege: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Jochen": "christian", "Katja": "lucy", "Zöllner": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Autokredit --------------------------------------------------------------------------------------
    ("[fall]Jochen kauft sich für den Weg zur Arbeit ein gebrauchtes Auto. [kredit]Die Bank finanziert es mit einem Kredit "
     "über achtzehntausend Euro. [nur]Das Auto gehört Jochen, und nur er fährt es. [katja]Seine Freundin Katja verdient "
     "gut, braucht aber kein Auto. [bank]Frau Zöllner von der Bank sagt zu Jochen:", 0.3),
    # --- A2 Fall: die Bank will eine Sicherheit, Katja unterschreibt ----------------------------------------------------
    ("[zo1]Wir brauchen noch eine Sicherheit. Sie bleiben natürlich unser Kreditnehmer.", 0.25, "Zöllner"),
    ("[jo1]Katja, kannst du für mich einspringen?", 0.25, "Jochen"),
    ("[ka1]Klar, ich helfe dir.", 0.3, "Katja"),
    ("[zettel]Katja schreibt mit der Hand an die Bank: Ich übernehme die Schulden von Jochen aus dem Autokredit über "
     "achtzehntausend Euro. [unter]Sie unterschreibt, und die Bank nimmt die Erklärung an.", 0.3),
    # --- A3 Fall: Jochen zahlt nicht mehr, die Frage ----------------------------------------------------------------
    ("[spaet]Ein Jahr später zahlt Jochen die Raten nicht mehr. Zwölftausend Euro sind offen. [brief]Frau Zöllner wendet "
     "sich an Katja.", 0.25),
    ("[zo2]Sie haben die Schulden übernommen. Bitte zahlen Sie die zwölftausend Euro.", 0.25, "Zöllner"),
    ("[ka2]Ich wollte Jochen doch nur helfen, den Kredit zu bekommen!", 0.3, "Katja"),
    ("[frage]Was hat Katja da eigentlich unterschrieben? [frage2]Eine Schuldübernahme, einen Schuldbeitritt oder eine "
     "Bürgschaft?", 0.5),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.6),
    # --- C Auslegung ------------------------------------------------------------------------------------------------------
    ("[ausl]Entscheidend ist nicht allein das Wort übernehmen. [ausl2]Nach den Paragrafen hundertdreiunddreißig und "
     "hundertsiebenundfünfzig zählt der wirkliche Wille, [ausl3]so wie "
     "die Bank ihn verstehen durfte. [drei]Drei Rechtsinstitute kommen in Betracht.", PS),
    # --- D1 Schuldübernahme, §§ 414, 415, 417 (Wortlaut § 414) ---------------------------------------------------------
    ("[w414]Erstens: die befreiende Schuldübernahme. Paragraf vierhundertvierzehn: Eine Schuld kann von einem Dritten "
     "durch Vertrag mit dem Gläubiger in der Weise übernommen werden, dass der Dritte an die Stelle des bisherigen "
     "Schuldners tritt. [p415]Vereinbaren Schuldner und Übernehmer die Übernahme, hängt sie nach Paragraf "
     "vierhundertfünfzehn von der Genehmigung des Gläubigers ab. [frei]Folge: Der Altschuldner wird frei. [p417]Der "
     "Übernehmer kann nach Paragraf vierhundertsiebzehn die Einwendungen aus dem Verhältnis von Gläubiger und "
     "Altschuldner erheben.", P),
    ("[streng]Weil der Gläubiger dabei seinen Schuldner verliert, muss sein Wille, ihn zu entlassen, "
     "nach dem Bundesgerichtshof deutlich erkennbar sein.", PS),
    # --- D2 Schuldbeitritt ----------------------------------------------------------------------------------------------
    ("[beit]Zweitens: der Schuldbeitritt, auch kumulative Schuldübernahme. [beit2]Er ist nicht allgemein geregelt, aber "
     "nach Paragraf dreihundertelf Absatz eins als Vertrag möglich. [ges]Der Beitretende wird neben dem Altschuldner "
     "Gesamtschuldner nach Paragraf vierhunderteinundzwanzig. [nakz]Seine Schuld ist nicht "
     "akzessorisch, sie kann eigene Wege gehen. [formfr]Und der Beitritt ist grundsätzlich formfrei.", PS),
    # --- D3 Bürgschaft, § 765 Abs. 1 (Wortlaut), §§ 767, 768, 770, 771 ----------------------------------------------------
    ("[w765]Drittens: die Bürgschaft. Paragraf siebenhundertfünfundsechzig Absatz eins: Durch den Bürgschaftsvertrag "
     "verpflichtet sich der Bürge gegenüber dem Gläubiger eines Dritten, für die Erfüllung der Verbindlichkeit des "
     "Dritten einzustehen. [fremd]Wer bürgt, steht also für eine fremde Schuld ein. [akz]Seine Haftung ist akzessorisch: "
     "Nach Paragraf siebenhundertsiebenundsechzig ist der jeweilige Bestand der Hauptschuld maßgebend. [einr]Er kann "
     "die Einreden des Hauptschuldners erheben, Paragraf siebenhundertachtundsechzig, und nach Paragraf "
     "siebenhundertsiebzig die Zahlung verweigern, solange der Hauptschuldner anfechten oder der Gläubiger aufrechnen "
     "kann. [p771]Außerdem hat er grundsätzlich die Einrede der Vorausklage, Paragraf "
     "siebenhunderteinundsiebzig.", P),
    # --- D4 § 766 (Wortlaut) ------------------------------------------------------------------------------------------------
    ("[w766]Für die Bürgschaft gilt Paragraf "
     "siebenhundertsechsundsechzig: Zur Gültigkeit des Bürgschaftsvertrags ist schriftliche Erteilung der "
     "Bürgschaftserklärung erforderlich. [w766b]Die Erteilung der Bürgschaftserklärung in elektronischer Form ist "
     "ausgeschlossen.", PS),
    # --- E Abgrenzung (Dreispalter) ----------------------------------------------------------------------------------------
    ("[tab]Bei der Schuldübernahme wird der Altschuldner frei, bei Beitritt und Bürgschaft bleibt er "
     "verpflichtet. [t2]Der Beitretende schuldet selbst als Gesamtschuldner, wer bürgt, steht für eine fremde Schuld ein. "
     "[t3]Nur die Bürgschaft ist akzessorisch, [t4]und für sie schreibt das Gesetz eigens die Schriftform vor.", PS),
    ("[k1q]Abgrenzen musst du in zwei Schritten. Erstens: Soll der Altschuldner frei werden? Nur dann ist es "
     "eine Schuldübernahme. [k2q]Zweitens: Will der Dritte eine eigene Schuld begründen, ist es ein Beitritt. Will er nur "
     "für die fremde Schuld einstehen, eine Bürgschaft. [indiz]Ein wichtiges Indiz für den Beitritt ist nach dem "
     "Bundesgerichtshof ein eigenes wirtschaftliches oder rechtliches Interesse an der Tilgung der Schuld. "
     "[zweif]Bleiben Zweifel, nimmt die herrschende Meinung eine Bürgschaft an, damit die Schriftform nicht umgangen "
     "wird.", PS),
    # --- F Subsumtion -------------------------------------------------------------------------------------------------------
    ("[sub]Zurück zu Katja. [s1]Die Bank wollte Jochen nicht entlassen, er bleibt Kreditnehmer. Eine Schuldübernahme "
     "scheidet aus. [s2]Nur Jochen nutzt das Auto. Ein eigenes Interesse an dem Kredit hat Katja nicht, "
     "sie wollte Jochen nur helfen. [s3]Sie will also nur für eine fremde Schuld einstehen. Das ist eine Bürgschaft, trotz "
     "des Wortes übernehmen. [s4]Und die Form ist gewahrt: Katja hat schriftlich erklärt und eigenhändig unterschrieben.", PS),
    # --- G Ergebnis -----------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Katja haftet als Bürgin für die offenen zwölftausend Euro. [erg2]Ihre Haftung hängt an der "
     "Kreditschuld von Jochen. [erg3]Erhebt sie die Einrede der Vorausklage, muss die Bank aber grundsätzlich zuerst "
     "erfolglos versuchen, bei Jochen zu vollstrecken.", PS),
    # --- H Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bestimme zuerst durch Auslegung, was die Erklärung ist."
     " [tipp2]Tritt ein Verbraucher einem Kreditvertrag bei, wendet der Bundesgerichtshof die Regeln über "
     "Verbraucherdarlehen entsprechend an, etwa mit Widerrufsrecht. [tipp3]Und überfordert eine Bürgschaft einen dem "
     "Schuldner nahestehenden Menschen finanziell krass, vermutet die Rechtsprechung, dass sie nach Paragraf "
     "hundertachtunddreißig Absatz eins sittenwidrig ist.", PS),
    # --- I Klausurschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema für den Anspruch aus Bürgschaft: [k1]Römisch eins: Rechtsnatur der Erklärung durch "
     "Auslegung. [k1a]Altschuldner frei, [k1b]eigene Schuld oder fremde Schuld? [k2]Römisch "
     "zwei: wirksamer Bürgschaftsvertrag, [k2a]mit Einigung, Schriftform und ohne Sittenwidrigkeit. [k3]Römisch drei: "
     "Bestand der Hauptschuld. [k4]Römisch vier: Einreden des Bürgen. [k5]Römisch fünf: Ergebnis.", PS),
    # --- J Merksatz (Lexi) ----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wird der Altschuldner frei, ist es eine Schuldübernahme. [m2]Bleibt er verpflichtet, entscheidet der "
     "Wille: Eigene Schuld heißt Beitritt, Einstehen für fremde Schuld heißt Bürgschaft.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
