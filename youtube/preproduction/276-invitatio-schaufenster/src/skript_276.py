"""Folge 276 · Invitatio ad offerendum: Ist der Preis im Schaufenster ein Angebot? (Fr · Klausurpraxis · BGB AT · Abgrenzung;
§§ 145, 133, 157 BGB; zusätzlich §§ 146, 433 Abs. 1 Satz 1 BGB, §§ 10, 20 PAngV).
Beispielfall nach dem Plan-Hook („Im Schaufenster hängt die Jacke für 20 statt 200 Euro – musst du sie zu dem Preis
bekommen?“): Edelgard sieht am Samstagvormittag im Schaufenster eines kleinen Modegeschäfts (fiktiv, ohne Namen oder Marke)
eine Wolljacke mit dem Preisschild 20 €; gemeint waren 200 €, beim Beschriften fehlte eine Null. Sie verlangt im Laden von
Herrn Böckmann (Inhaber) die Jacke für 20 €; er lehnt ab. Aufbau als Abgrenzung: Anspruch § 433 Abs. 1 Satz 1 → § 145
(Wortlautkarte), Rechtsbindungswille → §§ 133, 157 (Wortlautkarten) → Schaufenster/Katalog/Prospekt = invitatio (h. M.;
Gründe nach BGH 1 StR 146/17 Rn. 21) → Angebot der Kundin, Ablehnung, § 146 → Abgrenzung Selbstbedienungsladen (Streit,
BGH VIII ZR 171/10 Rn. 14 f.), SB-Tankstelle (Rn. 13, 16), Warenautomat (überwiegende Ansicht), Onlineshop (Folge 251),
Sofort kaufen (Folge 255) → Ergebnis, Preisangabenrecht ein Satz → Klausurtipp → Schema → Merksatz.
Belege je Cue in ../RECHTSSTAND.md.
Stimmen (Pool stephan, hilde, christian, lucy): Edelgard (hilde, Frau, älter), Herr Böckmann (christian, Mann, mittel);
stephan und lucy nicht besetzt. Erzählerin und Lexi: Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; keine Abkürzungen (synth_el buchstabiert BGB, BGH)."""

P, PS = 0.3, 0.5

