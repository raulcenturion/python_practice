# ============================
# 📝 Ejercicios: Wiki scraper
# 📘 Teoría: teoria.py (misma carpeta)
# ============================
# Correr:  .venv/bin/python Lecciones/scraping/03_wiki_scraper/practica.py

from __future__ import annotations

from urllib.parse import urljoin

from bs4 import BeautifulSoup

# 🔸 Ejemplo:
# from urllib.parse import urljoin
# print(urljoin("https://en.wikipedia.org/wiki/X", "/wiki/Y"))

HTML_ARTICULO = """
<html>
<head>
  <meta property="og:image" content="https://example.com/og.png">
</head>
<body>
  <h1>Artículo demo</h1>
  <a href="/wiki/A">A</a>
  <a href="https://example.com/b">B</a>
</body>
</html>
"""


# ============================
# ENUNCIADOS
# ============================

def ejercicio_1_h1() -> None:
    # ENUNCIADO:
    # Parseá HTML_ARTICULO e imprimí el texto del primer <h1>.
    #
    # GUÍA:
    # soup = BeautifulSoup(HTML_ARTICULO, "html.parser")
    # print(soup.find("h1").get_text(strip=True))
    #
    # TIP:
    # get_text(strip=True) limpia espacios alrededor.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1")


def ejercicio_2_links_absolutos() -> None:
    # ENUNCIADO:
    # Listá todos los href como URL absolutas usando urljoin.
    # Base: "https://en.wikipedia.org/wiki/Demo"
    #
    # GUÍA:
    # base = "https://en.wikipedia.org/wiki/Demo"
    # for a in soup.find_all("a", href=True):
    #     print(urljoin(base, a["href"]))
    #
    # TIP:
    # href="/wiki/A" + base → https://en.wikipedia.org/wiki/A

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2")


def ejercicio_3_og_image() -> None:
    # ENUNCIADO:
    # Extraé meta property="og:image" y mostrá su content.
    #
    # GUÍA:
    # og = soup.find("meta", property="og:image")
    # print(og.get("content") if og else "sin og:image")
    #
    # TIP:
    # Open Graph define previews al compartir el link.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 3")


def ejercicio_4_funcion_scrape() -> None:
    # ENUNCIADO:
    # Escribí scrape_page(url=None, html=None) -> dict con keys:
    #   h1 (list[str]), links (list[str]), og_image (str|None)
    # Probala con html=HTML_ARTICULO y url base inventada.
    # (Opcional) Si tenés red: scrape_page(url="https://en.wikipedia.org/wiki/Python")
    #
    # GUÍA:
    # Reutilizá la idea de teoria.py: BeautifulSoup + urljoin + find meta.
    #
    # TIP:
    # Si html y url son None → raise ValueError.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 4")


# ============================
# Runner
# ============================
if __name__ == "__main__":
    ejercicios = [
        ("1", ejercicio_1_h1),
        ("2", ejercicio_2_links_absolutos),
        ("3", ejercicio_3_og_image),
        ("4", ejercicio_4_funcion_scrape),
    ]
    for eid, fn in ejercicios:
        print(f"\n=== Ejercicio {eid} ===")
        try:
            fn()
        except NotImplementedError as e:
            print(f"⏳ Pendiente: {e}")
            print("Leé ENUNCIADO / GUÍA / TIP arriba y completá '# --- TU SOLUCIÓN ---'.")
