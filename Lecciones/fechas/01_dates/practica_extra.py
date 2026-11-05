# Práctica extra — fechas
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r fechas/01 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    from datetime import date
    assert vigente(2030, 1, date(2026, 5, 1)) and not vigente(2020, 1, date(2026, 5, 1))


def prueba_1():
    from datetime import date
    assert es_habil(date(2026, 5, 4)) and not es_habil(date(2026, 5, 9))


from datetime import date


def vigente(anio, mes, hoy):
    raise NotImplementedError


def es_habil(dia):
    """True de lunes a viernes. Ejemplo: un sábado es False"""
    raise NotImplementedError


PRUEBAS = [
    ("vigente", prueba_0),
    ("es_habil", prueba_1),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
