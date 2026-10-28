"""Folge 197 · Zweistufentheorie: Stadthalle, Förderkredit und Kita-Platz (Mi · Examenswissen · Verwaltungsrecht AT,
Format Streitstand). Beispielfall nach dem Plan-Hook („Die städtische Hallen-GmbH vermietet nur an Vereine, die dem
Bürgermeister gefallen.“): Die Stadt betreibt ihre Stadthalle über eine eigene GmbH (alle Anteile bei der Stadt). Frau Lammers
(um 60), Vorsitzende des Chors Liederkranz (Verein mit Sitz in der Stadt), will den großen Saal für das Frühjahrskonzert mieten;
der Termin ist frei, der Schachclub hat dort im letzten Monat sein Turnier gespielt. Der Geschäftsführer Herr Scheffler lehnt ab:
Der Bürgermeister (fiktiv, ohne Partei, nicht im Bild) möchte den Chor nicht in der Halle.
Aufbau (Streitstand mit Fall): Fall → Sachverhalt → Problem (Eigengesellschaft: Rechtsweg? Anspruchsgegner?), Verweis auf
Folge 192 → Zweistufentheorie (Ob/Wie) → 1. Stufe: Zulassungsanspruch (§ 8 Abs. 2, 4 GO NRW Wortlaut, Normtabelle, Art. 28
Abs. 2 GG), Widmung, Kapazität, Gleichbehandlung (Art. 3 Abs. 1 GG) → 2. Stufe: Mietvertrag privat → GmbH: kein
Zulassungsanspruch gegen die Gesellschaft, Verschaffungs-/Einwirkungsanspruch gegen die Stadt (BVerwG 8 C 35.20 Rn. 14),
Verwaltungsrechtsweg § 40 Abs. 1 S. 1 VwGO → Förderkredit, Kita-Platz (§ 24 SGB VIII eigenständig) → Kritik (als Meinung) →
Lösung → zurück im Foyer → Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Volltextsuche 04.10.2026): Lammers, Scheffler (nie im Genitiv).
Stimmen (Pool stephan, hilde, christian, lucy): Frau Lammers hilde (Frau, älter), Herr Scheffler christian (Mann, mittel);
stephan nicht verwendet (keine Stephan/Christian-Paarung). Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gesetzesnamen im Sprechtext als Wörter (keine Abkürzungen wie GmbH/VwGO/GG)."""

P, PS = 0.3, 0.5

