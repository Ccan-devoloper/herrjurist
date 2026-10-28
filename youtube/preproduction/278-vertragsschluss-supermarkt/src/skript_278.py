"""Folge 278 · Vertragsschluss Supermarkt: Wann kaufst du die Milch? (Mi · Examenswissen · BGB AT · Streitstand;
§§ 145, 433, 280 I, 241 II BGB; zusätzlich § 311 Abs. 2 Nr. 2, § 276 Abs. 2, § 823 Abs. 1 BGB, § 9 Abs. 1 JuSchG).
Beispielfall nach dem Plan-Hook („Die Glasflasche rutscht dir im Gang aus der Hand – bevor du überhaupt an der Kasse
warst.“): Erhard nimmt am Dienstagabend in einem Supermarkt (fiktiv, ohne Namen oder Marke) eine kalte Glasflasche Milch
mit einer Hand aus dem Kühlregal, den Blick auf der Einkaufsliste im Handy; die beschlagene Flasche rutscht ihm aus der
Hand und zerbricht. Niemand wird verletzt. Frau Kesting (Filialleiterin) verlangt 1,49 €. Er: noch nicht gekauft.
Aufbau als Streitstand (Anknüpfung an Folge 276, dort nur angerissen): Anspruch § 433 Abs. 2 (Wortlautkarte) → Streit
nach BGHZ 66, 51, Gründe V. 1 (Ansicht 1: Auslage = Angebot, Annahme durch Vorweisen an der Kasse; Ansicht 2: Auslage =
invitatio, Angebot durch Vorweisen, Annahme durch Registrieren), Argumente je ein Satz (§ 9 Abs. 1 JuSchG) → Folge für
die Flasche: nach beiden Ansichten erst an der Kasse (BGH VIII ZR 171/10 Rn. 14 f.; BGHZ 66, 51, Gründe V. 4) → kein
Kaufpreis → § 311 Abs. 2 Nr. 2 und § 241 Abs. 2 (Wortlautkarten), § 280 Abs. 1 (Wortlautkarte, Satz 2 Vermutung),
Fahrlässigkeit, § 823 Abs. 1 mit Beweislast (BGHZ 66, 51, Gründe IV.) → Gegenrichtung Gemüseblatt-Fall (Gründe V. 1, 4;
Verweis Folge 031) → Ergebnis → Klausurtipp → Schema → Merksatz. Belege je Cue in ../RECHTSSTAND.md.
Stimmen (Pool stephan, hilde, christian, lucy): Erhard (stephan, Mann, mittel), Frau Kesting (lucy, Frau, jung);
hilde und christian nicht besetzt (Vorfolge 276: hilde/christian). Erzählerin und Lexi: Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; keine Abkürzungen (synth_el buchstabiert BGB, BGH)."""

P, PS = 0.3, 0.5

