"""Folge 213 · Öffentliche Sicherheit im Polizeirecht: Was die Polizei schützt (Fr · Klausurpraxis · Polizei- und
Ordnungsrecht, Format Schema). Beispielfall nach dem Plan-Hook („Die Polizei schreitet ein, weil jemand Graffiti auf seine
eigene Garage sprüht – darf sie das?“), Beispielland Nordrhein-Westfalen (PolG NRW ab 13.12.2025, BauO NRW 2018 ab 01.09.2026):
Frau Schulze sprüht ein buntes Bild aus Blumen und Wellen auf das Tor ihrer eigenen Garage. Ihr Nachbar Herr Gebauer ruft die
Polizei. Herr Neumann (Polizei) fordert sie auf, sofort aufzuhören. Frau Schulze: „Das ist meine Garage.“
Aufbau (Schema mit Fall): Fall → Frage → Sachverhalt → Generalklausel § 8 I PolG NRW (Wortlaut), Merkmal öffentliche Sicherheit
→ drei Schutzgüter (BVerfGE 69, 315 [352], DFR Rn. 77; Legaldefinition § 4 Nr. 1 SächsPVDG; Regelannahme bei drohender
Straftat; öffentliche Ordnung nur abgrenzend) → Fall: 1. Rechtsordnung: § 303 II StGB (Wortlaut) verlangt eine fremde Sache;
keine Gestaltungssatzung (§ 89 I Nr. 1 BauO NRW, Fallannahme) → 2. Rechte des Einzelnen: nur eigenes Eigentum, § 903 S. 1 BGB
→ 3. Staat nicht betroffen → keine Gefahr → Gegenfall: Garage gehört der Vermieterin Frau Dietz → § 303 II → Gefahr →
Subsidiarität beim Schutz privater Rechte, § 1 II PolG NRW (Wortlaut; Beispiel: Kreide, nur vorübergehend) → Länder-Overlay
(NRW, Brandenburg, Sachsen – nur am Landesportal geprüfte Normen) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben und reserviert (namen_reserviert.txt): Schulze, Neumann, Gebauer, Dietz.
Stimmen (Pool william, sabrina, marc, laura_ruhig): Frau Schulze sabrina, Herr Neumann marc, Herr Gebauer william,
Frau Dietz laura_ruhig. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal (per Assertion geprüft). Zahlen und Paragrafen im Sprechtext als Wörter."""
import re as _re

P, PS = 0.3, 0.5

