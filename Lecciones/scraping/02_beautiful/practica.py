# ============================
# 📝 Ejercicios: BeautifulSoup
# 📘 Teoría: teoria.py (misma carpeta)
# ============================
# Correr:  .venv/bin/python Lecciones/scraping/02_beautiful/practica.py

from __future__ import annotations

from pathlib import Path

from bs4 import BeautifulSoup

DIR = Path(__file__).resolve().parent

# 🔸 Ejemplo:
# soup = BeautifulSoup("<h1>Hola</h1>", "html.parser")
# print(soup.find("h1").text)


# ============================
# ENUNCIADOS
# ============================

def ejercicio_1_title() -> None:
    # ENUNCIADO:
    # Parseá DIR/"sample.html" con BeautifulSoup e imprimí soup.title.text.
    #
    # GUÍA:
    # html = (DIR / "sample.html").read_text(encoding="utf-8")
    # soup = BeautifulSoup(html, "html.parser")
    # print(soup.title.text)
    #
    # TIP:
    # Si title puede faltar:  soup.title.text if soup.title else "(sin)"

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1")


def ejercicio_2_items() -> None:
    # ENUNCIADO:
    # Listá cada <li class="item">: data-id y el texto del <span class="precio">.
    #
    # GUÍA:
    # for li in soup.find_all("li", class_="item"):
    #     print(li.get("data-id"), li.find("span", class_="precio").text)
    #
    # TIP:
    # En BS4 el kwarg de clase CSS es class_ (class es palabra reservada).

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2")


def ejercicio_3_links() -> None:
    # ENUNCIADO:
    # Imprimí texto y href de todos los <a>.
    # También imprimí el content de meta property="og:image" si existe.
    #
    # GUÍA:
    # for a in soup.find_all("a"):
    #     print(a.text.strip(), a.get("href"))
    # og = soup.find("meta", property="og:image")
    #
    # TIP:
    # og["content"] puede lanzar KeyError → preferí og.get("content").

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 3")


def ejercicio_4_example_opcional() -> None:
    # ENUNCIADO (opcional / red):
    # GET https://example.com → BeautifulSoup → imprimí title y primer h1.
    # Si falla requests/red, avisá sin crashear.
    #
    # GUÍA:
    # headers = {"User-Agent": "welcomePy-student/1.0"}
    # r = requests.get(..., timeout=10)
    #
    # TIP:
    # No uses tiendas reales como demo obligatorio: el HTML cambia seguido.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 4")


# ============================
# Runner
# ============================
if __name__ == "__main__":
    ejercicios = [
        ("1", ejercicio_1_title),
        ("2", ejercicio_2_items),
        ("3", ejercicio_3_links),
        ("4", ejercicio_4_example_opcional),
    ]
    for eid, fn in ejercicios:
        print(f"\n=== Ejercicio {eid} ===")
        try:
            fn()
        except NotImplementedError as e:
            print(f"⏳ Pendiente: {e}")
            print("Leé ENUNCIADO / GUÍA / TIP arriba y completá '# --- TU SOLUCIÓN ---'.")
