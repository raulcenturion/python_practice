# Práctica extra — invertir un dict
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r logica/04 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert invertir({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}


def prueba_1():
    assert faltantes({'pan': 1}, {'pan': 2, 'leche': 1}) == ['leche']


def invertir(tabla):
    """Devolvé un dict nuevo con claves y valores cambiados. Los valores son únicos. Ejemplo: invertir({'a': 1}) → {1: 'a'}"""
    raise NotImplementedError


def faltantes(stock, pedido):
    """Claves de pedido que no están en stock. Ejemplo: faltantes({'pan': 1}, {'pan': 2, 'leche': 1}) → ['leche']"""
    raise NotImplementedError


PRUEBAS = [
    ("invertir", prueba_0),
    ("faltantes", prueba_1),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
