"""Folge 242 · Vormerkung §§ 883 ff. BGB: Schutz vor dem Doppelverkauf (Mi · Examenswissen · Sachenrecht, Format Schema).
Beispielfall nach dem Plan-Hook („Nach dem Notartermin verkauft der Verkäufer das Haus noch einmal an einen Meistbietenden.“):
Mats kauft von Herrn Stenzel ein Haus für 420.000 €. Beim Notar (ohne Namen, kein echter Ort) unterschreiben beide den
Kaufvertrag, Herr Stenzel bewilligt eine Vormerkung für Mats; zwei Wochen später ist sie eingetragen. Dann bietet Frau
Ostendorf 470.000 €; Herr Stenzel verkauft und übereignet ihr das Haus, sie wird als Eigentümerin eingetragen.
Schema: Problem (Eigentum erst mit Eintragung, §§ 873, 925; Verweis 145) → § 883 Abs. 1 (Wortlautkarte) mit vier
Voraussetzungen: 1. zu sichernder Anspruch (Akzessorietät, BGH V ZR 176/22 Rn. 31), 2. Bewilligung (§ 885 Abs. 1,
Wortlautkarte) oder einstweilige Verfügung, 3. Eintragung, 4. Berechtigung (gutgläubiger Ersterwerb nur bei bestehendem
Anspruch, V ZR 91/21 Rn. 23) → Wirkung § 883 Abs. 2 (Wortlautkarte, relative Unwirksamkeit, V ZR 240/09 Rn. 7, 10) →
Durchsetzung § 888 Abs. 1 (Wortlautkarte; Zweiterwerberin bleibt eingetragen bis zur Zustimmung, V ZR 240/09 Rn. 7, 13)
→ Ergebnis, § 106 Abs. 1 InsO (IX ZR 70/20 Rn. 34) → Klausurtipp (Lexi, § 888 Abs. 1; Einwendungen V ZR 240/09 Rn. 8)
→ Schema → Merksatz. Belege: ../RECHTSSTAND.md.
Figuren: Mats (niklas), Herr Stenzel (helmut), Frau Ostendorf (ela_froh); Lexi/Erzählerin Carla.
Namen nie im Genitiv. Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede.
[marke] = Cue; jede Marke genau einmal. Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Mats": "niklas", "Stenzel": "helmut", "Ostendorf": "ela_froh"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: der Notartermin ----------------------------------------------------------------------------------------
    ("[fall]Nach dem Notartermin verkauft der Verkäufer das Haus noch einmal, an einen Meistbietenden. [mats]So kann es "
     "Mats gehen. [haus]Er kauft von Herrn Stenzel ein Haus für vierhundertzwanzigtausend Euro. [notar]Beim Notar "
     "unterschreiben beide den Kaufvertrag, [bew]und Herr Stenzel bewilligt eine Vormerkung für Mats.", P),
    ("[st1]Glückwunsch! Bald gehört das Haus Ihnen.", P, "Stenzel"),
    ("[ma1]Dann warte ich jetzt nur noch auf das Grundbuch.", P, "Mats"),
    ("[eintr]Zwei Wochen später steht die Vormerkung im Grundbuch.", P),
    # --- A2 Fall: vor dem Haus ---------------------------------------------------------------------------------------------
    ("[west]Dann meldet sich Frau Ostendorf bei Herrn Stenzel.", P),
    ("[we1]Ich zahle Ihnen vierhundertsiebzigtausend Euro für das Haus!", P, "Ostendorf"),
    ("[st2]Da sage ich nicht nein.", P, "Stenzel"),
    ("[zweit]Herr Stenzel verkauft ihr das Haus und erklärt die Auflassung, [weg]und Frau Ostendorf wird als Eigentümerin "
     "ins Grundbuch eingetragen.", P),
    ("[frage]Hat Mats das Haus verloren? [frage2]Und was bringt ihm die Vormerkung?", PS),
    # --- B Sachverhalt ------------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C Das Problem ------------------------------------------------------------------------------------------------------
    ("[prob]Das Problem: Eigentum am Grundstück gibt es erst mit der Eintragung, Paragrafen achthundertdreiundsiebzig und "
     "neunhundertfünfundzwanzig. [prob2]Bis dahin bleibt Herr Stenzel Eigentümer und kann noch einmal verfügen. "
     "[prob3]Ohne Vormerkung wäre der Erwerb von Frau Ostendorf voll wirksam, und Mats hätte nur noch Ansprüche gegen "
     "Herrn Stenzel, etwa auf Schadensersatz. [prob4]Mehr zu den drei Schritten im Video zum Hauskauf. [loes]Für die "
     "Zwischenzeit gibt es die Vormerkung.", PS),
    # --- D § 883 Abs. 1 (Wortlaut), vier Voraussetzungen ---------------------------------------------------------------------
    ("[norm]Paragraf achthundertdreiundachtzig Absatz eins: [w883]Zur Sicherung des Anspruchs auf Einräumung oder "
     "Aufhebung eines Rechts an einem Grundstück kann eine Vormerkung in das Grundbuch eingetragen werden. "
     "[vier]Zusammen mit Paragraf achthundertfünfundachtzig ergeben sich vier Voraussetzungen: [v1]ein zu sichernder "
     "Anspruch, [v2]eine Bewilligung oder einstweilige Verfügung, [v3]die Eintragung [v4]und die Berechtigung des "
     "Bewilligenden.", PS),
    # --- E 1. Anspruch, Akzessorietät -------------------------------------------------------------------------------------------
    ("[a1]Erstens der zu sichernde Anspruch. Er muss auf eine dingliche Rechtsänderung gerichtet sein. [a2]Mats hat aus "
     "dem Kaufvertrag nach Paragraf vierhundertdreiunddreißig einen Anspruch auf Übereignung des Hauses. [a3]Der Vertrag "
     "ist notariell beurkundet, also wirksam. [akz]Wichtig ist die Akzessorietät: Nach dem Bundesgerichtshof ist die "
     "Vormerkung ein streng akzessorisches Sicherungsmittel. [akz2]Sie erlischt, wenn der gesicherte Anspruch nicht mehr "
     "besteht. [kuenft]Gesichert werden können auch künftige oder bedingte Ansprüche.", P),
    # --- F 2. Bewilligung, § 885 Abs. 1 (Wortlaut) -------------------------------------------------------------------------------
    ("[b1]Zweitens die Bewilligung. [w885]Nach Paragraf achthundertfünfundachtzig Absatz eins erfolgt die Eintragung auf "
     "Grund einer einstweiligen Verfügung oder auf Grund der Bewilligung desjenigen, dessen Grundstück von der Vormerkung "
     "betroffen wird. [b2]Hier hat Herr Stenzel beim Notar bewilligt. [evf]Weigert sich ein Verkäufer, hilft die "
     "einstweilige Verfügung. [evf2]Eine Gefährdung des Anspruchs muss man dafür nicht glaubhaft machen.", P),
    # --- G 3. Eintragung, 4. Berechtigung -----------------------------------------------------------------------------------------
    ("[e1]Drittens die Eintragung. [e2]Die Vormerkung für Mats steht im Grundbuch, und zwar schon vor der Übereignung an "
     "Frau Ostendorf. [ber]Viertens die Berechtigung: Herr Stenzel muss Eigentümer sein. [ber2]Das ist er, er steht zu Recht im "
     "Grundbuch. [gut]Stünde er nur zu Unrecht im Grundbuch, könnte Mats die Vormerkung nach dem Bundesgerichtshof gutgläubig erwerben, "
     "entsprechend Paragraf achthundertzweiundneunzig, [gut2]aber nur, wenn der gesicherte Anspruch wirklich besteht. "
     "[zw]Zwischenergebnis: Mats hat eine wirksame Vormerkung.", PS),
    # --- H Wirkung § 883 Abs. 2 (Wortlaut) ------------------------------------------------------------------------------------------
    ("[wirk]Und was bewirkt sie? [w8832]Paragraf achthundertdreiundachtzig Absatz zwei: Eine Verfügung, die nach der "
     "Eintragung der Vormerkung über das Grundstück oder das Recht getroffen wird, ist insoweit unwirksam, als sie den "
     "Anspruch vereiteln oder beeinträchtigen würde. [verf]Der zweite Kaufvertrag ist keine Verfügung, er bleibt "
     "wirksam. [verf2]Verfügung ist die Übereignung an Frau Ostendorf, und sie vereitelt den Anspruch von Mats. "
     "[rel]Unwirksam ist sie aber nur relativ, also nur Mats gegenüber. [rel2]Allen anderen gegenüber ist Frau Ostendorf "
     "Eigentümerin.", PS),
    # --- I Durchsetzung § 888 Abs. 1 (Wortlaut) ------------------------------------------------------------------------------------
    ("[durch]Wie kommt Mats nun ins Grundbuch? [w888]Nach Paragraf achthundertachtundachtzig Absatz eins kann er von der "
     "Erwerberin die Zustimmung zu seiner Eintragung verlangen, soweit ihr Erwerb ihm gegenüber unwirksam ist. "
     "[bleibt]Bis dahin bleibt Frau Ostendorf im Grundbuch. [bleibt2]Erst mit ihrer Zustimmung kann Mats als Eigentümer "
     "eingetragen werden. [zwei]Er braucht also zweierlei: [zwei2]von Herrn Stenzel die Übereignung [zwei3]und von Frau "
     "Ostendorf die Zustimmung.", PS),
    # --- J Ergebnis, Insolvenz ------------------------------------------------------------------------------------------------------
    ("[erg]Für den Fall heißt das: Mats verliert das Haus nicht. [erg2]Mit der Übereignung durch Herrn Stenzel und der "
     "Zustimmung von Frau Ostendorf wird er eingetragen und Eigentümer. [ins]Und wird Herr Stenzel insolvent, kann Mats "
     "nach Paragraf hundertsechs der Insolvenzordnung für seinen Anspruch Befriedigung aus der Insolvenzmasse verlangen. "
     "[ins2]Die Vormerkung ist also auch insolvenzfest.", PS),
    # --- K Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Vormerkung prüfst du meist im Anspruch aus Paragraf achthundertachtundachtzig Absatz eins, "
     "hier Mats gegen Frau Ostendorf auf Zustimmung. [tipp2]Dort prüfst du inzident: wirksame Vormerkung, "
     "vormerkungswidrige Verfügung und Frau Ostendorf als Erwerberin. [tipp3]Und denk an die Akzessorietät: Frau Ostendorf "
     "kann alles einwenden, was gegen den gesicherten Anspruch spricht.", PS),
    # --- L Klausurschema -----------------------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für den Anspruch aus Paragraf achthundertachtundachtzig: [k1]Römisch eins: eine wirksame "
     "Vormerkung, also gesicherter Anspruch, Bewilligung oder einstweilige Verfügung, Eintragung und Berechtigung. "
     "[k2]Römisch zwei: eine vormerkungswidrige Verfügung nach der Eintragung. [k3]Römisch drei: der Anspruchsgegner ist "
     "der Erwerber. [k4]Rechtsfolge: Zustimmung zur Eintragung.", PS),
    # --- M Merksatz (Lexi) -------------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Vormerkung sichert den Käufer bis zu seiner Eintragung. [mk2]Spätere Verfügungen sind ihm "
     "gegenüber unwirksam, soweit sie seinen Anspruch vereiteln oder beeinträchtigen. [mk3]Durchgesetzt wird das mit dem "
     "Zustimmungsanspruch aus Paragraf achthundertachtundachtzig.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
    assert not re.search(r"\b(Stenzels|Ostendorfs)\b|Mats'", text), "Genitiv eines Namens"
    assert not re.search(r"\d", text), "Ziffer im Sprechtext"
    assert not re.search(r"\b(BGB|ZPO|InsO|BGH|GBO)\b", text), "Abkürzung im Sprechtext"
    assert not re.search(r"erfunden|fiktiv", text, re.I), "Fiktiv-Hinweis"
