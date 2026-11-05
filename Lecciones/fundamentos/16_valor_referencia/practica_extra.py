# Práctica extra — valor y referencia
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 16 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    base = [1, 2]
    assert duplicar(base) == [1, 2, 1, 2] and base == [1, 2]


def prueba_1():
    base = ['a']
    assert anotar_copia(base, 'b') == ['a', 'b'] and base == ['a']


def duplicar(numeros):
    """Devolvé una lista nueva con los elementos repetidos dos veces. La original queda igual. Ejemplo: duplicar([1, 2]) → [1, 2, 1, 2]"""
    raise NotImplementedError


def anotar_copia(items, texto):
    """Devolvé una lista nueva con el texto agregado al final. No uses append sobre la lista recibida. Ejemplo: anotar_copia(['a'], 'b') → ['a', 'b']"""
    raise NotImplementedError


PRUEBAS = [
    ("duplicar", prueba_0),
    ("anotar_copia", prueba_1),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