STIMMEN = {"Lammers": "hilde", "Scheffler": "christian"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Foyer der Stadthalle ---------------------------------------------------------------------------------------
    ("[fall]Die Stadt betreibt ihre Stadthalle nicht selbst, sondern über eine eigene Gesellschaft mit beschränkter Haftung. "
     "[anteile]Alle Anteile gehören der Stadt. [chor]Frau Lammers, die Vorsitzende des Chors Liederkranz, kommt ins Foyer.", P),
    ("[la1]Wir möchten den großen Saal für unser Frühjahrskonzert mieten. Der Termin ist doch frei.", P, "Lammers"),
    ("[sc1]Das stimmt. Aber der Bürgermeister möchte Ihren Chor nicht in der Halle haben.", P, "Scheffler"),
    ("[schach]Dabei hat der Schachclub erst im letzten Monat dort sein Turnier gespielt. [frage]Kann der Chor den Saal "
     "verlangen, und von wem: von der Gesellschaft oder von der Stadt? [frage2]Die Antwort liefert die Zweistufentheorie.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Problem und Zweistufentheorie -----------------------------------------------------------------------------------
    ("[prob]Das Problem: Die Stadt handelt hier durch eine private Gesellschaft. [prob2]Damit stellen sich zwei Fragen: "
     "Welcher Rechtsweg ist eröffnet, und gegen wen richtet sich der Anspruch? [verweis]Wie man öffentliches und privates "
     "Recht grundsätzlich abgrenzt, zeigt die Folge zu den Abgrenzungstheorien.", P),
    ("[zst]Die Zweistufentheorie teilt den Vorgang in zwei Stufen. [st1]Auf der ersten Stufe geht es um das Ob: Wird der "
     "Chor überhaupt zugelassen? [st1b]Diese Frage ist öffentlich-rechtlich. [st2]Auf der zweiten Stufe geht es um das Wie: "
     "Miete, Zeiten, Hausordnung. [st2b]Das kann ein privatrechtlicher Mietvertrag regeln.", PS),
    # --- D Erste Stufe: Zulassungsanspruch aus der Gemeindeordnung -----------------------------------------------------------
    ("[go]Grundlage für das Ob ist die Gemeindeordnung. In Nordrhein-Westfalen heißt es in Paragraf acht Absatz zwei: Alle "
     "Einwohner einer Gemeinde sind im Rahmen des geltenden Rechts berechtigt, die öffentlichen Einrichtungen der Gemeinde "
     "zu benutzen. [go4]Nach Absatz vier gilt das entsprechend für Personenvereinigungen, also auch für den Chor.", P),
    ("[tab]Die anderen Länder regeln das ähnlich, oft unter anderer Nummer. [a28]Dahinter steht Artikel achtundzwanzig "
     "Absatz zwei Grundgesetz: Die Stadt regelt ihre örtlichen Angelegenheiten selbst. [a28b]Sie darf ihre Halle deshalb einer "
     "eigenen Gesellschaft übertragen, muss sich aber den Einfluss auf sie vorbehalten.", PS),
    ("[vor]Der Anspruch hat Grenzen. [widm]Erstens die Widmung: Die Halle ist für Konzerte und Veranstaltungen der "
     "örtlichen Vereine bestimmt. [kap]Zweitens die Kapazität: Der Termin ist frei. [gleich]Drittens die Gleichbehandlung "
     "nach Artikel drei Absatz eins Grundgesetz: Wer dem Schachclub den Saal gibt, braucht für ein Nein beim Chor einen "
     "sachlichen Grund. [kein]Dass der Chor dem Bürgermeister nicht gefällt, ist keiner.", PS),
    # --- E Zweite Stufe: Mietvertrag ------------------------------------------------------------------------------------------
    ("[wie]Ist das Ob geklärt, folgt das Wie: Die Gesellschaft schließt mit dem Chor einen Mietvertrag. [wie2]Streit über "
     "die Miete oder die Bedingungen der Nutzung gehört dann vor die Zivilgerichte.", PS),
    # --- F Eigengesellschaft: Einwirkungsanspruch gegen die Stadt -------------------------------------------------------------
    ("[gmbh]Jetzt das Besondere an unserem Fall: Die Gemeindeordnung verpflichtet die Stadt, nicht ihre Gesellschaft. "
     "[gegen]Einen Zulassungsanspruch aus der Gemeindeordnung hat der Chor gegen die Gesellschaft deshalb nicht, und eine "
     "Klage gegen sie gehört nicht vor das Verwaltungsgericht. [einw]Der Anspruch wandelt sich in einen Verschaffungs- oder "
     "Einwirkungsanspruch gegen die Stadt: Sie muss auf ihre Gesellschaft einwirken, damit der Chor den Saal bekommt. "
     "[bverwg]So sieht es auch das Bundesverwaltungsgericht. [macht]Weil der Stadt alle Anteile gehören, kann sie das auch.", P),
    ("[rweg]Dieser Anspruch folgt aus der Gemeindeordnung, also aus Sonderrecht der Stadt. Deshalb ist der "
     "Verwaltungsrechtsweg nach Paragraf vierzig Absatz eins Satz eins Verwaltungsgerichtsordnung eröffnet.", PS),
    # --- G Weitere Anwendungsfelder ---------------------------------------------------------------------------------------------
    ("[weitere]Das Muster kehrt wieder. [kredit]Beim klassischen Förderkredit ist die Bewilligung das Ob und öffentlich-rechtlich; der "
     "Darlehensvertrag ist das Wie und privatrechtlich. [kita]Beim Kita-Platz ist Vorsicht geboten: Der Anspruch aus "
     "Paragraf vierundzwanzig Sozialgesetzbuch acht ist ein eigener Anspruch gegen den Träger der öffentlichen "
     "Jugendhilfe; der Betreuungsvertrag mit der Kita kann trotzdem privatrechtlich sein.", PS),
    # --- H Kritik (Meinungsstand) -----------------------------------------------------------------------------------------------
    ("[krit]Die Zweistufentheorie ist umstritten. [k1]Kritiker sagen: Sie spaltet einen einheitlichen Vorgang künstlich auf, "
     "und oft bleibt unklar, wo das Ob endet und das Wie beginnt. [k2]Manche wollen den Vorgang deshalb einheitlich "
     "behandeln, etwa durch einen öffentlich-rechtlichen Vertrag. [k3]Das Bundesverwaltungsgericht wendet die Theorie nur an, "
     "wenn ein Vorgang wirklich zwei Phasen hat. [k4]Für den Zugang zu öffentlichen Einrichtungen halten die Gerichte an der "
     "Unterscheidung fest.", PS),
    # --- I Lösung des Falls ------------------------------------------------------------------------------------------------------
    ("[loes]Zurück zum Chor. [l1]Die Stadthalle ist eine öffentliche Einrichtung der Stadt, auch wenn ihre Gesellschaft sie "
     "betreibt. [l2]Der Chor ist als Verein aus der Stadt berechtigt, das Konzert liegt im Widmungszweck, und der Termin ist "
     "frei. [l3]Ein sachlicher Grund für das Nein fehlt. [l4]Also kann der Chor von der Stadt verlangen, dass sie auf ihre "
     "Gesellschaft einwirkt, und das notfalls vor dem Verwaltungsgericht.", P),
    ("[la2]Dann wende ich mich an die Stadt und nicht an die Gesellschaft.", P, "Lammers"),
    ("[sc2]Und den Mietvertrag schließen danach wir mit Ihnen.", PS, "Scheffler"),
    # --- J Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe bei einer Eigengesellschaft zuerst, wer der richtige Anspruchsgegner ist. [kt1]Geht es um die "
     "Zulassung, richtet sich die Klage gegen die Gemeinde, und zwar auf Einwirkung. [kt2]Und trenne sauber: Streit über das "
     "Ob gehört vor das Verwaltungsgericht, Streit über den Mietvertrag vor das Zivilgericht.", PS),
    # --- K Schema -------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [q1]Römisch eins: Verwaltungsrechtsweg, weil es um das Ob geht. [q2]Römisch zwei: der "
     "Zulassungsanspruch aus der Gemeindeordnung. [q2a]Erstens, öffentliche Einrichtung, [q2b]zweitens, berechtigter Nutzer, "
     "[q2c]drittens, Widmung und Kapazität, [q2d]viertens, Gleichbehandlung. [q3]Römisch drei: Betreibt eine Gesellschaft die "
     "Einrichtung, Einwirkungsanspruch gegen die Gemeinde. [q4]Römisch vier: Das Wie regelt der Mietvertrag.", PS),
    # --- L Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Über das Ob entscheidet das öffentliche Recht, über das Wie oft das Privatrecht. [mk2]Und schiebt die "
     "Stadt eine Gesellschaft vor, bleibt sie selbst in der Pflicht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
