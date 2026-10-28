"""Folge 243 · § 252 StPO: Die Ehefrau schweigt – Verhörsperson als Zeuge? (Fr · Klausurpraxis · StPO · Streitstand).
Hook nach dem Themenplan: Eine Ehefrau belastet ihren Mann bei der Polizei schwer, beruft sich vor Gericht aber auf ihr
Zeugnisverweigerungsrecht. Delikt neutral: Betrug im gemeinsamen Malerbetrieb (Rechnungen für Arbeiten, die nie gemacht
wurden). Keine Gewalt, keine Beziehungskonflikte.
Aufbau: Fall (Malerbetrieb → Polizei → Hauptverhandlung mit Vernehmung des Polizeibeamten → Urteil, Revision) → Fragen →
Sachverhalt → § 252 (Wortlautkarte, vollständig gesprochen) → Streit: Rspr. Verwertungsverbot, Verhörsperson unzulässig
(GSSt 1/16 Rn. 32; 3 StR 377/18 Rn. 12; 1 StR 222/23 Rn. 7) vs. Wortlaut-Ansicht und umfassendes Verbot (GSSt 1/16 Rn. 29,
36), GSSt 1/16 Rn. 26/64 → Ausnahme Richter (Leitsatz, Rn. 32, 63; Vorhalt: 3 StR 108/12) → Gestattung (2 StR 112/12 Rn. 7 f.;
1 StR 222/23 Rn. 6, 8) → Äußerungen außerhalb einer Vernehmung (1 StR 137/12 Rn. 12) → Lösung als Revisionsrüge (§ 344 Abs. 2
S. 2 Wortlautkarte; 2 StR 112/12 Rn. 6 f.; 3 StR 108/12; 1 StR 222/23 Rn. 4, 12; Verweis 072) → Klausurtipp (Lexi) →
Merksatz (Lexi). Grundlagen § 52 und Beweisverwertungsverbote nur verwiesen (Folgen 224, 221). Belege: ../RECHTSSTAND.md.
Namen (eindeutig deutsch, in keiner früheren Folge, reserviert): Hasselbach (Ehepaar). Polizeibeamter, Vorsitzender,
Verteidigerin und Freundin sind Funktionsrollen.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.35, 0.7

STIMMEN = {"Polizeibeamter": "marc", "Vorsitzender": "william", "Hasselbach": "sabrina", "Verteidigerin": "laura_ruhig"}  # Lexi = Carla

SEGMENTE = [
    # --- A Malerbetrieb -------------------------------------------------------------------------------------------------
    ("[fall]Herr und Frau Hasselbach führen zusammen einen Malerbetrieb. [buero]Sie macht die Buchhaltung. "
     "[vorwurf]Gegen ihn wird wegen Betrugs ermittelt: Er soll Kunden Arbeiten berechnet haben, die nie gemacht wurden.", 0.5),
    # --- B Polizei ------------------------------------------------------------------------------------------------------
    ("[pol]Ein Polizeibeamter vernimmt Frau Hasselbach als Zeugin und belehrt sie.", 0.2),
    ("[p1]Gegen Ihren Ehemann müssen Sie nicht aussagen.", 0.35, "Polizeibeamter"),
    ("[aus1]Trotzdem belastet sie ihn schwer.", 0.2),
    ("[w0]Die falschen Rechnungen hat er selbst geschrieben.", 0.5, "Hasselbach"),
    # --- C Hauptverhandlung ---------------------------------------------------------------------------------------------
    ("[hv]Monate später, in der Hauptverhandlung, belehrt sie der Vorsitzende erneut.", 0.2),
    ("[r1]Als Ehefrau des Angeklagten dürfen Sie das Zeugnis verweigern.", 0.3, "Vorsitzender"),
    ("[w1]Gegen meinen Mann sage ich nicht aus.", 0.4, "Hasselbach"),
    ("[verh]Da hört das Gericht den Polizeibeamten als Zeugen über ihre frühere Aussage.", 0.2),
    ("[p2]Sie sagte, die falschen Rechnungen habe er selbst geschrieben.", 0.4, "Polizeibeamter"),
    ("[urteil]Herr Hasselbach wird verurteilt. [rev]Seine Verteidigerin legt Revision ein.", 0.5),
    # --- D Fragen -------------------------------------------------------------------------------------------------------
    ("[fragen]Durfte der Polizeibeamte über die Aussage berichten? [frage2]Was wäre bei einem Richter anders? "
     "[frage3]Und wie rügt man das in der Revision?", 0.6),
    # --- E Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- F § 252 Wortlaut ------------------------------------------------------------------------------------------------
    ("[a252]Als Ehefrau darf sie nach Paragraf zweiundfünfzig das Zeugnis verweigern. [a252b]Für ihre frühere Aussage "
     "gilt Paragraf zweihundertzweiundfünfzig: [wl]Die Aussage eines vor der Hauptverhandlung vernommenen Zeugen, der erst "
     "in der Hauptverhandlung von seinem Recht, das Zeugnis zu verweigern, Gebrauch macht, darf nicht verlesen werden. "
     "[wort]Vom Polizeibeamten als Zeugen steht dort nichts. [verw]Die Grundlagen zu Paragraf zweiundfünfzig und zu den "
     "Beweisverwertungsverboten zeigen unsere Folgen dazu.", P),
    # --- G Streit: Verhörsperson ------------------------------------------------------------------------------------------
    ("[rspr]Die Rechtsprechung liest Paragraf zweihundertzweiundfünfzig weiter: als Verwertungsverbot. [rspr2]Die frühere "
     "Aussage darf grundsätzlich auch nicht auf anderem Weg eingeführt werden, [verhb]also auch nicht durch die "
     "Verhörsperson, etwa den Polizeibeamten. [zweck]Der Grund: Die Zeugin soll bis zur Hauptverhandlung frei entscheiden, "
     "ob ihre frühere, vielleicht voreilige Aussage verwertet wird.", P),
    ("[ga1]Eine Gegenansicht hält sich an den Wortlaut: Verboten sei nur das Verlesen, jede Vernehmungsperson, die "
     "ordnungsgemäß belehrt hat, dürfe aussagen. [ga2]Andere gehen weiter und sperren alles, sogar den Richter. "
     "[gsst]Der Große Senat musste die Frage zur Polizei nicht entscheiden und hat den Gesetzgeber aufgerufen. "
     "[praxis]Der Bundesgerichtshof hält seitdem an der Sperre für die Verhörsperson fest.", PS),
    # --- H Ausnahme Richter ----------------------------------------------------------------------------------------------
    ("[richter]Die wichtigste Ausnahme: Hat ein Richter die Zeugin vorher über ihr Zeugnisverweigerungsrecht belehrt, darf er "
     "als Zeuge über ihre Aussage gehört werden. [qual]Eine weitergehende Belehrung über die spätere Verwertbarkeit ist "
     "nicht nötig, so der Große Senat. [grund]Begründet wird das mit dem höheren Gewicht richterlicher Vernehmungen. "
     "[vorhalt]Beweismittel ist die Erinnerung des Richters; sein Protokoll darf ihm nur vorgehalten, nicht verlesen "
     "werden.", PS),
    # --- I Gestattung ----------------------------------------------------------------------------------------------------
    ("[gest]Zweite Ausnahme: die Gestattung. Die Zeugin verweigert das Zeugnis, erlaubt aber ausdrücklich, ihre frühere "
     "Aussage zu verwerten. [gest2]Dann darf auch der Polizeibeamte berichten. [gest3]Vorher ist sie qualifiziert zu "
     "belehren, über diese Möglichkeit und ihre Folgen; beides gehört ins Protokoll. [teil]Auf einzelne Vernehmungen "
     "beschränken kann sie die Erlaubnis nicht: Dann bleibt alles gesperrt, außer der Aussage vor dem Richter nach "
     "Belehrung.", PS),
    # --- J Außerhalb einer Vernehmung ------------------------------------------------------------------------------------
    ("[spont]Nicht gesperrt sind Äußerungen außerhalb einer Vernehmung, etwa eine echte Spontanäußerung. "
     "[spont2]Hätte Frau Hasselbach einer Freundin von den Rechnungen erzählt, dürfte die Freundin darüber aussagen.", PS),
    # --- K Lösung als Revisionsrüge --------------------------------------------------------------------------------------
    ("[l1]Zurück zum Fall. [l1a]Frau Hasselbach ist die Ehefrau des Angeklagten und hat erst in der Hauptverhandlung das "
     "Zeugnis verweigert. [l1b]Ihre Aussage stammt aus einer polizeilichen Vernehmung, und die Verwertung hat sie nicht "
     "gestattet. [l1c]Der Polizeibeamte durfte also nicht über ihre Aussage gehört werden.", P),
    ("[v1]Ich rüge die Verletzung von Paragraf zweihundertzweiundfünfzig.", 0.35, "Verteidigerin"),
    ("[l2]Das ist eine Verfahrensrüge. [l2a]Paragraf dreihundertvierundvierzig verlangt dafür, [l2b]dass die den Mangel enthaltenden Tatsachen "
     "angegeben werden. [l2c]Also etwa: die Ehe, die polizeiliche Aussage, die Zeugnisverweigerung in der "
     "Hauptverhandlung, die Vernehmung des Polizeibeamten und dass das Urteil auf seiner Aussage aufbaut. [l2d]Dass keine Gestattung vorlag, "
     "muss die Revision nicht eigens vortragen. [l2e]Und anders als beim Belehrungsfehler des Beschuldigten braucht es "
     "keinen Widerspruch in der Hauptverhandlung. [l2f]Weil das Urteil auf der Aussage beruhen kann, hat die Rüge Erfolg. "
     "[verw072]Mehr zum Aufbau in unserer Folge zur Verfahrensrüge.", PS),
    # --- L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüf in vier Schritten. [s1]Erstens: Hat die Zeugin ein Recht nach Paragraf zweiundfünfzig, und "
     "schweigt sie erst in der Hauptverhandlung? [s2]Zweitens: Wie soll die frühere Aussage in den Prozess, durch "
     "Verlesen oder durch die Verhörsperson? [s3]Drittens: Greift eine Ausnahme, also belehrter Richter, Gestattung oder "
     "eine Äußerung außerhalb einer Vernehmung? [s4]Viertens, in der Revision: Verfahrensrüge mit allen Tatsachen und "
     "das Beruhen.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Paragraf zweihundertzweiundfünfzig verbietet dem Wortlaut nach nur das Verlesen. [mz]Nach der "
     "Rechtsprechung sperrt er auch die Verhörsperson. Berichten darf nur der Richter, der belehrt hat, es sei denn, "
     "die Zeugin gestattet die Verwertung.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = "".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
