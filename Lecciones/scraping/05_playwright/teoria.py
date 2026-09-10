# ============================
# 📘 Playwright — automatizar un navegador
# ============================
# Playwright controla Chromium/Firefox/WebKit de verdad (no solo HTTP).
# Sirve para: páginas con mucho JavaScript, clicks, formularios, tests E2E.
#
# Instalación (una vez):
#   .venv/bin/pip install playwright
#   .venv/bin/playwright install chromium
#
# Este archivo NO crashea si Playwright falta: salta el demo con un mensaje.

from __future__ import annotations

import re

print("--- Cómo instalar Playwright ---")
print("1) .venv/bin/pip install playwright")
print("2) .venv/bin/playwright install chromium")
print("3) Correr este archivo de nuevo.")

# ============================
# 🔹 Import defensivo
# ============================
print("\n--- Import ---")

try:
    from playwright.sync_api import sync_playwright, expect
except ImportError:
    sync_playwright = None  # type: ignore[assignment]
    expect = None  # type: ignore[assignment]
    print("Playwright no instalado → demo omitida (OK).")
    print("Tip: pip install playwright && playwright install chromium")
else:
    print("Playwright import OK.")

# ============================
# 🔹 Ética
# ============================
print("\n--- Ética ---")
print("Un navegador real pesa más que requests: andá despacio.")
print("No uses esto para martillar sitios ni saltar paywalls.")

# ============================
# 🔹 Demo sync (estilo script)
# ============================
print("\n--- Demo sync: abrir example.com ---")

if sync_playwright is None:
    print("Saltando demo: falta playwright.")
else:
    try:
        with sync_playwright() as p:
            # headless=True → sin ventana (CI / servers)
            # headless=False → ves el navegador (debug)
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://example.com", wait_until="domcontentloaded")
            title = page.title()
            print("title:", title)
            h1 = page.locator("h1").first
            print("h1:", h1.inner_text())
            browser.close()
    except Exception as exc:  # noqa: BLE001 — browsers pueden faltar
        print("Demo no pudo correr:", type(exc).__name__, exc)
        print("Tip: ¿corriste `playwright install chromium`?")

# ============================
# 🔹 Estilo pytest (funciones test_*)
# ============================
# Con el plugin pytest-playwright, `page` llega como fixture.
# Acá mostramos el esqueleto; no hace falta pytest para leer la idea.


def test_has_title_example(page=None) -> None:
    """Ejemplo estilo pytest: title contiene 'Example'.

    Si corrés este archivo solo, `page` es None y salimos sin error.
    Con pytest + pytest-playwright: page es un Page real.
    """
    if page is None:
        print("(test_has_title_example: sin fixture page → skip)")
        return
    page.goto("https://example.com")
    expect(page).to_have_title(re.compile("Example", re.I))


def test_h1_visible(page=None) -> None:
    if page is None:
        print("(test_h1_visible: sin fixture page → skip)")
        return
    page.goto("https://example.com")
    expect(page.get_by_role("heading", level=1)).to_be_visible()


print("\n--- Esqueleto pytest ---")
test_has_title_example()
test_h1_visible()
print("Tip: para tests reales → pip install pytest pytest-playwright")

# ============================
# 🔹 Resumen
# ============================
# - Playwright = navegador automatizado (JS renderizado)
# - sync_playwright() → launch → new_page → goto → locators
# - headless=True por defecto en CI; False para ver qué pasa
# - try/except ImportError → la lección no se rompe sin el paquete
# - Estilo pytest: test_* + fixture page + expect(...)
