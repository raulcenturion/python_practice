# Práctica extra — variables
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 04 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert aplicar(1000, -200) == 800


def prueba_1():
    assert intercambiar(1, 2) == (2, 1)


def prueba_2():
    assert con_comision(1000) == 990 and con_comision(50) == 50


def aplicar(saldo, delta):
    """Sumá delta al saldo y devolvé el saldo nuevo. No uses una variable global. Ejemplo: aplicar(1000, -200) → 800"""
    raise NotImplementedError


def intercambiar(a, b):
    """Devolvé la tupla (b, a). Ejemplo: intercambiar(1, 2) → (2, 1)"""
    raise NotImplementedError


def con_comision(monto):
    """Restá el 1% entero del monto (división entera) y devolvé lo que queda. 1000 → 990. Ejemplo: con_comision(1000) → 990"""
    raise NotImplementedError


PRUEBAS = [
    ("aplicar", prueba_0),
    ("intercambiar", prueba_1),
    ("con_comision", prueba_2),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
