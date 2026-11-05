# Práctica extra — tareas de un día
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r Lecciones/integradores/02_gestor_tareas/practica_extra.py

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert pendientes_hasta([{'titulo': 'a', 'vence': '2026-01-01', 'hecha': False}, {'titulo': 'b', 'vence': '2026-01-01', 'hecha': True}], '2026-01-02') == [{'titulo': 'a', 'vence': '2026-01-01', 'hecha': False}]


def pendientes_hasta(tareas, dia):
    """Las no hechas con vence <= dia. Hecha es la clave hecha, un bool. Ejemplo: una hecha no entra"""
    raise NotImplementedError


PRUEBAS = [
    ("pendientes_hasta", prueba_0),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
