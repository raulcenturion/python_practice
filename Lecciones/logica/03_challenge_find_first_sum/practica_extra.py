# Práctica extra — los dos más cercanos
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r logica/03 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert mejor_par([3, 8, 5, 1], 10) == (1, 8)


def mejor_par(numeros, meta):
    """Devolvé (a, b) con a <= b, a + b <= meta, y esa suma la más alta posible. None si no hay par. Ejemplo: mejor_par([3, 8, 5, 1], 10) → (1, 8) no, 5+3=8 y 1+8=9, gana (1, 8)"""
    raise NotImplementedError


PRUEBAS = [
    ("mejor_par", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
