"""Folge 106 · Laptop für Kanzlei und Netflix: Der Verbraucherbegriff (§ 13 BGB) (Mo · Der Fall · Zivilrecht/Schuldrecht AT,
Format Abgrenzung). Fiktiver Fall nach dem Plan-Hook („Die Anwältin kauft einen Laptop – für die Kanzlei und abends für
Netflix“): Rechtsanwältin Ricarda (eigene Kanzlei) bestellt im Mai online bei Herrn Kortmann (Elektronikhandel im Internet,
Unternehmer) einen Laptop für 1.200 € über ihr privates Kundenkonto, Rechnung an die Wohnung, Lieferung an die Kanzlei.
Nutzung: 40 % Kanzlei, 60 % privat. Eine Woche nach der Lieferung widerruft sie per E-Mail; Herr Kortmann lehnt ab
(Anwältin, Lieferung an die Kanzlei, kein Widerrufsrecht für Unternehmer).
Rechtsfolge, an der es hängt: Widerrufsrecht § 312g Abs. 1 i. V. m. § 355 BGB (Fernabsatzvertrag § 312c).
Abgrenzung: (1) § 13 BGB (Wortlautkarte), (2) § 14 Abs. 1 BGB (Wortlautkarte; Anwältin: freier Beruf, kein Gewerbe,
§ 2 BRAO, aber selbständig beruflich), (3) dual use: „überwiegend“ seit 13.6.2014 (BT-Drs. 17/13951, S. 61; ErwG 17
RL 2011/83/EU), Gegenfall 60 % Kanzlei, strengere EuGH-Linie Gruber (C-464/01, Rn. 41, 54) im Zuständigkeitsrecht,
(4) objektiver Zweck, erkennbare Umstände, im Zweifel Verbraucher (BGH VIII ZR 7/09 Rn. 10–12, Lampenfall;
VIII ZR 49/19 Rn. 84; VIII ZR 191/19 Rn. 21). Ergebnis: Verbraucherin, Widerruf wirksam. Klausurtipp und Merksatz mit Lexi.
Figuren: Ricarda (hilde), Herr Kortmann (christian); Lexi/Erzählerin Carla. Belege: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin Carla (auch Lexi), (text, pause, rolle) = Figurenrede. [marke] = Cue für Bild/Tafel/
Prüfpfad; jede Marke kommt genau einmal vor. Zahlen und Paragrafen im Sprechtext als Wörter. „Netflix“ nur einmal (Hook),
im Bild kein Logo, nur ein neutrales Film-Icon."""

P, PS = 0.3, 0.5

STIMMEN = {"Ricarda": "hilde", "Kortmann": "christian"}  # Lexi = Erzählerstimme (Carla)

