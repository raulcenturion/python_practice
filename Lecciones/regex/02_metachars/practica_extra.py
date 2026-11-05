# Práctica extra — enmascarar
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r regex/02 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert enmascarar('4242424242424242') == '************4242'


def prueba_1():
    assert solo_digitos('123') and not solo_digitos('12a') and not solo_digitos('')


def enmascarar(numero):
    """Si el texto tiene 4 dígitos o menos, devolvelo igual. Si tiene más, asteriscos y los últimos 4. Ejemplo: enmascarar('4242424242424242') termina en 4242"""
    raise NotImplementedError


import re


def solo_digitos(texto):
    raise NotImplementedError


PRUEBAS = [
    ("enmascarar", prueba_0),
    ("solo_digitos", prueba_1),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
