"""Folge 058 · Heroinspritzen-Fall: Eigenverantwortliche Selbstgefährdung (Mo · Der Fall · Strafrecht/StGB AT · Klassiker-Fall).
Fiktiver Fall nach dem Hook des Themenplans, sehr zurückhaltend dargestellt (keine Spritzen, kein Konsum, keine Drogen- oder
Sterbebilder; nur Päckchen, Warnschild, leere Wohnung, Rettungswagen-Symbol): Achim bringt seinem alten Freund Udo, einem
erfahrenen, nüchternen Konsumenten, wie verabredet ein Päckchen Heroin; Udo setzt sich allein die zu hohe Dosis selbst.
Echter Fall: BGH, Urt. v. 14.2.1984 – 1 StR 808/83, BGHSt 32, 262 (dort besorgte der Angeklagte die Spritzen, das Heroin hatte
der Freund; Verurteilung wegen fahrlässiger Tötung aufgehoben). § 222 StGB (Wortlaut), Kausalität (+), eigenverantwortliche
Selbstgefährdung (BGHSt 32, 262 III.1/2; BGHSt 59, 150 Rn. 71–73; BGHSt 61, 21 Rn. 14); Grenzen: überlegenes Sachwissen
(Variante 1; Warnung, 1 StR 638/99 Rn. 10, 13–15), fehlende Eigenverantwortlichkeit (Variante 2: Rausch; Irrtum/Täuschung,
BGHSt 59, 150 Rn. 73; 2 StR 563/18 Rn. 20), Fremdgefährdung über die Tatherrschaft (BGHSt 49, 34 Rn. 17 f.; 2 StR 563/18
Rn. 20), Ausblick Gisela-Fall (BGHSt 19, 135, zitiert in 6 StR 68/21 Rn. 14); Variante 3: Ingerenz ab Bewusstlosigkeit
(2 StR 563/18 Rn. 19 f.; BGHSt 61, 21 Rn. 16–18; BGHSt 46, 279 Rn. 28), § 13; § 30 Abs. 1 Nr. 3 BtMG (Wortlaut; 1 StR 638/99
Rn. 11 mit BGHSt 37, 179, 182 f.; Leichtfertigkeit BGHSt 46, 279 Rn. 24). Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Namen nie im Genitiv mit -s (Erfahrung 015/047/051/055)."""

P, PS = 0.4, 0.5

