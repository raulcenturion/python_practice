# Práctica extra — una clave de cajero
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r regex/03 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert clave_valida('1234') and not clave_valida('123') and not clave_valida('1234567')


import re


def clave_valida(texto):
    raise NotImplementedError


PRUEBAS = [
    ("clave_valida", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
