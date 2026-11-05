# Práctica extra — archivos y JSON
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 15 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    import tempfile, os
    ruta = os.path.join(tempfile.gettempdir(), 'extra_movs.json')
    assert guardar_y_leer(ruta, [{'monto': 100}]) == [{'monto': 100}]


def prueba_1():
    assert total_json([{'monto': 10}, {'monto': 5}]) == 15


import json
from pathlib import Path


def guardar_y_leer(ruta, movimientos):
    raise NotImplementedError


def total_json(movimientos):
    """Sumá la clave monto de cada dict. Ejemplo: total_json([{'monto': 10}, {'monto': 5}]) → 15"""
    raise NotImplementedError


PRUEBAS = [
    ("guardar_y_leer", prueba_0),
    ("total_json", prueba_1),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
