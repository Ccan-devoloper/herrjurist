"""Folge 207 · Gesamtsaldierung: Der Vermögensschaden beim Betrug § 263 erklärt (Fr · Klausurpraxis · StGB BT, Format Schema).
Fall nach dem Plan-Hook („Ein Käufer zahlt 300 Euro für einen ‚Designer-Sessel‘, der in Wahrheit ein Nachbau ist – aber exakt
300 Euro wert.“): Samstag, Garagenverkauf. Gundula (um 60) sucht einen bequemen Sessel für ihre Leseecke. Alwin (um 45) bietet
vor seiner Garage einen „Designer-Sessel“ für 300 € an; er weiß, dass es ein Nachbau ist, hält 300 € aber für den richtigen
Preis. Auf Nachfrage sagt er: „Ja, ein echtes Designerstück.“ Gundula zahlt bar. Später schätzt die Gutachterin Ulla den Sessel:
ein gut gemachter Nachbau, genau 300 € wert. Keine echten Marken, keine Klischees; Personen fiktiv.
Aufbau (Schema mit Fall, Auftrag): Hook → Sachverhalt → § 263 I (Wortlautkarte), Merkmal „Vermögen beschädigt“, Vermögensbegriff
in einem Satz → Gesamtsaldierung (vor/nach der Verfügung, Gegenleistung gleicht aus) → Waage 300 € − 300 € = 0 € → kein Schaden
trotz Täuschung (BGHSt 16, 321; BGH 2 StR 283/25 Rn. 10) → Korrekturen: individueller Schadenseinschlag (BGHSt 16, 321;
3 StR 171/17), Eingehungsschaden (1 StR 13/18 Rn. 9), Gefährdungsschaden (BVerfG 2 BvR 2500/09 Rn. 174–176) → Gegenfall
120 € → 180 € → Versuch § 263 II in einem Satz → Klausurtipp (Lexi: Schaden immer beziffern) → Prüfschema → Merksatz (Lexi).
Täuschung, Irrtum, Verfügung nur kurz (Verweis Folge 065). Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Auftragsliste, Reservierungsliste, Volltextsuche 06.10.2026):
Gundula, Alwin, Ulla. Nie im Genitiv mit -s. Stimmen (Pool stephan, hilde, christian, lucy): Gundula hilde (Frau, älter),
Alwin stephan (Mann, mittel), Ulla lucy (Frau, jung); christian nicht verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gerichtsnamen im Sprechtext als Wörter (keine Abkürzungen wie StGB/BGH)."""

P, PS = 0.3, 0.5

