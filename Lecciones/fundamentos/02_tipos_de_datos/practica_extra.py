# Práctica extra — tipos
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 02 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert clasificar(True) == 'logico' and clasificar(3) == 'entero' and clasificar(None) == 'vacio'


def prueba_1():
    assert es_monto(1500) and not es_monto(True) and not es_monto(1.5)


def prueba_2():
    assert contar_tipos([1, True, 'a']) == {'entero': 1, 'logico': 1, 'texto': 1}


def clasificar(valor):
    """Devolvé 'entero', 'decimal', 'texto', 'logico' o 'vacio' según el tipo. None es vacio. bool es logico, aunque herede de int. Ejemplo: clasificar(True) → 'logico'"""
    raise NotImplementedError


def es_monto(valor):
    """True solo si es int y no es bool. Un float no cuenta: la plata de estos ejercicios va en centavos enteros. Ejemplo: es_monto(1500) es True; es_monto(True) es False"""
    raise NotImplementedError


def contar_tipos(valores):
    """Devolvé un dict con la cantidad de cada clasificar() de la lista. Ejemplo: contar_tipos([1, True, 'a'])"""
    raise NotImplementedError


PRUEBAS = [
    ("clasificar", prueba_0),
    ("es_monto", prueba_1),
    ("contar_tipos", prueba_2),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
