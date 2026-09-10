# ============================
# 📝 Ejercicios: Scraping básico (requests + regex)
# 📘 Teoría: teoria.py (misma carpeta)
# ============================
# Correr:  .venv/bin/python Lecciones/scraping/01_basic/practica.py

from __future__ import annotations

from pathlib import Path
import re

DIR = Path(__file__).resolve().parent

# 🔸 Ejemplo (patrón):
# html = "<title>Hola</title>"
# m = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
# print(m.group(1) if m else "sin title")


# ============================
# ENUNCIADOS
# ============================

def ejercicio_1_status_local() -> None:
    # ENUNCIADO:
    # Leé DIR/"sample.html" y "simulá" un status exitoso:
    # imprimí "status_code: 200" y la longitud del HTML (len).
    #
    # GUÍA:
    # 1) texto = (DIR / "sample.html").read_text(encoding="utf-8")
    # 2) print("status_code:", 200)
    # 3) print("len:", len(texto))
    #
    # TIP:
    # Path(__file__).parent apunta a la carpeta de la lección (estable).

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1")


def ejercicio_2_title_regex() -> None:
    # ENUNCIADO:
    # Del sample.html, extráé el <title> con re.search e imprimilo.
    #
    # GUÍA:
    # patrón = r"<title>(.*?)</title>"
    # m = re.search(patrón, html, re.IGNORECASE | re.DOTALL)
    # print(m.group(1).strip())
    #
    # TIP:
    # DOTALL (re.S) hace que . también matchee saltos de línea.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2")


def ejercicio_3_precio_y_links() -> None:
    # ENUNCIADO:
    # 1) Extraé el texto de <p class="precio">…</p> con regex.
    # 2) Contá cuántos "<a " hay (aproximado) con re.findall.
    #
    # GUÍA:
    # precio = re.search(r'<p\s+class="precio">(.*?)</p>', html, re.I | re.S)
    # links = re.findall(r"<a\s", html, re.I)
    #
    # TIP:
    # Esto es frágil a propósito → motivá BeautifulSoup en la lección 02.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 3")


def ejercicio_4_get_opcional() -> None:
    # ENUNCIADO (opcional / red):
    # Hacé GET a https://example.com con User-Agent propio.
    # Imprimí status_code y el <title> con regex.
    # Si falla la red o falta requests, avisá sin crashear.
    #
    # GUÍA:
    # import requests
    # r = requests.get(url, headers={"User-Agent": "..."}, timeout=10)
    #
    # TIP:
    # try/except requests.RequestException → mensaje amigable.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 4")


# ============================
# Runner
# ============================
if __name__ == "__main__":
    ejercicios = [
        ("1", ejercicio_1_status_local),
        ("2", ejercicio_2_title_regex),
        ("3", ejercicio_3_precio_y_links),
        ("4", ejercicio_4_get_opcional),
    ]
    for eid, fn in ejercicios:
        print(f"\n=== Ejercicio {eid} ===")
        try:
            fn()
        except NotImplementedError as e:
            print(f"⏳ Pendiente: {e}")
            print("Leé ENUNCIADO / GUÍA / TIP arriba y completá '# --- TU SOLUCIÓN ---'.")
