"""Folge 251 · Preisfehler Onlineshop: Muss der Händler liefern? (§ 119 BGB) (Mi · Examenswissen · BGB AT · Alltagsfall;
§§ 119 Abs. 1, 120, 121, 122, 142 Abs. 1, 312i Abs. 1 Satz 1 Nr. 3 BGB).
Beispielfall nach dem Plan-Hook („Der Fernseher steht im Shop für 49 statt 499 Euro – du bestellst sofort und bekommst eine
Bestätigungsmail“), Sachverhalt angelehnt an BGH, Urt. v. 26.1.2005 – VIII ZR 79/04 (Datentransferfehler der Software):
Frau Wetzel gibt 499 € in ihr System ein, die Software überträgt 49 € in den Shop. Herr Kübler bestellt am Montagabend,
bekommt sofort eine automatische Eingangsbestätigung („Vielen Dank, wir haben Ihre Bestellung erhalten.“) und am
Dienstagmorgen eine zweite automatische Mail („Ihr Auftrag wird jetzt von unserer Versandabteilung bearbeitet.“, Wortlaut
wie im BGH-Fall). Am Dienstagmittag bemerkt Frau Wetzel den Fehler und ficht telefonisch an.
Belege je Cue in ../RECHTSSTAND.md: VIII ZR 79/04 (Volltext bundesgerichtshof.de, ohne Randnummern: S. 5–9, Abschnitt II A);
X ZR 37/12 Rn. 13, 14, 17, 19 (Eingangsbestätigung in der Regel reine Wissenserklärung, Annahme bei angekündigter
vorbehaltloser Ausführung, automatisierte Erklärungen).
Stimmen (Pool william, sabrina, marc, laura_ruhig): Herr Kübler (marc, Mann, mittel), Frau Wetzel (sabrina, Frau, mittel);
william und laura_ruhig nicht besetzt. Erzählerin und Lexi: Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; keine Abkürzungen (synth_el buchstabiert BGB, BGH)."""

P, PS = 0.3, 0.5

