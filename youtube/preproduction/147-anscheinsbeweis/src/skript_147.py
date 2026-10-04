"""Folge 147 · Anscheinsbeweis, Vermutung, Beweislastumkehr: Nie mehr verwechseln (Fr · 2. Examen · ZPO, Format Sonderlage).
Beispielfall nach dem Plan-Hook („Der Hintermann fährt auf und behauptet, die Vorderfrau habe ohne jeden Grund eine
Vollbremsung gemacht.“): Frau Kretschmer bremst im Stadtverkehr, Herr Hertel fährt ihr hinten auf (Auffahren unstreitig).
Niemand ist verletzt, nur Blechschaden (Stoßstange, 2.400 €). Sie verlangt Ersatz; er bestreitet sein Verschulden und
behauptet eine grundlose Vollbremsung. Zeugen oder andere Beweise gibt es nicht.
Kern: drei Werkzeuge mit derselben Tafelstruktur (Grundlage – was ändert sich – wie wehrt sich der Gegner):
1. Anscheinsbeweis: kein Gesetz, Erfahrungssatz bei typischem Geschehensablauf (BGH VI ZR 18/24 Rn. 19), Teil der freien
   Beweiswürdigung (BGH KZR 26/17 Rn. 49 f.); weder Beweisvermutung noch Beweislastumkehr, Erschüttern durch voll bewiesene
   Tatsachen (BGH XI ZR 91/14 Rn. 24, 46);
2. gesetzliche Vermutung: § 292 S. 1 ZPO (Wortlautkarte, vorgelesen), § 477 Abs. 1 S. 1 BGB (Wortlautkarte, Jahresfrist,
   Art. 229 § 58 EGBGB), Beweis des Gegenteils (BGH VIII ZR 257/23 Rn. 25, 52, 55, zu § 477 a. F.);
3. Beweislastumkehr: § 280 Abs. 1 S. 2 BGB (Wortlautkarte), BGH III ZR 6/18 Rn. 14.
Lösung: Anschein gegen den Auffahrenden (BGH VI ZR 32/16 Rn. 10–12; VI ZR 177/10 Rn. 7, 11), § 4 Abs. 1 StVO
(Wortlautkarte), BGH VI ZR 18/24 Rn. 16 (scharfes Bremsen stets einkalkulieren), § 17 StVG ein Satz (VI ZR 32/16 Rn. 8, 14).
Merktabelle, Klausurtipp (Formulierung angelehnt an VI ZR 32/16 Rn. 13), Merksatz. Verweise: 141 (Beweislast), 125 (§ 477).
Belege: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache, nicht vergeben: Hertel, Kretschmer (nie im Genitiv).
Stimmen: Herr Hertel helmut; Frau Kretschmer spricht nicht. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter; StVO/StVG ausgeschrieben (nicht in der Abkürzungsliste von synth_el)."""

P, PS = 0.3, 0.5