SEGMENTE = [
    # --- A1 Fall: die Bestellung ------------------------------------------------------------------------------------
    ("[fall]Ricarda ist Anwältin. Sie kauft einen Laptop: für ihre Kanzlei und abends für Netflix. [shop]Im Mai bestellt sie "
     "ihn online bei Herrn Kortmann, der einen Elektronikhandel im Internet betreibt, für zwölfhundert Euro. "
     "[konto]Sie bestellt über ihr privates Kundenkonto, die Rechnung geht an ihre Wohnung. [liefer]Liefern lässt sie "
     "an die Kanzlei, weil sie tagsüber dort ist.", 0.3),
    # --- A2 Fall: die Nutzung -------------------------------------------------------------------------------------------
    ("[nutz]Den Laptop nutzt sie zu vierzig Prozent für die Kanzlei, [privat]zu sechzig Prozent privat: Filme, Fotos, "
     "Urlaubsplanung.", 0.3),
    # --- A3 Fall: der Widerruf ------------------------------------------------------------------------------------------
    ("[woche]Eine Woche nach der Lieferung gefällt ihr das Display nicht mehr. Sie schreibt Herrn Kortmann eine E-Mail.", 0.25),
    ("[ri1]Ich widerrufe den Kaufvertrag.", 0.25, "Ricarda"),
    ("[ko1]Sie sind Anwältin, und geliefert wurde an Ihre Kanzlei. Für Unternehmer gibt es kein Widerrufsrecht.", 0.25,
     "Kortmann"),
    ("[ri2]Ich nutze den Laptop aber überwiegend privat.", 0.3, "Ricarda"),
    ("[frage]Ist Ricarda Verbraucherin, obwohl sie den Laptop auch beruflich nutzt? [frage2]Daran hängt ihr "
     "Widerrufsrecht.", 0.5),
    # --- B Sachverhalt ---------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 4.6),
    # --- C Rechtsfolge: Widerrufsrecht ---------------------------------------------------------------------------------
    ("[wr]Zuerst die Rechtsfolge, an der alles hängt. [w312]Nach Paragraf dreihundertzwölf g Absatz eins hat der "
     "Verbraucher bei Fernabsatzverträgen ein Widerrufsrecht. [fern]Ricarda hat online bestellt, und Herr Kortmann "
     "handelt gewerblich, ist also Unternehmer. [frist]Die Frist beträgt vierzehn Tage und beginnt frühestens mit dem "
     "Erhalt der Ware. Nach einer Woche ist Ricarda rechtzeitig. [offen]Offen ist nur: Ist sie Verbraucherin?", P),
    # --- D § 13 BGB (Wortlaut) -----------------------------------------------------------------------------------------
    ("[w13]Paragraf dreizehn: Verbraucher ist jede natürliche Person, die ein Rechtsgeschäft zu Zwecken abschließt, die "
     "überwiegend weder ihrer gewerblichen noch ihrer selbständigen beruflichen Tätigkeit zugerechnet werden können. "
     "[mp]Ricarda ist eine natürliche Person, [mr]und der Kauf ist ein Rechtsgeschäft. [mz]Entscheidend ist der Zweck.", P),
    # --- E § 14 Abs. 1 BGB (Wortlaut), freier Beruf ------------------------------------------------------------------------
    ("[w14]Das Gegenstück ist Paragraf vierzehn Absatz eins: Unternehmer ist eine natürliche oder juristische Person oder "
     "eine rechtsfähige Personengesellschaft, die bei Abschluss eines Rechtsgeschäfts in Ausübung ihrer gewerblichen oder "
     "selbständigen beruflichen Tätigkeit handelt. [frei]Eine Anwältin betreibt kein Gewerbe, sie übt einen freien Beruf "
     "aus. [selb]Mit eigener Kanzlei ist ihre Tätigkeit aber selbständig beruflich. [rolle]Ob Ricarda Verbraucherin oder Unternehmerin ist, "
     "hängt also nicht an ihrem Beruf, sondern am Zweck dieses Geschäfts.", P),
    # --- F dual use: überwiegend (Waage), Gegenfall, EuGH Gruber -------------------------------------------------------------
    ("[dual]Was gilt bei gemischter Nutzung, dem sogenannten Dual Use? [ueberw]Seit Juni zweitausendvierzehn steht in "
     "Paragraf dreizehn das Wort überwiegend. [begr]Der Gesetzgeber stellt damit klar: Bei Verträgen mit doppeltem Zweck "
     "kommt es auf den überwiegenden Zweck an. [sub]Bei Ricarda überwiegt mit sechzig Prozent der private Zweck. "
     "[gegen]Läge der Kanzleianteil bei sechzig Prozent, wäre sie Unternehmerin.", PS),
    ("[gruber]Strenger ist der Europäische Gerichtshof im Zuständigkeitsrecht: Nach dem Urteil Gruber genügt dort ein "
     "Überwiegen des privaten Zwecks nicht, der berufliche Zweck muss ganz untergeordnet sein. [nat]Für Paragraf dreizehn zählt aber das "
     "Überwiegen.", PS),
    # --- G objektiver Zweck, erkennbare Umstände, im Zweifel Verbraucher (BGH) ------------------------------------------------
    ("[erk]Und wenn der Händler den Zweck nicht kennt? [obj]Maßgeblich ist grundsätzlich der objektiv verfolgte Zweck. [zweif]Nach dem "
     "Bundesgerichtshof ist das Handeln einer natürlichen Person grundsätzlich Verbraucherhandeln, Zweifel gehen nicht zu "
     "ihren Lasten. [eind]Anders nur, wenn die für den Vertragspartner erkennbaren Umstände eindeutig und zweifelsfrei auf "
     "berufliches Handeln hinweisen.", P),
    ("[lampe]Im Lampenfall bestellte eine Rechtsanwältin Lampen für ihre Wohnung und ließ sie an die Kanzlei liefern. "
     "[lampe2]Sie blieb Verbraucherin. [hier]Auch bei Ricarda zeigt nur die Lieferadresse auf die Kanzlei, Kundenkonto und "
     "Rechnung sind privat. Das ist nicht eindeutig. [bew]Den privaten Zweck muss Ricarda im Streit allerdings beweisen.", PS),
    # --- H Ergebnis ---------------------------------------------------------------------------------------------------------------
    ("[erg]Ergebnis: Ricarda ist Verbraucherin, ihr Widerruf ist wirksam. [erg2]Beide müssen die Leistungen "
     "zurückgewähren, spätestens nach vierzehn Tagen: [erg3]Ricarda den Laptop, Herr Kortmann die zwölfhundert Euro.", PS),
    # --- I Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Lass dich von der Kanzleiadresse nicht täuschen. Eine Lieferung an die Kanzlei oder die Zahlung "
     "vom Geschäftskonto machen allein niemanden zum Unternehmer. [tipp2]Prüfe zuerst den objektiven Zweck und dann, ob "
     "eindeutige Umstände dagegen sprechen.", PS),
    # --- J Klausurschema --------------------------------------------------------------------------------------------------------
    ("[sch]Dein Klausurschema zur Abgrenzung: [k1]Römisch eins: natürliche Person. [k2]Römisch zwei: Rechtsgeschäft. "
     "[k3]Römisch drei: Zweck, bei gemischter Nutzung der überwiegende Zweck. [k4]Römisch vier: keine eindeutigen "
     "Umstände für berufliches Handeln, im Zweifel Verbraucher. [k5]Scheitert die Verbrauchereigenschaft, prüfe den "
     "Unternehmer nach Paragraf vierzehn.", PS),
    # --- K Merksatz (Lexi) ------------------------------------------------------------------------------------------------------
    ("[merke]Merke: Es zählt der überwiegende Zweck des Geschäfts, nicht der Beruf. [mz2]Und im Zweifel handelt eine "
     "natürliche Person als Verbraucher.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen;", text.count("Netflix"), "× Netflix")
