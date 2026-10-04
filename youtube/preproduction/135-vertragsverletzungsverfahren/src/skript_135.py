"""Folge 135 · Vertragsverletzungsverfahren (Art. 258 AEUV): Das Prüfungsschema (Fr · Klausurpraxis · Schema;
Öffentliches Recht/Europarecht). Fall: der echte Nitrat-Fall, EuGH, Urt. v. 21.6.2018 – C-543/16 (Kommission/Deutschland),
nur so weit, wie im Volltext belegt (Rn. 1, 20–25, 30, 33–36, 49, 52 f., 59–61, 62–70, 113 f., 132–136, Tenor);
Nachgang nur laut Pressemitteilung der Kommission INF/19/4251 (Aufforderungsschreiben nach Art. 260 AEUV, Juli 2019).
Keine Landwirte als Figuren, Feld und Grundwasser als neutrale Icons. Klausurfrage: Hat die Klage der Kommission Erfolg?
Rahmen: zwei Jurastudierende in der Lerngruppe (fiktiv): Antonia (julia) und Konstantin (niklas).
Schema: A. Zulässigkeit – 1. Zuständigkeit (Art. 256 Abs. 1 AEUV), 2. Parteifähigkeit (Art. 258, Art. 259 ein Satz),
3. Vorverfahren (Wortlautkarte Art. 258; Deckungsgleichheit C-152/98 Rn. 23; maßgeblicher Zeitpunkt C-543/16 Rn. 70,
C-152/98 Rn. 21), 4. Klageart/Rechtsschutzbedürfnis (C-431/92 Rn. 19–21); B. Begründetheit – Verstoß, Zurechnung
(C-416/17 Rn. 106 f.; Länder: C-543/16 Rn. 132–136), innerstaatliche Gründe unbeachtlich (C-543/16 Rn. 113 f.);
C. Urteil – Feststellung, Art. 260 Abs. 1; Wortlautkarte Art. 260 Abs. 2 (auszugsweise); Art. 260 Abs. 3 ein Satz.
Verweis auf die Voraussetzungsfolge 131 (Klagearten) in zwei Sätzen. Belege: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen, Daten und Artikel im Sprechtext als Wörter. Kein Genitiv der Namen.
Abkürzungen (EU, EuGH) im Sprechtext ausgeschrieben."""

P, PS = 0.3, 0.5

