"""Folge 270 · Amtsgericht Zuständigkeit 2026: Streitwert bis 10.000 Euro (Fr · 2. Examen · ZPO · Format Sonderlage).
Beispielfall nach dem Plan-Hook: Tischlermeister Herr Haberkorn (Tischlerei Haberkorn, fiktiv) hat bei einem Kunden eine
Holztreppe eingebaut; die Rechnung über 9.200 € ist offen. Er fragt, ob er zum Landgericht und damit zwingend zum Anwalt
muss. Seine Tochter Irmela ist Referendarin. Frau Bergfeld (Büro der Tischlerei) erinnert an eine ältere Klage über
7.000 €, eingegangen beim Landgericht am 10.12.2025, zugestellt am 8.1.2026.
Aufbau (Sonderlage laut Auftrag): 1. Hook mit Zahlen → 2. § 23 Nr. 1 GVG (Wortlautkarte, aktuelle Fassung) und § 71 Abs. 1
GVG (Wortlautkarte); Änderungsgesetz vom 8.12.2025, BGBl. 2025 I Nr. 318 → 3. Rechenbeispiel 9.200 € (§ 4 Abs. 1, § 5 ZPO)
→ kein Anwaltszwang (§ 78 Abs. 1 S. 1 ZPO, Wortlautkarte; § 79 Abs. 1 S. 1 ZPO) → 4. Altverfahren: § 44 S. 1 EGGVG
(Wortlautkarte) und perpetuatio fori § 261 Abs. 3 Nr. 2 ZPO (Wortlautkarte), Ausnahme § 506 ZPO → 5. Abgrenzung § 495a ZPO
(Wortlautkarte) → Sonderzuständigkeiten § 23 Nr. 2, § 71 Abs. 2 GVG (Tafel mit geprüften Beispielen) → 6. Klausurtipp
(Lexi; Achtung alte Skripte: 5.000 €; Hilfsmittel je Land) → Schema → Merksatz (Lexi). Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Reservierung „270: Haberkorn, Irmela, Bergfeld“): Herr Haberkorn,
Irmela, Frau Bergfeld; nie im Genitiv.
Stimmen (Pool stephan, hilde, christian, lucy): Herr Haberkorn christian (Mann, mittel), Irmela lucy (Frau, jung), Frau Bergfeld
hilde (Frau, älter); stephan nicht verwendet (also nie stephan und christian in einer Szene). Lexi = Erzählerin Carla.
„GVG“ steht nicht in der Abkürzungsliste von synth_el.py; im Sprechtext deshalb „G.V.G.“ (so wie synth_el ZPO → „Z.P.O.“
aufbereitet), Untertitel werden in meta_270.py zurückgeführt.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Daten und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Haberkorn": "christian", "Irmela": "lucy", "Bergfeld": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: in der Tischlerei ---------------------------------------------------------------------------------------
    ("[fall]In einer Tischlerei. [rechnung]Tischlermeister Haberkorn hält eine offene Rechnung in der Hand: [treppe]eine "
     "Holztreppe, eingebaut bei einem Kunden, [summe]neuntausendzweihundert Euro. [irmela]Seine Tochter Irmela ist "
     "Referendarin.", P),
    ("[ha1]Der Kunde zahlt einfach nicht. Muss ich damit zum Landgericht? Dann brauche ich ja zwingend einen Anwalt.",
     P, "Haberkorn"),
    ("[ir1]Nicht mehr, Papa. Seit zweitausendsechsundzwanzig geht das Amtsgericht bis zehntausend Euro.",
     P, "Irmela"),
    # Neufassung 08.10.2026 (Bild-Satz-Passung): Erstfassung „Im Büro sitzt Frau Bergfeld.“ – die Pose blazer-4 steht;
    # Frau Bergfeld kommt jetzt aus dem Büro (Tür rechts) dazu.
    ("[bergfeld]Aus dem Büro kommt Frau Bergfeld dazu.", P),
    ("[be1]Und unsere Klage vom Dezember über siebentausend Euro? Die liegt beim Landgericht.", PS, "Bergfeld"),
    ("[hook]Zehntausend statt fünftausend Euro: [hook2]Das ist die neue Wertgrenze. [frage]Wann ist das Amtsgericht "
     "jetzt zuständig, [frage2]was gilt für Altverfahren, [frage3]und was "
     "haben die tausend Euro in Paragraf vierhundertfünfundneunzig a ZPO damit zu tun?", PS),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 23 Nr. 1 und § 71 Abs. 1 GVG --------------------------------------------------------------------------------
    ("[w23]Die Grundnorm steht in Paragraf dreiundzwanzig Nummer eins G.V.G. [w23b]Das Amtsgericht ist zuständig für "
     "Streitigkeiten über Ansprüche, deren Gegenstand an Geld oder Geldeswert die Summe von zehntausend Euro nicht "
     "übersteigt. [bis]Genau zehntausend Euro gehören also noch zum Amtsgericht.", P),
    ("[w71]Den Rest regelt Paragraf einundsiebzig Absatz eins: [w71b]Vor die Zivilkammern der Landgerichte gehören alle "
     "bürgerlichen Rechtsstreitigkeiten, die nicht den Amtsgerichten zugewiesen sind.", P),
    ("[reform]Bis Ende zweitausendfünfundzwanzig lag die Grenze bei fünftausend Euro. [gesetz]Angehoben hat sie ein Gesetz "
     "vom achten Dezember zweitausendfünfundzwanzig, [kraft]in Kraft seit dem ersten Januar zweitausendsechsundzwanzig.", PS),
    # --- D Rechenbeispiel ------------------------------------------------------------------------------------------------
    ("[rech]Zur Rechnung von Herrn Haberkorn. [r1]Neuntausendzweihundert Euro Werklohn liegen unter zehntausend Euro. "
     "[r2]Zinsen und Kosten zählen nicht mit, wenn er sie als Nebenforderungen verlangt, Paragraf vier ZPO. [r3]Also ist "
     "das Amtsgericht zuständig.", P),
    ("[r4]Aber Vorsicht: Mehrere Ansprüche in einer Klage werden zusammengerechnet, Paragraf fünf. [r5]Klagt er eine "
     "zweite Rechnung über tausend Euro mit ein, sind es zehntausendzweihundert Euro: [r6]Landgericht.", PS),
    ("[w78]Und der Anwalt? Paragraf achtundsiebzig Absatz eins ZPO: [w78b]Vor den Landgerichten und Oberlandesgerichten "
     "müssen sich die Parteien durch einen Rechtsanwalt vertreten lassen. [ag]Für das Amtsgericht gilt das nicht. "
     "[selbst]Dort darf Herr Haberkorn den Prozess selbst führen, Paragraf neunundsiebzig.", P),
    ("[ha2]Dann führe ich den Prozess selbst.", P, "Haberkorn"),
    ("[ir2]Kannst du. Ein Anwalt ist erlaubt, aber keine Pflicht.", PS, "Irmela"),
    # --- E Altverfahren: § 44 EGGVG, perpetuatio fori --------------------------------------------------------------------
    ("[alt]Jetzt die Klage vom Dezember: [alt2]Sie ging am zehnten Dezember zweitausendfünfundzwanzig beim Landgericht ein "
     "[alt3]und wurde im Januar zugestellt. [w44]Dafür gibt es eine Übergangsvorschrift: Paragraf "
     "vierundvierzig des Einführungsgesetzes zum Gerichtsverfassungsgesetz. [w44b]Ist ein Verfahren vor dem ersten Januar "
     "zweitausendsechsundzwanzig anhängig geworden, gilt Paragraf dreiundzwanzig Nummer eins in der alten Fassung.", P),
    ("[anh]Anhängig heißt: bei Gericht eingegangen, auf die Zustellung kommt es nicht an. [lg]Für die Klage vom "
     "Dezember bleibt es also bei fünftausend Euro und damit beim Landgericht.", P),
    ("[be2]Dann bleibt es dort beim Anwalt.", P, "Bergfeld"),
    ("[w261]Und wenn sich später etwas ändert? Paragraf zweihunderteinundsechzig Absatz drei Nummer zwei ZPO: [w261b]Die "
     "Zuständigkeit des Prozessgerichts wird durch eine Veränderung der sie begründenden Umstände nicht berührt. "
     "[pf]Das ist die perpetuatio fori. [pf2]Zahlt der Kunde im Prozess dreitausend Euro und sinkt der Streitwert, "
     "bleibt das Landgericht zuständig. [pf3]Diese Wirkung beginnt mit der Rechtshängigkeit, also mit der Zustellung der "
     "Klage.", P),
    ("[w506]Eine Ausnahme: Erweitert der Kläger am Amtsgericht seine Klage über zehntausend Euro, "
     "[w506b]verweist das Amtsgericht auf Antrag an das Landgericht, Paragraf fünfhundertsechs ZPO.", PS),
    # --- F Abgrenzung § 495a ZPO -----------------------------------------------------------------------------------------
    ("[w495]Nicht verwechseln: Paragraf vierhundertfünfundneunzig a ZPO. [w495b]Das Gericht kann sein Verfahren nach "
     "billigem Ermessen bestimmen, wenn der Streitwert tausend Euro nicht übersteigt. [antrag]Auf Antrag muss mündlich "
     "verhandelt werden.", P),
    ("[ver]Das ist ein vereinfachtes Verfahren am Amtsgericht, keine Zuständigkeitsnorm. [neu495]Auch diese Grenze stieg "
     "zum selben Stichtag, von sechshundert auf tausend Euro. [bsp]Eine Rechnung über achthundert "
     "Euro landet beim Amtsgericht wie jede bis zehntausend Euro; [frei]das Gericht darf das Verfahren nur freier "
     "gestalten.", PS),
    # --- G Sonderzuständigkeiten (Tafel) ---------------------------------------------------------------------------------
    ("[sonder]Manche Streitigkeiten hängen gar nicht vom Wert ab. [s23]Dem Amtsgericht weist Paragraf dreiundzwanzig "
     "Nummer zwei etwa Streit aus Wohnraummiete zu, [s23b]Streit nach dem Wohnungseigentumsgesetz, [s23c]Wildschäden "
     "[s23d]und, neu seit zweitausendsechsundzwanzig, bestimmte Nachbarstreitigkeiten.", P),
    ("[s71]Dem Landgericht weist Paragraf einundsiebzig Absatz zwei etwa Streit über Anordnungen beim Bauvertrag zu, "
     "[s71b]und ebenfalls neu Streit aus Heilbehandlungen, [s71c]aus Veröffentlichungen in Presse und Internet [s71d]und "
     "über die Vergabe öffentlicher Aufträge.", P),
    ("[treppe2]Herr Haberkorn streitet nur um den Werklohn, [wert]bei ihm entscheidet der Wert.", PS),
    # --- H Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Achtung, alte Skripte nennen noch fünftausend Euro. [tipp2]Welche Hilfsmittel in welchem Stand "
     "zugelassen sind, ist von Land zu Land verschieden. [tipp3]Und schau im Aktenauszug auf den Eingangsstempel der "
     "Klage: Ging sie vor zweitausendsechsundzwanzig ein, gilt die alte Grenze.", PS),
    # Nachvertonung 08.10.2026: „das Amtsgericht“ in [k4] hörten whisper small und medium übereinstimmend als
    # „Ansgericht/Anzgericht“ → Satz leicht umgestellt („ist das Amtsgericht zuständig“), Segment einmal neu vertont.
    # --- I Prüfschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema zur sachlichen Zuständigkeit. [k1]Römisch eins: Gibt es eine Zuständigkeit ohne Rücksicht auf den "
     "Wert, [k1a]etwa nach Paragraf dreiundzwanzig Nummer zwei oder einundsiebzig Absatz zwei? [k2]Römisch zwei: der "
     "Streitwert, [k2a]ohne Nebenforderungen, mehrere Ansprüche zusammengerechnet. [k3]Römisch drei: Wann wurde die Klage "
     "anhängig? [k3a]Vor zweitausendsechsundzwanzig fünftausend, danach zehntausend Euro. "
     "[k4]Römisch vier: Bis zur Grenze ist das Amtsgericht zuständig, darüber das Landgericht mit Anwaltszwang. "
     "[k5]Römisch fünf: "
     "Spätere Veränderungen nach Rechtshängigkeit lassen die Zuständigkeit unberührt, [k5a]außer bei einer Erweiterung nach Paragraf "
     "fünfhundertsechs.", PS),
    # --- J Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Amtsgericht bis zehntausend Euro, ohne Anwaltszwang. [m2]Die fünftausend Euro aus alten Skripten "
     "gelten nur noch für Klagen, die vor zweitausendsechsundzwanzig eingegangen sind.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
