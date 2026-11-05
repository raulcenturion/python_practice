# Práctica extra — presupuesto
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r Lecciones/integradores/00_repaso_presupuesto_cli/practica_extra.py

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert balance([('ingreso', 100), ('egreso', 40)]) == 60


def balance(filas):
    """Ingresos menos egresos. Cada fila es ('ingreso', monto) o ('egreso', monto). Ejemplo: balance([('ingreso', 100), ('egreso', 40)]) → 60"""
    raise NotImplementedError


PRUEBAS = [
    ("balance", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
