"""Folge 038 · Körperverletzung § 223 StGB: Misshandlung & Gesundheitsschädigung (Examenswissen, Format Schema).
Fall in einer Wohngemeinschaft: Sigrid schneidet ihrer auf dem Sofa eingeschlafenen Mitbewohnerin Katrin heimlich die
langen Haare ab. Wortlaut § 223 I, II; körperliche Misshandlung (BGH 3 StR 354/16 Rn. 4; Haare: BGH 4 StR 634/07 Rn. 3),
Bagatellgrenze (Ohrfeige/Stups), Gesundheitsschädigung (BGH 4 StR 168/13 Rn. 13: Abführmittel; psychische Folgen
nur bei pathologischem, somatisch-objektivierbarem Zustand, Rn. 13 f.), ärztlicher Heileingriff (Rspr.: BGH 4 StR 549/06
Rn. 22; Lehre als Gegenansicht), Versuch § 223 II, Strafantrag §§ 230, 77b; Klausurtipp (Schere: BGH 4 StR 634/07 Rn. 4),
Schema, Merksatz. Belege je Aussage: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.7

STIMMEN = {"Katrin": "lucy", "Sigrid": "hilde", "Lindner": "william"}  # Lexi spricht mit der Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Wohngemeinschaft am Sonntagabend ------------------------------------------------------------------------
    ("[fall]Sonntagabend in einer Wohngemeinschaft. [katrin]Katrin ist auf dem Sofa eingeschlafen. [sigrid]Ihre "
     "Mitbewohnerin Sigrid ärgert sich seit Wochen über Katrins lange Haare im Abfluss. [schere]Sie holt eine Schere "
     "[schnitt]und schneidet Katrin die langen Haare heimlich ab. [wach]Katrin wacht auf und greift sich an den Kopf.", 0.3),
    ("[k1]Meine Haare! Das ist Körperverletzung!", 0.3, "Katrin"),
    ("[s1]Das hat doch gar nicht wehgetan.", 0.4, "Sigrid"),
    ("[frage]Wer hat recht? [frage2]Wann ist eine Person körperlich misshandelt, und wann an der Gesundheit geschädigt?", 0.6),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall mit allen Varianten zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 223 ------------------------------------------------------------------------------------------------
    ("[p223]Maßstab ist Paragraf zweihundertdreiundzwanzig. [p223w]Absatz eins: Wer eine andere Person körperlich "
     "misshandelt oder an der Gesundheit schädigt, wird mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe "
     "bestraft. [abs2]Absatz zwei: Der Versuch ist strafbar. [andere]Opfer muss eine andere Person sein; wer sich selbst "
     "verletzt, fällt nicht darunter. [zwei]Der Tatbestand hat zwei Varianten: [vm]die körperliche Misshandlung [vg]und die "
     "Gesundheitsschädigung. [eine]Eine genügt, oft liegen beide vor.", PS),
    # --- D Körperliche Misshandlung --------------------------------------------------------------------------------------
    ("[mh]Erste Variante: körperliche Misshandlung. [mhdef]Nach dem Bundesgerichtshof ist das eine üble und unangemessene "
     "Behandlung, die das körperliche Wohlbefinden [unvers]oder die körperliche Unversehrtheit [nnu]nicht nur unerheblich "
     "beeinträchtigt. [schmerz]Schmerz ist also nicht nötig. [haare]Katrin hat im Schlaf nichts gespürt. Aber ihre langen "
     "Haare sind ab, ihr Aussehen ist deutlich verändert. [unv_ok]Die körperliche Unversehrtheit ist mehr als nur "
     "unerheblich beeinträchtigt. [dread]Auch der Bundesgerichtshof hat das Abschneiden von Haaren als Körperverletzung "
     "bestätigt. [mh_ok]Sigrids Einwand zieht also nicht: Sie hat Katrin körperlich misshandelt.", PS),
    # --- E Bagatellgrenze: Ohrfeige und Stups ----------------------------------------------------------------------------
    ("[bag]Wo liegt die Grenze? [bag2]Nicht jeder vorsätzliche Schlag oder Stoß ist eine Körperverletzung, betont der "
     "Bundesgerichtshof. [v1]Variante eins: Katrin gibt Sigrid eine kräftige Ohrfeige. [ohr]Die Wange brennt und rötet "
     "sich. Das Wohlbefinden ist mehr als nur unerheblich beeinträchtigt, [ohr_ok]also eine Misshandlung. [stups]Stupst "
     "Katrin Sigrid dagegen nur leicht an die Schulter, [stups_no]bleibt das unter der Schwelle.", PS),
    # --- F Gesundheitsschädigung -----------------------------------------------------------------------------------------
    ("[gs]Zweite Variante: die Gesundheitsschädigung. [gsdef]Das ist jedes Hervorrufen oder Steigern eines Zustands, der "
     "vom Normalzustand der körperlichen Funktionen nachteilig abweicht. [art]Auf welche Art das geschieht, ist gleich. "
     "[v2]Variante zwei: Sigrid rührt heimlich ein Abführmittel in Katrins Tee. [durch]Katrin bekommt Durchfall und "
     "Bauchkrämpfe. [gs_ok]Ihre Körperfunktionen weichen nachteilig vom Normalzustand ab: eine Gesundheitsschädigung. "
     "[beide]Die Krämpfe sind zugleich eine Misshandlung.", PS),
    # --- G Psychische Folgen ---------------------------------------------------------------------------------------------
    ("[psy]Und psychische Folgen? [v3]Variante drei: Katrin ist über ihre Haare so aufgewühlt, dass sie zwei Nächte "
     "schlecht schläft. [rein]Rein psychische Empfindungen genügen nach dem Bundesgerichtshof nicht, [aufr]auch keine "
     "bloße Aufregung oder Angst. [somat]Erst ein pathologischer, körperlich objektivierbarer Zustand ist eine "
     "Gesundheitsschädigung, [schlaf]etwa wenn sich das Schlafverhalten dauerhaft ändert. [v3_no]Zwei unruhige Nächte "
     "reichen dafür nicht.", PS),
    # --- H Ärztlicher Heileingriff ---------------------------------------------------------------------------------------
    ("[arzt]Ein Klassiker ist der ärztliche Heileingriff. [v4]Variante vier: Hautarzt Doktor Lindner hat Katrin über "
     "Ablauf und Risiken aufgeklärt und will ihr ein verdächtiges Muttermal entfernen.", 0.3),
    ("[l1]Darf ich das Muttermal jetzt entfernen?", 0.3, "Lindner"),
    ("[k2]Ja, ich bin einverstanden.", 0.4, "Katrin"),
    ("[fach]Er entfernt es fachgerecht. [rspr]Nach der Rechtsprechung erfüllt der ärztliche Heileingriff den Tatbestand der Körperverletzung. [einw]Rechtmäßig "
     "ist er grundsätzlich nur mit wirksamer Einwilligung, [aufkl]und die setzt eine ordnungsgemäße Aufklärung voraus. [lehre]Teile der "
     "Lehre sehen das anders: Ein ärztlich angezeigter und kunstgerecht ausgeführter Eingriff sei schon keine "
     "Körperverletzung. [v4_erg]Hier kommen beide Ansichten zum selben Ergebnis: Doktor Lindner ist nicht strafbar.", PS),
    # --- I Versuch -------------------------------------------------------------------------------------------------------
    ("[vers]Bleibt der Versuch. [v5]Variante fünf: Sigrid setzt die Schere schon an, da wacht Katrin auf und hält ihre "
     "Haare fest. [tatent]Sigrid wollte die Haare abschneiden [ansetz]und hat nach ihrer Vorstellung unmittelbar "
     "angesetzt. [vers_ok]Nach Absatz zwei ist auch der Versuch strafbar.", PS),
    # --- J Ergebnis und Strafantrag --------------------------------------------------------------------------------------
    ("[erg]Zurück zum Grundfall: [rw]Rechtfertigungs- oder Entschuldigungsgründe sind nicht ersichtlich. [erg2]Sigrid hat "
     "sich wegen Körperverletzung strafbar gemacht. [p230]Verfolgt wird die Tat aber nur auf Antrag, Paragraf "
     "zweihundertdreißig, [oeff]außer die Strafverfolgungsbehörde bejaht ein besonderes öffentliches Interesse. [frist]Den "
     "Antrag muss Katrin binnen drei Monaten stellen, [kennt]ab Kenntnis von Tat und Täterin.", PS),
    # --- K Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Definiere beide Varianten und subsumiere getrennt. [tipp2]Und greif bei der Schere nicht "
     "vorschnell zu Paragraf zweihundertvierundzwanzig: [tipp3]Ein Gegenstand zum Haareabschneiden ist nach dem "
     "Bundesgerichtshof in der Regel kein gefährliches Werkzeug.", PS),
    # --- L Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k_i]Römisch eins: Tatbestand. [k1a]Objektiv: eine andere Person, [k1b]körperliche "
     "Misshandlung [k1c]oder Gesundheitsschädigung, [k1d]dazu Kausalität und objektive Zurechnung. [k1e]Subjektiv: Vorsatz. "
     "[k_ii]Römisch zwei: Rechtswidrigkeit, beim Arzt vor allem die Einwilligung. [k_iii]Römisch drei: Schuld. "
     "[k_iv]Römisch vier: Strafantrag. [k_v]Scheitert die Vollendung, prüfst du den Versuch nach Absatz zwei.", PS),
    # --- M Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Misshandlung braucht keinen Schmerz, aber eine mehr als nur unerhebliche körperliche Beeinträchtigung. "
     "[m2]Gesundheitsschädigung heißt: ein nachteilig abweichender körperlicher Zustand. [m3]Psychische Folgen zählen nur, "
     "wenn sie krankhaft und körperlich objektivierbar sind.", 1.3),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