STIMMEN = {"Schulze": "sabrina", "Neumann": "marc", "Gebauer": "william", "Dietz": "laura_ruhig"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall: das Garagentor -------------------------------------------------------------------------------------------
    ("[fall]Samstagvormittag in einer Wohnstraße in Nordrhein-Westfalen. [spruehen]Frau Schulze sprüht ein buntes Bild auf "
     "das Tor ihrer Garage: [blumen]große Blumen und Wellen. [gebauer]Ihr Nachbar Herr Gebauer sieht das und greift zum "
     "Telefon.", P),
    ("[ge1]Hier beschmiert jemand eine Garage. Kommen Sie bitte schnell!", P, "Gebauer"),
    # --- B Fall: die Polizei kommt ----------------------------------------------------------------------------------------
    ("[neumann]Kurz darauf hält ein Streifenwagen. Herr Neumann von der Polizei steigt aus.", 0.2),
    ("[ne1]Hören Sie bitte sofort mit dem Sprühen auf.", P, "Neumann"),
    ("[sc1]Warum? Das ist meine Garage. Ich darf sie bemalen, wie ich will.", 0.4, "Schulze"),
    ("[frage]Darf die Polizei hier einschreiten?", 0.6),
    # --- C Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D Generalklausel, Merkmal öffentliche Sicherheit -------------------------------------------------------------------
    ("[gk]Für die Aufforderung, aufzuhören, gibt es keine Standardmaßnahme. Grundlage ist die Generalklausel. [land]Polizeirecht "
     "ist Landesrecht. Wir nehmen Nordrhein-Westfalen als Beispiel; die anderen Länder haben ähnliche Regeln, oft unter anderer "
     "Nummer. [wl8]Paragraf acht des Polizeigesetzes: Die Polizei kann die notwendigen Maßnahmen treffen, um eine konkrete "
     "Gefahr für die öffentliche Sicherheit oder Ordnung abzuwehren. [merkmal]Entscheidend ist hier die öffentliche Sicherheit. "
     "Was schützt sie überhaupt?", PS),
    # --- E Drei Schutzgüter ----------------------------------------------------------------------------------------------
    ("[drei]Die öffentliche Sicherheit hat drei Schutzgüter. [s1]Erstens die Unverletzlichkeit der objektiven Rechtsordnung. "
     "[s2]Zweitens die subjektiven Rechte und Rechtsgüter des Einzelnen, etwa Leben, Gesundheit, "
     "Freiheit, Ehre, Eigentum und Vermögen. [s3]Drittens Bestand und Funktionsfähigkeit des Staates und seiner Einrichtungen. "
     "[bverfg]Diese Schutzgüter nennt auch das Bundesverfassungsgericht im Brokdorf-Beschluss. [sachsen]Sachsen hat diese Definition sogar "
     "ins Gesetz geschrieben. [regel]Und in der Regel ist die öffentliche Sicherheit gefährdet, wenn eine strafbare Verletzung "
     "dieser Schutzgüter droht. [ordnung]Davon zu trennen ist die öffentliche Ordnung: ungeschriebene Regeln, die nach "
     "herrschender Anschauung für ein geordnetes Zusammenleben unerlässlich sind.", PS),
    # --- F Fall: 1. Rechtsordnung ----------------------------------------------------------------------------------------
    ("[pr1]Jetzt zum Fall, zuerst die Rechtsordnung. Herr Gebauer denkt an Sachbeschädigung. [wl303]Paragraf dreihundertdrei "
     "Absatz zwei des Strafgesetzbuchs: Bestraft wird, wer unbefugt das Erscheinungsbild einer fremden Sache nicht nur "
     "unerheblich und nicht nur vorübergehend verändert. [dauer]Das Bild ist groß und hält dauerhaft. [fremd]Aber die Sache muss "
     "fremd sein, und die Garage gehört Frau Schulze. [keine]Also keine Straftat. [satzung]Gemeinden können zwar per Satzung "
     "Anforderungen an die äußere Gestaltung stellen. Frau Schulzes Gemeinde hat das nicht getan. [rok]Die Rechtsordnung ist "
     "nicht verletzt.", PS),
    # --- G Fall: 2. Rechte des Einzelnen, 3. Staat, Ergebnis ---------------------------------------------------------------
    ("[pr2]Zweitens, die Rechte des Einzelnen. [eigen]Betroffen ist nur das Eigentum von Frau Schulze selbst. [p903]Und nach "
     "Paragraf neunhundertdrei des Bürgerlichen Gesetzbuchs kann der Eigentümer mit seiner Sache nach Belieben verfahren, "
     "soweit nicht das Gesetz oder Rechte Dritter entgegenstehen. [geschmack]Dass Herrn Gebauer die Farben nicht gefallen, "
     "verletzt kein Recht. [pr3]Drittens, der Staat: Keine staatliche Einrichtung ist betroffen. [oo]Und ein buntes Bild auf der "
     "eigenen Garage verstößt auch gegen keine ungeschriebene Regel, die für das Zusammenleben unerlässlich wäre. "
     "[erg]Ergebnis: Es fehlt eine Gefahr. Herr Neumann darf nicht einschreiten.", PS),
    # --- H Gegenfall: Mietgarage ----------------------------------------------------------------------------------------
    ("[gegen]Jetzt der Gegenfall: Frau Schulze hat die Garage nur gemietet. Eigentümerin ist ihre Vermieterin, Frau Dietz.", 0.2),
    ("[di1]Das ist meine Garage. Davon war nie die Rede!", P, "Dietz"),
    ("[gfremd]Dann ist die Garage für Frau Schulze eine fremde Sache. Sie verändert ihr Erscheinungsbild ohne Erlaubnis, "
     "deutlich und dauerhaft. [g303]Das ist eine Sachbeschädigung nach Paragraf dreihundertdrei Absatz zwei. [gschutz]Verletzt "
     "sind die Rechtsordnung und das Eigentum von Frau Dietz. [ggefahr]Mit jedem weiteren Sprühstoß wächst der Schaden: Eine "
     "konkrete Gefahr liegt vor. [gdarf]Herr Neumann darf einschreiten.", PS),
    # --- I Subsidiarität beim Schutz privater Rechte -----------------------------------------------------------------------
    ("[subs]Und wenn nur private Rechte betroffen sind? [kreide]Angenommen, Frau Schulze malt mit Kreide, die der nächste Regen "
     "abwäscht. Dann verändert sie das Erscheinungsbild nur vorübergehend, Paragraf dreihundertdrei scheidet aus. [privat]Es "
     "bleiben die Rechte von Frau Dietz aus Mietvertrag und Eigentum, also private Rechte. [wl12]Für sie gilt Paragraf eins "
     "Absatz zwei: Der Schutz privater Rechte obliegt der Polizei nur dann, wenn gerichtlicher Schutz nicht rechtzeitig zu "
     "erlangen ist und wenn ohne polizeiliche Hilfe die Verwirklichung des Rechts vereitelt oder wesentlich erschwert werden "
     "würde. [kgericht]Kreide lässt sich abwaschen, und Frau Dietz kann ihre Rechte vor Gericht durchsetzen. Ein Fall für die "
     "Polizei ist das nicht. [straf]Droht dagegen eine Straftat, schützt die Polizei zugleich die Rechtsordnung. Dann sperrt "
     "diese Klausel nicht.", PS),
    # --- J Länder-Overlay ------------------------------------------------------------------------------------------------
    ("[tab]Ein Blick in drei Länder. [tnrw]In Nordrhein-Westfalen steht die Generalklausel in Paragraf acht, der Schutz privater "
     "Rechte in Paragraf eins Absatz zwei. [tbb]Brandenburg hat Paragraf zehn und ebenfalls Paragraf eins Absatz zwei. [tsn]Sachsen "
     "hat Paragraf zwölf und Paragraf zwei Absatz zwei. Dort braucht es für den Schutz privater Rechte zusätzlich einen "
     "Antrag der berechtigten Person. [teigen]Schlag die Nummern in deinem Landesgesetz nach.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst die Rechtsordnung, vor allem Straf- und Bußgeldnormen. [tipp2]Lies dabei jedes Merkmal "
     "genau. Bei der Sachbeschädigung entscheidet oft das Wort fremd. [tipp3]Bleiben nur private Rechte übrig, sprich die "
     "Subsidiaritätsklausel an.", PS),
    # --- L Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema für die öffentliche Sicherheit. [q1]Eins, Unverletzlichkeit der Rechtsordnung: Verstößt das "
     "Verhalten gegen ein Gesetz? [q2]Zwei, Rechte und Rechtsgüter des Einzelnen: Wessen Recht ist betroffen? [q3]Drei, Bestand "
     "und Funktionsfähigkeit des Staates. [q4]Vier, bei rein privaten Rechten die Subsidiarität: Gerichtsschutz nicht rechtzeitig, "
     "Recht sonst vereitelt. [q5]Fünf, Ergebnis: Gefahr für die öffentliche Sicherheit, ja oder nein.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Die öffentliche Sicherheit schützt die Rechtsordnung, die Rechte des Einzelnen und den Staat. [m2]Die eigene "
     "Garage zu bemalen, ist kein Fall für die Polizei, solange kein Gesetz es verbietet. [m3]Und private Rechte schützt sie nur, "
     "wenn gerichtliche Hilfe zu spät käme.", 1.4),
]

_alle = [m for s in SEGMENTE for m in _re.findall(r"\[(\w+)\]", s[0])]
assert len(_alle) == len(set(_alle)), f"Marke doppelt: {[m for m in _alle if _alle.count(m) > 1]}"
assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)

if __name__ == "__main__":
    txt = [_re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE]
    print(len(SEGMENTE), "Segmente,", len(_alle), "Marken,", sum(len(t) for t in txt), "Zeichen")
