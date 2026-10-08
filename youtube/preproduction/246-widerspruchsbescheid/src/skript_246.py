"""Folge 246 · Widerspruchsbescheid schreiben: Tenor, Gründe, Kosten, Belehrung (Fr · 2. Examen · VwGO-Praxis · Schema).
Übungsfall nach dem Hook des Themenplans („Als Referendarin im Landratsamt sollst du über einen Widerspruch gegen eine
Hundehaltungsuntersagung entscheiden“), Land und Behörden fiktiv (Land mit Landratsamt, dessen Recht den Widerspruch vorsieht):
Herr Holzapfel hält einen verspielten Mischling. Die Gemeinde hatte angeordnet, den Hund draußen an der Leine zu führen; dreimal
lief er dennoch frei durch den Ort, einmal sprang er eine Joggerin an. Die Gemeinde untersagt die Hundehaltung (Bescheid vom
2.3.2026). Herr Holzapfel legt Widerspruch ein („ganz lieb“, Zaun erhöht). Herr Sperling (Gemeinde) hilft nicht ab und legt
die Akte dem Landratsamt vor; Referendarin Körner entwirft den Widerspruchsbescheid.
Aufbau (Perspektive Bescheidentwurf): 1. Vorverfahren? (§ 68 I 1, 2 VwGO, Wortlautkarte; Länder-Overlay nur amtlich geprüft:
§ 110 JustG NRW, § 80 NJG); 2. Abhilfe § 72, Zuständigkeit § 73 I (Wortlautkarte); 3. Bescheid: Kopf, Tenor, Gründe
(I. Sachverhalt, II. Zulässigkeit § 70, Begründetheit: Rechtmäßigkeit und Zweckmäßigkeit, BVerwG 1 C 2.14 Rn. 13), Kosten
(§ 73 III 3 VwGO, § 80 I 3, III 2 VwVfG bzw. Landes-VwVfG, z. B. § 80 VwVfG NRW), Rechtsbehelfsbelehrung (§ 58 I, § 74 I 1,
§ 79 I Nr. 1 VwGO, Muster), Zustellung (§ 73 III VwGO, Wortlautkarte; § 3 VwZG); 4. typische Fehler (Zweckmäßigkeit,
Belehrung → § 58 II); Klausurtipp (§ 79 I Nr. 1), Schema, Merksatz mit Lexi.
Stimmen (Pool william, sabrina, marc, laura_ruhig): Herr Holzapfel william (Mann, älter), Herr Sperling marc (Mann, mittel),
Referendarin Körner laura_ruhig (Frau, mittel); sabrina nicht gebraucht. Erzählerin und Lexi: Carla ohne Rolle.
Namen nie im Genitiv mit -s. Belege je Cue: ../RECHTSSTAND.md.
Segmente: (text, pause) = Erzählerin, (text, pause, rolle) = Figurenrede. [marke] = Cue; jede Marke genau einmal.
Zahlen und Paragrafen im Sprechtext als Wörter."""
import re as _re

P, PS = 0.3, 0.5

STIMMEN = {"Holzapfel": "william", "Sperling": "marc", "Körner": "laura_ruhig"}

