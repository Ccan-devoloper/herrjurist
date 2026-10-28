"""Folge 279 · E-Examen Jura: Klausuren am Computer schreiben (Fr · Methodik · Examen, Format Methodik).
Rahmen nach dem Plan-Hook („Statt Stift jetzt Tastatur – was ändert sich wirklich?“): In einem fiktiven Prüfungssaal
stehen Laptops auf den Tischen. Die Jurastudentin Telse (Anfang 20, Nordrhein-Westfalen) schreibt bald die Aufsichtsarbeiten
der staatlichen Pflichtfachprüfung; ihr Bruder Jost (Ende 20) hat das zweite Examen in Bayern am Laptop geschrieben.
Aufbau nach Auftrag: Hook → Sachverhalt → Was ist das E-Examen (Wortlautkarte § 5d Abs. 6 DRiG; Länderbeispiele NRW und
Bayern als Tafel) → Was ändert sich (Gliederung, Korrigieren/Umstellen, Rechtschreibung, Zeit, Lesbarkeit) → Was bleibt
(Aufgabentext und Konzeptpapier auf Papier, Gesetze und Kommentare als Bücher, Gutachtenstil, Schwerpunkte) →
Vorbereitung (Probeklausuren am Rechner, Zehnfingersystem, Demoportale, Tastatur) → Ergebnis (Saal) → Klausurtipp (Lexi)
→ E-Examen in 5 Schritten → Merksatz (Lexi). Länderangaben nur für die an amtlicher Quelle geprüften Länder NRW
(§§ 10, 13, 51 JAG NRW; Seiten des Landesjustizprüfungsamts) und Bayern (Seiten des Landesjustizprüfungsamts; JAPO auf
gesetze-bayern.de gesperrt, nicht umgangen). Keine Softwaremarken, keine Statistik. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Volltextsuche unter youtube/preproduction und themenplanung:
0 Treffer; Reservierung „279: Telse, Jost“): Telse, Jost; nie im Genitiv.
Stimmen (Pool niklas, helmut, ela_froh, julia): Telse ela_froh (Frau, jung, fröhlich – Thema ohne Ernstfall), Jost niklas
(Mann, jung); julia nicht (Vorfolge 273), helmut (älter) passt zu keiner Rolle. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen, Paragrafen und Gesetzesnamen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Telse": "ela_froh", "Jost": "niklas"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Prüfungssaal mit Laptops --------------------------------------------------------------------------------
    ("[fall]Ein Prüfungssaal kurz vor dem Examen. [lap]Auf den Tischen stehen Laptops. [tel]Telse studiert Jura in "
     "Nordrhein-Westfalen und schreibt bald ihre Examensklausuren. [jos]Ihr Bruder Jost hat sein zweites Examen in Bayern "
     "schon am Laptop geschrieben.", P),
    ("[t1]Tippen oder mit der Hand schreiben? Was ändert sich da wirklich?", P, "Telse"),
    ("[j1]Mehr als die Tastatur. Aber das Wichtigste bleibt gleich.", P, "Jost"),
    ("[hook]Statt Stift jetzt Tastatur. [hook2]Das ist das E-Examen: Du schreibst die Examensklausuren am Computer. "
     "[wie]Hier siehst du, wo das geregelt ist, was sich ändert, was bleibt und wie du dich vorbereitest.", P),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist die Ausgangslage von Telse. Halte das Video ruhig kurz an.", 5.0),
    # --- C Rechtsgrundlage: § 5d Abs. 6 DRiG (Wortlaut) ------------------------------------------------------------------
    ("[was]Wo ist das E-Examen geregelt? [drig]Im Deutschen Richtergesetz, Paragraf fünf d Absatz sechs. [wl1]Das Nähere "
     "regelt das Landesrecht. [wl2]Es kann auch bestimmen, dass in den staatlichen Prüfungen schriftliche Leistungen "
     "elektronisch erbracht werden dürfen. [land]Ob und wie, entscheidet also dein Land. Hier zwei Beispiele.", P),
    # --- D Länderbeispiele: NRW und Bayern -------------------------------------------------------------------------------
    ("[nrw]In Nordrhein-Westfalen müssen die Prüfungsämter seit dem ersten Januar zweitausendvierundzwanzig die "
     "elektronische Klausur ermöglichen, im ersten und im zweiten Examen. [nrw2]Du hast die Wahl zwischen Hand und Laptop. "
     "[nrw3]Laut Landesjustizprüfungsamt kannst du sogar vor Beginn einer Klausur noch zur Hand wechseln. [by]In Bayern "
     "gibt es das E-Examen im zweiten Examen seit dem zweiten Termin zweitausendvierundzwanzig, im ersten seit dem zweiten "
     "Termin zweitausendsechsundzwanzig. [by2]Auch dort ist es freiwillig. Du wählst aber schon vor der Prüfung, und die "
     "Wahl ist grundsätzlich bindend. [beide]In beiden Ländern schreibst du im Prüfungssaal auf einem gestellten Laptop. "
     "Ein eigener ist nicht erlaubt.", P),
    # --- E Was ändert sich? ----------------------------------------------------------------------------------------------
    ("[aend]Was ändert sich beim Schreiben? [gl]Erstens die Gliederung: Überschriften setzt du mit Absätzen und Einzügen. "
     "Eine automatische Gliederung bietet die bayerische Software nicht. [um]Zweitens das Korrigieren und Umstellen: Du "
     "löschst, fügst ein und verschiebst ganze Absätze, ohne dass etwas durchgestrichen ist. [rs]Eine Rechtschreibprüfung "
     "kannst du in Nordrhein-Westfalen ein- und ausschalten, in Bayern gibt es keine.", P),
    ("[j2]Ich habe deshalb am Ende selbst Korrektur gelesen.", P, "Jost"),
    ("[zeit]Drittens die Zeit: In Bayern zeigt die Prüfungssoftware keine Uhr an. [zeit2]Eine Viertelstunde vor Schluss "
     "gibt die Aufsicht einen Hinweis, und abgeben musst du dort selbst per Klick. [zeit3]In Nordrhein-Westfalen wird "
     "die Arbeit bei Zeitablauf automatisch gespeichert. [les]Viertens die Lesbarkeit: Deine "
     "Handschrift muss niemand mehr entziffern. [les2]In Bayern bekommen die Prüfer deine Arbeit ausgedruckt, den "
     "Korrekturrand ergänzt die Software.", P),
    # --- F Was bleibt? ---------------------------------------------------------------------------------------------------
    ("[bleibt]Was bleibt gleich? [pap]Den Aufgabentext bekommst du in beiden Ländern weiter auf Papier. [komm]Die "
     "Gesetzestexte bringst du selbst mit, als Bücher, im zweiten Examen in Nordrhein-Westfalen auch die Kommentare. "
     "Elektronisch gibt es sie nicht. "
     "[gut]Und es geht um dasselbe wie bisher: Gutachtenstil, Argumente und die richtigen Schwerpunkte. [mehr]Tippen geht "
     "schneller und verführt zu langen Texten. Mehr Text ist aber nicht automatisch besser.", P),
    # --- G Vorbereitung --------------------------------------------------------------------------------------------------
    ("[vorb]Wie bereitest du dich vor? [probe]Schreib deine Probeklausuren am Rechner, in voller Länge und mit fester Zeit. "
     "[zehn]Übe das Tippen mit zehn Fingern, damit dein Blick beim Text bleibt. [demo]Beide Länder bieten ein Demoportal "
     "mit der Schreiboberfläche. [demo2]Das nordrhein-westfälische speichert zwischen und eignet sich laut Prüfungsamt "
     "auch für längere Probeklausuren. [demo3]Das bayerische zeigt nur die Funktionen, speichern kann es nicht. [tast]In "
     "Bayern darfst du eine eigene Tastatur mitbringen, aber nur ein zugelassenes Modell.", P),
    # --- H Ergebnis ------------------------------------------------------------------------------------------------------
    ("[erg]Telse setzt sich an einen der Laptops und tippt die ersten Sätze.", 0.2),
    ("[t2]Ich schreibe am Laptop. Vorher übe ich im Demoportal und schreibe jede Probeklausur am Rechner.", P, "Telse"),
    ("[j3]Und gliedere zuerst auf dem Papier. Dann erst tippst du.", PS, "Jost"),
    # --- I Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Mach die Lösungsskizze zuerst auf dem Konzeptpapier und markiere dort deine Schwerpunkte. "
     "[tipp2]Erst dann tippst du das Gutachten. [tipp3]Verschieben geht am Laptop zwar leicht, aber ein Umbau mitten in "
     "der Klausur kostet Zeit.", PS),
    # --- J E-Examen in fünf Schritten (Schema) ---------------------------------------------------------------------------
    ("[sch]Dein E-Examen in fünf Schritten. [k1]Römisch eins: Regeln deines Landes prüfen, also Wahl und Frist. "
     "[k2]Römisch zwei: Demoportal ausprobieren. [k3]Römisch drei: Probeklausuren am Rechner schreiben. [k4]Römisch vier: "
     "Lösungsskizze auf Papier, dann tippen. [k5]Römisch fünf: Zeit und Schwerpunkte im Blick behalten.", PS),
    # --- K Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Im E-Examen ändert sich das Werkzeug, nicht der Maßstab. [m2]Es zählen Gutachtenstil und Schwerpunkte. "
     "[m3]Ob und wie du am Laptop schreibst, regelt dein Land, also frag dein Prüfungsamt.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
