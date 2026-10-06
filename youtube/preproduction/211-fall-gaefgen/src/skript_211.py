"""Folge 211 · Fall Gäfgen: Folterdrohung, § 136a StPO & Fernwirkung (Mo · Der Fall · StPO · Klassiker-Fall).
Leitentscheidungen: EGMR (Große Kammer), Gäfgen/Deutschland, Urt. v. 1.6.2010 – Nr. 22978/05 (HUDOC 001-99015, zitiert mit §§);
LG Frankfurt a. M., Beschl. v. 9.4.2003 und Urt. v. 28.7.2003 (nach EGMR §§ 24–36); LG Frankfurt a. M., Urt. v. 20.12.2004 –
5/27 KLs 7570 Js 203814/03 (4/04), NJW 2005, 692 (Daschner; Inhalt nach EGMR §§ 47–51); BGH 1 StR 316/05 Rn. 22 f.;
BGHSt 34, 362, 364 (Fernwirkung grundsätzlich abgelehnt).
DARSTELLUNG: Das Kind wird nie gezeigt und nie benannt, keine Tatdetails, keine Gewalt, keine Folterinstrumente; die Drohung
steht nur als Sprechblase. Täter, Polizisten und Richterin sind fiktive Figuren mit fiktiven Namen: Herr Wallmann
(Beschuldigter, spricht nicht), Herr Rombach (stellvertretender Polizeipräsident; Stimme william), Kommissar Leitner (marc),
Verteidigerin (sabrina), Vorsitzende Richterin (laura_ruhig). „Gäfgen“ nur als Fallbezeichnung auf Titel und Tafel.
Erzählerin und Lexi: Carla ohne Rolle.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter. Belege je Cue: ../RECHTSSTAND.md."""

P, PS = 0.3, 0.5

STIMMEN = {"Rombach": "william", "Leitner": "marc", "Verteidigerin": "sabrina", "Richterin": "laura_ruhig"}

