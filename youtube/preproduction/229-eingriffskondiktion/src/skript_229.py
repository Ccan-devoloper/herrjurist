"""Folge 229 · Dein Foto in fremder Werbung: Die Eingriffskondiktion (§ 812 BGB) (Mo · Der Fall · Bereicherungsrecht ·
Klassiker-Fall; §§ 812 Abs. 1 Satz 1 Alt. 2, 818 Abs. 2 BGB; § 22 Satz 1 KUG). Leitentscheidung: BGH, Urt. v. 8.5.1956 –
I ZR 62/54, BGHZ 20, 345 (Paul Dahlke) – Volltext frei nicht abrufbar; Inhalt über BGH I ZR 41/24 Rn. 124, 126 und eine
Sekundärquelle belegt; tragende Aussagen an BGH VI ZR 123/11 Rn. 24, I ZR 120/19 Rn. 24, 26, 36, 38, 58 f., I ZR 234/10
Rn. 15, 42, IX ZR 204/11 Rn. 15, I ZR 187/10 Rn. 46, VI ZR 250/19 Rn. 8 – Belege je Cue in ../RECHTSSTAND.md.
DARSTELLUNG: Paul Dahlke (reale Person) erscheint nicht als Figur, nur als Fallbezeichnung auf der Fundstellen-Pille. Im Fall
der fiktive Kai Möbius und die fiktive Limonadenfirma „Brauselust“ (keine echte Marke); Marketingleiter Wendorf, eine
Kollegin und ein Fotograf (stumm) sind ebenfalls erfunden.
Stimmen: Kai (niklas), Wendorf (helmut), Kollegin (ela_froh, heiterer Satz); julia nicht besetzt. Erzählerin und Lexi: Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; keine Abkürzungen (synth_el buchstabiert BGB, BGH; „GmbH“
und „KUG“ werden deshalb nicht gesprochen)."""

P, PS = 0.3, 0.5

STIMMEN = {"Kollegin": "ela_froh", "Kai": "niklas", "Wendorf": "helmut"}  # Lexi = Carla

