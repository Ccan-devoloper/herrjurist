"""Folge 200 · Baugebiete BauNVO: Was darf ins Wohngebiet? (§ 30 BauGB) (Mi · Examenswissen · Baurecht, Format Schema).
Beispielfall nach dem Plan-Hook („Im reinen Wohngebiet soll eine Kita öffnen, im allgemeinen Wohngebiet ein Tattoo-Studio.“):
Ein qualifizierter Bebauungsplan (2022) einer Gemeinde setzt für eine neue Siedlung im Norden ein reines, im Süden ein
allgemeines Wohngebiet fest. Frau Möhring (um 35) will im Norden in einem Einfamilienhaus eine Kita mit zwei Gruppen und
30 Plätzen für Kinder aus der Siedlung eröffnen. Herr Tiemann (um 30) mietet im Süden ein kleines Ladenlokal für sein
Tattoo-Studio: nur nach Termin, kein Lärm nach draußen, Kundschaft aus der ganzen Stadt.
Aufbau (Schema): Fall → Sachverhalt → § 30 Abs. 1 BauGB (Wortlautkarte) → Baugebiete § 1 Abs. 2 BauNVO (Tabelle), § 1 Abs. 3
→ Aufbau §§ 2 ff. (Abs. 1–3), § 31 Abs. 1 BauGB (Wortlautkarte), Gebietsverträglichkeit → Kita im WR (§ 3 BauNVO,
Wortlautkarte; Gegenfall große Kita; § 22 Abs. 1a BImSchG, Wortlautkarte) → Studio im WA (§ 4 BauNVO, Wortlautkarte;
Gebietsversorgung; Abs. 3 Nr. 2; Ausnahme; § 246e BauGB) → § 15 Abs. 1 BauNVO (Wortlautkarte; Verweis 113) → Ergebnis →
Schema → Klausurtipp (Lexi) → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Volltextsuche 04.10.2026): Möhring, Tiemann (nie im Genitiv).
Stimmen (Pool stephan, hilde, christian, lucy): Frau Möhring lucy (Frau, jung), Herr Tiemann stephan (Mann, mittel);
hilde und christian nicht verwendet (keine Stephan/Christian-Paarung). Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gesetzesnamen im Sprechtext als Wörter (keine Abkürzungen wie BauGB/BauNVO)."""

P, PS = 0.3, 0.5