STIMMEN = {"Kübler": "marc", "Wetzel": "sabrina"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: Herr Kübler zu Hause am Laptop ------------------------------------------------------------------------
    ("[fall]Herr Kübler sucht einen neuen Fernseher. [shop]Im Onlineshop von Frau Wetzel kostet ein großes Gerät plötzlich "
     "nur neunundvierzig Euro. [sonst]Sonst verlangt sie vierhundertneunundneunzig. [bestellt]Am Montagabend bestellt er "
     "sofort. [mail1]Sofort kommt eine automatische E-Mail: Vielen Dank, wir haben Ihre Bestellung erhalten. "
     "[mail2]Am Dienstagmorgen folgt eine zweite: Ihr Auftrag wird jetzt von unserer Versandabteilung bearbeitet.", P),
    # --- A2 Frau Wetzel im Lager -------------------------------------------------------------------------------------
    ("[lager]Am Dienstagmittag sieht Frau Wetzel die Bestellung. [fehler]Sie hatte vierhundertneunundneunzig Euro in ihr "
     "System eingegeben, doch die Software hat den Preis falsch in den Shop übertragen. [anruf]Sie ruft Herrn Kübler "
     "sofort an.", P),
    # --- A3 Telefonat ------------------------------------------------------------------------------------------------
    ("[w1]Der Preis im Shop war ein Softwarefehler. Ich fechte den Kauf an und liefere nicht.", P, "Wetzel"),
    ("[k1]Aber ich habe zwei Bestätigungen! Ich will den Fernseher für neunundvierzig Euro.", P, "Kübler"),
    ("[frage]Muss Frau Wetzel liefern? [frage2]Ist schon die erste Mail eine Annahme? [frage3]Und darf sie sich wegen des "
     "Fehlers vom Vertrag lösen?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Anspruch und Aufbau ---------------------------------------------------------------------------------------
    ("[ansp]Herr Kübler verlangt Lieferung, also Übergabe und Übereignung nach Paragraf vierhundertdreiunddreißig Absatz "
     "eins. [aufbau]Du prüfst zwei Stufen: Ist ein Kaufvertrag zustande gekommen? [aufbau2]Und ist er durch Anfechtung "
     "wieder weggefallen?", P),
    # --- D I. Vertragsschluss: invitatio, Bestellung = Angebot (VIII ZR 79/04 S. 5; X ZR 37/12 Rn. 14) -----------------
    ("[inv]Römisch eins: der Vertragsschluss. Der Fernseher im Shop ist nach dem Bundesgerichtshof noch kein Angebot, "
     "sondern nur eine Einladung, selbst eines abzugeben. [v014]Wie das genau funktioniert, zeigt unsere Folge zu Angebot "
     "und Annahme. [best]Das Angebot macht also Herr Kübler mit seiner Bestellung.", P),
    # --- D Eingangsbestätigung (Wortlautkarte § 312i Abs. 1 Satz 1 Nr. 3; X ZR 37/12 Rn. 19) ---------------------------
    ("[w312]Die erste Mail schreibt das Gesetz vor: Nach Paragraf dreihundertzwölf i Absatz eins Satz eins Nummer drei muss "
     "der Händler den Zugang der Bestellung unverzüglich elektronisch bestätigen. [wiss]Eine solche Bestätigung ist nach "
     "dem Bundesgerichtshof in der Regel nur eine Wissenserklärung, keine Annahme. [ausl]Was sie im Einzelfall bedeutet, "
     "zeigt die Auslegung aus Sicht des Empfängers. [erhalten]Wir haben Ihre Bestellung erhalten: Das meldet nur den "
     "Eingang.", P),
    # --- D Annahme durch die zweite Mail (VIII ZR 79/04 S. 5 f.; X ZR 37/12 Rn. 17, 19) ---------------------------------
    ("[ann]Anders die zweite Mail: Sie kündigt an, dass der Auftrag vorbehaltlos ausgeführt wird. [konkl]Das ist eine "
     "Annahme; so hat der Bundesgerichtshof eine fast gleichlautende Mail ausgelegt. [auto]Dass ein Computer sie "
     "verschickt hat, ändert nichts: Die Erklärung stammt von Frau Wetzel. [vertrag]Der Kaufvertrag ist also geschlossen, "
     "zu neunundvierzig Euro.", PS),
    # --- E II. Anfechtung: § 119 Abs. 1 (Wortlautkarte) --------------------------------------------------------------
    ("[anf]Römisch zwei: Ist der Vertrag durch Anfechtung nichtig? [w119]Nach Paragraf hundertneunzehn Absatz eins kann "
     "anfechten, wer über den Inhalt seiner Erklärung im Irrtum war oder eine Erklärung dieses Inhalts überhaupt nicht "
     "abgeben wollte. [vertippt]Wer sich vertippt, ist der klassische Fall: ein Erklärungsirrtum. [hier]Frau Wetzel hat "
     "sich aber gar nicht vertippt. Den Fehler machte die Software.", P),
    # --- F § 120 (Wortlautkarte) und BGH VIII ZR 79/04 S. 7 ------------------------------------------------------------
    ("[w120]Hier hilft der Gedanke von Paragraf hundertzwanzig: Eine Erklärung, die durch die zur Übermittlung verwendete "
     "Person oder Einrichtung unrichtig übermittelt wird, kann man anfechten wie einen Irrtum. [bgh]Der "
     "Bundesgerichtshof sagt: Es macht keinen Unterschied, ob sich jemand selbst vertippt oder ob eine unerkannt "
     "fehlerhafte Software das richtig Eingegebene auf dem Weg zum Kunden verfälscht. [bereich]Das gilt auch, wenn der "
     "Fehler noch im eigenen System passiert. Es bleibt ein Erklärungsirrtum.", P),
    # --- F Fortwirken in der Annahme, Kausalität (VIII ZR 79/04 S. 6–8) -------------------------------------------------
    ("[fort]Aber Achtung: Der falsche Preis stand zuerst nur auf der Shopseite, und die war kein Angebot. [fort2]Angefochten "
     "wird deshalb die Annahme. In ihr wirkt der Fehler fort, denn sie wurde automatisch zu neunundvierzig Euro erklärt. "
     "[kaus]Hätte Frau Wetzel den Fehler gekannt, hätte sie so nicht angenommen.", P),
    # --- G Abgrenzung Kalkulationsirrtum (VIII ZR 79/04 S. 8 f.) --------------------------------------------------------
    ("[kalk]Anders beim Kalkulationsirrtum: Hätte sie sich schon bei der Berechnung des Preises verrechnet, wäre das ein "
     "Irrtum im Beweggrund. [kalk2]Der berechtigt grundsätzlich nicht zur Anfechtung, selbst wenn eine Software falsch "
     "gerechnet hat.", PS),
    # --- H Frist § 121, Erklärung § 143, Folge § 142 Abs. 1 -----------------------------------------------------------
    ("[frist]Die Anfechtung muss nach Paragraf hunderteinundzwanzig unverzüglich erfolgen, also ohne schuldhaftes Zögern, "
     "sobald sie den Fehler kennt. [anruf2]Frau Wetzel hat noch am selben Mittag gegenüber Herrn Kübler angefochten. "
     "[p142]Damit ist der Kaufvertrag nach Paragraf hundertzweiundvierzig Absatz eins von Anfang an nichtig.", PS),
    # --- I Folge § 122 (Wortlautkarte) --------------------------------------------------------------------------------
    ("[w122]Ganz leer geht Herr Kübler aber nicht aus. Nach Paragraf hundertzweiundzwanzig muss Frau Wetzel ihm den "
     "Schaden ersetzen, den er dadurch erleidet, dass er auf die Gültigkeit der Erklärung vertraut. [vs]Das ist der "
     "Vertrauensschaden, etwa Kosten, die er im Vertrauen auf den Kauf schon hatte. [erf]Nicht ersetzt wird, was er bei "
     "Erfüllung gehabt hätte, also der günstige Fernseher. [abs2]Und kannte er den Fehler oder musste er ihn kennen, "
     "entfällt der Ersatz nach Absatz zwei ganz.", PS),
    # --- J Ergebnis ---------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Frau Wetzel muss nicht liefern. [erg2]Der Vertrag kam erst mit der zweiten Mail zustande, und "
     "den hat sie wirksam angefochten.", PS),
    # --- K Klausurtipp (Lexi) -----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne zwei Fragen. Erst: Welche Erklärung ist die Annahme? [tipp2]Dann: Wirkt der Fehler in "
     "genau dieser Erklärung fort? [tipp3]Und grenze ab: Ein Fehler beim Erklären oder Übermitteln berechtigt zur "
     "Anfechtung, ein Fehler beim Kalkulieren grundsätzlich nicht.", PS),
    # --- L Prüfungsschema ---------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfungsschema: Herr Kübler gegen Frau Wetzel auf Lieferung. [s1]Römisch eins: Kaufvertrag, [s1a]Shop nur "
     "Einladung, Bestellung als Angebot, [s1b]Annahme durch die zweite Mail, nicht schon durch die Eingangsbestätigung. "
     "[s2]Römisch zwei: Nichtigkeit durch Anfechtung, [s2a]Erklärungsirrtum, auch bei fehlerhafter Software, [s2b]Erklärung "
     "gegenüber Herrn Kübler, unverzüglich. [s3]Römisch drei: Ergebnis, kein Lieferanspruch, aber Vertrauensschaden nach "
     "Paragraf hundertzweiundzwanzig.", PS),
    # --- M Merksatz (Lexi) --------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Eingangsbestätigung ist in der Regel noch keine Annahme. [merk2]Und verfälscht die eigene Software "
     "den Preis, darf der Händler anfechten, schuldet aber grundsätzlich den Vertrauensschaden.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    assert not re.search(r"\bBGB\b|\bBGH\b|\d|§", text), "Abkürzung oder Ziffer im Sprechtext"
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
