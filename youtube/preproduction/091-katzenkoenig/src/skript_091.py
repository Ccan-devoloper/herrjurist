"""Folge 091 · Katzenkönig-Fall: Mittelbare Täterschaft – Täter hinter dem Täter (Mo · Der Fall · StGB AT, Klassiker-Fall).
Der echte Fall vereinfacht erzählt, mit anderen Namen (BGH, Urt. v. 15.9.1988 – 4 StR 352/88, BGHSt 35, 347; Volltext mit
Seitenmarken der amtlichen Sammlung, Belege in ../RECHTSSTAND.md). Zurückhaltend: kein Messer, kein Angriff, keine
Verletzung im Bild; der „Katzenkönig“ nur als Krone in einer Gedankenblase; das Opfer wird nicht als Figur gezeigt
(FOLGE-ABLAUF Abschnitt 1: Opfer realer Taten nicht als Comicfigur), nur ihr Blumenladen; sie überlebt.
Lösung: A. Ulrich (Vordermann): versuchter Mord (Heimtücke, S. 349), kein Rücktritt, § 34 (keine Gefahr; Leben gegen Leben
nicht abwägbar, Bewertungsirrtum, S. 350), § 35 (geschützter Personenkreis, S. 350), § 17 (Wortlaut) vermeidbar (S. 350)
→ schuldhaft. B. Irmgard und Wolfram: § 25 I Alt. 2 (Wortlaut), Verantwortungsprinzip/Anstiftung § 26 vs. BGH (S. 351–353),
BGH-Formel wörtlich (S. 354), Subsumtion (S. 354 f.), Bedeutung: Heimtücke-Kenntnis/niedrige Beweggründe (S. 351) →
Ergebnis → Klausurtipp → Schema → Merksatz.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen und im Testvideo nicht vergeben: Irmgard, Wolfram, Ulrich.
Namen nie im Genitiv mit -s. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.9

STIMMEN = {"Irmgard": "sabrina", "Wolfram": "marc", "Ulrich": "william"}  # Lexi = Carla

SEGMENTE = [
    # --- A Fall ----------------------------------------------------------------------------------------------------------------
    ("[fall]Irmgard, Wolfram und Ulrich leben in einer engen Beziehung. [ulrich]Ulrich ist Polizeibeamter, aber "
     "leicht zu beeinflussen. [kk]Mit Tricks und Ritualen bringen die beiden anderen ihn dazu, an den Katzenkönig zu glauben, eine "
     "Macht, die seit Jahrtausenden das Böse verkörpern soll. [motiv]Irmgard will die Frau ihres früheren Freundes töten lassen, "
     "aus Hass und Eifersucht. Wolfram ist einverstanden.", 0.3),
    ("[i1]Der Katzenkönig verlangt ein Menschenopfer: die Frau aus dem Blumenladen. Sonst vernichtet er Millionen Menschen.",
     0.3, "Irmgard"),
    ("[u1]Aber das wäre Mord.", 0.3, "Ulrich"),
    ("[w1]Das Tötungsverbot gilt für uns nicht. Wir retten die Menschheit.", 0.3, "Wolfram"),
    ("[glaubt]Ulrich glaubt ihnen und wägt ab: ein Leben gegen Millionen. [tat]Am späten Abend sucht er die Frau in ihrem "
     "Blumenladen auf und greift sie von hinten an, um sie zu töten, während sie nichts ahnt. [flieht]Als andere ihr zu Hilfe "
     "kommen, flieht er und rechnet mit ihrem Tod. [lebt]Sie überlebt.", 0.3),
    ("[frage]Ulrich hat selbst gehandelt. Sind Irmgard und Wolfram dann nur Anstifter, [frage2]oder Täter hinter dem Täter?", 0.6),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Der echte Fall --------------------------------------------------------------------------------------------------------
    ("[echt]So lag der Katzenkönig-Fall, Bundesgerichtshof, Urteil vom fünfzehnten September neunzehnhundertachtundachtzig. "
     "[vereinf]Wir erzählen ihn vereinfacht und mit anderen Namen. [lg]Das Landgericht verurteilte alle drei wegen versuchten "
     "Mordes. [bgh2]Die Schuldsprüche blieben beim BGH bestehen. Aufgehoben wurden nur die Strafen: Das Landgericht hatte die "
     "Milderung beim Versuch nicht ausreichend geprüft.", PS),
    # --- D A. Ulrich: versuchter Mord --------------------------------------------------------------------------------------------
    ("[ua]Beginne mit dem Tatnächsten, Ulrich. Die Frau lebt, in Betracht kommt versuchter Mord. [entschl]Ulrich "
     "wollte sie töten und hat unmittelbar angesetzt. [heim]Dabei nutzte er ihre Arg- und Wehrlosigkeit bewusst aus: "
     "Heimtücke. [rt]Zurückgetreten ist er nicht, er floh, ohne etwas zu ihrer Rettung zu tun.", PS),
    # --- E Rechtswidrigkeit: § 34 ------------------------------------------------------------------------------------------------
    ("[n34]Gerechtfertigt nach Paragraf vierunddreißig? Eine echte Gefahr gab es nicht. [glaube]Ulrich glaubte zwar an sie. "
     "Doch selbst dann darf man Leben nicht gegen Leben abwägen. [bew]Seine falsche Abwägung ist ein Bewertungsirrtum. Der "
     "Vorsatz bleibt, es geht um einen Verbotsirrtum.", PS),
    # --- F Schuld: § 35 ----------------------------------------------------------------------------------------------------------
    ("[n35]In der Schuld denkst du an den entschuldigenden Notstand. [kreis]Paragraf fünfunddreißig hilft aber nur dem, der die "
     "Gefahr von sich, einem Angehörigen oder einer ihm nahestehenden Person abwenden will. [fremd]Ulrich ging es um Millionen "
     "Menschen, nicht um sich oder seine Angehörigen. [abs2]Deshalb hilft auch Absatz zwei nicht, der vermeintliche "
     "Notstand.", PS),
    # --- G Wortlautkarte § 17 ----------------------------------------------------------------------------------------------------
    ("[p17]Bleibt der Verbotsirrtum, Paragraf siebzehn: Fehlt dem Täter bei Begehung der Tat die Einsicht, Unrecht zu tun, so "
     "handelt er ohne Schuld, wenn er diesen Irrtum nicht vermeiden konnte. [satz2]Konnte er ihn vermeiden, kann die Strafe "
     "gemildert werden. [irrt]Ulrich hielt die Tötung für erlaubt, um Millionen zu retten. [verm]Vermeidbar, sagt der BGH: "
     "Gerade als Polizeibeamter hätte er bei gebührender Gewissensanspannung und nach Befragung einer Vertrauensperson, etwa "
     "eines Geistlichen, erkennen können, dass man Menschenleben nicht gegeneinander aufrechnen darf. [uerg]Ulrich handelt "
     "also schuldhaft.", PS),
    # --- H B. Hintermänner: Wortlautkarte § 25 Abs. 1 ----------------------------------------------------------------------------
    ("[hb]Jetzt Irmgard und Wolfram. Sie haben die Tat nicht selbst ausgeführt. [p25]Paragraf fünfundzwanzig Absatz eins: Als "
     "Täter wird bestraft, wer die Straftat selbst oder durch einen anderen begeht. [alt2]Durch einen anderen: Das ist die "
     "mittelbare Täterschaft. [werk]Meist fehlt dem Werkzeug etwas, etwa der Vorsatz oder die Schuld. [prob]Ulrich aber "
     "handelt vorsätzlich und schuldhaft.", PS),
    # --- I Streit: Verantwortungsprinzip und BGH ---------------------------------------------------------------------------------
    ("[vp]Nach dem Verantwortungsprinzip endet die mittelbare Täterschaft dort, wo der Vordermann selbst voll verantwortlich "
     "ist. [anst]Dann wären Irmgard und Wolfram nur Anstifter, Paragraf sechsundzwanzig. [bgh]Der BGH folgt dem nicht: Allein "
     "die Vermeidbarkeit des Irrtums sei kein taugliches Abgrenzungskriterium, denn auch Ulrich fehlte die Unrechtseinsicht. "
     "[herr]Maßgeblich ist die Tatherrschaft des Hintermanns, wertend im Einzelfall ermittelt.", PS),
    # --- J BGH-Formel ------------------------------------------------------------------------------------------------------------
    ("[formel]Mittelbarer Täter einer versuchten oder vollendeten Tötung ist jedenfalls, wer mit Hilfe des von ihm bewusst hervorgerufenen Irrtums das Geschehen gewollt "
     "auslöst und steuert, [werkz]so dass der Irrende bei wertender Betrachtung als ein, wenn auch schuldhaft handelndes, "
     "Werkzeug anzusehen ist. [thdt]Man spricht vom Täter hinter dem Täter.", PS),
    # --- K Subsumtion -----------------------------------------------------------------------------------------------------------
    ("[subs]So liegt es hier. Irmgard und Wolfram haben den Wahn hervorgerufen und bewusst ausgenutzt, um seine Bedenken "
     "auszuschalten. [anw]Sie bestimmten auch wesentliche Teile der Ausführung, Ulrich hielt sich an ihre "
     "Anweisungen. [wissen]Damit beherrschten sie die Tat kraft ihrer Einwirkung und ihres überlegenen Wissens. [gem]Untereinander "
     "handelten sie gemeinschaftlich.", PS),
    # --- L Warum es darauf ankommt -----------------------------------------------------------------------------------------------
    ("[heimt]Der Streit zählt hier: Als Anstifter zum Mord hätten sie die Heimtücke kennen müssen. Das ließ "
     "sich nach Überzeugung des Landgerichts nicht nachweisen. [nb]Als Täter haften sie wegen ihrer eigenen niedrigen Beweggründe.", PS),
    # --- M Ergebnis --------------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Irmgard und Wolfram sind strafbar wegen versuchten Mordes in mittelbarer Täterschaft, Paragraf "
     "fünfundzwanzig Absatz eins, zweite Alternative. [erg2]Ulrich: versuchter Mord, mit möglicher Milderung "
     "nach Paragraf siebzehn.", PS),
    # --- N Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst den Vordermann vollständig, bis zur Schuld. Erst dort zeigt sich, dass er voll "
     "verantwortlich handelt. [tipp2]Den Streit entscheidest du nur, wenn es darauf ankommt. [tipp3]Hier kommt es darauf an, weil "
     "eine Anstiftung zum Mord am Vorsatz zur Heimtücke scheitern würde.", PS),
    # --- O Klausurschema ---------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sa]A. Strafbarkeit von Ulrich: versuchter Mord. [sa1]Vorprüfung, Tatentschluss mit Heimtücke, "
     "unmittelbares Ansetzen. [sa2]Rechtswidrigkeit: Paragraf vierunddreißig scheitert. [sa3]Schuld: kein Notstand, "
     "Verbotsirrtum vermeidbar. [sa4]Kein Rücktritt. [sb]B. Strafbarkeit von Irmgard und Wolfram: versuchter Mord in "
     "mittelbarer Täterschaft. [sb1]Im Tatentschluss: Tatherrschaft trotz voll verantwortlichen Vordermanns, mit dem Streit, "
     "und niedrige Beweggründe. [sb2]Unmittelbares Ansetzen, spätestens mit dem Ansetzen von Ulrich. "
     "[sb3]Dann Rechtswidrigkeit und Schuld.", PS),
    # --- P Merksatz (Lexi) -------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Auch hinter einem voll verantwortlichen Täter kann ein mittelbarer Täter stehen. [m2]Entscheidend ist, ob "
     "er mit einem bewusst hervorgerufenen Irrtum das Geschehen auslöst und steuert.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
