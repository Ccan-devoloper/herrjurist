"""Folge 265 · „Gekauft wie gesehen“: Hält der Gewährleistungsausschluss? (Mo · Der Fall · Kaufrecht · Alltagsfall;
§§ 434, 444, 476 BGB; zusätzlich §§ 309 Nr. 7, 8 b, 437, 474 BGB).
Fall nach dem Plan-Hook („Im privaten Autokaufvertrag steht ‚gekauft wie gesehen, keine Gewährleistung‘ – der Motor ist
hinüber“): Christel kauft von Herrn Burmeister, einer Privatperson, dessen alten Kleinwagen für 4.500 €. Nach Besichtigung
und Probefahrt sagt er: „Der Motor läuft einwandfrei.“ Im handschriftlichen, gemeinsam formulierten Kaufvertrag steht
„Motor läuft einwandfrei.“ und darunter „Gekauft wie gesehen, keine Gewährleistung.“ Drei Wochen später ist der Motor
hinüber; die Mechanikerin stellt fest, dass der Schaden schon beim Kauf da war. Herr Burmeister wusste davon nichts und
beruft sich auf den Ausschluss.
Aufbau (Plan): Hook → 1. Sachmangel § 434 (Wortlautkarte Abs. 1, Abs. 2 S. 1 Nr. 1, Abs. 3 S. 1 Nr. 1; Verweis Folge 059)
→ 2. Ausschluss wirksam? (Privatverkauf, § 476 nur beim Verbrauchsgüterkauf, Individualvereinbarung, AGB-Grenze § 309
Nr. 7/8 in einem Satz) → 3. Reichweite: „gekauft wie gesehen“ allein nur wahrnehmbare Mängel (BGH VIII ZR 261/14 Rn. 22),
mit „keine Gewährleistung“ umfassend (BGH VIII ZR 136/04) → 4. § 444 (Wortlautkarte): Arglist (−), Garantie (−);
Abgrenzung Folge 262 in einem Satz → 5. Beschaffenheitsvereinbarung geht vor (BGHZ 170, 86 Rn. 30 f.; st. Rspr.,
BGH VIII ZR 161/23 Rn. 23, 38, 40) → 6. Ergebnis je Variante (Tafel; Verweis Folge 063) → 7. Klausurtipp (Lexi) →
Schema → Merksatz.
Belege je Cue: ../RECHTSSTAND.md (Normwortlaut gesetze-im-internet.de, Abruf 08.10.2026; BGH-Volltexte mit Rn.).
Stimmen (Pool william, sabrina, marc, laura_ruhig): Christel (laura_ruhig, Frau, mittel), Herr Burmeister (william, Mann,
älter), Mechanikerin (sabrina, Frau, mittel; Funktionsrolle ohne Namen). marc nicht besetzt. Erzählerin/Lexi: Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; keine Abkürzungen. Kein Genitiv eines Namens."""

P, PS = 0.3, 0.5

STIMMEN = {"Christel": "laura_ruhig", "Burmeister": "william", "Mechanikerin": "sabrina"}  # Lexi = Erzählerstimme

