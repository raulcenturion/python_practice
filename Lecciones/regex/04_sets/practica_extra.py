# Práctica extra — un alias de cuenta
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r regex/04 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert alias_ok('ana1') and not alias_ok('1ana') and not alias_ok('ab')


import re


def alias_ok(texto):
    raise NotImplementedError


PRUEBAS = [
    ("alias_ok", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
