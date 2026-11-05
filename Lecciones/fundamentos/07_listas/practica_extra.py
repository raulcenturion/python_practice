# Práctica extra — listas
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 07 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert rotar([1, 2, 3, 4], 1) == [4, 1, 2, 3] and rotar([1, 2, 3, 4], 0) == [1, 2, 3, 4]


def prueba_1():
    assert ventana_maxima([1, 3, 2, 5], 2) == 7


def prueba_2():
    assert unicos([2, 1, 2, 3, 1]) == [2, 1, 3]


def rotar(numeros, k):
    """Devolvé una lista nueva con los últimos k elementos al frente. No modifiques la original. Ejemplo: rotar([1, 2, 3, 4], 1) → [4, 1, 2, 3]"""
    raise NotImplementedError


def ventana_maxima(numeros, k):
    """La suma más alta de k elementos seguidos. k cabe en la lista. Ejemplo: ventana_maxima([1, 3, 2, 5], 2) → 7"""
    raise NotImplementedError


def unicos(numeros):
    """Devolvé los valores una sola vez, en el orden de la primera aparición. Ejemplo: unicos([2, 1, 2, 3, 1]) → [2, 1, 3]"""
    raise NotImplementedError


PRUEBAS = [
    ("rotar", prueba_0),
    ("ventana_maxima", prueba_1),
    ("unicos", prueba_2),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
