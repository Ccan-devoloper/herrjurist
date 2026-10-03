"""Folge 104 · Mittäterschaft § 25 II StGB: Tatplan, Tatbeitrag, Zurechnung (Mi · Examenswissen · StGB AT, Format Schema).
Fall nach dem Plan-Hook: Kioskraub zu dritt (Thea steht Schmiere, Kilian droht nur mit Worten und Körpersprache, Fenja
greift in die Kasse: 650 €), Ansgar hat alles geplant und bleibt zu Hause. Keine Waffe, niemand wird verletzt.
Aufbau: Wortlaut § 25 II, Voraussetzungen und Rechtsfolge → Aufbau (gemeinsame Prüfung Kilian/Fenja, getrennte Prüfung
Thea/Ansgar; Hefendehl-Skript KK 716 f.) → Raub kurz (Verweis Folge 087) → 1. gemeinsamer Tatplan (BGH 5 StR 533/22 Rn. 7;
sukzessive Mittäterschaft ein Satz: 4 StR 115/24 Rn. 56) → 2. gemeinsame Tatausführung, Zueignungsabsicht selbst
(3 StR 148/18 Rn. 7) → Abgrenzung Täter/Gehilfe: Tatherrschaftslehre vs. BGH (3 StR 363/22 Rn. 8; 3 StR 189/19 Rn. 4 f.)
→ Thea: Schmiere (4 StR 665/11 Rn. 24; 4 StR 420/05 Rn. 4 f.), Wortlaut § 27 I, Hilfeleisten (3 StR 496/23 Rn. 42)
→ Ansgar: strenge/gemäßigte Tatherrschaftslehre/BGH, Streitentscheid → Rechtsfolge, Exzess (4 StR 115/24 Rn. 44)
→ Ergebnis → Klausurtipp → Schema → Merksatz. Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Ansgar, Kilian, Fenja, Thea, Emil.
Nie im Genitiv mit -s. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.45

STIMMEN = {"Ansgar": "helmut", "Kilian": "niklas", "Fenja": "julia"}  # Thea und Emil sprechen nicht; Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: die Planung ----------------------------------------------------------------------------------------------
    ("[fall]Ansgar hat einen Plan. [kiosk]Der Kiosk an der Ecke soll überfallen werden, kurz vor Ladenschluss, wenn der "
     "Inhaber Emil allein ist. [idee]Die Idee stammt von Ansgar. Er hat den Kiosk ausgesucht, die Uhrzeit festgelegt und "
     "die Rollen verteilt.", 0.3),
    ("[a1]Kilian redet, Fenja holt das Geld, Thea passt draußen auf. Ich bleibe zu Hause.", 0.3, "Ansgar"),
    ("[teil]Die Beute wollen sich Ansgar, Kilian und Fenja teilen. Thea bekommt fest fünfzig Euro. [weg_a]Während des "
     "Überfalls hat Ansgar keinen Kontakt zu den anderen.", 0.3),
    # --- A2 Fall: der Kiosk ------------------------------------------------------------------------------------------------
    ("[ecke]Am Abend steht Thea an der Ecke. Sie soll pfeifen, falls jemand kommt. Das gibt den anderen Sicherheit. "
     "[theke]Kilian baut sich vor der Theke auf.", 0.3),
    ("[k1]Hände weg vom Telefon, sonst schlage ich zu!", 0.3, "Kilian"),
    ("[emil]Emil weicht erschrocken zurück. [kasse]Fenja greift in die Kasse und nimmt sechshundertfünfzig Euro.", 0.3),
    ("[f1]Ich hab das Geld. Los!", 0.3, "Fenja"),
    ("[flucht]Die drei laufen davon. Verletzt wird niemand. [frage]Wer ist hier Mittäter, wer nur Gehilfe? [frage2]Und "
     "was ist mit Ansgar, der gar nicht dabei war?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 25 II, Voraussetzungen ------------------------------------------------------------------------------
    ("[p25]Paragraf fünfundzwanzig, Absatz zwei: [p25w]Begehen mehrere die Straftat gemeinschaftlich, so wird jeder als "
     "Täter bestraft. [vor]Mittäterschaft hat zwei Voraussetzungen: [v1]einen gemeinsamen Tatplan [v2]und eine gemeinsame "
     "Tatausführung.", PS),
    # --- D Aufbau -----------------------------------------------------------------------------------------------------------
    ("[aufbau]Zuerst der Aufbau. [gem]Ist die Mittäterschaft eindeutig, etwa bei gleichwertigen Beiträgen, prüfst du die "
     "Beteiligten gemeinsam. [getr]Ist sie bei einem fraglich, prüfst du getrennt: erst den Tatnächsten, dann die anderen "
     "mit Zurechnung. [wahl]Kilian und Fenja prüfen wir gemeinsam: Jeder "
     "verwirklicht einen Teil des Raubes, ihr Zusammenwirken liegt auf der Hand. [wahl2]Thea und Ansgar prüfen wir danach "
     "getrennt, denn gerade ihre Täterschaft ist das Problem.", PS),
    # --- E Kilian und Fenja: Raub, Zurechnung --------------------------------------------------------------------------------
    ("[raub]Also: Raub durch Kilian und Fenja. [drohk]Kilian droht mit Schlägen, also mit gegenwärtiger Gefahr für Leib. "
     "[wegf]Fenja nimmt das Geld aus der Kasse und bricht damit den Gewahrsam von Emil. [final]Die Drohung soll genau diese "
     "Wegnahme ermöglichen. Details kennst du aus unserer Folge zum Raub. [keiner]Aber keiner erfüllt alles "
     "allein: Kilian nimmt nichts weg, Fenja droht nicht. Deshalb die Zurechnung.", PS),
    ("[tp]Erstens: der gemeinsame Tatplan. [tp1]Die vier haben die Rollen ausdrücklich verabredet. [konk]Ein Tatplan "
     "kann aber auch stillschweigend entstehen, etwa durch arbeitsteiliges Handeln. [sukz]Und wer erst während der "
     "Ausführung einsteigt und das Bisherige kennt und billigt, kann noch sukzessiver Mittäter werden.", PS),
    ("[ta]Zweitens: die gemeinsame Tatausführung. Jeder braucht einen wesentlichen Tatbeitrag. [ta1]Drohung und Griff in "
     "die Kasse greifen ineinander, beide Beiträge sind wesentlich. [zueig]Nicht zugerechnet wird die Zueignungsabsicht, "
     "die braucht jeder selbst. Beide wollen ihren Anteil behalten. [kf]Kilian und Fenja sind Mittäter eines Raubes.", PS),
    # --- F Abgrenzung Täter – Gehilfe -----------------------------------------------------------------------------------
    ("[abgr]Schwieriger sind Thea und Ansgar: Täter oder nur Gehilfe? [thl]Die "
     "Tatherrschaftslehre fragt, ob jemand das Geschehen arbeitsteilig mitbeherrscht. "
     "[bgh]Der Bundesgerichtshof entscheidet in einer wertenden Gesamtbetrachtung. [kr1]Maßgeblich sind "
     "der Grad des eigenen Interesses an der Tat, [kr2]der Umfang der Tatbeteiligung [kr3]und die Tatherrschaft oder "
     "wenigstens der Wille dazu.", PS),
    # --- G Thea: Schmiere stehen, § 27 ------------------------------------------------------------------------------------
    ("[thea]Zuerst Thea. Schmiere stehen ist ein Klassiker: [klass]Je nach Gewicht kann es Mittäterschaft sein oder nur "
     "Beihilfe. [thea2]Thea hat nicht mitgeplant und bekommt nur fünfzig Euro. Ihr eigenes Interesse ist gering. "
     "[thea3]Sie sichert nur ab, auf Ob und Wie der Tat hat sie keinen Einfluss. [bgh_s]Eine solche bloße Absicherung sieht "
     "der Bundesgerichtshof als untergeordneten Beitrag. [beide]Beide Ansichten kommen hier zum selben Ergebnis: Thea ist "
     "keine Mittäterin.", PS),
    ("[p27]Bleibt die Beihilfe, Paragraf siebenundzwanzig, Absatz eins: [p27w]Als Gehilfe wird bestraft, wer vorsätzlich "
     "einem anderen zu dessen vorsätzlich begangener rechtswidriger Tat Hilfe geleistet hat. [hilfe]Hilfe leistet, wer die "
     "Tat fördert oder erleichtert. [thea4]Thea sichert den Überfall ab und bestärkt die anderen, und das weiß sie. "
     "[thea5]Thea ist Gehilfin.", PS),
    # --- H Ansgar: der Planer ohne Mitwirkung im Ausführungsstadium ----------------------------------------------------------
    ("[ans]Jetzt Ansgar. [streng]Die strenge Tatherrschaftslehre verlangt von jedem "
     "Mittäter einen Beitrag im Ausführungsstadium, zumindest Kontakt zu den anderen während der Tat. [streng2]Danach wäre "
     "Ansgar nur Anstifter. [gemae]Die gemäßigte Tatherrschaftslehre lässt einen Beitrag in der Vorbereitung genügen, wenn "
     "ein Plus an Planung das Fehlen am Tatort ausgleicht. [bgh_a]Der Bundesgerichtshof verlangt keine Anwesenheit am "
     "Tatort. Auch eine bloße Vorbereitung kann reichen.", PS),
    ("[ents]Wir folgen der gemäßigten Ansicht. [arg1]Entscheidend ist das Gewicht eines Beitrags, nicht sein Zeitpunkt. "
     "[arg2]Sonst stünde gerade der besser da, der so gut plant, dass er selbst nicht hingehen muss. [ans2]Ansgar hatte die "
     "Idee, hat Ort, Zeit und Rollen bestimmt und will ein Drittel der Beute. [ans3]Das gleicht sein Fehlen am Tatort aus. "
     "Auch nach dem Bundesgerichtshof ist Ansgar Mittäter.", PS),
    # --- I Rechtsfolge, Exzess, Ergebnis -------------------------------------------------------------------------------------
    ("[rf]Die Rechtsfolge: Drohung und Wegnahme werden allen Mittätern wechselseitig zugerechnet, jeder wird als Täter "
     "bestraft. [exz]Die Grenze ist der Tatplan: Weicht einer wesentlich davon ab, ist das ein Exzess, und der wird den "
     "anderen nicht zugerechnet.", PS),
    ("[erg]Ergebnis: Kilian, Fenja und Ansgar haben gemeinschaftlich einen Raub begangen, Paragrafen zweihundertneunundvierzig "
     "und fünfundzwanzig Absatz zwei. [erg2]Thea hat Beihilfe zum Raub geleistet, Paragraf siebenundzwanzig. Ihre Strafe "
     "wird gemildert.", PS),
    # --- J Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Zurechnung prüfst du genau dort, wo dem Beteiligten ein Merkmal fehlt, [tipp2]bei Kilian also "
     "bei der Wegnahme. [tipp3]Den Streit um den Planer entscheidest du nur, wenn die Ansichten zu verschiedenen "
     "Ergebnissen kommen. Bei Ansgar ist das so.", PS),
    # --- K Klausurschema -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema mit Zurechnung. [s_i]Römisch eins: Tatbestand. "
     "[s1]Erst die objektiven Merkmale, die der Beteiligte selbst erfüllt. [s2]Für die übrigen die Zurechnung nach Paragraf "
     "fünfundzwanzig Absatz zwei: [s2a]gemeinsamer Tatplan, ohne Exzess, [s2b]und gemeinsame Tatausführung mit wesentlichem "
     "Tatbeitrag, dabei die Abgrenzung zur Beihilfe. [s3]Dann der subjektive Tatbestand, in eigener Person. [s_ii]Römisch "
     "zwei: Rechtswidrigkeit. [s_iii]Römisch drei: Schuld.", PS),
    # --- L Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Mittäter ist, wer auf Grund eines gemeinsamen Tatplans einen wesentlichen Beitrag leistet. [m_2]Dann "
     "wird ihm zugerechnet, was die anderen im Rahmen des Plans tun. [m_3]Nicht die Anwesenheit am Tatort entscheidet, "
     "sondern das Gewicht des Beitrags.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
