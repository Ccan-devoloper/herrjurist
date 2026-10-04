"""Folge 138 · EU-Rechtsakte Art. 288 AEUV: Verordnung, Richtlinie, Beschluss (Fr · Klausurpraxis · Öffentliches Recht/
Europarecht, Format Schema). Hook nach dem Plan („Die DSGVO galt sofort überall, die Pauschalreiserichtlinie brauchte erst
ein deutsches Gesetz – warum?“) als fiktive Mini-Szene: Herr Stegemann (kleines Reisebüro, stellt Pauschalreisen zusammen)
und Frau Kettner (seine Datenschutzbeauftragte). Kern als Schema/Übersicht:
1. Primär- und Sekundärrecht (Art. 1 Abs. 3 EUV, Art. 1 Abs. 2 AEUV),
2. Art. 288 AEUV als Wortlautkarte (Abs. 2–5, vorgelesen; Abs. 1 als Aufzählung): Verordnung (DSGVO Art. 99 Abs. 2;
   BDSG § 1 Abs. 5, ErwG 10 DSGVO), Richtlinie (RL (EU) 2015/2302 Art. 28; §§ 651a ff. BGB, Art. 229 § 42 EGBGB;
   BT-Drs. 18/10822), Beschluss (Art. 108 Abs. 2 AEUV), Empfehlung/Stellungnahme,
3. nicht umgesetzte Richtlinien: vertikale unmittelbare Wirkung (Ratti Rn. 22 f., 43; Becker Rn. 24 f.), keine horizontale
   (Faccini Dori Rn. 3, 8, 20, 25), richtlinienkonforme Auslegung (Faccini Dori Rn. 26), Staatshaftung (Francovich
   Rn. 39 f.; Dillenkofer Rn. 10 f., 29),
4. Ergebnis → Klausurtipp (Lexi) → Klausurschema als Tabelle → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Keine echten Personen als Figuren; Frau Faccini Dori nur als Fallname.
Figuren: Herr Stegemann (william), Frau Kettner (sabrina); Lexi/Erzählerin Carla. Namen nicht im Genitiv.
Abkürzungen im Sprechtext ausgeschrieben (Datenschutz-Grundverordnung, Vertrag über die Arbeitsweise der Union); „BGB“
buchstabiert synth_el selbst. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor. Zahlen im Sprechtext als Wörter."""

P, PS = 0.3, 0.55

