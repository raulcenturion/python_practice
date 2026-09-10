# ============================
# 📘 BeautifulSoup — parsear HTML
# ============================
# BeautifulSoup convierte un string HTML en un árbol de nodos.
# Así buscás por tag, clase, id o atributos sin pelear con regex.
#
# Requiere:  .venv/bin/pip install beautifulsoup4
# Parser: "html.parser" (incluido en Python; no hace falta lxml).

from pathlib import Path

from bs4 import BeautifulSoup

try:
    import requests
except ImportError:
    requests = None  # type: ignore[assignment]

DIR = Path(__file__).resolve().parent

# ============================
# 🔹 Ética (recordatorio)
# ============================
print("--- Ética ---")
print("User-Agent claro, pocos requests, preferí demos locales.")
print("Tip: tiendas en vivo cambian clases → demos frágiles. Usá sample.html.")

# ============================
# 🔹 Parsear HTML local
# ============================
print("\n--- BeautifulSoup sobre sample.html ---")

html = (DIR / "sample.html").read_text(encoding="utf-8")
# Paso 1: crear el "soup" (árbol)
soup = BeautifulSoup(html, "html.parser")

# Paso 2: title → .text (o .string) limpia tags internos
print("title:", soup.title.text if soup.title else "(sin title)")

# Paso 3: find = primer match; find_all = lista
h1 = soup.find("h1")
print("primer h1:", h1.text.strip() if h1 else "(sin h1)")

# find_all por clase CSS (en BS4: class_ porque class es keyword de Python)
items = soup.find_all("li", class_="item")
print("items encontrados:", len(items))
for item in items:
    # .get("data-id") lee un atributo; .attrs es el dict completo
    data_id = item.get("data-id")
    precio = item.find("span", class_="precio")
    print(f"  id={data_id} texto={item.get_text(' ', strip=True)} precio={precio.text if precio else '?'}")

# ============================
# 🔹 Atributos y enlaces
# ============================
print("\n--- Links: texto + href ---")

for a in soup.find_all("a"):
    href = a.get("href")  # puede ser None si no hay href
    print(" ", a.text.strip(), "→", href)

# og:image (meta property) — útil en SEO / previews
og = soup.find("meta", property="og:image")
print("og:image:", og["content"] if og and og.get("content") else "(no hay)")

# Tip: soup.prettify() imprime HTML indentado (útil para inspeccionar).

# ============================
# 🔹 HTML string en memoria
# ============================
print("\n--- String en memoria ---")

mini = "<div><p id='hola'>Hola <b>mundo</b></p></div>"
s2 = BeautifulSoup(mini, "html.parser")
p = s2.find("p", id="hola")
print("p.text:", p.text if p else None)          # "Hola mundo" (incluye hijos)
print("p attrs:", p.attrs if p else None)        # {'id': 'hola'}

# ============================
# 🔹 GET opcional a example.com
# ============================
print("\n--- Opcional: https://example.com ---")

HEADERS = {"User-Agent": "welcomePy-student/1.0 (learning; contact: local)"}

if requests is None:
    print("Saltando GET: falta requests.")
else:
    try:
        r = requests.get("https://example.com", headers=HEADERS, timeout=10)
        print("status_code:", r.status_code)
        if r.status_code == 200:
            live = BeautifulSoup(r.text, "html.parser")
            print("title:", live.title.text.strip() if live.title else "(sin)")
            print("h1:", live.find("h1").text.strip() if live.find("h1") else "(sin)")
    except requests.RequestException as exc:
        print("Red no disponible:", type(exc).__name__)

# ============================
# 🔹 Resumen
# ============================
# - BeautifulSoup(html, "html.parser")
# - find / find_all(tag, class_="...", id="...")
# - .text / .get_text(strip=True) → texto visible
# - .get("href") / .attrs → atributos
# - Mejor que regex para HTML real (estructura + tolerancia)
