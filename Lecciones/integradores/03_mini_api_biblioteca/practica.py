# ============================
# 🧪 Integrador 03 — Mini API biblioteca (DIFÍCIL)
# 📘 Enunciado: enunciado.md | Tips: tips.md
# ============================
# Creá models.py y app.py. Después completá demo().

from __future__ import annotations

import asyncio


async def demo() -> None:
    """
    Demo async de la mini API.
    Pasos sugeridos (enunciado.md / tips.md):
    1) Libro inválido → ValidationError
    2) POST de 2 libros válidos
    3) GET /libros
    4) GET /libros/{id}
    5) GET /stats
    6) DELETE uno
    7) asyncio.gather con dos POST en paralelo
    """
    print("=== Demo Mini API Biblioteca ===")
    print("Implementá app.py + models.py y esta demo. Si te trabás → tips.md")
    await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(demo())
