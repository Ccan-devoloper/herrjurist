"""Folge 215 · Differenzhypothese und Naturalrestitution: Schadensrecht §§ 249 ff. BGB – Schema
(Mi · Examenswissen · Zivilrecht/Schuldrecht AT, Format Schema).
Beispielfall nach dem Plan-Hook („Dein Fahrrad wird angefahren – bekommst du die Reparatur oder Geld?“):
Hedi stellt ihr Rad vor einer Bäckerei ab; Ludolf parkt rückwärts aus und fährt es an (Rahmen verbogen, Hinterrad kaputt).
Werkstatt von Trude: Reparatur 400 € plus 76 € Umsatzsteuer; gleichwertiges Rad 900 €. Ludolf will das Rad vom Schwager
reparieren lassen; Hedi will das Geld und selbst entscheiden, was sie damit macht.
Ablauf: Haftungsgrund vorausgesetzt (§ 823 Abs. 1) → 1. Schaden: Differenzhypothese (BGH VI ZR 239/23 Rn. 8) →
2. Herstellung § 249 Abs. 1 (Wortlautkarte) → 3. Geld statt Herstellung § 249 Abs. 2 Satz 1 (Wortlautkarte; Ersetzungsbefugnis
VI ZR 69/12 Rn. 9; erforderlich VI ZR 300/24 Rn. 11), fiktive Abrechnung (VI ZR 9/17 Rn. 7; VI ZR 300/24 Rn. 12), Satz 2
Umsatzsteuer (Wortlautkarte; VI ZR 146/16 Rn. 9), § 250 → 4. Geldentschädigung § 251 Abs. 1 (Wortlautkarte; merkantiler
Minderwert VI ZR 239/23 Rn. 6), Abs. 2 Satz 1 (Wortlautkarte; Vorrang der Herstellung VI ZR 9/17 Rn. 6) → Abwandlung 1.200 €:
Ersatzrad als Herstellung, Wiederbeschaffungsaufwand (VI ZR 174/24 Rn. 21), Kfz 130 % (VI ZR 387/14 Rn. 6 f.) → Ergebnis →
Klausurtipp (VII ZR 46/17 LS 1) → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Figuren: Hedi (lucy), Ludolf (stephan), Trude (hilde); Lexi/Erzählerin Carla. Nie im Genitiv.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Hedi": "lucy", "Ludolf": "stephan", "Trude": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: das Rad wird angefahren -------------------------------------------------------------------------------------
    ("[fall]Dein Fahrrad wird angefahren. Bekommst du die Reparatur oder Geld? [hedi]Hedi stellt ihr Rad vor einer Bäckerei "
     "ab. [stoss]Ludolf parkt rückwärts aus und fährt das Rad an. [kaputt]Der Rahmen ist verbogen, das Hinterrad kaputt.", P),
    ("[lu1]Oh nein, das tut mir leid! Das bringe ich wieder in Ordnung.", P, "Ludolf"),
    # --- A2 Fall: Werkstatt ----------------------------------------------------------------------------------------------------
    ("[werk]Hedi bringt das Rad in die Werkstatt von Trude.", P),
    ("[tr1]Die Reparatur kostet vierhundert Euro, plus sechsundsiebzig Euro Umsatzsteuer.", P, "Trude"),
    ("[wert]Ein gleichwertiges Rad würde neunhundert Euro kosten.", P),
    # --- A3 Fall: Schwager oder Geld -------------------------------------------------------------------------------------------
    ("[idee]Ludolf hat eine andere Idee.", P),
    ("[lu2]Mein Schwager repariert Räder. Der macht das für mich.", P, "Ludolf"),
    ("[he1]Nein danke. Ich will das Geld. Was ich damit mache, entscheide ich.", P, "Hedi"),
    ("[frage]Muss Hedi sich auf den Schwager einlassen? [frage2]Und wie viel Geld bekommt sie, wenn sie gar nicht "
     "reparieren lässt?", PS),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Haftungsgrund vorausgesetzt -----------------------------------------------------------------------------------------
    ("[grund]Dass Ludolf haftet, setzen wir voraus, etwa aus Paragraf achthundertdreiundzwanzig Absatz eins: Er hat "
     "fahrlässig das Eigentum von Hedi verletzt. [grund2]Heute geht es um die Rechtsfolge: Was ist der Schaden, und wie wird "
     "er ersetzt? [sys]Die Anspruchsgrundlagen ordnet das Video zum Schadensersatzschema.", P),
    # --- D 1. Schaden: Differenzhypothese --------------------------------------------------------------------------------------
    ("[dh]Erstens: Gibt es einen Schaden? Das klärt die Differenzhypothese. [dh2]Verglichen wird die tatsächliche "
     "Vermögenslage nach dem Unfall [dh3]mit der Lage, die ohne den Unfall bestehen würde. [dh4]So formuliert es auch der "
     "Bundesgerichtshof. [dh5]Ohne den Unfall hätte Hedi ein heiles Rad, jetzt hat sie ein beschädigtes. [dh6]Diese "
     "Differenz ist ihr Schaden.", PS),
    # --- E 2. Herstellung, § 249 Abs. 1 (Wortlaut) -----------------------------------------------------------------------------
    ("[w1]Zweitens: Wie wird ersetzt? Paragraf zweihundertneunundvierzig Absatz eins: Wer zum Schadensersatz verpflichtet "
     "ist, hat den Zustand herzustellen, der bestehen würde, wenn der zum Ersatz verpflichtende Umstand nicht eingetreten "
     "wäre. [nr]Das ist die Naturalrestitution: Grundsätzlich schuldet der Schädiger Herstellung, nicht Geld. [nr2]Nach "
     "Absatz eins allein könnte Ludolf das Rad also selbst reparieren lassen, etwa beim Schwager.", PS),
    # --- F 3. Geld statt Herstellung, § 249 Abs. 2 Satz 1 (Wortlaut) ----------------------------------------------------------
    ("[w2]Drittens: Absatz zwei Satz eins. Bei der Beschädigung einer Sache kann der Gläubiger statt der Herstellung den "
     "dazu erforderlichen Geldbetrag verlangen. [wahl]Die Wahl liegt also bei Hedi, man spricht von der Ersetzungsbefugnis. "
     "[wahl2]Den Schwager muss sie nicht hinnehmen. [erf]Erforderlich ist, was ein verständiger, wirtschaftlich denkender "
     "Eigentümer aufwenden würde, hier die Reparatur für vierhundert Euro.", P),
    ("[fik]Und wenn Hedi gar nicht reparieren lässt? [fik2]Das darf sie. Sie ist in der Verwendung des Geldes frei und "
     "kann fiktiv abrechnen, also nach den geschätzten Reparaturkosten.", P),
    # --- G § 249 Abs. 2 Satz 2 (Wortlaut), § 250 --------------------------------------------------------------------------------
    ("[w3]Eine Grenze zieht Satz zwei: Der Geldbetrag schließt die Umsatzsteuer nur mit ein, wenn und soweit sie "
     "tatsächlich angefallen ist. [ust]Rechnet Hedi fiktiv ab, bekommt sie vierhundert Euro. [ust2]Lässt sie reparieren, "
     "fällt die Umsatzsteuer an, und die sechsundsiebzig Euro kommen dazu. [p250]Wo Absatz zwei nicht greift, führt "
     "Paragraf zweihundertfünfzig zum Geld: eine Frist zur Herstellung mit der Erklärung, sie danach abzulehnen.", PS),
    # --- H 4. Geldentschädigung, § 251 (Wortlaut) -------------------------------------------------------------------------------
    ("[w4]Viertens: Wann gibt es von vornherein Geld? Paragraf zweihunderteinundfünfzig Absatz eins: Soweit die Herstellung "
     "nicht möglich oder zur Entschädigung des Gläubigers nicht genügend ist, hat der Ersatzpflichtige den Gläubiger in Geld "
     "zu entschädigen. [mmw]Beim Auto gehört dazu der merkantile Minderwert: Ein Unfallwagen bleibt trotz Reparatur weniger "
     "wert.", P),
    ("[w5]Und Absatz zwei Satz eins: Der Ersatzpflichtige kann den Gläubiger in Geld entschädigen, wenn die Herstellung nur "
     "mit unverhältnismäßigen Aufwendungen möglich ist. [vor]Erst diese Grenze beendet den Vorrang der Herstellung, sagt "
     "der Bundesgerichtshof.", PS),
    # --- I Abwandlung: Reparatur 1.200 € ---------------------------------------------------------------------------------------
    ("[var]Ändern wir den Fall: Die Reparatur würde tausendzweihundert Euro kosten. [var2]Ein gleichwertiges Rad gibt es "
     "für neunhundert Euro. [var3]Auch ein Ersatzrad ist Herstellung, und Hedi muss den wirtschaftlicheren Weg wählen. "
     "[var4]Sie bekommt also neunhundert Euro, abzüglich des Restwerts ihres kaputten Rads, sagen wir fünfzig Euro. "
     "[var5]Das macht achthundertfünfzig Euro.", P),
    ("[kfz]Beim Auto lässt der Bundesgerichtshof ausnahmsweise eine Reparatur bis hundertdreißig Prozent des "
     "Wiederbeschaffungswerts zu, wenn fachgerecht repariert wird. [kfz2]Mit tausendzweihundert Euro läge die Reparatur "
     "auch darüber.", PS),
    # --- J Ergebnis ------------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Hedi muss sich nicht auf den Schwager einlassen. [erg2]Sie kann vierhundert Euro verlangen, mit "
     "Reparaturrechnung vierhundertsechsundsiebzig.", PS),
    # --- K Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne Haftungsgrund und Rechtsfolge. Die Paragrafen zweihundertneunundvierzig bis "
     "zweihunderteinundfünfzig prüfst du erst beim Schaden. [tipp2]Und Vorsicht bei der fiktiven Abrechnung: Im "
     "Werkvertragsrecht hat der Bundesgerichtshof sie für Mängelbeseitigungskosten aufgegeben. [tipp3]Im Deliktsrecht "
     "bleibt sie möglich.", PS),
    # --- L Klausurschema -------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Rechtsfolge: [k1]Eins: Schaden nach der Differenzhypothese. [k2]Zwei: grundsätzlich "
     "Herstellung, Paragraf zweihundertneunundvierzig Absatz eins. [k3]Drei: bei einer beschädigten Sache Geld statt "
     "Herstellung, Absatz zwei, [k3b]Umsatzsteuer nur, wenn angefallen. [k4]Vier: Geldentschädigung nach Paragraf "
     "zweihunderteinundfünfzig, wenn die Herstellung unmöglich, ungenügend oder unverhältnismäßig ist. [k5]Zur Höhe stets: "
     "der erforderliche Betrag, also der wirtschaftlichere Weg.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Erst die Differenz feststellen, dann die Art des Ersatzes. [mk2]Bei einer beschädigten Sache darf der "
     "Geschädigte statt der Herstellung Geld verlangen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
    assert not re.search(r"\b(Hedis|Ludolfs|Trudes)\b", text), "Genitiv eines Namens"
