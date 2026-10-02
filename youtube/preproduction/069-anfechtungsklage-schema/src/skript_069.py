"""Folge 069 · Anfechtungsklage Schema (§ 42 I VwGO): Zulässigkeit und Begründetheit (Fr · Klausurpraxis ·
Verwaltungsprozessrecht). Übungsfall nach dem Hook des Themenplans („Die Stadt untersagt dir per Bescheid den Betrieb
deines Foodtrucks“), Beispielland Nordrhein-Westfalen: Frau Ebeling verkauft mittags Suppen aus ihrem Foodtruck im
Gewerbegebiet. Sie hat seit drei Jahren 30.000 € Steuerschulden und keinen Plan zur Tilgung. Die Stadt hört sie an; dann
bringt Herr Gerlach vom Gewerbeamt den Bescheid: Untersagung des Gewerbes (§ 35 I 1 GewO), schriftlich, begründet, mit
richtiger Rechtsbehelfsbelehrung. Drei Wochen später klagt sie beim Verwaltungsgericht.
A. Zulässigkeit: § 40 I 1 VwGO (BVerwG 3 B 40.21 Rn. 10, 12), § 42 I Alt. 1 (Wortlautkarte), § 42 II (Wortlautkarte;
Möglichkeitstheorie BVerwG 4 C 3.20 Rn. 9; Adressatentheorie BVerwG 9 B 4.19 Rn. 18), Vorverfahren § 68 I 2 VwGO i. V. m.
§ 110 I 1, III 2 Nr. 4 JustG NRW, Klagefrist § 74 I 2 (§ 58 II ein Satz), Klagegegner § 78 I Nr. 1 (Nr. 2 in NRW nicht
genutzt), §§ 61, 62, Rechtsschutzbedürfnis. B. Begründetheit § 113 I 1 (Wortlautkarte): Ermächtigungsgrundlage § 35 I 1 GewO,
formell (Zuständigkeit nach Landesrecht, Anhörung § 28 I, Heilung § 45 I Nr. 3, II, Form § 39 I VwVfG/VwVfG NRW), materiell
(Unzuverlässigkeit, BVerwG 8 C 6.14 Rn. 14; gebundene Entscheidung, § 114 VwGO), Rechtsverletzung (9 B 4.19 Rn. 18).
Klausurtipp und Merksatz mit Lexi.
Fiktive Figuren: Frau Ebeling (sabrina), Herr Gerlach (william), die Richterin (laura_ruhig). Belege je Aussage: RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Ebeling": "sabrina", "Gerlach": "william", "Richterin": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Mittag im Gewerbegebiet, der Bescheid ------------------------------------------------------------------
    ("[fall]Mittags im Gewerbegebiet. Frau Ebeling verkauft Suppen aus ihrem Foodtruck. [brief]Vor zwei Wochen hat die "
     "Stadt sie angeschrieben: Sie durfte sich zu ihren Steuerschulden äußern. [gerlach]Heute bringt Herr Gerlach vom "
     "Gewerbeamt den Bescheid.", 0.2),
    ("[ge1]Frau Ebeling, Sie schulden dem Finanzamt seit drei Jahren dreißigtausend Euro. Wir untersagen Ihnen das "
     "Gewerbe.", 0.3, "Gerlach"),
    ("[eb1]Ich zahle doch, sobald der Sommer gut läuft! Dagegen klage ich.", 0.3, "Ebeling"),
    ("[klage]Drei Wochen später erhebt sie Klage beim Verwaltungsgericht. [frage]Hat die Klage Erfolg? [frage2]Das Schema, am "
     "Beispiel Nordrhein-Westfalen.", 0.6),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Aufbau und Rechtsweg -------------------------------------------------------------------------------------------
    ("[aufbau]Die Anfechtungsklage prüfst du in zwei Schritten: [aufbau2]A, Zulässigkeit, B, Begründetheit. "
     "[rweg]Erstens, der Verwaltungsrechtsweg, Paragraf vierzig Absatz eins: eine öffentlich-rechtliche Streitigkeit "
     "nichtverfassungsrechtlicher Art. [rweg2]Ein Gewerbe untersagen darf nur eine Behörde, keine "
     "Privatperson: öffentliches Recht. [rweg3]Verfassungsorgane streiten nicht, und eine "
     "abdrängende Sonderzuweisung fehlt.", P),
    # --- D Statthafte Klageart, Wortlaut § 42 I ---------------------------------------------------------------------------
    ("[wl42]Zweitens, die statthafte Klageart. Paragraf zweiundvierzig Absatz eins: Durch Klage kann die Aufhebung eines "
     "Verwaltungsakts begehrt werden, die Anfechtungsklage. [va]Die Untersagung regelt verbindlich einen Einzelfall mit "
     "Wirkung nach außen, ist also ein Verwaltungsakt. [va2]Frau Ebeling will ihn loswerden: Anfechtungsklage. [va3]Mehr "
     "dazu in unseren Videos zum Verwaltungsakt und zu den Klagearten.", P),
    # --- E Klagebefugnis, Wortlaut § 42 II -------------------------------------------------------------------------------
    ("[wl422]Drittens, die Klagebefugnis, Absatz zwei: Soweit gesetzlich nichts anderes bestimmt ist, ist die Klage nur "
     "zulässig, wenn der Kläger geltend macht, durch den Verwaltungsakt oder seine Ablehnung oder Unterlassung in seinen "
     "Rechten verletzt zu sein. [mt]Es genügt, dass eine Verletzung möglich ist. Ausgeschlossen ist sie nur, wenn die "
     "Rechte offensichtlich und eindeutig nach keiner Betrachtungsweise bestehen oder zustehen können. [adr]Als Adressatin "
     "eines belastenden Bescheids kann Frau Ebeling jedenfalls in ihrer allgemeinen Handlungsfreiheit verletzt sein, "
     "Artikel zwei Absatz eins Grundgesetz: [adr2]die Adressatentheorie.", P),
    # --- F Vorverfahren und Klagefrist -------------------------------------------------------------------------------------
    ("[vv]Viertens, das Vorverfahren. Nach Paragraf achtundsechzig kommt vor die Klage der Widerspruch, außer "
     "ein Gesetz bestimmt etwas anderes. [nrw]In Nordrhein-Westfalen entfällt er nach Paragraf hundertzehn "
     "Justizgesetz in der Regel, ausdrücklich auch bei der Gewerbeordnung. [land]In deinem "
     "Land kann das anders sein.", P),
    ("[frist]Fünftens, die Klagefrist, Paragraf vierundsiebzig Absatz eins: Ohne Vorverfahren läuft sie einen Monat ab "
     "Bekanntgabe des Verwaltungsakts. [rbb]Fehlt die Rechtsbehelfsbelehrung oder "
     "ist sie falsch, gilt nach Paragraf achtundfünfzig eine Jahresfrist. [frist2]Frau Ebeling klagt nach drei Wochen, "
     "rechtzeitig.", P),
    # --- G Klagegegner, Beteiligte, Rechtsschutzbedürfnis -------------------------------------------------------------------
    ("[kg]Sechstens, der richtige Klagegegner, Paragraf achtundsiebzig Absatz eins Nummer eins: die Körperschaft, deren "
     "Behörde den Bescheid erlassen hat. Das ist das Rechtsträgerprinzip. [kg2]Frau Ebeling verklagt also die Stadt, nicht "
     "das Gewerbeamt. [kg3]Nach Nummer zwei kann das Landesrecht die Behörde selbst zum Gegner machen. "
     "Nordrhein-Westfalen tut das nicht.", P),
    ("[bet]Siebtens, Beteiligten- und Prozessfähigkeit, Paragrafen einundsechzig und zweiundsechzig: Frau Ebeling als "
     "natürliche, die Stadt als juristische Person. [rsb]Achtens, das "
     "Rechtsschutzbedürfnis: Ohne Klage würde der Bescheid bestandskräftig. [zul]Die Klage ist zulässig.", PS),
    # --- H Begründetheit, Wortlaut § 113 I 1 -------------------------------------------------------------------------------
    ("[wl113]B, Begründetheit. Paragraf hundertdreizehn Absatz eins Satz eins: Soweit der Verwaltungsakt rechtswidrig und "
     "der Kläger dadurch in seinen Rechten verletzt ist, hebt das Gericht den Verwaltungsakt und den etwaigen "
     "Widerspruchsbescheid auf. [zwei]Zwei Fragen also: Ist der Bescheid rechtswidrig? "
     "Und ist sie dadurch in ihren Rechten verletzt?", P),
    # --- I Ermächtigungsgrundlage und formelle Rechtmäßigkeit --------------------------------------------------------------
    ("[egl]Erstens, die Ermächtigungsgrundlage. Ein belastender Bescheid braucht ein Gesetz. Hier: Paragraf fünfunddreißig "
     "Absatz eins Gewerbeordnung, die Gewerbeuntersagung. [formell]Zweitens, die formelle Rechtmäßigkeit. Zuständig ist die "
     "Stadt, das regelt das Landesrecht. [anh]Verfahren: Vor einem belastenden Bescheid ist der Betroffene anzuhören, "
     "Paragraf achtundzwanzig Verwaltungsverfahrensgesetz. Frau Ebeling durfte sich äußern. [heil]Fehlt die Anhörung, "
     "kann sie bis zum Abschluss der letzten Tatsacheninstanz nachgeholt werden, Paragraf fünfundvierzig. [form]Form: Der Bescheid ist schriftlich und begründet, Paragraf neununddreißig.", P),
    # --- J Materielle Rechtmäßigkeit ---------------------------------------------------------------------------------------
    ("[tb]Drittens, die materielle Rechtmäßigkeit. Tatbestand: Tatsachen müssen die Unzuverlässigkeit belegen. "
     "[unz]Unzuverlässig ist, wer nach dem Gesamteindruck seines Verhaltens nicht die Gewähr bietet, sein Gewerbe künftig "
     "ordnungsgemäß zu betreiben. [steuer]Erhebliche Steuerrückstände sind dafür ein Anhaltspunkt. Das entfällt nur, wenn "
     "jemand zahlungswillig ist und nach einem sinnvollen und erfolgversprechenden Sanierungskonzept arbeitet. [steuer2]Frau Ebeling hofft nur "
     "auf einen guten Sommer. Sie ist unzuverlässig, und die Untersagung ist zum Schutz der Allgemeinheit "
     "erforderlich.", P),
    ("[rf]Rechtsfolge: Nach Paragraf fünfunddreißig ist das Gewerbe zu untersagen. Die Stadt hat kein Ermessen. [erm]Hat "
     "die Behörde Ermessen, prüft das Gericht nach Paragraf hundertvierzehn nur Ermessensfehler.", P),
    # --- K Rechtsverletzung und Ergebnis -----------------------------------------------------------------------------------
    ("[rv]Der Bescheid ist also rechtmäßig. [rv2]Wäre er rechtswidrig, wäre Frau Ebeling als Adressatin regelmäßig auch in "
     "ihren Rechten verletzt. [urteil]Das Verwaltungsgericht entscheidet:", 0.2),
    ("[ri1]Die Klage ist zulässig, aber unbegründet. Sie wird abgewiesen.", 0.6, "Richterin"),
    # --- L Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Halte die Reihenfolge ein, aber schreib nicht zu jedem Punkt einen Absatz. [tipp1]Was "
     "unproblematisch ist, stellst du in einem Satz fest, etwa das Rechtsschutzbedürfnis. "
     "[tipp2]Deine Zeit gehört den echten Problemen, hier der Unzuverlässigkeit.", PS),
    # --- M Klausurschema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sa]A, Zulässigkeit: [s1]Verwaltungsrechtsweg, [s2]statthafte Klageart, "
     "[s3]Klagebefugnis, [s4]Vorverfahren, [s5]Klagefrist, [s6]Klagegegner, [s7]Beteiligten- und Prozessfähigkeit, "
     "[s8]Rechtsschutzbedürfnis. [sb]B, Begründetheit: [s9]Ermächtigungsgrundlage, [s10]formelle und "
     "[s11]materielle Rechtmäßigkeit, [s12]Verletzung in eigenen Rechten.", PS),
    # --- N Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Anfechtungsklage ist begründet, soweit der Verwaltungsakt rechtswidrig ist und den Kläger in seinen "
     "Rechten verletzt. [m2]Unproblematisches kurz, Probleme gründlich.", 1.4),
]