STIMMEN = {"Hertel": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: auf der Stadtstraße ------------------------------------------------------------------------------------------
    ("[fall]Ein Nachmittag im Stadtverkehr. [vorn]Vorne fährt Frau Kretschmer, [hinten]dahinter Herr Hertel. "
     "[bremst]Frau Kretschmer bremst, [auf]und Herr Hertel fährt ihr hinten auf. [blech]Verletzt ist niemand, aber ihre "
     "Stoßstange ist eingedrückt. [aus]Herr Hertel steigt aus.", 0.3),
    ("[h1]Sie hat ohne jeden Grund eine Vollbremsung gemacht!", 0.3, "Hertel"),
    # --- A2 Fall: Klage und Frage ---------------------------------------------------------------------------------------------
    ("[klage]Frau Kretschmer verlangt von ihm Ersatz ihres Schadens, zweitausendvierhundert Euro. [best]Herr Hertel "
     "bestreitet, schuld zu sein. [zeug]Zeugen gibt es nicht. [frage]Muss sie ihm beweisen, dass er zu dicht aufgefahren "
     "ist? [frage2]Und reicht seine Behauptung, um sich zu wehren?", 0.5),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.8),
    # --- C Drei Werkzeuge, ein Raster -----------------------------------------------------------------------------------------
    ("[drei]Drei Werkzeuge helfen dem, der etwas beweisen muss, und sie werden ständig verwechselt: [w1]der "
     "Anscheinsbeweis, [w2]die gesetzliche Vermutung [w3]und die Beweislastumkehr. [raster]Wir prüfen jedes mit denselben "
     "drei Fragen: [r1]Worauf beruht es? [r2]Was ändert sich? [r3]Und wie wehrt sich der Gegner?", P),
    ("[grund]Der Ausgangspunkt steht im Video zur Beweislast: Jede Partei beweist die Voraussetzungen der Norm, die ihr "
     "günstig ist. [grund2]Bleibt es unklar, verliert, wer die Beweislast trägt.", PS),
    # --- D 1. Anscheinsbeweis ------------------------------------------------------------------------------------------------
    ("[a1]Erstens: der Anscheinsbeweis. [a2]Er ist nicht allgemein im Gesetz geregelt. Er beruht auf einem Erfahrungssatz: [a3]Bei einem "
     "typischen Geschehensablauf schließt das Gericht von feststehenden Tatsachen auf eine Ursache oder ein Verschulden. "
     "[a4]Das ist Teil der freien Beweiswürdigung nach Paragraf zweihundertsechsundachtzig ZPO.", P),
    ("[a5]Was ändert sich? Bewiesen werden müssen nur die Tatsachen, an die der Erfahrungssatz anknüpft. [a6]Die "
     "Beweislast bleibt, wo sie war. [a7]Der Bundesgerichtshof sagt ausdrücklich: Der Anscheinsbeweis begründet weder eine "
     "zwingende Beweisregel noch eine Beweisvermutung und auch keine Beweislastumkehr.", P),
    ("[a8]Und der Gegner? Er muss den Anschein nur erschüttern. [a9]Dafür braucht er Tatsachen, die einen atypischen "
     "Verlauf ernsthaft möglich machen. [a10]Diese Tatsachen muss er allerdings voll beweisen. [a11]Gelingt das, fällt der "
     "Anschein weg, und die beweisbelastete Partei muss den vollen Beweis führen.", PS),
    # --- E 2. Gesetzliche Vermutung -------------------------------------------------------------------------------------------
    ("[v1]Zweitens: die gesetzliche Vermutung. [v2]Hier spricht das Gesetz selbst. Paragraf zweihundertzweiundneunzig "
     "Satz eins ZPO: Stellt das Gesetz für das Vorhandensein einer Tatsache eine Vermutung auf, so ist der Beweis des "
     "Gegenteils zulässig, sofern nicht das Gesetz ein anderes vorschreibt.", P),
    ("[v3]Was ändert sich? Bewiesen werden muss nur die Vermutungsbasis, die vermutete Tatsache selbst nicht. [v4]Beispiel: "
     "Paragraf vierhundertsiebenundsiebzig BGB. Zeigt sich beim Verbrauchsgüterkauf innerhalb eines Jahres seit "
     "Gefahrübergang ein abweichender Zustand, [v5]wird vermutet, dass die Ware schon bei Gefahrübergang mangelhaft war. "
     "[v6]Die Jahresfrist gilt für Verträge seit dem ersten Januar zweitausendzweiundzwanzig. Mehr dazu im Video zum "
     "Verbrauchsgüterkauf.", P),
    ("[v7]Und der Gegner? Erschüttern reicht hier nicht. Er muss das Gegenteil voll beweisen. [v8]Bleibt es unklar, gilt "
     "die Vermutung. [v9]Passend dazu lautet die Überschrift von Paragraf vierhundertsiebenundsiebzig: Beweislastumkehr.", PS),
    # --- F 3. Beweislastumkehr ------------------------------------------------------------------------------------------------
    ("[u1]Drittens: die Beweislastumkehr. [u2]Hier gibt es keinen Schluss von einer Tatsache auf eine andere. Eine "
     "Beweislastregel verteilt die Beweislast für ein Merkmal anders als nach der Grundregel. [u3]Paragraf zweihundertachtzig Absatz "
     "eins Satz zwei BGB: Dies gilt nicht, wenn der Schuldner die Pflichtverletzung nicht zu vertreten hat.", P),
    ("[u4]Was ändert sich? Die Beweislast selbst wechselt. [u5]Der Gläubiger beweist die Pflichtverletzung, [u6]der "
     "Schuldner muss beweisen, dass er sie nicht zu vertreten hat. [u7]Und wie wehrt er sich? Nur mit dem vollen Beweis. "
     "[u8]Bleibt es unklar, haftet er.", PS),
    # --- G Lösung des Falls ---------------------------------------------------------------------------------------------------
    ("[l1]Zurück zum Auffahrunfall. [l2]Nach der Rechtsprechung des Bundesgerichtshofs spricht bei Auffahrunfällen grundsätzlich der erste Anschein dafür, "
     "dass der Auffahrende schuldhaft gehandelt hat: [l3]Er hat den Sicherheitsabstand nicht eingehalten, war unaufmerksam "
     "oder zu schnell. [l4]Frau Kretschmer muss also nur das Auffahren beweisen, und das ist unstreitig.", P),
    ("[l5]Herr Hertel behauptet eine grundlose Vollbremsung. [l6]Die bloße Behauptung erschüttert nichts. Er muss die "
     "Tatsachen beweisen, die den Ablauf untypisch machen. [l7]Anders wäre es, wenn feststünde, dass sie kurz vorher vor "
     "ihm die Spur gewechselt hat. Dann fehlte in der Regel schon der typische Ablauf.", P),
    ("[l8]Und mit plötzlichem scharfem Bremsen muss der Hintermann nach dem Bundesgerichtshof stets rechnen. [l9]Paragraf "
     "vier Absatz eins der Straßenverkehrs-Ordnung verlangt in der Regel einen Abstand, bei dem er auch dann noch halten kann. "
     "[l10]Könnte Herr Hertel beweisen, dass sie ohne zwingenden Grund stark gebremst hat, zählte dieser Verstoß gegen Satz zwei bei der "
     "Abwägung nach Paragraf siebzehn Straßenverkehrsgesetz mit.", P),
    ("[l11]So aber bleibt der Anschein. Herr Hertel haftet. [l12]Der Bundesgerichtshof hat in einem ähnlichen Fall "
     "gebilligt, dass der Auffahrende allein haftet.", PS),
    # --- H Merktabelle --------------------------------------------------------------------------------------------------------
    ("[tab]Jetzt alle drei nebeneinander. [t1]Die Grundlage: [t1a]beim Anschein ein Erfahrungssatz, [t1b]bei der Vermutung das "
     "Gesetz, [t1c]bei der Umkehr eine Beweislastregel. [t2]Die Beweislast: [t2a]Beim Anschein bleibt sie. [t2b]Bei der Vermutung muss der Gegner das "
     "Gegenteil beweisen. [t2c]Bei der Umkehr wechselt sie. [t3]Die Gegenwehr: [t3a]erschüttern, [t3b]das Gegenteil voll "
     "beweisen, [t3c]die Entlastung voll beweisen.", PS),
    # --- I Klausurtipp (Lexi) -------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Benenne das Werkzeug genau und nimm das passende Verb. [tipp2]Einen Anschein erschütterst du, "
     "eine Vermutung widerlegst du, und bei der Umkehr trägt der Gegner die Beweislast. [tipp3]Für den Fall passt, angelehnt "
     "an den Bundesgerichtshof: Für ein unfallursächliches Verschulden des Beklagten spricht ein nicht erschütterter "
     "Anscheinsbeweis. [tipp4]Und schreib nie, der Anscheinsbeweis kehre die Beweislast um.", PS),
    # --- J Merksatz (Lexi) ----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Den Anschein erschüttert man, die Vermutung widerlegt man nur mit dem vollen Beweis des Gegenteils. "
     "[mk2]Und bei der Beweislastumkehr verliert im Zweifel der Gegner.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
