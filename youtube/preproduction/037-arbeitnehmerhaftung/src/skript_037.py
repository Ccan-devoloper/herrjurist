"""Folge 037 · Firmenwagen geschrottet: Arbeitnehmerhaftung – wer zahlt den Schaden? (Mo · Der Fall · Zivilrecht/Arbeitsrecht).
Übungsfall: Außendienstmitarbeiterin Imke fährt auf einer Dienstfahrt mit dem Firmenwagen im Stau auf einen Lkw auf
(Blechschaden, niemand verletzt; normale Fahrlässigkeit). Reparatur 12.000 Euro, keine Vollkasko. Ihr Arbeitgeber,
Herr Schäfer (Inhaber eines Werkzeughandels), verlangt den vollen Betrag.
Kern: § 280 Abs. 1 BGB (Wortlaut), § 619a BGB (Wortlaut, Beweislast beim Arbeitgeber), innerbetrieblicher Schadensausgleich
nach BAG GS, Beschl. v. 27.9.1994 – GS 1/89 (A), BAGE 78, 56 (§ 254 BGB analog, Betriebsrisiko, betrieblich veranlasste
Tätigkeit, Haftung nach Verschuldensgrad, Abwägung), BAG 8 AZR 418/09 (Rn. 14, 17, 18, 25), 8 AZR 705/11 (Rn. 22, 26, 29,
45), 8 AZR 116/14 (Rn. 25), 8 AZR 432/11 (Rn. 13); Gegenfälle grobe Fahrlässigkeit, Vorsatz, Personenschaden § 105 SGB VII.
Figuren: Imke (julia), Herr Schäfer (christian); Lexi/Erzählerin Carla. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.8

STIMMEN = {"Imke": "julia", "Schaefer": "christian"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Dienstfahrt -------------------------------------------------------------------------------------------
    ("[fall]Imke arbeitet im Außendienst eines Werkzeughändlers. [fahrt]Mit dem Firmenwagen fährt sie zu einem Kunden. "
     "[stau]Auf der Landstraße staut sich der Verkehr. [auffahr]Imke ist einen Moment unaufmerksam, hält zu wenig Abstand "
     "und fährt auf einen Lastwagen auf.", 0.3),
    ("[i1]Oh nein, der Firmenwagen!", 0.3, "Imke"),
    ("[blech]Verletzt wird niemand. [lkw]Den Schaden am Lastwagen zahlt die Haftpflichtversicherung des Firmenwagens, als Fahrerin "
     "ist Imke mitversichert. [kosten]Doch die Reparatur des Firmenwagens kostet zwölftausend Euro, [kasko0]und eine "
     "Vollkaskoversicherung gibt es nicht.", 0.3),
    # --- B Im Büro -----------------------------------------------------------------------------------------------------------
    ("[buero]Ihr Chef, Herr Schäfer, verlangt das Geld von ihr.", 0.2),
    ("[s1]Sie haben den Wagen beschädigt. Sie zahlen die Reparatur!", 0.3, "Schaefer"),
    ("[i2]Aber ich war doch dienstlich unterwegs!", 0.4, "Imke"),
    ("[frage]Muss Imke die zwölftausend Euro ersetzen? [frage2]Und was ändert der Grad ihres Verschuldens?", 0.6),
    # --- C Sachverhalt ---------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Anspruchsgrundlage: § 280 Abs. 1 BGB --------------------------------------------------------------------------------
    ("[agl]Herr Schäfer stützt sich auf Paragraf zweihundertachtzig Absatz eins. [w280]Verletzt der Schuldner eine Pflicht "
     "aus dem Schuldverhältnis, so kann der Gläubiger Ersatz des hierdurch entstehenden Schadens verlangen. [w280b]Dies gilt "
     "nicht, wenn der Schuldner die Pflichtverletzung nicht zu vertreten hat.", P),
    ("[sv1]Das Schuldverhältnis ist der Arbeitsvertrag. [pv]Aus ihm folgt die Pflicht, Rücksicht auf das Eigentum des "
     "Arbeitgebers zu nehmen, Paragraf zweihunderteinundvierzig Absatz zwei. [pv2]Mit dem Auffahrunfall hat Imke diese "
     "Pflicht verletzt. [schad]Der Schaden: zwölftausend Euro.", PS),
    # --- E § 619a BGB: Beweislast --------------------------------------------------------------------------------------------
    ("[w619]Im Arbeitsverhältnis gilt aber Paragraf sechshundertneunzehn a. [w619b]Abweichend von Paragraf zweihundertachtzig "
     "Absatz eins hat der Arbeitnehmer dem Arbeitgeber Ersatz für den aus der Verletzung einer Pflicht aus dem "
     "Arbeitsverhältnis entstehenden Schaden nur zu leisten, wenn er die Pflichtverletzung zu vertreten hat.", P),
    ("[bew]Das heißt: Nicht Imke muss sich entlasten. [bew2]Herr Schäfer muss beweisen, dass sie die Pflichtverletzung zu "
     "vertreten hat. [bew3]Hier steht fest: Sie war unaufmerksam, also fahrlässig, Paragraf zweihundertsechsundsiebzig.", PS),
    # --- F Innerbetrieblicher Schadensausgleich ------------------------------------------------------------------------------
    ("[ibs]Muss sie deshalb alles zahlen? Nein. [gs]Der Große Senat des Bundesarbeitsgerichts hat neunzehnhundertvierundneunzig "
     "entschieden: [gs2]Bei betrieblich veranlasster Tätigkeit ist die Haftung des Arbeitnehmers beschränkt. "
     "[p254]Grundlage ist Paragraf zweihundertvierundfünfzig, entsprechend angewendet. [risk]Denn der Arbeitgeber muss sich "
     "sein Betriebsrisiko zurechnen lassen: Er organisiert den Betrieb und gestaltet die Arbeitsbedingungen.", PS),
    # --- G Betrieblich veranlasst --------------------------------------------------------------------------------------------
    ("[bv]Erste Voraussetzung: eine betrieblich veranlasste Tätigkeit. [bv2]Gemeint ist, was dem Arbeitnehmer übertragen ist "
     "oder was er im Interesse des Betriebs tut. [bv3]Die Fahrt zum Kunden gehört zu ihrer Arbeit. [bv4]Anders bei einer "
     "Privatfahrt am Wochenende: Das ist ihr allgemeines Lebensrisiko, die Beschränkung greift dann nicht.", PS),
    # --- H Haftung nach dem Grad des Verschuldens ----------------------------------------------------------------------------
    ("[stufen]Dann kommt es auf den Grad des Verschuldens an. [st1]Leichteste Fahrlässigkeit: Sie haftet gar nicht. "
     "[st2]Normale, auch mittlere Fahrlässigkeit: Der Schaden wird in aller Regel geteilt. [st3]Grobe Fahrlässigkeit: Sie "
     "trägt in aller Regel den ganzen Schaden. [st4]Vorsatz: Sie haftet voll.", PS),
    # --- I Subsumtion und Abwägung --------------------------------------------------------------------------------------------
    ("[mittel]Imke war einen Moment unaufmerksam und hielt zu wenig Abstand, ein grober Verstoß liegt nicht vor. "
     "[mittel2]Das ist normale Fahrlässigkeit. [abw]Also wird geteilt, nach einer Abwägung aller Umstände. [abw1]Dazu gehören "
     "der Grad des Verschuldens und die Gefahr der Tätigkeit, [abw2]die Höhe des Schadens im Verhältnis zum Verdienst: "
     "Zwölftausend Euro sind vier Monatsgehälter. [abw3]Und das Risiko, das der Arbeitgeber versichern konnte.", P),
    ("[kasko]Zur Vollkasko: [kasko1]Eine Pflicht, sie abzuschließen, hat Herr Schäfer nicht. [kasko2]Doch ein Risiko, das er "
     "durch eine Versicherung decken konnte, spricht in der Abwägung für Imke. [erg]Ergebnis: Imke trägt nur einen Teil "
     "des Schadens. [erg2]Die genaue Quote bestimmt das Gericht im Einzelfall.", PS),
    # --- J Gegenfälle: grobe Fahrlässigkeit, Vorsatz -------------------------------------------------------------------------
    ("[grob]Und wenn Imke während der Fahrt eine Nachricht ins Handy tippt? [grob1]Nehmen wir an, das ist grob fahrlässig: "
     "Sie hat die Sorgfalt in ungewöhnlich hohem Maß verletzt. [grob2]Dann trägt sie in aller Regel den ganzen Schaden. "
     "[grob3]Doch auch hier sind Erleichterungen möglich, [grob4]vor allem, wenn ihr Verdienst in einem deutlichen "
     "Missverhältnis zum Schadensrisiko steht. [grob5]Eine feste Obergrenze, etwa drei Monatsgehälter, gibt es aber nicht. "
     "[vors]Bei Vorsatz bleibt es bei der vollen Haftung.", PS),
    # --- K Abgrenzung: Personenschaden § 105 SGB VII ----------------------------------------------------------------------------
    ("[pers]Noch eine Abgrenzung: Hätte Imke bei dem Unfall einen mitfahrenden Kollegen verletzt, gälte für diesen "
     "Personenschaden Paragraf hundertfünf des Siebten Sozialgesetzbuchs. [pers2]Dann haftet sie ihm grundsätzlich nur bei "
     "Vorsatz.", PS),
    # --- L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Haftungsbeschränkung erst, wenn der Anspruch aus Paragraf zweihundertachtzig steht, "
     "[tipp1]etwa beim Umfang des Ersatzes. [tipp2]Und vergiss Paragraf sechshundertneunzehn a nicht: Im Arbeitsverhältnis "
     "wird das Vertretenmüssen nicht vermutet. [tipp3]Die Grundsätze gelten auch für den Anspruch aus Paragraf "
     "achthundertdreiundzwanzig.", PS),
    # --- M Klausurschema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sc1]Anspruch des Arbeitgebers aus Paragraf zweihundertachtzig Absatz eins. [sc2]Römisch "
     "eins: Schuldverhältnis, der Arbeitsvertrag. [sc3]Römisch zwei: Pflichtverletzung. [sc4]Römisch drei: Vertretenmüssen, "
     "Beweislast nach Paragraf sechshundertneunzehn a. [sc5]Römisch vier: Schaden.", P),
    ("[sc6]Römisch fünf: Haftungsbeschränkung. Erstens: betrieblich veranlasste Tätigkeit. [sc7]Zweitens: Grad des "
     "Verschuldens. [sc8]Drittens: Abwägung aller Umstände, Paragraf zweihundertvierundfünfzig analog.", PS),
    # --- N Merksatz (Lexi) ---------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer bei der Arbeit einen Schaden anrichtet, haftet nach dem Grad seines Verschuldens. "
     "[m2]Bei leichtester Fahrlässigkeit gar nicht, bei normaler anteilig, bei grober in aller Regel voll.", 1.4),
]
