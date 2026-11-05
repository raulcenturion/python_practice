# Práctica extra — repaso corto
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r Lecciones/integradores/00_previo_repaso_fundamentos/practica_extra.py

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert saldo_final(100, [-20, 5]) == 85


def prueba_1():
    assert por_concepto([{'concepto': 'pan', 'monto': 1}, {'concepto': 'pan', 'monto': 2}]) == {'pan': [1, 2]}


def saldo_final(inicial, deltas):
    """Empezá en inicial y sumá cada delta, en orden. Ejemplo: saldo_final(100, [-20, 5]) → 85"""
    raise NotImplementedError


def por_concepto(filas):
    """Agrupá los montos de cada concepto en una lista. Ejemplo: dos 'pan' quedan juntos"""
    raise NotImplementedError


PRUEBAS = [
    ("saldo_final", prueba_0),
    ("por_concepto", prueba_1),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
