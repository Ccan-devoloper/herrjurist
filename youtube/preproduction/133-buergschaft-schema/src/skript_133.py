"""Folge 133 · Für Freunde bürgen? Bürgschaft Schema §§ 765 ff. BGB (Mo · Der Fall · Schema; Zivilrecht, weitere
Vertragstypen). Fall nach dem Plan-Hook („Du bürgst für den Kredit deiner Schwester – plötzlich zahlt sie nicht mehr“):
Hilke nimmt für eine neue Küche einen Bankkredit über 15.000 € auf (Zinsen 75 € im Monat). Herr Seibold von der Bank
verlangt eine Bürgschaft; Hilke bittet ihre Schwester Marlies (netto 3.400 € im Monat), die in der Bank eigenhändig eine
Urkunde unterschreibt: „Ich bürge selbstschuldnerisch für den Kredit von Hilke über 15.000 Euro.“ Zwei Jahre später zahlt
Hilke nicht mehr, die Bank kündigt, 9.000 € sind offen; die Bank verlangt sie von Marlies. Anspruchsschema der Bank gegen
die Bürgin aus § 765 I (Wortlautkarte): I. entstanden – 1. Bürgschaftsvertrag, Schriftform § 766 S. 1 (Wortlautkarte),
§ 126 I, Ausnahme § 350 HGB; 2. keine Sittenwidrigkeit § 138 I (BGH XI ZR 82/11 Rn. 9, im Fall verneint); 3. Hauptschuld,
§ 767 I 1; II. nicht erloschen; III. durchsetzbar – §§ 768, 770, Einrede der Vorausklage § 771 (Wortlautkarte),
ausgeschlossen nach § 773 I Nr. 1 (Wortlautkarte); Ergebnis; IV. Rückgriff: § 774 I 1 (Wortlautkarte; wie § 426 II),
Auftrag § 670 (BGH XI ZR 362/15 Rn. 20, 21). Klausurtipp (Lexi): selbstschuldnerisch ≠ Gesamtschuld (BGH IX ZR 36/22
Rn. 17). Klausurschema progressiv, Merksatz (Lexi).
Figuren: Marlies (sabrina), Hilke (laura_ruhig), Herr Seibold (william); Lexi/Erzählerin Carla. Belege: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter. Kein Genitiv der Namen.
„der Bürge“ im Fließtext vermieden („wer bürgt“), weil die Erkenner in Folge 099 „Bürger“ hörten."""

P, PS = 0.3, 0.5

