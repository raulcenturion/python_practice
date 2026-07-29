# ============================
# 🧪 Integrador 03 — Mini API biblioteca (DIFÍCIL)
# 📘 Enunciado: enunciado.md | Tips: tips.md
# ============================
# Creá models.py y app.py. Después completá demo().

from __future__ import annotations

import asyncio


async def demo() -> None:
    print("=== Demo Mini API Biblioteca ===")
    print("Implementá app.py + models.py y esta demo. Si te trabás → tips.md")
    # Placeholder async: reemplazalo por tus await app.handle(...)
    await asyncio.sleep(0)
    # Pasos sugeridos:
    # 1. Crear libro inválido y capturar ValidationError
    # 2. Crear 2 libros válidos con app.handle("POST", "/libros", data=...)
    # 3. Listar GET /libros
    # 4. GET /libros/{libro_id}
    # 5. GET /stats
    # 6. DELETE uno
    # 7. asyncio.gather con dos POST en paralelo


if __name__ == "__main__":
    asyncio.run(demo())
