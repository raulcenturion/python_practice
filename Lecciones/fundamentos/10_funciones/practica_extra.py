# Práctica extra — funciones
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 10 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert recortar('tarjeta-visa-oro', 7) == 'tarjeta...' and recortar('hola') == 'hola'


def prueba_1():
    assert aplicar(lambda n: n + 1, [1, 2]) == [2, 3]


def prueba_2():
    assert limitar(5000, 100, 1000) == 1000 and limitar(50, 100, 1000) == 100


def recortar(texto, n=10):
    """Si el texto mide más que n, devolvé los primeros n caracteres más '...'. Si no, el texto entero. n vale 10 si no lo pasan. Ejemplo: recortar('tarjeta-visa-oro', 7) → 'tarjeta...'"""
    raise NotImplementedError


def aplicar(fn, valores):
    """Devolvé la lista de fn(x) para cada x. Ejemplo: aplicar(lambda n: n + 1, [1, 2]) → [2, 3]"""
    raise NotImplementedError


def limitar(monto, minimo, maximo):
    """Devolvé monto si está entre minimo y maximo. Si se pasa, el tope de ese lado. Ejemplo: limitar(5000, 100, 1000) → 1000"""
    raise NotImplementedError


PRUEBAS = [
    ("recortar", prueba_0),
    ("aplicar", prueba_1),
    ("limitar", prueba_2),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
