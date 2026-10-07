"""Folge 231 · Erlaubnistatbestandsirrtum (ETBI): Alle Schuldtheorien erklärt (Fr · Klausurpraxis · StGB AT · Streitstand).
Fiktiver Fall nach dem Plan-Hook: Herbstabend im Stadtpark, es ist dunkel. Bärbel (Joggerin, Mitte 40) verliert beim Laufen
unbemerkt ihr Handy. Helge (Spaziergänger, um 65) hebt es auf, läuft ihr hinterher und ruft „Hallo! Warten Sie!“. Unter einer
Laterne hält er das Handy hoch, es glänzt. Bärbel hält es für ein Messer, ruft „Bleiben Sie weg!“ und sprüht Pfefferspray.
Helges Augen brennen. Prüfung: § 223 (§ 224 I Nr. 2: Pfefferspray als gefährliches Werkzeug, BGH 1 StR 112/17 Rn. 16) kurz;
Rechtswidrigkeit: § 32 Abs. 2 (Wortlautkarte) – kein Angriff, keine Notwehrlage (BGH 4 StR 36/22 Rn. 10) → rechtswidrig;
Irrtum: ETBI (BGH 4 StR 36/22 Rn. 11; 3 StR 450/10 Rn. 12), Abgrenzung Erlaubnisirrtum (§ 17) ein Satz; § 16 Abs. 1 Satz 1 und
§ 17 Satz 1 als Wortlautkarten; fünf Theorien je mit Ergebnis und Kritik, Teilnahme-Argument (§§ 26, 27 Wortlaut);
BGH: § 16 entsprechend, Vorsatz bzw. Vorsatzschuld (4 StR 36/22 Rn. 11; 2 StR 375/11 Rn. 32; 3 StR 199/15 Rn. 12);
Ergebnis: § 229 bei vermeidbarem Irrtum (2 StR 375/11 Rn. 36; 4 StR 558/99 Rn. 14), Gegenfall unvermeidbar; Klausurtipp
(Prüfungsstandort Schuld), Schema und Merksatz mit Lexi. Belege je Cue: ../RECHTSSTAND.md.
DARSTELLUNG: Pfefferspray nur als Symbol (Icon), keine Verletzung im Bild; Helge sympathisch (Finder), Bärbel verängstigt.
Stimmen (Pool william, sabrina, marc, laura_ruhig): Bärbel sabrina (Frau, mittel), Helge william (Mann, älter).
Erzählerin und Lexi: Carla ohne Rolle. Namen nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Bärbel": "sabrina", "Helge": "william"}

SEGMENTE = [
    # --- A Fall: abends im Stadtpark ---------------------------------------------------------------------------------------
    ("[fall]Ein Herbstabend im Stadtpark, es ist schon dunkel. [baerbel]Bärbel dreht ihre Joggingrunde, Musik im Ohr. "
     "[handy]Dabei rutscht ihr das Handy aus der Tasche, ohne dass sie es merkt. [helge]Helge, ein älterer Spaziergänger, "
     "hebt es auf und läuft ihr hinterher.", 0.2),
    ("[he1]Hallo! Warten Sie!", P, "Helge"),
    ("[dreht]Bärbel dreht sich um. Ein Mann rennt im Dunkeln auf sie zu. [glanz]Unter einer Laterne hebt er die Hand, "
     "darin glänzt etwas. [messer]Bärbel glaubt: ein Messer.", 0.2),
    ("[ba1]Bleiben Sie weg!", P, "Bärbel"),
    ("[spray]Sie zieht ihr Pfefferspray und sprüht es ihm ins Gesicht. [augen]Helges Augen brennen, ein Arzt muss sie "
     "später ausspülen.", 0.2),
    ("[he2]Ich wollte Ihnen doch nur Ihr Handy bringen!", P, "Helge"),
    ("[frage]Bärbel hat sich gegen einen Angriff gewehrt, den es nie gab. Ist sie wegen Körperverletzung strafbar? "
     "[frage2]Darüber streiten fünf Theorien.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Tatbestand kurz -------------------------------------------------------------------------------------------------
    ("[tb]Zuerst der Tatbestand: Das Spray in den Augen ist eine Körperverletzung nach Paragraf zweihundertdreiundzwanzig. "
     "[tb2]Pfefferspray sieht die Rechtsprechung als gefährliches Werkzeug an, also kommt auch Paragraf "
     "zweihundertvierundzwanzig in Betracht. [vors]Bärbel wollte ihn treffen: Sie handelte vorsätzlich.", P),
    # --- D Rechtswidrigkeit: § 32 Abs. 2 (Wortlautkarte), keine Notwehrlage ------------------------------------------------
    ("[rw]Ist sie durch Notwehr gerechtfertigt? [p32]Paragraf zweiunddreißig, Absatz zwei: Notwehr ist die Verteidigung, "
     "die erforderlich ist, um einen gegenwärtigen rechtswidrigen Angriff von sich oder einem anderen abzuwenden. "
     "[kein]Helge wollte aber nur das Handy zurückgeben. Einen Angriff gab es nicht. [rw_neg]Ohne Angriff keine "
     "Notwehrlage: Das Sprühen war rechtswidrig.", P),
    # --- E Irrtum: Erlaubnistatbestandsirrtum, Abgrenzung Erlaubnisirrtum ---------------------------------------------------
    ("[irrtum]Bärbel hat sich aber geirrt. [vorst]Sie stellte sich Umstände vor, die eine Notwehrlage begründen würden: "
     "einen Mann, der sie mit einem Messer angreift. [hypo]Wäre das wahr, wäre das Spray erforderlich und geboten, sie wäre "
     "gerechtfertigt. [etbi]Das ist ein Erlaubnistatbestandsirrtum, man spricht auch von Putativnotwehr. "
     "[eti]Anders der Erlaubnisirrtum: Wer wüsste, dass Helge nur das Handy bringt, und trotzdem glaubte, man dürfe jeden "
     "besprühen, der nachts auf einen zuläuft, irrt über das Recht. Das ist ein Fall von Paragraf siebzehn.", P),
    # --- F Problem: zwischen § 16 und § 17 (Wortlautkarten) ------------------------------------------------------------------
    ("[gesetz]Den Erlaubnistatbestandsirrtum regelt das Gesetz nicht ausdrücklich. [p16]Paragraf sechzehn, Absatz eins: "
     "Wer bei Begehung der Tat einen Umstand nicht kennt, der zum gesetzlichen Tatbestand gehört, handelt nicht vorsätzlich. "
     "[p17]Und Paragraf siebzehn: Fehlt dem Täter bei Begehung der Tat die Einsicht, Unrecht zu tun, so handelt er ohne "
     "Schuld, wenn er diesen Irrtum nicht vermeiden konnte. [dazw]Bärbel irrt über Tatsachen, wie bei Paragraf sechzehn, "
     "aber ihr fehlt das Unrechtsbewusstsein, wie bei Paragraf siebzehn. Deshalb der Streit.", P),
    # --- G Die fünf Theorien -----------------------------------------------------------------------------------------------
    ("[t1]Erstens die Vorsatztheorie: Zum Vorsatz gehört auch das Bewusstsein, Unrecht zu tun. [t1e]Das fehlte Bärbel, "
     "also kein Vorsatz. [t1k]Kritik: Paragraf siebzehn macht das fehlende Unrechtsbewusstsein zur Frage der Schuld. "
     "Mit dem Gesetz ist diese Theorie nicht vereinbar.", P),
    ("[t2]Zweitens die strenge Schuldtheorie: Jeder Irrtum über die Rechtswidrigkeit ist ein Verbotsirrtum nach Paragraf "
     "siebzehn. [t2e]Bärbel handelte dann vorsätzlich. Ohne Schuld ist sie nur, wenn sie den Irrtum nicht vermeiden "
     "konnte, sonst kann die Strafe nur gemildert werden. [t2k]Kritik: Wer sich nur über Tatsachen irrt, wird behandelt "
     "wie jemand, der sich über das Recht hinwegsetzt.", P),
    ("[t3]Drittens die Lehre von den negativen Tatbestandsmerkmalen: Rechtfertigungsgründe gehören schon zum Tatbestand, "
     "als Merkmale, die fehlen müssen. [t3e]Dann gilt Paragraf sechzehn direkt, Bärbels Vorsatz entfällt. "
     "[t3k]Kritik: Sie verwischt den Unterschied zwischen Tatbestand und Rechtswidrigkeit, den das Gesetz macht.", P),
    ("[t4]Viertens die eingeschränkte Schuldtheorie: Der Irrtum gleicht einem Tatbestandsirrtum, also gilt Paragraf "
     "sechzehn entsprechend. [t4e]Der Vorsatz entfällt. [t4k]Kritik: Dann fehlt eine vorsätzliche rechtswidrige Haupttat. "
     "[teiln]Anstiftung und Beihilfe setzen aber genau diese Tat voraus. Ein eingeweihter Helfer bliebe als Teilnehmer straflos.", P),
    ("[t5]Fünftens die rechtsfolgenverweisende eingeschränkte Schuldtheorie: [t5e]Der Vorsatz bleibt, es entfällt nur die "
     "Vorsatzschuld. Bärbel wird wie bei Paragraf sechzehn behandelt, also höchstens wegen Fahrlässigkeit bestraft. "
     "[t5p]Ihre Tat bleibt aber vorsätzlich und rechtswidrig, ein Helfer kann als Teilnehmer bestraft werden. "
     "[t5k]Kritik: Der doppelte Vorsatz, einmal im Tatbestand und einmal in der Schuld, wirkt konstruiert. "
     "[hm]Im Schrifttum gilt sie heute als herrschende Meinung.", P),
    ("[bgh]Der Bundesgerichtshof wendet Paragraf sechzehn entsprechend an. [bgh2]Mal schreibt er, der Vorsatz entfalle, "
     "mal, die Vorsatzschuld. Im Ergebnis gibt es keine Strafe wegen der Vorsatztat.", PS),
    # --- H Ergebnis: § 229? -------------------------------------------------------------------------------------------------
    ("[erg]Bärbel ist also nicht wegen vorsätzlicher Körperverletzung strafbar. [fahr]Bleibt die fahrlässige "
     "Körperverletzung nach Paragraf zweihundertneunundzwanzig. Fahrlässig handelt sie nur, wenn sie den Irrtum "
     "hätte vermeiden können. [lat]Helge hatte gerufen, und unter der Laterne war das Handy in seiner Hand zu erkennen. "
     "[fahr2]Ein kurzer Blick hätte genügt: Der Irrtum war vermeidbar, Bärbel ist wegen fahrlässiger Körperverletzung "
     "strafbar. [gegen]Wäre der Irrtum unvermeidbar gewesen, bliebe sie straflos.", PS),
    # --- I Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Mit der herrschenden Meinung prüfst du den Erlaubnistatbestandsirrtum in der Schuld, als "
     "Frage der Vorsatzschuld. [k1]Prüfe zuerst, ob der Täter gerechtfertigt wäre, wenn seine Vorstellung stimmte. "
     "[k2]Den Streit entscheidest du nur, wenn die Ergebnisse auseinandergehen: [k3]gegen die strenge Schuldtheorie, wenn "
     "der Irrtum vermeidbar war, [k4]zwischen den eingeschränkten Theorien nur, wenn es um Teilnehmer geht.", P),
    # --- J Gutachtenaufbau (Lexi), progressiv -------------------------------------------------------------------------------
    ("[sch]So baust du das Gutachten auf: [s1]Erstens der Tatbestand der gefährlichen Körperverletzung. [s2]Zweitens die "
     "Rechtswidrigkeit: keine Notwehrlage. [s3]Drittens die Schuld: Erlaubnistatbestandsirrtum, die Vorsatzschuld entfällt. "
     "[s4]Danach prüfst du die fahrlässige Körperverletzung.", PS),
    # --- K Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer sich irrig eine Notwehrlage vorstellt, wird nicht wegen der Vorsatztat bestraft. [m2]Höchstens "
     "wegen Fahrlässigkeit, wenn er den Irrtum hätte vermeiden können.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