STIMMEN = {"Möhring": "lucy", "Tiemann": "stephan"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die neue Siedlung, Kita im Norden ------------------------------------------------------------------------
    ("[fall]Eine Gemeinde hat einen Bebauungsplan für eine neue Siedlung. [wr]Im Norden setzt er ein reines Wohngebiet "
     "fest, [wa]im Süden ein allgemeines Wohngebiet. [kita]Im Norden will Frau Möhring in einem Einfamilienhaus eine Kita "
     "eröffnen.", P),
    ("[mo1]Zwei Gruppen, dreißig Plätze, und alle Kinder kommen hier aus der Siedlung.", P, "Möhring"),
    # --- A2 Fall: das Ladenlokal im Süden ----------------------------------------------------------------------------------
    ("[studio]Im Süden mietet Herr Tiemann ein kleines Ladenlokal für sein Tattoo-Studio.", P),
    ("[ti1]Ich arbeite nur nach Termin, und nach draußen dringt kein Lärm. Meine Kundschaft kommt aus der ganzen Stadt.",
     P, "Tiemann"),
    ("[frage]Darf die Kita ins reine Wohngebiet? [frage2]Und darf das Studio ins allgemeine Wohngebiet?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 30 Abs. 1 BauGB -----------------------------------------------------------------------------------------------
    ("[p30]Ausgangspunkt ist Paragraf dreißig Absatz eins Baugesetzbuch. [p30w]Ein Vorhaben ist zulässig, wenn es den "
     "Festsetzungen nicht widerspricht und die Erschließung gesichert ist. [quali]Das gilt für einen qualifizierten "
     "Bebauungsplan: Er setzt mindestens Art und Maß der baulichen Nutzung, die überbaubaren Grundstücksflächen und die "
     "örtlichen Verkehrsflächen fest. [hier]So ist es hier, und die Erschließung ist gesichert. [art]Offen ist nur die Art "
     "der baulichen Nutzung. [v188]Ob du überhaupt eine Genehmigung brauchst, zeigt das Video zum Schema der "
     "Baugenehmigung.", PS),
    # --- D Baugebiete § 1 Abs. 2 BauNVO (Tabelle) ---------------------------------------------------------------------------
    ("[bng]Die Art der Nutzung regelt die Baunutzungsverordnung. [p12]Paragraf eins Absatz zwei kennt zwölf Baugebiete, "
     "zum Beispiel: [twr]das reine Wohngebiet, [twa]das allgemeine Wohngebiet, [tmi]das Mischgebiet, [tmu]das urbane Gebiet "
     "aus Paragraf sechs a, [tge]das Gewerbegebiet [tgi]und das Industriegebiet. [p13]Setzt der Plan ein Baugebiet fest, "
     "werden nach Absatz drei die Paragrafen zwei bis vierzehn Bestandteil des Bebauungsplans.", PS),
    # --- E Aufbau §§ 2 ff., § 31 Abs. 1 BauGB, Gebietsverträglichkeit ------------------------------------------------------
    ("[aufbau]Die Gebietsvorschriften der Paragrafen zwei bis neun sind gleich gebaut. [abs1]Absatz eins nennt den Zweck des Gebiets. [abs2]Absatz zwei "
     "zählt auf, was allgemein zulässig ist, [abs3]Absatz drei, was ausnahmsweise zugelassen werden kann. [p31]Dazu "
     "Paragraf einunddreißig Absatz eins Baugesetzbuch: Ausnahmen, die der Plan nach Art und Umfang ausdrücklich vorsieht, "
     "können zugelassen werden. [erm]Darüber entscheidet die Behörde nach Ermessen. [gv]Ungeschrieben kommt die "
     "Gebietsverträglichkeit hinzu: Auch eine aufgezählte Nutzung ist unzulässig, wenn sie nach ihrer typischen "
     "Nutzungsweise den Charakter des Gebiets stört.", PS),
    # --- F Kita im reinen Wohngebiet: § 3 BauNVO, § 22 Abs. 1a BImSchG -----------------------------------------------------
    ("[kita1]Jetzt die Kita im reinen Wohngebiet. [p3a]Nach Paragraf drei Absatz eins dienen reine Wohngebiete dem Wohnen. "
     "[p3b]Allgemein zulässig sind nach Absatz zwei neben Wohngebäuden auch Anlagen zur Kinderbetreuung, die den "
     "Bedürfnissen der Bewohner des Gebiets dienen. [sub3]Frau Möhring betreut Kinder aus der Siedlung, ihre Kita dient "
     "also den Bewohnern. [gv3]Mit zwei Gruppen stört sie den Gebietscharakter auch nicht. [gross]Eine große Kita für die "
     "ganze Stadt wäre anders: Sie käme nur als sonstige Anlage für soziale Zwecke in Betracht, ausnahmsweise nach Absatz "
     "drei Nummer zwei.", P),
    ("[laerm]Und der Kinderlärm? [p22]Paragraf zweiundzwanzig Absatz eins a des Bundes-Immissionsschutzgesetzes: "
     "Geräuscheinwirkungen, die von Kindertageseinrichtungen durch Kinder hervorgerufen werden, sind im Regelfall keine "
     "schädliche Umwelteinwirkung. [kerg]Die Kita ist allgemein zulässig.", PS),
    # --- G Tattoo-Studio im allgemeinen Wohngebiet: § 4 BauNVO -------------------------------------------------------------
    ("[stu1]Nun das Tattoo-Studio im allgemeinen Wohngebiet. [p4a]Es dient nach Paragraf vier Absatz eins vorwiegend dem "
     "Wohnen. [p4b]Allgemein zulässig sind nach Absatz zwei Nummer zwei unter anderem die der Versorgung des Gebiets "
     "dienenden nicht störenden Handwerksbetriebe. [hw]Ob Tätowieren ein Handwerk ist, kann offenbleiben. [vers]Der "
     "Versorgung des Gebiets dient ein Betrieb, wenn er sich dem Wohngebiet funktional zuordnen lässt. [stadt]Die "
     "Kundschaft von Herrn Tiemann kommt aber aus der ganzen Stadt. [nein2]Absatz zwei scheidet aus.", P),
    ("[p4c]Bleibt Absatz drei Nummer zwei: Sonstige nicht störende Gewerbebetriebe können ausnahmsweise zugelassen werden. "
     "[ruhig]Nach dem Sachverhalt stört das kleine Studio, nur nach Termin und ohne Lärm, das Wohnen nicht. [aus]Möglich "
     "ist also eine Ausnahme nach Paragraf einunddreißig Absatz eins. [regel]Die Behörde muss dabei wahren, dass die "
     "Ausnahme die Ausnahme bleibt. [turbo]Der sogenannte Bau-Turbo, Paragraf zweihundertsechsundvierzig e, hilft hier nicht: "
     "Er erleichtert Abweichungen nur für den Wohnungsbau.", PS),
    # --- H § 15 Abs. 1 BauNVO ----------------------------------------------------------------------------------------------
    ("[p15]Zuletzt Paragraf fünfzehn Absatz eins Baunutzungsverordnung: [p15w]Eine an sich zulässige Anlage ist im "
     "Einzelfall unzulässig, wenn sie nach Anzahl, Lage, Umfang oder Zweckbestimmung der Eigenart des Baugebiets "
     "widerspricht oder unzumutbar stört. [h15]Dafür gibt der Sachverhalt bei beiden nichts her. [v113]Wie Nachbarn eine "
     "gebietsfremde Nutzung abwehren, zeigt das Video zur baurechtlichen Nachbarklage.", PS),
    # --- I Ergebnis --------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Die Kita ist im reinen Wohngebiet allgemein zulässig. [erg2]Das Studio kann im allgemeinen "
     "Wohngebiet nur im Wege der Ausnahme zugelassen werden.", P),
    ("[ti2]Dann beantrage ich die Ausnahme gleich mit.", PS, "Tiemann"),
    # --- J Schema ----------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für Paragraf dreißig Absatz eins. [s1]Erstens: qualifizierter Bebauungsplan. [s2]Zweitens: Art "
     "der baulichen Nutzung. [s2a]Baugebiet bestimmen, [s2b]Katalog nach Absatz zwei, [s2c]sonst Ausnahme nach Absatz "
     "drei und Paragraf einunddreißig Absatz eins oder Befreiung nach Paragraf einunddreißig Absatz zwei, [s2d]dazu die Gebietsverträglichkeit "
     "[s2e]und Paragraf fünfzehn. [s3]Drittens: die übrigen Festsetzungen, etwa das Maß. [s4]Viertens: gesicherte "
     "Erschließung.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Art der Nutzung immer in derselben Reihenfolge. [k1]Erst das Gebiet bestimmen, [k2]dann "
     "den Katalog in Absatz zwei, [k3]dann Ausnahme oder Befreiung nach Paragraf einunddreißig, [k4]zuletzt Paragraf "
     "fünfzehn. [k5]Und prüfe bei älteren Plänen, welche Fassung der Baunutzungsverordnung für sie gilt.", PS),
    # --- L Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Bebauungsplan wählt das Gebiet, [m2]die Baunutzungsverordnung liefert den Katalog. [m3]Was dort "
     "nicht allgemein zulässig ist, braucht eine Ausnahme oder eine Befreiung. [m4]Und Paragraf fünfzehn prüft am Ende "
     "den Einzelfall.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
