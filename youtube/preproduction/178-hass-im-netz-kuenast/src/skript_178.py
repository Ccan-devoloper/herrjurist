"""Folge 178 · Hass im Netz: Wann schützt die Meinungsfreiheit? Fall Künast (Mo · Der Fall · Klassiker-Fall;
§§ 185, 188, 192a, 193 StGB; Art. 5 I, II GG). Echter Fall sachlich nach dem Volltext: BVerfG (2. Kammer des Ersten
Senats), Beschl. v. 19.12.2021 – 1 BvR 1073/20 (Künast); Maßstäbe aus BVerfG (2. Kammer des Ersten Senats), Beschl. v.
19.5.2020 – 1 BvR 2397/19; zitiert nur mit Rn. Belege je Cue: ../RECHTSSTAND.md.
HÖCHSTE SENSIBILITÄT: keine Beschimpfung wörtlich, nicht angedeutet, nicht verpixelt – nur die Text-Pille
„derbe sexistische Beschimpfungen“; keine Figur und kein Porträt der Politikerin oder anderer realer Personen;
parteipolitisch neutral (keine Parteinamen, -farben, -logos); „Künast“ nur als Fallname; keine Plattformnamen/-logos.
Fiktiver Rahmen: Sprechstunde bei Professor Ruhland (Stimme helmut) mit dem Studenten Mattes (Stimme niklas); der Hook
(Stadträtin) ist erfunden und wird nur als Text gezeigt.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke
genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Mattes": "niklas", "Ruhland": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Einstieg in der Sprechstunde (fiktiver Hook) ---------------------------------------------------------------
    ("[fall]Sprechstunde bei Professor Ruhland. [hook]Sein Student zeigt ihm einen Bericht: Unter einem Beitrag über eine "
     "Stadträtin stehen derbe sexistische Beschimpfungen. [hook2]Sie verlangt von der Plattform Auskunft, wer sie "
     "geschrieben hat.", P),
    ("[ma1]Muss eine Politikerin so etwas nicht aushalten?", P, "Mattes"),
    ("[ru1]So ähnlich argumentierte das Kammergericht im Fall Künast. Das Bundesverfassungsgericht hob die Beschlüsse auf.", P,
     "Ruhland"),
    # --- B Der echte Fall (1 BvR 1073/20, Rn. 1–16, Tenor) ---------------------------------------------------------------
    ("[echt]Der echte Fall. [beitrag]Auf einer Social-Media-Plattform erscheint zweitausendneunzehn ein Beitrag mit dem Bild "
     "einer Politikerin und einem Zitat, das so nicht von ihr stammt. [komm]Darunter schreiben Nutzer "
     "Kommentare, viele davon derbe sexistische Beschimpfungen. [antrag]Die Politikerin beantragt beim Landgericht Berlin, "
     "der Plattform die Auskunft über die Daten der Verfasser zu gestatten. [vor]Das setzt voraus, dass die Kommentare "
     "etwa eine Beleidigung darstellen und nicht gerechtfertigt sind.", P),
    ("[lg]Das Landgericht hält zunächst alles für zulässige Meinung, weil die Kommentare einen Sachbezug hätten. "
     "[kg]Später erlauben Landgericht und Kammergericht die Auskunft für zwölf von zweiundzwanzig Kommentaren. "
     "[zehn]Für zehn bleibt es beim Nein: keine Schmähkritik, [hinnehmen]und teils heißt es, als Politikerin müsse sie "
     "das hinnehmen.", P),
    ("[bverfg]Das Bundesverfassungsgericht entscheidet am neunzehnten Dezember zweitausendeinundzwanzig: Die Beschlüsse "
     "verletzen ihr Persönlichkeitsrecht. [auf]Das Kammergericht muss neu entscheiden.", P),
    ("[frage]Wann schützt die Meinungsfreiheit solche Kommentare?", PS),
    # --- C Sachverhalt -----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D 1. Grundrechte, Schranke, § 193 (2397/19 Rn. 12, 14; 1073/20 Rn. 20, 26) ------------------------------------
    ("[a5]Erstens, die Grundrechte. Artikel fünf Absatz eins: Jeder hat das Recht, seine Meinung in Wort, Schrift und Bild "
     "frei zu äußern und zu verbreiten. [wert]Das gilt auch für polemische oder verletzende Werturteile. [a52]Die Schranken "
     "stehen in Absatz zwei, etwa die allgemeinen Gesetze. [p185]Dazu gehört Paragraf hundertfünfundachtzig StGB, "
     "siehe die Folgen zum Lüth-Urteil und zur Beleidigung. [apr]Gegenüber steht das Persönlichkeitsrecht "
     "aus Artikel zwei mit Artikel eins.", P),
    ("[p193]Ins Strafrecht kommt die Meinungsfreiheit vor allem über Paragraf hundertdreiundneunzig: die Wahrnehmung "
     "berechtigter Interessen.", P),
    # --- E 2. Kern: Abwägung als Regel, enge Ausnahmen (2397/19 Rn. 15–27) -------------------------------------------
    ("[kern]Zweitens, der Kern. [regel]Für eine Beleidigung muss das Gericht im Normalfall Ehre und Meinungsfreiheit "
     "abwägen. [ausn]Nur ausnahmsweise entfällt das: bei einem Angriff auf die Menschenwürde, bei einer Formalbeleidigung "
     "und bei einer Schmähung. [eng]Diese Ausnahmen sind eng.", P),
    ("[schmaeh]Eine Schmähung hat keinen irgendwie nachvollziehbaren Bezug mehr zu einer sachlichen Auseinandersetzung; es "
     "geht nur um das grundlose Verächtlichmachen der Person. [steig]Auch ausfällige Kritik ist nicht schon deshalb eine "
     "Schmähung. [formal]Eine Formalbeleidigung sind besonders krasse Schimpfwörter, mit Vorbedacht verwendet. Hier zählt "
     "die Form, nicht der Sachbezug. [mw]Die Menschenwürde ist verletzt, wenn eine Äußerung der Person den Kern ihrer "
     "Persönlichkeit abspricht.", P),
    ("[sonst]Liegt keine Ausnahme vor, spricht das noch nicht für die Meinungsfreiheit. Dann wird umfassend abgewogen, "
     "[offen]mit offenem Ergebnis.", P),
    # --- F 3. Der Fehler der Fachgerichte (1073/20 Rn. 40–48) -----------------------------------------------------------
    ("[fehler]Drittens, der Fehler im Fall Künast. [gleich]Das Kammergericht nahm an, eine Beleidigung liege nur vor, wenn "
     "die Äußerung bloß als Herabsetzung und Schmähung erscheine. Es setzte die Beleidigung also mit der Schmähkritik gleich. [sach]Der "
     "Sachbezug grenzt aber vor allem die Schmähung ab; zulässig macht er eine Äußerung nicht. [ausfall]Die Abwägung fiel "
     "praktisch vollständig aus. [politik]Und der Satz, als Politikerin müsse sie das hinnehmen, ersetzt keine Abwägung.", P),
    # --- G 4. Kriterien der Abwägung (1073/20 Rn. 31–37; 2397/19 Rn. 32) -----------------------------------------------
    ("[krit]Viertens, die Kriterien. [beitr]Die Meinungsfreiheit wiegt umso schwerer, je mehr eine Äußerung zur "
     "öffentlichen Meinungsbildung beiträgt, und umso leichter, je mehr sie nur Stimmung gegen eine Person macht. "
     "[macht]Machtkritik ist besonders geschützt, die Grenzen der Kritik an Politikern sind weiter. [grenze]Aber nicht jede "
     "persönliche Beschimpfung ist erlaubt. [pos]Einem Bundesminister kann mehr zuzumuten sein als einem Lokalpolitiker. "
     "[schutz]Und ihr Schutz liegt auch im öffentlichen Interesse, damit sich Menschen politisch engagieren.", P),
    ("[form]Wer schreibt, muss bedachter formulieren, auch im Netz. [anlass]Erheblich ist der Anlass. "
     "[wirk]Und eine dauerhafte, für viele sichtbare Äußerung im Netz trifft schwerer als ein Satz im kleinen Kreis.", P),
    # --- H 5. § 188, § 192a StGB (Wortlaut; BT-Drs. 19/17741, 19/20163) ----------------------------------------------
    ("[p188]Fünftens: Paragraf hundertachtundachtzig verschärft die Strafe für eine öffentliche "
     "Beleidigung einer Person des politischen Lebens, wenn das Motiv mit ihrer Stellung zusammenhängt und die Tat ihr "
     "Wirken erheblich erschweren kann. [kommunal]Das reicht bis hin zur kommunalen Ebene. [neu]Beides gilt erst seit dem "
     "Gesetz gegen Hasskriminalität; vorher erfasste die Vorschrift nur üble Nachrede und Verleumdung. [p192a]Neu ist auch "
     "die verhetzende Beleidigung, Paragraf hundertzweiundneunzig a, etwa wegen Herkunft oder Behinderung; das Geschlecht "
     "nennt sie nicht.", P),
    # --- I 6. Lösung des Hooks ------------------------------------------------------------------------------------------
    ("[loes]Und die Stadträtin? [kontext]Schmähkritik nimmt das Gericht nicht vorschnell an. [abw]In der Abwägung zählt: "
     "Die Beschimpfungen tragen nichts zur Sache bei, zielen sexistisch auf ihre Person und stehen für alle sichtbar im "
     "Netz. [lokal]Einer Stadträtin kann weniger zuzumuten sein als einer Ministerin. [tend]Viel spricht deshalb für eine "
     "Beleidigung und damit für die Auskunft.", PS),
    # --- J Zurück in der Sprechstunde -----------------------------------------------------------------------------------
    ("[ma2]Also muss sie das nicht einfach aushalten?", P, "Mattes"),
    ("[ru2]Nicht ohne Abwägung. Und reine Herabsetzung wiegt dabei wenig.", PS, "Ruhland"),
    # --- K Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Ermittle zuerst den Sinn der Äußerung, Tatsache oder Werturteil. [tipp2]Schmähkritik nimmst du "
     "nur ausnahmsweise und mit Begründung an. [tipp3]Sonst wägst du ab, bei Paragraf hundertdreiundneunzig. [tipp4]Schreib "
     "nie: Sachbezug vorhanden, also zulässig.", PS),
    # --- L Prüfschema -------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema. [k1]Römisch eins: Tatbestand. [k1a]Äußerung und ihr Sinn, Kundgabe der Missachtung, Vorsatz. "
     "[k1b]Gegen Politiker gegebenenfalls Paragraf hundertachtundachtzig. [k2]Römisch zwei: Rechtswidrigkeit. "
     "[k2a]Schmähung, Formalbeleidigung, Menschenwürde? Dann ohne Abwägung. [k2b]Sonst Abwägung bei Paragraf "
     "hundertdreiundneunzig. [k3]Römisch drei: Schuld. [k4]Römisch vier: Strafantrag.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Auch harte Kritik an Politikern ist geschützt, aber nicht jede Beschimpfung. [m2]Die Schmähkritik ist "
     "die enge Ausnahme; der Normalfall ist die Abwägung im Einzelfall.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
