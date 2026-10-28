"""Folge 063 · § 437 BGB: Die Käuferrechte auf einen Blick – Schema (Fr · Klausurpraxis · Zivilrecht/Kaufrecht).
Beispielfall nach dem Plan-Hook („Der neue Kühlschrank kühlt nicht – was kannst du jetzt verlangen, und in welcher
Reihenfolge?“): Manfred (Verbraucher) kauft im Elektrogeschäft von Frau Kemper (Unternehmerin) einen neuen Kühlschrank für
600 €; sie liefert ihn in seine Küche, er kühlt nicht (Kompressor von Anfang an defekt). Manfred verlangt einen neuen und
setzt zwei Wochen Frist; Frau Kemper sagt zu, vergisst den Auftrag. Manfred kauft woanders für 700 € und will sein Geld
zurück und die 100 € Mehrkosten.
Kern: Wortlautkarte § 437 (vollständig), Voraussetzungen (Kaufvertrag, Sachmangel bei Gefahrübergang – Verweis Folge 059 –,
kein Ausschluss), Vorrang der Nacherfüllung, Wortlautkarte § 439 I, § 439 II, III (ein Satz), IV, Fristsetzung als Brücke
(Entbehrlichkeit §§ 323 II, 440, 326 V; § 475d ein Satz), Rücktritt (§§ 437 Nr. 2, 323, 326 V, Erheblichkeit § 323 V 2,
§ 346), Minderung § 441 (Rechenbeispiel), Schadensersatz (§§ 280, 281, 283, 311a, Vermutung § 280 I 2, § 325), § 284
und § 438 je ein Satz, Klausurtipp, Schema, Merksatz.
Figuren: Manfred (william), Frau Kemper (laura_ruhig); Lexi/Erzählerin Carla. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.4, 0.6

STIMMEN = {"Manfred": "william", "Kemper": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Kauf, Lieferung, Anruf, Ersatzkauf -------------------------------------------------------------------
    ("[fall]Manfred kauft im Elektrogeschäft von Frau Kemper einen neuen Kühlschrank für sechshundert Euro. "
     "[liefer]Am nächsten Tag liefert sie ihn in seine Küche. [warm]Am Abend ist er innen noch warm: Der Kompressor "
     "ist von Anfang an defekt.", 0.3),
    ("[ma1]Der Kühlschrank kühlt nicht! Bringen Sie mir bitte innerhalb von zwei Wochen einen neuen.", 0.3, "Manfred"),
    ("[ke1]Ja, ich kümmere mich darum.", 0.4, "Kemper"),
    ("[verg]Doch Frau Kemper vergisst den Auftrag, und die zwei Wochen vergehen. [neu]Manfred kauft woanders einen "
     "gleichen Kühlschrank für siebenhundert Euro.", 0.3),
    ("[ma2]Ich will mein Geld zurück und die hundert Euro mehr!", 0.4, "Manfred"),
    ("[frage]Was kann Manfred verlangen, [frage2]und in welcher Reihenfolge?", 0.6),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 437 BGB (Wortlaut) -------------------------------------------------------------------------------------------
    ("[norm]Die Antwort steht in Paragraf vierhundertsiebenunddreißig. [w1]Ist die Sache mangelhaft, kann der Käufer "
     "erstens Nacherfüllung verlangen, [w2]zweitens zurücktreten oder den Kaufpreis mindern [w3]und drittens Schadensersatz "
     "oder Ersatz vergeblicher Aufwendungen verlangen. [verw]Jede Nummer verweist auf weitere Vorschriften; ihre "
     "Voraussetzungen müssen vorliegen.", P),
    # --- D I. Voraussetzungen ---------------------------------------------------------------------------------------------
    ("[vor]Römisch eins: die gemeinsamen Voraussetzungen. [v1]Es braucht einen wirksamen Kaufvertrag, [v2]einen Sachmangel "
     "bei Gefahrübergang [v3]und keinen Ausschluss der Mängelrechte. [vsub]Ein Kühlschrank, der nicht kühlt, eignet sich "
     "nicht für die gewöhnliche Verwendung, [vgef]und der Kompressor war schon bei der Übergabe defekt. [v059]Wie man den "
     "Mangel genau prüft, zeigt die Folge zu Paragraf vierhundertvierunddreißig. [vok]Einen Ausschluss gibt es hier nicht.", PS),
    # --- E II. Nacherfüllung, § 439 ---------------------------------------------------------------------------------------
    ("[ne]Römisch zwei: die Nacherfüllung, Paragraf vierhundertneununddreißig. Sie steht an erster Stelle, denn der "
     "Verkäufer bekommt eine zweite Chance. [w439]Absatz eins: Der Käufer kann als Nacherfüllung nach seiner Wahl die "
     "Beseitigung des Mangels oder die Lieferung einer mangelfreien Sache verlangen. [wahl]Manfred wählt einen neuen "
     "Kühlschrank.", P),
    ("[kost]Die Kosten der Nacherfüllung trägt der Verkäufer, etwa für Transport, Wege, Arbeit und Material, Absatz zwei. [einbau]Hat der "
     "Käufer die Sache bestimmungsgemäß eingebaut, muss der Verkäufer nach Absatz drei auch Ausbau und Einbau bezahlen. "
     "[verw4]Verweigern darf der Verkäufer die gewählte Art nach Absatz vier, wenn sie nur mit unverhältnismäßigen Kosten "
     "möglich ist. [andere]Dann beschränkt sich der Anspruch auf die andere Art.", PS),
    # --- F III. Frist als Brücke ------------------------------------------------------------------------------------------
    ("[brue]Römisch drei: die Brücke zu den weiteren Rechten. Rücktritt, Minderung und Schadensersatz statt der Leistung "
     "setzen grundsätzlich voraus, dass der Käufer erfolglos eine angemessene Frist zur Nacherfüllung gesetzt hat. "
     "[bgh1]So sichert das Gesetz nach dem Bundesgerichtshof den Vorrang der Nacherfüllung. [fsub]Manfred hat zwei Wochen "
     "gesetzt, und sie sind ungenutzt abgelaufen.", P),
    ("[entb]Entbehrlich ist die Frist etwa, wenn der Verkäufer ernsthaft und endgültig verweigert, [fehl]wenn die Nacherfüllung "
     "fehlschlägt, bei einer Nachbesserung in der Regel nach dem zweiten erfolglosen Versuch, [unm]oder wenn sie unmöglich "
     "ist. [p475d]Beim Verbrauchsgüterkauf genügt nach Paragraf vierhundertfünfundsiebzig d, dass der Unternehmer nach "
     "der Mitteilung des Mangels eine angemessene Zeit verstreichen lässt.", PS),
    # --- G IV. Rücktritt, Minderung ---------------------------------------------------------------------------------------
    ("[rt]Römisch vier: Rücktritt oder Minderung. Der Rücktritt läuft über Paragraf vierhundertsiebenunddreißig Nummer "
     "zwei mit Paragraf dreihundertdreiundzwanzig, [rt2]bei unmöglicher Nacherfüllung mit Paragraf dreihundertsechsundzwanzig "
     "Absatz fünf. [erh]Ausgeschlossen ist er, wenn die Pflichtverletzung unerheblich ist. [bgh2]Bei einem behebbaren Mangel "
     "ist sie nach dem Bundesgerichtshof in der Regel erheblich, wenn die Beseitigung mehr als fünf Prozent des Kaufpreises "
     "kostet. [rsub]Ein Kühlschrank, der gar nicht kühlt, ist erheblich mangelhaft. [rfolge]Manfred erklärt den Rücktritt "
     "und bekommt seine sechshundert Euro zurück, Zug um Zug gegen den Kühlschrank.", PS),
    ("[mi]Statt zurückzutreten, kann der Käufer den Kaufpreis mindern, Paragraf vierhunderteinundvierzig, [mi2]und zwar "
     "auch bei einem unerheblichen Mangel. [mbsp]Wäre nur das Gefrierfach defekt, könnte Manfred den Kühlschrank behalten. "
     "[mre]Gerechnet wird im Verhältnis: Ist er bei Vertragsschluss ohne Mangel achthundert Euro wert und mit Mangel nur "
     "sechshundert, verliert er ein Viertel. [mre2]Dann sinkt auch der Preis um ein Viertel, von sechshundert auf "
     "vierhundertfünfzig Euro.", PS),
    # --- H V. Schadensersatz ----------------------------------------------------------------------------------------------
    ("[se]Römisch fünf: Schadensersatz, Paragraf vierhundertsiebenunddreißig Nummer drei. [se1]Bei einem behebbaren Mangel "
     "gelten Paragraf zweihundertachtzig Absatz eins und drei und Paragraf zweihunderteinundachtzig, also wieder mit Frist. "
     "[se2]Ist die Nacherfüllung unmöglich, greift Paragraf zweihundertdreiundachtzig, [se3]war sie es schon bei "
     "Vertragsschluss, Paragraf dreihundertelf a.", P),
    ("[vm]Das Vertretenmüssen wird vermutet, Paragraf zweihundertachtzig Absatz eins Satz zwei. [vmsub]Frau Kemper hat "
     "die Nacherfüllung zugesagt und dann vergessen, entlasten kann sie sich nicht. [dk]Die hundert Euro Mehrkosten für "
     "den Ersatzkauf bekommt Manfred deshalb als Schadensersatz statt der Leistung. [p325]Und der Rücktritt schließt Schadensersatz nicht "
     "aus, Paragraf dreihundertfünfundzwanzig. [p284]Anstelle des Schadensersatzes statt der Leistung kann der Käufer nach "
     "Paragraf zweihundertvierundachtzig auch Ersatz vergeblicher Aufwendungen verlangen.", PS),
    # --- I Ergebnis, Verjährung -------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Manfred kann zurücktreten und seine sechshundert Euro zurückverlangen, [erg2]dazu hundert Euro "
     "Schadensersatz. [p438]Nacherfüllung und Schadensersatz verjähren in der Regel zwei Jahre nach der "
     "Ablieferung, Paragraf vierhundertachtunddreißig.", PS),
    # --- J Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe in dieser Reihenfolge. Erst die Voraussetzungen von Paragraf vierhundertsiebenunddreißig, "
     "[tipp1]dann das konkrete Recht mit seiner vollen Normkette. [tipp2]Und bei Rücktritt, Minderung und Schadensersatz "
     "statt der Leistung immer zuerst die Frist zur Nacherfüllung.", PS),
    # --- K Klausurschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema: [k1]Römisch eins: Kaufvertrag, Sachmangel bei Gefahrübergang, kein Ausschluss. "
     "[k2]Römisch zwei: Nacherfüllung nach Wahl des Käufers. [k3]Römisch drei: Frist zur Nacherfüllung, erfolglos oder "
     "entbehrlich.", P),
    ("[k4]Römisch vier: Rücktritt bei erheblichem Mangel, oder Minderung. [k5]Römisch fünf: Schadensersatz mit "
     "vermutetem Vertretenmüssen, oder Ersatz vergeblicher Aufwendungen.", PS),
    # --- L Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Erst bekommt der Verkäufer seine zweite Chance. [m2]Wer zurücktreten, mindern oder Schadensersatz "
     "statt der Leistung will, braucht grundsätzlich eine erfolglose Frist zur Nacherfüllung.", 1.4),
]
