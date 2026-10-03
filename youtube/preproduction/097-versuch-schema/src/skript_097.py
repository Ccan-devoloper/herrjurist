"""Folge 097 · Versuch Schema: Vorprüfung, Tatentschluss, unmittelbares Ansetzen (Mo · Der Fall · Strafrecht/StGB AT,
Format Schema). Fiktiver Fall nach dem Plan-Hook („Ein Mann schießt auf seinen Nachbarn und verfehlt ihn um Zentimeter“):
Nachbarschaftsstreit um ein Auto vor der Garage; Herbert holt eine alte Pistole mit einer einzigen Patrone, zielt aus fünf
Metern auf Gregor, will ihn töten und drückt ab; die Kugel verfehlt Gregor um Zentimeter, niemand wird verletzt.
Kern: Wortlautkarten § 22 und § 23 Abs. 1 StGB; Klausurschema versuchter Totschlag §§ 212, 22, 23 Abs. 1 StGB:
0. Vorprüfung (Nichtvollendung; Strafbarkeit des Versuchs, § 23 Abs. 1 i. V. m. § 12 Abs. 1: Verbrechen),
I. Tatbestand – 1. Tatentschluss (BGH 4 StR 324/19 Rn. 17; besondere subjektive Merkmale = Klausurstandard),
2. unmittelbares Ansetzen (BGH 5 StR 15/20 = BGHSt 65, 15, Rn. 4 f.; Waffe holen = Vorbereitung), II. Rechtswidrigkeit,
III. Schuld, IV. Rücktritt § 24 (fehlgeschlagener Versuch, BGH 2 StR 598/24 Rn. 11; 4 StR 169/25 Rn. 6),
Ergebnis, § 23 Abs. 2 i. V. m. § 49 Abs. 1, Konkurrenz (BGH 2 StR 180/13 Rn. 12); Klausurtipp, Schema, Merksatz (Lexi).
Belege je Aussage: ../RECHTSSTAND.md.
Figuren: Herbert (william, Mann älter), Gregor (marc, Mann mittel); Erzählerin/Lexi Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter. Namen nie im Genitiv mit -s."""

P, PS = 0.3, 0.5

