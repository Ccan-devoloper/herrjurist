"""Folge 082 · § 80 V VwGO: Imbiss sofort geschlossen – was tun? Das Grundschema (Mo · Der Fall · Öffentliches Recht/
Verwaltungsprozessrecht). Übungsfall nach dem Hook des Themenplans: Frau Steinke von der Lebensmittelüberwachung der Stadt
findet im Imbiss von Herrn Hinrichs Mäusekot auf der Arbeitsfläche und angenagte Brötchentüten. Die Stadt schließt den Imbiss
(Art. 138 Abs. 2 Buchst. h VO (EU) 2017/625) bis zur Schädlingsbekämpfung und ordnet die sofortige Vollziehung an
(§ 80 II 1 Nr. 4 VwGO), schriftlich begründet mit der Gesundheit der Gäste. Herr Hinrichs klagt und beantragt beim
Verwaltungsgericht, die aufschiebende Wirkung wiederherzustellen.
Kern: § 80 I 1 (Wortlautkarte), § 80 II 1 Nr. 1–4 (Wortlautkarte Nr. 4), § 80 V 1 (Wortlautkarte); A. Zulässigkeit: § 40 I 1,
Statthaftigkeit (§ 123 V), Antragsbefugnis analog § 42 II, Antragsgegner analog § 78, Rechtsschutzbedürfnis (§ 80 V 2, VI);
B. Begründetheit: formelle Rechtmäßigkeit der Vollziehungsanordnung (Zuständigkeit, § 80 III 1 – OVG NRW 4 B 1116/23 Rn. 7 f.,
7 B 34/25 Rn. 3; Anhörung str., ein Satz), Interessenabwägung (BVerwG 7 VR 7.19 Rn. 8; OVG NRW 15 B 814/19 Rn. 9;
besonderes Vollzugsinteresse OVG NRW 4 B 1116/23 Rn. 43), Subsumtion; Klausurtipp (§ 39 VII LFGB), Schema, Merksatz.
Fiktive Figuren: Herr Hinrichs (marc), Frau Steinke (sabrina), die Richterin (laura_ruhig). Belege je Aussage: RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue für Bild/Tafel/Prüfpfad; jede Marke kommt genau einmal vor."""

P, PS = 0.35, 0.7

