# ============================
# 📘 Scraping básico — requests + regex
# ============================
# Scraping = pedir HTML (HTTP) y extraer datos.
#
# En esta lección:
#   1) requests.get → status_code + texto HTML
#   2) re.search sobre un HTML PEQUEÑO (string / archivo local)
#   3) Tip ético + por qué las tiendas en vivo rompen demos
#
# Tip: regex sobre HTML es frágil → en la próxima lección usamos BeautifulSoup.

from pathlib import Path
import re

try:
    import requests
except ImportError:
    requests = None  # type: ignore[assignment]
    print("Tip: instalá requests →  .venv/bin/pip install requests")

DIR = Path(__file__).resolve().parent

# ============================
# 🔹 Ética breve
# ============================
print("--- Ética del scraping ---")
print("1) Respetá robots.txt y términos del sitio.")
print("2) Usá un User-Agent identificable (quién sos / para qué).")
print("3) No martillés el servidor: pocos requests, pausas, cache.")
print("4) Para aprender, preferí HTML local o sitios estables.")

# ============================
# 🔹 HTML local (demo estable)
# ============================
# Path next to this file → no depende de la red ni de una tienda.
print("\n--- HTML local (sample.html) ---")

html_local = (DIR / "sample.html").read_text(encoding="utf-8")
print("Primeros 80 chars:", html_local[:80].replace("\n", " "), "...")

# Extraer <title> con regex (grupo 1 = contenido entre tags)
title_match = re.search(r"<title>(.*?)</title>", html_local, re.IGNORECASE | re.DOTALL)
if title_match:
    print("title (regex):", title_match.group(1).strip())

# Extraer un precio de un <p class="precio">…</p>
precio_match = re.search(
    r'<p\s+class="precio">(.*?)</p>',
    html_local,
    re.IGNORECASE | re.DOTALL,
)
if precio_match:
    print("precio (regex):", precio_match.group(1).strip())

# Contar anchors de forma burda (solo demo: frágil)
n_links = len(re.findall(r"<a\s", html_local, re.IGNORECASE))
print("cantidad aproximada de <a :", n_links)

# Tip: si el HTML cambia espacios, atributos o el orden, el regex se rompe.

# ============================
# 🔹 Mismo patrón sobre un string en memoria
# ============================
print("\n--- HTML string en memoria ---")

html_mini = """
<html>
  <head><title>Mini demo</title></head>
  <body>
    <h1>Hola</h1>
    <span class="precio">USD 10</span>
  </body>
</html>
"""
# Paso 1: buscar title
m = re.search(r"<title>(.*?)</title>", html_mini, re.I | re.S)
print("title:", m.group(1) if m else "(sin title)")

# Paso 2: buscar precio (otra clase / tag → hay que reescribir el patrón)
m2 = re.search(r'class="precio">(.*?)<', html_mini, re.I | re.S)
print("precio:", m2.group(1).strip() if m2 else "(sin precio)")

# ============================
# 🔹 GET opcional a un sitio estable
# ============================
print("\n--- GET opcional: https://example.com ---")

HEADERS = {
    # User-Agent claro: no fingimos ser Googlebot.
    "User-Agent": "welcomePy-student/1.0 (learning; contact: local)",
}

if requests is None:
    print("Saltando GET: falta el paquete requests.")
else:
    try:
        # timeout evita colgarse si la red falla
        response = requests.get("https://example.com", headers=HEADERS, timeout=10)
        print("status_code:", response.status_code)
        if response.status_code == 200:
            live_title = re.search(r"<title>(.*?)</title>", response.text, re.I | re.S)
            print("title live:", live_title.group(1).strip() if live_title else "(sin title)")
    except requests.RequestException as exc:
        print("No se pudo conectar (OK para la lección):", type(exc).__name__, exc)

# Tip: páginas de tiendas (Apple, Amazon, etc.) cambian clases y estructura
# a menudo. Usarlas como demo "obligatoria" hace que la lección se rompa
# sin que hayas hecho nada mal. Por eso acá priorizamos HTML local + example.com.

# ============================
# 🔹 Resumen
# ============================
# - requests.get(url) → Response con .status_code y .text
# - re.search(patrón, html) → Match; .group(1) es el primer grupo (…)
# - Regex + HTML = frágil (espacios, attrs, JS, templates)
# - Siguiente paso: BeautifulSoup (parsea el DOM de forma más robusta)
# - Ética: robots, User-Agent, no martillar, preferir demos estables
