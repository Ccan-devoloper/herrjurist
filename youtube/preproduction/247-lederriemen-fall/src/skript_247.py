"""Folge 247 · Lederriemen-Fall: Eventualvorsatz oder bewusste Fahrlässigkeit? (Mo · Der Fall · StGB AT · Klassiker-Fall).
Echter Fall, vereinfacht und mit anderen Namen: BGH, Urt. v. 22.4.1955 – 5 StR 35/55, BGHSt 7, 363 (Lederriemen). Sachverhalt
nach übereinstimmenden Sekundärquellen (Original nicht frei verfügbar, siehe ../RECHTSSTAND.md): Zwei Männer wollen einen
Bekannten ausrauben; Schlaftabletten scheitern; der Plan, ihn mit einem Lederriemen bis zur Bewusstlosigkeit zu würgen, wird
verworfen, weil er sterben könnte; stattdessen Sandsack; einer nimmt den Riemen heimlich mit; der Sandsack platzt; beide drosseln
das Opfer mit dem Riemen, bis es sich nicht mehr rührt; Beute; vergebliche Wiederbelebung; Tod.
ACHTUNG Themenplan: Dort steht „erst Sandsack (verworfen, weil zu gefährlich), dann Riemen“ – nach den Quellen ist es umgekehrt
(Riemen als zu gefährlich verworfen, dann Sandsack, der platzt, dann doch Riemen). Das Skript folgt den Quellen.
Prüfung: § 15 (Wortlautkarte), §§ 212/211 vs. § 222 (und § 251); Problem Wollen; BGHSt 7, 363: Billigen im Rechtssinne (nach
BGH 1 StR 333/22 Rn. 2 und 5 StR 344/05 Rn. 28, die BGHSt 7, 363, 368 ff./369 zitieren); heutige Formel BGHSt 65, 42 Rn. 22
(Wissens-/Willenselement, bewusste Fahrlässigkeit), Rn. 23 (Gesamtschau, Gefährlichkeit als wesentlicher Indikator); Hemmschwelle
BGHSt 57, 183 Rn. 42, 45; Subsumtion; Mord (Habgier, Ermöglichungsabsicht: BGH 2 StR 391/20 Rn. 27 f., BGHSt 39, 159);
Gegenansichten Möglichkeits-/Wahrscheinlichkeitstheorie (Lehre, Uni Freiburg KK 200 f.); Klausurtipp, Schema, Merksatz (Lexi).
Vorsatzformen nur verwiesen (Folge 029).
DARSTELLUNG: keine Würgeszene, kein Riemen am Hals, keine Gewalt im Bild; nur Symbole (Riemen auf dem Tisch, Sandsack, Pillen);
das Opfer erscheint nicht als Figur (FOLGE-ABLAUF Abschnitt 1: Opfer realer Taten nicht als Comicfigur), keine Leiche.
Stimmen (Pool william, sabrina, marc, laura_ruhig): Willi william, Hans marc. Erzählerin und Lexi: Carla ohne Rolle.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Willi": "william", "Hans": "marc"}

SEGMENTE = [
    # --- A Fall: der Plan, die Nacht ----------------------------------------------------------------------------------------
    ("[fall]Ein echter Fall, vereinfacht und mit anderen Namen. [plan]Willi und Hans wollen einen Bekannten ausrauben, einen "
     "Versicherungskaufmann. [pillen]Erst versuchen sie es mit Schlaftabletten, vergeblich. [riemen]Dann schlägt Willi einen "
     "Lederriemen vor.", 0.2),
    ("[wi1]Mit dem Riemen würgen wir ihn, bis er bewusstlos ist.", P, "Willi"),
    ("[ha1]Zu gefährlich. Daran kann er sterben. Nehmen wir lieber einen Sandsack.", P, "Hans"),
    ("[sandsack]Der Sandsack soll den Mann nur betäuben. [heimlich]Doch Willi steckt den Riemen heimlich ein, für alle Fälle. "
     "[nacht]Die beiden übernachten bei ihrem Bekannten. Gegen vier Uhr morgens schlägt Hans mit dem Sandsack zu. "
     "[platzt]Der Sandsack platzt, es kommt zum Handgemenge. [zieh]Da greifen beide doch zum Riemen und drosseln ihn, bis er "
     "sich nicht mehr rührt. [beute]Sie suchen sich Kleidung aus seiner Wohnung aus. [tot]Ihre Wiederbelebungsversuche "
     "scheitern. Der Mann ist tot.", 0.4),
    ("[frage]Den Tod wollten die beiden gerade nicht. [frage2]Haben sie trotzdem vorsätzlich getötet, oder nur fahrlässig?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 15 (Wortlautkarte), Weiche Vorsatz/Fahrlässigkeit ------------------------------------------------------------
    ("[p15]Die Weiche stellt Paragraf fünfzehn: Strafbar ist nur vorsätzliches Handeln, wenn nicht das Gesetz fahrlässiges "
     "Handeln ausdrücklich mit Strafe bedroht. [folge]Mit Vorsatz wäre es Totschlag nach Paragraf zweihundertzwölf, vielleicht "
     "sogar Mord. [p222]Ohne Vorsatz kämen fahrlässige Tötung nach Paragraf zweihundertzweiundzwanzig und Raub mit Todesfolge "
     "in Betracht. [problem]Dass Würgen tödlich sein kann, wussten beide. Fraglich ist das Wollen: Eventualvorsatz oder "
     "bewusste Fahrlässigkeit? [f29]Die drei Vorsatzformen findest du in Folge neunundzwanzig.", P),
    # --- D BGHSt 7, 363: Billigen im Rechtssinne ----------------------------------------------------------------------------
    ("[bgh]Der Bundesgerichtshof entschied den Lederriemen-Fall neunzehnhundertfünfundfünfzig. [unerw]Er räumte ein: Vieles "
     "spricht dafür, dass den beiden der Tod höchst unerwünscht war. [recht]Doch Billigen ist im Rechtssinne zu verstehen. Der Erfolg muss nicht den Wünschen des "
     "Täters entsprechen. [notfalls]Es genügt, dass sich der Täter um seines Zieles willen notfalls damit abfindet, dass seine "
     "Handlung den an sich unerwünschten Erfolg herbeiführt. [heute]Darauf stützt sich der Bundesgerichtshof bis heute.", P),
    # --- E Heutige Formel, bewusste Fahrlässigkeit, Gesamtschau, Hemmschwelle -----------------------------------------------
    ("[formel]Die heutige Formel hat zwei Elemente. [wissen]Wissenselement: Der Täter erkennt den Tod als mögliche, nicht ganz "
     "fernliegende Folge. [wollen]Willenselement: Er billigt ihn oder findet sich um seines Zieles willen mit ihm ab, mag er "
     "ihm auch unerwünscht sein. [bf]Bewusst fahrlässig handelt dagegen, wer ernsthaft und nicht nur vage darauf vertraut, "
     "der Tod werde nicht eintreten. [gesamt]Entschieden wird in einer Gesamtschau aller Umstände. Die Gefährlichkeit der "
     "Handlung ist dabei ein wesentlicher Indikator. [hemm]Und bei Tötungsdelikten ersetzt das Schlagwort Hemmschwelle keine "
     "Begründung. Es verlangt nur eine sorgfältige Gesamtwürdigung.", P),
    # --- F Subsumtion -----------------------------------------------------------------------------------------------------
    ("[sub]Zurück zum Fall. [s_wissen]Beide sahen die Todesgefahr, deshalb hatten sie den Riemen zuerst verworfen. Das "
     "Wissenselement liegt vor. [s_vertr]Und ein Vertrauen? Als der Sandsack versagte, griffen sie trotzdem zum Riemen und "
     "zogen mit aller Kraft. Auf ein gutes Ende konnten sie da nur noch vage hoffen. [s_ziel]Um an die Beute zu kommen, "
     "nahmen sie den Tod notfalls hin. [s_unerw]Dass er ihnen höchst unerwünscht war, zeigen die Wiederbelebungsversuche. Am "
     "Billigen im Rechtssinne ändert das nichts. [s_ev]Beide handelten mit Eventualvorsatz.", P),
    # --- G Ergebnis: Totschlag, Mord ---------------------------------------------------------------------------------------
    ("[erg]Damit ist der Totschlag erfüllt. [mord]Weil sie würgten, um zu rauben, kommt sogar Mord in Betracht: aus Habgier "
     "und um eine andere Straftat zu ermöglichen. [mord2]Die Ermöglichungsabsicht verträgt sich nach dem Bundesgerichtshof auch "
     "mit bedingtem Tötungsvorsatz. [urteil]Im echten Fall wurden beide wegen Mordes verurteilt, und der Bundesgerichtshof "
     "bestätigte das.", PS),
    # --- H Gegenansichten (Lehre) ------------------------------------------------------------------------------------------
    ("[lehre]Die Lehre kennt auch Ansichten, die auf das Wollen verzichten. [moegl]Nach der Möglichkeitstheorie genügt, dass "
     "der Täter die konkrete Möglichkeit erkennt und trotzdem handelt. [wahr]Die Wahrscheinlichkeitstheorie verlangt, dass er "
     "den Erfolg für wahrscheinlich hält. [kritik]Dagegen spricht: Beim Wissen gleichen sich Eventualvorsatz und bewusste "
     "Fahrlässigkeit. Den Unterschied macht erst das Wollen.", PS),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne im subjektiven Tatbestand sauber zwischen Wissens- und Willenselement. [k1]Lass dich von einem "
     "unerwünschten Erfolg nicht täuschen. Auch ihn kann der Täter im Rechtssinne billigen. [k2]Suche im Sachverhalt nach "
     "echten Gründen für ein Vertrauen, etwa nach Vorsichtsmaßnahmen. Vages Hoffen genügt nicht.", P),
    # --- J Klausurschema (Lexi), progressiv --------------------------------------------------------------------------------
    ("[sch]So prüfst du Willi und Hans: [s1]Paragrafen zweihundertzwölf und zweihundertelf. Erstens der objektive Tatbestand: "
     "Der Mann ist tot, das Drosseln war ursächlich. [s2]Zweitens der Vorsatz: Wissenselement gegeben, Willenselement gegeben, "
     "also Eventualvorsatz. [s3]Drittens die Mordmerkmale: Habgier und Ermöglichungsabsicht. [s4]Danach Rechtswidrigkeit und "
     "Schuld.", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Billigen heißt nicht wünschen. [m2]Wer den Tod als möglich erkennt und ihn um seines Zieles willen notfalls "
     "hinnimmt, handelt mit Eventualvorsatz. [m3]Bewusst fahrlässig handelt nur, wer ernsthaft auf das Ausbleiben vertraut.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
