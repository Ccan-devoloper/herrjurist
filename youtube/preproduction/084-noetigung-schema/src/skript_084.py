"""Folge 084 · Nötigung § 240 Schema: Gewalt, Drohung & Verwerflichkeit (Fr · Klausurpraxis · StGB BT, Format Schema).
Fall nach dem Plan-Hook, gewaltfrei: Gesine ist aus ihrer Mietwohnung ausgezogen; Vermieter Gernot schuldet ihr die Kaution
(1.500 €). Sie hatte sich beim Bauamt über das lockere Balkongeländer beschwert. Gernot: Kaution erst nach Rücknahme der
Beschwerde. Gesine zieht zurück, Gernot überweist. Gernot sachlich, keine Karikatur.
Aufbau: Wortlaut § 240 I → Gewalt kurz (BGH 3 StR 204/20 Rn. 30, Verweis auf Folge 019) → Drohung (OLG Köln 1 ORs 52/24
Rn. 43; BGH 1 StR 162/13 Rn. 64, 65) → Drohung mit Unterlassen (OLG Köln Rn. 43, 46) → empfindliches Übel (BGH 1 StR 162/13
Rn. 68, 70) → Nötigungserfolg, Kausalität, Vorsatz → Rechtswidrigkeit zweistufig: Rechtfertigungsgründe, Wortlaut § 240 II,
„sozial unerträglich“ (BGH 1 StR 162/13 Rn. 74), Mittel-Zweck-Relation und fehlender Zusammenhang (OLG Hamm 7 U 8/21 Rn. 9)
→ Gegenfall Klage auf Miete (OLG Hamm Rn. 9) → Schuld, § 240 IV (ein Satz), Ergebnis → § 253 (ein Satz) → Klausurtipp
(BGH 3 StR 204/20 Rn. 31) → Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben: Gesine, Gernot.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal."""

P, PS = 0.4, 0.9

