"""Folge 227 · Notwehrprovokation: Absichtsprovokation & Schutzwehr, Trutzwehr (Mi · Examenswissen · StGB AT · Streitstand).
Fiktiver Fall: Samstagabend auf dem Weinfest am Marktplatz. Ferdinand kündigt seiner Kollegin Josefine an, Herrn Pelzer so lange
zu reizen, bis dieser zuschlägt („dann ist es Notwehr“), macht eine beleidigende Bemerkung (nur angedeutet), Herr Pelzer holt zum
Faustschlag aus, Frau Höfer ruft Ferdinand hinter ihren Weinstand; Ferdinand sticht mit einem Taschenmesser zu, Herr Pelzer wird
am Arm verletzt. Prüfung: §§ 223, 224 Abs. 1 Nr. 2 StGB kurz; § 32 Abs. 2 StGB (Wortlautkarte): Notwehrlage (+) – Angriff des
Provozierten rechtswidrig, die Beleidigung war nicht mehr gegenwärtig; Erforderlichkeit unterstellt (Sachverhalt); Problem
Gebotenheit (§ 32 Abs. 1, Wortlautkarte „geboten“): Absichtsprovokation – Rspr./h. M. Notwehr versagt (Rechtsmissbrauch,
BGH 4 StR 456/18 Rn. 6; 3 StR 331/00 Rn. 10) vs. actio illicita in causa (vom BGH nicht anerkannt, 3 StR 331/00 Rn. 15);
Abwandlung leichtfertige Provokation: Voraussetzungen (4 StR 456/18 Rn. 7), abgestufte Einschränkung Ausweichen – Schutzwehr –
Trutzwehr (4 StR 456/18 Rn. 6; 2 StR 211/24 Rn. 15; 4 StR 197/12 Rn. 15); Ergebnis; Klausurtipp, Schema und Merksatz mit Lexi.
DARSTELLUNG: kein Messer, keine Waffe im Bild, kein Stich, keine Verletzten; Beleidigung nur als Pille „beleidigende Bemerkung“.
Stimmen (Pool stephan, hilde, christian, lucy): Ferdinand stephan (Mann, mittel), Josefine lucy (Frau, jung), Frau Höfer hilde
(Frau, älter); Herr Pelzer spricht nicht (christian nicht nötig). Erzählerin und Lexi: Carla ohne Rolle. Belege je Cue: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter."""

P, PS = 0.3, 0.5

STIMMEN = {"Ferdinand": "stephan", "Josefine": "lucy", "Höfer": "hilde"}

