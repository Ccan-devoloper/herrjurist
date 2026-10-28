"""Folge 277 · § 34 BauGB: Wann fügt sich ein Neubau ein? Innenbereich erklärt (Mo · Der Fall · Baurecht · Schema).
Übungsfall nach dem Plan-Hook („In einer Straße mit Einfamilienhäusern will ein Investor einen sechsstöckigen Wohnblock
bauen“): Eine Straße am Stadtrand ohne Bebauungsplan, nur Einfamilienhäuser mit ein oder zwei Geschossen in offener Bauweise
mit Gärten. Herr Kronberg (Investor) kauft ein Grundstück, will das alte Haus abreißen und einen Wohnblock mit sechs
Geschossen und 24 Wohnungen errichten; Frau Morgenstern wohnt nebenan. Erschließung gesichert; Block hält Grenzabstände und
die Bautiefe der Nachbarhäuser ein. Der Gemeinderat verweigert nach zwei Monaten die Zustimmung nach § 34 Abs. 3b,
§ 36a BauGB (sechs Geschosse passen nicht zu seinen Vorstellungen für die Straße).
Aufbau (Plan): 1. Anwendbarkeit (§ 30 Abs. 1, Abgrenzung § 35; Ortsteil/Bebauungszusammenhang, BVerwG 4 C 5.14 Rn. 11)
→ 2. Einfügen: § 34 Abs. 1 (Wortlautkarte), nähere Umgebung und Rahmen (BVerwG 4 C 7.15 Rn. 9, 10, 17 mit BVerwGE 55,
369), Art über § 34 Abs. 2 (Wortlautkarte) i. V. m. § 3 BauNVO, Maß: Rahmenüberschreitung und bodenrechtliche Spannungen
(4 C 7.15 Rn. 17, Leitsatz 2), Bauweise/Grundstücksfläche, Erschließung → 3. Rücksichtnahme (ein Satz, Verweis Folge 274)
→ 4. § 34 Abs. 3b BauGB (Wortlautkarte; G v. 27.10.2025, BGBl. 2025 I Nr. 257, in Kraft 30.10.2025, unbefristet; § 36a)
→ Ergebnis → Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Darstellung: Investor nicht als Bösewicht (will Wohnungen schaffen), Anwohnerin sachlich.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Koordinatorliste, namen_reserviert.txt, Volltextsuche 08.10.2026):
Kronberg, Morgenstern (nie im Genitiv mit -s). Stimmen aus dem Pool (william, sabrina, marc, laura_ruhig): Herr Kronberg
marc (Mann, mittel), Frau Morgenstern sabrina (Frau, mittel); laura_ruhig und william nicht verwendet (Vorfolge 274).
Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gesetzesnamen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Kronberg": "marc", "Morgenstern": "sabrina"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Einfamilienhausstraße, der Wohnblock ------------------------------------------------------------------
    ("[fall]In einer ruhigen Straße am Stadtrand stehen Einfamilienhäuser mit Gärten, ein oder zwei Geschosse hoch. "
     "[ohnebp]Einen Bebauungsplan gibt es hier nicht. [kauf]Herr Kronberg hat eines der Grundstücke gekauft. Das alte Haus "
     "darauf will er abreißen. [block]An seiner Stelle soll ein Wohnblock mit sechs Geschossen und vierundzwanzig "
     "Wohnungen entstehen.", P),
    ("[kr1]Die Stadt braucht Wohnungen. Hier können vierundzwanzig Familien ein Zuhause finden.", P, "Kronberg"),
    ("[nebenan]Frau Morgenstern wohnt nebenan.", P),
    ("[mo1]Gegen neue Nachbarn habe ich nichts. Aber sechs Stockwerke direkt neben unseren Gärten? Passt das in diese "
     "Straße?", P, "Morgenstern"),
    ("[antrag]Herr Kronberg beantragt die Baugenehmigung. [frage]Fügt sich der Wohnblock in die Straße ein? [frage2]Und "
     "wenn nicht: Kann die Gemeinde trotzdem den Weg frei machen?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Anwendbarkeit: kein qualifizierter Plan, Innen- oder Außenbereich ----------------------------------------------
    ("[anw]Erstens: Welche Vorschrift gilt? [b30]Gibt es einen qualifizierten Bebauungsplan, richtet sich die Zulässigkeit "
     "nach Paragraf dreißig. Hier fehlt er. [abgr]Also kommt es darauf an: Innenbereich nach Paragraf vierunddreißig oder "
     "Außenbereich nach Paragraf fünfunddreißig? [ortst]Ein Ortsteil ist ein Bebauungskomplex, der nach der Zahl der Bauten "
     "ein gewisses Gewicht hat und Ausdruck einer organischen Siedlungsstruktur ist. [zus]Im Zusammenhang bebaut ist er, "
     "soweit die aufeinanderfolgende Bebauung trotz Baulücken den Eindruck der Geschlossenheit und Zusammengehörigkeit "
     "vermittelt. [strasse]Die Straße erfüllt beides, und das Grundstück liegt mittendrin. "
     "Paragraf vierunddreißig ist anwendbar.", PS),
    # --- D 2. Einfügen: § 34 Abs. 1 (Wortlautkarte), nähere Umgebung, Rahmen -------------------------------------------------
    ("[p34]Zweitens, das Einfügen. [w34]Paragraf vierunddreißig Absatz eins: Ein Vorhaben ist zulässig, wenn es sich nach "
     "Art und Maß der baulichen Nutzung, der Bauweise und der Grundstücksfläche, die überbaut werden soll, in die Eigenart "
     "der näheren Umgebung einfügt [w34b]und die Erschließung gesichert ist.", P),
    ("[naeh]Die nähere Umgebung reicht so weit, wie sich das Vorhaben auswirken kann und wie die Umgebung das Grundstück "
     "prägt. [gesond]Für jedes Merkmal wird sie gesondert bestimmt. [rahmen]Was dort tatsächlich steht, bildet den Rahmen. "
     "[inn]Wer sich in diesem Rahmen hält, fügt sich in der Regel ein.", PS),
    # --- E Art: § 34 Abs. 2 (Wortlautkarte), faktisches reines Wohngebiet ---------------------------------------------------
    ("[p2]Für die Art der Nutzung gilt Absatz zwei. [w2]Entspricht die Eigenart der näheren Umgebung einem Baugebiet der "
     "Baunutzungsverordnung, kommt es für die Art allein darauf an, ob das Vorhaben dort allgemein zulässig wäre. "
     "[fakt]Die Straße entspricht einem reinen Wohngebiet. [wohn]Dort sind Wohngebäude allgemein zulässig. Seiner Art nach "
     "fügt sich der Block also ein. [v200]Mehr dazu im Video zu den Baugebieten.", PS),
    # --- F Maß: Rahmenüberschreitung, bodenrechtliche Spannungen ------------------------------------------------------------
    ("[mass]Anders beim Maß. [mfak]Hier zählt, was man von außen sieht: Grundfläche, Geschosszahl und Höhe, in einer "
     "Gesamtbetrachtung. [ref]In der Straße hat kein Haus mehr als zwei Geschosse. Ein Vorbild für sechs gibt es nicht. "
     "[ueber]Der Block sprengt den Rahmen. [ausn]Ausnahmsweise fügt sich auch so ein Vorhaben ein, wenn es weder selbst noch "
     "durch seine Vorbildwirkung bodenrechtlich beachtliche Spannungen begründet. [spann]Hier könnten sich die Nachbarn auf "
     "den Block berufen und ebenfalls hoch bauen. Die Straße bekäme ein neues Gesicht. "
     "[neinm]Nach dem Maß fügt sich der Block nicht ein.", P),
    ("[bauw]Bauweise und Grundstücksfläche sind dagegen kein Problem: Der Block hält Abstand zu den Grenzen und bleibt in "
     "der Bautiefe der Nachbarhäuser. [ersch]Und die Erschließung über die Straße ist gesichert.", PS),
    # --- G 3. Rücksichtnahme ------------------------------------------------------------------------------------------------
    ("[rueck]Drittens, die Rücksichtnahme. Sie ist Teil des Einfügens: Auch ein Vorhaben im Rahmen fügt sich nicht ein, "
     "wenn es die gebotene Rücksicht auf die Nachbarn fehlen lässt. [v274]Wie Nachbarn ihre Rechte durchsetzen, zeigt unser Video "
     "zum Gebietserhaltungsanspruch.", PS),
    # --- H 4. § 34 Abs. 3b BauGB (Wortlautkarte), § 36a ---------------------------------------------------------------------
    ("[p3b]Viertens: Seit dem dreißigsten Oktober zweitausendfünfundzwanzig gibt es Absatz drei b. [w3b]Mit Zustimmung der "
     "Gemeinde kann im Einzelfall oder in mehreren vergleichbaren Fällen vom Erfordernis des Einfügens abgewichen werden, "
     "wenn das Vorhaben der Errichtung eines Wohngebäudes dient [w3bb]und auch unter Würdigung nachbarlicher Interessen mit "
     "den öffentlichen Belangen vereinbar ist. [begr]Nach der Gesetzesbegründung muss sich dann etwa das Maß nicht mehr "
     "einfügen. [befr]Anders als die Sonderregel in Paragraf zweihundertsechsundvierzig e ist "
     "Absatz drei b nicht befristet.", P),
    ("[zust]Die Zustimmung regelt Paragraf sechsunddreißig a. Die Gemeinde erteilt sie, wenn das Vorhaben zu ihren "
     "Vorstellungen von der städtebaulichen Entwicklung passt. [drei]Schweigt sie drei Monate, gilt die Zustimmung als "
     "erteilt. [rat]Hier lehnt der Gemeinderat nach zwei Monaten ab: Sechs Geschosse passen nicht zu seinen Vorstellungen "
     "für die Straße.", PS),
    # --- I Ergebnis ---------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Der Wohnblock fügt sich nach dem Maß nicht ein, und ohne Zustimmung der Gemeinde gibt es keine "
     "Abweichung. [erg2]Die Baugenehmigung ist abzulehnen.", P),
    ("[kr2]Dann plane ich neu, mit zwei Geschossen wie die Nachbarhäuser.", P, "Kronberg"),
    ("[mo2]Damit kann ich gut leben.", PS, "Morgenstern"),
    # --- J Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne die Maßstäbe sauber. [k1]Die Art prüfst du im faktischen Baugebiet nach Absatz zwei, "
     "[k2]Maß, Bauweise und Grundstücksfläche immer nach Absatz eins. [k3]Sprengt ein "
     "Vorhaben den Rahmen, prüfe die bodenrechtlichen Spannungen, vor allem die Vorbildwirkung. [k4]Und Absatz drei b "
     "kommt erst, wenn das Einfügen scheitert. Auf die Zustimmung der Gemeinde gibt es grundsätzlich keinen Anspruch.", PS),
    # --- K Schema -----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema zum Innenbereich. [s1]Eins, die Anwendbarkeit: kein qualifizierter Bebauungsplan, "
     "im Zusammenhang bebauter Ortsteil. [s2]Zwei, das Einfügen in die nähere Umgebung. [s2a]Die Art, im faktischen Baugebiet "
     "nach Absatz zwei. [s2b]Maß, Bauweise und Grundstücksfläche: im Rahmen oder ohne bodenrechtliche Spannungen. "
     "[s2c]Dazu die Rücksichtnahme. [s3]Drei, die gesicherte Erschließung. [s4]Vier, notfalls die Abweichung nach Absatz "
     "drei b mit Zustimmung der Gemeinde. [s5]Fünf, das Ergebnis.", PS),
    # --- L Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Im Innenbereich ersetzt die vorhandene Bebauung den Bebauungsplan. [m2]Wer ihren Rahmen sprengt, "
     "fügt sich nur ein, wenn keine bodenrechtlichen Spannungen entstehen. [m3]Für Wohngebäude öffnet Absatz drei b einen "
     "zweiten Weg, aber nur mit Zustimmung der Gemeinde.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
