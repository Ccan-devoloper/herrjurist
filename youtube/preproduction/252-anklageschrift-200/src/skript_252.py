"""Folge 252 · Anklageschrift § 200 StPO: Aufbau Schritt für Schritt (Fr · 2. Examen · StPO-Praxis · Schema).
Beispielfall nach dem Plan-Hook („Du hast den hinreichenden Tatverdacht bejaht und musst jetzt die Anklage zum
Schöffengericht schreiben“): Referendar Hiller (Station Staatsanwaltschaft Ahornstadt, erfunden) bekommt von seinem
Ausbilder, Oberstaatsanwalt Endres, den Auftrag, die Anklage zu entwerfen. In der Akte: Am 10.3.2026 gegen 14 Uhr steigt
jemand durch das offene Küchenfenster in die Erdgeschosswohnung von Frau Probst (niemand zu Hause), Schmuck für 2.400 €
verschwindet; Fingerabdrücke von Herrn Unger am Fensterrahmen, am nächsten Tag verkauft er einen Ring daraus in einem
Ankaufsladen. Unger (41, nicht vorbestraft) schweigt, er hat einen Verteidiger. Keine Gewalt gegen Personen.
Ablauf: Fall → Frage → Sachverhalt → § 200 Abs. 1 (Wortlautkarte) → § 200 Abs. 2 (Wortlautkarte) und Inhalt nach
Nr. 110 RiStBV → Schritt 1 Kopf/Personalien/Verteidiger (§ 140 Abs. 1 Nr. 1, 2 StPO) → Schritt 2 Anklagesatz (Einleitung,
Zeit/Ort, gesetzliche Merkmale, konkreter Tatvorwurf, Paragrafenkette) → Schritt 3 Beweismittel (§ 200 Abs. 1 S. 3,
Nr. 111 RiStBV) → Schritt 4 wesentliches Ergebnis → Schritt 5 Antrag (§ 199 Abs. 2, § 207 Abs. 1 StPO, Nr. 110 Abs. 3
RiStBV; Schöffengericht §§ 24, 25, 28 GVG, Verweis Folge 114) → zwei typische Fehler (Zeit/Ort fehlt; Tat zu ungenau,
Umgrenzungsfunktion, BGH StB 39/21 Rn. 17 f.) → Klausurtipp (Nr. 110 Abs. 2 lit. c RiStBV) → Schema → Merksatz.
Belege: ../RECHTSSTAND.md. Namen mit eindeutig deutscher Aussprache, in früheren Folgen nicht vergeben (Liste des
Koordinators, namen_reserviert.txt, grep über youtube/): Hiller, Endres, Unger, Probst (gesprochen), Dominik und Brack
(nur auf der Mustertafel). Stimmen nur aus dem Pool: Hiller niklas (Mann, jung), Endres helmut (Mann, älter); ela_froh und
julia nicht verwendet. Lexi = Erzählerin Carla.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau
einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Hiller": "niklas", "Endres": "helmut"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A Fall: Büro der Staatsanwaltschaft ------------------------------------------------------------------------
    ("[fall]Montagmorgen bei der Staatsanwaltschaft Ahornstadt. [hiller]Referendar Hiller sitzt über einer Akte. "
     "[endres]Da kommt Oberstaatsanwalt Endres herein, sein Ausbilder.", 0.3),
    ("[e1]Den hinreichenden Tatverdacht haben Sie bejaht. Jetzt schreiben Sie die Anklage zum Schöffengericht.", 0.3, "Endres"),
    ("[h1]Gern. Aber womit fange ich an, und was gehört alles hinein?", 0.4, "Hiller"),
    # --- B Fall: was in der Akte steht ------------------------------------------------------------------------------
    ("[akte]In der Akte: [tag]Am zehnten März zweitausendsechsundzwanzig, gegen vierzehn Uhr, [fenster]steigt jemand durch "
     "das offene Küchenfenster in die Erdgeschosswohnung von Frau Probst, in der sie lebt. [schmuck]Aus der Kommode "
     "verschwindet ihr Schmuck im Wert von zweitausendvierhundert Euro. [finger]Am Fensterrahmen findet die Polizei "
     "Fingerabdrücke von Herrn Unger. [beleg]Am nächsten Tag verkauft er einen Ring daraus in einem Ankaufsladen, "
     "mit seinem Ausweis. [schweigt]Unger schweigt; er hat einen Verteidiger.", 0.3),
    ("[frage]Was gehört in die Anklageschrift, und in welcher Reihenfolge?", 0.5),
    # --- C Sachverhalt ----------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- D § 200 Abs. 1 StPO (Wortlautkarte) --------------------------------------------------------------------------
    ("[p200]Den Inhalt regelt Paragraf zweihundert der Strafprozessordnung. [abs1]Nach Absatz eins bezeichnet die "
     "Anklageschrift [ang]den Angeschuldigten, [tat]die Tat, die ihm zur Last gelegt wird, [zeit]Zeit und Ort ihrer "
     "Begehung, [merk]die gesetzlichen Merkmale der Straftat [vorschr]und die anzuwendenden Strafvorschriften. "
     "[asatz]Das Gesetz nennt das den Anklagesatz. [s2]Außerdem gibt sie [bew]die Beweismittel an, [ger]das Gericht der "
     "Hauptverhandlung [vert]und den Verteidiger.", P),
    # --- E § 200 Abs. 2 StPO (Wortlautkarte) und Nr. 110 RiStBV -------------------------------------------------------
    ("[abs2]Absatz zwei verlangt zusätzlich das wesentliche Ergebnis der Ermittlungen. [ausn]Davon kann nur abgesehen "
     "werden, wenn Anklage beim Strafrichter erhoben wird. [hier]Hiller klagt zum Schöffengericht an, also gehört es "
     "hinein. [rist]Was im Einzelnen hineingehört, zählen die Richtlinien für das Strafverfahren in Nummer hundertzehn "
     "auf, [klar]und alles muss klar, übersichtlich und vor allem für den Angeschuldigten verständlich sein. [land]Die "
     "genaue Form unterscheidet sich von Land zu Land; maßgeblich sind die Hinweise deines Prüfungsamts.", PS),
    # --- F Schritt 1: Kopf, Personalien, Verteidiger ----------------------------------------------------------------
    ("[kopf]Schritt eins: der Kopf. [kopf1]Oben stehen die Staatsanwaltschaft, das Aktenzeichen und das Datum, "
     "darunter die Überschrift Anklageschrift. [pers]Dann die Personalien des Angeschuldigten: Name, Geburtstag und "
     "Geburtsort, Beruf, Anschrift, Familienstand und Staatsangehörigkeit. [vertr]Darunter der Verteidiger. "
     "[notw]Bei Unger ist die Verteidigung ohnehin notwendig: Ihm wird ein Verbrechen zur Last gelegt, und verhandelt "
     "wird vor dem Schöffengericht.", PS),
    # --- G Schritt 2: Anklagesatz – Einleitung und gesetzliche Merkmale ---------------------------------------------
    ("[as]Schritt zwei, das Herzstück: der Anklagesatz. [einl]Er beginnt mit der Einleitung: Der Angeschuldigte wird "
     "angeklagt, [einl2]am zehnten März zweitausendsechsundzwanzig in Ahornstadt [abstr]eine fremde bewegliche Sache "
     "einem anderen in der Absicht weggenommen zu haben, sie sich rechtswidrig zuzueignen, [abstr2]wobei er zur "
     "Ausführung der Tat in eine dauerhaft genutzte Privatwohnung einstieg. [abstr3]Das sind die gesetzlichen Merkmale, "
     "auf Unger bezogen.", P),
    # --- H Schritt 2: konkreter Tatvorwurf und Paragrafenkette ------------------------------------------------------
    ("[konkr]Dann folgt der konkrete Tatvorwurf: [k1]Gegen vierzehn Uhr stieg der Angeschuldigte durch das offene "
     "Küchenfenster in die Erdgeschosswohnung der Zeugin Probst im Lindenweg vier ein, in der sie lebt. [k2]Er nahm aus "
     "der Kommode Schmuck im Wert von zweitausendvierhundert Euro [k3]und verließ damit die Wohnung, um ihn für sich zu "
     "behalten. [kette]Am Ende die Paragrafenkette: [kette2]Verbrechen des Wohnungseinbruchdiebstahls, strafbar nach "
     "Paragraf zweihundertzweiundvierzig Absatz eins und Paragraf zweihundertvierundvierzig Absatz eins Nummer drei, "
     "Absatz vier des Strafgesetzbuchs.", PS),
    # --- I Schritt 3: Beweismittel ----------------------------------------------------------------------------------
    ("[bm]Schritt drei: die Beweismittel. [bm1]Aufgeführt wird nur, was wesentlich ist. [bm2]Bei "
     "Zeugen genügt der Wohn- oder Aufenthaltsort, nicht die volle Anschrift. [bm3]Hier sind das die Zeugin Probst, "
     "[bm4]das Gutachten zu den Fingerabdrücken, [bm5]der Ankaufsbeleg [bm6]und die Lichtbilder vom Tatort.", PS),
    # --- J Schritt 4: wesentliches Ergebnis der Ermittlungen --------------------------------------------------------
    ("[we]Schritt vier: das wesentliche Ergebnis der Ermittlungen. [we1]Es schildert knapp die Person, das Geschehen "
     "und die Beweislage: [we2]Unger schweigt, aber die Fingerabdrücke am Fensterrahmen [we3]und der Verkauf des Rings "
     "am nächsten Tag belasten ihn. [we4]Hier, nicht im Anklagesatz, steht, warum die Beweise tragen. [we5]Ein zweites "
     "Gutachten ist es aber nicht.", PS),
    # --- K Schritt 5: Antrag und Gericht ----------------------------------------------------------------------------
    ("[an]Schritt fünf: der Antrag. [an1]Die Anklageschrift enthält den Antrag, das Hauptverfahren zu eröffnen, "
     "[an2]und nennt das Gericht: Hiller beantragt, die Anklage zur Hauptverhandlung vor dem Amtsgericht Ahornstadt, Schöffengericht, "
     "zuzulassen. [zust]Warum Schöffengericht? [z1]Der Strafrichter entscheidet nur bei Vergehen, und das hier ist ein "
     "Verbrechen. [z2]Mehr als vier Jahre Freiheitsstrafe sind nicht zu erwarten, also bleibt es beim Amtsgericht. "
     "[f114]Die Zuständigkeit im Einzelnen zeigt Folge hundertvierzehn.", P),
    ("[e2]Gut. Jetzt lese ich gegen: Ist die Tat unverwechselbar beschrieben?", 0.4, "Endres"),
    # --- L Typische Fehler -------------------------------------------------------------------------------------------
    ("[fehler]Zwei Fehler sieht man in Klausuren immer wieder. [fe1]Erstens: Im Anklagesatz fehlen Tatzeit oder Tatort, "
     "obwohl Paragraf zweihundert sie ausdrücklich verlangt. [fe2]Zweitens: Die Tat ist zu ungenau beschrieben, "
     "[fe3]etwa so: Unger hat im Frühjahr in Ahornstadt Schmuck gestohlen. [umgr]Die Anklage muss die Tat aber als "
     "geschichtlichen Vorgang unverwechselbar kennzeichnen. [umgr2]Nur dann steht fest, worüber das Gericht urteilen "
     "soll und wie weit später der Strafklageverbrauch reicht. [unw]Fehlt diese Umgrenzung, ist die Anklage nach dem "
     "Bundesgerichtshof unwirksam, und das Verfahren ist einzustellen.", PS),
    # --- M Klausurtipp (Lexi) ----------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Schreib den Anklagesatz erst, wenn dein Gutachten steht. [tipp1]Bei mehreren "
     "Gesetzesverletzungen gibt er auch an, ob Tateinheit oder Tatmehrheit vorliegt. [tipp2]Und prüfe am Ende: Passen "
     "Paragrafenkette, Gericht und Antrag zu deinem Gutachten?", PS),
    # --- N Schema ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Aufbau auf einen Blick. [s1]Erstens: Kopf, Personalien und Verteidiger. [s2t]Zweitens: der Anklagesatz, "
     "[s2a]mit Zeit und Ort und den gesetzlichen Merkmalen, [s2b]dem konkreten Tatvorwurf [s2c]und der Paragrafenkette. "
     "[s3]Drittens: die Beweismittel. [s4]Viertens: das wesentliche Ergebnis der Ermittlungen. [s5]Fünftens: der Antrag "
     "auf Eröffnung vor dem zuständigen Gericht.", PS),
    # --- O Merksatz (Lexi) ------------------------------------------------------------------------------------------
    ("[merke]Merke: Der Anklagesatz umgrenzt die Tat: wer, wann, wo, was und nach welcher Vorschrift. [m2]Danach "
     "folgen Beweismittel, wesentliches Ergebnis und der Antrag auf Eröffnung.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
