"""Folge 094 · Sirius-Fall: Zur Selbsttötung überredet – mittelbare Täterschaft? (Mo · Der Fall · StGB AT, Klassiker-Fall).
Fiktiver Fall nach dem Vorbild von BGH, Urt. v. 5.7.1983 – 1 StR 168/83, BGHSt 32, 38 (Sirius-Fall); der echte Fall wird nur
kurz eingeordnet (Belege und Einschränkungen in ../RECHTSSTAND.md). Höchste Zurückhaltung (Thema Suizid): keine Methode im
Bild oder im Sprechtext, keine Verletzung, keine dramatisierende Musik; Wilma bleibt unverletzt; sachlicher Ton, keine
Verspottung der Getäuschten; am Ende ein ruhiger Satz mit Hilfsangebot (Telefonseelsorge, Nummern auf der Tafel).
Lösung: Ausgangspunkt Straflosigkeit der Selbsttötung und mangels Haupttat auch der Teilnahme (BGHSt 64, 121 Rn. 17), § 217 a. F.
nichtig (BVerfG 2 BvR 2347/15 Rn. 337) → § 25 Abs. 1 (Wortlaut), Opfer als Werkzeug gegen sich selbst, unfrei (BGHSt 64, 121
Rn. 20 f. mit BGHSt 32, 38, 41 f., 43) → Maßstab: Exkulpations- und Einwilligungslösung (BGHSt 64, 121 Rn. 25), BGH-Kriterien
(Rn. 21) → Täuschung: Art und Tragweite des Irrtums (BGHSt 32, 38, Gründe 1.) → Subsumtion → Versuch → Ergebnis: versuchter
Totschlag in mittelbarer Täterschaft (Mordmerkmal offen) → Klausurtipp → Schema → Merksatz → Hilfsangebot.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Wilma, Hartwig, Benedikt. Nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.9

STIMMEN = {"Hartwig": "helmut", "Wilma": "ela_froh", "Benedikt": "niklas"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall: der Gesprächsabend --------------------------------------------------------------------------------------------
    ("[fall]Wilma, Mitte dreißig, besucht seit Jahren die Gesprächsabende von Hartwig. [lehrer]Hartwig nennt sich "
     "spiritueller Lehrer, und Wilma vertraut ihm blind. [stern]Eines Abends erzählt er ihr, er stamme von einem fernen Stern "
     "und solle auserwählte Menschen weiterführen.", 0.3),
    ("[h1]Dein Körper hält dich zurück. Lässt du ihn hinter dir, wachst du sofort in einem höheren Körper auf und lebst "
     "weiter.", 0.3, "Hartwig"),
    ("[w1]Sterben will ich nicht. Aber weiterleben, das schon.", 0.3, "Wilma"),
    ("[weiss]Hartwig weiß, dass das nicht stimmt. Ginge Wilma diesen Weg, wäre sie tot, und genau das will er. [plan]Er "
     "legt alles fest, auch den Abend.", 0.4),
    # --- A2 Fall: Wilmas Wohnung -------------------------------------------------------------------------------------------------
    ("[abend]Am verabredeten Abend beginnt Wilma, den Plan umzusetzen. [bruder]Da kommt unerwartet ihr Bruder Benedikt "
     "vorbei.", 0.3),
    ("[b1]Wilma, hör auf! Ich hole Hilfe.", 0.3, "Benedikt"),
    ("[lebt]Wilma bleibt unverletzt. [frage]Die Teilnahme an einer Selbsttötung ist grundsätzlich straflos. Ist Hartwig also straflos, "
     "[frage2]oder hat er versucht, Wilma durch sie selbst zu töten?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Der echte Fall --------------------------------------------------------------------------------------------------------
    ("[echt]Das Vorbild ist der Sirius-Fall, Bundesgerichtshof, Urteil vom fünften Juli neunzehnhundertdreiundachtzig. "
     "[echt2]Dort hatte ein Mann einer Frau eingeredet, er stamme vom Stern Sirius und sie werde in einem neuen Körper "
     "weiterleben. [vers]Zuvor schloss sie auf sein Betreiben eine Lebensversicherung zu seinen Gunsten ab. [echt3]Auch sie überlebte. "
     "Der BGH bestätigte die Verurteilung wegen versuchten Mordes aus Habgier. [abgew]Unser Fall ist abgewandelt.", PS),
    # --- D Ausgangspunkt: Straflosigkeit -----------------------------------------------------------------------------------------
    ("[aus]Zuerst der Ausgangspunkt. Eine eigenverantwortliche Selbsttötung erfüllt keinen Tatbestand eines Tötungsdelikts. "
     "[akz]Anstiftung und Beihilfe brauchen aber eine rechtswidrige Haupttat. Fehlt sie, bleibt auch die Teilnahme "
     "straflos. [p217]Die frühere Sonderregel gegen die geschäftsmäßige Förderung, Paragraf zweihundertsiebzehn, hat das "
     "Bundesverfassungsgericht zweitausendzwanzig für nichtig erklärt. [f058]Und aus Folge achtundfünfzig kennst du: Wer eine "
     "eigenverantwortliche Selbstgefährdung nur ermöglicht, tötet nicht.", PS),
    # --- E § 25 Abs. 1: Werkzeug gegen sich selbst --------------------------------------------------------------------------------
    ("[hand]Hartwig hat die Tat nicht selbst ausgeführt. [p25]Paragraf fünfundzwanzig Absatz eins: Als Täter wird bestraft, wer "
     "die Straftat selbst oder durch einen anderen begeht. [werkz]Der andere kann auch das Opfer selbst sein, als Werkzeug "
     "gegen sich selbst. [unfrei]Dafür muss es unfrei handeln: Sein Entschluss beruht auf einem Wissens- oder "
     "Verantwortlichkeitsdefizit.", PS),
    # --- F Maßstab: der Streit ---------------------------------------------------------------------------------------------------
    ("[streit]Wann ist der Entschluss nicht frei? [exk]Die Exkulpationslösung fragt, ob das Opfer in einem Zustand handelt, "
     "der entsprechend den Paragrafen neunzehn, zwanzig und fünfunddreißig die Verantwortung ausschließen würde. [einw]Die "
     "Einwilligungslösung stellt höhere Anforderungen: Der Entschluss muss so frei und ernstlich sein wie eine wirksame "
     "Einwilligung. [bgh]Der BGH verlangt Einsichts- und Urteilsfähigkeit, einen mangelfreien Willen und einen festen "
     "Entschluss. [mangel]Mangelhaft ist er etwa bei Zwang, Drohung oder Täuschung.", PS),
    # --- G Täuschung über den Tod ------------------------------------------------------------------------------------------------
    ("[art]Bei einer Täuschung kommt es nach dem BGH auf Art und Tragweite des Irrtums an. [verschl]Verschleiert sie dem "
     "Opfer, dass es eine Ursache für den eigenen Tod setzt, ist der Täuschende Täter kraft überlegenen Wissens. [selbst]Er "
     "macht den Irrenden zum Werkzeug gegen sich selbst. [f091]Wie im Katzenkönig-Fall aus Folge einundneunzig entscheidet "
     "das überlegene Wissen. Nur ist das Werkzeug hier das Opfer selbst.", PS),
    # --- H Subsumtion ------------------------------------------------------------------------------------------------------------
    ("[subs]So liegt es hier. Wilma will nicht sterben, das lehnt sie ab. [glaubt]Sie glaubt, sie lebe sofort weiter. Sie "
     "irrt also über den Tod selbst. [beide]Über ihren Tod entscheidet sie gar nicht. Beide Ansichten kommen hier zum selben "
     "Ergebnis. [herr]Hartwig hat den Irrtum erzeugt, kennt die wahre Gefahr und steuert das Geschehen. Er hat die "
     "Tatherrschaft. [unglaub]Dass seine Geschichte unglaubhaft klingt, entlastet ihn nicht. So sah es auch der BGH.", PS),
    # --- I Versuch und Ergebnis --------------------------------------------------------------------------------------------------
    ("[versuch]Wilma lebt, in Betracht kommt also ein Versuch. [entschl]Hartwig wollte ihren Tod und wusste, dass er das "
     "Geschehen steuert. [ansetz]Unmittelbar angesetzt ist jedenfalls, als Wilma beginnt, den Plan umzusetzen. Ob der "
     "Versuch des Hintermanns schon früher beginnt, ist umstritten. [rt]Zurückgetreten ist Hartwig nicht, Benedikt hat sie "
     "aufgehalten.", PS),
    ("[erg]Ergebnis: Hartwig ist strafbar wegen versuchten Totschlags in mittelbarer Täterschaft, Paragrafen "
     "zweihundertzwölf, zweiundzwanzig, dreiundzwanzig und fünfundzwanzig Absatz eins, zweite Alternative. [mord]Für einen "
     "Mord bräuchte es ein Mordmerkmal, im echten Fall die Habgier. Dazu sagt unser Fall nichts.", PS),
    # --- J Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe beim Hintermann zuerst das Tötungsdelikt in mittelbarer Täterschaft, nicht die Teilnahme. "
     "[tipp2]Den Streit um den Maßstab entscheidest du nur, wenn die Ansichten auseinandergehen. [tipp3]Bei einer Täuschung "
     "über den Tod selbst tun sie das nicht.", PS),
    # --- K Klausurschema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema zum versuchten Totschlag in mittelbarer Täterschaft. [s0]Vorprüfung: nicht vollendet, der "
     "Versuch ist strafbar. [s1]Erstens Tatentschluss: Vorsatz zur Tötung und zur Tatherrschaft über das Werkzeug. [s1a]Hier "
     "prüfst du, ob das Opfer unfrei handelt, [s1b]mit dem Streit um den Maßstab und der Täuschung über den Tod. "
     "[s2]Zweitens unmittelbares Ansetzen, [s3]drittens Rechtswidrigkeit, [s4]viertens Schuld, [s5]dann der Rücktritt.", PS),
    # --- L Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Teilnahme an einer freien Selbsttötung ist straflos. [m2]Wer aber das Opfer über den Tod selbst "
     "täuscht, tötet durch das Opfer, als mittelbarer Täter.", 1.0),
    # --- M Hilfsangebot ----------------------------------------------------------------------------------------------------------
    ("[hilfe]Wenn dich das Thema selbst betrifft: Die Telefonseelsorge ist rund um die Uhr und kostenlos für dich da. "
     "[nummern]Die Nummern siehst du hier.", 4.5),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