SEGMENTE = [
    # --- A Fall: Haus mit Garten, Gemeinde, Landratsamt -----------------------------------------------------------------
    ("[fall]Ein Haus mit Garten am Ortsrand. [holz]Hier wohnt Herr Holzapfel mit seinem Hund, einem verspielten Mischling. "
     "[leine]Die Gemeinde hat angeordnet: Draußen gehört der Hund an die Leine. [frei]Doch dreimal läuft er frei durch den "
     "Ort. Einmal springt er eine Joggerin an, und sie stürzt. [bescheid]Nun untersagt die Gemeinde Herrn Holzapfel die "
     "Hundehaltung.", 0.2),
    ("[ho1]Er ist doch ganz lieb! Und den Zaun habe ich erhöht. Ich lege Widerspruch ein.", P, "Holzapfel"),
    ("[wid]Zwei Wochen später liegt sein Widerspruch bei der Gemeinde. [sperl]Herr Sperling prüft, ob die Gemeinde "
     "abhilft.", 0.2),
    ("[sp1]Die Untersagung bleibt. Wir helfen nicht ab und legen die Akte dem Landratsamt vor.", P, "Sperling"),
    ("[lra]Im Landratsamt landet die Akte bei Referendarin Körner.", 0.2),
    ("[ko1]Ich entwerfe den Widerspruchsbescheid. Aber was gehört da alles hinein?", P, "Körner"),
    ("[frage]Gibt es überhaupt ein Vorverfahren, und wer entscheidet? [frage2]Wie baust du Tenor, Gründe, Kosten und "
     "Belehrung? [frage3]Die Perspektive des zweiten Examens, mit einem Entwurf Schritt für Schritt.", PS),
    # --- B Sachverhalt -----------------------------------------------------------------------------------------------------
    ("[sv]Hier ist der Sachverhalt zum Nachlesen. Halte das Video ruhig kurz an.", 5.0),
    # --- C 1. Vorverfahren ------------------------------------------------------------------------------------------------
    ("[vv]Erstens: Gibt es überhaupt ein Vorverfahren? Vor der Anfechtungsklage sind Rechtmäßigkeit und Zweckmäßigkeit des "
     "Verwaltungsakts nachzuprüfen, Paragraf achtundsechzig Absatz eins. [wl68]Einer solchen Nachprüfung bedarf es aber "
     "nicht, wenn ein Gesetz dies bestimmt. [land]Viele Länder haben den Widerspruch so weitgehend abgeschafft, etwa "
     "Nordrhein-Westfalen und Niedersachsen, jeweils mit Ausnahmen. [land2]Prüfe also immer dein Landesrecht. In unserem "
     "Fall sieht es den Widerspruch vor.", P),
    # --- D 2. Abhilfe und Zuständigkeit -----------------------------------------------------------------------------------
    ("[abhilfe]Zweitens: Wer entscheidet? Zuerst die Ausgangsbehörde. Hält sie den Widerspruch für begründet, hilft sie ihm "
     "ab, Paragraf zweiundsiebzig. [wl73]Hilft sie nicht ab, ergeht ein Widerspruchsbescheid. Den erlässt grundsätzlich die "
     "nächsthöhere Behörde, Paragraf dreiundsiebzig Absatz eins. [naechst]In unserem Fall ist das das Landratsamt. [ausn]Ein Gesetz kann "
     "aber auch die Ausgangsbehörde selbst zuständig machen. Und in Selbstverwaltungsangelegenheiten entscheidet die "
     "Selbstverwaltungsbehörde.", P),
    # --- E 3. Der Bescheid: Kopf und Tenor ----------------------------------------------------------------------------------
    ("[kopf]Drittens, der Bescheid. Oben steht der Kopf: Behörde, Datum, Aktenzeichen, Adressat, die Art der Zustellung und "
     "die Überschrift Widerspruchsbescheid. [tenor]Dann der Tenor. Eins: Der Widerspruch wird zurückgewiesen. [tenor2]Zwei: "
     "Die Kosten des Verfahrens trägt der Widerspruchsführer. [tenor3]Drei: Für diesen Bescheid wird eine Gebühr erhoben. "
     "Ob und in welcher Höhe, regelt das Kostenrecht des Landes.", P),
    # --- F Gründe -----------------------------------------------------------------------------------------------------------
    ("[gruende]Es folgen die Gründe. Unter römisch eins der Sachverhalt: Bescheid, Widerspruch und Nichtabhilfe. "
     "[zul]Unter römisch zwei die rechtliche Würdigung. Zuerst die Zulässigkeit: Der Widerspruch ist statthaft und innerhalb "
     "eines Monats schriftlich erhoben, Paragraf siebzig. [begr]Dann die Begründetheit. Hier prüft die Widerspruchsbehörde "
     "mehr als ein Gericht: Rechtmäßigkeit und Zweckmäßigkeit. [recht]Die Rechtmäßigkeit prüfst du wie im Urteil. Hier ist "
     "die Untersagung rechtmäßig. [zweck]Bei der Zweckmäßigkeit beurteilst du selbst, ob die Untersagung das richtige Mittel "
     "ist. Würde eine neue Leinenpflicht reichen? [zweck2]Nein. Die alte hat Herr Holzapfel dreimal missachtet, und der "
     "höhere Zaun hilft beim Spaziergang nicht.", P),
    # --- G Kosten -----------------------------------------------------------------------------------------------------------
    ("[kosten]In den Gründen erläuterst du auch die Kostenentscheidung. Dass der Widerspruchsbescheid bestimmt, wer die Kosten trägt, verlangt "
     "Paragraf dreiundsiebzig Absatz drei. [k80]Die Erstattung regelt Paragraf achtzig Verwaltungsverfahrensgesetz, bei "
     "Landesbehörden das Gesetz des Landes. [k80b]Bleibt der Widerspruch erfolglos, erstattet der Widerspruchsführer der "
     "Ausgangsbehörde ihre notwendigen Aufwendungen. [anwalt]Hat er Erfolg, bestimmt die Kostenentscheidung auch, ob ein "
     "Anwalt notwendig war.", P),
    # --- H Rechtsbehelfsbelehrung und Zustellung -------------------------------------------------------------------------------
    ("[belehr]Dann die Rechtsbehelfsbelehrung. Sie nennt den Rechtsbehelf, das Gericht, seinen Sitz und die Frist, Paragraf "
     "achtundfünfzig. [muster]Etwa so: Gegen den Bescheid der Gemeinde vom zweiten März zweitausendsechsundzwanzig in "
     "Gestalt dieses Widerspruchsbescheids kann innerhalb eines Monats nach Zustellung Klage beim Verwaltungsgericht erhoben "
     "werden. [sitz]Name und Sitz des Gerichts trägst du konkret ein.", P),
    ("[zust]Zum Schluss die Zustellung. Paragraf dreiundsiebzig Absatz drei fasst zusammen: begründen, mit "
     "Rechtsmittelbelehrung versehen und zustellen, von Amts wegen nach dem Verwaltungszustellungsgesetz. [pzu]Etwa durch "
     "die Post mit Zustellungsurkunde. [frist]Ab der Zustellung läuft die Klagefrist von einem Monat, Paragraf "
     "vierundsiebzig.", PS),
    # --- I 4. Typische Fehler -------------------------------------------------------------------------------------------------
    ("[fehler]Viertens, typische Fehler. [f1]Fehler eins: Die Zweckmäßigkeit fehlt. Bei Ermessen beurteilt die "
     "Widerspruchsbehörde sie grundsätzlich mit. [f2]Fehler zwei: eine falsche Belehrung. Dann läuft statt eines Monats die "
     "Jahresfrist, Paragraf achtundfünfzig Absatz zwei.", PS),
    # --- J Klausurtipp (Lexi) ----------------------------------------------------------------------------------------------
    ("[tipp]Klausurtipp: Die Klage richtet sich gegen den ursprünglichen Bescheid in der Gestalt, die er durch den "
     "Widerspruchsbescheid gefunden hat, Paragraf neunundsiebzig. [tipp2]Deshalb nennt deine Belehrung beide Bescheide. "
     "[tipp3]Und würdige in den Gründen das Vorbringen, hier den höheren Zaun.", PS),
    # --- K Schema (Lexi) ---------------------------------------------------------------------------------------------------
    ("[sch]Dein Schema für den Widerspruchsbescheid. [s1]Eins, der Kopf. [s2]Zwei, der Tenor: Entscheidung, Kosten, Gebühr. "
     "[s3]Drei, die Gründe: Sachverhalt, Zulässigkeit, Begründetheit mit Rechtmäßigkeit und Zweckmäßigkeit, [s3b]dazu die "
     "Kosten nach Paragraf achtzig. [s4]Vier, die Rechtsbehelfsbelehrung. [s5]Fünf, die Zustellung.", PS),
    # --- L Merksatz (Lexi) -------------------------------------------------------------------------------------------------
    ("[merke]Merke: Die Widerspruchsbehörde prüft Rechtmäßigkeit und Zweckmäßigkeit. [m2]Und ihr Bescheid braucht Tenor, "
     "Gründe, Kosten, Belehrung und Zustellung.", 1.4),
]

_alle = [m for s in SEGMENTE for m in _re.findall(r"\[(\w+)\]", s[0])]
assert len(_alle) == len(set(_alle)), "Marke doppelt"

if __name__ == "__main__":
    n = sum(len(_re.sub(r"\[\w+\]", "", s[0])) for s in SEGMENTE)
    print(len(SEGMENTE), "Segmente,", len(_alle), "Marken,", n, "Zeichen")
