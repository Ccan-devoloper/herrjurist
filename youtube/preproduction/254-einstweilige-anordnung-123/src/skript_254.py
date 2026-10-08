"""Folge 254 · § 123 VwGO: Einstweilige Anordnung – Prüfungsschema (Mi · Examenswissen · Verwaltungsprozessrecht · Schema).
Übungsfall nach dem Hook des Themenplans („Das Stadtfest ist in zehn Tagen, die Stadt verweigert dir den Standplatz“):
Magda backt seit Jahren Waffeln auf dem Stadtfest, ihrem wichtigsten Geschäft im Jahr. Die Stadt veranstaltet das Fest als
festgesetztes Volksfest (§§ 60b, 69 GewO). Herr Eckstein vom Marktamt lehnt ihren Antrag ab, weil sie die Stadt in einem
Leserbrief kritisiert hat; laut Lageplan sind noch drei Plätze frei. Das Fest beginnt in zehn Tagen.
Aufbau: A. Zulässigkeit: I. Verwaltungsrechtsweg, II. Statthaftigkeit § 123 Abs. 5 (Wortlautkarte; Verpflichtungssituation,
§ 80 V nur verwiesen – Folge 082; Hauptsache Verpflichtungsklage nur verwiesen – Folge 093), Sicherungs- vs. Regelungsanordnung
§ 123 Abs. 1 S. 1/S. 2 (Wortlautkarte; VG Gelsenkirchen 18 L 76/26 Rn. 7), III. Antragsbefugnis analog § 42 II (§ 70 I GewO),
IV. Rechtsschutzbedürfnis (Vorbefassung, BVerwG 6 VR 4.21 Rn. 7 f., 10), Antrag vor Klageerhebung → B. Begründetheit:
§ 123 Abs. 3 i. V. m. §§ 920 Abs. 2, 294 ZPO (Wortlautkarte), I. Anordnungsanspruch (§ 70 I, III GewO, Wortlautkarte; OVG NRW
15 B 144/24 Rn. 7; 4 B 1069/18 Rn. 7), II. Anordnungsgrund, III. Vorwegnahme der Hauptsache (BVerwG 6 VR 3.13 Rn. 5, 7; BVerfG
1 BvR 569/05 Rn. 23–25; OVG NRW 15 B 144/24 Rn. 29, 32) → Ergebnis (Beschluss, § 123 Abs. 4) → Klausurtipp, Schema, Merksatz.
Belege je Cue: ../RECHTSSTAND.md.
Stimmen (Pool niklas, helmut, ela_froh, julia): Magda ela_froh (Frau, jung, fröhlich – sympathische Standbetreiberin, keine
ernste Rolle), Herr Eckstein helmut (Mann, älter), der Richter niklas (Mann, jung; Funktionsrolle ohne Namen). julia nicht
gebraucht. Erzählerin und Lexi: Carla ohne Rolle. Namen nie im Genitiv mit -s.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter."""
import re as _re

P, PS = 0.3, 0.5

STIMMEN = {"Magda": "ela_froh", "Eckstein": "helmut", "Richter": "niklas"}