STIMMEN = {"Herbert": "william", "Gregor": "marc"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Wohnstraße ---------------------------------------------------------------------------------------
    ("[fall]Samstagabend in einer ruhigen Wohnstraße. [herbert]Herbert, Anfang sechzig, und sein Nachbar [gregor]Gregor "
     "streiten seit Monaten. [auto]Immer wieder parkt Gregor sein Auto vor der Garage von Herbert.", 0.3),
    ("[h1]Fahr endlich dein Auto weg!", 0.3, "Herbert"),
    ("[holt]Herbert geht ins Haus und holt eine alte Pistole. [patrone]Darin steckt eine einzige Patrone. [zurueck]Er "
     "kommt zurück und zielt aus fünf Metern auf Gregor.", 0.3),
    ("[g1]Herbert, leg die Pistole weg!", 0.3, "Gregor"),
    ("[schuss]Herbert will Gregor töten und drückt ab. [verfehlt]Die Kugel verfehlt ihn um wenige Zentimeter und schlägt "
     "in die Hauswand ein. [flieht]Gregor rennt in sein Haus und schließt ab.", 0.3),
    ("[h2]Das war meine einzige Patrone.", 0.4, "Herbert"),
    ("[frage]Gregor bleibt unverletzt. Ist Herbert trotzdem strafbar? [frage2]Wir prüfen den versuchten Totschlag "
     "Schritt für Schritt.", 0.6),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut §§ 22, 23 I und Aufbau ----------------------------------------------------------------------------
    ("[p22]Paragraf zweiundzwanzig: [p22w]Eine Straftat versucht, wer nach seiner Vorstellung von der Tat zur "
     "Verwirklichung des Tatbestandes unmittelbar ansetzt. [p23]Und Paragraf dreiundzwanzig, Absatz eins: [p23w]Der "
     "Versuch eines Verbrechens ist stets strafbar, der Versuch eines Vergehens nur dann, wenn das Gesetz es ausdrücklich "
     "bestimmt. [aufbau]Daraus folgt der Aufbau: Vorprüfung, Tatentschluss, unmittelbares Ansetzen. [mord]Mordmerkmale "
     "legt der Fall nicht nahe. Wir prüfen also Paragraf zweihundertzwölf.", PS),
    # --- D 0. Vorprüfung ----------------------------------------------------------------------------------------------
    ("[vp]Null: die Vorprüfung. [vp1]Erstens ist die Tat nicht vollendet, denn Gregor lebt. [vp2]Zweitens muss der "
     "Versuch strafbar sein. [vp3]Totschlag ist mit Freiheitsstrafe nicht unter fünf Jahren bedroht, also ein Verbrechen "
     "nach Paragraf zwölf, Absatz eins. [vp4]Sein Versuch ist damit stets strafbar.", PS),
    # --- E I.1 Tatentschluss ------------------------------------------------------------------------------------------
    ("[te]Römisch eins: der Tatbestand, erstens der Tatentschluss. [te1]Nach dem Bundesgerichtshof braucht der Täter eine "
     "vorsatzgleiche Vorstellung, die sich auf alle Umstände des äußeren Tatbestands bezieht. [te2]Verlangt ein Delikt "
     "besondere subjektive Merkmale, etwa eine Absicht, gehören sie ebenfalls hierher. Paragraf zweihundertzwölf kennt "
     "keine. [te3]Herbert will Gregor töten, also einen anderen Menschen. Der Tatentschluss liegt vor.", PS),
    # --- F I.2 Unmittelbares Ansetzen ---------------------------------------------------------------------------------
    ("[ua]Zweitens das unmittelbare Ansetzen. [ua1]Nach der Formel der Rechtsprechung überschreitet der Täter subjektiv "
     "die Schwelle zum Jetzt geht es los. [ua2]Seine Handlung soll nach dem Tatplan ohne Zwischenschritte in die "
     "Tatbestandsverwirklichung einmünden. [ua3]Wesentlich ist auch, wie konkret das geschützte Rechtsgut aus seiner "
     "Sicht schon gefährdet ist. [ua4]Herbert hat abgedrückt und damit alles getan. Das Ansetzen ist unproblematisch. "
     "[vorb]Anders, solange er nur die Pistole aus dem Haus holt: Bis zum Schuss fehlen noch wesentliche Zwischenschritte. "
     "Das ist bloße Vorbereitung.", PS),
    # --- G II. Rechtswidrigkeit, III. Schuld --------------------------------------------------------------------------
    ("[rw]Römisch zwei: Rechtswidrigkeit. Gregor hat nur mit Worten gestritten. [rw2]Es gibt keinen Angriff, also keine "
     "Notwehr. [schuld]Römisch drei: Schuld. Für Schuldunfähigkeit oder eine Entschuldigung spricht nichts.", PS),
    # --- H IV. Rücktritt ----------------------------------------------------------------------------------------------
    ("[rt]Römisch vier: der Rücktritt nach Paragraf vierundzwanzig, ein eigener Prüfungspunkt nach der Schuld. [rt1]Er "
     "scheidet aus, wenn der Versuch fehlgeschlagen ist. [rt2]Das ist er nach dem Bundesgerichtshof, wenn die Tat mit den "
     "eingesetzten oder anderen naheliegenden Mitteln nicht mehr vollendet werden kann und der Täter das erkennt. "
     "[rt3]Maßgeblich ist seine Sicht nach dem Schuss. [rt4]Herbert hatte nur diese eine Patrone, und er weiß das. "
     "[rt5]Der Versuch ist fehlgeschlagen, ein Rücktritt ist ausgeschlossen.", PS),
    # --- I Ergebnis, Strafmilderung, Konkurrenz -----------------------------------------------------------------------
    ("[erg]Ergebnis: Herbert hat sich wegen versuchten Totschlags strafbar gemacht, nach den Paragrafen "
     "zweihundertzwölf, zweiundzwanzig und dreiundzwanzig, Absatz eins. [mild]Die Strafe kann nach Paragraf "
     "dreiundzwanzig, Absatz zwei, gemildert werden, in Verbindung mit Paragraf neunundvierzig, Absatz eins. [konk]Die "
     "versuchte gefährliche Körperverletzung tritt nach dem Bundesgerichtshof dahinter zurück.", PS),
    # --- J Klausurtipp (Lexi) -----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Gliedere den Tatbestand beim Versuch nicht in objektiv und subjektiv. [tipp2]Der objektive "
     "Tatbestand ist ja gerade nicht erfüllt. Prüfe zuerst den Tatentschluss, [tipp3]denn ob Herbert unmittelbar "
     "ansetzt, richtet sich nach seiner Vorstellung von der Tat.", PS),
    # --- K Klausurschema ----------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [s0]Null: Vorprüfung, also Nichtvollendung [s0b]und Strafbarkeit des Versuchs. "
     "[s1]Römisch eins: Tatbestand, mit erstens Tatentschluss [s1b]und zweitens unmittelbarem Ansetzen. [s2]Römisch zwei: "
     "Rechtswidrigkeit. [s3]Römisch drei: Schuld. [s4]Römisch vier: Rücktritt nach Paragraf vierundzwanzig, [s4b]der "
     "beim fehlgeschlagenen Versuch ausscheidet.", PS),
    # --- L Merksatz (Lexi) --------------------------------------------------------------------------------------------
    ("[merke]Merke: Versucht hat, wer nach seiner Vorstellung unmittelbar ansetzt. [m2]Der Tatentschluss kommt vor dem "
     "Ansetzen. [m3]Und wer erkennt, dass er die Tat mit seinen Mitteln nicht mehr vollenden kann, kann nicht mehr "
     "zurücktreten.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
