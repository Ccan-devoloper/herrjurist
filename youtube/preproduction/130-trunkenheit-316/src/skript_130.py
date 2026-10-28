"""Folge 130 · Trunkenheit im Verkehr § 316: 0,3 – 0,5 – 1,1 – 1,6 Promille (Mo · Der Fall · StGB BT, Format Schema).
Beispielfall nach dem Plan-Hook („Ein Autofahrer wird mit 0,8 Promille kontrolliert, fährt aber schnurgerade – ein anderer
hat 1,2 Promille“): Verkehrskontrolle am Ortsausgang, eine Polizistin hält nacheinander Heinrich (0,8 ‰ BAK, fährt
schnurgerade, keine Ausfallerscheinungen) und Siegfried (1,2 ‰ BAK, fährt ebenfalls unauffällig, hält sich für fahrtüchtig)
an. Niemand wird gefährdet oder verletzt. Kein Alkoholkonsum im Bild (nur ein neutrales Glas-Icon bei „alkoholischer Getränke“).
Prüfung: Wortlautkarte § 316 Abs. 1 StGB → 1. Führen eines Fahrzeugs im Verkehr → 2. absolute Fahruntüchtigkeit ab 1,1 ‰
(BGHSt 37, 89 nach BGH 4 StR 366/20 Rn. 8, 4 StR 439/22 Rn. 4, 6; Grundwert 1,0 + Sicherheitszuschlag 0,1 nach BGHSt 45, 140
= 4 StR 106/99 Rn. 12, 15 f.), unwiderleglich; Radfahrer 1,6 ‰ nach OLG-Rechtsprechung (OLG Karlsruhe 2 Rv 35 Ss 175/20;
BGH 4 StR 386/16 Rn. 2) → 3. relative Fahruntüchtigkeit (4 StR 366/20 Rn. 9; 4 StR 526/24 Rn. 5, 7), Untergrenze etwa
0,3 ‰ (OLG Hamm I-20 U 74/10 Rn. 28; kein BGH-Volltext mit Rn. gefunden, offengelegt) → 4. § 24a Abs. 1 StVG
(Wortlautkarte), § 25 Abs. 1 S. 2 StVG, § 24a Abs. 1a (THC, ein Satz), § 24c StVG (ein Satz) → 5. Vorsatz/Fahrlässigkeit
(4 StR 401/14 Rn. 7) → 6. § 315c Abs. 1 Nr. 1 a (konkrete Gefahr, 4 StR 391/24 Rn. 4) → Ergebnis (§ 21 OWiG, § 69 Abs. 2
Nr. 2 StGB) → Klausurtipp → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Heinrich, Siegfried (nie im Genitiv).
Die Polizistin bleibt ohne Namen (Funktionsrolle).
Stimmen (nur aus dem Pool william, sabrina, marc, laura_ruhig): Heinrich marc; Siegfried william; Polizistin sabrina.
Lexi = Erzählerin Carla. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue; jede Marke genau einmal. Zahlen, Promillewerte und Paragrafen im Sprechtext als Wörter; „Straßenverkehrsgesetz“
und „Ordnungswidrigkeitengesetz“ ausgeschrieben (synth_el kennt die Abkürzungen StVG/OWiG nicht)."""

P, PS = 0.3, 0.5

