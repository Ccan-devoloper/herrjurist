"""Folge 180 · Verfahrenshindernisse StPO: Strafantrag, Verjährung & Co. (Fr · 2. Examen · StPO-Praxis, Format Klausurfehler).
Beispielfall nach dem Plan-Hook („Der Nachbar hat wegen einer Beleidigung erst vier Monate später Anzeige und Strafantrag
gestellt“): Am Mittwoch, 11.3.2026, beleidigt Herr Stolte seinen Nachbarn Herrn Ostwald im Treppenhaus (Wortlaut nie gezeigt,
nur Text-Pille „beleidigende Äußerung“); am Donnerstag, 12.3.2026, schubst er ihn an den Briefkästen (Prellung am Arm; kein
Bild der Handlung). Herr Ostwald kennt Tat und Täter jeweils am selben Tag. Erst am Montag, 13.7.2026, erstattet er bei der
Polizei Anzeige und stellt Strafantrag. Im August entwirft Referendarin Hartlieb bei der Staatsanwaltschaft die
Abschlussverfügung; Herr Stolte ist wegen Körperverletzung vorbestraft.
Roter Faden: vier Klausurfehler (falsch – richtig – Fundstelle). Prüfung: Aufbau (zwei prozessuale Taten, Verweis Folge 039)
→ Strafantrag § 194 Abs. 1 S. 1 (Wortlautkarte), § 230, § 77, Form § 158 Abs. 2 StPO → Frist § 77b Abs. 1 S. 1, Abs. 2 S. 1
(Wortlautkarte) → Kalender Juni 2026 (Fristende 11.6./12.6., Antrag 13.7.) → Fehler 1 → § 230 Abs. 1 S. 1 (Wortlautkarte),
RiStBV Nr. 234 → Beleidigung absolutes Antragsdelikt (§ 194 Abs. 1 S. 2, 3 nur Sonderfälle) → Fehler 2 → Verjährung
§ 78 Abs. 3 Nr. 4, 5 (Wortlautkarte), §§ 78a, 78c → Fehler 3 → Strafklageverbrauch Art. 103 Abs. 3 GG (Wortlautkarte;
BVerfG 2 BvR 900/22 Rn. 3, 95) → Verfügung § 170 Abs. 2 S. 1 StPO (Wortlautkarte), § 376, § 374 StPO, Fehler 4 → Fehlertabelle
→ Prüfschema mit Reihenfolge (übliche Klausurpraxis) → Klausurtipp (Lexi) → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Volltextsuche 04.10.2026): Ostwald, Stolte, Hartlieb (nie im
Genitiv). Stimmen (Pool niklas, helmut, ela_froh, julia): Referendarin Hartlieb ela_froh (eifrig, heiter – Hauptstimme
anders als in 175/178), Herr Ostwald helmut (älterer Nachbar, ein Satz). Herr Stolte spricht nicht. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Ostwald": "helmut", "Hartlieb": "ela_froh"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: im Treppenhaus ---------------------------------------------------------------------------------------------
    ("[fall]Ein Mittwoch im März, das Treppenhaus eines Mietshauses. [streit]Herr Stolte und sein Nachbar, Herr Ostwald, "
     "streiten über ein Fahrrad im Flur. [bel]Dabei macht Herr Stolte eine beleidigende Äußerung. [schub]Am nächsten Tag "
     "schubst er ihn an den Briefkästen: eine Prellung am Arm.", P),
    # --- A2 Fall: auf der Polizeiwache ---------------------------------------------------------------------------------------
    ("[juli]Erst vier Monate später, im Juli, geht Herr Ostwald zur Polizei.", P),
    ("[os1]Ich zeige meinen Nachbarn an und stelle Strafantrag. Ich wollte erst Frieden im Haus.", P, "Ostwald"),
    # --- A3 Fall: bei der Staatsanwaltschaft ---------------------------------------------------------------------------------
    ("[akte]Im August liegt die Akte bei Referendarin Hartlieb. [verf]Sie entwirft die "
     "Abschlussverfügung.", P),
    ("[ha1]Der Strafantrag liegt vor. Ich klage beides an!", P, "Hartlieb"),
    ("[frage]Ein typischer Klausurfehler. [frage2]Welche Verfahrenshindernisse stehen im Weg, und was verfügt die "
     "Staatsanwaltschaft?", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Aufbau ------------------------------------------------------------------------------------------------------------
    ("[aufbau]Ein Verfahrenshindernis sperrt die Verfolgung, so klar die Tat auch ist. [a1]Wir prüfen den Strafantrag, "
     "[a2]das besondere öffentliche Interesse, [a3]die Verjährung [a4]und den Strafklageverbrauch. [taten]Vorweg: "
     "Beleidigung und Schubser liegen an zwei Tagen, also zwei prozessuale Taten mit je eigener Entscheidung, wie im "
     "Video zur Anklageklausur.", PS),
    # --- D Strafantrag: § 194, § 230, § 77, § 158 Abs. 2 StPO ----------------------------------------------------------------
    ("[p194]Paragraf hundertvierundneunzig Absatz eins Satz eins Strafgesetzbuch: Die Beleidigung wird nur auf Antrag "
     "verfolgt. [p230k]Für die Körperverletzung gilt nach Paragraf zweihundertdreißig grundsätzlich dasselbe. [p77]Den "
     "Antrag stellen darf nach Paragraf siebenundsiebzig der Verletzte, also Herr Ostwald. [form]Zur Form verlangt "
     "Paragraf hundertachtundfünfzig Absatz zwei Strafprozessordnung nur, dass Identität und Verfolgungswille "
     "sichergestellt sind.", P),
    # --- E Antragsfrist: § 77b StGB ------------------------------------------------------------------------------------------
    ("[p77b]Aber die Frist! Paragraf siebenundsiebzig b: Eine Tat, die nur auf Antrag verfolgbar ist, wird nicht "
     "verfolgt, wenn der Antragsberechtigte es unterlässt, den Antrag bis zum Ablauf einer Frist von drei Monaten zu "
     "stellen. [beginn]Die Frist beginnt mit Ablauf des Tages, an dem der Berechtigte von der Tat und der Person des "
     "Täters Kenntnis erlangt.", P),
    # --- F Kalender Juni 2026 ------------------------------------------------------------------------------------------------
    ("[kenn]Herr Ostwald kennt seinen Nachbarn: Kenntnis am Tattag, dem elften März. [ende]Die drei Monate "
     "enden mit Ablauf des elften Juni, eines Donnerstags. [schub2]Für den Schubser vom zwölften März endet die Frist am "
     "Freitag, dem zwölften Juni. [spaet]Der Antrag kommt am dreizehnten Juli: für beide Taten zu spät.", P),
    ("[f1]Klausurfehler Nummer eins: Strafantrag liegt vor, also verfolgbar. [f1r]Richtig: die Frist rechnen, ab "
     "Kenntnis von Tat und Täter, nicht ab der Anzeige.", PS),
    # --- G Ausweg: besonderes öffentliches Interesse, § 230 StGB -------------------------------------------------------------
    ("[p230]Gibt es einen Ausweg? Paragraf zweihundertdreißig Absatz eins Satz eins: nur auf Antrag, es sei denn, die "
     "Strafverfolgungsbehörde hält wegen des besonderen öffentlichen Interesses ein Einschreiten von Amts wegen für "
     "geboten. [rel]Ein relatives "
     "Antragsdelikt: Das Interesse hilft auch über den verspäteten Antrag hinweg. [vorstr]Herr Stolte ist wegen "
     "Körperverletzung vorbestraft; nach den Richtlinien für das Strafverfahren spricht das namentlich dafür. [bejaht]Die Staatsanwaltschaft bejaht es.", P),
    # --- H Beleidigung: absolutes Antragsdelikt ------------------------------------------------------------------------------
    ("[absol]Und die Beleidigung? [abs2]Für die einfache Beleidigung kennt Paragraf hundertvierundneunzig diesen Ausweg "
     "nicht: ein absolutes Antragsdelikt. [ausn]Die Ausnahmen der Sätze zwei und drei, etwa für "
     "Paragraf hundertachtundachtzig, passen auf einen Streit im Treppenhaus nicht.", P),
    ("[ha2]Dann bejahe ich eben auch hier das öffentliche Interesse!", P, "Hartlieb"),
    ("[f2]Klausurfehler Nummer zwei. [f2r]Richtig: Für diese Beleidigung ersetzt nichts den rechtzeitigen Antrag.", PS),
    # --- I Verjährung: §§ 78, 78a, 78c StGB ----------------------------------------------------------------------------------
    ("[p78]Dann die Verjährung. Paragraf achtundsiebzig Absatz drei: Nummer vier, fünf "
     "Jahre bei mehr als einem Jahr bis zu fünf Jahren im Höchstmaß; [nr5]Nummer fünf, drei Jahre für die übrigen Taten. "
     "[rahmen]Die Beleidigung droht bis zu einem Jahr an: drei Jahre. [qual]Erst die öffentliche Beleidigung reicht bis zu "
     "zwei Jahren: dann fünf. [kv5]Die Körperverletzung droht bis zu fünf Jahren an: fünf Jahre. [p78a]Die Frist beginnt mit "
     "Beendigung der Tat, Paragraf achtundsiebzig a; [p78c]die erste Vernehmung des Beschuldigten unterbricht sie, "
     "Paragraf achtundsiebzig c. [nichtv]Im August ist nichts verjährt.", P),
    ("[f3]Klausurfehler Nummer drei: fünf Jahre für jedes Vergehen. [f3r]Richtig: das Höchstmaß ablesen.", PS),
    # --- J Strafklageverbrauch: Art. 103 Abs. 3 GG ---------------------------------------------------------------------------
    ("[p103]Bleibt der Strafklageverbrauch. Artikel hundertdrei Absatz drei Grundgesetz: Niemand darf wegen derselben Tat "
     "auf Grund der allgemeinen Strafgesetze mehrmals bestraft werden. [urt]Nach dem Bundesverfassungsgericht sperrt das "
     "eine erneute Verfolgung, wenn über dieselbe Tat schon ein rechtskräftiges Strafurteil ergangen ist; [keins]hier "
     "gibt es keines.", P),
    # --- K Verfügung: § 170 Abs. 2 StPO, §§ 376, 374 StPO --------------------------------------------------------------------
    ("[p170]Die Folge: Paragraf hundertsiebzig Absatz zwei Satz eins Strafprozessordnung: Andernfalls stellt die "
     "Staatsanwaltschaft das Verfahren ein. [bele]Für die Beleidigung fehlt damit der genügende "
     "Anlass zur Anklage: Einstellung. [kva]Für die Körperverletzung, ein Privatklagedelikt, verlangt "
     "Paragraf dreihundertsechsundsiebzig ein öffentliches Interesse; mit dem besonderen liegt es vor: Anklage.", P),
    ("[ha3]Also: Beleidigung einstellen, Körperverletzung anklagen.", P, "Hartlieb"),
    ("[f4]Klausurfehler Nummer vier: bei verspätetem Antrag auf den Privatklageweg nach Paragraf dreihundertvierundsiebzig "
     "verweisen. [f4r]Richtig: Auch die Privatklage braucht einen rechtzeitigen Antrag.", PS),
    # --- L Fehlertabelle -----------------------------------------------------------------------------------------------------
    ("[tab]Die vier Fehler auf einen Blick: [t1]Frist nicht gerechnet. [t2]Öffentliches Interesse bei der Beleidigung. "
     "[t3]Verjährung pauschal. [t4]Privatklage trotz verspätetem Antrag.", PS),
    # --- M Prüfschema mit Reihenfolge ----------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für jede prozessuale Tat. [s1]Römisch eins: Strafbarkeit und hinreichender Tatverdacht. "
     "[s2]Römisch zwei: Verfahrenshindernisse: Strafantrag mit Frist, sonst besonderes öffentliches Interesse, Verjährung, "
     "Strafklageverbrauch. [s3]Römisch drei: die Verfügung, Anklage oder Einstellung. [reihe]Die Reihenfolge ist Klausurpraxis, "
     "kein Gesetz; manche prüfen den Strafantrag direkt beim Delikt. Maßgeblich ist der Bearbeitervermerk.", PS),
    # --- N Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Drei Fragen bei jedem Antragsdelikt. [k1]Antrag gestellt, vom Berechtigten? "
     "[k2]Rechtzeitig, ab Kenntnis gerechnet? [k3]Und wenn nicht: Gibt es den Ausweg über das besondere öffentliche "
     "Interesse?", PS),
    # --- O Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein Verfahrenshindernis schlägt jede noch so klare Strafbarkeit. [m2]Die Antragsfrist läuft drei Monate "
     "ab Kenntnis; das besondere öffentliche Interesse rettet nur relative Antragsdelikte.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