STIMMEN = {"Erhard": "stephan", "Kesting": "lucy"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: im Gang am Kühlregal ---------------------------------------------------------------------------------
    ("[fall]Die Glasflasche rutscht dir im Gang aus der Hand, bevor du überhaupt an der Kasse warst. Musst du sie bezahlen? "
     "[erh]Das fragt sich Erhard am Dienstagabend im Supermarkt. [griff]Er nimmt eine kalte Flasche Milch aus dem "
     "Kühlregal, mit einer Hand, den Blick auf der Einkaufsliste im Handy. [rutsch]Die beschlagene Flasche rutscht ihm durch "
     "die Finger [knall]und zerbricht auf dem Boden. Verletzt wird niemand.", P),
    # --- A2 Dialog -----------------------------------------------------------------------------------------------------
    ("[kest]Frau Kesting, die Filialleiterin, kommt dazu.", P),
    ("[k1]Die Flasche müssen Sie bezahlen, einen Euro neunundvierzig.", P, "Kesting"),
    ("[e1]Wieso? Gekauft habe ich sie doch noch gar nicht. An der Kasse war ich noch nicht.", P, "Erhard"),
    ("[frage]Muss Erhard die Milch bezahlen? [frage2]Wann kommt im Supermarkt überhaupt der Kaufvertrag zustande? "
     "[frage3]Und wer trägt das Risiko, solange du noch im Gang stehst?", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Anspruch § 433 Abs. 2 (Wortlautkarte), Anknüpfung an Folge 276 ------------------------------------------------
    ("[ansp]Für den Markt verlangt Frau Kesting den Kaufpreis. [w433]Paragraf vierhundertdreiunddreißig Absatz zwei: Der "
     "Käufer ist verpflichtet, dem Verkäufer den vereinbarten Kaufpreis zu zahlen. [ansp2]Das setzt einen Kaufvertrag "
     "voraus, also Angebot und Annahme nach den Paragrafen hundertfünfundvierzig folgende. [v276]Dass die Ware im "
     "Schaufenster nur eine Einladung ist, kennst du aus unserer Folge zum Schaufenster. [kern]Wie der Vertrag im "
     "Selbstbedienungsladen entsteht, ist dagegen umstritten.", P),
    # --- D Streitstand nach BGHZ 66, 51, Gründe V. 1 ---------------------------------------------------------------------
    ("[streit]Der Bundesgerichtshof hat beide Ansichten schon im Gemüseblatt-Fall beschrieben. [an1]Nach der ersten ist "
     "schon die Ware im Regal ein Angebot des Marktes an jeden. Du nimmst es an, wenn du die Ware an der Kasse vorlegst; "
     "bis dahin behältst du dir die Entscheidung vor. [arg1]Dafür spricht: Wer Ware mit Preis ins Regal stellt, will sie an "
     "jeden verkaufen, der sie zur Kasse bringt.", P),
    ("[an2]Nach der Gegenansicht, der heute überwiegenden, lädt das Regal nur ein. Das Angebot machst du selbst, wenn du "
     "die Ware an der Kasse vorlegst. [annahme]Angenommen ist es, wenn die Kassiererin den Preis registriert, also scannt "
     "oder eintippt. [arg2]Dafür spricht: Der Markt will an der Kasse noch prüfen können, etwa beim Jugendschutz. "
     "[jusch]Schnaps zum Beispiel darf er an Jugendliche nach Paragraf neun des Jugendschutzgesetzes gar nicht "
     "abgeben.", PS),
    # --- E Folge für die Flasche: nach beiden Ansichten erst an der Kasse ------------------------------------------------
    ("[beide]Für die Flasche von Erhard kann der Streit offenbleiben. Nach beiden Ansichten kommt der Kaufvertrag erst an der "
     "Kasse zustande. [regal]Das Herausnehmen aus dem Regal bindet noch nicht, so auch der Bundesgerichtshof. "
     "[kein433]Im Gang gab es also noch keinen Vertrag und damit keinen Anspruch auf den Kaufpreis. [aber]Ganz ohne "
     "Haftung ist Erhard aber nicht.", PS),
    # --- F1 § 311 Abs. 2 Nr. 2, § 241 Abs. 2 (Wortlautkarten) -----------------------------------------------------------
    ("[w311]Ein Schuldverhältnis entsteht schon durch die Anbahnung eines Vertrags, bei der der eine Teil dem anderen die "
     "Möglichkeit zur Einwirkung auf seine Rechtsgüter gewährt. So steht es in Paragraf dreihundertelf Absatz zwei. "
     "[anb]Genau das tut der Markt: Er lässt Erhard die Ware selbst in die Hand nehmen. [w241]Und Paragraf "
     "zweihunderteinundvierzig Absatz zwei verpflichtet jeden Teil zur Rücksicht auf die Rechte, Rechtsgüter und "
     "Interessen des anderen Teils. [pfl]Also auch den Kunden: Er muss mit fremder Ware sorgfältig umgehen. [v010]Die "
     "Grundlagen zeigt unsere Folge zur culpa in contrahendo.", P),
    # --- F2 § 280 Abs. 1 (Wortlautkarte), Vermutung, Fahrlässigkeit, § 823 Abs. 1 mit Beweislast -------------------------
    ("[w280]Anspruchsgrundlage ist Paragraf zweihundertachtzig Absatz eins: Verletzt der Schuldner eine Pflicht aus dem "
     "Schuldverhältnis, so kann der Gläubiger Ersatz des hierdurch entstehenden Schadens verlangen. [vm]Dies gilt nicht, wenn der Schuldner die "
     "Pflichtverletzung nicht zu vertreten hat. Das Vertretenmüssen wird also vermutet: Erhard muss sich entlasten. "
     "[fahr]Eine nasse Glasflasche mit einer Hand zu tragen und dabei aufs Handy zu schauen, ist fahrlässig. "
     "[anders]Hätte ihn ein anderer Kunde angerempelt, könnte das Verschulden fehlen; das müsste Erhard aber beweisen.", P),
    ("[d823]Daneben haftet er nach Paragraf achthundertdreiundzwanzig, weil er fahrlässig fremdes Eigentum verletzt hat. Dort muss "
     "aber der Markt sein Verschulden beweisen. [beweis]Diesen Beweisvorteil der culpa in contrahendo gegenüber dem Delikt "
     "hat der Bundesgerichtshof schon im Gemüseblatt-Fall hervorgehoben, damals noch nach altem Recht.", PS),
    # --- G Gegenrichtung: Schutzpflichten des Ladens (Gemüseblatt-Fall) -------------------------------------------------
    ("[gegen]Die Rücksichtspflicht gilt auch umgekehrt. [gb]Im Gemüseblatt-Fall rutschte ein Mädchen in der Kassenzone auf "
     "einem Gemüseblatt aus. [mutter]Wäre ihre Mutter gestürzt, hätte der Laden nach dem Bundesgerichtshof aus culpa in "
     "contrahendo gehaftet, obwohl der Kaufvertrag noch nicht geschlossen war. [v031]Wie das Kind selbst geschützt ist, "
     "zeigt unsere Folge zum Gemüseblatt-Fall.", PS),
    # --- H Ergebnis --------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Den Kaufpreis schuldet Erhard nicht, denn ein Kaufvertrag kam nie zustande. [erg2]Den Schaden an der "
     "Flasche muss er aber ersetzen, aus culpa in contrahendo und aus Delikt. [erg3]Er zahlt also nicht als Käufer, "
     "sondern als Schädiger.", PS),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Entscheide einen Streit nur, wenn es darauf ankommt. [tipp2]Kommen beide Ansichten zum selben "
     "Ergebnis, stellst du sie kurz dar und lässt ihn offen, wie der Bundesgerichtshof im Gemüseblatt-Fall. [tipp3]Und "
     "scheitert der Kaufpreis, prüfe weiter: culpa in contrahendo und Delikt.", PS),
    # --- L Prüfungsschema --------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfungsschema: Markt gegen Erhard. [s1]Römisch eins: Kaufpreis aus Paragraf vierhundertdreiunddreißig "
     "Absatz zwei. [s1a]Vertragsschluss im Selbstbedienungsladen umstritten, [s1b]nach beiden Ansichten erst an der Kasse, "
     "[s1c]also kein Vertrag und kein Kaufpreis. [s2]Römisch zwei: Schadensersatz aus culpa in contrahendo. "
     "[s2a]Schuldverhältnis durch Anbahnung, [s2b]Pflichtverletzung, [s2c]vermutetes Vertretenmüssen, [s2d]Schaden. "
     "[s3]Römisch drei: Delikt, dort beweist der Markt das Verschulden.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------
    ("[merke]Merke: Im Supermarkt kaufst du erst an der Kasse. [merk2]Bis dahin schuldest du keinen Kaufpreis, aber "
     "Rücksicht auf die Ware, und für verschuldete Schäden haftest du schon im Gang.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    assert not re.search(r"\bBGB\b|\bBGH\b|\d|§", text), "Abkürzung oder Ziffer im Sprechtext"
    assert not re.search(r"\b(Erhards|Kestings)\b", text), "Genitiv eines Namens"
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
