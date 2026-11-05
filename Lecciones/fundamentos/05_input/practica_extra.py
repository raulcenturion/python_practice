# Práctica extra — input
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 05 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert parsear_alta('Ana,1500') == {'nombre': 'Ana', 'centavos': 1500}


def prueba_1():
    assert opcion_menu('2') == 'extraer' and opcion_menu('9') == 'invalida'


def prueba_2():
    assert confirmar(' S ') and not confirmar('no')


def parsear_alta(linea):
    """La línea es 'nombre,centavos'. Devolvé un dict con esas claves. El monto es int. Ejemplo: parsear_alta('Ana,1500')"""
    raise NotImplementedError


def opcion_menu(texto):
    """1 es consultar, 2 es extraer, 3 es salir. Otro texto devuelve 'invalida'. Ejemplo: opcion_menu('2') → 'extraer'"""
    raise NotImplementedError


def confirmar(texto):
    """True si el texto, sin espacios y en minúscula, es 's' o 'si'. Ejemplo: confirmar(' S ') es True"""
    raise NotImplementedError


PRUEBAS = [
    ("parsear_alta", prueba_0),
    ("opcion_menu", prueba_1),
    ("confirmar", prueba_2),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
