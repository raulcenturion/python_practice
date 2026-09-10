# ============================
# 📝 Ejercicios: Playwright (intro)
# 📘 Teoría: teoria.py (misma carpeta)
# ============================
# Correr:  .venv/bin/python Lecciones/scraping/05_playwright/practica.py
# Requiere (para completar): pip install playwright && playwright install chromium

from __future__ import annotations

# 🔸 Ejemplo:
# try:
#     from playwright.sync_api import sync_playwright
# except ImportError:
#     sync_playwright = None


# ============================
# ENUNCIADOS
# ============================

def ejercicio_1_import_defensivo() -> None:
    # ENUNCIADO:
    # Intentá importar sync_playwright.
    # Si falta → print("Instalá playwright") y return.
    # Si está → print("OK", sync_playwright).
    #
    # GUÍA:
    # try:
    #     from playwright.sync_api import sync_playwright
    # except ImportError:
    #     print("Instalá playwright")
    #     return
    #
    # TIP:
    # Así la práctica no crashea en máquinas sin Playwright.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1")


def ejercicio_2_abrir_example() -> None:
    # ENUNCIADO:
    # Con sync API: abrí https://example.com en headless, imprimí page.title()
    # y el texto del h1. Cerrá el browser.
    # Si no hay playwright o falla el browser → mensaje, no traceback fatal.
    #
    # GUÍA:
    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=True)
    #     page = browser.new_page()
    #     page.goto("https://example.com")
    #     print(page.title())
    #     print(page.locator("h1").inner_text())
    #     browser.close()
    #
    # TIP:
    # headless=False para ver la ventana (debug).

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2")


def ejercicio_3_esqueleto_pytest() -> None:
    # ENUNCIADO:
    # Escribí una función test_title(page=None) que:
    #   - si page is None → print skip y return
    #   - si no → page.goto example.com y assert "Example" in page.title()
    # Llamala sin page (debe skipear limpio).
    #
    # GUÍA / TIP:
    # Con pytest-playwright, `page` llega como fixture automáticamente.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 3")


# ============================
# Runner
# ============================
if __name__ == "__main__":
    ejercicios = [
        ("1", ejercicio_1_import_defensivo),
        ("2", ejercicio_2_abrir_example),
        ("3", ejercicio_3_esqueleto_pytest),
    ]
    for eid, fn in ejercicios:
        print(f"\n=== Ejercicio {eid} ===")
        try:
            fn()
        except NotImplementedError as e:
            print(f"⏳ Pendiente: {e}")
            print("Leé ENUNCIADO / GUÍA / TIP arriba y completá '# --- TU SOLUCIÓN ---'.")
