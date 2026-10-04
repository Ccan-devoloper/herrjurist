"""Folge 141 · Beweislast ZPO: Wer verliert beim non liquet? (Fr · 2. Examen · ZPO, Format Schema).
Beispielfall nach dem Plan-Hook („Zwei Zeugen widersprechen sich exakt, und niemand weiß mehr, ob das Darlehen je ausgezahlt
wurde.“): Herr Wiedemann und Frau Krause vereinbaren ein zinsloses Darlehen über 5.000 €, rückzahlbar bis 31.3.2026
(unstreitig). Herr Wiedemann will ihr das Geld an einem Abend in ihrer Küche bar in einem Umschlag gegeben haben, ohne
Quittung; Frau Krause bestreitet die Auszahlung. Klage auf Rückzahlung (§ 488 Abs. 1 S. 2 BGB) zum Amtsgericht. Zeuge Herr
Reichert (Bekannter des Klägers): Übergabe; Zeugin Frau Fischer (Freundin der Beklagten): keine Übergabe; beide gleich
glaubhaft, keine weiteren Beweise.
Kern als Schema: 1. Beweisstation nur bei streitiger erheblicher Tatsache (Verweis 018); 2. freie Beweiswürdigung § 286 Abs. 1
ZPO (Wortlautkarte), BGH VI ZR 76/23 Rn. 15; 3. non liquet → Beweislast (§ 300 Abs. 1 ZPO); 4. Normentheorie (BGH IV ZR 68/22
Rn. 68; Verweis 103), Sonderregeln § 280 Abs. 1 S. 2, § 477, § 1006 BGB, subjektive Beweislast (BGH V ZR 28/22 Rn. 28);
5. Fall: Kläger beweisbelastet → Abweisung; Gegenvariante Rückzahlung (§ 362 BGB, BGH XI ZR 380/20 Rn. 31) → Beklagte
beweisbelastet; 6. Urteil: „Der Kläger ist beweisfällig geblieben.“ (übliche Formulierung, vgl. BGH VII ZR 274/17 Rn. 9),
§ 286 Abs. 1 S. 2 ZPO. Klausurtipp, Schema mit Waage, Merksatz. Belege: ../RECHTSSTAND.md.
Figuren: Herr Wiedemann (helmut), Herr Reichert (niklas), Frau Fischer (julia); Frau Krause und die Richterin sprechen nicht;
Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Wiedemann": "helmut", "Reichert": "niklas", "Fischer": "julia"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Hook: im Sitzungssaal ------------------------------------------------------------------------------------------
    ("[fall]Zwei Zeugen, eine Frage und zwei Antworten, die sich exakt widersprechen. [zeuge1]Zuerst Herr Reichert.", 0.25),
    ("[re1]Ich war dabei. Herr Wiedemann hat ihr fünftausend Euro bar gegeben.", 0.3, "Reichert"),
    ("[zeugin]Dann Frau Fischer.", 0.2),
    ("[fi1]Ich saß am selben Tisch. Da ist kein Geld übergeben worden.", 0.3, "Fischer"),
    ("[niemand]Und niemand weiß mehr, ob das Darlehen je ausgezahlt wurde.", 0.4),
    # --- A2 Fall: der Abend in der Küche --------------------------------------------------------------------------------------
    ("[streit]Worum geht es? [darl]Herr Wiedemann und Frau Krause vereinbaren ein Darlehen über fünftausend Euro, "
     "rückzahlbar bis Ende März. [abend]An einem Abend in ihrer Küche will er ihr das Geld bar gegeben haben. "
     "[quitt]Eine Quittung gibt es nicht.", 0.25),
    ("[wi1]Ich habe ihr das Geld gegeben, in einem Umschlag!", 0.3, "Wiedemann"),
    # --- A3 Fall: Klage und Frage ---------------------------------------------------------------------------------------------
    ("[best]Frau Krause bestreitet das: Sie habe nie Geld bekommen. [klage]Herr Wiedemann klagt vor dem Amtsgericht auf "
     "Rückzahlung. [hoert]Das Gericht hört beide Zeugen. Beide wirken gleich glaubwürdig. [frage]Wer verliert, wenn sich "
     "nicht klären lässt, was wirklich passiert ist?", 0.5),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.8),
    # --- C Aufbau -----------------------------------------------------------------------------------------------------------
    ("[plan]Wir prüfen in sechs Schritten: [s1]die streitige Tatsache, [s2]die freie Beweiswürdigung, [s3]das non liquet, "
     "[s4]die Beweislast, [s5]den Fall [s6]und die Formulierung im Urteil.", PS),
    # --- D 1. Streitige Tatsache ---------------------------------------------------------------------------------------------
    ("[st1]Erstens: In die Beweisstation kommst du nur, wenn eine erhebliche Tatsache streitig ist. Mehr dazu im Video zur "
     "Relationstechnik. [st2]Herr Wiedemann verlangt Rückzahlung nach Paragraf vierhundertachtundachtzig Absatz eins Satz zwei "
     "BGB. [st3]Danach muss der Darlehensnehmer das zur Verfügung gestellte Darlehen zurückzahlen. [st4]Vereinbarung und "
     "Fälligkeit sind unstreitig. [st5]Streitig ist allein die Auszahlung. Und ohne Auszahlung gibt es nichts zurückzuzahlen.", PS),
    # --- E 2. Freie Beweiswürdigung, § 286 Abs. 1 ZPO -------------------------------------------------------------------------
    ("[bw]Zweitens: die freie Beweiswürdigung. [w286]Paragraf zweihundertsechsundachtzig Absatz eins ZPO: Das Gericht hat "
     "unter Berücksichtigung des gesamten Inhalts der Verhandlungen und des Ergebnisses einer etwaigen Beweisaufnahme nach "
     "freier Überzeugung zu entscheiden, ob eine tatsächliche Behauptung für wahr oder für nicht wahr zu erachten sei.", P),
    ("[voll]Verlangt ist die volle Überzeugung des Gerichts. [bgh]Absolute Gewissheit braucht es nach dem Bundesgerichtshof "
     "aber nicht. Es genügt ein für das praktische Leben brauchbarer Grad von Gewissheit, der verbleibenden Zweifeln "
     "Schweigen gebietet, ohne sie völlig auszuschließen. [agg]Hier steht Aussage gegen Aussage. [gleich]Nichts spricht "
     "mehr für die eine als für die andere Version.", PS),
    # --- F 3. Non liquet ------------------------------------------------------------------------------------------------------
    ("[nl]Drittens: das non liquet, lateinisch für: Es ist nicht klar. [nl2]Das Gericht ist weder von der Auszahlung "
     "überzeugt noch davon, dass kein Geld geflossen ist. [nl3]Ein Urteil muss es trotzdem sprechen. [nl4]Jetzt, und erst "
     "jetzt, entscheidet die Beweislast. Die Unklarheit geht zulasten der Partei, die sie trägt.", PS),
    # --- G 4. Beweislast: Normentheorie ---------------------------------------------------------------------------------------
    ("[nt]Viertens: Wer trägt die Beweislast? Die Antwort gibt die Normentheorie, die auf Leo Rosenberg zurückgeht. "
     "[nt2]Nach dem Bundesgerichtshof muss jede Partei die tatsächlichen Voraussetzungen der ihr günstigen Normen darlegen "
     "und beweisen. [nt3]Der Kläger beweist also die anspruchsbegründenden Tatsachen. [nt4]Der Beklagte beweist, was den "
     "Anspruch hindert, vernichtet oder hemmt. Mehr zu dieser Einteilung im Video zu Einwendungen und Einreden.", P),
    # --- H Sonderregeln, subjektive Beweislast --------------------------------------------------------------------------------
    ("[sonder]Manchmal regelt das Gesetz die Beweislast selbst. [s280]Nach Paragraf zweihundertachtzig Absatz eins Satz "
     "zwei muss sich der Schuldner vom Vertretenmüssen entlasten. [s477]Beim Verbrauchsgüterkauf hilft dem Käufer die Vermutung aus Paragraf "
     "vierhundertsiebenundsiebzig. [s1006]Und nach Paragraf tausendsechs wird vermutet, dass der Besitzer einer beweglichen "
     "Sache ihr Eigentümer ist. [subj]Davon zu trennen ist die subjektive Beweislast, die Beweisführungslast. Sie fragt, wer "
     "Beweis antreten muss, etwa durch einen Zeugen. [subj2]Herr Wiedemann hat das getan und Herrn Reichert benannt.", PS),
    # --- I 5. Der Fall und die Gegenvariante ----------------------------------------------------------------------------------
    ("[fall5]Fünftens: der Fall. [f1]Die Auszahlung ist Voraussetzung des Rückzahlungsanspruchs, also anspruchsbegründend. "
     "[f2]Sie nützt Herrn Wiedemann, deshalb trägt er die Beweislast. [f3]Das non liquet geht zu seinen Lasten. [f4]Die "
     "Klage wird abgewiesen.", P),
    ("[gv]Und die Gegenvariante? [gv1]Frau Krause gibt zu, das Geld bekommen zu haben, sagt aber, sie habe es längst "
     "zurückgezahlt. [gv2]Dann ist die Auszahlung unstreitig. Die Rückzahlung wäre Erfüllung nach Paragraf "
     "dreihundertzweiundsechzig BGB, eine rechtsvernichtende Einwendung. [gv3]Die Beweislast trägt jetzt Frau Krause. "
     "[gv4]Bleibt es beim non liquet, wird sie verurteilt.", PS),
    # --- J 6. Formulierung im Urteil ------------------------------------------------------------------------------------------
    ("[urt]Sechstens: die Formulierung im Urteil. [u1]Üblich ist der knappe Satz: Der Kläger ist beweisfällig geblieben. "
     "[u2]Davor gehört die Beweiswürdigung, denn nach Absatz eins Satz zwei sind die Gründe anzugeben, die für die "
     "richterliche Überzeugung leitend gewesen sind. [u3]Du erklärst also, warum keine der beiden Aussagen überzeugt, "
     "und erst dann, wer die Beweislast trägt.", PS),
    # --- K Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Flüchte nicht zu früh in die Beweislast. [tipp2]Erst würdigst du jede Aussage. Nur wenn danach "
     "wirklich Zweifel bleiben, entscheidet die Beweislast. [tipp3]Und prüfe vorher, ob das Gesetz eine Sonderregel oder "
     "eine Vermutung enthält.", PS),
    # --- L Klausurschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Beweisstation: [k1]Römisch eins: eine streitige, erhebliche Tatsache. [k2]Römisch zwei: die "
     "Beweiswürdigung nach Paragraf zweihundertsechsundachtzig, Maßstab ist die volle Überzeugung. [k3]Römisch drei: Bleibt "
     "ein non liquet? [k4]Römisch vier: die Beweislast, zuerst gesetzliche Sonderregeln, sonst die Normentheorie. "
     "[k5]Römisch fünf: das Ergebnis zulasten der beweisbelasteten Partei.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Beim non liquet verliert, wer die Beweislast trägt. [mk2]Und die trägt jede Partei für die "
     "Voraussetzungen der Norm, die ihr günstig ist.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
