"""Folge 148 · Unfallflucht § 142: Wie lange muss ich warten? Zettel reicht nicht (Mo · Der Fall · StGB BT, Format Schema).
Fall nach dem Plan-Hook („Eine Autofahrerin schrammt nachts beim Ausparken ein anderes Auto, klemmt einen Zettel unter den
Scheibenwischer und fährt weiter“): Gerlinde parkt kurz vor Mitternacht auf einem öffentlichen Parkplatz aus und schrammt das
geparkte Auto von Bernhard (Schramme an der Tür, Reparatur rund 400 €). Niemand ist zu sehen. Sie schreibt Namen und
Telefonnummer auf einen Zettel, klemmt ihn unter den Scheibenwischer und fährt sofort weiter. Am Morgen findet Bernhard
Schramme und Zettel. Kein Aufprallbild (nur Kratzlinie, dezentes Kratzgeräusch als Handlungsgeräusch).
Prüfung: Wortlautkarte § 142 Abs. 1 → 1. Unfall im Straßenverkehr (BGH 4 StR 233/01 Rn. 7; OLG Naumburg 1 ORs 38/24:
Parkplatz, völlig belangloser Schaden) → 2. Unfallbeteiligte (Wortlautkarte Abs. 5) → 3. Entfernen vor Erfüllung von Nr. 1
(Anwesenheit) / Nr. 2 (Wartepflicht „angemessene Zeit“; Faktoren und Mindestwartezeit OLG Dresden 6 U 1480/17) → Zettel
(Wortlaut „zugunsten der anderen Unfallbeteiligten und der Geschädigten“, Person, Fahrzeug, Art der Beteiligung) → Vorsatz
→ Abs. 2 Nr. 1 und Wortlautkarte Abs. 3 S. 1 → Abs. 2 Nr. 2: unvorsätzliches Entfernen nicht erfasst (BVerfG, Beschl. v.
19.3.2007 – 2 BvR 2273/06, Rn. 18, 20; BGH 4 StR 413/10 Rn. 4 f.) → tätige Reue Abs. 4 (Wortlautkarte; BT-Drucks. 13/8587:
Parkunfälle) → Ergebnis → Klausurtipp → Schema → Merksatz. Belege: ../RECHTSSTAND.md. Reformüberlegungen (BMJ-Eckpunkte
23.11.2023) bewusst nicht im Video: kein Gesetzentwurf und keine Verkündung nachweisbar (siehe RECHTSSTAND.md).
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Gerlinde, Bernhard (nie im Genitiv).
Stimmen (nur aus dem Pool stephan, hilde, christian, lucy): Gerlinde hilde (Frau, älter), Bernhard christian (Mann, mittel);
Vorfolge 146 nutzte lucy/stephan, 147 helmut. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter; „Grundgesetz“, „Oberlandesgericht“, „Bundesverfassungsgericht“
ausgeschrieben."""

P, PS = 0.3, 0.5

