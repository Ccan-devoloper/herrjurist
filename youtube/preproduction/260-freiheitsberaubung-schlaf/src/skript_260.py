"""Folge 260 · Freiheitsberaubung § 239 im Schlaf: Muss das Opfer es merken? (Mi · Examenswissen · StGB BT · Streitstand).
Beispielfall nach dem Plan-Hook: Eine Altbauwohnung, nachts. Vermieter Herr Gerber (wohnt selbst in der Wohnung) ärgert sich
über seinen Untermieter Joscha und schließt um ein Uhr dessen Zimmertür von außen ab; das Zimmer hat keinen anderen Ausgang.
Gerber ist sicher, dass Joscha bis zum Morgen durchschläft. Um drei Uhr schließt er wieder auf. Joscha schläft durch und merkt
nichts.
Aufbau (Streitstand): Fall → Frage → Sachverhalt → § 239 Abs. 1 (Wortlautkarte), Rechtsgut Fortbewegungsfreiheit →
Ansicht 1 potenzielle Fortbewegungsfreiheit (BGH 5 StR 406/21 Rn. 21, 24 f.) → Ansicht 2 aktuelle Fortbewegungsfreiheit
(Darstellung BGH Rn. 22) → Was sagt der BGH (Urt. v. 8.6.2022 – 5 StR 406/21: List-/Täuschungsfall, Rn. 8 f., 19, 21, 23–27;
BGHSt 14, 314, 316 nur als von Rn. 21 zitierte Linie seit 1960) → Lösung je Ansicht, Versuch § 239 Abs. 2 (Wortlautkarte)
als Auffang, scheitert am Tatentschluss (vgl. BGH Rn. 26, § 22 StGB) → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
Belege: ../RECHTSSTAND.md. Namen (eindeutig deutsche Aussprache, nicht vergeben, eingetragen als „260: Gerber, Timo“ und
„260: Joscha (ersetzt Timo …)“): Herr Gerber (helmut, Mann, älter), Joscha (niklas, Mann, jung); ela_froh und julia nicht
verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Gerber": "helmut", "Joscha": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Nacht in der Altbauwohnung -------------------------------------------------------------------------
    ("[fall]Eine Altbauwohnung, kurz vor ein Uhr nachts. [joscha]Untermieter Joscha schläft fest in seinem Zimmer. "
     "[gerber]Sein Vermieter, Herr Gerber, wohnt in derselben Wohnung und ärgert sich über ihn. [schliesst]Gerber schließt das Zimmer "
     "von außen ab und steckt den Schlüssel ein. [ausgang]Einen anderen Ausgang hat das Zimmer nicht.", 0.3),
    ("[g1]Bis drei bleibt die Tür zu. Merkt er ja eh nicht.", 0.4, "Gerber"),
    ("[sicher]Gerber ist sicher, dass Joscha bis zum Morgen durchschläft. [drei]Um drei Uhr schließt er wieder auf. "
     "[morgen]Um sieben wacht Joscha auf.", 0.3),
    ("[j1]Ah, ich hab super geschlafen!", 0.4, "Joscha"),
    ("[frage]Joscha hat nichts gemerkt. Hat Gerber sich trotzdem wegen Freiheitsberaubung strafbar gemacht? "
     "[frage2]Muss das Opfer die Freiheitsberaubung überhaupt bemerken?", 0.5),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 239 Abs. 1 (Wortlautkarte), Rechtsgut ----------------------------------------------------------------------
    ("[norm]Paragraf zweihundertneununddreißig Absatz eins: [wl]Wer einen Menschen einsperrt oder auf andere Weise der "
     "Freiheit beraubt, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe bestraft. [rg]Geschützt ist die "
     "Fortbewegungsfreiheit: die Freiheit, seinen Aufenthalt nach eigenem Belieben zu verändern. [einsp]Gerber schließt "
     "die einzige Tür ab. Joscha könnte das Zimmer nicht verlassen, selbst wenn er wollte. [kern]Aber er will gar nicht: "
     "Er schläft. Genau hier beginnt der Streit.", PS),
    # --- D Ansicht 1: potenzielle Fortbewegungsfreiheit ----------------------------------------------------------------
    ("[pot]Erste Ansicht: Geschützt ist die potenzielle Fortbewegungsfreiheit. [pot2]Entscheidend ist nur, ob sich das "
     "Opfer fortbewegen könnte, wenn es wollte. [pot3]Ob es die Beschränkung überhaupt bemerkt, ist ohne Belang. "
     "Geschützt sind also auch Schlafende. [potarg]Dafür spricht der Wortlaut: Der Freiheit beraubt ist, wer nicht weg "
     "kann. Anders als die Nötigung verlangt die Norm nicht, dass dem Opfer ein Verhalten aufgezwungen wird.", P),
    # --- E Ansicht 2: aktuelle Fortbewegungsfreiheit --------------------------------------------------------------------
    ("[akt]Zweite Ansicht, im Schrifttum weit verbreitet: Geschützt ist nur die aktuelle Fortbewegungsfreiheit. "
     "[akt2]Der Freiheit beraubt ist nur, wer sich zu einem bestimmten Zeitpunkt wegbewegen will, aber nicht kann. "
     "[aktarg]Das Argument: Seit der Reform von neunzehnhundertachtundneunzig ist schon der Versuch strafbar. Wer bloß die "
     "Möglichkeit schützt, verlegt die Vollendung zu weit nach vorn. [aktarg2]Die Freiheitsberaubung sei letztlich ein "
     "Spezialfall der Nötigung.", PS),
    # --- F Was sagt der BGH? -------------------------------------------------------------------------------------------
    ("[bgh]Und der Bundesgerichtshof? Er folgt seit Langem der ersten Ansicht, schon in einem Urteil von "
     "neunzehnhundertsechzig. [bgh2]Im Juni zweitausendzweiundzwanzig hat er daran festgehalten. [bghfall]Dort ging es "
     "nicht um einen Schlafenden: Angehörige brachten eine junge Frau unter einem Vorwand im Auto zum Flughafen und im "
     "Flugzeug ins Ausland. Sie fuhr mit, weil sie getäuscht war.", P),
    ("[bghrn]Der BGH: Paragraf zweihundertneununddreißig schützt die potenzielle persönliche Bewegungsfreiheit. Ob der "
     "Betroffene seine Freiheitsbeschränkung überhaupt realisiert, ist ohne Belang. [bgherg]Das erschlichene "
     "Einverständnis half den Angeklagten deshalb nicht; die Verurteilung wegen Freiheitsberaubung blieb bestehen.", P),
    ("[bghgr]Die Gründe: der Wortlaut und das hohe Gut der Bewegungsfreiheit. [bghsys]Außerdem wird die "
     "Freiheitsberaubung schwerer bestraft als die Nötigung und steht vor ihr im Gesetz; ein bloßer Spezialfall sei sie "
     "nicht. [bghvers]Und für den Versuch bleibt Raum: etwa, wenn der Täter jemanden einschließen will, aber der Schlüssel "
     "nicht passt.", PS),
    # --- G Lösung im Fall ------------------------------------------------------------------------------------------------
    ("[loes]Zurück zu Gerber. [loes1]Nach der ersten Ansicht und dem BGH ist Joscha der Freiheit beraubt: Zwei Stunden lang "
     "hätte er sein Zimmer nicht verlassen können, wenn er gewollt hätte. [loes2]Dass er schlief und nichts merkte, ist "
     "egal. [vors]Gerber wusste, dass er die einzige Tür abschließt, und wollte das. [rw]Rechtfertigungs- und "
     "Entschuldigungsgründe sind nicht ersichtlich. [erg1]Ergebnis: vollendete Freiheitsberaubung.", P),
    ("[erg2]Nach der zweiten Ansicht fehlt der Erfolg: Joscha wollte in diesen zwei Stunden nirgendwohin. "
     "[vers]Bleibt der Versuch, Paragraf zweihundertneununddreißig Absatz zwei: Der Versuch ist strafbar. "
     "[tatent]Dafür bräuchte Gerber den Tatentschluss, Joscha an einem Fortbewegungswillen zu hindern. Er war aber sicher, "
     "dass Joscha durchschläft. [erg3]Nach dieser Ansicht ist Gerber nicht wegen Freiheitsberaubung strafbar. [abw]Anders nur, wenn er damit gerechnet "
     "hätte, dass Joscha aufwacht und hinauswill.", P),
    ("[streit]Weil die Ansichten zu verschiedenen Ergebnissen führen, musst du den Streit entscheiden. [streit2]Gut begründen "
     "lässt sich die erste Ansicht, mit dem BGH: Wortlaut und Systematik sprechen für sie. Dann ist Gerber strafbar.", PS),
    # --- H Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Den Streit brauchst du nur, wenn er den Fall entscheidet. [tipp1]Wollte das Opfer weg und konnte "
     "nicht, sind sich beide Ansichten einig; dann genügt ein Satz. [tipp2]Bei Schlafenden oder Getäuschten gehört der "
     "Streit in den Taterfolg: der Freiheit beraubt. [tipp3]Und folgst du der zweiten Ansicht, prüfe danach den Versuch, mit dem "
     "Tatentschluss als Schwerpunkt.", PS),
    # --- I Schema ----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für Paragraf zweihundertneununddreißig. [s1]Römisch eins, Tatbestand. Objektiv: ein Mensch, "
     "[s2]eingesperrt oder auf andere Weise der Freiheit beraubt; hier liegt der Streit. [s3]Subjektiv: Vorsatz. "
     "[s4]Römisch zwei, Rechtswidrigkeit. [s5]Römisch drei, Schuld. [s6]Scheitert die Vollendung, der Versuch nach "
     "Absatz zwei. [s7]Den dreistufigen Aufbau zeigt dir Folge elf.", PS),
    # --- J Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Nach dem BGH schützt Paragraf zweihundertneununddreißig die potenzielle Fortbewegungsfreiheit. "
     "[m2]Der Freiheit beraubt ist, wer nicht weg könnte, wenn er wollte. Merken muss er es nicht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