SEGMENTE = [
    # --- A1 Fall: Privatverkauf vor dem Haus ---------------------------------------------------------------------------
    ("[fall]Christel sucht einen gebrauchten Kleinwagen. [hof]Herr Burmeister verkauft privat sein altes Auto, für "
     "viertausendfünfhundert Euro. [probe]Christel sieht sich den Wagen an und macht eine Probefahrt. Alles wirkt in "
     "Ordnung.", P),
    ("[b1]Der Motor läuft einwandfrei.", P, "Burmeister"),
    ("[vertrag]Genau das steht im handschriftlichen Kaufvertrag: Motor läuft einwandfrei. [klausel]Und darunter: Gekauft "
     "wie gesehen, keine Gewährleistung. [unterschr]Beide unterschreiben, [schluessel]und Christel bekommt die Schlüssel.", P),
    # --- A2 Werkstatt ----------------------------------------------------------------------------------------------------
    ("[werk]Drei Wochen später steht der Wagen in der Werkstatt.", P),
    ("[m1]Der Motor ist hinüber. Und der Schaden war schon beim Kauf da.", P, "Mechanikerin"),
    # --- A3 Vor dem Haus: Herr Burmeister beruft sich auf den Ausschluss -------------------------------------------------
    ("[c1]Herr Burmeister, der Motor war von Anfang an kaputt!", P, "Christel"),
    ("[b2]Davon wusste ich nichts. Und es heißt: gekauft wie gesehen, keine Gewährleistung.", P, "Burmeister"),
    ("[frage]Hält dieser Ausschluss? [frage2]Oder kann Christel trotzdem ihre Mängelrechte geltend machen?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Sachmangel, § 434 (Wortlautkarte) --------------------------------------------------------------------------
    ("[mangel]Erster Schritt: Ist der Wagen mangelhaft? [p434]Nach Paragraf vierhundertvierunddreißig ist die Sache frei "
     "von Sachmängeln, wenn sie bei Gefahrübergang den subjektiven und den objektiven Anforderungen entspricht. "
     "[subj]Subjektiv heißt zuerst: Sie hat die vereinbarte Beschaffenheit. [motor]Vereinbart war: Motor läuft "
     "einwandfrei. Doch der Schaden war schon bei der Übergabe da. [objektiv]Und objektiv eignet sich ein Auto mit "
     "kaputtem Motor nicht für die gewöhnliche Verwendung. [mangelok]Ein Sachmangel liegt also vor. [v059]Die "
     "Einzelheiten zeigt unsere Folge zum Sachmangel.", PS),
    # --- D 2. Ausschluss wirksam? -----------------------------------------------------------------------------------------
    ("[aus]Zweiter Schritt: Ist die Gewährleistung wirksam ausgeschlossen? [priv]Christel kauft privat, von einer "
     "Privatperson. [v476]Paragraf vierhundertsechsundsiebzig sperrt solche Ausschlüsse nur beim Verbrauchsgüterkauf, "
     "also wenn ein Unternehmer an einen Verbraucher verkauft. [indiv]Den Ausschluss "
     "haben beide selbst formuliert. Er ist also grundsätzlich wirksam. [agb]Stünde er in vorformulierten Allgemeinen "
     "Geschäftsbedingungen, könnte er nach Paragraf dreihundertneun Nummer sieben die Haftung für Schäden an Leben, "
     "Körper und Gesundheit und für grobes Verschulden nicht ausschließen.", PS),
    # --- E 3. Reichweite: „gekauft wie gesehen“ -------------------------------------------------------------------------
    ("[ausl]Dritter Schritt: Wie weit reicht der Ausschluss? [gesehen]Gekauft wie gesehen allein meint nach dem "
     "Bundesgerichtshof in aller Regel nur Mängel, die man bei der Besichtigung wahrnehmen kann, vor allem sichtbare. "
     "[unsicht]Den Motorschaden konnte Christel nicht sehen. [keine]Aber hier steht zusätzlich: keine Gewährleistung. "
     "[umfass]Diese Verbindung versteht der Bundesgerichtshof als umfassenden Ausschluss. [zwerg]Er erfasst also "
     "grundsätzlich auch den versteckten Motorschaden.", PS),
    # --- F 4. § 444 (Wortlautkarte) ----------------------------------------------------------------------------------------
    ("[p444]Grenzen zieht Paragraf vierhundertvierundvierzig: Auf eine Vereinbarung, durch welche die Rechte des Käufers "
     "wegen eines Mangels ausgeschlossen oder beschränkt werden, kann sich der Verkäufer nicht berufen, soweit er den "
     "Mangel arglistig verschwiegen oder eine Garantie für die Beschaffenheit der Sache übernommen hat. [arg]Arglist "
     "scheidet aus: Herr Burmeister wusste nichts vom Schaden. [v262]Den Händler, der einen Unfallschaden verschweigt, "
     "und die Anfechtung zeigt unsere Folge zum Unfallwagen. [gar]Und eine Garantie? Sie geht weiter als eine bloße "
     "Angabe: Der Verkäufer haftet dann sogar ohne Verschulden auf Schadensersatz. [privgar]Beim Privatverkauf nimmt der "
     "Bundesgerichtshof eine Garantie ohne ausdrückliche Abrede nur unter besonderen Umständen an. [garnein]Die gibt es "
     "hier nicht. Paragraf vierhundertvierundvierzig hilft Christel also nicht.", PS),
    # --- G 5. Die vereinbarte Beschaffenheit geht vor (BGHZ 170, 86) ------------------------------------------------------
    ("[vorrang]Hat Christel damit verloren? Nein. Entscheidend ist der Satz: Motor läuft einwandfrei. [bghz]Der "
     "Bundesgerichtshof hat zweitausendsechs entschieden: Vereinbaren die Parteien eine bestimmte Beschaffenheit und "
     "zugleich einen pauschalen Ausschluss, gilt der Ausschluss in der Regel nicht für das Fehlen der vereinbarten Beschaffenheit. "
     "[sinn]Sonst wäre die Vereinbarung für den Käufer ohne Sinn und Wert. [heute]Das ist ständige Rechtsprechung, auch "
     "bei alten Autos und bei Teilen, die verschleißen. [ergeb]Der Ausschluss gilt hier also nur für andere Mängel. "
     "Für den vereinbarten Motor haftet Herr Burmeister.", PS),
    # --- H 6. Ergebnis je Variante -------------------------------------------------------------------------------------------
    ("[var]Das Ergebnis hängt also an einzelnen Sätzen im Vertrag. [va1]Ohne den Satz zum Motor greift der Ausschluss, "
     "und Christel hat keine Mängelrechte. [va2]Stünde dort nur gekauft wie gesehen, wäre der unsichtbare Motorschaden "
     "in der Regel nicht erfasst. [va3]Hätte Herr Burmeister den Schaden arglistig verschwiegen oder eine Garantie übernommen, "
     "könnte er sich nach Paragraf vierhundertvierundvierzig nicht auf den Ausschluss berufen. [va4]Und in unserem Fall geht die vereinbarte Beschaffenheit vor: "
     "Christel kann ihre Mängelrechte geltend machen, [v063]zuerst die Nacherfüllung. Mehr dazu in unserer Folge zu den "
     "Käuferrechten.", PS),
    # --- I Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe einen Ausschluss immer in drei Schritten. Ist er wirksam? Wie weit reicht er? Und darf "
     "sich der Verkäufer nach Paragraf vierhundertvierundvierzig darauf berufen? [tipp2]Lies dafür den ganzen Vertrag, "
     "nicht nur die Klausel. [tipp3]Ist daneben eine Beschaffenheit vereinbart, nimmt der Ausschluss sie in der Regel aus. "
     "Eine Garantie braucht es dafür nicht.", PS),
    # --- J Prüfungsschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfungsschema: Christel gegen Herrn Burmeister, Mängelrechte aus Paragraf vierhundertsiebenunddreißig. "
     "[s1]Römisch eins: Kaufvertrag und Sachmangel bei Gefahrübergang. [s2]Römisch zwei: der Gewährleistungsausschluss. "
     "[s2a]Erstens: wirksam vereinbart, kein Verbrauchsgüterkauf. [s2b]Zweitens: die Reichweite. Gekauft wie gesehen, "
     "keine Gewährleistung, schließt grundsätzlich umfassend aus. [s2c]Drittens: Paragraf vierhundertvierundvierzig. "
     "Arglist und Garantie fehlen. [s2d]Viertens: Der Ausschluss gilt nicht für die vereinbarte Beschaffenheit. "
     "[s3]Römisch drei: Ergebnis. Christel hat ihre Mängelrechte.", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Gekauft wie gesehen, keine Gewährleistung, schließt beim Privatkauf viel aus. "
     "[merk2]Aber regelmäßig nicht, was als Beschaffenheit vereinbart ist, und nie bei Arglist oder Garantie.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    assert not re.search(r"\bBGB\b|\bBGH\b|\bAGB\b|\d|§", text), "Abkürzung oder Ziffer im Sprechtext"
    assert not re.search(r"Christels|Burmeisters", text), "Genitiv eines Namens"
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