STIMMEN = {"Hinrichs": "marc", "Steinke": "sabrina", "Richterin": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Kontrolle im Imbiss, der Bescheid ------------------------------------------------------------------------
    ("[fall]Mittag an der Imbissbude von Herrn Hinrichs. Seit zwanzig Jahren verkauft er hier Currywurst und Pommes. "
     "[steinke]Heute kontrolliert Frau Steinke von der Lebensmittelüberwachung der Stadt die Küche. [kot]Sie findet Mäusekot "
     "auf der Arbeitsfläche und angenagte Brötchentüten.", 0.2),
    ("[st1]Herr Hinrichs, das ist Mäusekot. Dazu dürfen Sie sich jetzt äußern. Morgen bekommen Sie unseren Bescheid.",
     0.3, "Steinke"),
    ("[bescheid]Am nächsten Tag kommt er: Die Stadt schließt den Imbiss, bis die Mäuse bekämpft sind, und ordnet die "
     "sofortige Vollziehung an. Die Gesundheit der Gäste könne nicht bis zum Ende eines Prozesses warten.", 0.3),
    ("[hi1]Zwanzig Jahre ohne Beanstandung! Ich klage dagegen, dann darf ich doch weiter öffnen.", 0.3, "Hinrichs"),
    ("[klage]Er erhebt Klage beim Verwaltungsgericht. [frage]Darf er jetzt wieder öffnen? Und was kann er sofort tun?", 0.6),
    # --- B Sachverhalt --------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Grundsatz § 80 I, Entfallen nach § 80 II ---------------------------------------------------------------------
    ("[wl801]Ausgangspunkt ist Paragraf achtzig Absatz eins Satz eins: Widerspruch und Anfechtungsklage haben aufschiebende "
     "Wirkung. [aw]Solange sie besteht, darf die Behörde den Bescheid nicht vollziehen. [aw2]Herr Hinrichs hätte also "
     "recht, wenn es dabei bliebe.", P),
    ("[wl802]Doch Absatz zwei zählt auf, wann die aufschiebende Wirkung entfällt. [nr13]In den Nummern eins bis drei a "
     "kraft Gesetzes, etwa bei öffentlichen Abgaben und Kosten. [nr4]Nach Nummer vier, wenn die Behörde die sofortige "
     "Vollziehung besonders anordnet. [hier]Genau das hat die Stadt getan. Die Klage hält die Schließung nicht auf.", P),
    # --- D Antrag nach § 80 V 1 -------------------------------------------------------------------------------------------
    ("[wl805]Hilfe bringt Absatz fünf Satz eins: Auf Antrag kann das Gericht der Hauptsache die aufschiebende Wirkung in "
     "den Fällen des Absatzes zwei Satz eins Nummer eins bis drei a ganz oder teilweise anordnen, im Falle des Absatzes "
     "zwei Satz eins Nummer vier ganz oder teilweise wiederherstellen. [antrag]Herr Hinrichs beantragt also beim "
     "Verwaltungsgericht, die aufschiebende Wirkung seiner Klage wiederherzustellen.", P),
    # --- E A. Zulässigkeit ------------------------------------------------------------------------------------------------
    ("[zul]A, Zulässigkeit. [rweg]Erstens, der Verwaltungsrechtsweg nach Paragraf vierzig: Die Schließung stützt sich auf "
     "Lebensmittelrecht, das allein Behörden ermächtigt. Das ist öffentliches Recht. [statt]Zweitens, die Statthaftigkeit. "
     "In der Hauptsache wäre die Anfechtungsklage statthaft, denn die Schließung ist ein belastender Verwaltungsakt. "
     "[statt2]Dann gilt Paragraf achtzig Absatz fünf, nicht die einstweilige Anordnung nach Paragraf hundertdreiundzwanzig.", P),
    ("[befugt]Drittens, die Antragsbefugnis entsprechend Paragraf zweiundvierzig Absatz zwei: Als Adressat kann Herr "
     "Hinrichs in seiner Berufsfreiheit verletzt sein. [gegner]Viertens, der Antragsgegner entsprechend Paragraf "
     "achtundsiebzig: die Stadt als Rechtsträgerin, wenn dein Land nichts anderes bestimmt.", P),
    ("[rsb]Fünftens, das Rechtsschutzbedürfnis. Der Rechtsbehelf in der Hauptsache muss eingelegt oder noch möglich sein; "
     "der Antrag ist schon vor der Klage zulässig. [rsb2]Herr Hinrichs hat geklagt. [abs6]Einen vorherigen Antrag bei der "
     "Behörde verlangt Absatz sechs nur bei Abgaben und Kosten. [zul2]Der Antrag ist zulässig.", PS),
    # --- F B. Begründetheit: formelle Rechtmäßigkeit der Vollziehungsanordnung -------------------------------------------
    ("[begr]B, Begründetheit. Bei Nummer vier prüfst du zuerst die Anordnung der sofortigen Vollziehung selbst. "
     "[zust]Zuständig ist die Behörde, die den Bescheid erlassen hat oder über den Widerspruch entscheidet, hier die Stadt. [abs3]Nach Absatz drei muss sie das "
     "besondere Interesse an der sofortigen Vollziehung schriftlich begründen, bezogen auf den Einzelfall. [inhalt]Ob die "
     "Gründe inhaltlich tragen, spielt hier noch keine Rolle. [fehlt]Fehlt die Begründung, ist die Anordnung schon formell "
     "rechtswidrig.", P),
    ("[gaeste]Die Stadt nennt die Gesundheit der Gäste in genau diesem Imbiss. Das genügt. [anh]Ob die Behörde vor der "
     "Anordnung eigens anhören muss, ist umstritten. Herr Hinrichs konnte sich ohnehin äußern.", P),
    # --- G Interessenabwägung --------------------------------------------------------------------------------------------
    ("[abw]Dann wägt das Gericht selbst ab: das Aussetzungsinteresse von Herrn Hinrichs gegen das öffentliche "
     "Vollzugsinteresse. [eaus]Wesentlich sind die Erfolgsaussichten der Klage, summarisch geprüft. [fg1]Ist der Bescheid "
     "offensichtlich rechtswidrig, überwiegt das Aussetzungsinteresse. [fg2]Ist er offensichtlich rechtmäßig, braucht es "
     "bei Nummer vier zusätzlich ein besonderes Interesse, ihn schon vor dem Ende des Prozesses zu vollziehen. [fg3]Sind die Aussichten "
     "offen, entscheidet eine Folgenabwägung: Was wiegt schwerer, die Folgen eines Stopps oder die der sofortigen "
     "Vollziehung?", P),
    # --- H Subsumtion: Erfolgsaussichten, besonderes Vollzugsinteresse ----------------------------------------------------
    ("[egl]Im Fall: Rechtsgrundlage ist Artikel hundertachtunddreißig Absatz zwei der EU-Kontrollverordnung. Bei einem "
     "festgestellten Verstoß darf die Behörde einen Betrieb für einen angemessenen Zeitraum schließen. [hyg]Mäusekot in der "
     "Küche verstößt gegen die Hygieneregeln der EU: Die Küche muss sauber sein, Schädlinge sind zu bekämpfen. "
     "[verh]Eine bloße Reinigung reicht nicht, solange Mäuse in der Küche sind, und die Schließung gilt nur bis zur "
     "Bekämpfung. [offen]Der Bescheid ist offensichtlich rechtmäßig.", P),
    ("[eilig]Und das besondere Vollzugsinteresse? Jeden Tag essen Gäste aus dieser Küche. Ihr Schutz kann nicht bis zum "
     "Ende des Prozesses warten. [urteil]Das Verwaltungsgericht entscheidet:", 0.2),
    ("[ri1]Der Antrag ist zulässig, aber unbegründet. Er wird abgelehnt.", 0.4, "Richterin"),
    ("[ende]Herr Hinrichs lässt die Mäuse bekämpfen. Nach der Nachkontrolle darf er wieder öffnen.", PS),
    # --- I Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe zuerst, warum die aufschiebende Wirkung entfällt. [tipp1]Hat die Behörde die sofortige "
     "Vollziehung angeordnet, beantragst du die Wiederherstellung, sonst die Anordnung. [tipp2]Vorsicht im Lebensmittelrecht: "
     "Nach Paragraf neununddreißig Absatz sieben Lebensmittel- und Futtermittelgesetzbuch haben Rechtsbehelfe gegen "
     "bestimmte Anordnungen schon kraft Gesetzes keine aufschiebende Wirkung.", PS),
    # --- J Klausurschema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sa]A, Zulässigkeit: [s1]Verwaltungsrechtsweg, [s2]Statthaftigkeit, [s3]Antragsbefugnis, "
     "[s4]Antragsgegner, [s5]Rechtsschutzbedürfnis. [sb]B, Begründetheit: [s6]formelle Rechtmäßigkeit der Anordnung, "
     "[s7]dann die Interessenabwägung mit [s8]Erfolgsaussichten, [s9]besonderem Vollzugsinteresse und [s10]Folgenabwägung.", PS),
    # --- K Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Hat die Behörde die sofortige Vollziehung angeordnet, stellt das Gericht die aufschiebende Wirkung "
     "wieder her, sonst ordnet es sie an. [m2]Entscheidend ist die Interessenabwägung, vor allem nach den Erfolgsaussichten "
     "in der Hauptsache.", 1.4),
]
