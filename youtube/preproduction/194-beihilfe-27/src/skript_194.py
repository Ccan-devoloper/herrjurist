"""Folge 194 · Beihilfe § 27 StGB: Schema – wie viel Hilfe macht strafbar? (Mi · Examenswissen · StGB AT, Format Schema).
Fall nach dem Plan-Hook („Ein Freund leiht einem anderen sein Auto, obwohl er weiß, dass dieser damit zu einem Einbruch
fährt.“): Falko (um 35) erzählt seiner Freundin Hedda (um 35) am Freitagabend offen, dass er am Samstag in ein bewohntes
Einfamilienhaus am Stadtrand einbrechen will; welches Haus, sagt er nicht. Hedda findet das falsch, gibt ihm aber den
Autoschlüssel; von der Beute will sie nichts. Falko fährt am Samstag um 22 Uhr mit dem Auto hin, bricht ein, nimmt Schmuck
für 3.000 € mit und bringt ihn im Kofferraum weg. Einbruch nur als Haus-/Schloss-Icon, keine Anleitung, kein Werkzeug.
Aufbau (Schema): Fall → Sachverhalt → Wortlaut § 27 Abs. 1 und Abs. 2 → Schema I. 1. a) Haupttat (limitierte Akzessorietät,
§ 29), b) Hilfeleisten (physisch/psychisch; BGH-Förderungsformel vs. h. L. Kausalität), 2. doppelter Gehilfenvorsatz,
II., III., Strafe § 27 Abs. 2 → Lösung (§§ 242, 244 Abs. 1 Nr. 3, Abs. 4; Mittäterschaft ein Satz, Verweis Folge 104) →
Sonderfälle (sukzessive Beihilfe, neutrale Handlungen/Taxi, Unterlassen) → Klausurtipp (Lexi) → Merksatz (Lexi).
Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Auftragsliste und Volltextsuche 04.10.2026): Falko, Hedda.
Nie im Genitiv mit -s. Stimmen (Pool stephan, hilde, christian, lucy): Falko stephan (Mann, mittel), Hedda lucy (Frau,
jung); hilde und christian nicht verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gesetzesnamen im Sprechtext als Wörter (keine Abkürzungen wie StGB/BGH)."""

P, PS = 0.3, 0.5

