# Práctica extra — while
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 08 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert cantidad_digitos(1500) == 4


def prueba_1():
    assert mcd(12, 8) == 4


def prueba_2():
    assert billetes(1600) == (1, 1, 1)


def cantidad_digitos(n):
    """Cuántos dígitos tiene un entero positivo. Ejemplo: cantidad_digitos(1500) → 4"""
    raise NotImplementedError


def mcd(a, b):
    """Máximo común divisor con el algoritmo de Euclides. Ejemplo: mcd(12, 8) → 4"""
    raise NotImplementedError


def billetes(monto):
    """Devolvé cuántos billetes de 1000, 500 y 100 se necesitan, en ese orden, como tupla. El monto es múltiplo de 100. Ejemplo: billetes(1600) → (1, 1, 1)"""
    raise NotImplementedError


PRUEBAS = [
    ("cantidad_digitos", prueba_0),
    ("mcd", prueba_1),
    ("billetes", prueba_2),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
