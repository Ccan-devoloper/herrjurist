"""Folge 226 · Erfundenes Interview: Allgemeines Persönlichkeitsrecht im Zivilrecht (Mo · Der Fall · Deliktsrecht ·
Klassiker-Fall; § 823 Abs. 1 BGB i. V. m. Art. 1 Abs. 1, Art. 2 Abs. 1 GG). Leitentscheidung: BGH, Urt. v. 15.11.1994 –
VI ZR 56/94, BGHZ 128, 1 (Caroline von Monaco). Volltext frei nicht abrufbar; Inhalt belegt über BGH VI ZR 332/94 (Volltext),
BGH VI ZR 211/12 (BGHZ 199, 237), VI ZR 255/03 (BGHZ 160, 298), BVerfG 1 BvR 1127/96 sowie BVerfGE 34, 269 (Soraya),
54, 148 (Eppler), 54, 208 (Böll), 97, 125 – Belege je Cue in ../RECHTSSTAND.md.
DARSTELLUNG: Die reale Person wird nicht gezeigt und nicht karikiert; im Fall eine fiktive Schauspielerin (Juliane Hellberg)
und ein fiktives Magazin („Funkelblatt“, kein echter Verlag). Der echte Fall nur als „ein erfundenes Interview mit einer
Prinzessin“, der Name nur als Fallbezeichnung auf der Fundstellen-Pille.
Fiktiver Rahmen: Leserin am Kiosk (Stimme ela_froh, heiterer Satz), Chefredakteur Kettler (niklas), Juliane Hellberg
(Schauspielerin; julia – einzige ernste Frauenrolle, ela_froh dafür ungeeignet), Anwalt Dr. Ruhnau (helmut).
Erzählerin und Lexi: Carla ohne Rolle.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter; keine Abkürzungen (synth_el buchstabiert BGB, GG, BGH)."""

P, PS = 0.3, 0.5