STIMMEN = {"Gundula": "hilde", "Alwin": "stephan", "Ulla": "lucy"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Garagenverkauf --------------------------------------------------------------------------------------
    ("[fall]Samstagvormittag, ein Garagenverkauf. [gundula]Gundula sucht einen bequemen Sessel für ihre Leseecke. "
     "[alwin]Alwin bietet vor seiner Garage einen Designer-Sessel an, für dreihundert Euro. [nachbau]Er weiß: Es ist kein "
     "Original, sondern ein Nachbau. [preis]Dreihundert Euro hält er trotzdem für den richtigen Preis.", P),
    ("[g1]Ist das wirklich ein Original?", P, "Gundula"),
    ("[a1]Ja, ein echtes Designerstück.", P, "Alwin"),
    ("[zahlt]Gundula zahlt die dreihundert Euro bar [mit]und nimmt den Sessel mit.", P),
    # --- A2 Fall: das Gutachten in der Leseecke -----------------------------------------------------------------------
    ("[leseecke]Zu Hause stellt sie ihn in ihre Leseecke. [gutachten]Später lässt sie ihn von der Gutachterin Ulla "
     "schätzen.", P),
    ("[u1]Ein Nachbau, aber gut gemacht. Er ist genau dreihundert Euro wert.", P, "Ulla"),
    ("[frage]Gundula wurde getäuscht. Aber ist ihr Vermögen beschädigt? [frage2]Das klärt die Gesamtsaldierung.", 0.6),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 263 Abs. 1: das Merkmal „Vermögen beschädigt“ ------------------------------------------------------------
    ("[p263]Paragraf zweihundertdreiundsechzig, Absatz eins, verlangt, dass der Täter [beschaedigt]das Vermögen eines "
     "anderen beschädigt. [kette]Täuschung, Irrtum und Vermögensverfügung liegen hier vor: [kette2]Alwin lügt über das "
     "Original, Gundula glaubt ihm und zahlt. [v065]Wie man diese Merkmale prüft, zeigt unsere Folge zum Betrugsschema. "
     "[heute]Heute geht es nur um den Schaden. [vbegr]Vermögen ist nach der Rechtsprechung die Summe der geldwerten Güter "
     "einer Person, wirtschaftlich betrachtet.", PS),
    # --- D Gesamtsaldierung ----------------------------------------------------------------------------------------------
    ("[saldo]Den Schaden ermittelt man durch Gesamtsaldierung. [vorher]Man vergleicht den Wert des Vermögens unmittelbar "
     "vor der Verfügung [nachher]mit dem Wert unmittelbar danach. [komp]Was durch die Verfügung zugleich hereinkommt, gleicht "
     "den Abfluss aus. Das ist vor allem die Gegenleistung. [minder]Ein Schaden liegt nur vor, wenn unterm Strich eine "
     "Minderung bleibt.", PS),
    # --- E Rechnung im Fall: die Waage -----------------------------------------------------------------------------------
    ("[rech]Im Fall heißt das: [rech1]Vor der Verfügung hat Gundula dreihundert Euro. [rech2]Danach hat sie einen Sessel, der "
     "dreihundert Euro wert ist. [rech3]Dreihundert minus dreihundert ergibt null. [null]Ein Schaden bleibt nicht.", PS),
    # --- F Kein Schaden trotz Täuschung ----------------------------------------------------------------------------------
    ("[folge]Das überrascht viele: Gundula wurde belogen, und doch fehlt der Schaden. [dispo]Betrug schützt das Vermögen, "
     "nicht die Freiheit, ohne Täuschung zu entscheiden. [melk]So sieht es der Bundesgerichtshof seit dem Melkmaschinen-Fall: "
     "Wer wegen einer Täuschung verfügt, ist nicht schon deshalb geschädigt. [nb]Wird beim Kauf über Umstände getäuscht, die den "
     "Wert mitbestimmen, etwa Nachbau statt Original, entsteht ein Schaden regelmäßig nur, wenn die Sache objektiv den "
     "Preis nicht wert ist. [kein]Ein vollendeter Betrug von Alwin scheidet also aus.", PS),
    # --- G1 Korrektur: individueller Schadenseinschlag -------------------------------------------------------------------
    ("[indiv]Es gibt aber Korrekturen. Erstens: der individuelle Schadenseinschlag. Auch bei gleichem Wert kann der "
     "Getäuschte geschädigt sein, [i1]wenn er die Sache nicht zum vertraglich vorausgesetzten Zweck und auch nicht anders zumutbar "
     "verwenden kann, [i2]wenn er wegen der Verpflichtung zu vermögensschädigenden Maßnahmen gezwungen wird, etwa zu einem "
     "teuren Kredit, [i3]oder wenn ihm danach die Mittel für eine angemessene Lebensführung fehlen. [i4]Hier nicht: Gundula "
     "liest in dem Sessel, sie hat bar gezahlt und kommt weiter gut zurecht.", PS),
    # --- G2 Korrekturen: Eingehungsschaden und Gefährdungsschaden ------------------------------------------------------
    ("[eing]Zweitens kann der Schaden schon beim Vertragsschluss eintreten: Ist der erworbene Anspruch weniger wert als die "
     "eigene Verpflichtung, liegt ein Eingehungsschaden vor. [gef]Drittens kann schon die konkrete Gefahr eines künftigen "
     "Verlusts das Vermögen gegenwärtig mindern. [gef2]Auch dieser Gefährdungsschaden muss der Höhe nach beziffert werden.", PS),
    # --- H Gegenfall ------------------------------------------------------------------------------------------------------
    ("[gegen]Jetzt der Gegenfall. Angenommen, die Gutachterin kommt zu einem anderen Ergebnis.", P),
    ("[u2]Dieser Nachbau ist nur hundertzwanzig Euro wert.", P, "Ulla"),
    ("[grech]Dann gibt Gundula dreihundert Euro hin und erhält nur hundertzwanzig Euro Gegenwert. [grech2]Ihr Schaden "
     "beträgt hundertachtzig Euro. [gerg]Hat Alwin dann auch Vorsatz und Bereicherungsabsicht, ist der "
     "Betrugstatbestand erfüllt.", PS),
    # --- I Versuch --------------------------------------------------------------------------------------------------------
    ("[versuch]Und im Ausgangsfall ein Versuch nach Absatz zwei? Er scheidet aus, denn Alwin hält dreihundert Euro für den "
     "richtigen Preis; einen Schaden stellt er sich gar nicht vor.", PS),
    # --- J Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Beziffere den Schaden immer. [tipp2]Schreib die Rechnung hin: Leistung minus Gegenleistung, in "
     "Euro. [tipp3]Das verlangt auch das Bundesverfassungsgericht von den Strafgerichten, außer in einfach gelagerten Fällen. "
     "[tipp4]Und bleibt nichts übrig, schreib klar: kein Schaden, kein vollendeter Betrug.", PS),
    # --- K Prüfschema -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema für den Vermögensschaden. [s1]Erstens: der Vermögenswert unmittelbar vor der Verfügung. "
     "[s2]Zweitens: der Vermögenswert unmittelbar danach, samt Gegenleistung. [s3]Drittens: die Differenz, in Euro "
     "beziffert. [s4]Viertens: Korrekturen prüfen, also individuellen Schadenseinschlag, Eingehungs- und "
     "Gefährdungsschaden.", PS),
    # --- L Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Täuschung allein ist kein Schaden. [mk2]Entscheidend ist der Vergleich vor und nach der Verfügung, und "
     "am Ende steht eine Zahl in Euro.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
