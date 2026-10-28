"""Folge 204 · Sachrüge StPO: Wenn die Feststellungen das Urteil nicht tragen (Fr · 2. Examen · StPO-Praxis, Format Schema).
Beispielfall nach dem Plan-Hook („Das Urteil verurteilt wegen Betrugs, sagt aber kein Wort dazu, worin der Vermögensschaden
liegen soll“): Die Strafkammer des Landgerichts verurteilt Herrn Wichmann wegen Betrugs zu zwei Jahren und sechs Monaten
Freiheitsstrafe. Laut den Feststellungen verkaufte er Frau Danner einen Oldtimer für 85.000 € als „unfallfrei“, obwohl er
den schweren Unfallschaden kannte; sie glaubte ihm und zahlte. Zum Wert des Wagens mit Unfallschaden enthält das Urteil
nichts; strafschärfend nennt es einen „hohen Schaden“. Rechtsanwältin Hellmers bereitet die Revisionsbegründung vor.
Prüfung: § 337 Abs. 1, 2 StPO (Wortlautkarte: Gesetzesverletzung, Beruhen) → allgemeine Sachrüge (§ 344 Abs. 2 S. 1
Wortlautkarte; „Ich rüge die Verletzung materiellen Rechts.“; BGH 3 StR 300/20 Rn. 2) → Prüfungsgrundlage allein die
Urteilsurkunde (BGH 4 StR 569/15 Rn. 23), urteilsfremdes Vorbringen unbeachtlich (BGH 3 StR 277/22 Rn. 28), Verweis
Verfahrensrüge (Folgen 066/072) → vier Stufen: a) Subsumtion (BGH 1 StR 171/19 Rn. 47), b) Darstellungsmangel
(§ 267 Abs. 1 S. 1 Wortlautkarte; BGH 1 StR 482/24 Rn. 6), c) Beweiswürdigung (BGH 1 StR 52/26 Rn. 6), d) Strafzumessung
(BGH 5 StR 125/26 Rn. 8) → Fall: Gesamtsaldierung (BGH 2 StR 77/22 Rn. 8), Kauf (BGH 2 StR 283/25 Rn. 10, 11, 13),
Beruhen, Aufhebung § 353, Zurückverweisung § 354 Abs. 2 → Klausurtipp (Lexi) → Schema → Merksatz (Lexi).
Belege je Aussage: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben, in namen_reserviert.txt eingetragen: Wichmann,
Hellmers, Danner. Stimmen: Herr Wichmann stephan, Rechtsanwältin Hellmers lucy, Frau Danner hilde; Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Wichmann": "stephan", "Hellmers": "lucy", "Danner": "hilde"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: in der Kanzlei --------------------------------------------------------------------------------------------
    ("[fall]Eine Anwaltskanzlei. Das schriftliche Urteil ist gerade gekommen. [urteil]Das Landgericht hat Herrn Wichmann "
     "wegen Betrugs zu zwei Jahren und sechs Monaten Freiheitsstrafe verurteilt. [liest]Seine Verteidigerin, Rechtsanwältin "
     "Hellmers, liest die Urteilsgründe.", P),
    # --- A2 Fall: Rückblick, der Verkauf des Oldtimers ----------------------------------------------------------------------
    ("[rueck]Laut den Feststellungen verkaufte Herr Wichmann Frau Danner einen Oldtimer für fünfundachtzigtausend Euro.", P),
    ("[w1]Der Wagen ist unfallfrei.", P, "Wichmann"),
    ("[d1]Dann nehme ich ihn.", P, "Danner"),
    ("[unfall]In Wahrheit hatte der Wagen einen schweren Unfall hinter sich, und Herr Wichmann wusste das. [zahlt]Frau "
     "Danner glaubte ihm und zahlte.", P),
    # --- A3 Fall: zurück in der Kanzlei -------------------------------------------------------------------------------------
    ("[h1]Täuschung, Irrtum, Zahlung. Alles da. Aber was war der Wagen wert? Dazu steht hier kein Wort.", P, "Hellmers"),
    ("[w2]Der Wagen war das Geld doch wert!", P, "Wichmann"),
    ("[frage]Kann Herr Wichmann mit der Revision rügen, dass zum Schaden nichts im Urteil steht? [frage2]Und zählt, was er "
     "selbst über den Wert sagt?", PS),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 337 StPO --------------------------------------------------------------------------------------------------------
    ("[p337]Die Revision prüft nur Rechtsfehler. Paragraf dreihundertsiebenunddreißig: Das Urteil muss auf einer Verletzung "
     "des Gesetzes beruhen. [p337b]Verletzt ist das Gesetz, wenn eine Rechtsnorm nicht oder nicht richtig angewendet worden "
     "ist. [zwei]Zu prüfen sind also zwei Dinge: die Gesetzesverletzung [beruh]und das Beruhen.", PS),
    # --- D Allgemeine Sachrüge -----------------------------------------------------------------------------------------------
    ("[sach]Für Fehler im materiellen Recht gibt es die Sachrüge. [p344]Nach Paragraf dreihundertvierundvierzig Absatz zwei "
     "muss die Begründung nur zeigen, ob eine Rechtsnorm über das Verfahren oder eine andere Rechtsnorm verletzt sein soll. "
     "[satz]Deshalb genügt ein Satz: Ich rüge die Verletzung materiellen Rechts. [umf]Dann prüft das Revisionsgericht das "
     "Urteil umfassend auf sachlich-rechtliche Fehler.", PS),
    # --- E Prüfungsgrundlage: nur die Urteilsurkunde -------------------------------------------------------------------------
    ("[grund]Aber nur anhand der Urteilsurkunde: [feld]der Feststellungen, der Beweiswürdigung und der Strafzumessung. "
     "[akte]Die Akte zählt nicht, und was in der Hauptverhandlung gesagt wurde, rekonstruiert das Revisionsgericht nicht. "
     "[fremd]Was Herr Wichmann über den Wert sagt, steht nicht im Urteil. Es ist urteilsfremd und bleibt bei der Sachrüge "
     "außer Betracht. [verf]Für Fehler im Ablauf der Hauptverhandlung braucht es die Verfahrensrüge; dazu gibt es eigene Folgen.", PS),
    # --- F Vier Prüfungsstufen -----------------------------------------------------------------------------------------------
    ("[stufen]Auf die Sachrüge prüfst du vier Stufen. [sa]Erstens Subsumtionsfehler: Die Feststellungen sind vollständig, "
     "aber das Gericht wendet das Gesetz falsch an. [sa2]Hier nicht: Unfallfrei ist eine Tatsache, kein bloßes Werturteil. "
     "Die Täuschung ist richtig bejaht.", P),
    ("[sb]Zweitens der Darstellungsmangel. [p267]Paragraf zweihundertsiebenundsechzig Absatz eins: Die Urteilsgründe müssen "
     "die für erwiesen erachteten Tatsachen angeben, in denen die gesetzlichen Merkmale der Straftat gefunden werden. "
     "[sb2]Für jedes Merkmal braucht es also festgestellte Tatsachen. Fehlen sie, kann das Revisionsgericht die Subsumtion "
     "nicht nachprüfen.", P),
    ("[sc]Drittens die Beweiswürdigung. [sc2]Sie ist Sache des Tatgerichts und nur angreifbar, wenn sie lückenhaft, "
     "widersprüchlich oder unklar ist oder gegen Denkgesetze oder gesicherte Erfahrungssätze verstößt. [sc3]Hier stützt die "
     "Kammer den Unfallschaden schlüssig auf einen Sachverständigen.", P),
    ("[sd]Viertens die Strafzumessung. [sd2]Auch sie ist Sache des Tatgerichts. Das Revisionsgericht greift nur bei Rechtsfehlern ein, etwa wenn "
     "die Erwägungen in sich fehlerhaft sind oder sich die Strafe vom gerechten Schuldausgleich löst. [sd3]Hier wertet die "
     "Kammer strafschärfend einen hohen Schaden, den sie nirgends beziffert.", PS),
    # --- G Der Fall: fehlender Vermögensschaden ------------------------------------------------------------------------------
    ("[schaden]Zurück zum Darstellungsmangel. [saldo]Ein Vermögensschaden liegt vor, wenn die Verfügung den Gesamtwert des "
     "Vermögens mindert, ohne dass ein Zuwachs das ausgleicht. [kauf]Wer beim Kauf über wertbildende Umstände getäuscht wird, "
     "ist nach dem Bundesgerichtshof regelmäßig nur geschädigt, wenn die Sache objektiv den vereinbarten Preis nicht wert "
     "ist. [preis]Auf der einen Seite stehen also fünfundachtzigtausend Euro, [wert]auf der anderen der Wert des Wagens mit "
     "Unfallschaden. [luecke]Diesen Wert stellt das Urteil nicht fest. [traegt]Damit belegen die Feststellungen keinen "
     "Vermögensschaden. Der Schuldspruch wegen Betrugs hält sachlich-rechtlicher Prüfung nicht stand.", P),
    ("[beruhen]Darauf beruht er auch: Es ist nicht auszuschließen, dass der Wagen den Preis wert war. Dann fehlte der Schaden. [strafe]Mit dem Schuldspruch fällt "
     "die Strafe. [selbst]Selbst entscheiden kann der Bundesgerichtshof nicht, denn dafür braucht es neue Feststellungen. "
     "[aufh]Er hebt das Urteil auf, Paragraf dreihundertdreiundfünfzig, [zur]und verweist die Sache an eine andere "
     "Strafkammer zurück, Paragraf dreihundertvierundfünfzig Absatz zwei.", PS),
    # --- H Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp für deine Revisionsbegründung. [k1]Erhebe zuerst die allgemeine Sachrüge mit dem einen Satz. "
     "[k2]Dann führe sie aus, in dieser Reihenfolge: erst der Schuldspruch, Merkmal für Merkmal, dann die Strafzumessung. "
     "[k3]Formuliere eng am Urteil: Die Feststellungen belegen keinen Vermögensschaden; den Wert des Wagens teilt das Urteil "
     "nicht mit. [k4]Und argumentiere nur mit den Urteilsgründen, nie mit der Akte.", PS),
    # --- I Prüfschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema zur Sachrüge. [s1]Römisch eins: die allgemeine Sachrüge. [s2]Römisch zwei: Grundlage ist allein "
     "das Urteil. [s3]Römisch drei: der Schuldspruch, mit Subsumtion, Darstellung und Beweiswürdigung. [s4]Römisch vier: die "
     "Strafzumessung. [s5]Römisch fünf: das Beruhen, dann Aufhebung und Zurückverweisung.", PS),
    # --- J Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Sachrüge prüft nur das Urteil. [m2]Fehlt dort die Tatsache für ein Merkmal, trägt das Urteil den "
     "Schuldspruch nicht, und aus der Akte füllt das Revisionsgericht die Lücke nicht.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
