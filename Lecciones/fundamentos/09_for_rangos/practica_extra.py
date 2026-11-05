# Práctica extra — for y range
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 09 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert indices_pares(['a', 'b', 'c', 'd']) == ['a', 'c']


def prueba_1():
    assert tabla(2)[0] == '2 x 1 = 2' and tabla(2)[-1] == '2 x 10 = 20'


def prueba_2():
    assert sumar_pares([1, 2], [10, 20]) == [11, 22]


def indices_pares(items):
    """Devolvé los elementos que están en índice par: 0, 2, 4... Ejemplo: indices_pares(['a', 'b', 'c', 'd']) → ['a', 'c']"""
    raise NotImplementedError


def tabla(n):
    """Devolvé las 10 filas 'n x i = r' para i de 1 a 10. Ejemplo: tabla(2)[0] → '2 x 1 = 2'"""
    raise NotImplementedError


def sumar_pares(a, b):
    """Sumá elemento a elemento dos listas del mismo largo. Ejemplo: sumar_pares([1, 2], [10, 20]) → [11, 22]"""
    raise NotImplementedError


PRUEBAS = [
    ("indices_pares", prueba_0),
    ("tabla", prueba_1),
    ("sumar_pares", prueba_2),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
