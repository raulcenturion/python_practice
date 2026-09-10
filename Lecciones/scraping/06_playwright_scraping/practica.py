# ============================
# 📝 Ejercicios: Playwright scraping
# 📘 Teoría: teoria.py (misma carpeta)
# ============================
# Correr:  .venv/bin/python Lecciones/scraping/06_playwright_scraping/practica.py

from __future__ import annotations

# 🔸 Ejemplo:
# page.locator("h1").inner_text()
# page.locator("a").count()


# ============================
# ENUNCIADOS
# ============================

def ejercicio_1_abrir_body() -> None:
    # ENUNCIADO:
    # Con Playwright sync, abrí https://example.com y esperá el <body>.
    # Imprimí "body OK" si page.locator("body").count() >= 1.
    # Si falta playwright → mensaje y return (sin crash).
    #
    # GUÍA:
    # try:
    #     from playwright.sync_api import sync_playwright
    # except ImportError:
    #     print("Falta playwright"); return
    # with sync_playwright() as p:
    #     ...
    #     page.goto("https://example.com", wait_until="domcontentloaded")
    #
    # TIP:
    # wait_until="domcontentloaded" suele bastar para example.com.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1")


def ejercicio_2_extraer_h1() -> None:
    # ENUNCIADO:
    # Extraé el texto del h1 con page.locator("h1").first.inner_text().
    #
    # GUÍA:
    # print(page.locator("h1").first.inner_text())
    #
    # TIP:
    # .first evita ambigüedad si hubiera varios h1.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2")


def ejercicio_3_listar_links() -> None:
    # ENUNCIADO:
    # Listá texto + href de todos los <a>.
    # Usá locator("a"), .count(), .nth(i), get_attribute("href").
    #
    # GUÍA:
    # links = page.locator("a")
    # for i in range(links.count()):
    #     print(links.nth(i).inner_text(), links.nth(i).get_attribute("href"))
    #
    # TIP:
    # Preferí CSS. Si usás XPath: xpath=//a[@href] (completo y válido).

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 3")


def ejercicio_4_headless_tip() -> None:
    # ENUNCIADO:
    # Escribí una función scrapear(url, headless=True) que retorne el title.
    # Documentá en un comentario cuándo usar headless=False.
    # Probá con example.com (o skip si no hay playwright).
    #
    # TIP:
    # headless=False + slow_mo=100 → ideal para la primera depuración.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 4")


# ============================
# Runner
# ============================
if __name__ == "__main__":
    ejercicios = [
        ("1", ejercicio_1_abrir_body),
        ("2", ejercicio_2_extraer_h1),
        ("3", ejercicio_3_listar_links),
        ("4", ejercicio_4_headless_tip),
    ]
    for eid, fn in ejercicios:
        print(f"\n=== Ejercicio {eid} ===")
        try:
            fn()
        except NotImplementedError as e:
            print(f"⏳ Pendiente: {e}")
            print("Leé ENUNCIADO / GUÍA / TIP arriba y completá '# --- TU SOLUCIÓN ---'.")
