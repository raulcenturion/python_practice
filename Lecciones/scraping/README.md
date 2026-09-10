# Scraping — lecciones

Ruta de estudio: HTTP básico → BeautifulSoup → Wikipedia → CLI SEO → Playwright.

## Dependencias

Desde la raíz del proyecto (`welcomePy`), con el venv activo:

```bash
# HTTP + parseo HTML
.venv/bin/pip install requests beautifulsoup4

# Navegador automatizado (lecciones 05 y 06)
.venv/bin/pip install playwright
.venv/bin/playwright install chromium
```

Sin Playwright, las lecciones 05 y 06 **no deben crashear**: importan con `try/except ImportError` y saltan el demo.

## Cómo correr

```bash
# Teoría (01–04 usan red solo de forma opcional / estable: example.com, Wikipedia)
.venv/bin/python Lecciones/scraping/01_basic/teoria.py
.venv/bin/python Lecciones/scraping/02_beautiful/teoria.py
.venv/bin/python Lecciones/scraping/03_wiki_scraper/teoria.py
.venv/bin/python Lecciones/scraping/04_seo_cli/teoria.py --file Lecciones/scraping/04_seo_cli/sample.html
.venv/bin/python Lecciones/scraping/04_seo_cli/teoria.py --url https://example.com

.venv/bin/python Lecciones/scraping/05_playwright/teoria.py
.venv/bin/python Lecciones/scraping/06_playwright_scraping/teoria.py

# Práctica (stubs con NotImplementedError → mensaje "Pendiente")
.venv/bin/python Lecciones/scraping/01_basic/practica.py
```

Cada carpeta `0N_*` tiene `teoria.py` (demostración) y `practica.py` (ejercicios guiados).
En 01, 02 y 04 hay `sample.html` locales para demos estables sin depender de tiendas en vivo.

## Ética (resumen)

- Respetá `robots.txt` y los términos del sitio.
- Identificá tu cliente con un `User-Agent` claro.
- No martillés servidores: pausas, pocos requests, cacheá cuando puedas.
- Preferí HTML local / sitios estables (`example.com`, Wikipedia) para aprender.
- Las tiendas (Apple, Amazon, etc.) cambian el HTML a menudo: no sirven como demos obligatorias.
