# ============================
# 📝 Ejercicios: SEO CLI
# 📘 Teoría: teoria.py (misma carpeta)
# ============================
# Correr:  .venv/bin/python Lecciones/scraping/04_seo_cli/practica.py

from __future__ import annotations

import argparse
from pathlib import Path

from bs4 import BeautifulSoup

DIR = Path(__file__).resolve().parent

# 🔸 Ejemplo:
# parser = argparse.ArgumentParser()
# parser.add_argument("--file", type=Path)
# args = parser.parse_args(["--file", "sample.html"])


# ============================
# ENUNCIADOS
# ============================

def ejercicio_1_title_local() -> None:
    # ENUNCIADO:
    # Leé DIR/"sample.html", parseá con BeautifulSoup e imprimí:
    #   - el title
    #   - len(title) y si es ≤ 70
    #
    # GUÍA:
    # soup = BeautifulSoup((DIR/"sample.html").read_text(...), "html.parser")
    # title = soup.title.get_text(strip=True)
    #
    # TIP:
    # 70 es una regla práctica de SERP, no una ley.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1")


def ejercicio_2_contar_h1() -> None:
    # ENUNCIADO:
    # Contá los <h1> del sample.html.
    # Imprimí OK si hay exactamente 1; si no, avisá.
    #
    # GUÍA:
    # h1s = soup.find_all("h1")
    # print(len(h1s))
    #
    # TIP:
    # Ideal SEO on-page: un h1 principal por página.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2")


def ejercicio_3_argparse_cli() -> None:
    # ENUNCIADO:
    # Armá un argparse con --file y --url (mutuamente exclusivos, o default file).
    # Si corrés este ejercicio, parseá sys.argv simulando:
    #   ["--file", str(DIR / "sample.html")]
    # y llamá a tu función de análisis.
    #
    # GUÍA:
    # p = argparse.ArgumentParser()
    # g = p.add_mutually_exclusive_group()
    # g.add_argument("--file", type=Path)
    # g.add_argument("--url")
    # args = p.parse_args([...])
    #
    # TIP:
    # Colores ANSI son opcionales; agregá --no-color si querés.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 3")


def ejercicio_4_url_opcional() -> None:
    # ENUNCIADO (opcional / red):
    # Pedí https://example.com con User-Agent y reportá title + #h1.
    # Si falta red/requests, avisá sin crashear.
    #
    # TIP:
    # No uses tiendas reales como demo obligatorio.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 4")


# ============================
# Runner
# ============================
if __name__ == "__main__":
    ejercicios = [
        ("1", ejercicio_1_title_local),
        ("2", ejercicio_2_contar_h1),
        ("3", ejercicio_3_argparse_cli),
        ("4", ejercicio_4_url_opcional),
    ]
    for eid, fn in ejercicios:
        print(f"\n=== Ejercicio {eid} ===")
        try:
            fn()
        except NotImplementedError as e:
            print(f"⏳ Pendiente: {e}")
            print("Leé ENUNCIADO / GUÍA / TIP arriba y completá '# --- TU SOLUCIÓN ---'.")
