"""Folge 189 · Rechtfertigender Notstand § 34 StGB: Schema mit Berghütten-Fall (Fr · Klausurpraxis · StGB AT, Format Schema).
Beispielfall nach dem Plan-Hook („Ein Wanderer bricht bei einem Wettersturz die Tür einer verschlossenen Berghütte auf, um
nicht zu erfrieren“): Samstag, 17:40 Uhr, auf 2.150 m. Korbinian (Mitte 30) gerät allein in einen Wettersturz: Schneesturm,
−12 °C, kein Netz, bis ins Tal 3 Stunden. Die Berghütte von Frau Moser (um 55, Eigentümerin, bewirtschaftet sie im Sommer) ist im
Winter verschlossen, ein Schild verbietet das Betreten. Korbinian bricht die Tür auf (nur als Icon: Werkzeug, offene Tür), das
Schloss ist kaputt; er übersteht die Nacht. Am Morgen: Frau Moser, neues Schloss 380 €.
Aufbau (Schema): Fall → Sachverhalt → Tatbestand §§ 303, 123 kurz → Wortlautkarte § 34 S. 1, S. 2 → 1. Notstandslage
(Gefahr für Rechtsgut, gegenwärtig; BGH 1 StR 483/02 Rn. 27) → 2. Notstandshandlung (nicht anders abwendbar: geeignet,
erforderlich) → 3. Interessenabwägung (wesentlich überwiegt; Leben gegen Eigentum) → 4. Angemessenheit S. 2 → 5. subjektives
Rechtfertigungselement → § 904 BGB (Wortlautkarte S. 1, S. 2: Aggressivnotstand, Ersatzpflicht) → § 228 BGB (Wortlautkarte,
Defensivnotstand) → Spezialität (h. M.) → Abgrenzung § 32 (Verweis Folge 033) und § 35 (BGH 1 StR 483/02 Rn. 21) → Lösung →
Klausurtipp (Lexi) → Schema → Merksatz (Lexi). Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, nicht vergeben (Volltextsuche 04.10.2026): Korbinian, Moser. Stimmen (Pool william,
sabrina, marc, laura_ruhig): Korbinian marc (Mann, mittel), Frau Moser laura_ruhig (Frau, mittel). Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Korbinian": "marc", "Moser": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Wettersturz am Berg ------------------------------------------------------------------------------------------
    ("[fall]Samstag, siebzehn Uhr vierzig, auf zweitausendeinhundertfünfzig Metern. [korb]Korbinian, Mitte dreißig, ist "
     "allein auf Bergtour. [sturz]Da kommt ein Wettersturz: Schneesturm, minus zwölf Grad. [netz]Sein Handy hat kein Netz, "
     "[tal]bis ins Tal sind es drei Stunden.", P),
    # --- A2 Fall: an der Berghütte ---------------------------------------------------------------------------------------------
    ("[huette]Da sieht er eine Berghütte. Sie gehört Frau Moser, [zu]ist im Winter aber verschlossen, [schild]und ein "
     "Schild verbietet das Betreten.", P),
    ("[ko1]Wenn ich heute Nacht hier draußen bleibe, erfriere ich.", P, "Korbinian"),
    ("[auf]Korbinian bricht die Tür auf, [kaputt]das Schloss ist danach kaputt. [nacht]In der Hütte übersteht er die Nacht.", P),
    # --- A3 Fall: am nächsten Morgen -------------------------------------------------------------------------------------------
    ("[morgen]Am nächsten Morgen kommt Frau Moser zur Hütte. [preis]Ein neues Schloss kostet dreihundertachtzig Euro.", P),
    ("[mo1]Die Tür war abgesperrt! Wer bezahlt mir jetzt das neue Schloss?", P, "Moser"),
    ("[frage]Hat Korbinian sich strafbar gemacht? [frage2]Und muss er das Schloss bezahlen? [frage3]Wir prüfen den rechtfertigenden "
     "Notstand Schritt für Schritt.", PS),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Tatbestand kurz -----------------------------------------------------------------------------------------------------
    ("[tb]Zuerst kurz der Tatbestand: [tb303]Mit dem kaputten Schloss beschädigt Korbinian eine fremde Sache, Paragraf "
     "dreihundertdrei, [tb123]und er dringt in die fremde Hütte ein, Hausfriedensbruch, Paragraf hundertdreiundzwanzig. "
     "[vors]Vorsatz liegt vor. [rw]Fraglich ist die Rechtswidrigkeit.", PS),
    # --- D Wortlautkarte § 34 --------------------------------------------------------------------------------------------------
    ("[p34]Paragraf vierunddreißig Satz eins: Wer in einer gegenwärtigen, nicht anders abwendbaren Gefahr für ein Rechtsgut "
     "eine Tat begeht, um die Gefahr abzuwenden, handelt nicht rechtswidrig, [abw]wenn das geschützte Interesse das "
     "beeinträchtigte wesentlich überwiegt. [s2]Satz zwei: Die Tat muss ein angemessenes Mittel sein.", PS),
    # --- E 1. Notstandslage ----------------------------------------------------------------------------------------------------
    ("[lage]Erstens die Notstandslage: eine Gefahr für ein Rechtsgut. [leben]Korbinian droht zu erfrieren, also eine Gefahr "
     "für Leben und Leib. [gegenw]Gegenwärtig ist die Gefahr nach dem Bundesgerichtshof, wenn die Schutzmaßnahmen sofort "
     "eingeleitet werden müssen, um den Schaden sicher zu verhindern. [lage_ok]Bei minus zwölf Grad und einbrechender Nacht ist "
     "das der Fall.", PS),
    # --- F 2. Notstandshandlung ------------------------------------------------------------------------------------------------
    ("[handl]Zweitens die Notstandshandlung: Die Gefahr darf nicht anders abwendbar sein. [geeig]Die Tat muss geeignet sein: "
     "In der Hütte ist Korbinian vor Kälte und Wind geschützt. [erf]Und sie muss erforderlich sein, also das mildeste gleich "
     "wirksame Mittel. [kein]Ein Notruf geht nicht durch, der Abstieg dauert drei Stunden, eine andere Unterkunft gibt es "
     "nicht. [nur]Und er bricht nur die Tür auf, nichts sonst.", PS),
    # --- G 3. Interessenabwägung -----------------------------------------------------------------------------------------------
    ("[abwaeg]Drittens die Interessenabwägung: Das geschützte Interesse muss das beeinträchtigte wesentlich überwiegen. "
     "[krit]Abzuwägen sind vor allem die betroffenen Rechtsgüter und der Grad der drohenden Gefahren. [links]Auf der einen "
     "Seite stehen Leben und Gesundheit in akuter Gefahr, [rechts]auf der anderen ein Schloss für dreihundertachtzig Euro und "
     "das Hausrecht für eine Nacht. [ueber]Das Leben wiegt wesentlich schwerer.", PS),
    # --- H 4. Angemessenheit ---------------------------------------------------------------------------------------------------
    ("[angem]Viertens die Angemessenheit nach Satz zwei. [ausn]Sie spielt nur in Ausnahmefällen eine eigene Rolle, etwa "
     "wenn ein Mensch zum bloßen Mittel der Rettung gemacht wird. [angem_ok]Hier ist die Tat angemessen.", PS),
    # --- I 5. subjektives Rechtfertigungselement --------------------------------------------------------------------------------
    ("[subj]Fünftens das subjektive Rechtfertigungselement: [kennt]Korbinian muss die Notstandslage kennen [um]und handeln, "
     "um die Gefahr abzuwenden; so steht es im Wortlaut. [subj_ok]Er will nur nicht erfrieren. [erg34]Die Voraussetzungen des "
     "Paragrafen vierunddreißig liegen vor.", PS),
    # --- J § 904 BGB -----------------------------------------------------------------------------------------------------------
    ("[bgb]Aber Achtung: Für Eingriffe in Sachen gibt es speziellere Notstandsregeln im BGB. [p904]Paragraf neunhundertvier "
     "Satz eins: Der Eigentümer darf die Einwirkung auf seine Sache nicht verbieten, wenn sie zur Abwendung einer "
     "gegenwärtigen Gefahr notwendig [p904b]und der drohende Schaden unverhältnismäßig groß ist.", P),
    ("[aggr]Das ist der Aggressivnotstand: Die Gefahr kommt von außen, hier vom Wetter, [unbet]und Korbinian greift in eine "
     "unbeteiligte fremde Sache ein, die Tür. [verbot]Das Schild hilft Frau Moser deshalb nicht. [p904s2]Satz zwei: Der "
     "Eigentümer kann Ersatz des ihm entstehenden Schadens verlangen.", P),
    ("[mo2]Dann zahlen Sie mir das Schloss also trotzdem.", PS, "Moser"),
    # --- K § 228 BGB -----------------------------------------------------------------------------------------------------------
    ("[p228]Paragraf zweihundertachtundzwanzig regelt den Defensivnotstand: Wer eine fremde Sache beschädigt, um eine durch "
     "sie drohende Gefahr abzuwenden, handelt nicht widerrechtlich, [p228b]wenn das erforderlich ist und der Schaden nicht "
     "außer Verhältnis zur Gefahr steht. [hund]Hier geht die Gefahr von der Sache selbst aus, etwa von einem angreifenden "
     "Hund. [tuer]Die Tür aber bedroht Korbinian nicht.", PS),
    # --- L Spezialität ---------------------------------------------------------------------------------------------------------
    ("[spez]Nach herrschender Meinung gehen diese zivilrechtlichen Notstände bei Eingriffen in Sachen dem Paragrafen "
     "vierunddreißig vor.", PS),
    # --- M Abgrenzung §§ 32, 35 ------------------------------------------------------------------------------------------------
    ("[p32]Zur Abgrenzung: Notwehr scheidet aus, denn es fehlt ein Angriff durch einen Menschen; das Wetter greift nicht an. "
     "[v033]Mehr dazu im Video zum Notwehrschema. [p35]Und scheitert die Abwägung, etwa bei Leben gegen Leben, bleibt nur der "
     "entschuldigende Notstand, Paragraf fünfunddreißig: Die Tat bleibt rechtswidrig, der Täter handelt aber ohne "
     "Schuld. [ht]So der Bundesgerichtshof im Haustyrannen-Fall.", PS),
    # --- N Lösung --------------------------------------------------------------------------------------------------------------
    ("[lsg]Zurück zu Korbinian. [l303]Die Sachbeschädigung an der Tür rechtfertigt "
     "Paragraf neunhundertvier, [l123]den Hausfriedensbruch jedenfalls Paragraf vierunddreißig. [straflos]Korbinian ist straflos. [ersatz]Frau Moser schuldet er aber "
     "Ersatz für das Schloss, Paragraf neunhundertvier Satz zwei.", P),
    ("[ko2]Das Schloss zahle ich gern. Hauptsache, ich bin nicht erfroren.", PS, "Korbinian"),
    # --- O Klausurtipp (Lexi) --------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Prüfe bei Eingriffen in fremde Sachen zuerst die speziellen Notstände des BGB. [k1]Paragraf "
     "zweihundertachtundzwanzig, wenn die Gefahr von der Sache selbst ausgeht, [k2]Paragraf neunhundertvier, wenn du in eine "
     "unbeteiligte Sache eingreifst. [k3]Paragraf vierunddreißig fängt alle übrigen Fälle auf.", PS),
    # --- P Klausurschema -------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für Paragraf vierunddreißig. [s1]Eins, Notstandslage: gegenwärtige Gefahr für ein Rechtsgut. "
     "[s2h]Zwei, Notstandshandlung: geeignet und erforderlich. [s3]Drei, Interessenabwägung: Das geschützte Interesse "
     "überwiegt wesentlich. [s4]Vier, Angemessenheit nach Satz zwei. [s5]Fünf, das subjektive Rechtfertigungselement.", PS),
    # --- Q Merksatz (Lexi) -----------------------------------------------------------------------------------------------------
    ("[merke]Merke: Paragraf vierunddreißig rechtfertigt, wenn das geschützte Interesse wesentlich überwiegt. [m2]Bei Sachen "
     "gehen die Paragrafen zweihundertachtundzwanzig und neunhundertvier BGB vor, [m3]und wer nach Paragraf neunhundertvier "
     "eingreift, muss den Schaden ersetzen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
