# Práctica extra — funciones de orden superior
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 14 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert mayores([100, 500, 200], 150) == [500, 200]


def prueba_1():
    original = [{'monto': 30}, {'monto': 10}]
    assert ordenar_por_monto(original)[0]['monto'] == 10 and original[0]['monto'] == 30


def prueba_2():
    assert en_mayuscula(['ana', 'Sol']) == ['ANA', 'SOL']


def mayores(montos, piso):
    """Devolvé los montos estrictamente mayores que el piso, en el mismo orden. Ejemplo: mayores([100, 500, 200], 150) → [500, 200]"""
    raise NotImplementedError


def ordenar_por_monto(filas):
    """Lista de dicts ordenada por la clave 'monto', de menor a mayor. No modifiques la lista original: devolvé otra. Ejemplo: el de monto 10 queda primero"""
    raise NotImplementedError


def en_mayuscula(textos):
    """Devolvé cada texto en mayúscula, en el mismo orden. Ejemplo: en_mayuscula(['ana']) → ['ANA']"""
    raise NotImplementedError


PRUEBAS = [
    ("mayores", prueba_0),
    ("ordenar_por_monto", prueba_1),
    ("en_mayuscula", prueba_2),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
