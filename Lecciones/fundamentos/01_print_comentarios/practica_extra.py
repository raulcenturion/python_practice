# Práctica extra — print y comentarios
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 01 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert linea_ticket('Cafe', 800) == 'Cafe: 800'


def prueba_1():
    assert banner('OK') == '-----OK-----'


def prueba_2():
    assert resumen('Kiosco', 2, 1500) == 'Kiosco\nitems: 2\ntotal: 1500'


def linea_ticket(concepto, monto):
    """Devolvé `concepto` y el monto separados por dos puntos y un espacio. Ejemplo: linea_ticket('Cafe', 800) → 'Cafe: 800'"""
    raise NotImplementedError


def banner(titulo):
    """Devolvé el título centrado con guiones a cada lado, ancho total 12. Si el título es más corto, rellená con `-`. Ejemplo: banner('OK') empieza y termina con `-`"""
    raise NotImplementedError


def resumen(comercio, items, total):
    """Devolvé tres líneas unidas con salto de línea: comercio, cantidad de ítems y total. Ejemplo: resumen('Kiosco', 2, 1500)"""
    raise NotImplementedError


PRUEBAS = [
    ("linea_ticket", prueba_0),
    ("banner", prueba_1),
    ("resumen", prueba_2),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
