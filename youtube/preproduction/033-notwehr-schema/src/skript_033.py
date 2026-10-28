"""Folge 033 · Notwehr Schema § 32 StGB – so prüfst du die Notwehr (Fr · Klausurpraxis, Format Schema).
Fiktiver Fall: Vor der Stadtbibliothek zerrt Torsten (Mitte 20) an der Tasche von Ulrike (Mitte 40). Ulrike warnt
("Lass los, sonst wehre ich mich!"), der Passant Herr Kluge (um 70) ruft die Polizei; Torsten zerrt fester, Ulrike tritt ihm
gegen das Schienbein, er lässt los (Bluterguss). § 223 StGB nur kurz; Schwerpunkt § 32 StGB (Wortlautkarte Abs. 1 und 2):
1. Notwehrlage (Angriff, gegenwärtig, rechtswidrig), 2. Notwehrhandlung (gegen den Angreifer, erforderlich: geeignet und
mildestes gleich wirksames Mittel, Warnung/Androhung; geboten: sozialethische Einschränkungen im Überblick), 3. Verteidigungswille,
Rechtsfolge; Abgrenzung § 33 kurz (Wortlautkarte). Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.9

STIMMEN = {"Ulrike": "laura_klar", "Torsten": "niklas", "Kluge": "helmut"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: vor der Stadtbibliothek ------------------------------------------------------------------------------
    ("[fall]Dienstagnachmittag vor der Stadtbibliothek. [ulrike]Ulrike, Mitte vierzig, schließt ihr Fahrrad auf, die Tasche "
     "über der Schulter. [torsten]Da kommt Torsten, Mitte zwanzig, packt die Tasche und zerrt daran.", 0.2),
    ("[t1]Her mit der Tasche!", 0.3, "Torsten"),
    ("[haelt]Ulrike hält die Tasche mit beiden Händen fest.", 0.2),
    ("[u1]Lass los, sonst wehre ich mich!", 0.3, "Ulrike"),
    ("[kluge]Ein älterer Passant, Herr Kluge, zieht sein Handy hervor.", 0.2),
    ("[kl1]Ich rufe die Polizei!", 0.3, "Kluge"),
    ("[zerrt]Doch Torsten zerrt nur noch fester. [tritt]Da tritt Ulrike ihm kräftig gegen das Schienbein. [los]Torsten lässt "
     "los und humpelt davon. [blau]Am Schienbein bekommt er einen Bluterguss.", 0.3),
    ("[frage]Hat Ulrike sich wegen Körperverletzung strafbar gemacht? [frage2]An diesem Fall prüfen wir die Notwehr Schritt "
     "für Schritt.", 0.6),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Tatbestand kurz, Wortlaut § 32 ------------------------------------------------------------------------------
    ("[tb]Zuerst kurz der Tatbestand der Körperverletzung, Paragraf zweihundertdreiundzwanzig. [tb2]Der Tritt ist eine "
     "körperliche Misshandlung, der Bluterguss eine Gesundheitsschädigung, und Ulrike handelt vorsätzlich. [rw]Fraglich ist "
     "die Rechtswidrigkeit. Ulrike könnte durch Notwehr gerechtfertigt sein.", P),
    ("[p32]Paragraf zweiunddreißig, Absatz eins: Wer eine Tat begeht, die durch Notwehr geboten ist, handelt nicht "
     "rechtswidrig. [abs2]Absatz zwei: Notwehr ist die Verteidigung, die erforderlich ist, um einen gegenwärtigen rechtswidrigen "
     "Angriff von sich oder einem anderen abzuwenden. [aufbau]Daraus ergibt sich der Aufbau: Notwehrlage, Notwehrhandlung und "
     "Verteidigungswille.", PS),
    # --- D 1. Notwehrlage ----------------------------------------------------------------------------------------------
    ("[lage]Erstens die Notwehrlage. [angriff]Ein Angriff liegt vor: Torsten will Ulrike die Tasche entreißen. Damit greift er "
     "ihr Eigentum und ihren Besitz an, und auch diese Güter darf man verteidigen. [gegenw]Gegenwärtig ist ein Angriff, der "
     "unmittelbar bevorsteht, gerade stattfindet oder noch andauert. Torsten zerrt in diesem Moment an der Tasche. "
     "[rechtsw]Rechtswidrig ist der Angriff, weil er im Widerspruch zur Rechtsordnung steht. [lage_ok]Die Notwehrlage liegt vor.", P),
    # --- E 2. Notwehrhandlung: gegen den Angreifer, Erforderlichkeit ---------------------------------------------------
    ("[handl]Zweitens die Notwehrhandlung. [gegen]Sie muss sich gegen den Angreifer richten, und der Tritt trifft Torsten "
     "selbst. [erf]Dann die Erforderlichkeit. Nach dem Bundesgerichtshof ist die Abwehr erforderlich, wenn sie den Angriff "
     "sofort und endgültig abwehrt und das mildeste Mittel ist, das in der konkreten Lage zur Verfügung steht. [geeig]Geeignet "
     "war der Tritt, denn Torsten ließ los.", P),
    ("[milder]Gab es ein milderes Mittel, das genauso sicher gewirkt hätte? [warn]Ulrike hat zuerst gewarnt, ohne Erfolg. "
     "[festh]Nur festhalten? Torsten zerrte immer fester. [polizei]Und die Polizei wäre zu spät gekommen. [risiko]Auf ein "
     "milderes Mittel muss Ulrike nur zurückgreifen, wenn seine Wirkung unzweifelhaft ist. [flucht]Fliehen oder die Tasche "
     "loslassen muss sie nicht, denn damit würde sie den Angriff einfach hinnehmen. [erf_ok]Der Tritt war erforderlich.", P),
    ("[droh]Übrigens: Greift jemand gegen einen unbewaffneten Angreifer zu einer lebensgefährlichen Waffe, verlangt der "
     "Bundesgerichtshof in der Regel, den Einsatz zuerst anzudrohen oder weniger gefährlich zu versuchen.", PS),
    # --- F Gebotenheit -------------------------------------------------------------------------------------------------
    ("[geboten]Dann die Gebotenheit. Eine Abwägung der Rechtsgüter verlangt die Notwehr grundsätzlich nicht. [sozial]Nur in "
     "Ausnahmefällen schränkt die Rechtsprechung das Notwehrrecht aus sozialethischen Gründen ein. [fg1]Etwa bei Angriffen "
     "erkennbar Schuldloser, wie Kinder, [fg2]bei einem krassen Missverhältnis, wenn eine gefährliche Abwehr nur eine Bagatelle "
     "abwehrt, [fg3]wenn der Verteidiger den Angriff vorwerfbar provoziert hat, [fg4]oder bei enger familiärer Verbundenheit. "
     "[fg_rf]Dann kann verlangt werden, auszuweichen oder sich schonender zu wehren.", P),
    ("[geb_ok]Bei Ulrike passt keine Fallgruppe. Torsten ist erwachsen, Ulrike hat nichts provoziert, und ein Tritt gegen das "
     "Schienbein steht in keinem krassen Missverhältnis zum Griff nach ihrer Tasche. [geb_erg]Die Abwehr ist geboten.", PS),
    # --- G 3. Verteidigungswille ---------------------------------------------------------------------------------------
    ("[wille]Drittens der Verteidigungswille. Ulrike muss zumindest auch handeln, um den Angriff abzuwehren. [wut]Ärger oder "
     "Wut daneben schaden nicht, solange der Abwehrzweck nicht ganz in den Hintergrund tritt. [wille_ok]Ulrike wollte ihre "
     "Tasche behalten.", P),
    # --- H Ergebnis und Rechtsfolge ------------------------------------------------------------------------------------
    ("[ergebnis]Ergebnis: Ulrike handelt in Notwehr und damit nicht rechtswidrig. Sie hat sich nicht strafbar gemacht. "
     "[duld]Und weil ihre Abwehr rechtmäßig ist, kann Torsten sich gegen sie nicht seinerseits auf Notwehr berufen.", PS),
    # --- I Abgrenzung § 33 ---------------------------------------------------------------------------------------------
    ("[p33]Kurz zur Abgrenzung: Wehrt sich jemand stärker als erforderlich, ist die Tat nicht gerechtfertigt. [p33b]Dann kann "
     "Paragraf dreiunddreißig helfen: Überschreitet der Täter die Grenzen der Notwehr aus Verwirrung, Furcht oder Schrecken, "
     "so wird er nicht bestraft. [p33c]Die Tat bleibt rechtswidrig, aber der Täter ist entschuldigt. [p33d]Voraussetzung ist "
     "eine echte Notwehrlage.", PS),
    # --- J Klausurtipp (Lexi) ------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Notwehr prüfst du in der Rechtswidrigkeit, nach dem Tatbestand. Den Schwerpunkt setzt du meist "
     "bei der Erforderlichkeit. [tipp2]Nenne dort die milderen Mittel konkret, wie Warnung, Festhalten oder Hilfe rufen, und "
     "begründe, warum sie nicht genauso sicher gewirkt hätten. [tipp3]Die Gebotenheit sprichst du nur an, wenn der Sachverhalt "
     "eine Fallgruppe nahelegt.", PS),
    # --- K Klausurschema -----------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema zur Notwehr. [k1]Erstens die Notwehrlage: [k1a]ein Angriff, [k1b]gegenwärtig [k1c]und "
     "rechtswidrig. [k2]Zweitens die Notwehrhandlung: [k2a]Verteidigung gegen den Angreifer, [k2b]erforderlich, also geeignet "
     "und das mildeste gleich wirksame Mittel, [k2c]und geboten. [k3]Drittens der Verteidigungswille. [k4]Folge: Die Tat ist "
     "nicht rechtswidrig.", PS),
    # --- L Merksatz (Lexi) ---------------------------------------------------------------------------------------------
    ("[merke]Merke: Notwehr braucht eine Notwehrlage, eine erforderliche und gebotene Verteidigung und den Verteidigungswillen. "
     "[m2]Erforderlich ist das mildeste Mittel, das sicher wirkt. [m3]Und fliehen muss der Angegriffene grundsätzlich nicht.", 1.4),
]