STIMMEN = {"Antonia": "julia", "Konstantin": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Nitrat im Grundwasser ---------------------------------------------------------------------------------
    ("[fall]Nitrat im Grundwasser. [mess]An rund der Hälfte der Messstellen im deutschen Belastungsmessnetz lag der Wert "
     "bei fünfzig Milligramm pro Liter oder darüber. [richt]Die Nitratrichtlinie verlangt Aktionsprogramme mit Regeln "
     "zum Düngen. [zusatz]Reichen sie nicht, muss der Staat nachschärfen.", P),
    # --- A2 Der Weg nach Luxemburg --------------------------------------------------------------------------------------
    ("[bericht]Zweitausendzwölf schickt Deutschland seinen Nitratbericht nach Brüssel. [besser]Die Kommission liest "
     "daraus: Die Wasserqualität hat sich nicht verbessert. [mahn]Im Oktober zweitausenddreizehn folgt ein Mahnschreiben, "
     "[stell]im Juli zweitausendvierzehn die begründete Stellungnahme mit zwei Monaten Frist. [dueng]Deutschland kündigt "
     "eine neue Düngeverordnung an, doch bei Fristablauf gilt sie nicht. [klage]Im Oktober zweitausendsechzehn klagt die "
     "Kommission vor dem Gerichtshof.", P),
    # --- A3 Lerngruppe ------------------------------------------------------------------------------------------------
    ("[lern]Antonia und Konstantin nehmen den Fall als Klausur.", P),
    ("[an1]Hat die Klage der Kommission Erfolg?", P, "Antonia"),
    ("[ko1]Aber zweitausendsiebzehn kam doch eine neue Düngeverordnung!", 0.6, "Konstantin"),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Verweis und Wortlaut Art. 258 ------------------------------------------------------------------------------
    ("[verw]Die Verfahren vor dem Gerichtshof im Überblick findest du im Video zu den Klagearten. [heute]Hier geht es um "
     "das Prüfungsschema der Vertragsverletzungsklage, aufgebaut in Zulässigkeit, Begründetheit und Urteil.", PS),
    ("[wl258]Artikel zweihundertachtundfünfzig: Meint die Kommission, ein Mitgliedstaat habe gegen die Verträge "
     "verstoßen, gibt sie ihm Gelegenheit zur Äußerung [stell2]und dann eine mit Gründen versehene Stellungnahme ab. "
     "[w258b]Kommt der Staat ihr nicht innerhalb der Frist nach, kann die Kommission den Gerichtshof anrufen.", PS),
    # --- D A. Zulässigkeit ------------------------------------------------------------------------------------------------
    ("[zul]A, Zulässigkeit. [zust]Erstens, die Zuständigkeit: Es entscheidet der Gerichtshof selbst. Artikel "
     "zweihundertsechsundfünfzig weist diese Klage nicht dem Gericht der Union zu. [partei]Zweitens, die Parteifähigkeit: "
     "Klägerin ist die Kommission, Beklagte die Bundesrepublik Deutschland. [a259]Nach Artikel zweihundertneunundfünfzig "
     "kann auch ein Mitgliedstaat klagen, muss aber zuerst die Kommission befassen.", PS),
    ("[vorv]Drittens, das ordnungsgemäße Vorverfahren. [mahn2]Das Mahnschreiben gibt Gelegenheit zur Äußerung, "
     "[begr]die begründete Stellungnahme setzt eine Frist. [deck]Die Klage darf nur auf Rügen gestützt werden, die schon "
     "im Vorverfahren erhoben wurden. Der Streitgegenstand muss deckungsgleich sein. [nit3]Im Nitrat-Fall hielt die "
     "Stellungnahme die Rügen des Mahnschreibens aufrecht, die Frist lief am elften September zweitausendvierzehn ab.", PS),
    ("[zeit]Dieser Tag ist entscheidend: Ob ein Verstoß vorliegt, beurteilt der Gerichtshof nach der Lage bei "
     "Fristablauf. Spätere Änderungen zählen nicht. [rsb]Viertens, Klageart und Rechtsschutzbedürfnis: Statthaft ist die "
     "Vertragsverletzungsklage. Ein besonderes Interesse muss die Kommission nicht nachweisen, auch nicht, wenn der Staat "
     "den Verstoß später abstellt. [zul2]Die Klage ist zulässig.", PS),
    # --- E B. Begründetheit --------------------------------------------------------------------------------------------
    ("[bgr]B, Begründetheit: Hat Deutschland gegen Unionsrecht verstoßen? [zurech]Der Mitgliedstaat steht für alle seine "
     "Stellen ein, auch für Länder und Gerichte. Im Nitrat-Fall zählten etwa die Regeln der Länder zur Lagerung von Dung. "
     "[pfl]Die Richtlinie verlangt zusätzliche Maßnahmen, sobald deutlich wird, dass das Aktionsprogramm nicht reicht.", PS),
    ("[eutro]Der Gerichtshof stellte fest: An Nord- und Ostsee hatte sich die Überdüngung der Küstengewässer nicht "
     "gebessert. Die Maßnahmen reichten nicht. [prog]Auch das Aktionsprogramm selbst war mangelhaft, etwa bei Sperrzeiten, "
     "gefrorenen Böden, Hanglagen und dem Lagerraum für Dung.", PS),
    ("[recht]Deutschland verteidigte sich: Die Wirkung früherer Regeln lasse sich noch nicht bewerten, und Regeln je "
     "nach Region seien schwer zu verwalten. [intern]Das half nicht: Ein Mitgliedstaat kann sich nicht auf Umstände seiner "
     "internen Rechtsordnung berufen.", P),
    ("[an2]Und die Düngeverordnung von zweitausendsiebzehn kam erst nach Fristablauf. Sie zählt nicht.", P, "Antonia"),
    ("[bgr2]Die Klage ist begründet.", PS),
    # --- F C. Urteil und Art. 260 ------------------------------------------------------------------------------------------
    ("[urt]C, das Urteil: Am einundzwanzigsten Juni zweitausendachtzehn stellte der Gerichtshof den Verstoß fest. "
     "[fest]Das ist ein Feststellungsurteil. Nach Artikel zweihundertsechzig Absatz eins muss Deutschland die Maßnahmen "
     "ergreifen, die sich aus dem Urteil ergeben.", PS),
    ("[wl260]Tut der Staat das nicht, kann die Kommission nach Absatz zwei erneut den Gerichtshof anrufen, nachdem sie "
     "ihm Gelegenheit zur Äußerung gegeben hat. [geld]Der Gerichtshof kann dann einen Pauschalbetrag oder ein Zwangsgeld "
     "verhängen. [abs3]Nach Absatz drei geht das schon im ersten Urteil, wenn ein Staat die Umsetzung einer Richtlinie "
     "nicht mitteilt.", PS),
    ("[danach]Im Nitrat-Fall beschloss die Kommission im Juli zweitausendneunzehn, Deutschland nach Artikel "
     "zweihundertsechzig ein Aufforderungsschreiben zu schicken: Die Mängel seien nicht vollständig behoben.", PS),
    # --- G Ergebnis ----------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Die Klage der Kommission hat Erfolg. Sie ist zulässig und begründet.", P),
    ("[ko2]Dann zählt die neue Düngeverordnung erst bei der Umsetzung des Urteils.", PS, "Konstantin"),
    # --- H Klausurtipp (Lexi) ----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Vergleiche Mahnschreiben, Stellungnahme und Klageantrag. [tipp2]Eine Rüge, die im Vorverfahren "
     "fehlte, kann die Kommission nicht nachschieben. [tipp3]Und Änderungen nach Fristablauf prüfst du nicht als "
     "Rechtfertigung: Sie lassen den Verstoß bestehen.", PS),
    # --- I Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sa]A, Zulässigkeit: [sa1]Zuständigkeit des Gerichtshofs, [sa2]Parteifähigkeit, "
     "[sa3]ordnungsgemäßes Vorverfahren mit deckungsgleichem Streitgegenstand, [sa4]Klageart und Rechtsschutzbedürfnis. "
     "[sb]B, Begründetheit: [sb1]Verstoß des Mitgliedstaats bei Fristablauf, [sb2]keine Rechtfertigung durch "
     "innerstaatliche Gründe. [sc]C, Urteil: [sc1]Feststellung nach Artikel zweihundertsechzig Absatz eins, "
     "[sc2]bei Nichtbefolgung Pauschalbetrag oder Zwangsgeld nach Absatz zwei.", PS),
    # --- J Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Das Vorverfahren zieht den Rahmen, [m1]der Fristablauf hält die Lage fest, [m2]und wer das Urteil "
     "missachtet, riskiert ein Zwangsgeld.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
