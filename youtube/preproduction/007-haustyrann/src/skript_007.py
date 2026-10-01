"""Folge 007 · Haustyrannen-Fall: Den Peiniger im Schlaf töten? (frei nach BGH, Urt. v. 25.3.2003 – 1 StR 483/02 = BGHSt 48, 255;
Linie bestätigt in BGH, Urt. v. 14.12.2023 – 3 StR 185/23). Namen erfunden, keine realen Beteiligten.
Heimtücke beim schlafenden Opfer, §§ 32, 34 StGB scheitern, § 35 I (Dauergefahr, nicht anders abwendbar), § 35 II (Irrtum,
Vermeidbarkeit), Vorrang der gesetzlichen Milderung vor der Rechtsfolgenlösung.
Belege je Aussage: RECHTSSTAND.md. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad. Sensibles Thema: Gewalt nur benannt, nicht gezeigt; Lea nicht besetzt."""

P, PS = 0.4, 0.9

STIMMEN = {"Ralf": "marc", "Nadine": "laura_klar", "Beraterin": "julia"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: das Haus (Tag) ------------------------------------------------------------------------------
    ("[haus]Ein Wohnhaus, ein Ehepaar, zwei Töchter. [jahre]Seit fünfzehn Jahren misshandelt Ralf seine Frau Nadine. "
     "[steigt]Die Gewalt wird immer schlimmer, inzwischen trifft sie auch die Töchter.", 0.4),
    ("[r1]Wenn du gehst, finde ich dich. Überall.", 0.4, "Ralf"),
    ("[angst]Nadine glaubt ihm. Ralf ist als äußerst gewalttätig bekannt.", 0.6),
    # --- B Fall: die Nacht -----------------------------------------------------------------------------------
    ("[nacht]Eines Nachts kommt Ralf gegen halb vier nach Hause. [streit]Er beschimpft Nadine und schlägt sie. "
     "[schlaf]Dann legt er sich schlafen.", 0.5),
    # --- C Fall: der Vormittag ---------------------------------------------------------------------------------
    ("[morgen]Am Vormittag findet Nadine seinen Revolver. [ringen]Lange ringt sie mit sich. "
     "[tat]Gegen Mittag geht sie ins Schlafzimmer und erschießt den schlafenden Ralf.", 0.7),
    ("[n1]Ich sah keinen anderen Ausweg.", 0.5, "Nadine"),
    ("[frage]Durfte Nadine ihren Peiniger im Schlaf töten? Ist das Mord, oder ist sie entschuldigt?", 0.6),
    # --- D Sachverhalt -----------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt noch einmal zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- E Tatbestand: Heimtücke ----------------------------------------------------------------------------
    ("[a]Wir prüfen Mord, Paragraf zweihundertelf. [tb]Nadine hat Ralf vorsätzlich getötet. "
     "[heim]In Betracht kommt Heimtücke: Heimtückisch tötet, wer in feindlicher Willensrichtung die Arg- und Wehrlosigkeit "
     "des Opfers bewusst zur Tötung ausnutzt.", P),
    ("[schlaf2]Ein Schlafender ist wehrlos. Seine Arglosigkeit hat er mit in den Schlaf genommen. "
     "[nie]Ralf rechnete auch nicht mit einem Angriff, denn Nadine hatte sich nie gewehrt. "
     "[heim_erg]Sie nutzte das bewusst aus. Heimtücke liegt vor.", PS),
    # --- F Rechtswidrigkeit: §§ 32, 34 ------------------------------------------------------------------------
    ("[rw]Ist die Tat gerechtfertigt? [nw]Notwehr verlangt einen gegenwärtigen Angriff. Ralf schläft, ein Angriff läuft "
     "gerade nicht. [nw_erg]Notwehr scheidet aus.", P),
    ("[ns]Beim rechtfertigenden Notstand muss das geschützte Interesse wesentlich überwiegen. "
     "[ns2]Die Gesundheit von Nadine und den Töchtern überwiegt aber nicht Ralfs Leben. "
     "[ns3]Selbst bei akuter Lebensgefahr fiele die Abwägung nicht zu ihren Gunsten aus. [rw_erg]Die Tat ist rechtswidrig.", PS),
    # --- G Schuld: § 35 I, Gefahr -------------------------------------------------------------------------------
    ("[schuld]Bleibt die Schuld: der entschuldigende Notstand, Paragraf fünfunddreißig. [gefahr]Er verlangt keinen "
     "Angriff, sondern eine gegenwärtige Gefahr für Leben, Leib oder Freiheit.", P),
    ("[dauer]Naheliegend ist hier eine Dauergefahr: Die Gewalt kann jederzeit wieder ausbrechen. [jetzt]Und diese Gefahr ist "
     "gegenwärtig, obwohl Ralf schläft. Er hatte Nadine schon nachts ohne Anlass geschlagen, und nach dem Aufwachen drohte neue Gewalt.", P),
    ("[ehe]Dass Nadine trotz allem bei ihm blieb, macht ihr die Gefahr nicht zumutbar.", PS),
    # --- H Schuld: nicht anders abwendbar -------------------------------------------------------------------------
    ("[anders]Entscheidend: Die Gefahr darf nicht anders abwendbar sein, die Tat muss das einzig "
     "geeignete Mittel sein. [hilfe]Nadine hätte mit den Töchtern in ein Frauenhaus gehen oder die Polizei um Hilfe bitten können.", P),
    ("[b1]Sie und Ihre Töchter können noch heute zu uns kommen.", 0.4, "Beraterin"),
    ("[regel]Der Bundesgerichtshof sagt: Eine solche Dauergefahr ist in der Regel anders abwendbar, indem man Hilfe Dritter "
     "holt, vor allem vom Staat. [ausnahme]Anders nur, wenn konkrete Umstände die Wirksamkeit dieser Hilfe von vornherein zweifelhaft machen.", P),
    ("[versucht]Nadine hat Hilfe nicht gesucht. [offen]Ob Hilfe hier ausnahmsweise aussichtslos war, musste das Landgericht "
     "noch klären. Der Bundesgerichtshof hielt das für eher fernliegend.", PS),
    # --- I Schuld: § 35 II Irrtum ---------------------------------------------------------------------------------
    ("[irrtum]Nadine hielt ihre Lage aber für ausweglos. Dann kommt es auf Paragraf fünfunddreißig Absatz zwei an. "
     "[unverm]War der Irrtum unvermeidbar, bleibt sie straflos. [verm]War er vermeidbar, wird sie bestraft, aber die Strafe "
     "muss gemildert werden.", P),
    ("[pruef]Ob der Irrtum vermeidbar war, hängt davon ab, ob sie mögliche Auswege gewissenhaft geprüft hat. "
     "Bei einer Tötung gelten dafür strenge Anforderungen. [zeit]Lange Bedenkzeit, in der sie sich "
     "Rat hätte holen können, spricht für Vermeidbarkeit.", PS),
    # --- J Strafe: § 49 I vor Rechtsfolgenlösung ----------------------------------------------------------------
    ("[folge]Und die Strafe? Mord wird mit lebenslanger Freiheitsstrafe bestraft. [lg]Im Originalfall milderte das Landgericht "
     "trotzdem, wegen außergewöhnlicher Umstände: neun Jahre, nach der sogenannten Rechtsfolgenlösung.", P),
    ("[gs]Diese Milderung hat der Große Senat für Ausnahmefälle des Heimtückemords "
     "entwickelt. [vorrang]Der Bundesgerichtshof stellt klar: Eine gesetzliche Milderung geht vor, hier also die nach "
     "Paragraf fünfunddreißig Absatz zwei. [rahmen]Der Strafrahmen ist derselbe: drei bis fünfzehn Jahre. "
     "[gewicht]Aber die jahrelangen Misshandlungen dürfen dann bei der Strafhöhe stärker mildernd zählen.", PS),
    ("[erg]Der Bundesgerichtshof hob die Verurteilung deshalb auf. "
     "[erg2]Für deine Klausur heißt das: Mord, nicht gerechtfertigt, in der Regel nicht entschuldigt. "
     "[erg3]Bei vermeidbarem Irrtum: zwingend gemilderte Strafe.", PS),
    # --- K Klausurtipp (Lexi) -------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Trenne Angriff und Gefahr. [tipp1]Gegen den schlafenden Tyrannen scheitert Notwehr am Angriff, "
     "die Dauergefahr prüfst du beim Notstand.", PS),
    # --- L Klausurschema -------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Römisch eins, Tatbestand: Tötung, Vorsatz und Heimtücke. "
     "[k2]Römisch zwei, Rechtswidrigkeit: Notwehr scheitert am Angriff, Notstand an der Abwägung.", P),
    ("[k3]Römisch drei, Schuld: Paragraf fünfunddreißig mit Dauergefahr, Gegenwärtigkeit und "
     "anderer Abwendbarkeit. [k4]Dann der Irrtum nach Absatz zwei und seine Vermeidbarkeit. "
     "[k5]Römisch vier, Strafe: Milderung nach Paragraf neunundvierzig vor der Rechtsfolgenlösung.", PS),
    # --- M Merksatz (Lexi) ------------------------------------------------------------------------------------
    ("[merke]Merke: Gegen den schlafenden Haustyrannen gibt es keine Notwehr. [m2]Und entschuldigt ist die Tötung in der "
     "Regel nicht, denn Hilfe von außen geht vor.", 1.4),
]
