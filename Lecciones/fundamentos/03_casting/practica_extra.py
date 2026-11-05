# Práctica extra — casting
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 03 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert a_centavos('12.50') == 1250 and a_centavos('0.05') == 5


def prueba_1():
    assert a_entero_seguro('42') == 42 and a_entero_seguro('x') is None


def prueba_2():
    assert si_no('SI') is True and si_no('no') is False and si_no('quizas') is None


def a_centavos(texto):
    """El texto es pesos con punto y dos decimales. Devolvé el entero en centavos. Ejemplo: a_centavos('12.50') → 1250"""
    raise NotImplementedError


def a_entero_seguro(texto):
    """Devolvé el int, o None si el texto no es un entero. Ejemplo: a_entero_seguro('42') → 42; a_entero_seguro('x') → None"""
    raise NotImplementedError


def si_no(texto):
    """Aceptá 'si' o 'no' en cualquier mayúscula. Otro texto devuelve None. Ejemplo: si_no('SI') → True"""
    raise NotImplementedError


PRUEBAS = [
    ("a_centavos", prueba_0),
    ("a_entero_seguro", prueba_1),
    ("si_no", prueba_2),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
