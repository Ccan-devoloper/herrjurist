#!/usr/bin/env python3
"""Brücke zur privaten Instagram-Schnittstelle (instagrapi) für interaktive Stories.

Warum überhaupt: Die offizielle Graph-Publishing-API kennt keinen nativen
Umfrage-Sticker. Eine ins Bild gemalte Umfrage sieht aus wie eine, ist aber
nicht antippbar und liefert keine Ergebnisse. Wer echte Interaktion will,
kommt an der privaten Schnittstelle nicht vorbei.

Was das kostet: Diese Schnittstelle ist nicht freigegeben. Instagram kann
Endpunkte ändern, Anmeldungen mit einer Challenge blockieren und im
schlimmsten Fall das Konto sperren. Deshalb gilt hier:

  * Dieses Skript ist NIE der einzige Weg. Schlägt es fehl, geht dieselbe
    Story über die Graph API raus - der Aufrufer sorgt dafür.
  * Bei einer Challenge wird NICHT wiederholt. Eine Wiederholungsschleife
    gegen eine Anmeldesperre ist genau das, was ein Konto endgültig kostet.
  * Die Sitzung wird wiederverwendet. Jede neue Anmeldung von einer neuen
    Runner-IP sieht für Instagram nach einer Übernahme aus; eine bestehende
    Sitzung sieht nach dem immer gleichen Gerät aus.

Ein- und Ausgabe laufen über JSON auf stdin/stdout, damit der Node-Teil die
Zugangsdaten nicht über die Kommandozeile reichen muss (dort läse sie jeder
Prozess auf demselben Rechner mit). Alles Geschwätzige geht nach stderr,
damit stdout eine einzige, verlässlich lesbare JSON-Zeile bleibt.
"""

import json
import logging
import sys
from pathlib import Path

logging.basicConfig(stream=sys.stderr, level=logging.WARNING)


def antwort(**felder):
    """Genau eine JSON-Zeile auf stdout - und Schluss."""
    sys.stdout.write(json.dumps(felder, ensure_ascii=False) + "\n")
    sys.stdout.flush()
    sys.exit(0 if felder.get("ok") else 1)


def main():
    auftrag = json.load(sys.stdin)
    bild = Path(auftrag["bild"])
    if not bild.exists():
        antwort(ok=False, art="aufruf", fehler=f"Bild nicht gefunden: {bild}")

    try:
        from instagrapi import Client
        from instagrapi.types import StoryPoll, StoryLink
        from instagrapi.exceptions import (
            ChallengeRequired, TwoFactorRequired, LoginRequired,
            PleaseWaitFewMinutes, ClientError,
        )
    except ImportError as e:
        antwort(ok=False, art="aufbau", fehler=f"instagrapi fehlt: {e}")

    client = Client()
    client.delay_range = [2, 6]          # kein Stakkato - das fällt auf

    # --- Anmelden -------------------------------------------------------
    # Zuerst mit der gespeicherten Sitzung. Nur wenn die nicht mehr trägt,
    # wird neu angemeldet; jede Neuanmeldung ist ein Risiko für sich.
    sitzung = auftrag.get("sitzung")
    angemeldet = False
    if sitzung:
        try:
            client.set_settings(sitzung)
            client.login(auftrag["nutzer"], auftrag["passwort"])   # nutzt die Sitzung, wenn sie gilt
            client.get_timeline_feed()                             # beweist, dass sie wirklich trägt
            angemeldet = True
        except (LoginRequired, ClientError) as e:
            logging.warning("Gespeicherte Sitzung trägt nicht mehr: %s", e)
            client = Client()
            client.delay_range = [2, 6]

    if not angemeldet:
        if not auftrag.get("neuanmeldungErlaubt", True):
            antwort(ok=False, art="sitzung", fehler="Sitzung abgelaufen und Neuanmeldung nicht erlaubt")
        try:
            client.login(auftrag["nutzer"], auftrag["passwort"])
        except TwoFactorRequired:
            antwort(ok=False, art="challenge", fehler="Zwei-Faktor-Bestätigung verlangt - von Hand anmelden und Sitzung neu erzeugen")
        except ChallengeRequired:
            antwort(ok=False, art="challenge", fehler="Instagram verlangt eine Bestätigung (Challenge) - NICHT wiederholen")
        except PleaseWaitFewMinutes as e:
            antwort(ok=False, art="bremse", fehler=f"Instagram bremst: {e}")
        except Exception as e:                                     # noqa: BLE001 - jeder Fehler ist hier ein Rückfall
            antwort(ok=False, art="login", fehler=f"{type(e).__name__}: {e}")

    # --- Story hochladen ------------------------------------------------
    polls, links = [], []
    u = auftrag.get("umfrage")
    if u:
        polls.append(StoryPoll(
            x=u["x"], y=u["y"], width=u["width"], height=u["height"],
            question=u["frage"], options=list(u["optionen"]),
        ))
    l = auftrag.get("link")
    if l:
        links.append(StoryLink(webUri=l["url"], x=l.get("x", 0.5), y=l.get("y", 0.82),
                               width=l.get("width", 0.6), height=l.get("height", 0.07)))

    try:
        story = client.photo_upload_to_story(bild, links=links, polls=polls)
    except ChallengeRequired:
        antwort(ok=False, art="challenge", fehler="Challenge beim Hochladen - NICHT wiederholen",
                sitzung=client.get_settings())
    except PleaseWaitFewMinutes as e:
        antwort(ok=False, art="bremse", fehler=f"Instagram bremst: {e}", sitzung=client.get_settings())
    except Exception as e:                                         # noqa: BLE001
        antwort(ok=False, art="upload", fehler=f"{type(e).__name__}: {e}", sitzung=client.get_settings())

    antwort(ok=True, medienId=str(story.pk), sitzung=client.get_settings())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:                                          # noqa: BLE001
        antwort(ok=False, art="unerwartet", fehler=f"{type(e).__name__}: {e}")
