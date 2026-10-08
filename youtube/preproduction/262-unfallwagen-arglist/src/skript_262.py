"""Folge 262 · Unfallwagen verschwiegen: Arglistige Täuschung oder Mängelrechte? (Mo · Der Fall · BGB AT · Alltagsfall;
§§ 123, 124, 142, 437, 444 BGB; zusätzlich §§ 14, 143, 119 Abs. 2, 325, 326 Abs. 5, 346, 434 Abs. 3, 476, 812 BGB).
Fall nach dem Plan-Hook („Der Händler verschweigt den reparierten Unfallschaden – du erfährst es erst beim TÜV“; im Video
markenneutral „bei der Hauptuntersuchung“): Angelika, selbständige Hebamme, kauft für ihre Hausbesuche beim (fiktiven)
Gebrauchtwagenhändler Herrn Hecker einen Kombi für 8.000 € unter Ausschluss jeder Gewährleistung. Herr Hecker hat den
Wagen als Unfallwagen angekauft und den schweren Frontschaden in seiner eigenen Werkstatt reparieren lassen; er sagt
nichts, Angelika fragt nicht. Drei Monate später entdeckt der Prüfer bei der Hauptuntersuchung den reparierten
Unfallschaden. Eine Woche später ficht Angelika schriftlich gegenüber Herrn Hecker an und verlangt die 8.000 € zurück.
Aufbau (Plan): Hook → § 123 Abs. 1 (Wortlautkarte): Täuschung durch Unterlassen (Aufklärungspflicht; Unfallschaden beim
Gebrauchtwagenhändler), Irrtum und Kausalität, Arglist → § 124 Abs. 1, 2 (Wortlautkarte), § 143, § 142 Abs. 1, § 812 →
Konkurrenz: Anfechtung neben §§ 437 ff. (keine Sperre bei Arglist), anders § 119 Abs. 2 (ein Satz, h. M.) → § 444
(Wortlautkarte), § 476 (ein Satz) → Vergleich Anfechtung/Rücktritt (Verweis Folgen 063, 236) → Klausurtipp (BGH VIII ZR
37/24: Anfechtung kann als Rücktritt auszulegen sein) → Schema → Merksatz. Voraussetzung (Folge 023) nur verwiesen.
Belege je Cue: ../RECHTSSTAND.md (Normwortlaut gesetze-im-internet.de, Abruf 08.10.2026; BGH-Volltexte mit Rn.).
Stimmen (Pool william, sabrina, marc, laura_ruhig): Angelika (sabrina, Frau, mittel), Herr Hecker (marc, Mann, mittel),
Prüfer (william, Mann, älter; Funktionsrolle ohne Namen). laura_ruhig nicht besetzt (Folge 259). Erzählerin/Lexi: Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; keine Abkürzungen. Kein Genitiv eines Namens."""

P, PS = 0.3, 0.5