SEGMENTE = [
    # --- A Fall: Weinfest am Marktplatz ----------------------------------------------------------------------------------
    ("[fall]Samstagabend auf dem Weinfest am Marktplatz. [stand]Am Weinstand von Frau Höfer stehen Ferdinand und seine "
     "Kollegin Josefine. [pelzer]Ein paar Meter weiter steht Herr Pelzer, mit dem Ferdinand seit Langem Streit hat. "
     "[leise]Ferdinand sagt leise:", 0.2),
    ("[fe1]Pass auf. Wenn der gleich zuschlägt, ist es Notwehr.", P, "Ferdinand"),
    ("[jo1]Lass das, Ferdinand. Das gibt nur Ärger.", P, "Josefine"),
    ("[bem]Ferdinand geht zu Herrn Pelzer und macht eine beleidigende Bemerkung, genau wie geplant. [faust]Herr Pelzer "
     "wird wütend und holt zum Faustschlag aus.", 0.2),
    ("[ho1]Ferdinand, schnell, hier hinter den Stand!", P, "Höfer"),
    ("[messer]Doch Ferdinand zieht ein Taschenmesser und sticht zu. [arm]Herr Pelzer wird am Arm verletzt und muss ins "
     "Krankenhaus.", P),
    ("[polizei]Der Polizei sagt Ferdinand später:", 0.2),
    ("[fe2]Er wollte mich schlagen. Ich habe mich nur verteidigt.", P, "Ferdinand"),
    ("[frage]Kann sich auf Notwehr berufen, wer den Angriff selbst herausgefordert hat? [frage2]Und was gilt, wenn er den "
     "Streit gar nicht wollte?", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen, mit einer Abwandlung. Halte das Video ruhig kurz an.", 5.0),
    # --- C Tatbestand kurz -------------------------------------------------------------------------------------------------
    ("[tb]Zuerst der Tatbestand: Der Stich ist eine Körperverletzung nach Paragraf zweihundertdreiundzwanzig, [tb2]mit dem "
     "Messer sogar eine gefährliche nach Paragraf zweihundertvierundzwanzig. [vors]Ferdinand handelte vorsätzlich. "
     "[rw]Fraglich ist die Rechtswidrigkeit: Ist er durch Notwehr gerechtfertigt?", P),
    # --- D § 32 Abs. 2 (Wortlautkarte), Notwehrlage -----------------------------------------------------------------------
    ("[p32]Paragraf zweiunddreißig, Absatz zwei: Notwehr ist die Verteidigung, die erforderlich ist, um einen gegenwärtigen "
     "rechtswidrigen Angriff von sich oder einem anderen abzuwenden. [v033]Das ganze Schema zeigt unsere Folge zur Notwehr.", P),
    ("[lage]Erstens die Notwehrlage. [angr]Herr Pelzer holt zum Schlag aus: ein gegenwärtiger Angriff auf Ferdinands Körper. "
     "[rechtsw]Und er ist rechtswidrig. [vorbei]Die Beleidigung war schon vorbei, gegen sie gab es nichts mehr abzuwehren. "
     "[vergelt]Ein Schlag als Antwort ist keine Notwehr, sondern Vergeltung. [lage_ok]Die Notwehrlage liegt also vor, obwohl "
     "Ferdinand sie selbst herbeigeführt hat. [erf]Auch die Erforderlichkeit unterstellen wir: Herr Pelzer ist deutlich "
     "kräftiger, ein milderes Mittel hätte den Schlag nicht sicher abgewehrt.", P),
    # --- E Problem: Gebotenheit (§ 32 Abs. 1, Wortlautkarte) --------------------------------------------------------------
    ("[geb]Das Problem steckt in Absatz eins: Wer eine Tat begeht, die durch Notwehr geboten ist, handelt nicht rechtswidrig. "
     "[sozial]Aus sozialethischen Gründen kann die Verteidigung eingeschränkt sein. [prov]Eine anerkannte Fallgruppe ist die "
     "Notwehrprovokation. [stufen]Der Bundesgerichtshof unterscheidet dabei, wie der Täter provoziert hat: absichtlich, "
     "vorsätzlich oder leichtfertig.", P),
    # --- F Absichtsprovokation: Streitstand -------------------------------------------------------------------------------
    ("[absicht]Absichtlich provoziert, wer einen Angriff gezielt herausfordert, um den Gegner unter dem Deckmantel der "
     "Notwehr zu verletzen. [hier]Genau so Ferdinand: Er wollte, dass Herr Pelzer zuschlägt. [rspr]Nach ständiger "
     "Rechtsprechung ist ihm Notwehr dann grundsätzlich ganz versagt. [miss]Er handelt rechtsmissbräuchlich: Er täuscht "
     "Verteidigung nur vor, in Wirklichkeit will er angreifen. [hm]Die herrschende Lehre sieht das im Ergebnis genauso.", P),
    ("[aiic]Die Lehre von der actio illicita in causa hält die Abwehr selbst dagegen für gerechtfertigt und will den Täter "
     "stattdessen für sein provozierendes Vorverhalten bestrafen. [aiic2]Der Bundesgerichtshof hat das nicht anerkannt, und "
     "im Schrifttum wird diese Figur ganz überwiegend abgelehnt. [folge]Ferdinands Stich war also nicht geboten.", P),
    # --- G Abwandlung: leichtfertige Provokation, abgestufte Einschränkung ------------------------------------------------
    ("[abw]Jetzt die Abwandlung: Ferdinand wollte keinen Streit. [rutsch]Die Bemerkung rutschte ihm im Ärger heraus; dass "
     "Herr Pelzer darauf zuschlägt, lag aber nahe. [leicht]Das ist eine leichtfertige Provokation. "
     "[voraus]Sie schränkt die Notwehr ein, wenn das Vorverhalten rechtswidrig oder sozialethisch zu missbilligen ist und "
     "eng mit dem Angriff zusammenhängt. [erlaubt]Erlaubtes Verhalten genügt dafür in der Regel nicht. [ehre]Eine Beleidigung ist "
     "aber rechtswidrig, und der Schlag folgt sofort.", P),
    ("[einge]Ferdinand behält sein Notwehrrecht, es ist aber abgestuft eingeschränkt. [aus]Zuerst muss er nach Möglichkeit "
     "ausweichen. [schutz]Geht das nicht, darf er Schutzwehr üben, also den Angriff nur abwehren, etwa den "
     "Schlag abblocken. [trutz]Zur Trutzwehr, also zum Gegenangriff, mit einer lebensgefährlichen Waffe darf er erst "
     "greifen, wenn er alle Möglichkeiten der Schutzwehr ausgeschöpft hat. [vorsatz]Bei vorsätzlicher Provokation steigen die "
     "Anforderungen, je schwerer sie wiegt: Dann muss er unter Umständen sogar ein weniger sicheres Abwehrmittel hinnehmen.", P),
    ("[stand2]Hinter den Weinstand hätte Ferdinand ausweichen können, Frau Höfer hatte ihn sogar gerufen. [nicht2]Der sofortige "
     "Stich war also auch in der Abwandlung nicht geboten. [anders]Anders, wenn er weder ausweichen noch sich anders schützen "
     "kann: Dann darf er sich am Ende auch mit dem Messer wehren.", PS),
    # --- H Ergebnis ---------------------------------------------------------------------------------------------------------
    ("[erg]Im Ausgangsfall ist Ferdinand also nicht gerechtfertigt. [strafbar]Er handelte schuldhaft und ist wegen "
     "gefährlicher Körperverletzung strafbar, bei Tötungsvorsatz auch wegen versuchten Totschlags.", PS),
    # --- I Klausurtipp (Lexi) -----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Provokation prüfst du in der Gebotenheit, nicht schon bei der Notwehrlage. [t1]Denn der Angriff "
     "des Provozierten bleibt rechtswidrig. [t2]Frag dann zuerst: Wollte der Täter den Angriff? [t3]Ein Signal im "
     "Sachverhalt ist eine Ankündigung wie die von Ferdinand. [t4]Fehlt die Absicht, prüfst du die Stufen: ausweichen, "
     "Schutzwehr, Trutzwehr.", P),
    # --- J Gutachtenaufbau (Lexi), progressiv -------------------------------------------------------------------------------
    ("[sch]So baust du das Gutachten auf: [s1]Erstens der Tatbestand der gefährlichen Körperverletzung. [s2]Zweitens die "
     "Rechtswidrigkeit: Notwehrlage gegeben, Stich erforderlich, [s2b]aber wegen der Absichtsprovokation nicht geboten. "
     "[s3]Drittens die Schuld.", PS),
    # --- K Merksatz (Lexi) --------------------------------------------------------------------------------------------------
    ("[merke]Merke: Wer den Angriff absichtlich provoziert, hat grundsätzlich kein Notwehrrecht. [m2]Wer sonst vorwerfbar "
     "provoziert, muss ausweichen, sich schützen und darf erst zuletzt zurückschlagen.", 1.2),
]

if __name__ == "__main__":
    import re
    marken = [m for s in SEGMENTE for m in re.findall(r"\[(\w+)\]", s[0])]
    assert len(marken) == len(set(marken)), [m for m in marken if marken.count(m) > 1]
    text = " ".join(re.sub(r"\[\w+\]", "", s[0]) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(marken), "Marken,", len(text), "Zeichen")
