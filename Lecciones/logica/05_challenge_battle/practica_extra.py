# Práctica extra — mejor de tres
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r logica/05 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert mejor_de(['a', 'a', 'b']) == 'a' and mejor_de(['a', 'b']) == 'empate'


def mejor_de(rondas):
    """rondas es una lista de 'a' o 'b'. Devolvé 'a', 'b' o 'empate'. Gana el primero que llega a ganar. Si no, el que tenga más. Si igualan, empate. Ejemplo: mejor_de(['a', 'a', 'b']) → 'a'"""
    raise NotImplementedError


PRUEBAS = [
    ("mejor_de", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
