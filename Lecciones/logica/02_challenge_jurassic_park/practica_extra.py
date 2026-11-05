# Práctica extra — racha de gastos
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r logica/02 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert racha([1, -2, 3, 4]) == 7 and racha([-5, -1]) == -1


def racha(numeros):
    """La suma consecutiva más alta. La lista tiene al menos un número. Ejemplo: racha([1, -2, 3, 4]) → 7"""
    raise NotImplementedError


PRUEBAS = [
    ("racha", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
