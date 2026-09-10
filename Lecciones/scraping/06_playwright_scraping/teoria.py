# ============================
# 📘 Playwright scraping — ejemplo sync que funciona
# ============================
# Objetivo: scrapear una página estable (example.com) con el navegador.
# Selectores CSS simples (no XPath frágiles de blogs que cambian).
#
# Tip: headless=True (rápido / CI) vs headless=False (ves clicks).
# Si Playwright no está → salimos con mensaje, sin crash.

from __future__ import annotations

print("--- Playwright scraping ---")
print("Instalación: pip install playwright && playwright install chromium")

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sync_playwright = None  # type: ignore[assignment]
    print("Playwright no instalado → demo omitida (OK).")


def scrape_example(headless: bool = True) -> dict:
    """Abre example.com y extrae title, h1 y links.

    Retorna un dict simple (fácil de testear / imprimir).
    """
    if sync_playwright is None:
        raise ImportError("Falta playwright")

    with sync_playwright() as p:
        # Tip: headless=False + slow_mo=200 ayuda a depurar.
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        # wait_until=domcontentloaded: no espera imágenes/redes innecesarias
        page.goto("https://example.com", wait_until="domcontentloaded")

        title = page.title()
        # CSS locator (estable en example.com)
        h1 = page.locator("h1").first.inner_text()

        # Todos los <a> visibles
        links = page.locator("a")
        hrefs: list[str] = []
        for i in range(links.count()):
            href = links.nth(i).get_attribute("href")
            text = links.nth(i).inner_text().strip()
            hrefs.append(f"{text} → {href}")

        # Ejemplo de XPath CORRECTO (si lo necesitás):
        # page.locator("xpath=//h1").inner_text()
        # Evitá xpath rotos tipo './div/' sin nodo válido.

        browser.close()
        return {"title": title, "h1": h1, "links": hrefs}


# ============================
# 🔹 Ética
# ============================
print("\n--- Ética ---")
print("Navegador real = más carga. Pocas páginas, delays, User-Agent default OK.")
print("example.com es estable; blogs/tiendas cambian DOM y rompen demos.")

# ============================
# 🔹 Demo
# ============================
print("\n--- Demo sync (example.com) ---")

if sync_playwright is None:
    print("Saltando scrape: instalá playwright para ver el resultado.")
else:
    try:
        data = scrape_example(headless=True)
        print("title:", data["title"])
        print("h1:", data["h1"])
        print("links:")
        for line in data["links"]:
            print(" ", line)
    except Exception as exc:  # noqa: BLE001
        print("No se pudo scrapear:", type(exc).__name__, exc)
        print("Tip: .venv/bin/playwright install chromium")

# Tip headless vs headed:
#   headless=True  → sin ventana (default en servers)
#   headless=False → ves el Chromium (útil la primera vez)

# ============================
# 🔹 Resumen
# ============================
# - sync_playwright → chromium.launch → page.goto → locator
# - Preferí CSS (h1, a) sobre XPath complejos en demos
# - headless True/False según debug vs automatización
# - ImportError / browser missing → mensaje amable, no crash