STIMMEN = {"Marlies": "sabrina", "Hilke": "laura_ruhig", "Seibold": "william"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Kredit für die Küche ------------------------------------------------------------------------------
    ("[fall]Hilke will sich eine neue Küche kaufen. [kredit]Dafür braucht sie von der Bank einen Kredit über "
     "fünfzehntausend Euro, [zins]die Zinsen betragen fünfundsiebzig Euro im Monat. [bank]Herr Seibold von der Bank "
     "sagt:", 0.3),
    ("[se1]Den Kredit bekommen Sie, wenn jemand für Sie bürgt.", 0.3, "Seibold"),
    ("[frag]Hilke fragt ihre Schwester Marlies.", 0.25),
    ("[hi1]Marlies, bürgst du für mich?", 0.25, "Hilke"),
    ("[ma1]Klar, für dich mache ich das.", 0.3, "Marlies"),
    # --- A2 Fall: die Urkunde --------------------------------------------------------------------------------------------
    ("[netto]Marlies verdient netto dreitausendvierhundert Euro im Monat. [urk]In der Bank unterschreibt sie eigenhändig "
     "eine Urkunde: Ich bürge selbstschuldnerisch für den Kredit von Hilke über fünfzehntausend Euro. [an]Herr Seibold "
     "nimmt die Erklärung an.", 0.3),
    # --- A3 Fall: zwei Jahre später, die Frage --------------------------------------------------------------------------
    ("[spaet]Zwei Jahre später zahlt Hilke die Raten nicht mehr. [kuend]Die Bank kündigt den Kredit, neuntausend Euro "
     "sind offen. [brief]Herr Seibold wendet sich an Marlies.", 0.25),
    ("[se2]Bitte zahlen Sie die neuntausend Euro für Ihre Schwester.", 0.25, "Seibold"),
    ("[ma2]Dann holen Sie sich das Geld doch erst bei Hilke!", 0.3, "Marlies"),
    ("[frage]Muss Marlies zahlen? [frage2]Und bekommt sie ihr Geld danach von Hilke zurück?", 0.5),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.6),
    # --- C Anspruchsgrundlage § 765 Abs. 1 (Wortlaut) und Aufbau ------------------------------------------------------------
    ("[agl]Die Bank könnte gegen Marlies einen Anspruch aus Paragraf siebenhundertfünfundsechzig Absatz eins haben. "
     "[w765]Danach verpflichtet sich, wer bürgt, gegenüber dem Gläubiger eines Dritten, für dessen Verbindlichkeit "
     "einzustehen. [aufbau]Wir prüfen: Ist der Anspruch entstanden, ist er nicht erloschen, und ist er durchsetzbar?", PS),
    # --- D1 I. 1. Bürgschaftsvertrag und Schriftform (Wortlaut § 766 S. 1) ---------------------------------------------------
    ("[i1]Römisch eins: Ist der Anspruch entstanden? Eins: ein wirksamer Bürgschaftsvertrag. [einig]Marlies und die Bank "
     "haben sich geeinigt. [w766]Dazu Paragraf siebenhundertsechsundsechzig Satz eins: Zur Gültigkeit des "
     "Bürgschaftsvertrags ist schriftliche Erteilung der Bürgschaftserklärung erforderlich. [nur]Schriftlich sein muss "
     "also nur die Erklärung von Marlies, und nach Satz zwei nicht elektronisch. [eigen]Sie hat eigenhändig "
     "unterschrieben, Paragraf hundertsechsundzwanzig Absatz eins. Die Form ist gewahrt. [hgb]Nur wenn die Bürgschaft "
     "für einen Kaufmann ein Handelsgeschäft ist, entfällt die Form nach Paragraf dreihundertfünfzig HGB.", PS),
    # --- D2 I. 2. keine Sittenwidrigkeit (BGH XI ZR 82/11 Rn. 9) --------------------------------------------------------------
    ("[i2]Zwei: keine Sittenwidrigkeit nach Paragraf hundertachtunddreißig Absatz eins. [krass]Nach dem "
     "Bundesgerichtshof ist die bürgende Person grundsätzlich krass überfordert, wenn sie voraussichtlich nicht einmal "
     "die laufenden Zinsen aus dem pfändbaren Teil ihres Einkommens und Vermögens tragen kann. [verm]Steht sie dem "
     "Schuldner persönlich besonders nahe, wird dann widerleglich vermutet, dass sie aus emotionaler Verbundenheit "
     "gebürgt und die Bank das in sittlich anstößiger Weise ausgenutzt hat. [s138]Marlies verdient netto "
     "dreitausendvierhundert Euro, die Zinsen betragen fünfundsiebzig Euro im Monat. [s138b]Krass überfordert ist sie "
     "nicht, die Bürgschaft ist wirksam.", PS),
    # --- D3 I. 3. Hauptschuld, § 767 Abs. 1 S. 1 -------------------------------------------------------------------------
    ("[i3]Drei: Die Hauptschuld muss bestehen. [akz]Die Bürgschaft ist akzessorisch: Nach Paragraf "
     "siebenhundertsiebenundsechzig Absatz eins kommt es auf den jeweiligen Bestand der Hauptschuld an. [haupt]Hilke "
     "schuldet aus dem Darlehen nach Paragraf vierhundertachtundachtzig Absatz eins noch neuntausend Euro, fällig nach "
     "der Kündigung. Der Anspruch ist entstanden.", PS),
    # --- D4 II. nicht erloschen ---------------------------------------------------------------------------------------------
    ("[ii]Römisch zwei: Der Anspruch ist nicht erloschen. [erl]Niemand hat die neuntausend Euro gezahlt. Hätte Hilke "
     "gezahlt, wäre Marlies wegen der Akzessorietät frei geworden.", PS),
    # --- D5 III. durchsetzbar: §§ 768, 770, 771 (Wortlaut), 773 Abs. 1 Nr. 1 (Wortlaut) ---------------------------------------
    ("[iii]Römisch drei: Ist der Anspruch durchsetzbar? [p768]Nach Paragraf siebenhundertachtundsechzig kann Marlies die "
     "Einreden der Hauptschuldnerin erheben, etwa die Verjährung. [p770]Nach Paragraf siebenhundertsiebzig darf sie die "
     "Zahlung verweigern, solange Hilke anfechten oder die Bank aufrechnen kann. [keine]Dafür gibt es hier keine "
     "Anhaltspunkte.", P),
    ("[w771]Bleibt die Einrede der Vorausklage nach Paragraf siebenhunderteinundsiebzig: Wer bürgt, darf die Zahlung "
     "verweigern, solange die Bank nicht erfolglos versucht hat, gegen die Schuldnerin zu vollstrecken. [w773]Ausgeschlossen ist sie "
     "nach Paragraf siebenhundertdreiundsiebzig Absatz eins Nummer eins aber bei einem Verzicht, insbesondere, wenn man "
     "sich als Selbstschuldner verbürgt hat. [s773]Genau das hat Marlies unterschrieben. Die Bank muss nicht erst bei "
     "Hilke vollstrecken.", PS),
    # --- E Ergebnis ----------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Marlies muss der Bank die neuntausend Euro zahlen.", PS),
    # --- F IV. Rückgriff: § 774 Abs. 1 S. 1 (Wortlaut), § 670 (BGH XI ZR 362/15 Rn. 20, 21) -----------------------------------
    ("[iv]Römisch vier: der Rückgriff. [w774]Zahlt Marlies, geht nach Paragraf siebenhundertvierundsiebzig Absatz eins "
     "Satz eins die Forderung der Bank gegen Hilke auf sie über. [legal]Das ist ein gesetzlicher Forderungsübergang, "
     "wie beim Gesamtschuldnerausgleich nach Paragraf vierhundertsechsundzwanzig Absatz zwei. [p670]Außerdem hat Hilke "
     "sie gebeten, für sie zu bürgen. Das ist ein Auftrag, und daraus kann Marlies nach Paragraf sechshundertsiebzig Ersatz "
     "verlangen. [wahl]Beide Wege erkennt der Bundesgerichtshof an, das Geld bekommt sie aber nur einmal. [risiko]Ob "
     "Hilke zahlen kann, ist allerdings das Risiko von Marlies: Wer bürgt, trägt das Insolvenzrisiko der Schuldnerin.", PS),
    # --- G Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Selbstschuldnerisch heißt nur, dass die Einrede der Vorausklage fehlt. [tipp2]Wer so bürgt, "
     "wird nach dem Bundesgerichtshof trotzdem nicht Gesamtschuldner neben der Schuldnerin. [tipp3]Prüfe also auch "
     "hier die Hauptschuld und die Einreden nach Paragraf siebenhundertachtundsechzig. [tipp4]Und beim Rückgriff nennst "
     "du beide Wege: Paragraf siebenhundertvierundsiebzig und den Auftrag.", PS),
    # --- H Klausurschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema für den Anspruch aus Bürgschaft: [k1]Römisch eins: Anspruch entstanden, [k1a]mit "
     "wirksamem Bürgschaftsvertrag und Schriftform, [k1b]ohne Sittenwidrigkeit [k1c]und mit bestehender Hauptschuld. "
     "[k2]Römisch zwei: nicht erloschen. [k3]Römisch drei: durchsetzbar, [k3a]also keine Einreden nach den Paragrafen "
     "siebenhundertachtundsechzig, siebenhundertsiebzig und siebenhunderteinundsiebzig, [k3b]mit dem Ausschluss nach "
     "Paragraf siebenhundertdreiundsiebzig. [k4]Römisch vier: Rückgriff "
     "nach der Zahlung.", PS),
    # --- I Merksatz (Lexi) --------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer bürgt, steht für eine fremde Schuld ein, [m2]schriftlich und akzessorisch. [m3]Wer "
     "selbstschuldnerisch bürgt, kann die Bank nicht erst zur Schuldnerin schicken. [m4]Nach der Zahlung holt man sich "
     "das Geld über Paragraf siebenhundertvierundsiebzig zurück, wenn die Schuldnerin zahlen kann.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
