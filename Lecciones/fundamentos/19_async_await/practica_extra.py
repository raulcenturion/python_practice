# Práctica extra — async y await
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 19 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    import asyncio
    assert asyncio.run(sumar_esperas(2, 3)) == 10


import asyncio


async def dos_veces(n):
    await asyncio.sleep(0)
    return n * 2


async def sumar_esperas(a, b):
    raise NotImplementedError


PRUEBAS = [
    ("sumar_esperas", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
