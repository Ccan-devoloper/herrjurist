"""Folge 209 · Schadensersatz statt der Leistung §§ 280, 281 BGB – Schema (Mi · Examenswissen · Schuldrecht AT, Format Schema).
Beispielfall nach dem Plan-Hook („Der Händler liefert die bezahlten Felgen nicht – du kaufst woanders teurer ein.“):
Jörn (privat) kauft am 1.9.2026 im Reifenhandel von Ingolf vier Felgen für 1.200 € und zahlt sofort; Lieferung zugesagt bis
8.9.2026. Nichts kommt. Am 10.9. E-Mail „Bitte liefern Sie die Felgen umgehend.“ Ingolf: „Die Felgen kommen bald,
versprochen.“ Drei Wochen später (1.10.) nichts da; Jörn kauft gleichwertige Felgen bei Herta für 1.450 € und schreibt
Ingolf: Felgen nicht mehr, Geld zurück, 250 € Mehrkosten. Ingolf: „Aber die Felgen kommen doch nächste Woche!“
Schema: Anspruchsgrundlage §§ 280 Abs. 1, 3, 281 Abs. 1 S. 1 (Wortlautkarten § 280 Abs. 1, 3; § 281 Abs. 1 S. 1) →
1. Schuldverhältnis → 2. Pflichtverletzung (fällig, durchsetzbar, möglich; Formulierungen wie Folge 116) → 3. Frist
(„umgehend“ genügt: BGH VIII ZR 49/15 Rn. 25, VIII ZR 254/08 Rn. 10 f.; zu kurze Frist: Verweis 116) → 4. Entbehrlichkeit
§ 281 Abs. 2 (Wortlautkarte; VIII ZR 226/14 Rn. 33; BT-Drucks. 14/6040 S. 140) → 5. Vertretenmüssen § 280 Abs. 1 S. 2 →
6. Schaden 1.450 € − 1.200 € = 250 € (§ 249 Abs. 1; VIII ZR 169/12 LS, Rn. 27) → § 281 Abs. 4 (Wortlautkarte;
VIII ZR 169/12 Rn. 29) → Abgrenzung Verzögerungsschaden (Verweis 112), Rücktritt (Verweis 116), § 325 → Ergebnis →
Klausurtipp → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Figuren: Jörn (niklas), Ingolf (helmut), Herta (ela_froh, ein freundlicher Satz); Lexi/Erzählerin Carla. Nie im Genitiv.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Jörn": "niklas", "Ingolf": "helmut", "Herta": "ela_froh"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Kauf im Reifenhandel ----------------------------------------------------------------------------------
    ("[fall]Der Händler liefert die bezahlten Felgen nicht, und du kaufst woanders teurer ein. [joern]So geht es Jörn. "
     "[laden]Am ersten September kauft er im Reifenhandel von Ingolf vier Felgen für tausendzweihundert Euro. "
     "[zahlt]Jörn zahlt sofort.", P),
    ("[in1]Die Felgen liefere ich Ihnen bis zum achten September.", P, "Ingolf"),
    # --- A2 Fall: Warten, E-Mail „umgehend“ -----------------------------------------------------------------------------------
    ("[warten]Doch der achte September vergeht, und nichts kommt. [mail]Am zehnten September schreibt Jörn eine E-Mail.", P),
    ("[jo1]Bitte liefern Sie die Felgen umgehend.", P, "Jörn"),
    ("[antw]Ingolf antwortet knapp.", P),
    ("[in2]Die Felgen kommen bald, versprochen.", P, "Ingolf"),
    # --- A3 Fall: Deckungskauf bei Herta ---------------------------------------------------------------------------------------
    ("[drei]Drei Wochen später ist immer noch nichts da. [herta]Am ersten Oktober fragt Jörn bei Herta nach gleichwertigen "
     "Felgen.", P),
    ("[he1]Die habe ich da, für tausendvierhundertfünfzig Euro.", P, "Herta"),
    # --- A4 Fall: Jörn schreibt Ingolf -----------------------------------------------------------------------------------------
    ("[kauft]Jörn kauft sie und schreibt an Ingolf.", P),
    ("[jo2]Ihre Felgen will ich nicht mehr. Ich will mein Geld zurück, und die zweihundertfünfzig Euro Mehrkosten zahlen Sie "
     "auch!", P, "Jörn"),
    ("[in3]Aber die Felgen kommen doch nächste Woche!", P, "Ingolf"),
    ("[frage]Kann Jörn die Mehrkosten verlangen? [frage2]Und war „umgehend“ überhaupt eine Frist?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Anspruchsgrundlage, § 280 Abs. 1 und 3 (Wortlaut) -------------------------------------------------------------------
    ("[agl]Die Mehrkosten verlangt Jörn als Schadensersatz statt der Leistung. [agl2]Anspruchsgrundlage sind die Paragrafen "
     "zweihundertachtzig Absätze eins und drei und zweihunderteinundachtzig. [sys]Das System dahinter erklärt das Video zum "
     "Schadensersatzschema.", P),
    ("[w280]Paragraf zweihundertachtzig Absatz eins: Verletzt der Schuldner eine Pflicht aus dem Schuldverhältnis, so kann "
     "der Gläubiger Ersatz des hierdurch entstehenden Schadens verlangen. Dies gilt nicht, wenn der Schuldner die "
     "Pflichtverletzung nicht zu vertreten hat. [w3]Absatz drei: Statt der Leistung nur unter "
     "zusätzlichen Voraussetzungen, hier des Paragrafen zweihunderteinundachtzig.", P),
    # --- D § 281 Abs. 1 Satz 1 (Wortlaut) ---------------------------------------------------------------------------------------
    ("[w281]Paragraf zweihunderteinundachtzig Absatz eins Satz eins verlangt zweierlei: [w281a]Der Schuldner erbringt die "
     "fällige Leistung nicht oder nicht wie geschuldet, [w281b]und der Gläubiger hat ihm erfolglos eine angemessene Frist "
     "zur Leistung oder Nacherfüllung bestimmt. [plan]Daraus ergibt sich das Schema in sechs Schritten.", PS),
    # --- E 1. Schuldverhältnis ---------------------------------------------------------------------------------------------------
    ("[s1]Erstens: ein Schuldverhältnis. [s1b]Jörn und Ingolf haben einen Kaufvertrag geschlossen, Paragraf "
     "vierhundertdreiunddreißig.", P),
    # --- F 2. Pflichtverletzung --------------------------------------------------------------------------------------------------
    ("[p1]Zweitens: die Pflichtverletzung. Ingolf erbringt eine fällige, durchsetzbare Leistung nicht. [p2]Vereinbart war "
     "die Lieferung bis zum achten September. Spätestens dann ist sie fällig, und sie bleibt aus. [p3]Durchsetzbar ist sie "
     "auch: Jörn hat schon bezahlt, Ingolf hat keine Einrede.", P),
    # --- G 3. Frist --------------------------------------------------------------------------------------------------------------
    ("[f1]Drittens: eine angemessene Frist, erfolglos abgelaufen. [f2]Jörn hat kein Datum genannt, sondern nur „umgehend“ "
     "geschrieben. [f3]Das genügt. Nach dem Bundesgerichtshof reicht es, wenn der Gläubiger sofortige, unverzügliche oder "
     "umgehende Leistung verlangt. [f4]Ein bestimmter Endtermin ist nicht nötig. [f5]Und eine zu kurze Frist setzt eine angemessene in Gang; das kennst du aus "
     "dem Video zum Rücktritt. [f6]Jörn wartet drei Wochen. Das genügt jedenfalls, um vier Felgen zu liefern. [f7]Die Frist "
     "ist erfolglos abgelaufen.", PS),
    # --- H 4. Entbehrlichkeit, § 281 Abs. 2 (Wortlaut) ---------------------------------------------------------------------------
    ("[e1]Viertens: Manchmal ist die Fristsetzung entbehrlich. [e2]Nach Paragraf zweihunderteinundachtzig Absatz zwei, wenn "
     "der Schuldner die Leistung ernsthaft und endgültig verweigert, [e3]oder wenn besondere Umstände die sofortige "
     "Geltendmachung des Schadensersatzanspruchs rechtfertigen. [e5]An eine Erfüllungsverweigerung stellt der Bundesgerichtshof "
     "strenge Anforderungen: Der Schuldner muss unmissverständlich zum Ausdruck bringen, dass er unter keinen Umständen "
     "leisten wird. [e6]Ingolf vertröstet Jörn nur, er will ja liefern. [e7]Hier war die Frist also nötig, und Jörn hat sie "
     "gesetzt.", PS),
    # --- I 5. Vertretenmüssen ----------------------------------------------------------------------------------------------------
    ("[v1]Fünftens: Vertretenmüssen. [v2]Nach Paragraf zweihundertachtzig Absatz eins Satz zwei wird es vermutet; Ingolf "
     "müsste sich entlasten. [v3]Er nennt keinen Grund für die Verzögerung.", P),
    # --- J 6. Schaden (Rechenweg) ------------------------------------------------------------------------------------------------
    ("[d1]Sechstens: der Schaden. [d2]Jörn ist so zu stellen, als hätte Ingolf ordnungsgemäß geliefert, Paragraf "
     "zweihundertneunundvierzig Absatz eins. [d3]Dann hätte er die Felgen für tausendzweihundert Euro. [d4]Jetzt zahlt er "
     "für gleichwertige Felgen tausendvierhundertfünfzig Euro. [d5]Die Differenz, zweihundertfünfzig Euro, ist sein "
     "Schaden. [d6]Der Bundesgerichtshof sagt ausdrücklich: Die Mehrkosten eines Deckungskaufs sind kein "
     "Verzögerungsschaden, sondern ein Schaden statt der Leistung.", PS),
    # --- K Folge: § 281 Abs. 4 (Wortlaut) ----------------------------------------------------------------------------------------
    ("[r1]Und Ingolf, der nächste Woche doch noch liefern will? [r2]Paragraf zweihunderteinundachtzig Absatz vier: Der "
     "Anspruch auf die Leistung ist ausgeschlossen, sobald der Gläubiger statt der Leistung Schadensersatz verlangt hat. "
     "[r3]Mit seiner E-Mail hat Jörn das getan. [r4]Er kann nicht beides verlangen, die Felgen und den Schadensersatz "
     "statt der Felgen.", PS),
    # --- L Abgrenzung: Verzögerungsschaden, Rücktritt, § 325 ---------------------------------------------------------------------
    ("[ab1]Zur Abgrenzung. [ab2]Schäden, die allein durch die Verspätung entstehen und auch bei späterer Lieferung bleiben, "
     "etwa die Gebühr für einen geplatzten Montagetermin, sind Verzögerungsschaden. [ab2b]Dafür braucht es Verzug, Paragraf "
     "zweihundertachtzig Absatz zwei mit zweihundertsechsundachtzig; mehr im Video zum Schuldnerverzug. [ab3]Und die bezahlten tausendzweihundert Euro? Die bekommt Jörn über den Rücktritt nach Paragraf "
     "dreihundertdreiundzwanzig zurück. [ab4]Paragraf dreihundertfünfundzwanzig stellt klar: Der Rücktritt schließt den "
     "Schadensersatz nicht aus.", PS),
    # --- M Ergebnis --------------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Jörn kann von Ingolf zweihundertfünfzig Euro Schadensersatz statt der Leistung verlangen.", PS),
    # --- N Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Ordne den Schaden zuerst ein. Mehrkosten eines Deckungskaufs sind Schaden statt der Leistung, "
     "[tipp2]also brauchst du grundsätzlich eine erfolglose Frist. [tipp3]Und lies die Erklärung des Gläubigers genau: "
     "Auch „umgehend“ ist eine Fristsetzung.", PS),
    # --- O Klausurschema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema: [k0]Anspruch aus den Paragrafen zweihundertachtzig Absätze eins und drei, zweihunderteinundachtzig. "
     "[k1]Eins: Schuldverhältnis. [k2]Zwei: Pflichtverletzung, also fällige, durchsetzbare Leistung nicht erbracht. "
     "[k3]Drei: angemessene Frist erfolglos abgelaufen, [k4]vier: oder Frist entbehrlich. [k5]Fünf: Vertretenmüssen, "
     "vermutet. [k6]Sechs: Schaden. [k7]Folge: kein Anspruch mehr auf die Leistung.", PS),
    # --- P Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer woanders teurer nachkauft, verlangt Schadensersatz statt der Leistung. [mk2]Den gibt es "
     "grundsätzlich erst nach einer erfolglosen Frist.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
    assert not re.search(r"\b(Jörns|Ingolfs|Hertas)\b", text), "Genitiv eines Namens"