SEGMENTE = [
    # --- A Fall: Im Marktamt ---------------------------------------------------------------------------------------------
    ("[fall]Das Stadtfest ist in zehn Tagen, und die Stadt verweigert Magda den Standplatz. [magda]Seit Jahren backt sie "
     "dort Waffeln, es ist ihr wichtigstes Geschäft im Jahr. [lage]Laut Lageplan sind noch drei Plätze frei. "
     "[eckstein]Herr Eckstein vom Marktamt nennt ihr den Grund:", 0.2),
    ("[ec1]Sie haben die Stadt in einem Leserbrief kritisiert. Für Sie gibt es dieses Jahr keinen Platz.", P, "Eckstein"),
    ("[ma1]Aber ich darf doch meine Meinung sagen!", P, "Magda"),
    ("[bescheid]Die Ablehnung bekommt sie schriftlich. [monate]Eine Klage würde Monate dauern, das Fest wäre längst "
     "vorbei. [frage]Wie kommt Magda schnell zu ihrem Standplatz? [frage2]Das Prüfungsschema der einstweiligen Anordnung.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C A. Zulässigkeit: Rechtsweg, Statthaftigkeit § 123 Abs. 5 (Wortlautkarte) ----------------------------------------
    ("[zul]A, Zulässigkeit. [rweg]Erstens, der Verwaltungsrechtsweg: Die Stadt veranstaltet das Fest und entscheidet über "
     "die Zulassung durch Bescheid. Das ist öffentliches Recht. [wl5]Zweitens, die Statthaftigkeit. Paragraf "
     "hundertdreiundzwanzig Absatz fünf: Die Vorschriften der Absätze eins bis drei gelten nicht für die Fälle der "
     "Paragrafen achtzig und achtzig a. [subs]Die einstweilige Anordnung tritt also zurück, wenn es um aufschiebende "
     "Wirkung geht. [haupt]Entscheidend ist die Hauptsache. Magda will nicht nur die Ablehnung loswerden, sie will die "
     "Zulassung. Das wäre eine Verpflichtungsklage. [statt]Eine aufschiebende Wirkung brächte ihr keinen Platz. Statthaft "
     "ist also der Antrag nach Paragraf hundertdreiundzwanzig. [verweis]Mehr zur Abgrenzung in unseren Videos zu Paragraf "
     "achtzig Absatz fünf und zur Verpflichtungsklage.", P),
    # --- D Sicherungs- oder Regelungsanordnung, § 123 Abs. 1 (Wortlautkarte) ------------------------------------------------
    ("[wl1]Welche Anordnung? Absatz eins kennt zwei. [sich]Die Sicherungsanordnung nach Satz eins schützt vor einer "
     "Veränderung des bestehenden Zustands. [regl]Die Regelungsanordnung nach Satz zwei regelt einen vorläufigen Zustand in "
     "einem streitigen Rechtsverhältnis, um wesentliche Nachteile abzuwenden. [ma_r]Magda will nichts Bestehendes sichern, "
     "sie will einen Platz bekommen, den sie noch nicht hat. Also: Regelungsanordnung.", P),
    # --- E III. Antragsbefugnis, IV. Rechtsschutzbedürfnis ----------------------------------------------------------------
    ("[befugt]Drittens, die Antragsbefugnis entsprechend Paragraf zweiundvierzig Absatz zwei: Magda kann einen Anspruch auf "
     "Zulassung aus Paragraf siebzig Gewerbeordnung haben. [rsb]Viertens, das Rechtsschutzbedürfnis. Grundsätzlich musst "
     "du dich zuerst an die Behörde wenden. [rsb2]Magda hat den Standplatz beantragt, die Stadt hat abgelehnt. "
     "[vor]Klagen muss sie noch nicht: Der Antrag ist schon vor Klageerhebung möglich. [zul2]Der Antrag ist zulässig.", PS),
    # --- F B. Begründetheit: Glaubhaftmachung (Wortlautkarte § 123 Abs. 3, §§ 920 Abs. 2, 294 Abs. 1 ZPO) ------------------
    ("[begr]B, Begründetheit. Magda braucht einen Anordnungsanspruch und einen Anordnungsgrund. [wl3]Beides muss sie "
     "glaubhaft machen: Absatz drei verweist auf Paragraf neunhundertzwanzig Absatz zwei Zivilprozessordnung. "
     "[z294]Nach Paragraf zweihundertvierundneunzig darf sie dafür alle Beweismittel nutzen, auch eine Versicherung an "
     "Eides statt. [mittel]Magda legt den Bescheid und den Lageplan vor und versichert an Eides statt, was Herr Eckstein "
     "gesagt hat.", P),
    # --- G I. Anordnungsanspruch (§ 70 GewO, Wortlautkarte) ---------------------------------------------------------------
    ("[aa]Erstens, der Anordnungsanspruch. Er liegt vor, wenn ihr Anspruch überwiegend wahrscheinlich besteht. [wl70]Das "
     "Stadtfest ist als Volksfest festgesetzt. Nach Paragraf siebzig Gewerbeordnung darf dann jeder teilnehmen, der zum "
     "Teilnehmerkreis gehört. [aus]Ausschließen darf die Stadt nur aus sachlich gerechtfertigten Gründen, vor allem wenn "
     "der Platz nicht reicht. [frei]Hier sind aber Plätze frei. [kritik]Und ein kritischer Leserbrief ist kein sachlicher "
     "Grund, er ist von der Meinungsfreiheit gedeckt. [null]Die Stadt hat keinen Spielraum mehr: Sie muss Magda zulassen.", P),
    # --- H II. Anordnungsgrund, III. Vorwegnahme der Hauptsache -----------------------------------------------------------
    ("[ag]Zweitens, der Anordnungsgrund, also die Eilbedürftigkeit. [ag2]Das Fest beginnt in zehn Tagen, eine Entscheidung "
     "in der Hauptsache käme zu spät.", P),
    ("[vw]Aber Vorsicht: Mit der Zulassung bekäme Magda schon alles, was sie mit der Klage erreichen will. [vw2]Nach dem "
     "Fest bliebe für die Hauptsache nichts mehr übrig. Die Eilentscheidung nähme sie vorweg. [verbot]Das darf das Gericht "
     "grundsätzlich nicht, es soll nur vorläufig regeln. [ausn]Eine Ausnahme macht das Bundesverwaltungsgericht, wenn das "
     "Abwarten schwere und unzumutbare Nachteile hätte, die sich später nicht mehr beseitigen lassen, [ausn2]und wenn die "
     "Hauptsache erkennbar Erfolg hätte. Dafür gilt ein strenger Maßstab. [art19]So verlangt es der effektive Rechtsschutz "
     "aus Artikel neunzehn Absatz vier Grundgesetz, betont das Bundesverfassungsgericht. [beides]Bei Magda trifft beides "
     "zu: Ihr wichtigstes Fest wäre unwiederbringlich verloren, und ihr Anspruch ist eindeutig.", P),
    # --- I Ergebnis: Beschluss -------------------------------------------------------------------------------------------
    ("[erg]Das Verwaltungsgericht entscheidet durch Beschluss.", 0.2),
    ("[ri1]Die Stadt muss die Antragstellerin zum Stadtfest zulassen.", P, "Richter"),
    ("[ende]Zehn Tage später verkauft Magda ihre Waffeln auf dem Stadtfest.", PS),
    # --- J Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Schau genau, ob der Behörde noch ein Spielraum bleibt. [tipp1]Gibt es mehr Bewerber als Plätze, "
     "bekommst du meist nur eine neue Entscheidung über deinen Antrag. [tipp2]Die Zulassung selbst gibt es in der Regel nur, "
     "wenn der Spielraum auf null geschrumpft ist.", PS),
    # --- K Klausurschema (Lexi) --------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [sa]A, Zulässigkeit: [s1]Verwaltungsrechtsweg, [s2]Statthaftigkeit mit Absatz fünf und der "
     "Art der Anordnung, [s3]Antragsbefugnis, [s4]Rechtsschutzbedürfnis. [sb]B, Begründetheit: [s5]Anordnungsanspruch "
     "[s6]und Anordnungsgrund, [s7]beide glaubhaft gemacht. [s8]Und bei einer Vorwegnahme der Hauptsache die strengen "
     "Ausnahmen.", PS),
    # --- L Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Geht es nicht um aufschiebende Wirkung, hilft im Eilverfahren Paragraf hundertdreiundzwanzig. [m2]Die "
     "Hauptsache vorwegnehmen darf das Gericht nur, wenn sonst unzumutbare Nachteile drohen und die Hauptsache erkennbar "
     "Erfolg hätte.", 1.4),
]

_alle = [m for s in SEGMENTE for m in _re.findall(r"\[(\w+)\]", s[0])]
assert len(_alle) == len(set(_alle)), "Marke doppelt"