STIMMEN = {"Heinrich": "marc", "Siegfried": "william", "Polizistin": "sabrina"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Kontrolle Heinrich ---------------------------------------------------------------------------------------
    ("[fall]Ein Freitagnachmittag am Ortsausgang. [kontr]Die Polizei kontrolliert den Verkehr. [hein]Heinrich fährt heran, "
     "schnurgerade und ohne jeden Fahrfehler.", 0.3),
    ("[p1]Allgemeine Verkehrskontrolle. Bitte einmal kräftig pusten.", 0.3, "Polizistin"),
    ("[test]Der Atemtest schlägt an. [blut1]Die Blutprobe ergibt später null Komma acht Promille.", 0.3),
    ("[h1]Aber ich bin doch ganz normal gefahren!", 0.3, "Heinrich"),
    # --- A2 Fall: Kontrolle Siegfried --------------------------------------------------------------------------------------
    ("[sieg]Kurz darauf hält die Polizistin Siegfried an. Auch er fährt völlig unauffällig. [blut2]Seine Blutprobe ergibt "
     "eins Komma zwei Promille.", 0.3),
    ("[s1]Ich fühle mich topfit.", 0.3, "Siegfried"),
    ("[niemand]Gefährdet oder verletzt wurde niemand. [frage]Haben sich beide strafbar gemacht? [frage2]Oder ist einer "
     "von ihnen nur ordnungswidrig gefahren?", 0.5),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlautkarte § 316 Abs. 1, Führen im Verkehr --------------------------------------------------------------------
    ("[p316]Paragraf dreihundertsechzehn Absatz eins: Wer im Verkehr ein Fahrzeug führt, obwohl er infolge des Genusses "
     "alkoholischer Getränke [p316b]nicht in der Lage ist, das Fahrzeug sicher zu führen, wird bestraft. [fuehr]Beide haben "
     "ihr Auto auf einer öffentlichen Straße geführt. [kern]Entscheidend ist die Fahruntüchtigkeit infolge Alkohols. "
     "[zahl]Eine Promillezahl steht nicht im Gesetz. Die Grenzwerte hat die Rechtsprechung entwickelt, als Beweisregeln.", PS),
    # --- D absolute Fahruntüchtigkeit: 1,1 ‰, Radfahrer 1,6 ‰ ----------------------------------------------------------------
    ("[abs]Erstens die absolute Fahruntüchtigkeit. [abs11]Ab eins Komma eins Promille Blutalkohol ist jeder Kraftfahrer "
     "fahruntüchtig. [bgh]So entschied der Bundesgerichtshof neunzehnhundertneunzig: [zuschl]ein Grundwert von eins Komma "
     "null plus null Komma eins Sicherheitszuschlag. [unwid]Dieser Wert gilt unwiderleglich. Ein Gegenbeweis ist "
     "ausgeschlossen, auch durch schnurgerades Fahren. [sieg_abs]Siegfried hat eins Komma zwei Promille. Dass er sich fit "
     "fühlt, hilft ihm nicht.", PS),
    ("[rad]Für Radfahrer liegt die Grenze höher. [rad16]Die Oberlandesgerichte nehmen überwiegend eins Komma sechs Promille an; "
     "[radbgh]der Bundesgerichtshof sah bisher keinen Anlass, das zu überprüfen.", PS),
    # --- E relative Fahruntüchtigkeit ab etwa 0,3 ‰ -------------------------------------------------------------------------
    ("[rel]Zweitens die relative Fahruntüchtigkeit. [rel03]Auch unter eins Komma eins, nach der Rechtsprechung etwa ab null "
     "Komma drei Promille, kann ein Fahrer fahruntüchtig sein. [aus]Dann müssen aber alkoholbedingte Ausfallerscheinungen "
     "hinzukommen, etwa Schlangenlinien oder ein typischer Fahrfehler. [kaus]Ein Fehler, der auch nüchtern passiert wäre, "
     "genügt nicht. [hein_rel]Heinrich fuhr schnurgerade und ohne Auffälligkeiten. [hein_neg]Für ihn scheidet Paragraf "
     "dreihundertsechzehn deshalb aus.", PS),
    # --- F § 24a StVG: 0,5 ‰ ------------------------------------------------------------------------------------------------
    ("[owi]Folgenlos bleibt die Fahrt für Heinrich trotzdem nicht. [p24a]Paragraf vierundzwanzig a Absatz eins "
     "Straßenverkehrsgesetz: Ordnungswidrig handelt, wer ein Kraftfahrzeug führt, obwohl er [atem]null Komma zwei fünf "
     "Milligramm pro Liter oder mehr Alkohol in der Atemluft [p24b]oder null Komma fünf Promille oder mehr Alkohol im Blut hat. "
     "[ohne]Ausfallerscheinungen braucht es hier nicht. [fv]Es drohen eine Geldbuße und in der Regel ein Fahrverbot. "
     "[hein_owi]Heinrich mit null Komma acht Promille handelt also ordnungswidrig.", PS),
    ("[thc]Für Cannabis gibt es in Absatz eins a einen eigenen Grenzwert. [anf]Und wer in der Probezeit oder unter "
     "einundzwanzig ist, darf überhaupt kein Kraftfahrzeug unter Alkoholwirkung führen, Paragraf vierundzwanzig c.", PS),
    # --- G Vorsatz, § 315c ---------------------------------------------------------------------------------------------------
    ("[vors]Zurück zu Siegfried: Vorsatz oder Fahrlässigkeit? [vors2]Vorsätzlich handelt, wer seine Fahruntüchtigkeit "
     "kennt oder mit ihr rechnet und sich damit abfindet. [grenz]Den Grenzwert selbst muss er nicht kennen. [fahrl]Siegfried "
     "hält sich für fahrtüchtig, hätte es aber erkennen können. Das ist fahrlässig, strafbar nach Absatz zwei.", PS),
    ("[p315c]Und Paragraf dreihundertfünfzehn c? Er verlangt zusätzlich eine konkrete Gefahr für einen anderen Menschen "
     "oder für fremde Sachen von bedeutendem Wert, [beinahe]also einen Beinahe-Unfall. [keine]Hier wurde niemand "
     "gefährdet. [subs]Paragraf dreihundertsechzehn bleibt deshalb anwendbar; bei einer konkreten Gefahr träte er "
     "zurück.", PS),
    # --- H Ergebnis ----------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Siegfried ist strafbar wegen fahrlässiger Trunkenheit im Verkehr. [owig]Seine Ordnungswidrigkeit "
     "tritt zurück, Paragraf einundzwanzig Ordnungswidrigkeitengesetz. [fe]In der Regel wird ihm die Fahrerlaubnis "
     "entzogen. [erg2]Heinrich handelt nur ordnungswidrig.", PS),
    # --- I Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Der Grenzwert ist kein Tatbestandsmerkmal, sondern eine Beweisregel. [tipp2]Prüfe unter eins "
     "Komma eins Promille immer, ob Ausfallerscheinungen festgestellt sind und ob sie gerade auf dem Alkohol beruhen.", PS),
    # --- J Prüfschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Prüfschema zu Paragraf dreihundertsechzehn. [k1]Römisch eins, Tatbestand. Objektiv: Führen eines "
     "Fahrzeugs im Verkehr [k1b]und Fahruntüchtigkeit infolge Alkohols: [k1c]absolut ab eins Komma eins, bei Radfahrern "
     "eins Komma sechs, [k1d]relativ mit Ausfallerscheinungen. [k1e]Subjektiv Vorsatz, sonst Fahrlässigkeit nach Absatz "
     "zwei. [k2]Römisch zwei und drei: Rechtswidrigkeit und Schuld. [k3]Dann die Konkurrenzen: Vorrang von Paragraf "
     "dreihundertfünfzehn c. [k4]Ohne Straftat bleibt ab null Komma fünf Promille Paragraf vierundzwanzig a.", PS),
    # --- K Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Ab eins Komma eins Promille hilft auch schnurgerades Fahren nicht. [m2]Darunter braucht die Straftat "
     "Ausfallerscheinungen, die Ordnungswidrigkeit nur null Komma fünf Promille.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
