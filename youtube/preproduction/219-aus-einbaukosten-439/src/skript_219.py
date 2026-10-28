"""Folge 219 · Aus- und Einbaukosten § 439 III BGB: Der Fliesen-Fall Weber/Putz (Fr · Klausurpraxis · Kaufrecht ·
Klassiker-Fall). Fall nach dem Plan-Hook („Die gekauften Fliesen haben Farbfehler – aber sie liegen schon im ganzen Bad“):
Herr Oltmann (Verbraucher) kauft im Fliesenhandel von Frau Reinecke (Unternehmerin) Fliesen für 1.400 €; ein Fliesenleger
verlegt sie im ganzen Bad. Erst auf der fertigen Fläche zeigen sich deutliche Farbunterschiede (Herstellungsfehler, nicht
behebbar). Ausbau und neu verlegen: 5.200 €. Frau Reinecke: neue Fliesen ja, Ausbau und Verlegen nein.
Kern: I. Sachmangel (§ 434 Abs. 3, Verweis 059) und Nacherfüllung (§ 439 Abs. 1, Verweis 063); Hintergrund: Rechtslage vor
2018, EuGH Weber/Putz (Rn. 47, 62, 71, 74, 78), BGH VIII ZR 70/08 (Rn. 54: 600 €), VIII ZR 226/11 (Rn. 17: nur
Verbrauchsgüterkauf); II./III. § 439 Abs. 3 heute (Wortlautkarte; seit 2018 für alle Kaufverträge; seit 2022 „bevor der
Mangel offenbar wurde“ statt Satz 2 mit § 442), Subsumtion, Geld statt Selbstvornahme, Vorschuss § 475 Abs. 5;
IV. Verweigerung § 439 Abs. 4 (Wortlautkarte), Wegfall der Weber/Putz-Sonderregel § 475 Abs. 4 a. F. (BT-Drs. 19/27424
S. 29); Ergebnis, Regress § 445a; Klausurtipp, Schema, Merksatz.
Figuren: Herr Oltmann (marc), Frau Reinecke (laura_ruhig), der Fliesenleger (william); Lexi/Erzählerin Carla.
Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Oltmann": "marc", "Reinecke": "laura_ruhig", "Fliesenleger": "william"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Kauf, Verlegen, Farbfehler, Streit ------------------------------------------------------------------
    ("[fall]Herr Oltmann kauft im Fliesenhandel von Frau Reinecke neue Fliesen für sein Bad, für tausendvierhundert "
     "Euro. [verleg]Ein Fliesenleger verlegt sie im ganzen Bad. [schlier]Erst auf der fertigen Fläche zeigen sich im "
     "Tageslicht deutliche Farbunterschiede: ein Fehler aus der Herstellung, der sich nicht beheben lässt.", 0.3),
    ("[fl1]Die Fliesen müssen alle wieder raus. Ausbauen und neu verlegen kostet fünftausendzweihundert Euro.", 0.3,
     "Fliesenleger"),
    ("[ol1]Ich brauche neue Fliesen. Und Sie zahlen den Ausbau und das Verlegen.", 0.3, "Oltmann"),
    ("[re1]Neue Fliesen bekommen Sie. Aber ich habe Ihnen Fliesen verkauft, nicht das Verlegen.", 0.4, "Reinecke"),
    ("[frage]Muss Frau Reinecke auch Ausbau und Einbau bezahlen?", 0.6),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C I. Sachmangel und Nacherfüllung -----------------------------------------------------------------------------
    ("[mang]Römisch eins: Sachmangel und Nacherfüllung. [m1]Fliesen mit deutlichen Farbunterschieden haben nicht die "
     "übliche Beschaffenheit, Paragraf vierhundertvierunddreißig Absatz drei. [m059]Wie man den Mangel genau prüft, zeigt "
     "die Folge zum Sachmangel. [ne]Herr Oltmann kann deshalb Nacherfüllung verlangen, Paragraf vierhundertneununddreißig "
     "Absatz eins. [ne2]Nachbessern lässt sich der Fehler nicht, also bleibt die Lieferung neuer Fliesen. [v063]Alle "
     "Käuferrechte im Überblick zeigt die Folge zu Paragraf vierhundertsiebenunddreißig.", PS),
    # --- D Hintergrund: vor 2018, EuGH Weber/Putz, BGH ----------------------------------------------------------------
    ("[alt]Doch umfasst die Lieferung neuer Fliesen auch den Ausbau der alten und das Verlegen der neuen? [alt1]Lange "
     "hieß es in Deutschland: Der Verkäufer bringt nur neue Fliesen. [alt2]Ausbau und Einbau gab es allenfalls als "
     "Schadensersatz, also nur bei Verschulden. [alt3]Und eine Händlerin, die einen Fehler aus der Herstellung nicht "
     "kennt, trifft in der Regel kein Verschulden.", P),
    ("[eugh]Dann kam ein Fliesen-Fall vor den Gerichtshof der Europäischen Union: Weber und Putz, zweitausendelf. [eu1]Nach der "
     "Verbrauchsgüterkaufrichtlinie muss der Verkäufer die mangelhafte Sache selbst ausbauen und die neue einbauen, oder "
     "die Kosten dafür tragen, [eu2]auch wenn er den Einbau gar nicht schuldete. [eu3]Sonst wäre die Ersatzlieferung "
     "nicht unentgeltlich: Der Käufer müsste den Einbau zweimal bezahlen. [eu4]Die einzig mögliche Abhilfe darf der "
     "Verkäufer nicht wegen hoher Kosten verweigern. [eu5]Er darf die Erstattung aber auf einen angemessenen Betrag begrenzen.", P),
    ("[bgh]Der Bundesgerichtshof setzte das um und begrenzte im deutschen Fliesen-Fall die Ausbaukosten auf sechshundert "
     "Euro. [bgh2]Zwischen Unternehmern galt die Lösung aber nicht, etwa für einen Handwerker, der Material kauft und beim "
     "Kunden einbaut.", PS),
    # --- E II. § 439 Abs. 3 BGB heute (Wortlaut) -----------------------------------------------------------------------
    ("[heute]Seit zweitausendachtzehn regelt das Gesetz die Frage für alle Kaufverträge: Paragraf vierhundertneununddreißig "
     "Absatz drei. [w1]Hat der Käufer die mangelhafte Sache gemäß ihrer Art und ihrem Verwendungszweck eingebaut, "
     "[w2]bevor der Mangel offenbar wurde, [w3]muss der Verkäufer im Rahmen der Nacherfüllung die erforderlichen "
     "Aufwendungen für das Entfernen und den Einbau ersetzen.", PS),
    ("[ein]Römisch zwei: der Einbau. [ein1]Fliesen werden verlegt, dafür sind sie gemacht. [ein2]Die Farbunterschiede "
     "zeigten sich erst auf der fertigen Fläche; vorher waren sie nicht offenbar. [kenn]Achtung bei älteren Büchern: Bis "
     "Ende zweitausendeinundzwanzig verwies Satz zwei auf Paragraf vierhundertzweiundvierzig, dann schadete schon grob "
     "fahrlässige Unkenntnis beim Einbau. [kenn2]Diesen Satz gibt es nicht mehr.", PS),
    ("[auf]Römisch drei: die erforderlichen Aufwendungen. [auf1]Das sind die fünftausendzweihundert Euro des "
     "Fliesenlegers. [auf2]Auf ein Verschulden von Frau Reinecke kommt es nicht an, [auf3]und der Kaufvertrag muss den "
     "Einbau nicht vorsehen. [geld]Herr Oltmann bekommt Geld; selbst ausbauen muss Frau Reinecke nicht. [vors]Als "
     "Verbraucher kann er sogar einen Vorschuss verlangen, Paragraf vierhundertfünfundsiebzig Absatz fünf.", PS),
    # --- F IV. Verweigerung, § 439 Abs. 4 BGB --------------------------------------------------------------------------
    ("[verw]Römisch vier: Kann die Verkäuferin verweigern? [v1]Nach Absatz vier darf sie die gewählte Art der "
     "Nacherfüllung verweigern, wenn sie nur mit unverhältnismäßigen Kosten möglich ist. [v2]Abzuwägen sind vor allem "
     "der Wert der Sache ohne Mangel und die Bedeutung des Mangels. [v3]Hier stehen fünftausendzweihundert Euro "
     "Einbaukosten neben Fliesen für tausendvierhundert Euro.", P),
    ("[v4]Die Sonderregel aus Weber und Putz für Verbraucher, früher Paragraf vierhundertfünfundsiebzig Absatz vier, ist "
     "seit zweitausendzweiundzwanzig gestrichen. [v5]Nach der Gesetzesbegründung muss der Verkäufer auch beim Verbraucher keine "
     "unverhältnismäßige Leistung erbringen; [v6]der Käufer kann dann zurücktreten oder mindern. [v7]Frau Reinecke verweigert aber nicht, sie bietet neue Fliesen an.", PS),
    # --- G Ergebnis, Regress ------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Frau Reinecke muss neue Fliesen liefern [erg2]und Herrn Oltmann die fünftausendzweihundert Euro "
     "für Ausbau und Einbau ersetzen. [regr]Darauf sitzen bleibt sie nicht: Nach Paragraf vierhundertfünfundvierzig a "
     "kann sie diese Aufwendungen von ihrem Lieferanten verlangen, wenn der Mangel schon bei der Lieferung an sie "
     "bestand.", PS),
    # --- H Klausurtipp (Lexi) -----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Aus- und Einbaukosten in der Nacherfüllung, nicht beim Schadensersatz. [tipp1]Die "
     "Anspruchsgrundlage ist Paragraf vierhundertsiebenunddreißig Nummer eins mit Paragraf vierhundertneununddreißig "
     "Absatz drei, ein Verschulden brauchst du nicht. [tipp2]Und prüfe die geltende Fassung: Es kommt darauf an, ob der "
     "Mangel vor dem Einbau offenbar war.", PS),
    # --- I Klausurschema ----------------------------------------------------------------------------------------------
    ("[sch]Dein Schema: [k1]Römisch eins: Kaufvertrag und Sachmangel bei Gefahrübergang. [k2]Römisch zwei: Einbau "
     "gemäß Art und Verwendungszweck, bevor der Mangel offenbar wurde. [k3]Römisch drei: erforderliche Aufwendungen für "
     "Entfernen und Einbau. [k4]Römisch vier: keine berechtigte Verweigerung nach Absatz vier.", PS),
    # --- J Merksatz (Lexi) --------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer mangelhafte Ware bestimmungsgemäß einbaut, bevor der Mangel offenbar wird, [mk2]bekommt Ausbau und Einbau im "
     "Rahmen der Nacherfüllung ersetzt, auch ohne Verschulden des Verkäufers.", 1.4),
]
