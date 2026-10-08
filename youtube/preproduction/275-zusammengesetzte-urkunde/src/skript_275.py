"""Folge 275 · Zusammengesetzte Urkunde: Das vertauschte Preisschild § 267 (Mi · Examenswissen · StGB BT, Format Abgrenzung).
Fall nach dem Plan-Hook („Ein Kunde klebt im Baumarkt das Preisschild eines billigen Bohrers auf einen teuren“): In einem
Baumarkt (fiktiv, ohne Marke) hängen zwei Bohrmaschinen, auf jeder klebt ein Preisschild des Marktes (29 € und 149 €).
Karlheinz (um 60) zieht das Schild der billigen ab, reißt das Schild der teuren ab und klebt das 29-€-Schild fest auf die
teure. An der Kasse tippt die Kassiererin Frau Gundlach den Preis vom Schild ein; Karlheinz zahlt 29 € und nimmt die teure
Maschine mit.
Aufbau nach Auftrag: 1. Hook → Sachverhalt → 2. § 267 Abs. 1 (Wortlautkarte), Urkundenbegriff kurz (Verweis auf die Folge
zur gefälschten Entschuldigung) → 3. zusammengesetzte Urkunde: Erklärung + Bezugsobjekt fest verbunden = neue Beweiseinheit
(OLG Karlsruhe, Beschl. v. 13.3.2019 – 1 Rv 3 Ss 691/18, Rn. 26–31; BGH 3 StR 521/18 Rn. 33), wann fest verbunden
(Rn. 31, 36, 37) → 4. Umkleben: Verfälschen durch Austausch des Bezugsobjekts (Rn. 36; a. A. SK-Hoyer), zugleich Herstellen
einer unechten Urkunde (Übungsliteratur ZJS 2009, 72 f.; ZJS 2022, 83 f.), Gebrauchen (BGH 3 StR 521/18 Rn. 34); Variante
offener Karton (Rn. 37 mit OLG Köln 1 Ss 231/78) → 5. Betrug an der Kasse (Wortlautkarte § 263 Abs. 1; Rn. 18, 20, 21),
Konkurrenzen (BGH 3 StR 156/08 Rn. 11; 5 StR 38/23 Rn. 12) → 6. Klausurtipp (Lexi, § 274: Rn. 33) → Prüfschema → Merksatz
(Lexi). Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Volltextsuche unter youtube/preproduction und themenplanung:
0 Treffer; Reservierung „275: Karlheinz, Gundlach“): Karlheinz, Gundlach; nie im Genitiv.
Stimmen (Pool niklas, helmut, ela_froh, julia): Karlheinz helmut (Mann, älter), Frau Gundlach ela_froh (Frau, jung,
freundlich); niklas und julia sprachen in der Vorfolge 273. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Beträge im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Karlheinz": "helmut", "Gundlach": "ela_froh"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Baumarkt, Werkzeugregal --------------------------------------------------------------------------------
    ("[fall]Ein Baumarkt, die Werkzeugabteilung. [zwei]Im Regal hängen zwei Bohrmaschinen, auf jeder klebt ein "
     "Preisschild des Marktes: [billig]auf der einen neunundzwanzig Euro, [teuer]auf der anderen hundertneunundvierzig "
     "Euro. [abzieh]Karlheinz zieht das billige Schild ab. [abreiss]Das Schild der teuren Maschine reißt er ab, [kleb]und "
     "das billige klebt er fest darauf.", P),
    ("[ka1]So, jetzt kostet die hier neunundzwanzig Euro.", P, "Karlheinz"),
    # --- A2 Fall: Kasse --------------------------------------------------------------------------------------------------
    ("[kasse]An der Kasse tippt die Kassiererin, Frau Gundlach, den Preis vom Schild ein.", P),
    ("[ga1]Neunundzwanzig Euro, bitte.", P, "Gundlach"),
    ("[zahlt]Karlheinz zahlt und nimmt die teure Maschine mit. [frage]Hat er eine Urkunde gefälscht? Das Preisschild "
     "selbst ist ja echt. [frage2]Und was gilt für den Betrug an der Kasse?", 0.6),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 267 Abs. 1 und Urkundenbegriff (Verweis) ------------------------------------------------------------------
    ("[p267]Paragraf zweihundertsiebenundsechzig, Absatz eins: [w267]Wer zur Täuschung im Rechtsverkehr eine unechte "
     "Urkunde herstellt, eine echte Urkunde verfälscht oder eine unechte oder verfälschte Urkunde gebraucht, wird mit "
     "Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe bestraft. [begriff]Was eine Urkunde ist, kennst du aus der "
     "Folge zur gefälschten Entschuldigung: [def]eine verkörperte Gedankenerklärung, die zum Beweis im Rechtsverkehr "
     "geeignet und bestimmt ist und ihren Aussteller erkennen lässt. [drei]Kurz: Perpetuierung, Beweis und Garantie.", PS),
    # --- D Zusammengesetzte Urkunde ------------------------------------------------------------------------------------
    ("[allein]Nur: Ein Preisschild allein sagt bloß neunundzwanzig Euro. Wofür, verrät erst die Ware. [zus]Hier hilft "
     "die zusammengesetzte Urkunde. Eine Erklärung wird mit ihrem Bezugsobjekt fest verbunden, [einheit]und beide bilden "
     "zusammen eine neue Beweiseinheit. [bz]Die Erklärung kann auch ein bloßes Zeichen sein, ein sogenanntes "
     "Beweiszeichen. Der Klassiker ist die Fahrzeugidentifikationsnummer am Auto. [olg]Aufgeklebte Preisschilder auf "
     "Waren zählt das Oberlandesgericht Karlsruhe ebenfalls dazu, und für den Strichcode im Baumarkt hat es das "
     "entschieden. [aussage]Schild und Maschine sagen zusammen: Der Markt bietet diese Maschine für neunundzwanzig Euro "
     "zum Kauf an. [aussteller]Aussteller ist der Baumarkt. Eine Unterschrift braucht es nicht, es genügt, dass erkennbar ist, wer "
     "dahintersteht.", PS),
    # --- E Wann fest verbunden? ----------------------------------------------------------------------------------------
    ("[fest]Entscheidend ist die feste Verbindung. Sie muss nicht untrennbar sein, aber auf Dauer angelegt. "
     "[kleber]Ein mit Klebstoff aufgeklebtes Etikett genügt. [lose]Ein nur lose angeheftetes Schild dagegen nicht, "
     "[steck]ebenso wenig ein Teil, das bloß aufgesteckt ist. [vorher]Vor der Tat gab es also zwei echte "
     "zusammengesetzte Urkunden: jede Maschine mit ihrem Schild.", PS),
    # --- F Umkleben: Verfälschen oder Herstellen -------------------------------------------------------------------------
    ("[umk]Jetzt das Umkleben. [neu]Karlheinz verbindet das billige Schild fest mit der teuren Maschine. Die neue "
     "Einheit sieht so aus, als hätte der Markt genau das erklärt. Das hat er nicht. [verf]Die Rechtsprechung nimmt ein "
     "Verfälschen an: Eine zusammengesetzte Urkunde kann schon durch den Austausch ihres Bezugsobjekts verfälscht werden. "
     "[herst]Zugleich stellt Karlheinz eine unechte Urkunde her, denn der Markt ist nur scheinbar ihr Aussteller. In "
     "Falllösungen tritt das Herstellen dann hinter dem Verfälschen zurück. [gegen]Eine Gegenansicht hält den bloßen "
     "Austausch des Bezugsobjekts nicht für ein Verfälschen. [neufest]Wichtig ist: Auch die neue Verbindung muss fest "
     "sein. Hier klebt das Schild fest auf der teuren Maschine.", PS),
    ("[gebr]An der Kasse legt Karlheinz die Maschine vor. Damit gebraucht er die Urkunde. [subj]Er handelt vorsätzlich "
     "und will, dass Frau Gundlach die Kombination für echt hält und nur neunundzwanzig Euro verlangt. Das ist Täuschung "
     "im Rechtsverkehr. [karton]Anders liegt es, wenn jemand die teure Maschine in den offenen Karton der billigen "
     "steckt: Das Schild klebt dann nur am Karton. Mit dem Inhalt ist es nicht fest verbunden, und Paragraf "
     "zweihundertsiebenundsechzig scheidet regelmäßig aus.", PS),
    # --- G Betrug an der Kasse ---------------------------------------------------------------------------------------
    ("[betrug]Bleibt der Betrug an der Kasse. [p263]Paragraf zweihundertdreiundsechzig, Absatz eins, verlangt: "
     "[w263]Täuschung, Irrtum, Vermögensverfügung und Schaden, dazu Vorsatz und Bereicherungsabsicht. "
     "[t1]Wer eine Ware mit falschem Schild an der Kasse vorlegt, spiegelt schlüssig einen falschen Preis vor. "
     "[t2]Frau Gundlach hält neunundzwanzig Euro für den richtigen Preis. [t3]Sie händigt die Maschine freiwillig aus. "
     "Das ist eine Vermögensverfügung, kein Gewahrsamsbruch, also kein Diebstahl. [t4]Der Markt gibt die teure Maschine "
     "her und bekommt nur den Preis der billigen. [t5]Karlheinz handelt vorsätzlich und will sich rechtswidrig "
     "bereichern.", PS),
    ("[erg]Rechtswidrig und schuldhaft handelt er auch. [konk]Urkundenfälschung und Betrug stehen in Tateinheit, denn "
     "das Vorlegen an der Kasse ist Gebrauchen und Täuschung zugleich. [erg2]Ergebnis: Karlheinz ist strafbar wegen "
     "Urkundenfälschung in Tateinheit mit Betrug.", PS),
    # --- H Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Frag bei jedem Schild zuerst, womit es fest verbunden ist. Erst Schild und Ware zusammen sind "
     "die Urkunde. [tipp2]Und prüfe das abgerissene teure Schild gesondert: Wer ein fest aufgeklebtes Etikett abreißt, "
     "kann sich wegen Urkundenunterdrückung nach Paragraf zweihundertvierundsiebzig strafbar machen.", PS),
    # --- I Prüfschema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k1]Römisch eins: Tatbestand. [k1a]Objektiv erstens die zusammengesetzte Urkunde: Erklärung "
     "und Bezugsobjekt, fest verbunden. [k1b]Zweitens die Tathandlung: Verfälschen durch Austausch, zugleich Herstellen, "
     "und Gebrauchen an der Kasse. [k1c]Subjektiv Vorsatz und Handeln zur Täuschung im Rechtsverkehr. [k2]Römisch zwei "
     "und drei: Rechtswidrigkeit und Schuld. [k4]Römisch vier: Konkurrenzen, Tateinheit mit Betrug.", PS),
    # --- J Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein Preisschild allein ist keine Urkunde, erst fest verbunden mit der Ware. [m2]Wer es fest auf eine "
     "andere Ware klebt, fälscht eine Urkunde, [m3]und wer damit an der Kasse bezahlt, begeht zugleich einen "
     "Betrug.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
