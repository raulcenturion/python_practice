# ============================
# 📘 Wiki scraper — función reutilizable
# ============================
# Objetivo: una función que recibe URL **o** HTML ya cargado y extrae:
#   - h1 (título principal)
#   - enlaces absolutos con urljoin
#   - og:image (Open Graph) si existe
#
# Ética: User-Agent claro, timeout, no martillar Wikipedia.
# Tip: Wikipedia es relativamente estable; igual preferí cache / HTML de prueba.

from __future__ import annotations

from urllib.parse import urljoin

from bs4 import BeautifulSoup

try:
    import requests
except ImportError:
    requests = None  # type: ignore[assignment]

HEADERS = {
    "User-Agent": "welcomePy-student/1.0 (learning wiki scraper; contact: local)",
}

# HTML de respaldo (demo sin red)
HTML_DEMO = """
<html>
<head>
  <title>Python (demo)</title>
  <meta property="og:image" content="https://example.com/python.png">
</head>
<body>
  <h1>Python</h1>
  <p>Lenguaje de programación.</p>
  <a href="/wiki/Programming">Programming</a>
  <a href="https://example.com">Example</a>
</body>
</html>
"""


def scrape_page(url: str | None = None, html: str | None = None) -> dict:
    """Extrae h1, links absolutos y og:image.

    Pasá `html=` para demos locales (estable).
    Pasá `url=` para pedir la página (requiere requests + red).
    """
    if html is None and url is None:
        raise ValueError("Pasá url= o html=")

    base = url or "https://example.com/"

    if html is None:
        if requests is None:
            raise ImportError("Instalá requests para scrapear por URL")
        # Paso 1: GET con timeout y User-Agent
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        html = response.text
        base = response.url  # por si hubo redirect

    # Paso 2: parsear
    soup = BeautifulSoup(html, "html.parser")

    # Paso 3: h1(s)
    h1s = [h.get_text(strip=True) for h in soup.find_all("h1")]

    # Paso 4: links → absolutos con urljoin(base, href)
    links: list[str] = []
    for a in soup.find_all("a", href=True):
        links.append(urljoin(base, a["href"]))

    # Paso 5: og:image
    og = soup.find("meta", property="og:image")
    og_image = og.get("content") if og else None

    return {
        "h1": h1s,
        "links": links,
        "og_image": og_image,
        "base": base,
    }


# ============================
# 🔹 Demo con HTML local (siempre funciona)
# ============================
print("--- Demo con HTML provisto ---")
data = scrape_page(html=HTML_DEMO, url="https://en.wikipedia.org/wiki/Python_(programming_language)")
print("h1:", data["h1"])
print("links (primeros 5):", data["links"][:5])
print("og:image:", data["og_image"])
# Tip: og:image es la imagen de preview al compartir el link en redes.

# ============================
# 🔹 Demo opcional: Wikipedia en vivo
# ============================
print("\n--- Demo opcional: Wikipedia (red) ---")

WIKI = "https://en.wikipedia.org/wiki/Python_(programming_language)"

if requests is None:
    print("Saltando Wikipedia: falta requests.")
else:
    try:
        live = scrape_page(url=WIKI)
        print("h1:", live["h1"][:3])
        print("n links:", len(live["links"]))
        print("og:image:", (live["og_image"] or "")[:80], "...")
    except Exception as exc:  # noqa: BLE001 — demo educativa
        print("No se pudo scrapear Wikipedia:", type(exc).__name__, exc)

# Ética: Wikipedia permite bots razonables; igual andá despacio y cacheá.

# ============================
# 🔹 Resumen
# ============================
# - Una función scrape_page(url= | html=) → dict con h1, links, og_image
# - urljoin(base, href) convierte /wiki/X en URL absoluta
# - meta property="og:image" → preview social
# - Preferí html= en tests; url= solo cuando hace falta red
