"""Folge 154 · Wunsiedel-Beschluss: Darf ein Gesetz eine Meinung verbieten? (Mo · Der Fall · Klassiker-Fall;
Art. 5 I, II GG; § 130 IV StGB). Echter Fall sachlich nacherzählt: BVerfG, Beschl. v. 4.11.2009 – 1 BvR 2150/08,
BVerfGE 124, 300 (Wunsiedel), Volltext bundesverfassungsgericht.de, zitiert nur mit Rn. (LS = Leitsatz).
Allgemeines Gesetz (Kombinationsformel) zusätzlich BVerfGE 7, 198 <209 f.> (Lüth, Folge 146).
HÖCHSTE SENSIBILITÄT: Rudolf Heß wird einmal sachlich benannt („führender Nationalsozialist“, Rn. 19); keine Figur für
ihn oder für Teilnehmer, keine Darstellung der Veranstaltung, keine Symbole, keine Parolen, keine Zitate von Teilnehmern
oder Transparenten (auch nicht das Motto aus Rn. 7). Kein Pro und Contra zur NS-Ideologie.
Fiktive Figuren: Swantje (Jurastudentin, Stimme lucy) und Professor Ahlborn (Seminarleiter, Stimme christian).
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter. Belege je Cue: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Swantje": "lucy", "Ahlborn": "christian"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Einstieg im Seminar (fiktiv) ----------------------------------------------------------------------------------
    ("[fall]Grundrechte-Seminar. [buch]Professor Ahlborn legt ein Gesetzbuch auf den Tisch und fragt:", P),
    ("[ah1]Darf ein Gesetz eine bestimmte Meinung verbieten?", P, "Ahlborn"),
    ("[sw1]Eigentlich nicht. Ein Gesetz muss doch für alle Meinungen gleich gelten.", P, "Swantje"),
    ("[klassiker]Das Bundesverfassungsgericht hat diese Frage im Wunsiedel-Beschluss beantwortet.", PS),
    # --- B Der echte Fall (Rn. 1–9, 24) ---------------------------------------------------------------------------------
    ("[stadt]In der Stadt Wunsiedel liegt das Grab von Rudolf Heß, einem führenden Nationalsozialisten. [anm]Ein "
     "Veranstalter meldet dort jährlich eine Gedenkveranstaltung für ihn an, auch für den "
     "zwanzigsten August zweitausendfünf. [verbot]Das Landratsamt verbietet die Veranstaltung "
     "nach dem Versammlungsgesetz. [grund]Begründung: Es drohe eine Straftat nach Paragraf hundertdreißig Absatz vier StGB.", P),
    ("[klage]Der Veranstalter klagt und scheitert in drei Instanzen, zuletzt beim Bundesverwaltungsgericht. [vb]Er erhebt Verfassungsbeschwerde: "
     "[vbgrund]Paragraf hundertdreißig Absatz vier sei kein allgemeines Gesetz, weil er sich gegen eine bestimmte "
     "politische Richtung wende.", P),
    ("[frage]Darf der Gesetzgeber eine Meinung gezielt verbieten?", PS),
    # --- C Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D I. Schutzbereich (Rn. 45, 49 f.) ----------------------------------------------------------------------------
    ("[a5]Artikel fünf Absatz eins: Jeder hat das Recht, seine Meinung in Wort, Schrift und Bild frei zu äußern und zu "
     "verbreiten. [wert]Geschützt ist eine Meinung, egal ob sie wertvoll oder wertlos, gefährlich oder harmlos ist. "
     "[ns]Selbst die Verbreitung nationalsozialistischen Gedankenguts fällt nicht von vornherein aus dem Schutzbereich. "
     "[art8]Weil die Versammlung wegen ihres Inhalts "
     "verboten wurde, richtet sich auch Artikel acht hier nach Artikel fünf; [brok]mehr dazu beim Brockdorf-Beschluss.", P),
    # --- E § 130 Abs. 4 StGB, Eingriff (Rn. 3, 51) ---------------------------------------------------------------------
    ("[p130]Paragraf hundertdreißig Absatz vier bestraft, wer öffentlich oder in einer Versammlung den öffentlichen "
     "Frieden in einer die Würde der Opfer verletzenden Weise dadurch stört, dass er die nationalsozialistische Gewalt- "
     "und Willkürherrschaft billigt, verherrlicht oder rechtfertigt. [eingriff]Die Vorschrift knüpft an den Inhalt "
     "einer Meinung an und greift damit in die Meinungsfreiheit ein.", P),
    # --- F III. Rechtfertigung: allgemeine Gesetze (Rn. 54–58; BVerfGE 7, 198 <209 f.>) --------------------------------
    ("[a52]Absatz zwei: Diese Rechte finden ihre Schranken in den "
     "Vorschriften der allgemeinen Gesetze. [wann]Doch wann ist ein Gesetz allgemein? [sonder]Die Sonderrechtslehre "
     "fragt: Richtet es sich gegen eine Meinung als solche? [abwl]Die Abwägungslehre fragt: Schützt es ein Rechtsgut, "
     "das Vorrang vor der Meinungsfreiheit hat? [kombi]Schon im Lüth-Urteil verbindet das Gericht beides: Das Gesetz "
     "darf nicht eine Meinung als solche verbieten, sondern muss ein Rechtsgut schützen, das ohne Rücksicht "
     "auf eine bestimmte Meinung zu schützen ist und Vorrang vor der Meinungsfreiheit hat. [blind]Es muss meinungsneutral sein, gleichsam blind gegenüber denen, auf die es angewendet wird.", P),
    # --- G § 130 Abs. 4 StGB ist kein allgemeines Gesetz (Rn. 10, 61 f.) ---------------------------------------------------
    ("[bverwg]Das Bundesverwaltungsgericht hielt Paragraf hundertdreißig Absatz vier noch für ein allgemeines Gesetz, "
     "[nein]das Bundesverfassungsgericht nicht. [frieden]Zwar schützt die Vorschrift den öffentlichen Frieden, "
     "ein Rechtsgut, das auch sonst geschützt wird. [nur]Aber sie erfasst nur Äußerungen, die eine bestimmte Haltung zum "
     "Nationalsozialismus ausdrücken, nicht die Gutheißung anderer totalitärer Regime. [antwort]Und sie entstand als "
     "Antwort auf Versammlungen von Rechtsradikalen, gerade auch auf die Gedenkveranstaltungen in Wunsiedel. "
     "[sonderr]Damit ist sie Sonderrecht. [ehre]Auch die Schranke der persönlichen Ehre trägt sie nicht.", P),
    ("[sw2]Dann wäre das Verbot doch verfassungswidrig?", P, "Swantje"),
    # --- H1 Die Ausnahme (LS 1, Rn. 64–66) -----------------------------------------------------------------------------
    ("[ah2]Nein. Das Gericht erkennt eine Ausnahme an.", P, "Ahlborn"),
    ("[zitat]Für Bestimmungen, die der propagandistischen Gutheißung der nationalsozialistischen Gewalt- und "
     "Willkürherrschaft Grenzen setzen, ist Artikel fünf Absatz eins und zwei eine Ausnahme vom Verbot des Sonderrechts "
     "für meinungsbezogene Gesetze immanent. [unrecht]Der Grund liegt im einzigartigen Unrecht und Schrecken dieser Herrschaft. [gegen]Das "
     "Grundgesetz kann geradezu als Gegenentwurf dazu gedeutet werden. [identi]Wer diese Herrschaft gutheißt, greift die "
     "Identität des Gemeinwesens an, mit friedensbedrohendem Potenzial.", P),
    # --- H2 Grenzen der Ausnahme (LS 2, Rn. 66–68) ----------------------------------------------------------------------
    ("[ah3]Aber Vorsicht: Für andere Meinungen gilt diese Ausnahme nicht.", P, "Ahlborn"),
    ("[geist]Rechtsradikales "
     "oder nationalsozialistisches Gedankengut allein wegen seiner geistigen Wirkung zu verbieten, erlaubt das Grundgesetz nicht. "
     "[vhm]Und auch Sonderrecht muss "
     "verhältnismäßig sein.", P),
    # --- I Verhältnismäßigkeit, öffentlicher Friede (Rn. 69–85, 95, 97 f., 103) -----------------------------------------
    ("[zweck]Legitimer Zweck ist der öffentliche Friede, aber eng verstanden: [kein]nicht als Schutz vor beunruhigenden "
     "Meinungen oder vor einer Vergiftung des geistigen Klimas, [friedl]sondern als Friedlichkeit, als Schutz vor "
     "Äußerungen, die erkennbar auf Aggression oder Rechtsbruch angelegt sind. [gea]Dafür ist die Vorschrift geeignet, "
     "erforderlich und angemessen. [verm]Bei einer Billigung kann die Störung des Friedens grundsätzlich vermutet "
     "werden, [atyp]außer in untypischen Fällen, etwa bei kleinen geschlossenen Versammlungen. [ww]Und wie im Lüth-Urteil gilt die "
     "Wechselwirkung: Die Vorschrift ist im Licht der Meinungsfreiheit auszulegen.", P),
    # --- J Anwendung im Fall, Ergebnis (Rn. 101, 107 f.; Tenor) --------------------------------------------------------
    ("[anw]Und im Fall? [symbol]Die Ehrung einer Person kann eine Billigung sein, wenn sie als Symbolfigur für die "
     "nationalsozialistische Herrschaft als solche steht. [person]Ein Lob, das nur der Person gilt, reicht nicht. "
     "[vertretbar]Hier durfte das Bundesverwaltungsgericht annehmen, dass die geplante Versammlung die "
     "nationalsozialistische Herrschaft im Ganzen gebilligt hätte. [erg]Ergebnis: Die Verfassungsbeschwerde wird "
     "zurückgewiesen.", PS),
    # --- K Zurück ins Seminar --------------------------------------------------------------------------------------------
    ("[sw3]Also darf ein Gesetz eine bestimmte Meinung verbieten?", P, "Swantje"),
    ("[ah4]Nur in dieser einen Ausnahme. Sonst muss es meinungsneutral sein.", PS, "Ahlborn"),
    # --- L Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe bei Artikel fünf Absatz zwei zuerst, ob das Gesetz allgemein ist. [tipp2]Wenn nicht, ist "
     "es Sonderrecht und grundsätzlich unzulässig. [tipp3]Die Wunsiedel-Ausnahme überträgst du nicht auf "
     "andere Meinungen.", PS),
    # --- M Prüfschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k1]Römisch eins: Schutzbereich, Artikel fünf Absatz eins Satz eins, auch für "
     "verfassungsfeindliche Meinungen. [k2]Römisch zwei: Eingriff. [k3]Römisch drei: "
     "Rechtfertigung. [k3a]Erstens: allgemeines Gesetz, also meinungsneutral? [k4]Zweitens: Wenn nein, Sonderrecht, zulässig "
     "nur in der Wunsiedel-Ausnahme. [k5]Drittens: Verhältnismäßigkeit, mit engem Begriff des öffentlichen Friedens. "
     "[k6]Viertens: Auslegung im Licht der Meinungsfreiheit.", PS),
    # --- N Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Ein Gesetz, das sich gegen eine bestimmte Meinung richtet, ist kein allgemeines Gesetz. [m2]Erlaubt "
     "ist solches Sonderrecht nur gegen die Gutheißung der nationalsozialistischen Gewalt- und Willkürherrschaft, und "
     "auch dann nur verhältnismäßig.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