SEGMENTE = [
    # --- A1 Fall: das Plakat an der Bushaltestelle ------------------------------------------------------------------------
    ("[fall]Kai Möbius wartet an der Bushaltestelle. [plakat]Neben ihm hängt ein neues Werbeplakat: Brauselust, die "
     "Limonade für den Sommer. [gesicht]Und auf dem Plakat: Kai, lachend, mit einer Flasche in der Hand.", P),
    ("[k1]Kai, guck mal! Das bist ja du, auf dem Plakat!", P, "Kollegin"),
    ("[ka1]Das bin ja ich. Gefragt hat mich niemand!", P, "Kai"),
    # --- A2 Rückblick: im Stadtpark -----------------------------------------------------------------------------------------
    ("[park]Das Foto entstand im Sommer im Stadtpark. [knips]Ein Fotograf der Firma Brauselust hat Kai beim Trinken "
     "fotografiert, ohne dass er es bemerkte. [plakate]Jetzt hängt das Bild auf hundertzwanzig Plakaten in der ganzen Stadt.", P),
    # --- A3 Im Büro der Firma -----------------------------------------------------------------------------------------------
    ("[buero]Kai geht zu Herrn Wendorf, dem Marketingleiter.", P),
    ("[ka2]Sie werben mit meinem Gesicht. Dafür will ich die übliche Lizenz: dreitausend Euro.", P, "Kai"),
    ("[w1]Sie hätten doch nie für Limonade geworben. Also haben Sie auch nichts verloren.", P, "Wendorf"),
    ("[frage]Muss die Firma zahlen, und wie viel? [lizenz]Für ein solches Werbefoto zahlt man üblicherweise dreitausend "
     "Euro. [klassiker]Unser Fall folgt einem Klassiker: [bgh]Neunzehnhundertsechsundfünfzig entschied der "
     "Bundesgerichtshof über die Werbung mit dem Bild eines Schauspielers, ohne dessen Einwilligung.", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C I. Anspruchsgrundlage (Wortlautkarte § 812 Abs. 1 Satz 1 BGB), Vorrang der Leistungskondiktion -----------------
    ("[norm]Anspruchsgrundlage ist Paragraf achthundertzwölf Absatz eins Satz eins. [w812]Wer durch die Leistung eines "
     "anderen oder in sonstiger Weise auf dessen Kosten etwas ohne rechtlichen Grund erlangt, ist ihm zur Herausgabe "
     "verpflichtet. [alt2]Hier geht es um die zweite Alternative, die Bereicherung in sonstiger Weise: die "
     "Eingriffskondiktion.", P),
    ("[vorr]Vorher fragst du: Hat Kai etwas geleistet? [nein]Nein. Er hat der Firma nichts zugewendet; sie hat sich sein "
     "Bild einfach genommen. [verweis]Warum die Leistungskondiktion sonst Vorrang hat, zeigt unsere Folge zum "
     "Bereicherungsrecht im Überblick.", PS),
    # --- D 1. Etwas erlangt (VI ZR 123/11 Rn. 24; I ZR 120/19 Rn. 58) ------------------------------------------------------
    ("[erl]Erstens: Was hat die Firma erlangt? [nutz]Nicht das Foto als Gegenstand, sondern die Nutzung von Kais Bildnis "
     "für ihre Werbung. [bgh1]So sieht es auch der Bundesgerichtshof: Bereicherungsgegenstand ist die Nutzung des "
     "Bildnisses.", P),
    # --- E 2. Auf Kosten: Lehre vom Zuweisungsgehalt (IX ZR 204/11 Rn. 15); § 22 S. 1 KUG (Wortlautkarte) -----------------
    ("[kosten]Zweitens: auf Kosten von Kai. [zuw]Hier hilft die Lehre vom Zuweisungsgehalt. [def]Die Eingriffskondiktion "
     "knüpft an die Verletzung einer Rechtsposition an, die dem Berechtigten zur ausschließlichen Verfügung und Verwertung "
     "zugewiesen ist.", P),
    ("[kug]Welche Rechtsposition ist das hier? Das Recht am eigenen Bild. [w22]Paragraf zweiundzwanzig Satz eins "
     "Kunsturhebergesetz: Bildnisse dürfen nur mit Einwilligung des Abgebildeten verbreitet oder öffentlich zur Schau "
     "gestellt werden. [werb]Ob und wie sein Bild für Werbung genutzt wird, entscheidet also Kai. [verm]Das ist ein "
     "vermögensrechtlicher Bestandteil seines Persönlichkeitsrechts. [eing]Wer ein fremdes Bildnis unbefugt für Werbung "
     "nutzt, greift deshalb in diesen Zuweisungsgehalt ein.", P),
    # --- F 3. Ohne rechtlichen Grund (I ZR 120/19 Rn. 36, 38) --------------------------------------------------------------
    ("[org]Drittens: ohne rechtlichen Grund. [einw]Eine Einwilligung hat Kai nie erteilt. [p23]Und auf die Ausnahme für "
     "Bildnisse aus dem Bereich der Zeitgeschichte kann sich nicht berufen, wer das Bild eines anderen allein für seine "
     "Werbung verwertet. [tbm]Alle Voraussetzungen liegen also vor.", PS),
    # --- G Rechtsfolge § 818 Abs. 2 (Wortlautkarte); fiktive Lizenz (I ZR 120/19 Rn. 58 f.) ------------------------------
    ("[rf]Und die Rechtsfolge? [unm]Die Nutzung selbst kann die Firma nicht herausgeben. [w818]Deshalb gilt Paragraf "
     "achthundertachtzehn Absatz zwei: Ist die Herausgabe wegen der Beschaffenheit des Erlangten nicht möglich oder ist "
     "der Empfänger aus einem anderen Grunde zur Herausgabe außerstande, so hat er den Wert zu ersetzen. [lizw]Der Wert der "
     "Nutzung ist die übliche Lizenzgebühr, die sogenannte fiktive Lizenz: also das, was vernünftige Vertragspartner "
     "vereinbart hätten. [hier]Hier sind das dreitausend Euro.", P),
    # --- Einwand Wendorf (VI ZR 123/11 Rn. 24; I ZR 41/24 Rn. 124) -------------------------------------------------------
    ("[einwand]Und der Einwand von Herrn Wendorf? [egal]Ob Kai für Limonade geworben hätte, ist unerheblich. [fing]Der "
     "Zahlungsanspruch unterstellt keine Zustimmung; er gleicht den rechtswidrigen Eingriff in eine Befugnis aus, die "
     "allein Kai zusteht. [wert]Wer ein fremdes Bild für Werbung nutzt, zeigt, dass er ihm einen wirtschaftlichen Wert "
     "beimisst. Daran muss er sich festhalten lassen.", P),
    # --- Entreicherung (§§ 818 Abs. 3, 819 Abs. 1, 818 Abs. 4 BGB) ------------------------------------------------------
    ("[entr]Auf Entreicherung nach Paragraf achthundertachtzehn Absatz drei kann sich die Firma nicht berufen: [kennt]Sie "
     "wusste, dass Kai nicht eingewilligt hatte, und haftet deshalb nach Paragraf achthundertneunzehn Absatz eins verschärft.", PS),
    # --- H Parallele Ansprüche (I ZR 120/19 Rn. 26; I ZR 41/24 Rn. 126; VI ZR 250/19 Rn. 8) ------------------------------
    ("[par]Daneben hat Kai weitere Ansprüche. [p823]Schadensersatz nach Paragraf achthundertdreiundzwanzig Absatz eins "
     "wegen Verletzung seines Persönlichkeitsrechts, oder nach Absatz zwei in Verbindung mit Paragraf zweiundzwanzig "
     "Kunsturhebergesetz. [versch]Diese Ansprüche setzen aber Verschulden voraus; die Eingriffskondiktion nicht. "
     "[unt]Und entsprechend Paragraf tausendvier Absatz eins Satz zwei kann Kai verlangen, dass die Firma die Werbung mit "
     "seinem Bild unterlässt.", PS),
    # --- I Ergebnis (zurück an die Bushaltestelle) ------------------------------------------------------------------------
    ("[erg]Ergebnis: Die Firma muss Kai dreitausend Euro zahlen, als Wertersatz nach Paragraf achthundertzwölf Absatz eins "
     "Satz eins, zweite Alternative, und Paragraf achthundertachtzehn Absatz zwei. [erg2]Und mit seinem Bild werben darf "
     "sie nicht mehr.", PS),
    # --- J Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe die Eingriffskondiktion auch dann, wenn der Schadensersatz am Verschulden scheitert; sie "
     "braucht keins. [tipp2]Und begründe das Merkmal auf dessen Kosten mit dem Zuweisungsgehalt: Ein Vermögensverlust des "
     "Abgebildeten ist nicht nötig.", PS),
    # --- K Prüfschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Eingriffskondiktion. [s1]Eins: etwas erlangt, hier die Nutzung des Bildnisses. [s2]Zwei: in "
     "sonstiger Weise, also ohne Leistung. [s3]Drei: auf Kosten des Anspruchstellers, durch Eingriff in den "
     "Zuweisungsgehalt, hier das Recht am eigenen Bild. [s4]Vier: ohne rechtlichen Grund, also ohne Einwilligung. "
     "[s5]Fünf: Rechtsfolge nach Paragraf achthundertachtzehn Absatz zwei: Wertersatz in Höhe der üblichen Lizenzgebühr.", PS),
    # --- L Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer mit einem fremden Bild wirbt, greift in dessen Zuweisungsgehalt ein. [m2]Er schuldet die übliche "
     "Lizenzgebühr, auch ohne Verschulden und auch, wenn der Abgebildete nie zugestimmt hätte.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    assert not re.search(r"\bGmbH\b|\bKUG\b|\d", text), "Abkürzung oder Ziffer im Sprechtext"
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
