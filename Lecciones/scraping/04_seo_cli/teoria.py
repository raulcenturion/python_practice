# ============================
# 📘 SEO CLI — title + h1 con argparse
# ============================
# Mini herramienta de terminal:
#   - --file sample.html  (demo estable, sin red)
#   - --url https://example.com  (opcional)
# Chequea: longitud del <title> y cantidad de <h1>.
#
# Tip: los colores ANSI son opcionales; en CI/logs a veces molestan.

from __future__ import annotations

import argparse
from pathlib import Path

from bs4 import BeautifulSoup

try:
    import requests
except ImportError:
    requests = None  # type: ignore[assignment]

DIR = Path(__file__).resolve().parent

# Códigos ANSI (opcional). Si no querés color: dejá strings vacíos.
USE_COLOR = True
GREEN = "\033[32m" if USE_COLOR else ""
RED = "\033[31m" if USE_COLOR else ""
BLUE = "\033[34m" if USE_COLOR else ""
RESET = "\033[0m" if USE_COLOR else ""

HEADERS = {"User-Agent": "welcomePy-student/1.0 (seo-cli; contact: local)"}
TITLE_MAX = 70  # regla práctica (no ley): titles largos se cortan en SERP


def cargar_html(file: Path | None, url: str | None) -> tuple[str, str]:
    """Devuelve (html, etiqueta_fuente)."""
    if file is not None:
        return file.read_text(encoding="utf-8"), str(file)
    if url is None:
        raise ValueError("Pasá --file o --url")
    if requests is None:
        raise ImportError("Para --url necesitás: pip install requests")
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    return r.text, url


def analizar_seo(html: str, fuente: str) -> None:
    soup = BeautifulSoup(html, "html.parser")
    print(f"{BLUE}Revisando:{RESET} {fuente}")
    print("\nSEO básico:")

    # --- title ---
    title = soup.title.get_text(strip=True) if soup.title else ""
    if not title:
        print(f"{RED}❌  No hay <title>{RESET}")
    else:
        print(f"Title ({len(title)} chars): {title}")
        if len(title) <= TITLE_MAX:
            print(f"{GREEN}✅  Longitud de title OK (≤ {TITLE_MAX}){RESET}")
        else:
            print(f"{RED}⚠️  Title largo (>{TITLE_MAX}); puede truncarse en buscadores{RESET}")

    # --- h1 ---
    h1s = [h.get_text(strip=True) for h in soup.find_all("h1")]
    if not h1s:
        print(f"{RED}❌  No hay <h1>{RESET}")
    elif len(h1s) > 1:
        print(f"{RED}❌  Hay {len(h1s)} h1 (ideal: 1){RESET}")
        for t in h1s:
            print("   ·", t)
    else:
        print(f"{GREEN}✅  Un solo h1:{RESET} {h1s[0]}")

    # Tip: meta description, h2, alt de imágenes… se pueden sumar igual.


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Chequeo SEO básico: title length + cantidad de h1.",
    )
    g = p.add_mutually_exclusive_group(required=False)
    g.add_argument("--file", "-f", type=Path, help="HTML local (recomendado)")
    g.add_argument("--url", "-u", type=str, help="URL a pedir (opcional)")
    p.add_argument(
        "--no-color",
        action="store_true",
        help="Desactiva colores ANSI",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    global USE_COLOR, GREEN, RED, BLUE, RESET

    args = build_parser().parse_args(argv)
    if args.no_color:
        USE_COLOR = False
        GREEN = RED = BLUE = RESET = ""

    # Default pedagógico: sample.html al lado de este archivo
    file = args.file
    url = args.url
    if file is None and url is None:
        file = DIR / "sample.html"
        print("(sin args → usando sample.html local)\n")

    try:
        html, fuente = cargar_html(file, url)
    except Exception as exc:  # noqa: BLE001
        print("No se pudo cargar HTML:", type(exc).__name__, exc)
        return 1

    analizar_seo(html, fuente)
    return 0


# ============================
# 🔹 Ética
# ============================
# --file no toca la red. --url: User-Agent + timeout, no martillar.

# ============================
# 🔹 Resumen
# ============================
# - argparse: --file / --url / --no-color
# - title ≤ ~70 chars; idealmente 1 solo <h1>
# - ANSI es cosmético (Tip: --no-color para logs limpios)
# - Preferí HTML local para demos; example.com si querés red estable

if __name__ == "__main__":
    raise SystemExit(main())
