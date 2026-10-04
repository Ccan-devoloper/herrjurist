"""Folge 136 · GoA Schema: Wann bekommt der Helfer seine Kosten? (§ 683 BGB) (Mo · Der Fall · Schema).
Beispielfall nach dem Plan-Hook („Du löschst den brennenden Mülleimer deines Nachbarn – und ruinierst dabei deine teure
Jacke“): Frau Huber ist zwei Wochen verreist. Am dritten Tag brennt die Mülltonne vor ihrem Haus, die Flammen drohen auf
ihren Carport überzugreifen. Ihr Nachbar Harald hat keinen Feuerlöscher zur Hand, zieht seine Jacke aus und erstickt
damit die Flammen. Niemand ist verletzt, die Jacke (noch 250 € wert) ist ruiniert. Harald verlangt 250 €; Frau Huber:
„Um Hilfe gebeten habe ich Sie nicht.“
Kern als Schema „Anspruch auf Aufwendungsersatz aus §§ 677, 683 S. 1, 670 BGB“: 1. Geschäftsbesorgung; 2. fremdes
Geschäft, Vermutung des Fremdgeschäftsführungswillens (BGH III ZR 273/16 Rn. 20), auch-fremdes Geschäft; 3. ohne Auftrag
(Wortlaut § 677); 4. Berechtigung § 683 S. 1 (Wortlaut): Interesse und mutmaßlicher Wille (BGH V ZR 102/15 Rn. 8, 12),
§ 679, § 680 (BGH III ZR 54/17 Rn. 48, 55); 5. Rechtsfolge § 670 (Wortlaut): erforderliche Aufwendungen, freiwillige
Vermögensopfer (BGH III ZR 399/14 Rn. 17), risikotypische Begleitschäden (h. M., ohne Aktenzeichen), Höhe 250 €;
Abgrenzung § 684 S. 1 (Verweis Bereicherungsrecht, Folge 073). Ergebnis, Klausurtipp, Schema, Merksatz.
Belege: ../RECHTSSTAND.md. Figuren: Harald (marc), Frau Huber (laura_ruhig); Lexi/Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Harald": "marc", "Huber": "laura_ruhig"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: Frau Huber verreist ---------------------------------------------------------------------------------------
    ("[fall]Frau Huber fährt für zwei Wochen in den Urlaub. [nachbar]Nebenan wohnt ihr Nachbar Harald.", P),
    # --- A2 Fall: die Mülltonne brennt --------------------------------------------------------------------------------------
    ("[feuer]Am dritten Tag brennt die Mülltonne vor ihrem Haus. [carport]Gleich daneben steht ihr Carport.", P),
    ("[ha1]Das Feuer greift gleich auf den Carport über!", P, "Harald"),
    # --- A3 Fall: Harald löscht mit der Jacke ------------------------------------------------------------------------------
    ("[loesch]Einen Feuerlöscher hat Harald nicht zur Hand. Er zieht seine Jacke aus und erstickt damit die Flammen. "
     "[aus]Das Feuer ist aus, verletzt ist niemand. [kaputt]Aber die Jacke ist ruiniert. [wert]Sie war noch "
     "zweihundertfünfzig Euro wert.", P),
    # --- A4 Fall: Frau Huber kommt zurück -----------------------------------------------------------------------------------
    ("[zurueck]Als Frau Huber zurückkommt, erzählt Harald ihr alles.", P),
    ("[ha2]Ihre Mülltonne hat gebrannt. Ich habe das Feuer mit meiner Jacke gelöscht. Bitte zahlen Sie mir "
     "zweihundertfünfzig Euro.", P, "Harald"),
    ("[hu1]Danke! Aber um Hilfe gebeten habe ich Sie nicht.", P, "Huber"),
    ("[frage]Muss Frau Huber die Jacke bezahlen?", PS),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Anspruchsgrundlage und Aufbau ---------------------------------------------------------------------------------
    ("[agl]Die Anspruchsgrundlage ist die Geschäftsführung ohne Auftrag: Paragrafen sechshundertsiebenundsiebzig, "
     "sechshundertdreiundachtzig Satz eins und sechshundertsiebzig. [auf1]Wir prüfen fünf Punkte: Geschäftsbesorgung, "
     "[auf2]fremdes Geschäft, [auf3]ohne Auftrag, [auf4]Berechtigung [auf5]und Rechtsfolge.", PS),
    # --- D 1. Geschäftsbesorgung -----------------------------------------------------------------------------------------
    ("[p1]Erstens: die Geschäftsbesorgung. [p1a]Gemeint ist jede Tätigkeit, auch eine rein tatsächliche. [p1b]Das "
     "Löschen des Feuers genügt.", PS),
    # --- E 2. fremdes Geschäft -------------------------------------------------------------------------------------------
    ("[p2]Zweitens: ein fremdes Geschäft. [p2a]Harald schützt den Carport von Frau Huber, also ihren Rechtskreis. Das "
     "Geschäft ist objektiv fremd. [p2b]Dann vermutet der Bundesgerichtshof den Fremdgeschäftsführungswillen: Harald "
     "wollte für sie handeln. [p2c]Das gilt auch beim auch-fremden Geschäft, wenn es zugleich eigene Interessen berührt, "
     "etwa wenn das Feuer auch sein Haus bedroht hätte.", PS),
    # --- F 3. ohne Auftrag, § 677 (Wortlaut) -----------------------------------------------------------------------------
    ("[p3]Drittens: ohne Auftrag oder sonstige Berechtigung. [p3a]Paragraf sechshundertsiebenundsiebzig erfasst, wer ein "
     "Geschäft für einen anderen besorgt, ohne von ihm beauftragt oder ihm gegenüber sonst dazu berechtigt zu sein. "
     "[p3b]Frau Huber hat Harald um nichts gebeten, das sagt sie ja selbst. [p3c]Einen Vertrag gibt es nicht.", PS),
    # --- G 4. Berechtigung, § 683 S. 1 (Wortlaut) ------------------------------------------------------------------------
    ("[p4]Viertens: die Berechtigung, Paragraf sechshundertdreiundachtzig Satz eins. [p4a]Die Übernahme muss dem "
     "Interesse und dem wirklichen oder mutmaßlichen Willen von Frau Huber entsprechen. [p4b]Im Interesse liegt sie, "
     "wenn sie objektiv nützlich ist: Ein Brand am Carport wird verhindert. [p4c]Ihren wirklichen Willen kennt niemand, "
     "sie ist verreist. [p4d]Dann zählt der mutmaßliche Wille, den sie bei objektiver Beurteilung geäußert hätte. Ohne "
     "andere Anhaltspunkte folgt er dem Interesse. [p4e]Maßgeblich ist der Zeitpunkt der Übernahme.", PS),
    # --- H Sonderregeln §§ 679, 680 --------------------------------------------------------------------------------------
    ("[p679]Zwei Sonderregeln kurz: Ein entgegenstehender Wille ist nach Paragraf sechshundertneunundsiebzig "
     "unbeachtlich, etwa wenn sonst eine Pflicht des Geschäftsherrn im öffentlichen Interesse nicht rechtzeitig erfüllt "
     "würde. [p680]Und wer eine dem Geschäftsherrn drohende dringende Gefahr abwenden will, haftet für Fehler dabei nach Paragraf sechshundertachtzig nur bei Vorsatz und "
     "grober Fahrlässigkeit.", PS),
    # --- I 5. Rechtsfolge, § 670 (Wortlaut) ------------------------------------------------------------------------------
    ("[p5]Fünftens: die Rechtsfolge. Harald kann wie ein Beauftragter Ersatz seiner Aufwendungen verlangen. [p5a]Nach "
     "Paragraf sechshundertsiebzig sind das Aufwendungen, die er den Umständen nach für erforderlich halten darf. "
     "[p5b]Die Jacke durfte er einsetzen: Ein Löscher war nicht da, das Feuer drohte überzugreifen.", PS),
    ("[p5c]Aufwendungen sind nach dem Bundesgerichtshof freiwillige Vermögensopfer. [p5d]Harald hat seine Jacke bewusst "
     "geopfert, um das Feuer zu ersticken. [p5e]Und selbst wenn man das als Schaden sieht: Nach herrschender Meinung "
     "werden auch Schäden ersetzt, in denen sich die typische Gefahr der Hilfe verwirklicht, sogenannte risikotypische "
     "Begleitschäden. [p5f]Ob dabei der Neupreis oder der Zeitwert zählt, kann offenbleiben: Harald verlangt nur den "
     "Wert, den die Jacke noch hatte.", PS),
    # --- J Abgrenzung § 684 S. 1 -----------------------------------------------------------------------------------------
    ("[p684]Und wenn die Berechtigung fehlt? Dann muss der Geschäftsherr nach Paragraf sechshundertvierundachtzig Satz "
     "eins nur herausgeben, was er durch die Geschäftsführung erlangt hat, nach Bereicherungsrecht. [p073]Dazu gibt es "
     "ein eigenes Video.", PS),
    # --- K Ergebnis ------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Harald hat ein Geschäft von Frau Huber berechtigt geführt. [erg2]Sie muss ihm zweihundertfünfzig "
     "Euro für die Jacke zahlen.", PS),
    # --- L Klausurtipp (Lexi) --------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Verwechsle nicht ohne Auftrag mit gegen den Willen. [tipp2]Dass niemand um Hilfe gebeten hat, "
     "gehört zu Punkt drei. [tipp3]Für die Berechtigung zählt allein der wirkliche oder mutmaßliche Wille bei der "
     "Übernahme.", PS),
    # --- M Klausurschema -------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für den Aufwendungsersatz: [k1]Römisch eins: Geschäftsbesorgung. [k2]Römisch zwei: fremdes "
     "Geschäft mit Fremdgeschäftsführungswillen, beim objektiv fremden Geschäft vermutet. [k3]Römisch drei: ohne Auftrag "
     "oder sonstige Berechtigung. [k4]Römisch vier: Berechtigung nach Paragraf sechshundertdreiundachtzig Satz eins, "
     "also Interesse und Wille, oder nach Paragraf sechshundertneunundsiebzig. [k5]Römisch fünf: Ersatz der "
     "erforderlichen Aufwendungen nach Paragraf sechshundertsiebzig, auch risikotypischer Begleitschäden.", PS),
    # --- N Merksatz (Lexi) -----------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer ungefragt im Interesse und mutmaßlichen Willen eines anderen hilft, [mk2]bekommt seine "
     "erforderlichen Aufwendungen ersetzt, [mk3]nach herrschender Meinung auch typische Schäden beim Helfen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
