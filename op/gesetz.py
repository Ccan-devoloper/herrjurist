"""Gesetzeswortlaut nachschlagen (gesetze-im-internet.de), um Normen, Zahlen und Zitate zu prüfen.

    python3 social/op/gesetz.py ao_1977/__193 "Zulässigkeit"
    python3 social/op/gesetz.py estg/__6 "3. Verbindlichkeiten"

Kürzel: ao_1977, estg, kstg_1977, gewstg, ustg_1980, erbstg_1974, bewg, astg, umwstg_2006, hgb, bgb, fgo, estdv_1955,
ustdv_1980, gewstdv, aeao gibt es dort nicht (BMF-Seite). Ausgabe: Fundstelle samt Umgebung."""
import html, os, re, sys, urllib.request

CACHE = os.path.join(os.environ.get("OP_RES", os.path.join(os.path.dirname(os.path.abspath(__file__)), ".res")), "cache", "gesetze")


def text(pfad):
    os.makedirs(CACHE, exist_ok=True)
    f = os.path.join(CACHE, pfad.replace("/", "_") + ".html")
    if not os.path.exists(f) or os.path.getsize(f) < 1000:
        urllib.request.urlretrieve("https://www.gesetze-im-internet.de/" + pfad + ".html", f)
    s = open(f, encoding="iso-8859-1", errors="ignore").read()
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s)))


if __name__ == "__main__":
    t = text(sys.argv[1])
    such = sys.argv[2:] or ["Nichtamtliches Inhaltsverzeichnis"]
    for s in such:
        for m in list(re.finditer(re.escape(s), t))[:3]:
            print("…", t[max(0, m.start() - 150):m.start() + 900], "\n")
