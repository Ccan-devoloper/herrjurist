"""Folge 107 · Computerbetrug § 263a: Fremde Karte am Geldautomaten (Mi · Examenswissen · StGB BT, Format Schema).
Beispielfall nach dem Plan-Hook („Ein Mann nimmt heimlich die Bankkarte seines Mitbewohners, dessen PIN er kennt, und hebt
am Automaten 500 Euro ab“): Heiko kennt die Geheimzahl seiner Mitbewohnerin Meike (beim gemeinsamen Einkaufen gesehen),
nimmt heimlich ihre Bankkarte aus der Geldbörse im Flur, hebt am Geldautomaten an der Ecke 500 € ab und legt die Karte
danach unbemerkt zurück; Rückgabewille von Anfang an.
Prüfung: A. § 263a I (Wortlautkarte; Struktur wie Betrug, BGH 3 StR 80/13 Rn. 8) → 1. Tathandlung: unbefugte Verwendung von
Daten, drei Auslegungen (BGH 2 StR 16/15 Rn. 10), betrugsspezifisch (2 StR 260/01 = BGHSt 47, 160, Rn. 10), Probe mit dem
gedachten Bankangestellten (2 StR 16/15 Rn. 11; 5 StR 362/25 Rn. 10) → 2. Beeinflussung (BGHSt 38, 120 = 2 StR 376/91,
HRRS-Rn. 5; 3 StR 80/13 Rn. 8) → 3. Schaden jedenfalls bei der Bank (2 StR 69/07 Rn. 23; § 675u BGB) → subjektiv → Ergebnis;
B. § 242 am Geld: fremd (3 StR 333/18 Rn. 8), aber keine Wegnahme (BGHSt 38, 120, HRRS-Rn. 11–18; 3 StR 333/18 Rn. 16);
C. § 242 an der Karte: keine Zueignungsabsicht (4 StR 308/25 Rn. 6; 1 StR 512/00 Rn. 5); D. § 246 subsidiär (3 StR 63/21
Rn. 33). Klausurtipp: berechtigter Karteninhaber (2 StR 260/01 Rn. 9 f.), § 266b nur im Drei-Partner-System (Rn. 17).
Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Heiko, Meike. Nie im Genitiv mit -s.
„Geheimzahl“ statt „PIN“ im Sprechtext (keine Buchstabierung). „Wegnahme“ spricht synth_el als „Weck-nahme“ (AUSSPRACHE),
Anker deshalb beim("…", "Weck").
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.6

# Stimmenpool dieser Folge: william, sabrina, marc, laura_ruhig. Eine Männer- und eine Frauenstimme genügen.
STIMMEN = {"Heiko": "marc", "Meike": "sabrina"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Karte im Flur, der Geldautomat, die Abbuchung ------------------------------------------------------
    ("[fall]Freitagabend in einer Wohngemeinschaft. [heiko]Heiko kennt die Geheimzahl seiner Mitbewohnerin Meike, er hat "
     "sie beim Einkaufen gesehen. [dusche]Meike steht unter der Dusche, ihre Geldbörse liegt im Flur. "
     "[nimmt]Heiko nimmt heimlich ihre Bankkarte heraus.", 0.3),
    ("[h1]Die Karte lege ich gleich wieder zurück.", 0.4, "Heiko"),
    ("[automat]Am Geldautomaten an der Ecke steckt er die Karte ein, [pin]tippt die Geheimzahl [betrag]und wählt "
     "fünfhundert Euro. [geld]Der Automat zahlt aus. [zurueck]Zu Hause legt Heiko die Karte unbemerkt "
     "zurück. [morgen]Am nächsten Morgen sieht Meike auf ihrem Handy die Kontoumsätze.", 0.3),
    ("[m1]Fünfhundert Euro abgehoben? Das war ich nicht!", 0.4, "Meike"),
    ("[frage]Hat sich Heiko strafbar gemacht? [frage2]Wir prüfen den Computerbetrug, dann den Diebstahl "
     "am Geld und an der Karte.", 0.6),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 263a Abs. 1 und Struktur -----------------------------------------------------------------------------
    ("[p263a]Paragraf zweihundertdreiundsechzig a, Absatz eins. [w263a]Bestraft wird, wer in Bereicherungsabsicht fremdes Vermögen beschädigt, indem er das "
     "Ergebnis eines Datenverarbeitungsvorgangs beeinflusst, zum Beispiel durch unbefugte Verwendung von Daten. [nach]Die Norm ist dem "
     "Betrug nachgebildet: [ersetzt]An die Stelle der Täuschung tritt die Tathandlung, an die Stelle von Irrtum und "
     "Verfügung die Beeinflussung eines Datenverarbeitungsvorgangs.", PS),
    # --- D 1. Tathandlung: Variante drei -----------------------------------------------------------------------------------
    ("[t1]Erstes Merkmal: die Tathandlung. [var]Von den vier Varianten kommt hier die dritte in Betracht: "
     "[var3]die unbefugte Verwendung von Daten. [echt]Karte und Geheimzahl sind echt, Heiko verwendet also richtige Daten. "
     "[frageu]Entscheidend ist, ob das unbefugt geschieht.", P),
    # --- E Drei Auslegungen von „unbefugt“ ------------------------------------------------------------------------------------
    ("[ausl]Was unbefugt heißt, ist umstritten. [subj]Nach der subjektiven Auslegung ist jede Verwendung "
     "gegen den Willen des Berechtigten unbefugt. Das wäre hier der Fall. [comp]Nach der computerspezifischen Auslegung "
     "kommt es darauf an, ob der Automat fehlerhaft beeinflusst wird. Hier arbeitet er aber "
     "fehlerfrei. [betr]Die Rechtsprechung und die herrschende Meinung legen betrugsspezifisch aus: Unbefugt ist "
     "nur eine Verwendung, die gegenüber einem Menschen eine Täuschung wäre. [arg]Denn die Norm soll nur die Lücke "
     "schließen, die der Betrug beim Computer lässt.", PS),
    # --- F Probe: der gedachte Bankangestellte -------------------------------------------------------------------------------
    ("[probe]Also die Probe: [angest]Man denkt sich statt des Automaten einen Bankangestellten, der dasselbe prüft "
     "wie der Automat. [erkl]Wer ihm Karte und Geheimzahl vorlegt, erklärt schlüssig, zur Verwendung "
     "der Karte berechtigt zu sein. [nicht]Heiko ist das nicht, er hat die Karte heimlich genommen. Der gedachte "
     "Angestellte würde getäuscht. [unbefok]Heiko verwendet die Daten also unbefugt.", PS),
    # --- G 2. Beeinflussung des Ergebnisses eines Datenverarbeitungsvorgangs ------------------------------------------------
    ("[dv]Zweites Merkmal: die Beeinflussung des Ergebnisses eines Datenverarbeitungsvorgangs. [dv2]Der Automat prüft "
     "Karte und Geheimzahl und gibt das Geld frei. [dv3]Beeinflussen heißt auch, einen solchen Vorgang in Gang zu setzen. "
     "[dv4]Das Ergebnis mindert das Vermögen unmittelbar, ohne weitere menschliche Entscheidung.", P),
    # --- H 3. Vermögensschaden ------------------------------------------------------------------------------------------------
    ("[schad]Drittes Merkmal: der Vermögensschaden. [bank]Die fünfhundert Euro kommen aus dem Vermögen der Bank. "
     "[erstatt]Für die nicht autorisierte Abhebung hat sie gegen Meike keinen Anspruch auf Erstattung ihrer "
     "Aufwendungen und muss das Konto wieder ausgleichen. [jedenf]Geschädigt ist also jedenfalls die Bank.", PS),
    # --- I Subjektiver Tatbestand, Ergebnis zu § 263a ------------------------------------------------------------------------
    ("[vors]Heiko handelt vorsätzlich: [vors2]Er weiß, dass er die Karte nicht benutzen darf, und will das Geld. [abs]Er "
     "handelt auch in der Absicht rechtswidriger Bereicherung, [abs2]denn auf die fünfhundert Euro hat er keinen Anspruch. "
     "[rws]Rechtswidrigkeit und Schuld liegen vor. [erg1]Heiko hat sich wegen Computerbetrugs strafbar gemacht.", PS),
    # --- J § 242 am Geld ------------------------------------------------------------------------------------------------------
    ("[geld242]Und das Geld: Hat Heiko es gestohlen? [w242]Paragraf zweihundertzweiundvierzig verlangt, dass der Täter eine fremde bewegliche "
     "Sache wegnimmt. "
     "[fremd]Fremd sind die Scheine: Nach dem Bundesgerichtshof übereignet die Bank das Geld nur dem Berechtigten, nicht "
     "einem unbefugten Abheber. [wegn]Es fehlt aber an der Wegnahme, also am Bruch fremden Gewahrsams. [gew]Die Bank "
     "überträgt den Gewahrsam an jeden, der den Automaten ordnungsgemäß mit Karte und Geheimzahl bedient. Ob er berechtigt "
     "ist, spielt dafür keine Rolle. [gew2]Das hat Heiko getan: Das Geld wird ihm übergeben, nicht "
     "weggenommen.", P),
    ("[streit]Früher nahmen manche Gerichte und Autoren hier trotzdem Diebstahl an. "
     "[streit2]Der Bundesgerichtshof lehnt das ab: Der Gesetzgeber wollte diesen Kartenmissbrauch gerade mit Paragraf "
     "zweihundertdreiundsechzig a erfassen. [kein242]Ein Diebstahl am Geld scheidet aus.", PS),
    # --- K § 242 an der Karte -------------------------------------------------------------------------------------------------
    ("[karte]Bleibt die Karte. [karte2]Sie ist fremd, und Heiko hat sie "
     "Meike weggenommen. [zueig]Fraglich ist die Zueignungsabsicht. [zdef]Der Täter muss die Sache "
     "ihrer Substanz oder ihrem Sachwert nach seinem Vermögen einverleiben wollen. [subst]Die Substanz will Heiko nicht: "
     "Er will die Karte von Anfang an unverändert zurücklegen. Das ist bloße Gebrauchsanmaßung. [sachw]Und einen Sachwert "
     "entzieht er ihr nicht: Die Karte verkörpert das Geld auf dem Konto nicht selbst, anders als etwa ein Sparbuch. "
     "[kein242k]Die Zueignungsabsicht fehlt, also auch hier kein Diebstahl.", PS),
    # --- L Ergebnis, Konkurrenzen -----------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Heiko ist strafbar wegen Computerbetrugs nach Paragraf zweihundertdreiundsechzig a. "
     "[konk]Eine Unterschlagung am Geld tritt dahinter zurück.", PS),
    # --- M Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Frag zuerst, wer die Karte benutzt. [tipp2]Überzieht der berechtigte Karteninhaber am Automaten "
     "sein Konto, ist das kein Computerbetrug. Er handelt nicht unbefugt, denn der Automat prüft nur den "
     "Verfügungsrahmen, nicht die Zahlungsfähigkeit. [tipp3]Für ihn kommt allenfalls Paragraf zweihundertsechsundsechzig b "
     "in Betracht, und nur im Drei-Partner-System.", PS),
    # --- N Prüfschema -----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [s1]A: Computerbetrug, Paragraf zweihundertdreiundsechzig a. [s1a]Römisch eins: Tatbestand. "
     "Objektiv: erstens unbefugte Verwendung von Daten, [s1b]zweitens Beeinflussung des "
     "Ergebnisses eines Datenverarbeitungsvorgangs, [s1c]drittens Vermögensschaden. [s1d]Subjektiv: Vorsatz [s1e]und "
     "Absicht rechtswidriger Bereicherung. [s1f]Römisch zwei und drei: Rechtswidrigkeit und Schuld. [s2]B: Diebstahl am "
     "Geld, ohne Wegnahme. [s3]C: Diebstahl an der Karte, ohne Zueignungsabsicht. [s4]D: Konkurrenzen.", PS),
    # --- O Merksatz (Lexi) ------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer eine heimlich genommene Karte mit Geheimzahl am Automaten einsetzt, begeht Computerbetrug, weil "
     "das gegenüber einem Menschen eine Täuschung wäre. [mk2]Das Geld stiehlt er nicht, denn der Automat übergibt es. "
     "[mk3]Und wer die Karte von vornherein zurücklegen will, stiehlt auch sie nicht.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