STIMMEN = {"Angelika": "sabrina", "Hecker": "marc", "Pruefer": "william"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: beim Gebrauchtwagenhändler ------------------------------------------------------------------------
    ("[fall]Angelika ist selbständige Hebamme und braucht ein Auto für ihre Hausbesuche. [hof]Beim Gebrauchtwagenhändler "
     "Herrn Hecker findet sie einen Kombi für achttausend Euro. [vorher]Was sie nicht weiß: Herr Hecker hat den Wagen als "
     "Unfallwagen angekauft und den schweren Frontschaden in seiner eigenen Werkstatt reparieren lassen.", P),
    ("[h1]Achttausend Euro, aber ohne jede Gewährleistung.", P, "Hecker"),
    ("[kauf]Nach Unfällen fragt Angelika nicht, und Herr Hecker sagt nichts. [unterschr]Sie unterschreibt.", P),
    # --- A2 Hauptuntersuchung ---------------------------------------------------------------------------------------
    ("[hu]Drei Monate später ist der Kombi bei der Hauptuntersuchung.", P),
    ("[p1]Hier wurde ein schwerer Unfallschaden repariert.", P, "Pruefer"),
    ("[a1]Davon hat mir Herr Hecker kein Wort gesagt! Ich will mein Geld zurück.", P, "Angelika"),
    ("[brief]Eine Woche später ficht Angelika den Kauf schriftlich an. [frage]Darf sie das, obwohl sie auch Mängelrechte "
     "hat? [frage2]Und hilft Herrn Hecker der Ausschluss der Gewährleistung?", PS),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Zwei Wege --------------------------------------------------------------------------------------------------
    ("[ansp]Angelika will ihr Geld zurück. Dafür gibt es zwei Wege: [weg1]die Anfechtung [weg2]oder den Rücktritt wegen "
     "eines Mangels.", P),
    # --- D § 123 Abs. 1 (Wortlautkarte) -------------------------------------------------------------------------------
    ("[p123]Paragraf hundertdreiundzwanzig Absatz eins: Wer zur Abgabe einer Willenserklärung durch arglistige Täuschung "
     "oder widerrechtlich durch Drohung bestimmt worden ist, kann die Erklärung anfechten. [pruef]Wir prüfen die "
     "Täuschung, den Irrtum mit Kausalität und die Arglist.", P),
    # --- E Täuschung durch Unterlassen --------------------------------------------------------------------------------
    ("[luege]Herr Hecker hat nicht gelogen. Er hat geschwiegen. [pflicht]Schweigen täuscht nur, wenn eine Pflicht zur "
     "Aufklärung besteht. [erwart]Aufklären muss "
     "man, auch ungefragt, über Tatsachen, deren Mitteilung der andere redlicherweise erwarten darf, weil sie für seine Entscheidung "
     "offensichtlich ausschlaggebend sind.", P),
    ("[gw]Für Gebrauchtwagen gilt nach dem Bundesgerichtshof: Ein Unfallschaden, den der Händler kennt, ist "
     "aufklärungspflichtig. [bagatell]Ausgenommen sind Bagatellschäden, etwa ein kleiner Lackschaden. [kennt]Herr Hecker kannte den "
     "schweren Frontschaden aus seiner eigenen Werkstatt. [unterl]Sein Schweigen ist eine Täuschung durch "
     "Unterlassen.", P),
    # --- F Irrtum, Kausalität, Arglist ----------------------------------------------------------------------------------
    ("[irrtum]Angelika irrt: Sie hält den Kombi für unfallfrei. [kaus]Und er ist ursächlich: Hätte sie vom "
     "Unfall gewusst, hätte sie den Wagen nicht gekauft.", P),
    ("[arg]Bleibt die Arglist. Arglistig verschweigt einen Mangel, wer ihn mindestens für möglich hält [arg2]und damit "
     "rechnet und billigend in Kauf nimmt, dass der andere ihn nicht kennt und bei Kenntnis nicht oder nicht so gekauft hätte. [argok]Herr Hecker "
     "kannte den Schaden und wusste, dass Angelika sonst nicht kaufen würde. Das ist Arglist.", PS),
    # --- G § 124 (Wortlautkarte), § 143, § 142 Abs. 1, § 812 ----------------------------------------------------------
    ("[p124]Zur Frist, Paragraf hundertvierundzwanzig: [p124a]Die Anfechtung kann nur binnen Jahresfrist "
     "erfolgen. [p124b]Bei arglistiger Täuschung beginnt die Frist, wenn der Anfechtungsberechtigte die Täuschung entdeckt. "
     "[frist]Angelika hat eine Woche nach der Entdeckung gegenüber Herrn Hecker angefochten, Paragraf "
     "hundertdreiundvierzig: rechtzeitig.", P),
    ("[p142]Die Folge regelt Paragraf hundertzweiundvierzig Absatz eins: Der Kaufvertrag ist als von Anfang an nichtig "
     "anzusehen. [p812]Zurückgegeben wird nach Paragraf achthundertzwölf: Angelika bekommt die achttausend Euro, Herr "
     "Hecker den Kombi. [v023]Das Grundschema zeigt unsere Folge zur Anfechtung in fünf Schritten.", PS),
    # --- H Konkurrenz: Anfechtung neben den Mängelrechten ---------------------------------------------------------------
    ("[konk]Aber darf Angelika überhaupt anfechten? [mangel]Der Kombi ist ja auch mangelhaft: Ein Unfallwagen hat nicht "
     "die übliche Beschaffenheit, die ein Käufer erwarten kann, [rep]und daran ändert auch die Reparatur nichts. "
     "[sperre]Trotzdem sperren die Mängelrechte die Anfechtung wegen Arglist nicht. [bgh]Der Bundesgerichtshof prüft bei "
     "Arglist beide Wege nebeneinander. [p119]Anders beim Eigenschaftsirrtum nach Paragraf hundertneunzehn Absatz zwei: "
     "Ihn verdrängen nach herrschender Meinung ab Gefahrübergang die Mängelrechte.", PS),
    # --- I § 444 (Wortlautkarte), § 476 ---------------------------------------------------------------------------------
    ("[aus]Und der Gewährleistungsausschluss? [unter]Angelika kauft beruflich, als Unternehmerin. Da ist ein "
     "Ausschluss grundsätzlich möglich. [v476]Gegenüber einem Verbraucher ginge das nach Paragraf "
     "vierhundertsechsundsiebzig nicht. [p444]Hier hilft Paragraf vierhundertvierundvierzig: Auf eine "
     "Vereinbarung, durch welche die Rechte des Käufers wegen eines Mangels ausgeschlossen oder beschränkt werden, kann "
     "sich der Verkäufer nicht berufen, soweit er den Mangel arglistig verschwiegen hat. [p444ok]Genau das hat Herr "
     "Hecker getan. [anfaus]Die Anfechtung trifft der Ausschluss ohnehin nicht, er betrifft nur die "
     "Mängelrechte.", PS),
    # --- K Vergleich: Anfechtung oder Rücktritt ---------------------------------------------------------------------------
    ("[vgl]Was ist für Angelika günstiger? [vgl1]Mit der Anfechtung fällt der Vertrag rückwirkend weg, "
     "und mit ihm die vertraglichen Mängelrechte. [vgl2]Beim Rücktritt bleibt der "
     "Vertrag die Grundlage. Rückabgewickelt wird nach Paragraf dreihundertsechsundvierzig, und Schadensersatz bleibt "
     "daneben möglich, Paragraf dreihundertfünfundzwanzig. [frist2]Eine Frist zur Nacherfüllung braucht Angelika in der Regel nicht: "
     "Aus einem Unfallwagen wird kein unfallfreier Wagen. [vgl3]Deshalb erklären Käufer in der Praxis oft "
     "beides: die Anfechtung und hilfsweise den Rücktritt. [v063]Mehr dazu in unseren Folgen zu den Käuferrechten und zum Schadensersatz im Kaufrecht.", PS),
    # --- L Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bei der Täuschung durch Unterlassen ist die Aufklärungspflicht der Knackpunkt. Begründe sie am "
     "Fall. [tipp2]Und lies die Erklärung des Käufers genau. [tipp3]Nach dem Bundesgerichtshof kann eine Anfechtung "
     "zugleich als Rücktritt auszulegen sein, wenn der Käufer den Vertrag auf jeden Fall rückabgewickelt haben will.", PS),
    # --- M Prüfungsschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfungsschema: Angelika gegen Herrn Hecker auf achttausend Euro. [s1]Römisch eins: Anfechtung und "
     "Rückgabe. [s1a]Erstens: arglistige Täuschung nach Paragraf hundertdreiundzwanzig: Täuschung, bei Schweigen mit "
     "Aufklärungspflicht, Irrtum, Kausalität, Arglist. [s1b]Zweitens: Anfechtungserklärung und Jahresfrist ab "
     "Entdeckung. [s1c]Drittens: nichtig von Anfang an, Rückgabe nach Paragraf achthundertzwölf. [s2]Römisch zwei: "
     "alternativ der Rücktritt. Der Unfallwagen ist mangelhaft, und der Ausschluss scheitert an Paragraf "
     "vierhundertvierundvierzig. [s3]Römisch drei: Ergebnis. Angelika bekommt ihr Geld zurück.", PS),
    # --- N Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer einen bekannten Unfallschaden verschweigt, täuscht arglistig. [merk2]Der Käufer kann anfechten "
     "oder seine Mängelrechte nutzen, und auf den Gewährleistungsausschluss kann sich der Händler nicht berufen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    assert not re.search(r"\bBGB\b|\bBGH\b|\d|§", text), "Abkürzung oder Ziffer im Sprechtext"
    assert not re.search(r"Angelikas|Heckers", text), "Genitiv eines Namens"
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
