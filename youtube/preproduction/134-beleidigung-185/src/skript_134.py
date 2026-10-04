"""Folge 134 · Beleidigung, üble Nachrede, Verleumdung: §§ 185–187 StGB erklärt (Mi · Examenswissen · Strafrecht/StGB BT,
Format Schema). Fall nach dem Plan-Hook: In der geschlossenen Chatgruppe „Nachbarn Ahornweg“ (63 Mitglieder) schreibt
Hannelore über Henner „Idiot“, Dörte behauptet, Henner schlage seine Kinder (Belege keine, nicht aufklärbar).
Variante: Dörte weiß, dass es nicht stimmt. Keine Kinder im Bild, keine Gewaltdarstellung (nur Chat-Blasen, Handys).
Aufbau: 1. Werturteil vs. Tatsachenbehauptung (BVerfGE 90, 241 Rn. 26 f.; BVerfGE 93, 266 Rn. 120) → 2. § 185 (Wortlautkarte;
Kundgabe der Missachtung: BGH 2 StR 302/08 Rn. 26, OLG Hamm 5 ORs 94/25 Rn. 15) mit § 193/Art. 5 I GG-Abwägung für
Hannelore (BVerfG 1 BvR 2397/19 Rn. 15, 26, 29, 33, 34) → 3. § 186 (Wortlautkarte auszugsweise; „nicht erweislich wahr“;
Beweisregel BVerfG 1 BvR 3388/14 Rn. 17; „objektive Bedingung der Strafbarkeit“ als herrschende Lehre offengelegt) mit
§ 193 und Sorgfaltspflicht (1 BvR 3388/14 Rn. 20 f.; BVerfGE 99, 185 Rn. 54 f.) → 4. § 187 (Wortlautkarte auszugsweise;
bewusst unwahr nicht geschützt: BVerfGE 90, 241 Rn. 28; 99, 185 Rn. 52); Qualifikation „öffentlich …“ für die geschlossene
Chatgruppe offen gelassen → § 194 Abs. 1 (ein Satz) → Abgrenzungstabelle, Ergebnis → Klausurtipp (Schmähkritik eng,
1 BvR 2397/19 Rn. 15, 19) → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Figuren: Henner (stephan), Hannelore (hilde), Dörte (lucy); Lexi/Erzählerin Carla. christian nicht verwendet.
Namen mit eindeutig deutscher Aussprache, nicht vergeben, nicht im Genitiv.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.55

STIMMEN = {"Henner": "stephan", "Hannelore": "hilde", "Dörte": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall ------------------------------------------------------------------------------------------------------------
    ("[fall]Die Chatgruppe „Nachbarn Ahornweg“ hat dreiundsechzig Mitglieder. [party]Es geht um die laute Gartenparty "
     "von Henner am Wochenende. [idiot]Hannelore schreibt: Henner ist ein Idiot. [kinder]Dörte legt nach: Henner schlägt "
     "seine Kinder. [beleg]Belege hat sie keine. Ob es stimmt, lässt sich nicht klären.", 0.3),
    ("[h1]Das ist eine Lüge! Ich stelle Strafantrag.", 0.3, "Henner"),
    ("[frage]Wer hat sich strafbar gemacht? [var]Und was gilt, wenn Dörte weiß, dass ihre Behauptung nicht stimmt?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Werturteil oder Tatsachenbehauptung --------------------------------------------------------------------------
    ("[schritt1]Der erste Schritt bei jedem Ehrdelikt: Ist die Äußerung ein Werturteil oder eine Tatsachenbehauptung? "
     "[wert]Ein Werturteil ist durch Stellungnahme und Dafürhalten geprägt. Es lässt sich nicht als wahr oder unwahr "
     "erweisen. [tats]Bei einer Tatsachenbehauptung steht die Beziehung zur Wirklichkeit im Vordergrund. Sie lässt sich "
     "überprüfen. [beweis]Das Kriterium ist also die Beweisbarkeit. [kontext]Maßgeblich ist der Sinn, den ein "
     "unvoreingenommenes und verständiges Publikum der Äußerung entnimmt, ausgehend vom Wortlaut, mit Kontext und "
     "Begleitumständen.", PS),
    ("[sub1]„Idiot“ ist eine Bewertung, beweisen lässt sie sich nicht: ein Werturteil. [sub2]Ob Henner seine Kinder "
     "schlägt, ist dagegen ein Vorgang, den man beweisen könnte: eine Tatsachenbehauptung.", PS),
    # --- D 2. Beleidigung, § 185 -------------------------------------------------------------------------------------------
    ("[p185]Für Hannelore: Beleidigung, Paragraf hundertfünfundachtzig. [wl185]Das Gesetz nennt nur die Strafe. Was eine "
     "Beleidigung ist, sagt es nicht. [kund]Die Rechtsprechung versteht darunter einen Angriff auf die Ehre eines anderen "
     "durch Kundgabe der Missachtung oder Nichtachtung. [erfasst]Erfasst sind Werturteile, gegenüber dem Betroffenen oder "
     "gegenüber Dritten. [t185]Nach allgemeiner Ansicht auch ehrenrührige Tatsachen, aber nur gegenüber dem Betroffenen "
     "selbst.", P),
    ("[sub185]Hannelore nennt Henner vor der ganzen Gruppe einen Idioten. Damit spricht sie ihm seinen Wert ab: Kundgabe "
     "der Missachtung. [vors185]Das weiß und will sie: Vorsatz.", PS),
    # --- E Rechtswidrigkeit: § 193 und Abwägung ----------------------------------------------------------------------------
    ("[rw185]Ist das gerechtfertigt? [p193]Hier kommt Paragraf hundertdreiundneunzig ins Spiel, die Wahrnehmung "
     "berechtigter Interessen. [abw]Über ihn wirkt die Meinungsfreiheit aus Artikel fünf Absatz eins Grundgesetz: Im "
     "Regelfall sind Meinungsfreiheit und Ehre abzuwägen.", 0.3),
    ("[ha1]Ich darf doch wohl meine Meinung sagen!", 0.3, "Hannelore"),
    ("[abw2]Sie darf, aber nicht um jeden Preis. Das Schimpfwort trägt zur Sache nichts bei. [schrift]Es steht "
     "schriftlich und dauerhaft im Chat, vor dreiundsechzig Nachbarn. [ehre]Die Ehre wiegt schwerer. Hannelore ist wegen "
     "Beleidigung strafbar.", PS),
    # --- F 3. Üble Nachrede, § 186 -----------------------------------------------------------------------------------------
    ("[p186]Für Dörte: üble Nachrede, Paragraf hundertsechsundachtzig. [wl186]Das Gesetz verlangt, in Beziehung auf einen "
     "anderen eine Tatsache zu behaupten oder zu verbreiten, [ehrenr]die ihn verächtlich zu machen oder in der öffentlichen "
     "Meinung herabzuwürdigen geeignet ist. [sub186]Dörte behauptet gegenüber den anderen Mitgliedern, Henner schlage seine "
     "Kinder. Das ist ehrenrührig. [vors186]Vorsatz hat sie.", P),
    ("[erweis]Strafbar ist das aber nur, wenn nicht diese Tatsache erweislich wahr ist. [risiko]Bleibt offen, ob die "
     "Behauptung stimmt, geht das zulasten dessen, der sie aufstellt. [obj]Die herrschende Lehre sieht darin eine objektive "
     "Bedingung der Strafbarkeit: Der Vorsatz muss sich darauf nicht beziehen. [sub_erw]Hier lässt sich nicht klären, ob "
     "es stimmt. Die Bedingung ist erfüllt.", 0.3),
    ("[do1]Ich wollte die Nachbarn doch nur warnen!", 0.3, "Dörte"),
    ("[rw186]Hilft Paragraf hundertdreiundneunzig? [sorg]Bei Tatsachen, deren Wahrheit sich nicht erweisen lässt, nur, "
     "wenn die Äußernde vorher sorgfältig geprüft hat. Je schwerer der Vorwurf, desto höher die Anforderungen. "
     "[sorg2]Dörte hat keine Belege und streut einen schweren Vorwurf vor dreiundsechzig Leuten. [erg186]Sie ist wegen "
     "übler Nachrede strafbar.", PS),
    # --- G 4. Verleumdung, § 187; Qualifikation; § 194 --------------------------------------------------------------------
    ("[p187]Jetzt die Variante: Dörte weiß, dass es nicht stimmt. [wl187]Dann greift die Verleumdung, Paragraf "
     "hundertsiebenundachtzig: wider besseres Wissen eine unwahre Tatsache behaupten oder verbreiten. [unwahr]Die "
     "Unwahrheit gehört hier zum Tatbestand und muss feststehen. [wissen]Wider besseres Wissen heißt: Dörte kennt sie "
     "sicher. [schutz]Bewusst unwahre Tatsachenbehauptungen schützt die Meinungsfreiheit nicht. [erg187]Dörte ist dann "
     "wegen Verleumdung strafbar.", PS),
    ("[quali]Alle drei Tatbestände haben einen höheren Strafrahmen, wenn die Tat öffentlich, in einer Versammlung oder "
     "durch Verbreiten eines Inhalts begangen ist. [offen]Ob eine geschlossene Chatgruppe dafür reicht, hängt vom "
     "Einzelfall ab. Unser Sachverhalt lässt das offen. [antrag]Verfolgt werden die Taten grundsätzlich nur auf Antrag, "
     "Paragraf hundertvierundneunzig Absatz eins. Henner hat ihn gestellt.", PS),
    # --- H Abgrenzungstabelle und Ergebnis ---------------------------------------------------------------------------------
    ("[tab]Die Abgrenzung auf einen Blick: [z185]Paragraf hundertfünfundachtzig erfasst Werturteile gegenüber jedem, "
     "Tatsachen nur gegenüber dem Betroffenen. [z186]Paragraf hundertsechsundachtzig: ehrenrührige Tatsachen gegenüber "
     "Dritten, die nicht erweislich wahr sind. [z187]Paragraf hundertsiebenundachtzig: unwahre Tatsachen gegenüber Dritten, "
     "wider besseres Wissen. [erg]Im Ergebnis: Hannelore Beleidigung, [erg2]Dörte üble Nachrede, [erg3]in der Variante "
     "Verleumdung.", PS),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Nimm nicht vorschnell Schmähkritik an. [tipp2]Sie liegt nur vor, wenn die Äußerung keinen "
     "nachvollziehbaren Bezug mehr zu einer sachlichen Auseinandersetzung hat. [tipp3]Im Regelfall musst du abwägen, und "
     "zwar bei Paragraf hundertdreiundneunzig.", PS),
    # --- J Klausurschema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k0]Vorweg: Werturteil oder Tatsache, und wem gegenüber? [k1]Römisch eins, Tatbestand: "
     "[k1a]die ehrverletzende Äußerung nach Paragraf hundertfünfundachtzig, hundertsechsundachtzig oder "
     "hundertsiebenundachtzig, [k1b]gegebenenfalls die Qualifikation, [k1c]dazu Vorsatz, bei der Verleumdung wider besseres "
     "Wissen. [k2]Römisch zwei, nur bei der üblen Nachrede: nicht erweislich wahr. [k3]Römisch drei, Rechtswidrigkeit mit "
     "Paragraf hundertdreiundneunzig und der Abwägung. [k4]Römisch vier, Schuld. [k5]Römisch fünf, der Strafantrag.", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Werturteile prüfst du bei Paragraf hundertfünfundachtzig. [m2]Ehrenrührige Tatsachen gegenüber Dritten "
     "bei hundertsechsundachtzig, wenn sie nicht erweislich wahr sind, [m3]und bei hundertsiebenundachtzig, wenn der Täter "
     "ihre Unwahrheit kennt.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