SEGMENTE = [
    # --- A Fall: Polizeipräsidium (EGMR §§ 12–18, 47) -------------------------------------------------------------------
    ("[fall]Frankfurt am Main, Herbst zweitausendzwei. [entf]Ein Kind ist entführt, die Eltern sollen eine Million Euro "
     "Lösegeld zahlen. [fest]Die Polizei beobachtet, wie Herr Wallmann das Geld abholt, und nimmt ihn fest. [falsch]Wo das "
     "Kind ist, verrät er nicht; er gibt nur falsche Hinweise.", P),
    ("[vize]Am nächsten Morgen will der stellvertretende Polizeipräsident, Herr Rombach, nicht länger warten.", 0.2),
    ("[ro1]Drohen Sie ihm Schmerzen an. Er muss sagen, wo das Kind ist.", P, "Rombach"),
    ("[leit]Kommissar Leitner führt die Anweisung aus.", 0.2),
    ("[le1]Sagen Sie, wo das Kind ist. Sonst werden Ihnen große Schmerzen zugefügt.", P, "Leitner"),
    ("[nennt]Nach rund zehn Minuten nennt Herr Wallmann das Versteck. [spaet]Für das Kind kommt jede Hilfe zu spät. "
     "[spur]Am Versteck sichert die Polizei Beweise gegen ihn, etwa Reifenspuren seines Autos.", P),
    ("[frage]Darf das Gericht seine Aussage verwerten? [frage2]Was ist mit den Spuren vom Versteck? [frage3]Und durfte die "
     "Polizei so handeln? [echt]Unser Fall folgt einem echten Fall, den zweitausendzehn der Europäische Gerichtshof für "
     "Menschenrechte entschieden hat.", PS),
    # --- B Sachverhalt ----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C § 136a StPO (Wortlaut; EGMR §§ 26, 28–30) -----------------------------------------------------------------------
    ("[norm]Die Antwort beginnt in Paragraf hundertsechsunddreißig a der Strafprozessordnung. [wl]Er schützt die Freiheit "
     "der Willensentschließung des Beschuldigten, etwa vor Misshandlung und Quälerei. [wl2]Und er sagt: Die Drohung mit "
     "einer unzulässigen Maßnahme ist verboten.", P),
    ("[sub]Schmerzen zuzufügen, um eine Aussage zu erzwingen, ist nie erlaubt. [sub2]Also war schon die Drohung damit "
     "verboten. [abs3]Die Folge steht in Absatz drei: Solche Aussagen dürfen nicht verwertet werden, auch wenn der "
     "Beschuldigte zustimmt. [gesetz]Hier entscheidet das Gesetz selbst, nicht erst eine Abwägung wie bei Belehrungsfehlern; "
     "[v171]die zeigt unsere Folge zum Belehrungsverstoß.", P),
    ("[fort]Das Landgericht Frankfurt ging noch weiter: [fort2]Auch alle späteren Aussagen bei Polizei, Staatsanwaltschaft "
     "und Richter waren unverwertbar, weil die Drohung fortwirkte. [qual]Das hätte nur eine qualifizierte Belehrung "
     "geändert, also der Hinweis, dass die früheren Aussagen nicht verwertet werden dürfen. [nurs]Belehrt wurde er aber "
     "nur über sein Schweigerecht.", PS),
    # --- D Fernwirkung in der Hauptverhandlung (EGMR §§ 25, 31–35; BGH 1 StR 316/05 Rn. 22 f.) ---------------------------
    ("[hv]In der Hauptverhandlung beantragt die Verteidigerin mehr.", 0.2),
    ("[ve1]Dann dürfen auch die Beweise vom Versteck nicht verwertet werden!", P, "Verteidigerin"),
    ("[fern]Das ist die Frage der Fernwirkung, bekannt als Lehre von den Früchten des vergifteten Baumes. [bgh]Der "
     "Bundesgerichtshof lehnt eine Fernwirkung grundsätzlich ab: [bgh2]Ein Verfahrensfehler soll nicht das ganze "
     "Strafverfahren lahmlegen. [lg]Das Landgericht wog im Fall ab: [lg2]die Schwere des Eingriffs gegen die Schwere des "
     "Vorwurfs, Mord an einem Kind. [lg3]Die Spuren auszuschließen, wäre unverhältnismäßig. Sie bleiben verwertbar.", P),
    ("[rich]Vor seiner Einlassung belehrt ihn die Vorsitzende Richterin neu.", 0.2),
    ("[ri1]Sie dürfen schweigen. Ihre früheren Aussagen werden nicht gegen Sie verwertet.", P, "Richterin"),
    ("[gest]Trotzdem gesteht Herr Wallmann noch einmal, aus Reue, wie er sagt. [urt]Auf dieses neue Geständnis stützt das "
     "Gericht die Verurteilung; [pruef]die Spuren dienen nur noch dazu, es zu überprüfen. [lebens]Das Urteil: lebenslange "
     "Freiheitsstrafe.", PS),
    # --- E EGMR: Art. 3 und Art. 6 EMRK (EGMR §§ 87, 107 f., 131 f., 165–188, Tenor) ------------------------------------
    ("[egmr]Herr Wallmann zieht vor den Europäischen Gerichtshof für Menschenrechte. [a3]Artikel drei der Konvention: "
     "Niemand darf der Folter oder unmenschlicher oder erniedrigender Behandlung oder Strafe unterworfen werden.", P),
    ("[ub]Die Große Kammer sieht in der Drohung eine unmenschliche Behandlung, aber noch keine Folter. [abs]Das Verbot "
     "gilt absolut, auch wenn ein Leben auf dem Spiel steht. [verl]Artikel drei ist verletzt.", P),
    ("[a6]Und das faire Verfahren nach Artikel sechs? [regel]Aussagen, die unter Verstoß gegen Artikel drei erlangt "
     "wurden, darf ein Gericht nie verwerten, Sachbeweise aus Folter ebenso wenig. [bear]Bei Sachbeweisen nach "
     "unmenschlicher Behandlung kommt es darauf an, ob sie das Urteil beeinflusst haben. [kette]Hier beruhte es auf dem "
     "neuen Geständnis, die Kette war unterbrochen. [a6nein]Artikel sechs ist nicht verletzt, entschieden mit elf zu "
     "sechs Stimmen.", PS),
    # --- F Die Polizisten: § 34 StGB, Menschenwürde (LG Frankfurt 20.12.2004 nach EGMR §§ 47–50, 124) -------------------
    ("[pol]Und die Polizisten? [lg04]Das Landgericht Frankfurt verurteilte Kommissar Leitner wegen Nötigung, "
     "[lg04b]Herrn Rombach, weil er seinen Untergebenen dazu verleitet hatte.", P),
    ("[n34]Gerechtfertigt durch Notstand, Paragraf vierunddreißig? [gef]Rombach glaubte, das Leben des Kindes retten zu "
     "können. [mw]Doch die Drohung verletzte die Menschenwürde aus Artikel eins Absatz eins Grundgesetz. [abs2]Ihr Schutz "
     "ist absolut und lässt keine Abwägung zu, also auch keinen Notstand. [v013]Warum die Würde nicht abwägbar ist, zeigt "
     "unsere Folge zum Luftsicherheitsgesetz, [v189]das Notstandsschema die Folge zu Paragraf vierunddreißig.", P),
    ("[strafe]Das Gericht verwarnte beide nur, mit Strafvorbehalt: [tagess]Die Geldstrafen müssen sie nur zahlen, wenn "
     "sie in der Bewährungszeit erneut straffällig werden. [mild]Dem Europäischen Gerichtshof war das zu mild.", PS),
    # --- G Klausurtipp mit Prüfungsaufbau (Lexi) ---------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne drei Fragen. [t1]Erstens: Ist die Aussage verwertbar? Paragraf hundertsechsunddreißig a "
     "Absatz drei, mit Fortwirkung und qualifizierter Belehrung. [t2]Zweitens: Sind die Folgebeweise verwertbar? "
     "Grundsätzlich keine Fernwirkung; [t2b]dazu die Kontrolle nach Artikel sechs: Hat der Beweis das Urteil beeinflusst? "
     "[t3]Drittens: Sind die Beamten strafbar? Der Notstand scheitert an der Menschenwürde.", PS),
    # --- H Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Eine Aussage unter verbotener Drohung ist stets unverwertbar. [m2]Für die Spuren daraus gibt es "
     "grundsätzlich keine Fernwirkung. [m3]Und die Menschenwürde kennt keine Ausnahme, auch nicht zur Rettung.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
