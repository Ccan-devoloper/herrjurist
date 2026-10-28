"""Folge 214 · Schießen wegen ein paar Äpfeln? Notwehr bei Bagatellen (Mo · Der Fall · StGB AT · Alltagsfall).
Fiktiver Fall: Samstagnacht im September klettern Jannes und Paulina (beide 16) auf die Obstwiese von Herrn Gehrke (68) und
pflücken Äpfel im Wert von etwa 20 € in einen Rucksack. Herr Gehrke droht, gibt einen Warnschuss ab und schießt den
Fliehenden mit Schrot auf die Beine; Jannes wird am Bein verletzt. Prüfung: §§ 223, 224 I Nr. 2 StGB kurz (Verweis Folge 042),
§ 32 StGB (Wortlautkarte Abs. 1, 2; Schema nur verwiesen auf Folge 033): Notwehrlage (+), Erforderlichkeit (+, vertretbar),
Gebotenheit (–) wegen unerträglichen Missverhältnisses (BGH 3 StR 450/10 Rn. 16; 2 StR 523/15 Rn. 21; 3 StR 199/15 Rn. 11),
Art. 2 Abs. 2 lit. a EMRK als Streitpunkt in einem Satz, § 33 StGB (Wortlautkarte) scheidet aus (Ärger), Klausurtipp,
Gutachtenaufbau und Merksatz mit Lexi.
DARSTELLUNG: keine Waffe im Bild, kein Schuss, keine Verletzten; Schuss und Verletzung nur erzählt (Pillen).
Stimmen: Herr Gehrke helmut (Mann, älter), Jannes niklas (Mann, jung), Paulina ela_froh (nur der fröhliche Satz im Hook).
Erzählerin und Lexi: Carla ohne Rolle. Belege je Cue: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Gehrke": "helmut", "Jannes": "niklas", "Paulina": "ela_froh"}

SEGMENTE = [
    # --- A Fall: Obstwiese bei Nacht -----------------------------------------------------------------------------------
    ("[fall]Samstagnacht im September, kurz vor Mitternacht. [wiese]Auf der Obstwiese von Herrn Gehrke, achtundsechzig, "
     "hängen die Äpfel reif an den Bäumen. [teens]Jannes und Paulina, beide sechzehn, klettern über den Zaun [pflueck]und "
     "pflücken einen Rucksack voll, Äpfel im Wert von etwa zwanzig Euro.", 0.2),
    ("[pa1]Die hier sind die besten im ganzen Dorf!", P, "Paulina"),
    ("[licht]Da geht im Haus das Licht an. [tuer]Wütend tritt Herr Gehrke mit seiner Schrotflinte vor die Tür.", 0.2),
    ("[ge1]Halt! Weg von meinen Bäumen, sonst schieße ich!", P, "Gehrke"),
    ("[ja1]Schnell, weg hier!", 0.2, "Jannes"),
    ("[flucht]Die beiden rennen mit dem Rucksack davon. [warn]Herr Gehrke gibt einen Warnschuss in die Luft ab. "
     "[weiter]Sie rennen weiter. [beine]Da zielt er auf ihre Beine und schießt. [treffer]Schrotkörner treffen Jannes am "
     "Bein; im Krankenhaus werden sie entfernt.", P),
    ("[polizei]Der Polizei sagt Herr Gehrke später:", 0.2),
    ("[ge2]Das waren meine Äpfel. Ich habe mich nur gewehrt.", P, "Gehrke"),
    ("[frage]Darf man wegen Äpfeln für zwanzig Euro auf Menschen schießen? [frage2]Hat Herr Gehrke sich strafbar gemacht?", PS),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Tatbestand kurz (§§ 223, 224 I Nr. 2; Verweis 042) -------------------------------------------------------------
    ("[tb]Zuerst der Tatbestand: Die Schrotkörner im Bein sind eine Körperverletzung nach Paragraf zweihundertdreiundzwanzig, "
     "[tb2]und weil er mit einer Waffe schoss, sogar eine gefährliche nach Paragraf zweihundertvierundzwanzig. [vors]Treffen "
     "wollte er, also handelte er vorsätzlich. [v042]Die Varianten zeigt unsere Folge zur gefährlichen Körperverletzung. "
     "[rw]Spannend wird die Rechtswidrigkeit: Ist Herr Gehrke durch Notwehr gerechtfertigt?", P),
    # --- D § 32 StGB, Wortlautkarte; Verweis 033 ---------------------------------------------------------------------------
    ("[p32]Paragraf zweiunddreißig, Absatz zwei: Notwehr ist die Verteidigung, die erforderlich ist, um einen gegenwärtigen "
     "rechtswidrigen Angriff von sich oder einem anderen abzuwenden. [abs1]Und Absatz eins: Wer eine Tat begeht, die durch "
     "Notwehr geboten ist, handelt nicht rechtswidrig. [v033]Das ganze Schema zeigt unsere Folge zur Notwehr; hier geht es "
     "um ihre Grenze.", P),
    # --- E 1. Notwehrlage (BGH 1 StR 126/21 Rn. 9) ---------------------------------------------------------------------------
    ("[lage]Erstens die Notwehrlage. [angr]Jannes und Paulina nehmen fremde Äpfel weg, ein Diebstahl, also ein Angriff auf "
     "das Eigentum von Herrn Gehrke. [sache]Auch Sachen darf man verteidigen. [gegenw]Gegenwärtig bleibt der Angriff, solange "
     "die beiden mit der Beute fliehen; [beute]so bejaht der Bundesgerichtshof die Notwehrlage, solange der Täter die Beute "
     "noch hat. [rechtsw]Rechtswidrig ist der Diebstahl ohnehin. [lage_ok]Die Notwehrlage liegt vor.", P),
    # --- F 2. a) Erforderlichkeit (BGH 1 StR 126/21 Rn. 14; 2 StR 523/15 Rn. 11; 3 StR 199/15 Rn. 9) ------------------------
    ("[erf]Zweitens die Notwehrhandlung, zuerst die Erforderlichkeit. [mild]Erforderlich ist das mildeste Mittel, das den "
     "Angriff sofort und endgültig beendet. [ruf]Gerufen und gedroht hatte Herr Gehrke schon, [warn2]auch der Warnschuss blieb "
     "ohne Wirkung. [pol2]Die Polizei wäre zu spät gekommen, und hinterherlaufen konnte er mit achtundsechzig nicht. "
     "[waffe]Bei einer lebensgefährlichen Waffe verlangt der Bundesgerichtshof in der Regel, den Einsatz erst anzudrohen "
     "oder sie weniger gefährlich einzusetzen, etwa auf die Beine zu zielen. [erf_ok]Genau das hat Herr Gehrke getan. "
     "Gut vertretbar: Der Schuss war erforderlich. [noch]Eine Abwägung von Äpfeln gegen Beine findet hier noch nicht statt.", P),
    # --- G 2. b) Gebotenheit (BGH 2 StR 523/15 Rn. 21; 1 StR 126/21 Rn. 18; 3 StR 450/10 Rn. 16; 3 StR 199/15 Rn. 11) --------
    ("[geb]Bleibt die Gebotenheit. [keine]Grundsätzlich verlangt Notwehr keine Abwägung der Rechtsgüter. [sozial]Aus "
     "sozialethischen Gründen kann sie aber eingeschränkt sein. [bgh]Nicht mehr geboten ist die Verteidigung laut "
     "Bundesgerichtshof, wenn die Rechtsgüter in einem unerträglichen Missverhältnis stehen, [bag]etwa wenn eine Abwehr, die "
     "Leib oder Leben des Angreifers gefährdet, einen evident bagatellhaften Angriff abwehren soll.", P),
    ("[hier]Genau so liegt es hier: [links]auf der einen Seite Äpfel für zwanzig Euro, [rechts]auf der anderen Schrot auf "
     "Menschen, das die Gesundheit und sogar das Leben gefährden kann. [nicht]Die Verteidigung ist nicht geboten. "
     "[hinnehm]Herr Gehrke hätte den Verlust hinnehmen oder sich auf weniger gefährliche Mittel beschränken müssen, etwa rufen und die "
     "Polizei verständigen.", P),
    ("[kind]Mit Kindern hat das nichts zu tun: Mit sechzehn sind Jannes und Paulina keine Kinder mehr, [kind2]die "
     "Einschränkung gegenüber erkennbar Schuldlosen greift nicht. Entscheidend ist allein das Missverhältnis. [emrk]Bei "
     "tödlicher Abwehr wird zusätzlich über Artikel zwei der Menschenrechtskonvention gestritten: Er lässt eine Tötung nur "
     "zu, um jemanden gegen rechtswidrige Gewalt zu verteidigen, nicht für Sachwerte. [emrk2]Ob das auch zwischen Privaten "
     "gilt, ist umstritten.", PS),
    # --- H Ergebnis, § 33 StGB (Wortlautkarte; BGH 3 StR 199/15 Rn. 18 f.) ----------------------------------------------------
    ("[erg]Herr Gehrke ist also nicht gerechtfertigt. [p33]Bleibt Paragraf dreiunddreißig: Überschreitet der Täter die "
     "Grenzen der Notwehr aus Verwirrung, Furcht oder Schrecken, so wird er nicht bestraft. [aerger]Herr Gehrke schoss aber "
     "aus Ärger, nicht aus Angst. [strafbar]Er hat sich wegen gefährlicher Körperverletzung strafbar gemacht. [dieb]Jannes "
     "und Paulina bleiben für ihren Diebstahl verantwortlich; das ist eine eigene Prüfung.", PS),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne Erforderlichkeit und Gebotenheit sauber. [t1]In der Erforderlichkeit fragst du nur nach dem "
     "mildesten gleich wirksamen Mittel, ohne Abwägung. [t2]Das Missverhältnis zwischen Beute und Abwehr gehört erst in die "
     "Gebotenheit. [t3]Geringer Beutewert und gefährliches Abwehrmittel im Sachverhalt sind dein Signal dafür.", P),
    # --- J Gutachtenaufbau (Lexi), progressiv ---------------------------------------------------------------------------------
    ("[sch]So baust du das Gutachten auf: [s1]Erstens der Tatbestand der gefährlichen Körperverletzung. [s2]Zweitens die "
     "Rechtswidrigkeit: Notwehrlage gegeben, Schuss erforderlich, [s2b]aber nicht geboten. [s3]Drittens die Schuld: kein "
     "Notwehrexzess.", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Notwehr kennt grundsätzlich keine Güterabwägung. [m2]Wer aber für eine Kleinigkeit Leib oder Leben eines "
     "Menschen gefährdet, handelt nicht geboten. [m3]Für ein paar Äpfel darf man nicht schießen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
