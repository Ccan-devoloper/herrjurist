"""Folge 049 · Rücknahme § 48 VwVfG: Muss das Café die Förderung zurückzahlen? (Mo · Der Fall · Verwaltungsrecht AT).
Übungsfall nach dem Hook des Themenplans (20.000 Euro Förderung, zwei Jahre später Rückforderung wegen Rechenfehlers):
Frau Hofmann (Café) erhält per endgültigem Bescheid 20.000 Euro aus einem Förderprogramm des Landes; ihre Angaben sind
richtig, die Förderstelle verrechnet sich (Umsatzrückgang 15 statt mindestens 30 Prozent). Das Geld geht für Miete, Löhne
und Lieferanten weg. Zwei Jahre später entdeckt Prüferin Ebert den Fehler, Herr Wagner hört Frau Hofmann an und nimmt den
Bescheid zurück (Erstattung nebst Zinsen). Prüfung: Rechtsgrundlage (§ 48 statt § 49), formell (Zuständigkeit, Anhörung
§ 28), materiell (rechtswidrig, begünstigend, Geldleistung § 48 II: Vertrauen, Verbrauch, Ausschluss Nr. 1–3, Abwägung),
Ergebnis; Gegenfall (falsche Angaben, Nr. 2): Rücknahme für die Vergangenheit, Jahresfrist § 48 IV (BVerwG 10 C 5.17),
Ermessen (kein intendiertes Ermessen, BVerwG 10 C 15.14), Erstattung und Zinsen § 49a I–III; Ausblick EU-Beihilfen.
Wortlautkarten: § 48 I 1 (vorgelesen), § 48 I 2 (vorgelesen), § 48 II 1–3 (Merkmale), § 48 IV 1 (vorgelesen), § 49a I 1
(Merkmale). Fiktive Figuren: Frau Hofmann (ela_warm), Herr Wagner (william), Prüferin Ebert (julia).
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Hofmann": "ela_warm", "Wagner": "william", "Ebert": "julia"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: das Café und der Förderbescheid -------------------------------------------------------------------
    ("[fall]Frau Hofmann führt ein kleines Café in der Altstadt. Der Umsatz ist eingebrochen. "
     "[antrag]Sie beantragt Geld aus einem Förderprogramm des Landes und gibt ihre Zahlen richtig an. "
     "[bescheid]Die Förderstelle bewilligt per Bescheid zwanzigtausend Euro.", 0.2),
    ("[ho1]Zwanzigtausend Euro! Damit kommen wir durch den Winter.", 0.3, "Hofmann"),
    ("[verbraucht]Sie bezahlt davon Miete, Löhne und Lieferanten, bis das Geld ausgegeben ist.", 0.3),
    # --- B Fall: zwei Jahre später in der Förderstelle -----------------------------------------------------------------
    ("[amt]Zwei Jahre später, in der Förderstelle. [ebert]Prüferin Ebert sieht sich die Akte noch einmal an.", 0.2),
    ("[eb1]Herr Wagner, hier ist ein Rechenfehler. Bei Frau Hofmann ist der Umsatz nur um fünfzehn Prozent gesunken. "
     "Gefördert wird erst ab dreißig.", 0.3, "Ebert"),
    ("[wa1]Dann hätte sie nichts bekommen dürfen. Wir fordern alles zurück.", 0.3, "Wagner"),
    ("[anh]Herr Wagner gibt Frau Hofmann Gelegenheit zur Stellungnahme. [rueck]Einen Monat nach ihrer Antwort nimmt er die "
     "Förderung zurück und verlangt die zwanzigtausend Euro mit Zinsen.", 0.3),
    ("[ho2]Das Geld ist doch längst ausgegeben. Und der Fehler lag beim Amt!", 0.3, "Hofmann"),
    # --- C Die Frage ----------------------------------------------------------------------------------------------------
    ("[frage]Muss das Café die Förderung zurückzahlen? [frage2]Die Antwort steht in den Paragrafen achtundvierzig "
     "und neunundvierzig a Verwaltungsverfahrensgesetz.", 0.6),
    # --- D Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Rechtsgrundlage ------------------------------------------------------------------------------------------------
    ("[rgl]Zuerst die Rechtsgrundlage. Der Förderbescheid war von Anfang an rechtswidrig, [abgr]also gilt die "
     "Rücknahme, Paragraf achtundvierzig. [widerruf]Der Widerruf nach Paragraf neunundvierzig "
     "betrifft rechtmäßige Verwaltungsakte, etwa bei zweckwidriger Verwendung. [land]Das Land wendet "
     "sein eigenes Verfahrensgesetz an, meist mit gleichem Wortlaut.", P),
    # --- F Formelle Rechtmäßigkeit --------------------------------------------------------------------------------------------
    ("[formell]Formell: Zuständig ist hier die Förderstelle, die auch bewilligt hat. [anh2]Weil die Rücknahme in ihre "
     "Rechte eingreift, muss sie vorher angehört werden, Paragraf achtundzwanzig. Das ist geschehen.", P),
    # --- G Wortlaut § 48 Abs. 1 --------------------------------------------------------------------------------------------
    ("[wl481]Materiell: Paragraf achtundvierzig Absatz eins Satz eins. Ein rechtswidriger Verwaltungsakt kann, auch nachdem "
     "er unanfechtbar geworden ist, ganz oder teilweise mit Wirkung für die Zukunft oder für die Vergangenheit "
     "zurückgenommen werden. [rw]Rechtswidrig ist der Bescheid: Fünfzehn Prozent Umsatzrückgang reichen nicht. "
     "[unanf]Dass er längst unanfechtbar ist, schadet nicht.", P),
    ("[beg]Aber Satz zwei schützt die Begünstigte: Ein begünstigender Verwaltungsakt darf nur unter den Einschränkungen "
     "der Absätze zwei bis vier zurückgenommen werden. [beg2]Der Förderbescheid begünstigt Frau Hofmann.", P),
    # --- H Vertrauensschutz § 48 Abs. 2 -----------------------------------------------------------------------------------
    ("[wl482]Für Geldleistungen gilt Absatz zwei. [v1]Die Rücknahme ist ausgeschlossen, soweit die Begünstigte auf den "
     "Bestand vertraut hat [v2]und ihr Vertrauen unter Abwägung mit dem öffentlichen Interesse schutzwürdig ist. [v3]In der "
     "Regel ist es das, wenn sie die Leistung verbraucht hat. [v4]Frau Hofmann hat vertraut, das Geld ist verbraucht.", P),
    ("[aus]Kein Vertrauen gibt es in drei Fällen, Satz drei. [aus1]Erstens: arglistige Täuschung, Drohung oder Bestechung. "
     "Nein. [aus2]Zweitens: wesentlich unrichtige oder unvollständige Angaben. Nein, ihre Zahlen "
     "stimmten. [aus3]Drittens: Sie kannte die Rechtswidrigkeit oder kannte sie grob fahrlässig nicht. Auch nein: Der "
     "Rechenfehler steckte in der Akte, der Bescheid nennt nur den Betrag.", P),
    ("[abw]Und die Abwägung? Steuergeld zurückholen will die Behörde bei jeder Rücknahme. [abw2]Aber besondere "
     "Umstände gegen den Regelfall gibt es nicht.", P),
    ("[erg]Ergebnis: Die Rücknahme ist rechtswidrig. [erg2]Ficht Frau Hofmann sie an, muss das Café die Förderung nicht "
     "zurückzahlen.", PS),
    # --- I Gegenfall: falsche Angaben, Jahresfrist ---------------------------------------------------------------------------
    ("[gegen]Jetzt der Gegenfall: Frau Hofmann hat ihren Umsatzrückgang zu hoch angegeben. [gegen2]Dann greift Nummer zwei, "
     "auf Vertrauen kann sie sich nicht berufen. [verg]Nach Satz vier wird dann in der Regel für die "
     "Vergangenheit zurückgenommen.", P),
    ("[wl484]Jetzt zählt die Frist, Absatz vier: Erhält die Behörde von Tatsachen Kenntnis, welche die Rücknahme eines "
     "rechtswidrigen Verwaltungsaktes rechtfertigen, so ist die Rücknahme nur innerhalb eines Jahres seit dem Zeitpunkt der "
     "Kenntnisnahme zulässig. [frist1]Die zwei Jahre seit dem Bescheid spielen also keine Rolle. [frist2]Nach ständiger "
     "Rechtsprechung des Bundesverwaltungsgerichts beginnt die Frist erst, wenn die Behörde die Rechtswidrigkeit erkannt hat "
     "und alle für die Entscheidung erheblichen Tatsachen vollständig kennt. [frist3]Das ist regelmäßig erst nach "
     "Anhörung und Stellungnahme der Fall. [frist4]Hier ist sie "
     "gewahrt.", P),
    # --- J Ermessen ---------------------------------------------------------------------------------------------------------
    ("[erm]Bleibt das Ermessen: Die Behörde kann zurücknehmen, sie muss nicht. [erm2]Ein intendiertes Ermessen gibt es bei "
     "der Rücknahme nach dem Bundesverwaltungsgericht grundsätzlich nicht, auch nicht bei Fördergeld. [erm3]Ein formelhafter "
     "Hinweis auf Sparsamkeit reicht nicht. Die Behörde muss abwägen, auch, in wessen Sphäre der Fehler lag.", P),
    # --- K Erstattung § 49a -------------------------------------------------------------------------------------------------
    ("[wl49a]Nimmt sie zurück, folgt Paragraf neunundvierzig a. Ist ein Verwaltungsakt mit Wirkung für die Vergangenheit "
     "zurückgenommen, sind bereits erbrachte Leistungen zu erstatten. [fest]Den Betrag setzt die Behörde durch "
     "schriftlichen Verwaltungsakt fest. [zins]Und nach Absatz drei wird verzinst, mit fünf Prozentpunkten über dem "
     "Basiszinssatz.", P),
    # --- L Ausblick Unionsrecht ---------------------------------------------------------------------------------------------
    ("[eu]Ein Ausblick: Bei EU-Beihilfen, deren Rückforderung die Kommission bestandskräftig verlangt hat, überlagert das Unionsrecht "
     "diesen Schutz. [eu2]Nach dem Europäischen Gerichtshof muss die Behörde dann sogar nach Ablauf der Jahresfrist "
     "zurücknehmen.", PS),
    # --- M Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Rücknahme prüfst du meist in der Begründetheit einer Anfechtungsklage gegen den "
     "Rücknahmebescheid. [tipp1]Den Vertrauensschutz prüfst du bei Absatz zwei, nicht erst im "
     "Ermessen. [tipp2]Und rechne die Jahresfrist ab der vollständigen Kenntnis, nicht ab dem Erlass des Bescheids.", PS),
    # --- N Klausurschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [q0]Rücknahme nach Paragraf achtundvierzig. [q1]A, Rechtsgrundlage, Abgrenzung zum "
     "Widerruf. [q2]B, formell: Zuständigkeit und Anhörung. [q3]C, materiell: Eins, rechtswidriger "
     "Verwaltungsakt. [q4]Zwei, begünstigend. [q5]Drei, bei Geldleistungen "
     "Vertrauensschutz nach Absatz zwei. [q6]Vier, Jahresfrist. [q7]Fünf, Ermessen. "
     "[q8]Danach: Erstattung und Zinsen nach Paragraf neunundvierzig a.", PS),
    # --- O Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer auf einen rechtswidrigen Förderbescheid vertraut und das Geld verbraucht hat, ist in der Regel "
     "geschützt. [m2]Wer wesentlich falsche Angaben macht, verliert diesen Schutz.", 1.4),
]
