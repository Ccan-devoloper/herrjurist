"""Folge 199 · Tanken ohne Geld – der Tankstellenfall: Vertrag an der Zapfsäule? (Mo · Der Fall · BGB AT, Klassiker-Fall).
Leitentscheidung: BGH, Urt. v. 4.5.2011 – VIII ZR 171/10, NJW 2011, 2871 (Volltext amtliches Portal, Rn. 1–27 gelesen).
Kaufvertrag schon mit dem Tanken (Rn. 13–16), Fälligkeit (Rn. 17), Verzug ohne Mahnung beim Wegfahren (Rn. 18–21),
Detektivkosten als Verzugsschaden (Rn. 23–26). Die Verteilung von Angebot und Annahme (betriebsbereite Säule als Angebot,
§§ 145, 151 BGB) stammt vom Berufungsgericht (Rn. 8); der BGH bestätigt das Ergebnis (Rn. 11) und begründet mit der
Interessenlage, ohne § 151 zu nennen → keine § 151-Wortlautkarte. Eigentum: vom BGH offengelassen („jedenfalls zur
Besitzverschaffung“, Rn. 16) → Meinungsstand OLG Düsseldorf NStZ 1982, 249 / OLG Hamm NStZ 1983, 266, OLG Koblenz
2 Ss 206/98. Strafrecht nur ein Satz mit Verweis auf Folge 022. Personen und Tankstelle fiktiv, keine Marke.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Liste des Auftrags, Volltextsuche 04.10.2026):
Armin (Kunde, Stimme marc), Margarete (Pächterin, Stimme laura_ruhig) – nie im Genitiv. Lexi = Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter. Belege: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Armin": "marc", "Margarete": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: an der Zapfsäule -----------------------------------------------------------------------------------------
    ("[fall]Du tankst für achtzig Euro, gehst zur Kasse – und dein Portemonnaie liegt zu Hause. [armin]So geht es Armin an "
     "einem Samstagmorgen. [saeule]An einer Selbstbedienungstankstelle tankt er seinen Kombi voll. [kasse]Dann geht er in "
     "den Shop zur Kasse [tasche]und greift in die Jackentasche.", P),
    ("[a1]Oh nein! Mein Portemonnaie liegt noch zu Hause auf dem Küchentisch.", P, "Armin"),
    # --- A2 Fall: an der Kasse ---------------------------------------------------------------------------------------------
    ("[marg]Hinter der Kasse steht Pächterin Margarete.", P),
    ("[g1]Achtzig Euro an Säule vier. Das Benzin ist aber schon in Ihrem Tank.", P, "Margarete"),
    ("[a2]Heißt das, ich habe schon gekauft? Bezahlt wird doch erst hier an der Kasse.", P, "Armin"),
    ("[frage]Wann kommt der Kaufvertrag zustande: schon an der Zapfsäule oder erst an der Kasse? [frage2]Und wem gehört das "
     "Benzin im Tank? [bgh]Darüber hat der Bundesgerichtshof entschieden, [bgh2]am vierten Mai zweitausendelf.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Angebot und Annahme: zwei Deutungen -----------------------------------------------------------------------------
    ("[ansp]Margarete verlangt achtzig Euro aus Paragraf vierhundertdreiunddreißig Absatz zwei BGB. [vert]Dafür braucht es "
     "einen Kaufvertrag, also Angebot und Annahme. [p145]Paragraf hundertfünfundvierzig: Wer einem anderen die Schließung "
     "eines Vertrags anträgt, ist an den Antrag gebunden. [zwei]Zwei Deutungen kommen in Betracht. [d1]Erstens: Die "
     "betriebsbereite Zapfsäule ist schon das Angebot, und Armin nimmt es an, indem er tankt. [d2]Zweitens: Die Säule lädt "
     "nur ein, und Armin macht sein Angebot erst an der Kasse, wie im Supermarkt.", PS),
    # --- D Der Fall des BGH ------------------------------------------------------------------------------------------------
    ("[urteil]Im Fall des BGH hatte ein Kunde für zehn Euro und einen Cent Diesel getankt, [riegel]an der Kasse aber nur "
     "einen Schokoriegel und zwei Vignetten bezahlt. [detek]Die Betreiberin ließ ihn von einem Detektivbüro ermitteln und "
     "verlangte die Kosten. [lg]Das Landgericht sah in der betriebsbereiten Zapfsäule ein Angebot, das der Kunde durch das "
     "Tanken annimmt, Paragrafen hundertfünfundvierzig und hunderteinundfünfzig. [bghja]Der BGH bestätigt das Ergebnis: "
     "Wer an einer Selbstbedienungstankstelle tankt, schließt bereits in diesem Zeitpunkt den Kaufvertrag. [nkasse]Nicht "
     "erst an der Kasse.", PS),
    # --- E Die Gründe ------------------------------------------------------------------------------------------------------
    ("[gr]Warum? [laden]Im Supermarkt kann man die Ware zurück ins Regal legen; das Herausnehmen bindet noch nicht. "
     "[tank]Benzin im Tank lässt sich dagegen praktisch nicht mehr zurückgeben. [betr]Der Betreiber hat mit dem Tanken "
     "jedenfalls den Besitz schon verschafft, und ohne Vertrag würde er das in der Regel nicht tun. [kunde]Und der redliche Kunde will "
     "das Benzin behalten dürfen, ohne dass es davon abhängt, ob der Betreiber an der Kasse noch mitmacht. [obj]Aus Sicht "
     "eines objektiven Beobachters steht der Vertrag also schon mit dem Einfüllen, ohne weitere Erklärung an der Kasse. "
     "[armfalsch]Armin hat also schon gekauft.", PS),
    # --- F Eigentum am Benzin ----------------------------------------------------------------------------------------------
    ("[eig]Aber wem gehört das Benzin? [abstr]Der Kaufvertrag verpflichtet nur. Das Eigentum geht durch eine eigene "
     "Übereignung über, Paragraf neunhundertneunundzwanzig Satz eins: [w929]Erforderlich ist, dass der Eigentümer die Sache "
     "dem Erwerber übergibt und beide darüber einig sind, dass das Eigentum übergehen soll. [ueberg]Übergeben ist das "
     "Benzin mit dem Tanken. [einig]Aber sind sich beide schon einig?", PS),
    ("[offen]Der BGH entscheidet das nicht; er spricht nur davon, dass der Betreiber jedenfalls den Besitz verschafft hat. "
     "[m1]Das Oberlandesgericht Düsseldorf lässt das Eigentum schon mit dem Einfüllen übergehen. [m2]Die "
     "Oberlandesgerichte Hamm und Koblenz sagen: Ware gegen Geld. Das Eigentum geht erst mit der Bezahlung über, [m3]sei es "
     "durch einen stillschweigenden Eigentumsvorbehalt, sei es durch eine Einigung unter der Bedingung der Zahlung. "
     "[misch]Vermischt sich das Benzin mit dem Rest im Tank, kann nach Paragraf neunhundertachtundvierzig zudem "
     "Miteigentum entstehen. [egal]Für die Zahlungspflicht spielt das alles keine Rolle.", PS),
    # --- G Folge: Kaufpreis, Fälligkeit, Verzug ----------------------------------------------------------------------------
    ("[w433]Paragraf vierhundertdreiunddreißig Absatz zwei: Der Käufer ist verpflichtet, dem Verkäufer den vereinbarten "
     "Kaufpreis zu zahlen. [faell]Fällig sind die achtzig Euro sofort, Paragraf zweihunderteinundsiebzig. [verzug]Wer "
     "einfach wegfährt, ohne zu zahlen, kommt nach dem BGH schon damit in Verzug, auch ohne Mahnung. [kosten]Im Fall des "
     "BGH musste der Kunde deshalb auch die Detektivkosten ersetzen.", PS),
    # --- H Praxis: Armin sagt Bescheid -------------------------------------------------------------------------------------
    ("[praxis]Armin fährt nicht einfach weg. Er sagt Margarete Bescheid.", P),
    ("[g2]Kein Problem. Ich notiere Ihren Namen und Ihre Adresse, und Sie bringen das Geld heute noch vorbei.", P, "Margarete"),
    ("[keinrs]Name und Adresse notieren oder ein Pfand nehmen: Das ist Praxis, kein Rechtssatz. [ausw]Den Personalausweis "
     "als Pfand darf die Tankstelle aber nicht verlangen, Paragraf eins Absatz eins Personalausweisgesetz. [straf]Strafbar "
     "ist Armin nicht: Er wollte zahlen und sagt offen Bescheid. [str2]Wer schon beim Tanken nicht zahlen will, begeht "
     "dagegen grundsätzlich einen, zumindest versuchten, Betrug; mehr dazu im Video zum Tankbetrug.", PS),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne zwei Fragen. [tp1]Wann ist der Kaufvertrag geschlossen? An der Selbstbedienungstankstelle "
     "schon mit dem Tanken. [tp2]Wann geht das Eigentum über? Das prüfst du gesondert bei Paragraf "
     "neunhundertneunundzwanzig, und dort ist es streitig. [tp3]Und grenze zum Supermarkt ab: Dort bindet das Herausnehmen "
     "aus dem Regal noch nicht.", PS),
    # --- J Prüfschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [c1]Römisch eins: Anspruch auf den Kaufpreis aus Paragraf vierhundertdreiunddreißig Absatz zwei. "
     "[c2]Erstens: Kaufvertrag durch Angebot und Annahme. [c3]Zweitens: Zeitpunkt: schon mit dem Tanken, nicht erst an der "
     "Kasse. [c4]Drittens: Fälligkeit sofort. [c5]Römisch zwei: Eigentum am Benzin, Paragraf neunhundertneunundzwanzig. "
     "[c6]Erstens: Übergabe mit dem Tanken. [c7]Zweitens: Einigung, streitig: schon beim Einfüllen oder erst mit der "
     "Bezahlung?", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: An der Selbstbedienungstankstelle steht der Kaufvertrag schon mit dem Tanken. [mk2]Wer dann nicht "
     "zahlen kann, schuldet den Kaufpreis trotzdem.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
