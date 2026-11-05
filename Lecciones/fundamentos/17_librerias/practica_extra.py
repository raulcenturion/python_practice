# Práctica extra — biblioteca estándar
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 17 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert sumar_plata(['0.10', '0.20']) == '0.30'


def prueba_1():
    assert sufijo('extracto.csv') == '.csv'


from decimal import Decimal


def sumar_plata(textos):
    raise NotImplementedError


from pathlib import Path


def sufijo(nombre):
    raise NotImplementedError


PRUEBAS = [
    ("sumar_plata", prueba_0),
    ("sufijo", prueba_1),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
