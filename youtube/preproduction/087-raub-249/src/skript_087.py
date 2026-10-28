"""Folge 087 · Raub § 249 StGB: Prüfungsschema mit Gewalt, Wegnahme & Finalität (Fr · Klausurpraxis · StGB BT, Format Schema).
Fall nach dem Plan-Hook (Mann stößt eine Frau zu Boden und nimmt ihr die Handtasche weg), zurückhaltend erzählt: Margit bleibt
bis auf einen Schreck unverletzt; Stoß und Sturz sind nie im Bild (nur vorher/nachher, abstrakte Symbole).
Aufbau: Wortlaut § 249 I → Aufbau → fremde bewegliche Sache, Wegnahme (Verweis auf Folge 051; BGH 4 StR 338/20 Rn. 5) →
qualifiziertes Nötigungsmittel, Unterschied zu § 240 (Wortlaut), Gewalt gegen eine Person (BGH 3 StR 445/21 Rn. 5, 8) →
finaler Zusammenhang (BGH 6 StR 572/23 Rn. 5; 1 StR 398/15 Rn. 15–17) → Abwandlung 1: Gewalt aus Wut, Wegnahmeentschluss
danach (6 StR 572/23 Rn. 5; 4 StR 368/24 Rn. 7) → § 252 (Wortlaut; BGH 1 StR 389/14 Rn. 11) und § 255 (BGH 5 StR 606/17 Rn. 13;
Lehre nur genannt) → Vorsatz, Zueignungsabsicht (BGH 3 StR 148/18 Rn. 7), Rechtswidrigkeit der Zueignung (3 StR 458/25 Rn. 5) →
Ergebnis, §§ 250, 251 (ein Satz) → Abwandlung 2: Entreißen (BGH 3 StR 445/21 Rn. 5, 8) → Klausurtipp (4 StR 368/24 Rn. 7)
→ Schema → Merksatz. Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Margit, Hagen. Nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.5

STIMMEN = {"Hagen": "marc", "Margit": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall ------------------------------------------------------------------------------------------------------------
    ("[fall]Dienstagnachmittag auf dem Weg vom Wochenmarkt zur Bushaltestelle. [margit]Margit trägt ihre Handtasche über der "
     "Schulter, [geld]darin ihre Geldbörse mit achtzig Euro. [hagen]Hagen hat sie am Marktstand beim Bezahlen gesehen.", 0.3),
    ("[h1]Die Handtasche hole ich mir.", 0.3, "Hagen"),
    ("[stoss]Er läuft auf Margit zu und stößt sie zu Boden, um an die Tasche zu kommen. [nimmt]Dann nimmt er die Handtasche "
     "[weg]und rennt davon. Er will sie samt Geld behalten. [schreck]Margit steht wieder auf. Sie hat sich erschrocken, "
     "verletzt ist sie nicht.", 0.3),
    ("[m1]Meine Tasche ist weg!", 0.4, "Margit"),
    ("[frage]Hat Hagen einen Raub begangen? [frage2]Wir prüfen Paragraf zweihundertneunundvierzig Schritt für Schritt, mit "
     "zwei Abwandlungen.", 0.6),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier sind der Fall und die Abwandlungen zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 249 I und Aufbau ---------------------------------------------------------------------------------------
    ("[p249]Paragraf zweihundertneunundvierzig, Absatz eins: [p249w]Wer mit Gewalt gegen eine Person oder unter Anwendung von "
     "Drohungen mit gegenwärtiger Gefahr für Leib oder Leben eine fremde bewegliche Sache einem anderen in der Absicht "
     "wegnimmt, die Sache sich oder einem Dritten rechtswidrig zuzueignen, wird mit Freiheitsstrafe nicht unter einem Jahr "
     "bestraft. [aufbau]Der Raub verbindet also eine Wegnahme wie beim Diebstahl mit einem qualifizierten Nötigungsmittel. "
     "[obj]Objektiv prüfst du die fremde bewegliche Sache, die Wegnahme, das Nötigungsmittel und den finalen Zusammenhang. "
     "[subj]Subjektiv Vorsatz und Absicht rechtswidriger Zueignung.", PS),
    # --- D Sache und Wegnahme ------------------------------------------------------------------------------------------------
    ("[sache]Erstens: Die Handtasche ist eine fremde bewegliche Sache, sie gehört Margit. [wegn]Zweitens: die Wegnahme, also "
     "der Bruch fremden und die Begründung neuen Gewahrsams. Die Einzelheiten kennst du aus unserer Folge zum Diebstahl. "
     "[wegn2]Hagen nimmt Margit die Tasche gegen ihren Willen ab und rennt damit davon. [wegok]Er hat neuen Gewahrsam, die "
     "Wegnahme liegt vor.", PS),
    # --- E Nötigungsmittel ---------------------------------------------------------------------------------------------------
    ("[nm]Drittens: das Nötigungsmittel. [nm2]Anders als bei der Nötigung, Paragraf zweihundertvierzig, genügt hier nicht jedes "
     "empfindliche Übel. [quali]Das Gesetz verlangt ein qualifiziertes Mittel: Gewalt gegen eine Person oder eine Drohung mit "
     "gegenwärtiger Gefahr für Leib oder Leben. [anzeige]Wer nur mit einer Anzeige droht, begeht keinen Raub. [gdef]Gewalt "
     "gegen eine Person liegt nach dem Bundesgerichtshof vor, wenn die Kraft des Täters wesentlicher Bestandteil der "
     "Wegnahme ist [gdef2]und vom Opfer als körperlicher Zwang empfunden wird. [g_ja]Hagen stößt Margit zu Boden. Das ist "
     "Gewalt gegen eine Person.", PS),
    # --- F Finaler Zusammenhang ----------------------------------------------------------------------------------------------
    ("[final]Viertens, und das ist der Kern: der finale Zusammenhang. [fdef]Die Gewalt muss das Mittel sein, um die Wegnahme "
     "zu ermöglichen. [fvor]Maßgeblich ist die Vorstellung des Täters: Er setzt die Gewalt ein, um wegzunehmen. [f_ja]Hagen "
     "stößt Margit, um an die Tasche zu kommen, und nimmt sie gleich danach. Die Finalität liegt vor.", PS),
    # --- G Abwandlung 1 ------------------------------------------------------------------------------------------------------
    ("[ab1]Abwandlung eins: Hagen stößt Margit nur aus Wut, weil sie ihn angerempelt hat. [ab1b]Erst als die Tasche am Boden "
     "liegt, beschließt er, sie mitzunehmen. [ab1c]Jetzt fehlt die Finalität: Die Gewalt war nicht das Mittel zur Wegnahme. "
     "[ab1d]Und es genügt nicht, dass der Täter die Wirkung einer früheren Gewalt bloß ausnutzt. [ab1e]Kein Raub, sondern "
     "Diebstahl. Den Stoß prüfst du gesondert.", PS),
    # --- H § 252 und § 255 ---------------------------------------------------------------------------------------------------
    ("[p252]Setzt der Täter die Gewalt erst nach der Wegnahme ein, um die Beute zu behalten, denk an räuberischen Diebstahl, "
     "Paragraf zweihundertzweiundfünfzig. [flucht]Will er dagegen nur fliehen, fehlt auch dafür die nötige Absicht. "
     "[p255]Gibt das Opfer die Sache unter Gewalt selbst heraus, kommt räuberische Erpressung in Betracht, Paragraf "
     "zweihundertfünfundfünfzig. [streit]Der Bundesgerichtshof grenzt nach dem äußeren Erscheinungsbild ab, Nehmen oder Geben; weite Teile der "
     "Lehre verlangen für die Erpressung eine Vermögensverfügung.", PS),
    # --- I Subjektiver Tatbestand --------------------------------------------------------------------------------------------
    ("[vors]Im subjektiven Tatbestand braucht Hagen Vorsatz für alle objektiven Merkmale. [zueig]Dazu kommt die "
     "Zueignungsabsicht: [zueig2]Die Aneignung muss er beabsichtigen, für die Enteignung genügt bedingter Vorsatz. "
     "[zueig3]Hagen will die Tasche samt Geld für sich behalten. [rwz]Einen Anspruch darauf hat er nicht, die erstrebte "
     "Zueignung ist rechtswidrig.", PS),
    # --- J Ergebnis, §§ 250, 251 ---------------------------------------------------------------------------------------------
    ("[rs]Rechtswidrigkeit und Schuld liegen vor. [erg]Hagen hat einen Raub begangen. [qual]Schwerer bestraft wird nach "
     "Paragraf zweihundertfünfzig, etwa wenn der Täter eine Waffe bei sich führt, und nach Paragraf zweihunderteinundfünfzig, "
     "wenn der Raub wenigstens leichtfertig den Tod eines Menschen verursacht.", PS),
    # --- K Abwandlung 2: Entreißen -------------------------------------------------------------------------------------------
    ("[ab2]Abwandlung zwei: Hagen kommt von hinten und reißt Margit die locker hängende Tasche im Vorbeilaufen von der "
     "Schulter, ehe sie reagieren kann. [ab2b]Die Kraft wirkt hier vor allem auf die Tasche. [ab2c]Prägen Überraschung, "
     "Schnelligkeit und Geschick das Bild und nicht körperlicher Zwang, bleibt es nach dem Bundesgerichtshof beim Diebstahl. "
     "[ab2d]Anders, wenn Margit die Tasche rechtzeitig bemerkt und festhält und Hagen sie nur mit erheblicher Kraft "
     "entreißen kann. [ab2e]Dann ist das Gewalt gegen eine Person, also Raub.", PS),
    # --- L Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Finalität sauber. [tipp2]Frag zuerst: Wann hat der Täter den Entschluss zur Wegnahme "
     "gefasst? [tipp3]Kam er erst nach der Gewalt, reicht das bloße Ausnutzen ihrer Wirkung nicht. [tipp4]Dann suchst du eine "
     "neue, zumindest konkludente Drohung. Sonst bleibt es beim Diebstahl.", PS),
    # --- M Klausurschema -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s_i]Römisch eins: Tatbestand. [s1a]Objektiv: fremde bewegliche Sache, [s1b]Wegnahme, "
     "[s1c]Gewalt gegen eine Person oder Drohung mit gegenwärtiger Gefahr für Leib oder Leben [s1d]und der finale "
     "Zusammenhang. [s1e]Subjektiv: Vorsatz [s1f]und Absicht rechtswidriger Zueignung. [s_ii]Römisch zwei: "
     "Rechtswidrigkeit. [s_iii]Römisch drei: Schuld. [s_iv]Danach, wenn nötig, die Qualifikationen der Paragrafen "
     "zweihundertfünfzig und zweihunderteinundfünfzig.", PS),
    # --- N Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Raub ist Wegnahme mit Gewalt gegen eine Person oder mit Drohung mit gegenwärtiger Gefahr für Leib oder "
     "Leben. [m_2]Die Gewalt muss das Mittel der Wegnahme sein. [m_3]Wer sich erst nach der Gewalt zur Wegnahme entschließt, "
     "begeht ohne neue Drohung nur einen Diebstahl.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