STIMMEN = {"Falko": "stephan", "Hedda": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Freitagabend vor der Haustür von Hedda ------------------------------------------------------------------
    ("[fall]Freitagabend. Falko steht bei seiner Freundin Hedda vor der Tür. [plan]Er erzählt ihr offen, was er vorhat: "
     "Am Samstag will er in ein Einfamilienhaus am Stadtrand einbrechen. [familie]Dort wohnt eine Familie, die an dem Abend "
     "nicht zu Hause ist. [welches]Welches Haus genau, sagt er nicht.", P),
    ("[fa1]Leihst du mir dein Auto? Mit dem Bus komme ich da nicht hin, und die Beute muss ja auch weg.", P, "Falko"),
    ("[he1]Ich finde das falsch. Aber gut, hier ist der Schlüssel. Bring ihn mir Sonntag zurück.", P, "Hedda"),
    ("[nichts]Von der Beute will Hedda nichts.", P),
    # --- A2 Fall: Samstag, das Haus am Stadtrand --------------------------------------------------------------------------
    ("[sa]Am Samstag um zweiundzwanzig Uhr fährt Falko mit dem Auto von Hedda zu dem Haus. [einbruch]Er bricht ein "
     "[beute]und nimmt Schmuck für dreitausend Euro mit. [koffer]Die Beute bringt er im Kofferraum weg. [frage]Falko ist "
     "Täter. Aber was ist mit Hedda? [frage2]Sie hat nur ein Auto verliehen. Wie viel Hilfe macht strafbar?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 27 ---------------------------------------------------------------------------------------------------
    ("[p27]Die Antwort steht in Paragraf siebenundzwanzig. [p27w]Absatz eins: Als Gehilfe wird bestraft, wer vorsätzlich "
     "einem anderen zu dessen vorsätzlich begangener rechtswidriger Tat Hilfe geleistet hat. [p27a2]Absatz zwei: Die "
     "Strafe für den Gehilfen richtet sich nach der Strafdrohung für den Täter. [p27s2]Sie ist nach Paragraf neunundvierzig "
     "Absatz eins zu mildern.", PS),
    # --- D Schema: I. 1. a) Haupttat ----------------------------------------------------------------------------------------
    ("[sch]Daraus folgt das Prüfschema. [s_i]Römisch eins: Tatbestand. [s1]Erstens, objektiv. [s1a]a: eine vorsätzliche, "
     "rechtswidrige Haupttat eines anderen. [akz]Schuldhaft muss der Haupttäter nicht handeln. [p29]Nach Paragraf "
     "neunundzwanzig wird jeder Beteiligte ohne Rücksicht auf die Schuld des anderen nach seiner Schuld bestraft. [lim]Man "
     "nennt das limitierte Akzessorietät.", PS),
    # --- E Schema: I. 1. b) Hilfeleisten, Meinungsstand -------------------------------------------------------------------
    ("[s1b]b: das Hilfeleisten. [phys]Hilfe kann physisch sein, etwa durch ein Tatmittel wie ein Auto, [psych]oder "
     "psychisch, durch Rat oder indem man den Täter in seinem Entschluss bestärkt. [zeit]Sie ist schon in der "
     "Vorbereitung möglich.", P),
    ("[streit]Umstritten ist, wie stark die Hilfe wirken muss. [bgh1]Der Bundesgerichtshof lässt genügen, dass sie die Tat "
     "fördert oder erleichtert. [bgh2]Ursächlich für den Erfolg muss sie nicht sein. [lehre]Die herrschende Lehre verlangt "
     "dagegen, dass sich die Hilfe im Erfolg auswirkt: [lehre2]Sie muss die Tat in ihrer konkreten Gestalt ermöglicht, "
     "erleichtert oder abgesichert haben. [arg]Sonst würde aus einer bloß versuchten Beihilfe, die straflos ist, eine "
     "vollendete. [meist]Meist kommen beide Ansichten aber zum selben Ergebnis.", PS),
    # --- F Schema: I. 2. doppelter Gehilfenvorsatz ---------------------------------------------------------------------------
    ("[s2]Zweitens, subjektiv: der doppelte Gehilfenvorsatz. [v1]Der Gehilfe braucht Vorsatz bezüglich der Haupttat, "
     "[v1b]und zwar in ihren wesentlichen Merkmalen, also Unrechtsgehalt und Angriffsrichtung. [v1c]Einzelheiten wie Ort "
     "und Zeit muss er nicht kennen. [v2]Und er braucht Vorsatz bezüglich seiner eigenen Hilfe: Er weiß, dass sie die Tat "
     "fördern kann.", PS),
    # --- G Schema: II., III., Strafe ----------------------------------------------------------------------------------------
    ("[s_ii]Römisch zwei: Rechtswidrigkeit. [s_iii]Römisch drei: Schuld. [strafe]Bei der Strafe gilt Paragraf "
     "siebenundzwanzig Absatz zwei: Die Milderung ist zwingend.", PS),
    # --- H Lösung -------------------------------------------------------------------------------------------------------------
    ("[loes]Jetzt der Fall. [h1]Zuerst die Haupttat: Falko bricht in ein bewohntes Haus ein und stiehlt dort. [h2]Das ist "
     "ein schwerer Wohnungseinbruchdiebstahl nach Paragraf zweihundertvierundvierzig Absatz eins Nummer drei und Absatz "
     "vier, [h2b]denn das Haus ist eine dauerhaft genutzte Privatwohnung. [h3]Falko handelt vorsätzlich und rechtswidrig. "
     "[mitt]Mittäterin ist Hedda nicht: Sie will nichts von der Beute und hat keinen Einfluss darauf, ob und wie die Tat "
     "abläuft. Mehr dazu in unserer Folge zur Mittäterschaft.", PS),
    ("[hl]Hilfeleisten: Mit dem Auto fährt Falko zum Haus und schafft die Beute weg. [hl2]Das erleichtert die Tat, nach dem "
     "Bundesgerichtshof genügt das. [hl3]Und weil die Tat genau so ablief, hat sich die Hilfe auch im Erfolg ausgewirkt. "
     "[hl4]Beide Ansichten kommen zum selben Ergebnis, ein Streitentscheid ist entbehrlich.", P),
    ("[vs]Vorsatz: Hedda weiß, dass Falko in ein bewohntes Haus einbrechen und dort stehlen will. [vs2]Welches Haus, weiß "
     "sie nicht. Das ist nur eine Einzelheit. [vs3]Sie weiß auch, dass ihr Auto ihm dabei hilft. [vs4]Dass sie die Tat "
     "falsch findet, ändert daran nichts. [rws]Rechtfertigungs- oder Entschuldigungsgründe gibt es nicht.", P),
    ("[erg]Ergebnis: Hedda ist strafbar wegen Beihilfe zum schweren Wohnungseinbruchdiebstahl. [rahmen]Ihr Strafrahmen wird "
     "gemildert: statt ein bis zehn Jahren drei Monate bis sieben Jahre und sechs Monate.", PS),
    # --- I Sonderfälle --------------------------------------------------------------------------------------------------------
    ("[sf]Drei Sonderfälle in Kürze. [sukz]Erstens, die sukzessive Beihilfe: Nach dem Bundesgerichtshof ist Hilfe auch nach "
     "der Vollendung noch bis zur Beendigung möglich, etwa beim Abtransport der Beute. [sukz2]Teile der Lehre ziehen die "
     "Grenze schon bei der Vollendung.", P),
    ("[taxi]Zweitens, neutrale Handlungen wie eine Taxifahrt. [taxi2]Weiß der Fahrer sicher, dass sein Fahrgast am Ziel "
     "einbrechen will, leistet er Beihilfe. [taxi3]Hält er das nur für möglich, regelmäßig nicht, [taxi4]es sei denn, das "
     "Risiko ist so hoch, dass er sich die Förderung eines erkennbar tatgeneigten Täters angelegen sein lässt. "
     "[unterl]Drittens: Beihilfe ist auch durch Unterlassen möglich, aber nur mit einer Garantenstellung nach Paragraf "
     "dreizehn.", PS),
    # --- J Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe immer erst den Täter, dann den Teilnehmer. [tipp2]Das heißt auch: Frag zuerst, ob jemand "
     "selbst Täter ist. Erst wenn nicht, kommt die Beihilfe. [tipp3]Und nenne im Obersatz die Haupttat genau: Beihilfe zum "
     "schweren Wohnungseinbruchdiebstahl, nicht bloß zum Diebstahl.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Hilfe leistet, wer eine fremde vorsätzliche, rechtswidrige Tat fördert. [mk2]Strafbar wird das mit "
     "doppeltem Vorsatz: [mk3]Der Gehilfe kennt die Haupttat in ihren wesentlichen Merkmalen und weiß, dass er hilft.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