STIMMEN = {"Edelgard": "hilde", "Boeckmann": "christian"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: vor dem Schaufenster -----------------------------------------------------------------------------
    ("[fall]Stell dir vor: Im Schaufenster hängt eine Jacke, und auf dem Schild steht zwanzig Euro statt zweihundert. "
     "Bekommst du sie zu dem Preis? [edel]Genau das passiert Edelgard am Samstagvormittag vor einem kleinen Modegeschäft. "
     "[schild]Auf dem Preisschild der Wolljacke stehen zwanzig Euro. [null]Gemeint waren zweihundert; beim Beschriften ist "
     "eine Null verloren gegangen.", P),
    # --- A2 Im Laden: Dialog ---------------------------------------------------------------------------------------
    ("[laden]Edelgard geht hinein, zu Herrn Böckmann, dem Inhaber.", P),
    ("[e1]Ich nehme die Jacke aus dem Schaufenster, für zwanzig Euro.", P, "Edelgard"),
    ("[b1]Das tut mir leid, auf dem Schild fehlt eine Null. Die Jacke kostet zweihundert Euro.", P, "Boeckmann"),
    ("[e2]Im Schaufenster steht zwanzig. Das ist Ihr Angebot, und ich nehme es an.", P, "Edelgard"),
    ("[frage]Muss Herr Böckmann ihr die Jacke für zwanzig Euro verkaufen? [frage2]War das Preisschild im Schaufenster schon "
     "ein Angebot? [frage3]Oder nur eine Einladung, selbst eines zu machen?", PS),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Anspruch ------------------------------------------------------------------------------------------------
    ("[ansp]Edelgard verlangt von Herrn Böckmann Übergabe und Übereignung der Jacke für zwanzig Euro, nach Paragraf "
     "vierhundertdreiunddreißig Absatz eins. [ansp2]Dafür braucht sie einen Kaufvertrag, also Angebot und Annahme. "
     "[v014]Wie beide zusammenpassen müssen, zeigt unsere Folge zu Angebot und Annahme. [kern]Hier geht es um die Frage "
     "davor: Wer hat überhaupt das Angebot gemacht?", P),
    # --- D1 § 145 BGB (Wortlautkarte), Rechtsbindungswille (BGH III ZR 220/25 Rn. 13) -------------------------------
    ("[w145]Paragraf hundertfünfundvierzig sagt: Wer einem anderen die Schließung eines Vertrags anträgt, ist an den Antrag "
     "gebunden, es sei denn, dass er die Gebundenheit ausgeschlossen hat. [rbw]Ein Angebot ist also eine Erklärung, mit der "
     "sich jemand schon binden will. Dieser Rechtsbindungswille ist das entscheidende Merkmal. [inv]Fehlt er, liegt nach dem "
     "Bundesgerichtshof nur eine Aufforderung vor, selbst ein Angebot abzugeben: eine invitatio ad offerendum.", P),
    # --- D2 Auslegung §§ 133, 157 BGB (Wortlautkarten), Empfängerhorizont (VIII ZR 79/04 S. 6) ------------------------
    ("[w133]Ob jemand sich binden will, klärst du durch Auslegung. Paragraf hundertdreiunddreißig: Bei der Auslegung einer "
     "Willenserklärung ist der wirkliche Wille zu erforschen und nicht an dem buchstäblichen Sinne des Ausdrucks zu haften. "
     "[w157]Und Paragraf hundertsiebenundfünfzig: Verträge sind so auszulegen, wie Treu und Glauben mit Rücksicht auf die "
     "Verkehrssitte es erfordern. [horiz]Es kommt also darauf an, wie ein verständiger Passant das Preisschild verstehen "
     "darf.", P),
    # --- E Schaufenster = invitatio (h. M.); Gründe (1 StR 146/17 Rn. 21); Werbung (III ZR 220/25, III ZR 62/11) -------
    ("[schauf]Und da gilt nach herrschender Meinung: Die Ware im Schaufenster ist kein Angebot, sondern nur eine Einladung. "
     "[gruende]Der Bundesgerichtshof begründet das für Angebote an die Allgemeinheit: Der Händler will vorher prüfen, ob er "
     "überhaupt liefern kann [bonit]und ob sein Kunde zahlen kann. [mehr]Außerdem weiß er nicht, wie viele Leute kommen. "
     "Wäre das Schild ein Angebot, könnten zehn Kunden dieselbe Jacke annehmen, und Herr Böckmann wäre zehnmal gebunden. "
     "[katalog]Dasselbe gilt für Katalog und Prospekt; für Werbeschreiben und Anzeigen hat der Bundesgerichtshof das "
     "ausdrücklich so gesehen.", P),
    # --- F Angebot der Kundin, Ablehnung, § 146 -------------------------------------------------------------------
    ("[edang]Das Angebot macht also erst Edelgard, mit ihrem Satz: Ich nehme die Jacke für zwanzig Euro. [frei]Ob er es "
     "annimmt, entscheidet Herr Böckmann. Er lehnt ab, und damit erlischt ihr Angebot nach Paragraf hundertsechsundvierzig. "
     "[leer]Ihr Satz, sie nehme sein Angebot an, geht ins Leere: Es gab keins.", PS),
    # --- G1 Abgrenzung: Selbstbedienungsladen (Streit), SB-Tankstelle (BGH VIII ZR 171/10 Rn. 13–16) -------------------
    ("[abgr]Grenze das in der Klausur sauber ab. [sb]Im Selbstbedienungsladen bindet das Herausnehmen aus dem Regal noch "
     "nicht; die Ware kann zurück ins Regal, so der Bundesgerichtshof. [sb1]Wie der Vertrag an der Kasse entsteht, ist "
     "umstritten. Nach einer Ansicht ist schon die Ware im Regal das Angebot, und du nimmst es an, wenn du sie an der Kasse "
     "vorlegst. [sb2]Nach der Gegenansicht lädt auch das Regal nur ein: Du bietest an der Kasse an, und die Kassiererin "
     "nimmt an. [tank]Anders an der Selbstbedienungstankstelle: Dort kommt der Kauf nach dem Bundesgerichtshof schon beim "
     "Tanken zustande, weil sich das Einfüllen praktisch nicht rückgängig machen lässt.", P),
    # --- G2 Abgrenzung: Warenautomat, Onlineshop (Folge 251), Sofort kaufen (Folge 255) ---------------------------------
    ("[auto]Beim Warenautomaten sieht die überwiegende Ansicht schon im Aufstellen ein Angebot an jeden, solange Ware da ist "
     "und der Automat funktioniert. [shop]Der Onlineshop ist wieder nur Einladung; das Angebot ist deine Bestellung, wie in "
     "unserer Folge zum Preisfehler im Onlineshop. [platt]Bei Sofort kaufen auf einer Plattform bietet dagegen der "
     "Verkäufer selbst zu einem festen Preis an; das zeigt unsere Folge zum Sofortkauf.", PS),
    # --- H Ergebnis; Preisangabenrecht (§§ 10, 20 PAngV) ------------------------------------------------------------
    ("[erg]Ergebnis: Das Preisschild im Schaufenster war kein Angebot. [erg2]Herr Böckmann musste ihr Angebot nicht "
     "annehmen. Ohne Kaufvertrag hat Edelgard keinen Anspruch auf die Jacke für zwanzig Euro. [pangv]Ein falsches "
     "Preisschild kann zwar gegen die Preisangabenverordnung verstoßen; einen Kaufvertrag zu zwanzig Euro macht das aber "
     "nicht.", PS),
    # --- I Klausurtipp (Lexi) ---------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Spring bei einem falschen Preis nicht sofort zur Anfechtung. [tipp2]Prüfe zuerst, wer das Angebot "
     "gemacht hat. War das Preisschild nur eine Einladung, hat der Händler noch nichts erklärt, was er anfechten müsste. "
     "[tipp3]Und begründe die Einladung mit dem fehlenden Rechtsbindungswillen, nicht bloß mit dem Wort Schaufenster.", PS),
    # --- L Prüfungsschema -------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfungsschema: Edelgard gegen Herrn Böckmann auf Übergabe und Übereignung der Jacke. [s1]Römisch eins: "
     "Kaufvertrag. [s1a]Angebot durch das Schaufenster? Nein, nur eine invitatio ad offerendum, denn es fehlt der "
     "Rechtsbindungswille, [s1b]Auslegung nach den Paragrafen hundertdreiunddreißig und hundertsiebenundfünfzig. "
     "[s1c]Angebot erst durch Edelgard im Laden, [s1d]keine Annahme, Herr Böckmann lehnt ab. [s2]Römisch zwei: Ergebnis, "
     "kein Anspruch.", PS),
    # --- M Merksatz (Lexi) ------------------------------------------------------------------------------------------
    ("[merke]Merke: Ware im Schaufenster, im Katalog oder im Prospekt ist in der Regel kein Angebot, sondern eine Einladung, eines "
     "abzugeben. [merk2]Das Angebot macht der Kunde, und ob er es annimmt, entscheidet der Händler.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    assert not re.search(r"\bBGB\b|\bBGH\b|\d|§", text), "Abkürzung oder Ziffer im Sprechtext"
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
