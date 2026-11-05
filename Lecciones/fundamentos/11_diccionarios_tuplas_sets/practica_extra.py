# Práctica extra — dict, tupla y set
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 11 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert frecuencia(['a', 'b', 'a']) == {'a': 2, 'b': 1}


def prueba_1():
    assert primer_par([2, 7, 11, 15], 9) == (0, 1) and primer_par([1, 2], 10) is None


def prueba_2():
    assert comunes([1, 2, 2], [2, 3]) == [2]


def frecuencia(valores):
    """Dict con cuántas veces aparece cada valor. Ejemplo: frecuencia(['a', 'b', 'a']) → {'a': 2, 'b': 1}"""
    raise NotImplementedError


def primer_par(numeros, meta):
    """Índices i < j del primer par que suma meta, recorriendo desde la izquierda. Si no hay, None. Un dict recuerda el índice de cada número ya visto. Ejemplo: primer_par([2, 7, 11, 15], 9) → (0, 1)"""
    raise NotImplementedError


def comunes(a, b):
    """Lista ordenada de los números que están en las dos listas. Ejemplo: comunes([1, 2, 2], [2, 3]) → [2]"""
    raise NotImplementedError


PRUEBAS = [
    ("frecuencia", prueba_0),
    ("primer_par", prueba_1),
    ("comunes", prueba_2),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