STIMMEN = {"Gerlinde": "hilde", "Bernhard": "christian"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: nachts auf dem Parkplatz --------------------------------------------------------------------------------
    ("[fall]Kurz vor Mitternacht auf einem öffentlichen Parkplatz. [aus]Gerlinde parkt aus [kratz]und schrammt dabei das "
     "Auto von Bernhard. [schaden]An der Tür bleibt eine lange Schramme. [leer]Weit und breit ist niemand zu sehen.", 0.3),
    ("[g1]Ist doch nur ein Kratzer. Ich lasse einen Zettel da.", 0.3, "Gerlinde"),
    ("[zettel]Sie schreibt Namen und Telefonnummer auf, klemmt den Zettel unter den Scheibenwischer [weg]und fährt sofort "
     "weiter.", 0.3),
    # --- A2 Fall: am nächsten Morgen --------------------------------------------------------------------------------------
    ("[morgen]Am nächsten Morgen findet Bernhard die Schramme und den Zettel.", 0.3),
    ("[b1]Ein Zettel? Und wenn der weggeweht wäre?", 0.3, "Bernhard"),
    ("[frage]Hat sich Gerlinde wegen unerlaubten Entfernens vom Unfallort strafbar gemacht? [frage2]Und wie lange hätte sie "
     "warten müssen?", 0.5),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlautkarte § 142 Abs. 1 ---------------------------------------------------------------------------------------
    ("[p142]Paragraf hundertzweiundvierzig Absatz eins bestraft einen Unfallbeteiligten, der sich nach einem Unfall im "
     "Straßenverkehr vom Unfallort entfernt, [nr1]bevor er die Feststellungen durch seine Anwesenheit ermöglicht hat [nr2]oder "
     "eine nach den Umständen angemessene Zeit gewartet hat.", PS),
    # --- D 1. Unfall im Straßenverkehr --------------------------------------------------------------------------------------
    ("[unfall]Erstens der Unfall im Straßenverkehr: jedes schädigende Ereignis, das mit dem Straßenverkehr und seinen Gefahren "
     "zusammenhängt. [park]Ein allgemein zugänglicher Parkplatz gehört dazu. [baga]Nur ein völlig belangloser Schaden scheidet "
     "aus, also einer, für den man üblicherweise keinen Ersatz verlangt. [schr]Eine Schramme für vierhundert Euro ist das "
     "nicht.", PS),
    # --- E 2. Unfallbeteiligte (Wortlautkarte Abs. 5) ------------------------------------------------------------------------
    ("[abs5]Zweitens Gerlinde als Unfallbeteiligte. Nach Absatz fünf ist das jeder, dessen Verhalten nach den Umständen zur "
     "Verursachung beigetragen haben kann. [ger5]Gerlinde hat beim Ausparken selbst geschrammt.", PS),
    # --- F 3. Entfernen: Nr. 1 und Nr. 2 (Wartepflicht) ----------------------------------------------------------------------
    ("[entf]Drittens das Entfernen. [anw]Nummer eins verlangt Anwesenheit und die Angabe, dass man beteiligt ist, gegenüber "
     "jemandem, der zu Feststellungen bereit ist. [niem]Nachts war aber niemand da. [warte]Dann gilt Nummer zwei: warten. "
     "[minuten]Eine feste Minutenzahl nennt das Gesetz nicht. [fakt]Es kommt auf die Umstände an: Uhrzeit, Verkehr, wie "
     "auffällig der Unfall ist und wie hoch der Schaden. [olg]Das Oberlandesgericht Dresden verlangte selbst bei kleinem "
     "Schaden auf einer wenig befahrenen Straße mindestens zehn Minuten. [null]Gerlinde hat gar nicht gewartet.", PS),
    # --- G Warum der Zettel nicht reicht ------------------------------------------------------------------------------------
    ("[zett]Und der Zettel? [zugun]Das Gesetz kennt nur zwei Wege: die Feststellungen zugunsten der anderen "
     "Unfallbeteiligten und der Geschädigten durch Anwesenheit ermöglichen oder angemessen warten. [ersatz]Einen Zettel als Ersatz sieht es nicht "
     "vor. [person]Wer wegfährt, lässt niemanden mehr prüfen, wer er ist, welches Auto er fährt und wie er beteiligt war. "
     "[vors]Gerlinde wusste von der Schramme; ihr Zettel zeigt es sogar. Sie handelte vorsätzlich.", PS),
    # --- H Abs. 2 Nr. 1 und Abs. 3 (Wortlautkarte) --------------------------------------------------------------------------
    ("[abs2]Auch wer lange genug gewartet hat, ist nicht einfach frei. Nach Absatz zwei Nummer eins muss er die Feststellungen "
     "danach unverzüglich nachträglich ermöglichen. [abs3]Wie, sagt Absatz drei: Er meldet dem Berechtigten oder einer nahe "
     "gelegenen Polizeidienststelle, dass er beteiligt war, [abs3b]nennt Anschrift, Aufenthalt, Kennzeichen und Standort "
     "seines Fahrzeugs [abs3c]und hält es für Feststellungen bereit. [spaet]Diese Meldung kommt nach dem Warten, nicht statt "
     "des Wartens. [nurtel]Und auf dem Zettel von Gerlinde standen ohnehin nur Name und Telefonnummer.", PS),
    # --- I Abs. 2 Nr. 2, BVerfG (Gegenvariante) -----------------------------------------------------------------------------
    ("[abs22]Absatz zwei Nummer zwei erfasst, wer sich berechtigt oder entschuldigt entfernt hat. [bverfg]Wer den Unfall gar "
     "nicht bemerkt und erst später davon erfährt, fällt nach dem Bundesverfassungsgericht nicht darunter. [analog]Unvorsätzlich "
     "ist nicht dasselbe wie berechtigt oder entschuldigt; alles andere wäre eine verbotene Analogie nach Artikel hundertdrei "
     "Absatz zwei Grundgesetz. [gegen]Hätte Gerlinde die Schramme nicht bemerkt, wäre sie also nach Paragraf "
     "hundertzweiundvierzig nicht strafbar.", PS),
    # --- J Tätige Reue, Abs. 4 (Wortlautkarte) ------------------------------------------------------------------------------
    ("[abs4]Bleibt Absatz vier, die tätige Reue. [a4a]Er gilt nur für Unfälle außerhalb des fließenden Verkehrs [a4b]mit "
     "ausschließlich nicht bedeutendem Sachschaden. [a4c]Ermöglicht der Täter innerhalb von vierundzwanzig Stunden freiwillig "
     "die Feststellungen nachträglich, [a4d]mildert das Gericht die Strafe oder kann ganz von Strafe absehen. [parkunf]Gemeint "
     "sind nach den Gesetzesmaterialien vor allem Parkunfälle, [vier]und vierhundert Euro für eine Schramme sind kein bedeutender "
     "Schaden.", PS),
    # --- K Ergebnis --------------------------------------------------------------------------------------------------------
    ("[rws]Rechtswidrigkeit und Schuld liegen vor. [erg]Ergebnis: Gerlinde ist strafbar nach Paragraf hundertzweiundvierzig "
     "Absatz eins Nummer zwei. [erg2]Meldet sie sich aber innerhalb von vierundzwanzig Stunden selbst bei Bernhard oder bei der "
     "Polizei und macht die Angaben nach Absatz drei, greift Absatz vier.", PS),
    # --- L Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst Absatz eins, Nummer eins vor Nummer zwei. [tipp2]Absatz zwei kommt nur, wenn sich der "
     "Täter erlaubt entfernt hat: nach der Wartefrist oder berechtigt oder entschuldigt. [tipp3]Beim Vorsatz muss er den Unfall "
     "und den Schaden zumindest für möglich halten. [tipp4]Und Absatz vier prüfst du erst am Ende, bei der Strafe.", PS),
    # --- M Prüfschema -------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema zu Paragraf hundertzweiundvierzig. [s1]Römisch eins, Tatbestand: Unfall im Straßenverkehr, "
     "Unfallbeteiligter; [s1b]Entfernen, bevor Nummer eins oder Nummer zwei erfüllt ist, [s1c]oder nach Absatz zwei: erlaubt "
     "entfernt und nicht unverzüglich nachträglich ermöglicht; [s1d]dazu Vorsatz. [s2]Römisch zwei und drei: Rechtswidrigkeit "
     "und Schuld. [s3]Römisch vier: tätige Reue nach Absatz vier.", PS),
    # --- N Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer nach einem Unfall niemanden antrifft, muss warten, so lange die Umstände es verlangen. [m2]Ein Zettel "
     "ersetzt das Warten nicht. [m3]Wer trotzdem wegfährt, kann sich bei kleinen Parkschäden nur noch über Absatz vier "
     "helfen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
