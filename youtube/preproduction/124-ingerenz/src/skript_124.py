"""Folge 124 · Ingerenz: Wer die Gefahr schafft, muss sie beseitigen – § 13 StGB (Mo · Der Fall · StGB AT, Format Schema).
Beispielfall nach dem Plan-Hook („Ein Autofahrer verletzt fahrlässig einen Fußgänger und fährt weiter, obwohl der Verletzte
ohne Hilfe zu verbluten droht“): Eckhard fährt innerorts mit siebzig statt fünfzig (§ 3 Abs. 3 Nr. 1 StVO), bremst zu spät
und erfasst einen Fußgänger, der schwer verletzt am Straßenrand liegt und ohne schnelle Hilfe zu sterben droht. Eckhard hält
an, steigt aus, sieht ihn liegen, steigt wieder ein und fährt weiter: Er will nicht als Unfallverursacher entdeckt werden und
nimmt den Tod in Kauf. Eine Radfahrerin findet den Mann und ruft den Rettungsdienst; er überlebt (daher nur Versuch).
Prüfung: A. § 229 (ein Satz) → B. versuchter Totschlag durch Unterlassen, §§ 212, 22, 23 Abs. 1, 13: Wortlautkarte § 13 Abs. 1
(Auszug), Garantenstellung aus Ingerenz (BGH 4 StR 416/20 Rn. 22; 2 StR 563/18 Rn. 19, 21 f.), Abgrenzung verkehrsgerechtes
Verhalten (ein Satz, Folgerung aus denselben Rn.), bedingter Vorsatz (1 StR 474/19 Rn. 14, 16, 20), unmittelbares Ansetzen
(ein Satz; Fallgruppe nach 4 StR 361/17 Rn. 6, 12, 15) → C. Mordmerkmal Verdeckungsabsicht: Wortlautkarte § 211 Abs. 2
(Auszug), andere Straftat und Entdeckung als Unfallverursacher (4 StR 297/02 Rn. 6, 12; 4 StR 361/17 Rn. 14, 16), bedingter
Tötungsvorsatz vereinbar (4 StR 361/17 Rn. 11; 1 StR 675/99 Rn. 11), Streit „Verdecken durch Unterlassen“ mit Entscheid
(4 StR 297/02 Rn. 6; 1 StR 675/99 Rn. 21; Kaspar/Broichmann ZJS 2013, 346, 351 f.), § 13 Abs. 2 → D. § 142 Abs. 1
(Wortlautkarte Auszug) → § 323c tritt zurück (vgl. 3 StR 633/14 Rn. 21) → Konkurrenzen (zwei Sätze) → Ergebnis →
Klausurtipp → Schema → Merksatz. Versuch nur verwiesen (Folge 097), Garantenstellung allgemein verwiesen (Folge 115).
Belege: ../RECHTSSTAND.md. Name mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Eckhard (nie im Genitiv).
Fußgänger und Radfahrerin bleiben ohne Namen (Funktionsrollen).
Stimmen: Eckhard christian; Radfahrerin lucy; der Fußgänger spricht nicht. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Eckhard": "christian", "Radfahrerin": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die Dorfstraße -------------------------------------------------------------------------------------------
    ("[fall]Ein Sonntagnachmittag in einem Dorf. [schnell]Eckhard fährt mit siebzig statt der erlaubten fünfzig. "
     "[fuss]Ein älterer Mann, den Eckhard nicht kennt, überquert die Straße. [brems]Eckhard bremst zu spät und "
     "erfasst ihn. [halt]Mit fünfzig hätte er rechtzeitig halten können.", 0.3),
    ("[liegt]Der Mann liegt schwer verletzt am Straßenrand. [gefahr]Ohne schnelle Hilfe droht er zu sterben. "
     "[aus]Eckhard hält an, steigt aus und sieht ihn liegen.", 0.3),
    ("[e1]Wenn ich jetzt Hilfe rufe, bin ich dran.", 0.3, "Eckhard"),
    ("[weg]Eckhard steigt wieder ein und fährt weiter. [vors]Er will nicht als Unfallverursacher entdeckt werden. "
     "[tod]Dass der Mann ohne Hilfe stirbt, hält er für möglich und nimmt es in Kauf.", 0.3),
    # --- A2 Fall: die Radfahrerin -------------------------------------------------------------------------------------------
    ("[rad]Zehn Minuten später kommt eine Radfahrerin vorbei.", 0.3),
    ("[r1]Hier liegt ein verletzter Mann. Bitte kommen Sie schnell!", 0.3, "Radfahrerin"),
    ("[klinik]Der Rettungsdienst bringt den Mann ins Krankenhaus. Er überlebt.", 0.4),
    ("[frage]Eckhard hat den Mann nur fahrlässig angefahren. Musste er ihm trotzdem helfen? "
     "[frage2]Und kommt sogar ein Mord durch Unterlassen in Betracht?", 0.5),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C A. Die Fahrt: § 229 ----------------------------------------------------------------------------------------------
    ("[fahrt]Zuerst die Fahrt: Eckhard ist zu schnell gefahren und hat dadurch den Mann verletzt. Das ist eine fahrlässige "
     "Körperverletzung, Paragraf zweihundertneunundzwanzig. [kern]Spannender ist das Weiterfahren. Hier wirft man "
     "Eckhard kein Tun vor, sondern ein Unterlassen: Er hat keine Hilfe gerufen. [delikt]Wir prüfen den versuchten Totschlag "
     "durch Unterlassen. [versuch]Versuch, weil der Mann überlebt. Wie man den Versuch prüft, zeigt das Video zum "
     "Versuchsschema.", PS),
    # --- D Wortlautkarte § 13 Abs. 1, Ingerenz ------------------------------------------------------------------------------
    ("[p13]Paragraf dreizehn Absatz eins: Wer es unterlässt, einen Erfolg abzuwenden, der zum Tatbestand eines "
     "Strafgesetzes gehört, ist nach diesem Gesetz nur dann strafbar, [einst]wenn er rechtlich dafür einzustehen hat, dass "
     "der Erfolg nicht eintritt. [garant]Eckhard muss also Garant sein. Familie oder eine Übernahme scheiden aus; den "
     "Überblick gibt das Video zur Garantenstellung. [ing]In Betracht kommt die Ingerenz: [ing2]Garant ist, wer durch pflichtwidriges "
     "Vorverhalten die nahe Gefahr des Erfolgs geschaffen hat.", PS),
    # --- E Ingerenz im Fall -------------------------------------------------------------------------------------------------
    ("[pfl]Eckhard ist zwanzig Kilometer pro Stunde zu schnell gefahren. Das ist pflichtwidrig. [nahe]Dadurch hat er die "
     "nahe Gefahr geschaffen, dass der Mann stirbt. [garant2]Also ist Eckhard Garant aus Ingerenz. [verkehr]Wer sich dagegen "
     "verkehrsgerecht verhält, handelt nicht pflichtwidrig und wird durch einen Unfall nicht zum Garanten aus Ingerenz.", PS),
    # --- F Vorsatz, unmittelbares Ansetzen ----------------------------------------------------------------------------------
    ("[entspr]Die Entsprechungsklausel ist beim Tötungsdelikt unproblematisch. [vors2]Eckhard kennt den Unfall, hält den Tod "
     "für möglich, ebenso, dass ein Notruf den Mann retten könnte, und nimmt den Tod in Kauf. Das ist bedingter "
     "Tötungsvorsatz. [ansetz]Unmittelbar angesetzt hat er, als er wegfuhr: Der Mann war "
     "schon in Lebensgefahr, und Eckhard gab jede Rettungsmöglichkeit aus der Hand. [rueck]Ein Rücktritt scheidet aus: Eckhard hat "
     "sich nicht bemüht, den Tod zu verhindern.", PS),
    # --- G Mordmerkmal Verdeckungsabsicht -----------------------------------------------------------------------------------
    ("[mord]Und Mord? [p211]Paragraf zweihundertelf Absatz zwei: Mörder ist, wer, um eine andere Straftat zu verdecken, "
     "einen Menschen tötet. [vortat]Die andere Straftat ist die fahrlässige Körperverletzung. [entd]Eckhard will nicht als "
     "Täter entdeckt werden. [bed]Dass er den Tod nur in Kauf nimmt, schadet nicht: Nach seiner Vorstellung verdeckt die Flucht "
     "die Tat auch dann, wenn der Mann überlebt, denn der Mann kennt ihn nicht.", PS),
    ("[streit]Umstritten war, ob man durch bloßes Unterlassen verdecken kann. [alt]Früher verneinte das der "
     "Bundesgerichtshof, und Teile der Lehre folgen ihm: Wer nur wegfährt, decke bloß nicht auf. [neu]Heute bejahen der "
     "Bundesgerichtshof und die herrschende Lehre das Verdecken durch Unterlassen. [entsch]Zu Recht: Der Wortlaut verlangt "
     "kein aktives Tun, und von Eckhard wird keine Selbstanzeige verlangt, nur ein Notruf, der auch anonym möglich ist. "
     "[verd]Eckhard handelt also in Verdeckungsabsicht. [milder]Die Strafe kann nach Paragraf dreizehn Absatz zwei "
     "gemildert werden.", PS),
    # --- H § 142, § 323c, Konkurrenzen, Ergebnis ----------------------------------------------------------------------------
    ("[p142]Außerdem hat Eckhard sich unerlaubt vom Unfallort entfernt, Paragraf hundertzweiundvierzig: [p142b]Er ist "
     "weggefahren, bevor er die Feststellung seiner Person ermöglicht oder angemessen gewartet hat. [p323]Die unterlassene "
     "Hilfeleistung nach Paragraf dreihundertdreiundzwanzig c tritt hinter dem versuchten Mord zurück. [konk]Versuchter Mord und unerlaubtes Entfernen stehen in Tateinheit, die fahrlässige "
     "Körperverletzung steht dazu in Tatmehrheit.", PS),
    ("[erg]Ergebnis: Eckhard ist strafbar wegen fahrlässiger Körperverletzung und wegen versuchten Mordes durch "
     "Unterlassen in Tateinheit mit unerlaubtem Entfernen vom Unfallort.", PS),
    # --- I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne die Fahrt als Tun vom Weiterfahren als Unterlassen. [tipp2]Und prüfe beim Verdeckungsmord durch "
     "Unterlassen, ob die Vortat schon mit Tötungsvorsatz begangen wurde. Dann fehlt die andere Straftat, die verdeckt werden soll.", PS),
    # --- J Prüfschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für den versuchten Mord durch Unterlassen. [s0]Vorprüfung: Die Tat ist nicht vollendet, der "
     "Versuch ist strafbar. [s1]Römisch eins, Tatentschluss. [s1a]Der Vorsatz umfasst den Tod, die mögliche Rettung "
     "[s1b]und die Garantenstellung, hier aus Ingerenz. [s1c]Dazu kommt die Entsprechung. [s1d]Und als Mordmerkmal die "
     "Verdeckungsabsicht. [s2]Römisch zwei, unmittelbares Ansetzen. [s3]Römisch drei und vier: Rechtswidrigkeit und Schuld. "
     "[s5]Danach Rücktritt und die Strafmilderung.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer durch pflichtwidriges Verhalten eine Lebensgefahr schafft, muss sie beseitigen. [m2]Fährt er weiter, "
     "um seine Tat zu verdecken, droht ein Mord durch Unterlassen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
