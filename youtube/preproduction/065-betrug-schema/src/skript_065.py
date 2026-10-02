"""Folge 065 · Betrug § 263 Schema: Täuschung, Irrtum, Verfügung, Schaden (Mi · Examenswissen · StGB BT, Format Schema).
Beispielfall nach dem Plan-Hook: Detlef bietet in einer Online-Kleinanzeige ein Smartphone „neu und originalverpackt“ für
400 € an (Foto eines unbeschädigten Geräts, dazu „Top-Handy, ein echtes Schnäppchen!“), obwohl das Display des Geräts, das er
verschicken will, gesprungen ist. Waltraud fragt am Telefon nach, überweist 400 € per Vorkasse und erhält das beschädigte
Gerät (Wert 150 €).
Prüfung: Wortlautkarte § 263 I → Kette und Funktionszusammenhang → 1. Täuschung über Tatsachen (ausdrücklich/konkludent,
BGH 1 StR 171/19 Rn. 48; 5 StR 181/06 Rn. 20; Anpreisung) → 2. Irrtum (BGH 3 StR 162/13 Rn. 8) → 3. Vermögensverfügung
(BGH 4 StR 456/22 Rn. 22; Trickdiebstahl BGH 1 StR 402/16 Rn. 11) → 4. Schaden (Gesamtsaldierung, Eingehungs- und
Erfüllungsschaden BGH 1 StR 13/18 Rn. 8 f.; Bezifferung BVerfG 2 BvR 2559/08 Rn. 112, 2 BvR 2500/09 Rn. 176) → subjektiver
Tatbestand (Vorsatz; Absicht, Rechtswidrigkeit BGH 5 StR 65/02 Rn. 7; Stoffgleichheit BGH 4 StR 66/24 Rn. 4) →
Rechtswidrigkeit, Schuld → Ergebnis → Ausblick § 263 II, III, § 263a → Klausurtipp → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Detlef, Waltraud. Nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.6

# Eine Männerstimme (christian) und eine Frauenstimme (hilde); stephan und lucy werden nicht eingesetzt.
STIMMEN = {"Detlef": "christian", "Waltraud": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: die Kleinanzeige ------------------------------------------------------------------------------------------
    ("[fall]Sonntagabend. [detlef]Detlef stellt eine Kleinanzeige ins Netz: [anzeige]ein Smartphone, neu und "
     "originalverpackt, für vierhundert Euro. [foto]Das Foto zeigt ein unbeschädigtes Gerät. [display]Detlef weiß aber: "
     "Das Display des Geräts, das er verschicken will, ist gesprungen. [preis]Dazu schreibt er: Top-Handy, ein echtes "
     "Schnäppchen! [waltraud]Waltraud interessiert sich dafür und ruft an.", 0.3),
    ("[w1]Ist das Handy wirklich neu?", 0.3, "Waltraud"),
    ("[d1]Ja, ganz neu, noch nie benutzt.", 0.3, "Detlef"),
    ("[vorkasse]Waltraud überweist die vierhundert Euro per Vorkasse. [paket]Zwei Tage später kommt das Paket, "
     "[auspacken]und sie packt es aus.", 0.3),
    ("[w2]Das Display ist ja gesprungen!", 0.4, "Waltraud"),
    ("[wert]So ist das Gerät nur noch hundertfünfzig Euro wert. [frage]Hat sich Detlef wegen Betrugs strafbar gemacht? "
     "[frage2]Wir prüfen Paragraf zweihundertdreiundsechzig Glied für Glied.", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut und Kette ----------------------------------------------------------------------------------------------
    ("[p263]Paragraf zweihundertdreiundsechzig, Absatz eins: [p263w]Wer in der Absicht, sich oder einem Dritten einen "
     "rechtswidrigen Vermögensvorteil zu verschaffen, das Vermögen eines anderen dadurch beschädigt, dass er durch "
     "Vorspiegelung falscher oder durch Entstellung oder Unterdrückung wahrer Tatsachen einen Irrtum erregt oder "
     "unterhält, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe bestraft. [kette]Daraus folgt eine Kette: "
     "Täuschung, Irrtum, Vermögensverfügung, Schaden. [verf0]Die Verfügung steht nicht im Wortlaut. Sie verbindet Irrtum "
     "und Schaden. [glied]Jedes Glied muss auf dem vorigen beruhen. [subj0]Im subjektiven Tatbestand folgen Vorsatz und "
     "Bereicherungsabsicht.", PS),
    # --- D 1. Täuschung über Tatsachen -------------------------------------------------------------------------------------
    ("[t1]Erstes Glied: die Täuschung über Tatsachen. [tats]Tatsachen sind gegenwärtige oder vergangene Ereignisse oder "
     "Zustände, die dem Beweis zugänglich sind. [neu]Ob ein Gerät neu und unbeschädigt ist, lässt sich prüfen. "
     "[ausdr]Detlef behauptet es ausdrücklich, in der Anzeige und am Telefon. [konkl]Konkludent täuscht, wer die "
     "Unwahrheit nicht ausspricht, sie aber nach der Verkehrsanschauung durch sein Verhalten miterklärt. [konkl2]So "
     "erklärt das Foto schlüssig: So sieht das Gerät aus. [anpreis]Anders Top-Handy, ein echtes Schnäppchen: Das ist eine "
     "reklamehafte Anpreisung, ein Werturteil ohne greifbaren Tatsachenkern. [tok]Die Täuschung liegt also in der "
     "Angabe neu und im Foto.", PS),
    # --- E 2. Irrtum -------------------------------------------------------------------------------------------------------
    ("[irr]Zweites Glied: der Irrtum. Das ist jeder Widerspruch zwischen der Vorstellung des Getäuschten und der "
     "Wirklichkeit. [irr2]Waltraud glaubt, sie kauft ein neues, heiles Gerät. [irr3]Und sie glaubt es, weil Detlef es "
     "behauptet hat. Der Irrtum beruht auf der Täuschung.", PS),
    # --- F 3. Vermögensverfügung -------------------------------------------------------------------------------------------
    ("[vf]Drittes Glied: die Vermögensverfügung. [vfdef]Das ist jedes Handeln, Dulden oder Unterlassen des Getäuschten, "
     "das unmittelbar eine Vermögensminderung herbeiführt. [vf2]Waltraud überweist vierhundert Euro. Ihr Vermögen "
     "sinkt sofort, ohne weiteren Schritt von Detlef. [vf3]Und sie zahlt gerade wegen ihres Irrtums. [trick]Zur "
     "Abgrenzung: Lässt sich der Täter ein Handy nur zum Telefonieren geben und läuft damit weg, nimmt er es eigenmächtig. "
     "Das ist Trickdiebstahl, kein Betrug.", PS),
    # --- G 4. Vermögensschaden ---------------------------------------------------------------------------------------------
    ("[schad]Viertes Glied: der Vermögensschaden. [saldo]Maßgeblich ist die Gesamtsaldierung: Man vergleicht den "
     "Vermögenswert unmittelbar vor und nach der Verfügung. [eing]Schon beim Vertragsschluss ist der Getäuschte "
     "geschädigt, wenn sein Anspruch weniger wert ist als seine Verpflichtung. Das ist der Eingehungsschaden. "
     "[erf]Mit der Zahlung materialisiert er sich als Erfüllungsschaden, bemessen nach der Differenz zwischen Leistung "
     "und Gegenleistung. [rech]Waltraud zahlt vierhundert Euro und erhält ein Gerät, das hundertfünfzig Euro wert ist. "
     "[rech2]Ihr Schaden beträgt zweihundertfünfzig Euro. [bezif]Das Bundesverfassungsgericht verlangt, den Schaden der "
     "Höhe nach zu beziffern und wirtschaftlich nachvollziehbar darzulegen, außer in einfach gelagerten Fällen. "
     "[kette2]Damit steht die Kette: Die Täuschung bewirkt den Irrtum, der Irrtum die Verfügung, die Verfügung den "
     "Schaden. Der objektive Tatbestand ist erfüllt.", PS),
    # --- H Subjektiver Tatbestand ------------------------------------------------------------------------------------------
    ("[vors]Im subjektiven Tatbestand braucht Detlef Vorsatz für jedes Glied. [vors2]Er kennt das gesprungene Display und "
     "will, dass Waltraud zahlt. [abs]Hinzu kommt die Absicht, sich einen rechtswidrigen Vermögensvorteil zu verschaffen. "
     "[abs2]Detlef kommt es gerade auf die vierhundert Euro an. [rwv]Rechtswidrig ist der Vorteil, weil er keinen Anspruch "
     "darauf hat, für ein Gerät mit gesprungenem Display vierhundert Euro zu bekommen. Vereinbart war ein neues. "
     "[stoff]Außerdem muss der Vorteil stoffgleich sein, also die Kehrseite des Schadens. [stoff2]Das Geld fließt "
     "unmittelbar aus dem Vermögen von Waltraud an Detlef.", PS),
    # --- I Rechtswidrigkeit, Schuld, Ergebnis ------------------------------------------------------------------------------
    ("[rw]Rechtfertigungsgründe sind nicht ersichtlich. [schuld]Detlef handelt auch schuldhaft. [erg]Ergebnis: Detlef "
     "hat sich wegen Betrugs strafbar gemacht.", PS),
    # --- J Ausblick --------------------------------------------------------------------------------------------------------
    ("[versuch]Ein Ausblick: Hätte Waltraud den Schwindel bemerkt und nicht gezahlt, käme ein Versuch in Betracht, "
     "strafbar nach Absatz zwei. [p3]Betrügt Detlef gewerbsmäßig, liegt nach Absatz drei in der Regel ein besonders "
     "schwerer Fall vor. [p263a]Und wird kein Mensch getäuscht, sondern ein Datenverarbeitungsvorgang beeinflusst, greift "
     "der Computerbetrug, Paragraf zweihundertdreiundsechzig a.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Verknüpfe die Kette sauber. [tipp2]Frage bei jedem Glied, ob es auf dem vorigen beruht: Irrtum "
     "durch Täuschung, Verfügung wegen des Irrtums, Schaden durch die Verfügung. [tipp3]Und rechne den Schaden konkret "
     "aus: vierhundert minus hundertfünfzig Euro.", PS),
    # --- L Prüfschema ------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k1]Römisch eins: Tatbestand. [k1a]Objektiv: erstens Täuschung über Tatsachen, [k1b]zweitens "
     "Irrtum, [k1c]drittens Vermögensverfügung, [k1d]viertens Vermögensschaden, [k1e]verbunden durch Kausal- und "
     "Funktionszusammenhang. [k1f]Subjektiv: Vorsatz [k1g]und Absicht rechtswidriger, stoffgleicher Bereicherung. "
     "[k2]Römisch zwei: Rechtswidrigkeit. [k3]Römisch drei: Schuld. [k4]Römisch vier: Strafzumessung, besonders "
     "schwerer Fall nach Absatz drei.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Betrug ist eine Kette. Täuschung, Irrtum, Verfügung und Schaden müssen aufeinander beruhen. "
     "[m2]Bloße Anpreisungen sind keine Tatsachen. [m3]Und den Schaden zeigt der Vergleich vor und nach der Verfügung, "
     "in Euro beziffert.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
