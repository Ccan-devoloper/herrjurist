"""Folge 112 · Schuldnerverzug § 286 BGB: Wann gibt es Zinsen und Mahnkosten? (Mo · Der Fall · Zivilrecht/Schuldrecht AT,
Format Schema). Beispielfall nach dem Plan-Hook („Der Kunde zahlt die Rechnung nicht – ab wann schuldet er Verzugszinsen
und Anwaltskosten?“): Klara (Fahrradwerkstatt mit Laden, Unternehmerin) verkauft Gustav (privat, Verbraucher) am 2.7.2026
ein Elektrorad für 2.400 €; er nimmt es mit, Rechnung „zahlbar sofort“ ohne Hinweis nach § 286 Abs. 3 Satz 1 Halbs. 2.
Er zahlt nicht. Erste Mahnung von Klara selbst (mit 5 € Mahngebühr), Zugang 10.8.2026; Gustav meldet sich nicht.
Am 1.9.2026 beauftragt Klara eine Anwältin, deren Schreiben 231,95 € kostet; Gustav zahlt weiter nicht.
Kern als Schema: I. Voraussetzungen § 286 – 1. fälliger, durchsetzbarer Anspruch (§§ 433 Abs. 2, 271 Abs. 1; Verweis 103),
2. Mahnung § 286 Abs. 1 Satz 1 (Wortlaut; BGH VII ZR 107/25 Rn. 48) oder Entbehrlichkeit § 286 Abs. 2 Nr. 1, 3
(VIII ZR 215/15 Rn. 23), 3. 30-Tage-Regel § 286 Abs. 3 Satz 1 (Wortlaut; VIII ZR 215/15 Rn. 18), 4. Vertretenmüssen
§ 286 Abs. 4 (VIII ZR 175/14 Rn. 18); Zeitstrahl; II. Rechtsfolgen – § 288 Abs. 1 (Wortlaut; Basiszinssatz 1,52 % seit
1.7.2026, bundesbank.de), § 288 Abs. 2, 5 als Abgrenzung, Verzögerungsschaden §§ 280 Abs. 1, 2, 286 (VIII ZR 138/23
Rn. 71, 77; IX ZR 280/14 Rn. 9; IV ZR 292/13 Rn. 51), § 287; Ergebnis mit Zeitstrahl; Klausurtipp; Schema; Merksatz.
Figuren: Klara (julia), Gustav (helmut); Lexi/Erzählerin Carla. Belege: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Klara": "julia", "Gustav": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: in der Fahrradwerkstatt, 2. Juli 2026 -----------------------------------------------------------------
    ("[fall]Klara hat eine kleine Fahrradwerkstatt mit Laden. [kauf]Am zweiten Juli zweitausendsechsundzwanzig kauft "
     "Gustav dort privat ein Elektrorad für zweitausendvierhundert Euro. [rech]Er nimmt es gleich mit, dazu die Rechnung: "
     "zahlbar sofort. [hinw]Einen Hinweis, dass er nach dreißig Tagen in Verzug kommt, enthält sie nicht.", 0.3),
    ("[gu1]Ich überweise das in den nächsten Tagen.", 0.3, "Gustav"),
    # --- A2 Fall: Klara schreibt die Mahnung ------------------------------------------------------------------------------
    ("[mahn]Doch Gustav zahlt nicht. Im August schreibt Klara ihm selbst eine Mahnung.", 0.3),
    ("[kl1]Bitte zahlen Sie jetzt die zweitausendvierhundert Euro, dazu fünf Euro Mahngebühr.", 0.3, "Klara"),
    # --- A3 Fall: bei Gustav zu Hause -------------------------------------------------------------------------------------
    ("[zug]Am zehnten August liegt der Brief in seinem Briefkasten.", 0.3),
    ("[gu2]Das hat noch Zeit. Gerade bin ich knapp bei Kasse.", 0.3, "Gustav"),
    ("[still]Er meldet sich nicht. [anw]Am ersten September beauftragt Klara eine Anwältin. [anw2]Deren Schreiben kostet "
     "sie zweihunderteinunddreißig Euro fünfundneunzig, [noch]und Gustav zahlt immer noch nicht.", 0.4),
    ("[frage]Ab wann schuldet Gustav Verzugszinsen? [frage2]Und muss er die Mahngebühr und die Anwaltskosten ersetzen?", 0.5),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Vier Voraussetzungen -------------------------------------------------------------------------------------------
    ("[plan]Der Verzug nach Paragraf zweihundertsechsundachtzig hat vier Voraussetzungen: [p1]einen fälligen, "
     "durchsetzbaren Anspruch, [p2]eine Mahnung oder ihre Entbehrlichkeit, [p3]oder stattdessen die Dreißig-Tage-Regel, "
     "[p4]und Vertretenmüssen. [p5]Danach kommen die Rechtsfolgen.", PS),
    # --- D I. 1. Fälliger, durchsetzbarer Anspruch ------------------------------------------------------------------------
    ("[a1]Erstens: ein fälliger, durchsetzbarer Anspruch. [a433]Klara hat einen Anspruch auf den Kaufpreis, Paragraf "
     "vierhundertdreiunddreißig Absatz zwei. [afaell]Fällig ist er sofort, Paragraf zweihunderteinundsiebzig Absatz eins. "
     "[aeinr]Und er ist durchsetzbar: Klara hat das Rad schon übergeben, eine Einrede hat Gustav nicht. [a103]Mehr dazu im Video "
     "zu Einwendung und Einrede.", P),
    # --- E I. 2. Mahnung, § 286 Abs. 1 Satz 1 (Wortlaut) ------------------------------------------------------------------
    ("[m1]Zweitens: die Mahnung. Paragraf zweihundertsechsundachtzig Absatz eins Satz eins: Leistet der Schuldner auf eine "
     "Mahnung des Gläubigers nicht, die nach dem Eintritt der Fälligkeit erfolgt, so kommt er durch die Mahnung in Verzug. "
     "[mdef]Mahnung ist jede eindeutige und bestimmte Aufforderung, die geschuldete Leistung zu erbringen. [mfall]Der "
     "Brief von Klara erreicht Gustav am zehnten August, nach der Fälligkeit.", P),
    # --- F Entbehrlichkeit, § 286 Abs. 2 ----------------------------------------------------------------------------------
    ("[ent]Entbehrlich ist die Mahnung nach Absatz zwei etwa, [ent1]wenn für die Leistung eine Zeit nach dem Kalender "
     "bestimmt ist; ein Termin, den nur der Gläubiger setzt, genügt grundsätzlich nicht. [ent3]Oder wenn der "
     "Schuldner die Leistung ernsthaft und endgültig verweigert. [entn]Beides liegt hier nicht vor.", PS),
    # --- G I. 3. Dreißig-Tage-Regel, § 286 Abs. 3 Satz 1 (Wortlaut) -------------------------------------------------------
    ("[d1]Drittens: die Dreißig-Tage-Regel. Nach Absatz drei Satz eins kommt der Schuldner einer Entgeltforderung "
     "spätestens in Verzug, wenn er nicht innerhalb von dreißig Tagen nach Fälligkeit und Zugang einer Rechnung leistet. "
     "[d2]Gegenüber einem Verbraucher gilt das aber nur, wenn die Rechnung auf diese Folgen besonders hinweist. "
     "[d3]Gustav ist Verbraucher, und der Hinweis fehlt. [d4]Die Regel hilft Klara also nicht.", P),
    # --- H I. 4. Vertretenmüssen, § 286 Abs. 4 ----------------------------------------------------------------------------
    ("[v1]Viertens: Vertretenmüssen. Nach Absatz vier kommt der Schuldner nicht in Verzug, solange die Leistung infolge "
     "eines Umstands unterbleibt, den er nicht zu vertreten hat. [vverm]Das Vertretenmüssen wird also vermutet. "
     "[vgeld]Knapp bei Kasse zu sein, entlastet nicht: Für seine finanzielle "
     "Leistungsfähigkeit muss jeder einstehen.", PS),
    # --- I Zwischenergebnis am Zeitstrahl ---------------------------------------------------------------------------------
    ("[zs]Zwischenergebnis am Zeitstrahl: [zs1]Fällig wird der Kaufpreis am zweiten Juli. [zs2]Nach dreißig Tagen "
     "passiert nichts, der Hinweis fehlt. [zs3]Erst mit der Mahnung am zehnten August kommt Gustav in Verzug.", PS),
    # --- J II. Rechtsfolgen: Verzugszinsen, § 288 Abs. 1 (Wortlaut) -------------------------------------------------------
    ("[r1]Römisch zwei: die Rechtsfolgen. Zuerst die Zinsen, Paragraf zweihundertachtundachtzig Absatz eins: Eine "
     "Geldschuld ist während des Verzugs zu verzinsen. Der Verzugszinssatz beträgt für das Jahr fünf Prozentpunkte über "
     "dem Basiszinssatz. [rbasis]Der Basiszinssatz liegt seit dem ersten Juli zweitausendsechsundzwanzig bei eins Komma "
     "fünf zwei Prozent. [rsatz]Für Gustav also sechs Komma fünf zwei Prozent im Jahr, "
     "rund dreizehn Euro im Monat. [rnach]Einen Schaden muss Klara dafür nicht nachweisen.", P),
    ("[r2]Ohne Verbraucher wären es bei Entgeltforderungen neun Prozentpunkte, Absatz zwei, [r5]dazu "
     "vierzig Euro Pauschale, Absatz fünf. [rnein]Beides scheidet hier aus, Gustav ist Verbraucher.", PS),
    # --- K Verzögerungsschaden, §§ 280 Abs. 1, 2, 286, und § 287 ------------------------------------------------------------
    ("[s1]Weitere Schäden ersetzt Paragraf zweihundertachtzig Absatz eins und zwei mit Paragraf "
     "zweihundertsechsundachtzig: der Verzögerungsschaden. [s2]Er muss aber durch den Verzug entstanden sein. [s3]Die "
     "fünf Euro Mahngebühr scheiden deshalb aus: Die erste Mahnung hat den Verzug erst begründet, sie ist Sache des "
     "Gläubigers. [s4]Anders die Anwältin: Sie kam erst, als Gustav schon in Verzug war. [s5]Solche "
     "Anwaltskosten sind nach dem Bundesgerichtshof regelmäßig ersatzfähig, auch in einfachen Fällen.", P),
    ("[s287]Paragraf zweihundertsiebenundachtzig verschärft zudem die Haftung: Im Verzug hat der Schuldner jede "
     "Fahrlässigkeit zu vertreten und haftet wegen der Leistung auch für Zufall.", PS),
    # --- L Ergebnis (Zeitstrahl) --------------------------------------------------------------------------------------------
    ("[e1]Ergebnis: Gustav muss die zweitausendvierhundert Euro zahlen, [e2]dazu Verzugszinsen ab dem elften August, "
     "dem Tag nach dem Zugang der Mahnung. [e3]Die Anwaltskosten von zweihunderteinunddreißig Euro fünfundneunzig muss "
     "er ersetzen, [e4]die Mahngebühr nicht.", PS),
    # --- M Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bestimme zuerst den Tag des Verzugsbeginns und prüfe dann jede Kostenposition "
     "einzeln. [tipp2]Typischer Fehler: Lässt der Gläubiger schon die erste Mahnung vom Anwalt schreiben, sind dessen "
     "Kosten kein Verzugsschaden.", PS),
    # --- N Klausurschema ----------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema: [k1]Römisch eins: die Voraussetzungen. [k11]Eins: fälliger, durchsetzbarer Anspruch. [k12]Zwei: "
     "Mahnung oder Entbehrlichkeit. [k13]Drei: oder die Dreißig-Tage-Regel. [k14]Vier: Vertretenmüssen, vermutet. "
     "[k2]Römisch zwei: die Rechtsfolgen. [k21]Verzugszinsen, [k22]Verzögerungsschaden [k23]und Haftungsverschärfung.", PS),
    # --- O Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Zinsen und Verzugskosten gibt es erst ab dem Verzug. [mk2]Beim Verbraucher löst ihn meist erst die "
     "Mahnung aus, [mk3]und diese erste Mahnung zahlt der Gläubiger selbst.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