STIMMEN = {"Stegemann": "william", "Kettner": "sabrina"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: das Reisebüro --------------------------------------------------------------------------------------------
    ("[fall]Herr Stegemann führt ein kleines Reisebüro und stellt dort auch Pauschalreisen zusammen. [kett]Frau Kettner ist "
     "seine Datenschutzbeauftragte. [ordner]Heute bringt sie einen Ordner mit.", 0.3),
    ("[k1]Für Ihre Kundendaten gilt die Datenschutz-Grundverordnung. Sie gilt hier unmittelbar, wie in jedem Mitgliedstaat.",
     0.3, "Kettner"),
    ("[s1]Und warum steht mein Pauschalreiserecht dann im BGB und nicht in der EU-Richtlinie?", 0.4, "Stegemann"),
    ("[frage]Beides kommt aus der EU. [dsg]Die Datenschutz-Grundverordnung galt ab dem fünfundzwanzigsten Mai "
     "zweitausendachtzehn unmittelbar in allen Mitgliedstaaten. [prl]Die Pauschalreiserichtlinie brauchte dagegen erst ein "
     "deutsches Gesetz. [warum]Warum?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Primär- und Sekundärrecht ---------------------------------------------------------------------------------------
    ("[ebene]Zuerst die Ebenen. [prim]Zum Primärrecht gehören vor allem die Verträge selbst: der EU-Vertrag und der Vertrag über die "
     "Arbeitsweise der Union. [sek]Sekundärrecht erlassen die Organe der Union auf ihrer Grundlage. [formen]Welche Formen es "
     "dafür gibt, sagt Artikel zweihundertachtundachtzig.", PS),
    # --- D Wortlautkarte Art. 288 AEUV ------------------------------------------------------------------------------------
    ("[abs1]Absatz eins nennt fünf Handlungsformen: [h1]Verordnungen, [h2]Richtlinien, [h3]Beschlüsse, [h4]Empfehlungen und "
     "[h5]Stellungnahmen. [abs2]Absatz zwei: Die Verordnung hat allgemeine Geltung. Sie ist in allen ihren Teilen verbindlich "
     "und gilt unmittelbar in jedem Mitgliedstaat. [abs3]Absatz drei: Die Richtlinie ist für jeden Mitgliedstaat, an den sie "
     "gerichtet wird, hinsichtlich des zu erreichenden Ziels verbindlich, überlässt jedoch den innerstaatlichen Stellen die "
     "Wahl der Form und der Mittel. [abs4]Absatz vier: Beschlüsse sind in allen ihren Teilen verbindlich. Sind sie an "
     "bestimmte Adressaten gerichtet, so sind sie nur für diese verbindlich. [abs5]Und Absatz fünf: Die Empfehlungen und "
     "Stellungnahmen sind nicht verbindlich.", PS),
    # --- E Verordnung -----------------------------------------------------------------------------------------------------
    ("[vo]Die Verordnung wirkt also wie ein Gesetz in allen Mitgliedstaaten zugleich: allgemein, vollständig und unmittelbar. "
     "[vo2]Genau so steht es am Ende der Datenschutz-Grundverordnung: in allen ihren Teilen verbindlich, unmittelbar in "
     "jedem Mitgliedstaat. [bdsg]Das Bundesdatenschutzgesetz setzt sie "
     "nicht um. Es ergänzt sie nur, wo sie Spielraum lässt, und tritt zurück, soweit sie unmittelbar gilt.", PS),
    # --- F Richtlinie -----------------------------------------------------------------------------------------------------
    ("[rl]Die Richtlinie dagegen richtet sich an die Mitgliedstaaten. Verbindlich ist nur das Ziel. [form]Wie sie es "
     "erreichen, entscheiden sie selbst, etwa durch ein Gesetz. [frist]Dafür setzt die Richtlinie eine Umsetzungsfrist. "
     "[prl2]Die Pauschalreiserichtlinie verlangte: Vorschriften erlassen bis zum ersten Januar zweitausendachtzehn, anwenden ab "
     "dem ersten Juli zweitausendachtzehn. [bgb]Deutschland hat sie im BGB umgesetzt, in den Paragrafen "
     "sechshunderteinundfünfzig a folgende.", PS),
    # --- G Beschluss, Empfehlung, Stellungnahme ---------------------------------------------------------------------------
    ("[be]Der Beschluss ist in allen Teilen verbindlich. Richtet er sich an bestimmte Adressaten, bindet er nur diese. "
     "[beih]Etwa wenn die Kommission beschließt, dass ein Staat eine mit dem Binnenmarkt unvereinbare Beihilfe aufheben oder umgestalten muss. "
     "Gebunden ist dann dieser Staat. [empf]Empfehlungen und Stellungnahmen binden dagegen niemanden.", PS),
    # --- H Nicht umgesetzte Richtlinie: vertikal ---------------------------------------------------------------------------
    ("[prob]Und wenn ein Staat eine Richtlinie nicht rechtzeitig umsetzt? [ratti]Dann kann er dem Einzelnen nach Ablauf der "
     "Frist sein eigenes Versäumnis nicht entgegenhalten, so der Gerichtshof etwa in Ratti und Becker. [genau]Ist eine Bestimmung "
     "unbedingt und hinreichend genau, kann sich der Einzelne gegenüber dem Staat unmittelbar auf sie berufen. [vert]Man "
     "spricht von vertikaler unmittelbarer Wirkung.", PS),
    # --- I Keine horizontale Wirkung, Auswege ------------------------------------------------------------------------------
    ("[horiz]Zwischen Privaten gilt das nicht. [fd]Im Fall Faccini Dori widerrief eine Verbraucherin einen Vertrag über einen "
     "Englischkurs im Fernunterricht, den sie im Mailänder Hauptbahnhof abgeschlossen hatte. Italien hatte die Richtlinie dazu nicht umgesetzt. [fd2]Der Gerichtshof: Eine Richtlinie kann nicht selbst Pflichten für einen Bürger begründen. [fd3]Gegenüber "
     "dem Unternehmen konnte sie ihr Widerrufsrecht deshalb nicht auf die Richtlinie stützen.", PS),
    ("[ausw]Zwei Auswege bleiben. [rka]Erstens die richtlinienkonforme Auslegung: Gerichte legen das nationale Recht so weit "
     "wie möglich am Wortlaut und Zweck der Richtlinie aus. [fran]Zweitens die Staatshaftung nach Francovich: Der Staat muss "
     "Schäden ersetzen, wenn die Richtlinie Rechte verleihen soll, ihr Inhalt bestimmbar ist und der Verstoß den Schaden "
     "verursacht hat. [dill]Das traf Deutschland bei der alten Pauschalreiserichtlinie: Im Fall Dillenkofer bekamen Reisende "
     "nach der Pleite ihrer Veranstalter ihr Geld nicht zurück, der Insolvenzschutz war zu spät umgesetzt. [qual]Der "
     "Gerichtshof: Wer innerhalb der Frist gar nicht umsetzt, verstößt schon dadurch qualifiziert.", PS),
    # --- J Ergebnis: zurück im Reisebüro -----------------------------------------------------------------------------------
    ("[erg]Zurück zu Herrn Stegemann. [erg1]Die Datenschutz-Grundverordnung ist eine Verordnung: Sie gilt unmittelbar und "
     "braucht kein Umsetzungsgesetz. [erg2]Die Pauschalreiserichtlinie ist eine Richtlinie: Sie bindet Deutschland nur im Ziel. "
     "[erg3]Deshalb gelten für seine Pauschalreisen die Paragrafen sechshunderteinundfünfzig a folgende BGB, ausgelegt im "
     "Licht der Richtlinie.", 0.3),
    ("[s2]Also Datenschutz direkt aus der EU, Reiserecht aus dem BGB.", PS, "Stegemann"),
    # --- K Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Beruft sich jemand auf eine Richtlinie, prüfe zuerst: Ist die Umsetzungsfrist abgelaufen? [tipp2]Ist "
     "die Bestimmung unbedingt und hinreichend genau? [tipp3]Und wer ist der Gegner, der Staat oder ein Privater? [tipp4]Ist der "
     "Gegner privat, bleiben nur die richtlinienkonforme Auslegung und die Staatshaftung.", PS),
    # --- L Klausurschema als Tabelle --------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema als Tabelle. [z1]Römisch eins, verbindlich? [z1a]Verordnung in allen Teilen, [z1b]Richtlinie nur "
     "im Ziel, [z1c]Beschluss in allen Teilen. [z2]Römisch zwei, für wen? [z2a]Verordnung allgemein, [z2b]Richtlinie für "
     "die Mitgliedstaaten, an die sie gerichtet ist, [z2c]Beschluss für seine Adressaten. [z3]Römisch drei, Umsetzung nötig? [z3a]Verordnung nein, [z3b]Richtlinie ja, innerhalb der Frist, "
     "[z3c]Beschluss nein, der Adressat muss ihn befolgen. [z4]Römisch vier, Beispiele: [z4a]"
     "Datenschutz-Grundverordnung, [z4b]Pauschalreiserichtlinie, [z4c]Beihilfebeschluss der Kommission.", PS),
    # --- M Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Verordnung gilt unmittelbar, die Richtlinie wirkt über das Umsetzungsgesetz, und der Beschluss bindet "
     "seine Adressaten. [m2]Auf eine nicht umgesetzte Richtlinie beruft sich der Bürger gegen den Staat, nicht gegen Private.",
     1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