STIMMEN = {"Achim": "niklas", "Udo": "helmut"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Freitagabend bei Udo -------------------------------------------------------------------------------------
    ("[fall]Freitagabend in einer kleinen Wohnung. [udo]Udo, Mitte fünfzig, nimmt seit vielen Jahren Heroin und kennt die "
     "Gefahren genau. [achim]Sein alter Freund Achim kommt vorbei. [paeck]Wie verabredet hat er ihm ein Päckchen Heroin besorgt.", 0.3),
    ("[a1]Hier, wie besprochen. Pass auf dich auf.", 0.3, "Achim"),
    ("[u1]Keine Sorge, ich weiß, was ich tue.", 0.4, "Udo"),
    ("[geht]Achim geht nach Hause. [allein]Allein setzt sich Udo die Dosis selbst. Sie ist zu hoch. [morgen]Am nächsten "
     "Morgen kommt für Udo jede Hilfe zu spät.", 0.4),
    ("[frage]Hat Achim seinen Freund fahrlässig getötet? [frage2]Immerhin hat er das Heroin besorgt.", 0.6),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt mit drei Varianten zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Der echte Fall ------------------------------------------------------------------------------------------------
    ("[bgh]Der Fall geht auf ein Urteil des Bundesgerichtshofs vom vierzehnten Februar neunzehnhundertvierundachtzig zurück. "
     "[bgh2]Dort hatte der Angeklagte seinem Freund die Spritzen besorgt, das Heroin hatte der Freund selbst. [bgh3]Das "
     "Landgericht verurteilte wegen fahrlässiger Tötung. Der Bundesgerichtshof hob das auf.", PS),
    # --- D § 222 StGB ----------------------------------------------------------------------------------------------------
    ("[p222]Prüfen wir fahrlässige Tötung, Paragraf zweihundertzweiundzwanzig: Wer durch Fahrlässigkeit den Tod eines "
     "Menschen verursacht. [erfolg]Der Erfolg ist eingetreten, Udo ist tot. [kaus]Denkt man die Übergabe weg, hätte sich "
     "Udo diese Dosis nicht gesetzt. Achim ist kausal. [vorh]Und dass Heroin tödlich sein kann, konnte er "
     "voraussehen. [aber]Trotzdem verneint der Bundesgerichtshof in solchen Fällen eine fahrlässige Tötung.", PS),
    # --- E Eigenverantwortliche Selbstgefährdung --------------------------------------------------------------------------
    ("[eigen]Der Grund ist die eigenverantwortliche Selbstgefährdung. [satz]Eine eigenverantwortlich gewollte und "
     "verwirklichte Selbstgefährdung fällt nicht unter die Tötungsdelikte, wenn sich das bewusst eingegangene Risiko "
     "verwirklicht. [ermoegl]Wer sie nur veranlasst, ermöglicht oder fördert, kann deshalb nicht wegen eines Tötungsdelikts "
     "verurteilt werden.", P),
    ("[warum]Warum? Das Gesetz bestraft nur, wer einen anderen tötet. Selbst die vorsätzliche Teilnahme an einer freien "
     "Selbsttötung ist grundsätzlich straflos. [wider]Dann kann auch die fahrlässige Förderung nicht strafbar sein. "
     "[lehre]Die Lehre ordnet das bei der objektiven Zurechnung ein.", P),
    ("[subs]Udo war erfahren, nüchtern und kannte das Risiko. [selbst]Er hat sich die Dosis selbst gesetzt, er hatte das "
     "Geschehen in der Hand. [ergebnis]Der Tod ist Achim nicht zuzurechnen. Fahrlässige Tötung scheidet aus.", PS),
    # --- F Grenze 1: überlegenes Sachwissen ------------------------------------------------------------------------------
    ("[var1]Variante eins: Achim weiß, dass dieses Heroin ungewöhnlich stark ist. Udo weiß es nicht. [ueber]Dann kann die "
     "Lösung kippen. Die Strafbarkeit kann dort beginnen, wo jemand kraft überlegenen Sachwissens das Risiko besser erfasst als der, der sich selbst gefährdet. "
     "[warn]Warnt Achim ihn aber deutlich, gibt er sein Wissen weiter. Dann bleibt es bei der Selbstgefährdung.", PS),
    # --- G Grenze 2: fehlende Eigenverantwortlichkeit --------------------------------------------------------------------
    ("[var2]Variante zwei: Udo ist schwer betrunken und kann das Risiko nicht mehr abwägen. [rausch]Dann fehlt die "
     "Eigenverantwortlichkeit. [irrtum]Ebenso, wenn er sich über die Gefahr irrt, etwa weil Achim ihn täuscht. [jung]Wie "
     "streng der Maßstab ist, etwa bei Jugendlichen, ist in der Lehre umstritten.", PS),
    # --- H Grenze 3: Fremdgefährdung -------------------------------------------------------------------------------------
    ("[fremd]Und setzt Achim ihm die Dosis eigenhändig, ist das keine Selbstgefährdung mehr, sondern eine Fremdgefährdung. "
     "[herr]Entscheidend ist die Tatherrschaft. Liegt sie nicht allein beim Gefährdeten, sondern auch beim Beteiligten, "
     "begeht dieser eine eigene Tat. [gisela]Ähnlich grenzt der Bundesgerichtshof wie schon im Gisela-Fall die "
     "Tötung auf Verlangen ab: Täter ist, wer das zum Tod führende Geschehen beherrscht.", PS),
    # --- I Variante 3: Unterlassen nach Bewusstlosigkeit -----------------------------------------------------------------
    ("[var3]Variante drei: Achim bleibt. Udo wird bewusstlos. Achim bekommt Angst und geht, ohne den Notruf zu wählen. "
     "[rettung]Mit Hilfe hätte Udo überlebt. [ing]Jetzt hilft die Selbstgefährdung Achim nicht. Wer das Heroin strafbar "
     "überlassen hat, kann Garant aus Ingerenz sein, sobald etwa mit der Bewusstlosigkeit die Gefahr eintritt. [verzicht]Die "
     "Entscheidung von Udo umfasste die Gefahr, nicht den Verzicht auf Rettung. [unterl]Dann kommt Tötung durch "
     "Unterlassen in Betracht, Paragraf dreizehn: fahrlässig, oder mit Vorsatz als Totschlag.", PS),
    # --- J § 30 Abs. 1 Nr. 3 BtMG -----------------------------------------------------------------------------------------
    ("[btm]Und das Betäubungsmittelgesetz? Paragraf dreißig, Absatz eins, Nummer drei bestraft, wer Betäubungsmittel abgibt "
     "und dadurch leichtfertig den Tod verursacht. [immanent]Bei dieser Vorschrift hindert die Selbstgefährdung die Zurechnung nicht. Sie "
     "gehört nach dem Bundesgerichtshof typischerweise zu diesem Tatbestand. [leicht]Achim muss aber leichtfertig gehandelt "
     "haben, also aus besonderem Leichtsinn oder besonderer Gleichgültigkeit. [abgabe]Strafbar ist die unerlaubte Abgabe "
     "ohnehin, nach Paragraf neunundzwanzig. [echt]Im echten Fall spielte die Vorschrift keine Rolle, denn dort hatte der Angeklagte kein Heroin abgegeben.", PS),
    # --- K Klausurtipp (Lexi) ---------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bleib nicht bei der Kausalität stehen. Die Selbstgefährdung prüfst du bei der objektiven Zurechnung. "
     "[tipp2]Frag dort nach Eigenverantwortlichkeit, überlegenem Wissen und Tatherrschaft. [tipp3]Und scheidet Paragraf "
     "zweihundertzweiundzwanzig aus, denk an das Unterlassen und an das Betäubungsmittelgesetz.", PS),
    # --- L Klausurschema --------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema zur fahrlässigen Tötung. [k1]Erstens der Tatbestand: [k1a]Erfolg, Handlung und Kausalität, "
     "[k1b]objektive Sorgfaltspflichtverletzung bei Vorhersehbarkeit, [k1c]dann die objektive Zurechnung. [k1d]Hier fragst "
     "du: Ist die Selbstgefährdung eigenverantwortlich? [k1e]Fehlt überlegenes Wissen? [k1f]Hat das Opfer die "
     "Tatherrschaft? [k2]Zweitens Rechtswidrigkeit, [k3]drittens Schuld. [k4]Danach das Unterlassen ab der "
     "Bewusstlosigkeit [k5]und Paragraf dreißig Betäubungsmittelgesetz.", PS),
    # --- M Merksatz (Lexi) ------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer nur die eigenverantwortliche Selbstgefährdung eines anderen ermöglicht, tötet ihn nicht. [m2]Das "
     "kippt bei überlegenem Wissen, fehlender Eigenverantwortlichkeit oder eigener Tatherrschaft. [m3]Das "
     "Betäubungsmittelgesetz bleibt trotzdem anwendbar.", 1.4),
]