STIMMEN = {"Leserin": "ela_froh", "Kettler": "niklas", "Juliane": "julia", "Ruhnau": "helmut"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall: das erfundene Exklusiv-Interview (fiktiv, Nachbildung des Klassikers) ----------------------------------
    ("[fall]Am Kiosk liegt das neue Funkelblatt. [titel]Auf dem Titel: Exklusiv! Juliane Hellberg spricht über ihre "
     "Trennung. [seiten]Im Heft folgen vier Seiten Interview mit der Schauspielerin.", P),
    ("[l1]Ein Exklusiv-Interview mit Juliane Hellberg! Das nehme ich mit.", P, "Leserin"),
    ("[nie]Doch Juliane Hellberg hat nie mit dem Magazin gesprochen. [erfunden]Jedes Wort ist erfunden.", P),
    ("[redakt]In der Redaktion weiß man das. [auflage]Das Heft erscheint in einer Auflage von vierhunderttausend "
     "Exemplaren.", P),
    ("[ke1]Mit ihrem Namen auf dem Titel verkaufen wir mehr Hefte. Das Interview schreiben wir eben selbst.", P, "Kettler"),
    ("[kanzlei]Frau Hellberg geht zu ihrem Anwalt.", P),
    ("[j1]Ich habe nie mit diesem Magazin gesprochen!", P, "Juliane"),
    ("[r1]Dann verlangen wir Unterlassung, Widerruf und eine Geldentschädigung.", P, "Ruhnau"),
    ("[frage]Zu Recht? Und wonach richtet sich die Höhe der Geldentschädigung? [klassiker]Unser Fall ist einem Klassiker "
     "nachgebildet: Im echten Fall ging es um ein erfundenes Interview mit einer Prinzessin. [bgh]Der Bundesgerichtshof "
     "entschied am fünfzehnten November neunzehnhundertvierundneunzig.", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C I. Anspruchsgrundlage, sonstiges Recht, Rahmenrecht (Wortlautkarten § 823 I BGB, Art. 2 I, Art. 1 I GG) --------
    ("[norm]Anspruchsgrundlage ist Paragraf achthundertdreiundzwanzig Absatz eins. [w823]Wer vorsätzlich oder fahrlässig "
     "das Leben, den Körper, die Gesundheit, die Freiheit, das Eigentum oder ein sonstiges Recht eines anderen "
     "widerrechtlich verletzt, ist dem anderen zum Ersatz des daraus entstehenden Schadens verpflichtet. [schema]Das "
     "Grundschema kennst du aus unserer Folge zu Paragraf achthundertdreiundzwanzig.", P),
    ("[sonst]Das allgemeine Persönlichkeitsrecht steht nicht im Gesetzestext. [bghz13]Der Bundesgerichtshof hat es "
     "neunzehnhundertvierundfünfzig als sonstiges Recht anerkannt. [wurzel]Es wurzelt im Grundgesetz. [a21]Artikel zwei "
     "Absatz eins: Jeder hat das Recht auf die freie Entfaltung seiner Persönlichkeit. [a11]In Verbindung mit Artikel eins "
     "Absatz eins: Die Würde des Menschen ist unantastbar.", P),
    ("[rahmen]Anders als Körper oder Eigentum ist es ein Rahmenrecht. [abw]Seine Reichweite steht nicht von vornherein fest. "
     "Ob ein Eingriff rechtswidrig ist, zeigt erst eine Abwägung mit den Belangen der anderen Seite.", P),
    # --- D II. Eingriff: Unterschieben nicht getaner Äußerungen (BVerfGE 54, 148 LS 1, <155>; 34, 269 <282 f.>) ------------
    ("[mund]Was schützt es hier? [eppler]Das Persönlichkeitsrecht schützt davor, dass jemandem Äußerungen in den Mund "
     "gelegt werden, die er nicht getan hat. [selbst]Jeder soll selbst entscheiden, ob und wie er mit eigenen Worten an "
     "die Öffentlichkeit tritt. [privat]Das erfundene Interview betrifft zudem ihr Privatleben. [eingriff]Ein Eingriff "
     "liegt also vor.", P),
    # --- E III. Abwägung: Pressefreiheit (Wortlautkarte Art. 5 I 2 GG; BVerfGE 34, 269 <283 f.>; 54, 208 LS 2) -------------
    ("[presse]Auf der anderen Seite steht das Magazin. [a52]Artikel fünf Absatz eins Satz zwei: Die Pressefreiheit und die "
     "Freiheit der Berichterstattung durch Rundfunk und Film werden gewährleistet. [unterh]Das gilt auch für die "
     "Unterhaltungspresse. [nichts]Aber das Bundesverfassungsgericht sagt: Zu einer wirklichen Meinungsbildung kann ein "
     "erfundenes Interview nichts beitragen. [zitat]Auch das unrichtige Zitat schützt die Meinungsfreiheit nicht.", P),
    ("[vorrang]Die Abwägung fällt deshalb klar aus: Das Persönlichkeitsrecht überwiegt, der Eingriff ist rechtswidrig. "
     "[vors]Und weil die Redaktion das Interview bewusst erfunden hat, handelt sie vorsätzlich.", P),
    # --- F IV. Rechtsfolgen: Unterlassung, Widerruf (VI ZR 314/10 Rn. 8; BVerfGE 97, 125 LS 1, Rn. 85, 89) ----------------
    ("[folgen]Welche Ansprüche hat Frau Hellberg? [unterl]Erstens Unterlassung, nach Paragraf tausendvier Absatz eins "
     "Satz zwei analog in Verbindung mit Paragraf achthundertdreiundzwanzig Absatz eins: Das Magazin darf das Interview "
     "nicht weiter verbreiten. [widerruf]Zweitens Widerruf: Das Magazin muss öffentlich klarstellen, dass das Interview nie "
     "stattgefunden hat, notfalls auf der Titelseite.", P),
    # --- Geldentschädigung: Voraussetzungen, Abgrenzung § 253 II (VI ZR 211/12 Rn. 38, 40, 43 f.; BGHZ 128, 1, 13 f., 15 f.) ---
    ("[geld]Drittens die Geldentschädigung. [vor2]Sie setzt einen schwerwiegenden Eingriff voraus, der nicht in anderer "
     "Weise befriedigend aufgefangen werden kann. [schwer]Hier: ein erfundenes Interview über das Privatleben, groß auf "
     "dem Titel, mit Vorsatz. [reicht]Ein Widerruf allein gleicht das nicht aus. [p253]Achtung: Das ist kein Schmerzensgeld "
     "nach Paragraf zweihundertdreiundfünfzig Absatz zwei; dort fehlt das Persönlichkeitsrecht. [schutz]Der Anspruch geht "
     "auf den Schutzauftrag der Artikel eins und zwei des Grundgesetzes zurück.", P),
    # --- Höhe: Genugtuung, Prävention, Gewinnerzielung (BGHZ 128, 1, 15 f. nach VI ZR 332/94; BVerfG 1 BvR 1127/96 Rn. 9) ---
    ("[hoehe]Und die Höhe? [genug]Im Vordergrund steht die Genugtuung; außerdem soll die Entschädigung der Prävention "
     "dienen. [kommerz]Wer die Persönlichkeit eines Menschen vorsätzlich als Mittel zur Auflagensteigerung einsetzt, "
     "betreibt nach dem Bundesgerichtshof eine rücksichtslose Zwangskommerzialisierung. [gewinn]Dann gehört die Erzielung "
     "von Gewinnen als Bemessungsfaktor in die Entscheidung über die Höhe. [hemm]Von der Entschädigung muss ein echter "
     "Hemmungseffekt ausgehen. [grenze]Eine Gewinnabschöpfung ist das aber nicht, und die Höhe darf die Pressefreiheit "
     "nicht unverhältnismäßig einschränken.", PS),
    # --- G Ergebnis (zurück in die Kanzlei) -----------------------------------------------------------------------------
    ("[erg]Ergebnis: Frau Hellberg kann Unterlassung und Widerruf verlangen [erg2]und eine Geldentschädigung, bei deren "
     "Höhe das Gericht auch den angestrebten Gewinn berücksichtigt. [echt]Dass der angestrebte Gewinn in die Höhe "
     "einfließt, hat der Bundesgerichtshof im Fall der Prinzessin entschieden.", PS),
    # --- I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe Unterlassung, Widerruf und Geldentschädigung getrennt; jeder Anspruch hat eigene "
     "Voraussetzungen. [tipp2]Beim Persönlichkeitsrecht ist die Rechtswidrigkeit nicht schon durch den Eingriff indiziert; "
     "du begründest sie mit der Abwägung. [tipp3]Und stütze die Geldentschädigung nicht auf Paragraf "
     "zweihundertdreiundfünfzig Absatz zwei, sondern auf Paragraf achthundertdreiundzwanzig Absatz eins in Verbindung mit "
     "den Artikeln eins und zwei des Grundgesetzes.", PS),
    # --- J Prüfschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für die Geldentschädigung. [s1]Eins: Eingriff in das allgemeine Persönlichkeitsrecht als sonstiges "
     "Recht. [s2]Zwei: Rechtswidrigkeit nach Abwägung. [s3]Drei: Verschulden. [s4]Vier: eine schwerwiegende Verletzung, "
     "[s4b]die nicht anders befriedigend aufgefangen werden kann. [s5]Fünf: die Höhe, mit Genugtuung, Prävention und "
     "angestrebtem Gewinn.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer einem Menschen Worte in den Mund legt, verletzt sein Persönlichkeitsrecht. [m2]Und wer damit "
     "vorsätzlich Auflage macht, muss mit einer Geldentschädigung rechnen, die auch den angestrebten Gewinn berücksichtigt.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    assert all(len(s) == 2 or s[2] in STIMMEN for s in SEGMENTE)
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