STIMMEN = {"Gernot": "helmut", "Gesine": "julia"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall ------------------------------------------------------------------------------------------------------------
    ("[fall]Gesine ist aus ihrer Mietwohnung ausgezogen. [kaution]Ihr Vermieter Gernot schuldet ihr noch die Kaution, "
     "eintausendfünfhundert Euro. Forderungen gegen sie hat er keine. [balkon]Kurz vor dem Auszug hatte Gesine sich beim "
     "Bauamt über das lockere Balkongeländer beschwert.", 0.3),
    ("[g1]Ihre Kaution bekommen Sie erst, wenn Sie die Beschwerde beim Bauamt zurückziehen.", 0.3, "Gernot"),
    ("[s1]Aber die Kaution steht mir doch zu!", 0.3, "Gesine"),
    ("[zurueck]Gesine will ihr Geld. Sie zieht die Beschwerde zurück, [ueberw]und Gernot überweist die Kaution. "
     "[frage]Hat Gernot sich strafbar gemacht?", 0.6),
    # --- B Sachverhalt -------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Fall zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Wortlaut § 240 I --------------------------------------------------------------------------------------------------
    ("[pruef]Wir prüfen Nötigung, Paragraf zweihundertvierzig. [mittel0]Das Gesetz verlangt ein Nötigungsmittel: Gewalt oder "
     "Drohung mit einem empfindlichen Übel. [erfolg0]Dadurch muss das Opfer zu einer Handlung, Duldung oder Unterlassung "
     "genötigt werden.", PS),
    # --- D Gewalt (kurz) -----------------------------------------------------------------------------------------------------
    ("[gewalt]Gewalt verlangt eine körperliche Kraftentfaltung des Täters und eine unmittelbare körperliche Zwangswirkung beim "
     "Opfer. [verweis]Die Einzelheiten, etwa zur Sitzblockade, findest du in unserer Folge dazu. [g_nein]Gernot rührt Gesine "
     "nicht an. Gewalt scheidet aus.", PS),
    # --- E Drohung -----------------------------------------------------------------------------------------------------------
    ("[drohung]Bleibt die Drohung. [ddef]Drohen heißt: ein künftiges Übel in Aussicht stellen, auf dessen Eintritt der Täter "
     "Einfluss hat oder zu haben vorgibt. [uebel]Ein Übel ist eine künftige nachteilige Veränderung der Außenwelt. [geld]Hier "
     "bekäme Gesine ihre eintausendfünfhundert Euro nicht. [einfluss]Und darüber entscheidet allein Gernot.", P),
    ("[unterl]Gernot droht nur damit, etwas nicht zu tun, nämlich nicht zu zahlen. [unterl2]Auch mit einem Unterlassen kann "
     "man drohen, nach der Rechtsprechung sogar dann, wenn man zum Handeln gar nicht verpflichtet ist. [pflicht]Erst recht hier: "
     "Gernot muss die Kaution zurückzahlen.", PS),
    # --- F empfindliches Übel ------------------------------------------------------------------------------------------------
    ("[empf]Ist das Übel empfindlich? [edef]Das ist es, wenn der Nachteil so erheblich ist, dass seine Ankündigung die Bedrohte "
     "im Sinne des Täterverlangens motivieren kann. [besonnen]Anders nur, wenn gerade von ihr in ihrer Lage erwartet werden kann, "
     "dass sie der Drohung in besonnener Selbstbehauptung standhält. [e_ja]Solche Besonderheiten hat Gesine nicht. "
     "Eintausendfünfhundert Euro sind ein erheblicher Nachteil: Das Übel ist empfindlich.", PS),
    # --- G Erfolg, Kausalität, Vorsatz ---------------------------------------------------------------------------------------
    ("[erfolg]Der Nötigungserfolg: Gesine nimmt eine Handlung vor, sie zieht die Beschwerde zurück. [kausal]Und zwar gerade "
     "wegen der Drohung, das ist die Kausalität. [vorsatz]Gernot handelt vorsätzlich, er will genau diese Rücknahme. "
     "[tb_ja]Der Tatbestand ist erfüllt.", PS),
    # --- H Rechtswidrigkeit: zwei Stufen, Wortlaut § 240 II ------------------------------------------------------------------
    ("[rw]Jetzt die Rechtswidrigkeit, in zwei Stufen. [rf]Zuerst die allgemeinen Rechtfertigungsgründe: Notwehr oder Notstand "
     "liegen fern. [abs2]Dann Absatz zwei: Rechtswidrig ist die Tat, wenn die Anwendung der Gewalt oder die Androhung des Übels "
     "zu dem angestrebten Zweck als verwerflich anzusehen ist. [sozial]Das ist sie, wenn die Verquickung von Mittel und Zweck "
     "mit den Grundsätzen eines geordneten Zusammenlebens unvereinbar ist, also sozial unerträglich.", P),
    # --- I Mittel-Zweck-Relation ---------------------------------------------------------------------------------------------
    ("[mz]Entscheidend ist also die Mittel-Zweck-Relation. [mittel]Das Mittel: Gernot hält Geld zurück, das er schuldet. "
     "[zweck]Der Zweck: Gesine soll ihre Beschwerde bei der Behörde zurückziehen. [konnex]Beides hat nichts miteinander zu tun. "
     "Fehlt der Zusammenhang zwischen angedrohtem Übel und Zweck, spricht das für die Verwerflichkeit. [inkon]Die Lehre spricht "
     "von Inkonnexität. [v_ja]Gernot benutzt fremdes Geld als Druckmittel gegen eine Beschwerde. Das ist verwerflich.", P),
    ("[gegen]Gegenfall: Gesine schuldet noch eine Monatsmiete, und Gernot droht mit einer Klage, wenn sie nicht zahlt. "
     "[gegen2]Hier hängen Mittel und Zweck zusammen, und Gernot hat einen Anspruch. Verwerflich ist das nicht.", PS),
    # --- J Schuld, Absatz vier, Ergebnis, Erpressung -------------------------------------------------------------------------
    ("[schuld]Gernot handelt auch schuldhaft. [abs4]Ein besonders schwerer Fall nach Absatz vier, etwa der Missbrauch einer "
     "Stellung als Amtsträger, liegt nicht vor. [erg]Gernot ist wegen Nötigung strafbar.", P),
    ("[erpr]Eine Erpressung, Paragraf zweihundertdreiundfünfzig, scheidet aus: [erpr2]Die Rücknahme der Beschwerde ist kein "
     "Vermögensnachteil für Gesine, [erpr3]und behalten will Gernot die Kaution gar nicht, ihm fehlt die Bereicherungsabsicht.", PS),
    # --- K Klausurtipp (Lexi) ------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Bei der Nötigung prüfst du die Rechtswidrigkeit in zwei Stufen. [tipp2]Erst die allgemeinen "
     "Rechtfertigungsgründe. [tipp3]Greift keiner, stellst du die Verwerflichkeit nach Absatz zwei positiv fest. [tipp4]Denn das "
     "Nötigungsmittel allein zeigt die Verwerflichkeit noch nicht an.", PS),
    # --- L Klausurschema -----------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema. [k1]Römisch eins, Tatbestand. Objektiv: [k1a]das Nötigungsmittel, also Gewalt oder Drohung mit "
     "einem empfindlichen Übel, [k1b]der Nötigungserfolg [k1c]und die Kausalität. [k2]Subjektiv: Vorsatz. [k3]Römisch zwei, "
     "Rechtswidrigkeit: [k3a]allgemeine Rechtfertigungsgründe, [k3b]dann die Verwerflichkeit nach Absatz zwei. [k4]Römisch drei, "
     "Schuld. [k5]Römisch vier: ein besonders schwerer Fall nach Absatz vier.", PS),
    # --- M Merksatz (Lexi) ---------------------------------------------------------------------------------------------------
    ("[merke]Merke: Nötigung braucht Gewalt oder eine Drohung mit einem empfindlichen Übel. [m2]Auch die Drohung, nicht zu "
     "zahlen, genügt. [m3]Rechtswidrig ist sie nur, wenn das Mittel zum angestrebten Zweck verwerflich ist.", 1.4),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    doppelt = {m for m in marken if marken.count(m) > 1}
    assert not doppelt, f"Marken doppelt: {doppelt}"
    zeichen = sum(len(re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", zeichen, "Zeichen")
