"""Folge 129 · Mängelrechte Werkvertrag § 634 BGB: Schema und Unterschiede zum Kauf (Fr · Klausurpraxis · Schema).
Beispielfall nach dem Plan-Hook („Das neue Dach ist undicht – und der Dachdecker reagiert nicht auf Anrufe“): Beate lässt
das Dach ihres Hauses vom Dachdecker Herrn Wenzel für 18.000 € neu eindecken, prüft es und nimmt es ab. Zwei Monate später
nach starkem Regen Wasserflecken im Dachgeschoss; ein anderer Dachdecker findet den Anschluss am Schornstein undicht,
Reparatur laut Angebot 2.400 €. Herr Wenzel geht nicht ans Telefon und ruft nicht zurück.
Kern als Schema: 1. Werkvertrag § 631 und Abnahme als Zäsur (Verweis 095), Bauvertrag § 650a (ein Satz); 2. Mangel
§ 633 Abs. 2 (Wortlautkarte auszugsweise), Zeitpunkt Abnahme (BGH VII ZR 301/13 Rn. 32); 3. Rechte aus § 634
(Wortlautkarte): Nacherfüllung § 635 (Wahlrecht Unternehmer, anders § 439 Abs. 1; BGH VII ARZ 1/20 Rn. 27),
Selbstvornahme § 637 Abs. 1 (Wortlautkarte), Entbehrlichkeit (BGH VIII ZR 215/10 Rn. 24), Vorschuss § 637 Abs. 3
(BGH VII ARZ 1/20 Rn. 67; VII ZR 92/20 Rn. 28), Rücktritt/Minderung, Schadensersatz; 4. Verjährung § 634a Abs. 1 Nr. 2,
Abs. 2 (BGH VII ZR 348/13 Rn. 19); 5. Unterschiede zum Kauf als Tabelle. Ergebnis, Klausurtipp, Schema, Merksatz.
Belege: ../RECHTSSTAND.md. Figuren: Beate (ela_froh), Herr Wenzel (helmut); Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Wenzel": "helmut", "Beate": "ela_froh"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: das neue Dach -------------------------------------------------------------------------------------------
    ("[fall]Beate lässt das Dach ihres Hauses neu eindecken, vom Dachdecker Herrn Wenzel, für achtzehntausend Euro. "
     "[fertig]Nach drei Wochen ist er fertig.", P),
    ("[we1]Fertig! Das Dach hält jetzt viele Jahre.", P, "Wenzel"),
    ("[abn]Beate sieht sich alles genau an und nimmt das Dach ab. [bez]Sie zahlt die Rechnung.", P),
    # --- A2 Fall: Regen, Wasserflecken ------------------------------------------------------------------------------------
    ("[regen]Zwei Monate später regnet es stark. [fleck]Im Dachgeschoss zeigen sich Wasserflecken an der Decke. "
     "[gut]Ein anderer Dachdecker stellt fest: Der Anschluss am Schornstein ist undicht. [kost]Die Reparatur kostet "
     "laut seinem Angebot zweitausendvierhundert Euro.", P),
    # --- A3 Fall: niemand geht ran ----------------------------------------------------------------------------------------
    ("[anruf]Beate ruft Herrn Wenzel an. Niemand geht ran.", P),
    ("[be1]Herr Wenzel, mein Dach ist undicht! Bitte rufen Sie mich zurück.", P, "Beate"),
    ("[nie]Auch nach drei weiteren Anrufen: keine Antwort. [frage]Was kann Beate jetzt verlangen? [frage2]Und was ist "
     "anders als beim Kauf?", PS),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Werkvertrag und Abnahme ------------------------------------------------------------------------------------
    ("[p1]Erstens: Werkvertrag und Abnahme. [p1a]Herr Wenzel schuldet einen Erfolg, ein dichtes neues Dach. Das ist ein "
     "Werkvertrag nach Paragraf sechshunderteinunddreißig. [p056]Zur Abgrenzung vom Dienstvertrag gibt es ein eigenes Video. "
     "[p1b]Mängelrechte kann der Besteller grundsätzlich erst nach der Abnahme geltend machen. [p1c]Beate hat abgenommen; "
     "mehr dazu im Video zur Abnahme. [bau]Weil die Neueindeckung einen Teil des Hauses wiederherstellt, ist der Vertrag "
     "zugleich ein Bauvertrag nach Paragraf sechshundertfünfzig a. Dessen Regeln gelten nur ergänzend.", PS),
    # --- D 2. Mangel, § 633 Abs. 2 (Wortlaut auszugsweise) ---------------------------------------------------------------
    ("[m1]Zweitens: der Mangel, Paragraf sechshundertdreiunddreißig Absatz zwei. [m2]Frei von Sachmängeln ist das Werk, "
     "wenn es die vereinbarte Beschaffenheit hat, [m3]sonst wenn es sich für die vertraglich vorausgesetzte, sonst für die gewöhnliche Verwendung eignet. "
     "[m4]Ein Dach muss dicht sein. Am Schornstein dringt Wasser ein: ein Sachmangel. [m5]Maßgeblich ist nach dem "
     "Bundesgerichtshof grundsätzlich der Zeitpunkt der Abnahme. [m6]Der undichte Anschluss war schon da, als Beate "
     "abnahm; nur das Wasser zeigte sich später.", PS),
    # --- E 3. Rechte aus § 634 (Wortlaut), Nacherfüllung § 635 -----------------------------------------------------------
    ("[r1]Drittens: die Rechte aus Paragraf sechshundertvierunddreißig. [r2]Der Besteller kann Nacherfüllung verlangen, "
     "[r3]den Mangel selbst beseitigen und Ersatz der Aufwendungen verlangen, [r4]zurücktreten oder mindern [r5]und "
     "Schadensersatz verlangen. [nach]Zuerst kommt die Nacherfüllung, Paragraf sechshundertfünfunddreißig. [wahl]Wie "
     "nacherfüllt wird, wählt der Unternehmer: Er beseitigt den Mangel oder stellt das Werk neu her. [kauf1]Beim Kauf "
     "wählt dagegen der Käufer, Paragraf vierhundertneununddreißig Absatz eins.", PS),
    # --- F Selbstvornahme, § 637 Abs. 1 (Wortlaut) -----------------------------------------------------------------------
    ("[s1]Jetzt der Klausurklassiker, die Selbstvornahme, Paragraf sechshundertsiebenunddreißig Absatz eins: [s2]Der "
     "Besteller kann wegen eines Mangels des Werkes nach erfolglosem Ablauf einer von ihm zur Nacherfüllung bestimmten "
     "angemessenen Frist den Mangel selbst beseitigen und Ersatz der erforderlichen Aufwendungen verlangen, [s3]wenn "
     "nicht der Unternehmer die Nacherfüllung zu Recht verweigert. [s4]Entscheidend ist die Frist. Entbehrlich ist sie "
     "etwa, wenn der Unternehmer ernsthaft und endgültig verweigert. [s5]Daran stellt der Bundesgerichtshof strenge "
     "Anforderungen. Wer nicht ans Telefon geht, verweigert noch nicht endgültig. [s6]Beate muss also eine Frist "
     "setzen, am besten schriftlich.", PS),
    # --- G Vorschuss, § 637 Abs. 3 ---------------------------------------------------------------------------------------
    ("[v1]Vorfinanzieren muss sie die Reparatur nicht: Nach Absatz drei kann sie Vorschuss verlangen. [v2]Den Vorschuss "
     "muss sie nach dem Bundesgerichtshof für die Reparatur verwenden und danach abrechnen. [kauf2]Im Kaufrecht gibt es "
     "weder Selbstvornahme noch Vorschuss.", PS),
    # --- H Rücktritt, Minderung, Schadensersatz --------------------------------------------------------------------------
    ("[rm1]Rücktritt und Minderung setzen ebenfalls eine erfolglose Frist voraus, Paragrafen sechshundertsechsunddreißig "
     "und dreihundertdreiundzwanzig. [rm2]Bei einem unerheblichen Mangel ist der Rücktritt ausgeschlossen, mindern geht "
     "trotzdem, Paragraf sechshundertachtunddreißig. [se1]Schadensersatz statt der Leistung verlangt zusätzlich, dass "
     "der Unternehmer den Mangel zu vertreten hat; das wird vermutet, Paragrafen zweihundertachtzig und "
     "zweihunderteinundachtzig.", PS),
    # --- I 4. Verjährung, § 634a ------------------------------------------------------------------------------------------
    ("[vj1]Viertens: die Verjährung, Paragraf sechshundertvierunddreißig a. [vj2]Bei einem Bauwerk verjähren die "
     "Ansprüche in fünf Jahren, sonst bei Arbeiten an einer Sache in zwei. [vj3]Nach dem Bundesgerichtshof gehören dazu "
     "auch Arbeiten an einem bestehenden Gebäude, die für seinen Bestand wesentlich sind, wenn die Teile fest mit ihm "
     "verbunden werden. [vj4]Ein neu eingedecktes Dach erfüllt das. [vj5]Die Frist beginnt mit der Abnahme, Absatz "
     "zwei. Beate hat also Zeit.", PS),
    # --- J 5. Unterschiede zum Kauf (Tabelle) -----------------------------------------------------------------------------
    ("[u1]Fünftens: die Unterschiede zum Kauf auf einen Blick. [u2]Das Wahlrecht bei der Nacherfüllung hat beim Kauf der "
     "Käufer, beim Werkvertrag der Unternehmer. [u3]Selbstvornahme und Vorschuss gibt es nur im Werkvertrag. "
     "[u4]Maßgeblich für den Mangel ist beim Kauf der Gefahrübergang, in der Regel die Übergabe, beim Werk die Abnahme. "
     "[u5]Und die Verjährung beginnt beim Kauf mit der Ablieferung, beim Werk mit der Abnahme.", PS),
    # --- K Ergebnis ------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Beate setzt Herrn Wenzel schriftlich eine angemessene Frist zur Nacherfüllung, etwa zwei Wochen. "
     "[erg2]Läuft sie ergebnislos ab, darf sie einen anderen Dachdecker beauftragen [erg3]und von Herrn Wenzel einen "
     "Vorschuss von zweitausendvierhundert Euro verlangen. [erg4]Verjährt ist nichts.", PS),
    # --- L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Hat der Besteller den Mangel beseitigen lassen, ohne vorher eine Frist zu setzen, bekommt er die "
     "Kosten nach Paragraf sechshundertsiebenunddreißig nicht ersetzt. [tipp2]Prüfe deshalb immer zuerst die Frist und "
     "ob sie entbehrlich war.", PS),
    # --- M Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für Aufwendungsersatz und Vorschuss: [k1]Römisch eins: wirksamer Werkvertrag. [k2]Römisch zwei: "
     "Abnahme. [k3]Römisch drei: Mangel bei Abnahme, Paragraf sechshundertdreiunddreißig. [k4]Römisch vier: erfolglose "
     "angemessene Frist zur Nacherfüllung oder ihre Entbehrlichkeit. [k5]Römisch fünf: keine berechtigte Verweigerung "
     "durch den Unternehmer. [k6]Römisch sechs: Ersatz der erforderlichen Aufwendungen oder Vorschuss. [k7]Römisch "
     "sieben: keine Verjährung, Paragraf sechshundertvierunddreißig a.", PS),
    # --- N Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Im Werkvertrag wählt der Unternehmer, wie er nacherfüllt. [mk2]Lässt er die Frist verstreichen, "
     "darf der Besteller den Mangel selbst beseitigen lassen [mk3]und dafür Vorschuss verlangen. Das gibt es beim Kauf "
     "nicht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
