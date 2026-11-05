# Práctica extra — excepciones
# Enunciados, ejemplos y documentación: ejercicios.md (esta carpeta).
# Correr: ./r 13 practica_extra

import sys
from pathlib import Path

_lecciones = Path(__file__).resolve().parents[2]
if str(_lecciones) not in sys.path:
    sys.path.insert(0, str(_lecciones))
from menu_extra import abrir


def prueba_0():
    assert extraer_o_fallar(100, 40) == 60
    try:
        extraer_o_fallar(10, 40)
        raise AssertionError('tenía que fallar')
    except SaldoInsuficiente:
        pass


def prueba_1():
    assert mensaje_de(lambda: extraer_o_fallar(10, 40)) == 'sin_saldo' and mensaje_de(lambda: extraer_o_fallar(10, 0)) == 'monto_invalido'


class SaldoInsuficiente(Exception):
    pass


def extraer_o_fallar(saldo, monto):
    raise NotImplementedError


def mensaje_de(fn):
    """Si fn() termina bien, devolvé 'ok'. Si lanza SaldoInsuficiente, 'sin_saldo'. Si lanza ValueError, 'monto_invalido'. Ejemplo: mensaje_de(lambda: extraer_o_fallar(10, 40)) → 'sin_saldo'"""
    raise NotImplementedError


PRUEBAS = [
    ("extraer_o_fallar", prueba_0),
    ("mensaje_de", prueba_1),
]


if __name__ == "__main__":
    abrir(PRUEBAS, globals())
